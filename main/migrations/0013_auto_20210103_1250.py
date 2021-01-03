# Generated by Django 3.1.4 on 2021-01-03 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20210102_2313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='center',
            field=models.CharField(choices=[('long_island', 'Long Island'), ('virginia_beach', 'Virginia Beach'), ('westborough', 'Westborough'), ('new_haven', 'New Haven'), ('downingtown', 'Downingtown'), ('south_boston', 'South Boston'), ('jersey_city', 'Jersey City'), ('warrington', 'Warrington'), ('parsippany', 'Parsippany'), ('clifton', 'Clifton'), ('boston', 'Boston'), ('atlantic_city', 'Atlantic City'), ('edison', 'Edison'), ('westchester', 'Westchester'), ('philadelphia', 'Philadelphia'), ('richmond', 'Richmond'), ('new_york', 'New York'), ('cherry_hill', 'Cherry Hill'), ('syracuse', 'Syracuse'), ('delaware', 'Delaware'), ('hartford', 'Hartford'), ('springfield', 'Springfield'), ('scranton', 'Scranton'), ('harrisburg', 'Harrisburg'), ('washington_dc', 'Washington Dc'), ('northern_virginia', 'Northern Virginia'), ('hilltop', 'Hilltop'), ('roanoke', 'Roanoke'), ('allentown', 'Allentown'), ('albany_ny', 'Albany Ny'), ('robbinsville', 'Robbinsville'), ('lansdale', 'Lansdale'), ('columbia_sc', 'Columbia Sc'), ('tampa', 'Tampa'), ('greensboro', 'Greensboro'), ('montgomery', 'Montgomery'), ('birmingham', 'Birmingham'), ('memphis', 'Memphis'), ('albany_ga', 'Albany Ga'), ('jacksonville', 'Jacksonville'), ('charlotte', 'Charlotte'), ('greenville', 'Greenville'), ('miami', 'Miami'), ('florence', 'Florence'), ('columbia_tn', 'Columbia Tn'), ('perry', 'Perry'), ('dothan', 'Dothan'), ('huntsville', 'Huntsville'), ('augusta', 'Augusta'), ('gainesville', 'Gainesville'), ('mobile', 'Mobile'), ('savannah', 'Savannah'), ('atlanta', 'Atlanta'), ('chattanooga', 'Chattanooga'), ('knoxville', 'Knoxville'), ('melbourne', 'Melbourne'), ('nashville', 'Nashville'), ('calhoun', 'Calhoun'), ('orangeburg', 'Orangeburg'), ('orlando', 'Orlando'), ('raleigh', 'Raleigh'), ('myrtle_beach', 'Myrtle Beach'), ('clear_lake', 'Clear Lake'), ('san_antonio', 'San Antonio'), ('austin', 'Austin'), ('lubbock', 'Lubbock'), ('oklahoma_city', 'Oklahoma City'), ('jackson', 'Jackson'), ('denver', 'Denver'), ('midland', 'Midland'), ('beaumont', 'Beaumont'), ('little_rock', 'Little Rock'), ('panama', 'Panama'), ('corpus_christi', 'Corpus Christi'), ('dallas', 'Dallas'), ('new_orleans', 'New Orleans'), ('houston', 'Houston'), ('san_jose', 'San Jose'), ('los_angeles', 'Los Angeles'), ('salt_lake_city', 'Salt Lake City'), ('phoenix', 'Phoenix'), ('san_diego', 'San Diego'), ('tucson', 'Tucson'), ('portland', 'Portland'), ('bakersfield', 'Bakersfield'), ('san_francisco', 'San Francisco'), ('fresno', 'Fresno'), ('sacramento', 'Sacramento'), ('seattle', 'Seattle'), ('kalamazoo', 'Kalamazoo'), ('st_louis', 'St Louis'), ('minneapolis', 'Minneapolis'), ('cincinnati', 'Cincinnati'), ('kansas_city', 'Kansas City'), ('bloomington', 'Bloomington'), ('dayton', 'Dayton'), ('sterling_heights', 'Sterling Heights'), ('indianapolis', 'Indianapolis'), ('wichita', 'Wichita'), ('chicago', 'Chicago'), ('des_moines', 'Des Moines'), ('cleveland', 'Cleveland'), ('crystal_lake', 'Crystal Lake'), ('iowa_city', 'Iowa City'), ('evansville', 'Evansville'), ('lexington', 'Lexington'), ('munster', 'Munster'), ('detroit', 'Detroit'), ('louisville', 'Louisville'), ('milwaukee', 'Milwaukee'), ('pittsburgh', 'Pittsburgh'), ('columbus', 'Columbus'), ('calgary', 'Calgary'), ('toronto', 'Toronto'), ('windsor', 'Windsor'), ('winnipeg', 'Winnipeg'), ('ottawa', 'Ottawa'), ('regina', 'Regina'), ('red_deer', 'Red Deer'), ('fort_mcmurray', 'Fort Mcmurray'), ('cambridge', 'Cambridge'), ('vancouver', 'Vancouver'), ('scarborough', 'Scarborough'), ('montreal', 'Montreal'), ('brandon', 'Brandon'), ('saskatoon', 'Saskatoon'), ('edmonton', 'Edmonton')], max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='mandal',
            field=models.CharField(choices=[('kishore/kishori', 'Kishore/Kishori'), ('group_2', 'Group 2'), ('group_1', 'Group 1'), ('group_3', 'Group 3'), ('group_0', 'Group 0')], max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='region',
            field=models.CharField(choices=[('southwest', 'Southwest'), ('southeast', 'Southeast'), ('west', 'West'), ('canada', 'Canada'), ('northeast', 'Northeast'), ('midwest', 'Midwest')], max_length=60, null=True),
        ),
    ]
