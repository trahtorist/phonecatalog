# Generated by Django 4.1.1 on 2022-09-15 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Puesc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taxid', models.CharField(max_length=255)),
                ('puesc_answer', models.TextField(blank=True)),
            ],
        ),
    ]
