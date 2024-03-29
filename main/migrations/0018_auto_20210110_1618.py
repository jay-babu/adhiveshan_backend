# Generated by Django 3.1.4 on 2021-01-10 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20210108_1352'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='has_watched_tutorial',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='center',
            field=models.CharField(choices=[('harrisburg', 'Harrisburg'), ('jersey_city', 'Jersey City'), ('roanoke', 'Roanoke'), ('westborough', 'Westborough'), ('robbinsville', 'Robbinsville'), ('hartford', 'Hartford'), ('clifton', 'Clifton'), ('lansdale', 'Lansdale'), ('albany_ny', 'Albany Ny'), ('washington_dc', 'Washington Dc'), ('long_island', 'Long Island'), ('springfield', 'Springfield'), ('philadelphia', 'Philadelphia'), ('westchester', 'Westchester'), ('delaware', 'Delaware'), ('warrington', 'Warrington'), ('edison', 'Edison'), ('scranton', 'Scranton'), ('boston', 'Boston'), ('parsippany', 'Parsippany'), ('syracuse', 'Syracuse'), ('south_boston', 'South Boston'), ('atlantic_city', 'Atlantic City'), ('downingtown', 'Downingtown'), ('new_york', 'New York'), ('richmond', 'Richmond'), ('allentown', 'Allentown'), ('new_haven', 'New Haven'), ('cherry_hill', 'Cherry Hill'), ('virginia_beach', 'Virginia Beach'), ('northern_virginia', 'Northern Virginia'), ('hilltop', 'Hilltop'), ('columbia_sc', 'Columbia Sc'), ('huntsville', 'Huntsville'), ('birmingham', 'Birmingham'), ('nashville', 'Nashville'), ('montgomery', 'Montgomery'), ('memphis', 'Memphis'), ('melbourne', 'Melbourne'), ('savannah', 'Savannah'), ('miami', 'Miami'), ('charlotte', 'Charlotte'), ('jacksonville', 'Jacksonville'), ('calhoun', 'Calhoun'), ('raleigh', 'Raleigh'), ('atlanta', 'Atlanta'), ('greensboro', 'Greensboro'), ('orangeburg', 'Orangeburg'), ('albany_ga', 'Albany Ga'), ('knoxville', 'Knoxville'), ('myrtle_beach', 'Myrtle Beach'), ('greenville', 'Greenville'), ('mobile', 'Mobile'), ('chattanooga', 'Chattanooga'), ('dothan', 'Dothan'), ('orlando', 'Orlando'), ('florence', 'Florence'), ('columbia_tn', 'Columbia Tn'), ('perry', 'Perry'), ('augusta', 'Augusta'), ('tampa', 'Tampa'), ('gainesville', 'Gainesville'), ('dallas', 'Dallas'), ('jackson', 'Jackson'), ('austin', 'Austin'), ('beaumont', 'Beaumont'), ('panama', 'Panama'), ('oklahoma_city', 'Oklahoma City'), ('clear_lake', 'Clear Lake'), ('houston', 'Houston'), ('lubbock', 'Lubbock'), ('midland', 'Midland'), ('new_orleans', 'New Orleans'), ('san_antonio', 'San Antonio'), ('denver', 'Denver'), ('corpus_christi', 'Corpus Christi'), ('little_rock', 'Little Rock'), ('sacramento', 'Sacramento'), ('salt_lake_city', 'Salt Lake City'), ('tucson', 'Tucson'), ('seattle', 'Seattle'), ('fresno', 'Fresno'), ('bakersfield', 'Bakersfield'), ('phoenix', 'Phoenix'), ('portland', 'Portland'), ('los_angeles', 'Los Angeles'), ('san_diego', 'San Diego'), ('san_francisco', 'San Francisco'), ('san_jose', 'San Jose'), ('evansville', 'Evansville'), ('cleveland', 'Cleveland'), ('munster', 'Munster'), ('des_moines', 'Des Moines'), ('columbus', 'Columbus'), ('cincinnati', 'Cincinnati'), ('chicago', 'Chicago'), ('minneapolis', 'Minneapolis'), ('kalamazoo', 'Kalamazoo'), ('lexington', 'Lexington'), ('detroit', 'Detroit'), ('iowa_city', 'Iowa City'), ('bloomington', 'Bloomington'), ('pittsburgh', 'Pittsburgh'), ('dayton', 'Dayton'), ('louisville', 'Louisville'), ('crystal_lake', 'Crystal Lake'), ('milwaukee', 'Milwaukee'), ('sterling_heights', 'Sterling Heights'), ('wichita', 'Wichita'), ('st_louis', 'St Louis'), ('indianapolis', 'Indianapolis'), ('kansas_city', 'Kansas City'), ('winnipeg', 'Winnipeg'), ('vancouver', 'Vancouver'), ('montreal', 'Montreal'), ('saskatoon', 'Saskatoon'), ('brandon', 'Brandon'), ('regina', 'Regina'), ('calgary', 'Calgary'), ('fort_mcmurray', 'Fort Mcmurray'), ('ottawa', 'Ottawa'), ('toronto', 'Toronto'), ('scarborough', 'Scarborough'), ('windsor', 'Windsor'), ('edmonton', 'Edmonton'), ('red_deer', 'Red Deer'), ('cambridge', 'Cambridge')], max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='mandal',
            field=models.CharField(choices=[('kishore/kishori', 'Kishore/Kishori'), ('group_3', 'Group 3'), ('group_1', 'Group 1'), ('group_0', 'Group 0'), ('group_2', 'Group 2')], max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='region',
            field=models.CharField(choices=[('southwest', 'Southwest'), ('midwest', 'Midwest'), ('southeast', 'Southeast'), ('canada', 'Canada'), ('northeast', 'Northeast'), ('west', 'West')], max_length=60, null=True),
        ),
    ]
