# Generated by Django 3.1.4 on 2020-12-23 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20201223_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='center',
            field=models.CharField(choices=[('edison', 'Edison'), ('robbinsville', 'Robbinsville'), ('philadelphia', 'Philadelphia'), ('cherry_hill', 'Cherry Hill'), ('atlanta', 'Atlanta'), ('houston', 'Houston'), ('chino_hills', 'Chino Hills'), ('chicago', 'Chicago'), ('toronto', 'Toronto')], max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='mandal',
            field=models.CharField(choices=[('kishore/kishori', 'Kishore/Kishori'), ('group_2', 'Group 2'), ('group_1', 'Group 1'), ('group_0', 'Group 0'), ('group_3', 'Group 3')], max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='region',
            field=models.CharField(choices=[('west', 'West'), ('southeast', 'Southeast'), ('southwest', 'Southwest'), ('midwest', 'Midwest'), ('northeast', 'Northeast'), ('canada', 'Canada')], max_length=60, null=True),
        ),
    ]
