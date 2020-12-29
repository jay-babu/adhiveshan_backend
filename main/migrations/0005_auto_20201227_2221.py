# Generated by Django 3.1.4 on 2020-12-28 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20201227_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='center',
            field=models.CharField(choices=[('boston', 'Boston'), ('cherry_hill', 'Cherry Hill'), ('robbinsville', 'Robbinsville'), ('edison', 'Edison'), ('philadelphia', 'Philadelphia'), ('atlanta', 'Atlanta'), ('houston', 'Houston'), ('chino_hills', 'Chino Hills'), ('chicago', 'Chicago'), ('toronto', 'Toronto')], max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='mandal',
            field=models.CharField(choices=[('group_0', 'Group 0'), ('group_1', 'Group 1'), ('group_2', 'Group 2'), ('kishore/kishori', 'Kishore/Kishori'), ('group_3', 'Group 3')], max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='region',
            field=models.CharField(choices=[('northeast', 'Northeast'), ('southwest', 'Southwest'), ('canada', 'Canada'), ('west', 'West'), ('southeast', 'Southeast'), ('midwest', 'Midwest')], max_length=60, null=True),
        ),
    ]