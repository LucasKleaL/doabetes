# Generated by Django 2.2.12 on 2020-06-15 19:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doabetesite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='MarcaProduto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doabetesite.Marca')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doabetesite.Produto')),
            ],
        ),
    ]
