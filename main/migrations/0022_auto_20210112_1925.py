# Generated by Django 3.1.4 on 2021-01-13 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_auto_20210110_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mukhpathitem',
            name='english_content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='center',
            field=models.CharField(choices=[('cherry_hill', 'Cherry Hill'), ('philadelphia', 'Philadelphia'), ('westborough', 'Westborough'), ('robbinsville', 'Robbinsville'), ('springfield', 'Springfield'), ('jersey_city', 'Jersey City'), ('delaware', 'Delaware'), ('warrington', 'Warrington'), ('new_york', 'New York'), ('south_boston', 'South Boston'), ('roanoke', 'Roanoke'), ('harrisburg', 'Harrisburg'), ('syracuse', 'Syracuse'), ('clifton', 'Clifton'), ('albany_ny', 'Albany Ny'), ('downingtown', 'Downingtown'), ('northern_virginia', 'Northern Virginia'), ('virginia_beach', 'Virginia Beach'), ('washington_dc', 'Washington Dc'), ('long_island', 'Long Island'), ('parsippany', 'Parsippany'), ('westchester', 'Westchester'), ('allentown', 'Allentown'), ('lansdale', 'Lansdale'), ('atlantic_city', 'Atlantic City'), ('hilltop', 'Hilltop'), ('scranton', 'Scranton'), ('hartford', 'Hartford'), ('richmond', 'Richmond'), ('edison', 'Edison'), ('new_haven', 'New Haven'), ('boston', 'Boston'), ('chattanooga', 'Chattanooga'), ('birmingham', 'Birmingham'), ('memphis', 'Memphis'), ('dothan', 'Dothan'), ('huntsville', 'Huntsville'), ('savannah', 'Savannah'), ('orlando', 'Orlando'), ('columbia_tn', 'Columbia Tn'), ('myrtle_beach', 'Myrtle Beach'), ('mobile', 'Mobile'), ('florence', 'Florence'), ('nashville', 'Nashville'), ('miami', 'Miami'), ('perry', 'Perry'), ('knoxville', 'Knoxville'), ('calhoun', 'Calhoun'), ('raleigh', 'Raleigh'), ('augusta', 'Augusta'), ('tampa', 'Tampa'), ('melbourne', 'Melbourne'), ('montgomery', 'Montgomery'), ('orangeburg', 'Orangeburg'), ('atlanta', 'Atlanta'), ('columbia_sc', 'Columbia Sc'), ('jacksonville', 'Jacksonville'), ('greensboro', 'Greensboro'), ('gainesville', 'Gainesville'), ('greenville', 'Greenville'), ('albany_ga', 'Albany Ga'), ('charlotte', 'Charlotte'), ('panama', 'Panama'), ('houston', 'Houston'), ('corpus_christi', 'Corpus Christi'), ('little_rock', 'Little Rock'), ('dallas', 'Dallas'), ('lubbock', 'Lubbock'), ('oklahoma_city', 'Oklahoma City'), ('austin', 'Austin'), ('denver', 'Denver'), ('clear_lake', 'Clear Lake'), ('new_orleans', 'New Orleans'), ('san_antonio', 'San Antonio'), ('beaumont', 'Beaumont'), ('midland', 'Midland'), ('jackson', 'Jackson'), ('los_angeles', 'Los Angeles'), ('san_jose', 'San Jose'), ('salt_lake_city', 'Salt Lake City'), ('fresno', 'Fresno'), ('phoenix', 'Phoenix'), ('portland', 'Portland'), ('san_diego', 'San Diego'), ('tucson', 'Tucson'), ('san_francisco', 'San Francisco'), ('bakersfield', 'Bakersfield'), ('seattle', 'Seattle'), ('sacramento', 'Sacramento'), ('wichita', 'Wichita'), ('chicago', 'Chicago'), ('columbus', 'Columbus'), ('cleveland', 'Cleveland'), ('indianapolis', 'Indianapolis'), ('bloomington', 'Bloomington'), ('evansville', 'Evansville'), ('detroit', 'Detroit'), ('munster', 'Munster'), ('lexington', 'Lexington'), ('kalamazoo', 'Kalamazoo'), ('des_moines', 'Des Moines'), ('dayton', 'Dayton'), ('louisville', 'Louisville'), ('cincinnati', 'Cincinnati'), ('minneapolis', 'Minneapolis'), ('st_louis', 'St Louis'), ('kansas_city', 'Kansas City'), ('sterling_heights', 'Sterling Heights'), ('iowa_city', 'Iowa City'), ('pittsburgh', 'Pittsburgh'), ('milwaukee', 'Milwaukee'), ('crystal_lake', 'Crystal Lake'), ('fort_mcmurray', 'Fort Mcmurray'), ('red_deer', 'Red Deer'), ('toronto', 'Toronto'), ('windsor', 'Windsor'), ('edmonton', 'Edmonton'), ('winnipeg', 'Winnipeg'), ('brandon', 'Brandon'), ('saskatoon', 'Saskatoon'), ('vancouver', 'Vancouver'), ('scarborough', 'Scarborough'), ('ottawa', 'Ottawa'), ('montreal', 'Montreal'), ('regina', 'Regina'), ('cambridge', 'Cambridge'), ('calgary', 'Calgary')], max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='mandal',
            field=models.CharField(choices=[('group_0', 'Group 0'), ('group_2', 'Group 2'), ('kishore/kishori', 'Kishore/Kishori'), ('group_3', 'Group 3'), ('group_1', 'Group 1')], max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='region',
            field=models.CharField(choices=[('southeast', 'Southeast'), ('west', 'West'), ('canada', 'Canada'), ('southwest', 'Southwest'), ('midwest', 'Midwest'), ('northeast', 'Northeast')], max_length=60, null=True),
        ),
    ]
