from django.test import TestCase, Client

from ..models import Tournament

from is_valid import (
    is_decodable_json_where, is_str, is_list_of, is_dict_union, is_int, is_in,
)
from is_valid.test import assert_valid


class TestTournament(TestCase):

    def setUp(self):
        self.client = Client()

    def test_create_tournament(self):
        res = self.client.post(
            '/api/tournament/',
            {
                'name': 'Tournament',
                'players': [
                    {'name': f'Player {n}'}
                    for n in range(1, 9)
                ],
            },
            content_type='application/json',
        )

        self.assertEqual(res.status_code, 200)
        assert_valid(res.content, is_decodable_json_where({
            'name': 'Tournament',
            'token': is_str,
            'admin_token': is_str,
            'players': is_list_of({
                'id': is_int,
                'name': is_str,
            }),
            'games': is_list_of({
                'name': is_str,
                'players': is_list_of(is_dict_union(
                    player={
                        'player': is_int,
                    },
                    slot={
                        'game': is_str,
                        'position': is_in({1, 2, 3, 4}),
                        'player': None,
                    },
                )),
            }),
            'ranks': is_list_of({
                'rank': is_in({1, 2, 3, 4, 5, 6, 7, 8}),
                'game': is_str,
                'position': is_in({1, 2, 3, 4}),
                'player': None,
            }),
        }))
