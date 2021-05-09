# Generated by Django 2.2 on 2021-05-03 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Liquidacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documento', models.CharField(max_length=8)),
                ('nombre', models.CharField(max_length=145)),
                ('fecha_liquidacion', models.DateField()),
                ('programa_id', models.PositiveIntegerField()),
                ('jerarquia_id', models.PositiveIntegerField()),
                ('agrupacion_id', models.PositiveIntegerField()),
                ('codigo', models.PositiveIntegerField()),
                ('monto', models.FloatField()),
                ('tipo', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'liquidacion',
                'managed': False,
            },
        ),
    ]
