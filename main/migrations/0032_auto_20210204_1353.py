# Generated by Django 3.1.4 on 2021-02-04 18:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0031_auto_20210204_1332'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mukhpathitem',
            old_name='sanskrit_lipi_content',
            new_name='sanskrit_transliteration_content',
        ),
        migrations.AlterField(
            model_name='externalusermodel',
            name='code_expiration',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 5, 18, 53, 45, 110361, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='center',
            field=models.CharField(choices=[('richmond', 'Richmond'), ('parsippany', 'Parsippany'), ('hilltop', 'Hilltop'), ('syracuse', 'Syracuse'), ('scranton', 'Scranton'), ('washington_dc', 'Washington DC'), ('boston', 'Boston'), ('harrisburg', 'Harrisburg'), ('south_boston', 'South Boston'), ('clifton', 'Clifton'), ('roanoke', 'Roanoke'), ('albany_ny', 'Albany NY'), ('atlantic_city', 'Atlantic City'), ('delaware', 'Delaware'), ('allentown', 'Allentown'), ('philadelphia', 'Philadelphia'), ('westborough', 'Westborough'), ('warrington', 'Warrington'), ('long_island', 'Long Island'), ('westchester', 'Westchester'), ('cherry_hill', 'Cherry Hill'), ('springfield', 'Springfield'), ('lansdale', 'Lansdale'), ('new_york', 'New York'), ('virginia_beach', 'Virginia Beach'), ('edison', 'Edison'), ('jersey_city', 'Jersey City'), ('new_haven', 'New Haven'), ('downingtown', 'Downingtown'), ('hartford', 'Hartford'), ('robbinsville', 'Robbinsville'), ('northern_virginia', 'Northern Virginia'), ('orangeburg', 'Orangeburg'), ('birmingham', 'Birmingham'), ('chattanooga', 'Chattanooga'), ('melbourne', 'Melbourne'), ('gainesville', 'Gainesville'), ('raleigh', 'Raleigh'), ('greenville', 'Greenville'), ('orlando', 'Orlando'), ('memphis', 'Memphis'), ('charlotte', 'Charlotte'), ('nashville', 'Nashville'), ('perry', 'Perry'), ('montgomery', 'Montgomery'), ('miami', 'Miami'), ('myrtle_beach', 'Myrtle Beach'), ('calhoun', 'Calhoun'), ('tampa', 'Tampa'), ('albany_ga', 'Albany GA'), ('huntsville', 'Huntsville'), ('columbia_tn', 'Columbia TN'), ('atlanta', 'Atlanta'), ('mobile', 'Mobile'), ('savannah', 'Savannah'), ('florence', 'Florence'), ('dothan', 'Dothan'), ('columbia_sc', 'Columbia SC'), ('augusta', 'Augusta'), ('knoxville', 'Knoxville'), ('greensboro', 'Greensboro'), ('jacksonville', 'Jacksonville'), ('houston', 'Houston'), ('jackson', 'Jackson'), ('little_rock', 'Little Rock'), ('austin', 'Austin'), ('beaumont', 'Beaumont'), ('denver', 'Denver'), ('lubbock', 'Lubbock'), ('panama', 'Panama'), ('corpus_christi', 'Corpus Christi'), ('dallas', 'Dallas'), ('san_antonio', 'San Antonio'), ('new_orleans', 'New Orleans'), ('clear_lake', 'Clear Lake'), ('midland', 'Midland'), ('oklahoma_city', 'Oklahoma City'), ('los_angeles', 'Los Angeles'), ('san_jose', 'San Jose'), ('phoenix', 'Phoenix'), ('san_francisco', 'San Francisco'), ('tucson', 'Tucson'), ('bakersfield', 'Bakersfield'), ('san_diego', 'San Diego'), ('sacramento', 'Sacramento'), ('seattle', 'Seattle'), ('fresno', 'Fresno'), ('salt_lake_city', 'Salt Lake'), ('portland', 'Portland'), ('sterling_heights', 'Sterling Heights'), ('pittsburgh', 'Pittsburgh'), ('lexington', 'Lexington'), ('des_moines', 'Des Moines'), ('cleveland', 'Cleveland'), ('evansville', 'Evansville'), ('munster', 'Munster'), ('st_louis', 'St Louis'), ('crystal_lake', 'Crystal Lake'), ('indianapolis', 'Indianapolis'), ('dayton', 'Dayton'), ('milwaukee', 'Milwaukee'), ('cincinnati', 'Cincinnati'), ('kalamazoo', 'Kalamazoo'), ('iowa_city', 'Iowa City'), ('minneapolis', 'Minneapolis'), ('columbus', 'Columbus'), ('bloomington', 'Bloomington'), ('chicago', 'Chicago'), ('louisville', 'Louisville'), ('detroit', 'Detroit'), ('wichita', 'Wichita'), ('kansas_city', 'Kansas City'), ('vancouver', 'Vancouver'), ('brandon', 'Brandon'), ('ottawa', 'Ottawa'), ('calgary', 'Calgary'), ('saskatoon', 'Saskatoon'), ('edmonton', 'Edmonton'), ('red_deer', 'Red Deer'), ('montreal', 'Montreal'), ('scarborough', 'Scarborough'), ('fort_mcmurray', 'Fort Mcmurray'), ('winnipeg', 'Winnipeg'), ('windsor', 'Windsor'), ('regina', 'Regina'), ('toronto', 'Toronto'), ('cambridge', 'Cambridge')], max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('female', 'Female'), ('male', 'Male')], max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='mandal',
            field=models.CharField(choices=[('group_0', 'Group 0'), ('group_3', 'Group 3'), ('group_1', 'Group 1'), ('group_2', 'Group 2'), ('kishore/kishori', 'Kishore/Kishori')], max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='region',
            field=models.CharField(choices=[('midwest', 'Midwest'), ('southwest', 'Southwest'), ('west', 'West'), ('canada', 'Canada'), ('southeast', 'Southeast'), ('northeast', 'Northeast')], max_length=60, null=True),
        ),
    ]
