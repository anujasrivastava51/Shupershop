# Generated by Django 4.2.2 on 2023-09-11 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0011_contact_newslatter'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('message', models.TextField()),
                ('pic', models.ImageField(upload_to='uploads/testimonials')),
            ],
        ),
    ]
