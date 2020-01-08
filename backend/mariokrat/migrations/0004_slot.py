# Generated by Django 3.0 on 2020-01-07 20:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mariokrat', '0003_game'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField(blank=True, null=True)),
                ('rank', models.IntegerField(blank=True, null=True)),
                ('player', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='mariokrat.Player')),
                ('source', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='players_out', to='mariokrat.Game')),
                ('target', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='players_in', to='mariokrat.Game')),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='slots', to='mariokrat.Tournament')),
            ],
        ),
    ]