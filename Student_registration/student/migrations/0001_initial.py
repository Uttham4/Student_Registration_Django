# Generated by Django 4.2.5 on 2023-09-25 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='stud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_class', models.CharField(max_length=30)),
                ('s_school', models.CharField(max_length=30)),
                ('s_addr', models.CharField(max_length=30)),
                ('s_name', models.CharField(max_length=30)),
                ('s_email', models.EmailField(max_length=30)),
            ],
        ),
    ]
