# Generated by Django 3.1.4 on 2021-01-17 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0027_auto_20210116_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='center',
            field=models.CharField(choices=[('harrisburg', 'Harrisburg'), ('long_island', 'Long Island'), ('warrington', 'Warrington'), ('new_york', 'New York'), ('springfield', 'Springfield'), ('virginia_beach', 'Virginia Beach'), ('roanoke', 'Roanoke'), ('boston', 'Boston'), ('edison', 'Edison'), ('jersey_city', 'Jersey City'), ('washington_dc', 'Washington DC'), ('lansdale', 'Lansdale'), ('clifton', 'Clifton'), ('albany_ny', 'Albany NY'), ('hilltop', 'Hilltop'), ('scranton', 'Scranton'), ('hartford', 'Hartford'), ('richmond', 'Richmond'), ('atlantic_city', 'Atlantic City'), ('downingtown', 'Downingtown'), ('robbinsville', 'Robbinsville'), ('new_haven', 'New Haven'), ('syracuse', 'Syracuse'), ('northern_virginia', 'Northern Virginia'), ('allentown', 'Allentown'), ('philadelphia', 'Philadelphia'), ('cherry_hill', 'Cherry Hill'), ('parsippany', 'Parsippany'), ('delaware', 'Delaware'), ('south_boston', 'South Boston'), ('westborough', 'Westborough'), ('westchester', 'Westchester'), ('raleigh', 'Raleigh'), ('augusta', 'Augusta'), ('birmingham', 'Birmingham'), ('gainesville', 'Gainesville'), ('calhoun', 'Calhoun'), ('mobile', 'Mobile'), ('nashville', 'Nashville'), ('greensboro', 'Greensboro'), ('atlanta', 'Atlanta'), ('perry', 'Perry'), ('greenville', 'Greenville'), ('florence', 'Florence'), ('tampa', 'Tampa'), ('orangeburg', 'Orangeburg'), ('columbia_sc', 'Columbia SC'), ('melbourne', 'Melbourne'), ('myrtle_beach', 'Myrtle Beach'), ('huntsville', 'Huntsville'), ('savannah', 'Savannah'), ('columbia_tn', 'Columbia TN'), ('albany_ga', 'Albany GA'), ('memphis', 'Memphis'), ('dothan', 'Dothan'), ('miami', 'Miami'), ('knoxville', 'Knoxville'), ('chattanooga', 'Chattanooga'), ('jacksonville', 'Jacksonville'), ('orlando', 'Orlando'), ('charlotte', 'Charlotte'), ('montgomery', 'Montgomery'), ('corpus_christi', 'Corpus Christi'), ('beaumont', 'Beaumont'), ('denver', 'Denver'), ('lubbock', 'Lubbock'), ('midland', 'Midland'), ('new_orleans', 'New Orleans'), ('san_antonio', 'San Antonio'), ('clear_lake', 'Clear Lake'), ('houston', 'Houston'), ('austin', 'Austin'), ('panama', 'Panama'), ('oklahoma_city', 'Oklahoma City'), ('little_rock', 'Little Rock'), ('dallas', 'Dallas'), ('jackson', 'Jackson'), ('seattle', 'Seattle'), ('phoenix', 'Phoenix'), ('sacramento', 'Sacramento'), ('bakersfield', 'Bakersfield'), ('los_angeles', 'Los Angeles'), ('san_diego', 'San Diego'), ('fresno', 'Fresno'), ('salt_lake_city', 'Salt Lake'), ('portland', 'Portland'), ('san_jose', 'San Jose'), ('tucson', 'Tucson'), ('san_francisco', 'San Francisco'), ('bloomington', 'Bloomington'), ('detroit', 'Detroit'), ('iowa_city', 'Iowa City'), ('cleveland', 'Cleveland'), ('louisville', 'Louisville'), ('munster', 'Munster'), ('st_louis', 'St Louis'), ('dayton', 'Dayton'), ('evansville', 'Evansville'), ('minneapolis', 'Minneapolis'), ('pittsburgh', 'Pittsburgh'), ('sterling_heights', 'Sterling Heights'), ('kalamazoo', 'Kalamazoo'), ('lexington', 'Lexington'), ('cincinnati', 'Cincinnati'), ('crystal_lake', 'Crystal Lake'), ('milwaukee', 'Milwaukee'), ('wichita', 'Wichita'), ('kansas_city', 'Kansas City'), ('des_moines', 'Des Moines'), ('columbus', 'Columbus'), ('chicago', 'Chicago'), ('indianapolis', 'Indianapolis'), ('edmonton', 'Edmonton'), ('windsor', 'Windsor'), ('saskatoon', 'Saskatoon'), ('calgary', 'Calgary'), ('fort_mcmurray', 'Fort Mcmurray'), ('regina', 'Regina'), ('scarborough', 'Scarborough'), ('winnipeg', 'Winnipeg'), ('brandon', 'Brandon'), ('ottawa', 'Ottawa'), ('montreal', 'Montreal'), ('vancouver', 'Vancouver'), ('cambridge', 'Cambridge'), ('red_deer', 'Red Deer'), ('toronto', 'Toronto')], max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='mandal',
            field=models.CharField(choices=[('group_0', 'Group 0'), ('group_3', 'Group 3'), ('group_2', 'Group 2'), ('group_1', 'Group 1'), ('kishore/kishori', 'Kishore/Kishori')], max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='region',
            field=models.CharField(choices=[('southwest', 'Southwest'), ('west', 'West'), ('midwest', 'Midwest'), ('canada', 'Canada'), ('northeast', 'Northeast'), ('southeast', 'Southeast')], max_length=60, null=True),
        ),
    ]
