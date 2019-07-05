# Generated by Django 2.2.1 on 2019-07-05 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('completo', models.BooleanField()),
                ('salario', models.DecimalField(decimal_places=2, max_digits=5)),
                ('date_joined', models.DateField()),
            ],
            options={
                'db_table': 'profesores',
            },
        ),
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('matricula', models.CharField(max_length=6)),
                ('curp', models.CharField(max_length=15)),
                ('telefono', models.CharField(max_length=10, null=True)),
                ('date_joined', models.DateField()),
                ('profesores', models.ManyToManyField(blank=True, related_name='profesor_list', to='alumno.Profesor')),
            ],
            options={
                'db_table': 'alumnos',
            },
        ),
    ]