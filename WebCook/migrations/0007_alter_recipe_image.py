# Generated by Django 4.2 on 2024-04-03 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebCook', '0006_alter_recipe_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(upload_to='recipes'),
        ),
    ]
