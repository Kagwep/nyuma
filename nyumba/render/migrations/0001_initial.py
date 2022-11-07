# Generated by Django 4.1.1 on 2022-11-07 20:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catname', models.CharField(choices=[('Rent', 'Rent'), ('Buy', 'Buy')], max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Houses', 'Houses'), ('Apartments', 'Apartments'), ('Commercial Property', 'Commercial Property'), ('3-Bedroom', '3-Bedroom'), ('2-Bedroom', '2-Bedroom'), ('1-Bedroom', '1-Bedroom'), ('Bedsitter', 'Bedsitter')], max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategoriesCars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('SUV.', 'SUV'), ('Hatchback', 'Hatchback'), ('Crossover', 'Crossover'), ('Sedan', 'Sedan'), ('Sports Car', 'Sports Car'), ('Coupe', 'Coupe'), ('Minivan', 'Minivan')], max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='images/%y')),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='render.category')),
                ('sub_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='render.subcategories')),
            ],
        ),
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='images/%y')),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='render.category')),
                ('sub_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='render.subcategoriescars')),
            ],
        ),
    ]
