# Generated by Django 3.2.2 on 2021-05-10 08:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ServerProject', '0001_initial'),
        ('Accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Audit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('price', models.DecimalField(decimal_places=5, max_digits=5)),
                ('what_project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ServerProject.serverproject')),
                ('who_customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Accounts.customer')),
                ('who_provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Accounts.provider')),
            ],
        ),
    ]
