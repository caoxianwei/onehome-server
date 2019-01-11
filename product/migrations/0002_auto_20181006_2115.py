# Generated by Django 2.1.2 on 2018-10-06 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='price',
            new_name='goods_price',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='username',
            new_name='user_name',
        ),
        migrations.AddField(
            model_name='product',
            name='user_image_URL',
            field=models.ImageField(default='', upload_to='static/ProductUserImages/%Y/%m/%d'),
            preserve_default=False,
        ),
    ]