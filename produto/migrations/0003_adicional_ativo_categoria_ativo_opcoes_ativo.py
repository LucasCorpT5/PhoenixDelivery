# Generated by Django 4.0.6 on 2022-07-16 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0002_adicional_categoria_opcoes_produto_delete_teste_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='adicional',
            name='ativo',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='categoria',
            name='ativo',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='opcoes',
            name='ativo',
            field=models.BooleanField(default=True),
        ),
    ]
