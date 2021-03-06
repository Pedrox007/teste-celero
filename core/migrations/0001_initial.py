# Generated by Django 4.0.3 on 2022-03-25 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Athlete',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('height', models.IntegerField(blank=True, null=True)),
                ('weight', models.IntegerField(blank=True, null=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('season', models.CharField(choices=[('W', 'Winter'), ('S', 'Summer')], max_length=1)),
                ('city', models.CharField(max_length=255)),
            ],
            options={
                'unique_together': {('year', 'season')},
            },
        ),
        migrations.CreateModel(
            name='Modality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('noc', models.CharField(max_length=3)),
            ],
            options={
                'unique_together': {('name', 'noc')},
            },
        ),
        migrations.CreateModel(
            name='Participation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medal', models.CharField(blank=True, choices=[('G', 'Gold'), ('S', 'Silver'), ('B', 'Bronze')], max_length=1, null=True)),
                ('athlete', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.athlete')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.game')),
                ('modality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.modality')),
            ],
        ),
        migrations.AddField(
            model_name='modality',
            name='sport',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.sport'),
        ),
        migrations.AddField(
            model_name='athlete',
            name='game',
            field=models.ManyToManyField(through='core.Participation', to='core.game'),
        ),
        migrations.AddField(
            model_name='athlete',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.team'),
        ),
    ]
