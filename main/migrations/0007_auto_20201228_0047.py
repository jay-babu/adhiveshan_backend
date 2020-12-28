# Generated by Django 3.1.4 on 2020-12-28 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20201227_2255'),
    ]

    operations = [
        migrations.AddField(
            model_name='mukhpathitem',
            name='type',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='mukhpathitem',
            name='english_content',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='mukhpathitem',
            name='gujurati_content',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='mukhpathitem',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='mukhpathitem',
            name='transliteration_content',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='user',
            name='center',
            field=models.CharField(choices=[('robbinsville', 'Robbinsville'), ('edison', 'Edison'), ('boston', 'Boston'), ('philadelphia', 'Philadelphia'), ('cherry_hill', 'Cherry Hill'), ('atlanta', 'Atlanta'), ('houston', 'Houston'), ('chino_hills', 'Chino Hills'), ('chicago', 'Chicago'), ('toronto', 'Toronto')], max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='mandal',
            field=models.CharField(choices=[('group_1', 'Group 1'), ('group_3', 'Group 3'), ('group_0', 'Group 0'), ('kishore/kishori', 'Kishore/Kishori'), ('group_2', 'Group 2')], max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='region',
            field=models.CharField(choices=[('canada', 'Canada'), ('southwest', 'Southwest'), ('northeast', 'Northeast'), ('midwest', 'Midwest'), ('southeast', 'Southeast'), ('west', 'West')], max_length=60, null=True),
        ),
    ]
