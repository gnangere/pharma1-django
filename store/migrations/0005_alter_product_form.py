# Generated by Django 4.1 on 2023-03-11 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_product_form'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='form',
            field=models.CharField(choices=[('FL', 'FLACON'), ('BT', 'BOITE'), ('TB', 'TUBE'), ('CT', 'CARTON')], default='BOITE', max_length=20),
        ),
    ]