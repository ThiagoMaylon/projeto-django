# Generated by Django 4.2.7 on 2023-11-29 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome do Produto')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Preço do Produto')),
            ],
        ),
    ]
