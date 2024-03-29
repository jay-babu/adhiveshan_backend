# Generated by Django 3.1.4 on 2021-01-16 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_auto_20210115_2321'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='index',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='user',
            name='center',
            field=models.CharField(choices=[('parsippany', 'Parsippany'), ('lansdale', 'Lansdale'), ('edison', 'Edison'), ('south_boston', 'South Boston'), ('westchester', 'Westchester'), ('washington_dc', 'Washington Dc'), ('harrisburg', 'Harrisburg'), ('virginia_beach', 'Virginia Beach'), ('clifton', 'Clifton'), ('richmond', 'Richmond'), ('delaware', 'Delaware'), ('atlantic_city', 'Atlantic City'), ('boston', 'Boston'), ('robbinsville', 'Robbinsville'), ('philadelphia', 'Philadelphia'), ('new_york', 'New York'), ('downingtown', 'Downingtown'), ('cherry_hill', 'Cherry Hill'), ('hartford', 'Hartford'), ('syracuse', 'Syracuse'), ('scranton', 'Scranton'), ('springfield', 'Springfield'), ('hilltop', 'Hilltop'), ('jersey_city', 'Jersey City'), ('allentown', 'Allentown'), ('northern_virginia', 'Northern Virginia'), ('westborough', 'Westborough'), ('albany_ny', 'Albany Ny'), ('warrington', 'Warrington'), ('roanoke', 'Roanoke'), ('new_haven', 'New Haven'), ('long_island', 'Long Island'), ('greenville', 'Greenville'), ('columbia_sc', 'Columbia Sc'), ('orlando', 'Orlando'), ('montgomery', 'Montgomery'), ('perry', 'Perry'), ('calhoun', 'Calhoun'), ('albany_ga', 'Albany Ga'), ('raleigh', 'Raleigh'), ('jacksonville', 'Jacksonville'), ('savannah', 'Savannah'), ('gainesville', 'Gainesville'), ('charlotte', 'Charlotte'), ('mobile', 'Mobile'), ('nashville', 'Nashville'), ('myrtle_beach', 'Myrtle Beach'), ('atlanta', 'Atlanta'), ('memphis', 'Memphis'), ('greensboro', 'Greensboro'), ('augusta', 'Augusta'), ('florence', 'Florence'), ('miami', 'Miami'), ('orangeburg', 'Orangeburg'), ('melbourne', 'Melbourne'), ('tampa', 'Tampa'), ('chattanooga', 'Chattanooga'), ('columbia_tn', 'Columbia Tn'), ('knoxville', 'Knoxville'), ('huntsville', 'Huntsville'), ('birmingham', 'Birmingham'), ('dothan', 'Dothan'), ('new_orleans', 'New Orleans'), ('panama', 'Panama'), ('beaumont', 'Beaumont'), ('clear_lake', 'Clear Lake'), ('little_rock', 'Little Rock'), ('oklahoma_city', 'Oklahoma City'), ('jackson', 'Jackson'), ('denver', 'Denver'), ('lubbock', 'Lubbock'), ('corpus_christi', 'Corpus Christi'), ('dallas', 'Dallas'), ('san_antonio', 'San Antonio'), ('houston', 'Houston'), ('austin', 'Austin'), ('midland', 'Midland'), ('san_jose', 'San Jose'), ('san_francisco', 'San Francisco'), ('portland', 'Portland'), ('sacramento', 'Sacramento'), ('phoenix', 'Phoenix'), ('los_angeles', 'Los Angeles'), ('seattle', 'Seattle'), ('tucson', 'Tucson'), ('bakersfield', 'Bakersfield'), ('salt_lake_city', 'Salt Lake City'), ('fresno', 'Fresno'), ('san_diego', 'San Diego'), ('iowa_city', 'Iowa City'), ('st_louis', 'St Louis'), ('bloomington', 'Bloomington'), ('wichita', 'Wichita'), ('chicago', 'Chicago'), ('columbus', 'Columbus'), ('sterling_heights', 'Sterling Heights'), ('indianapolis', 'Indianapolis'), ('kansas_city', 'Kansas City'), ('pittsburgh', 'Pittsburgh'), ('cincinnati', 'Cincinnati'), ('lexington', 'Lexington'), ('louisville', 'Louisville'), ('kalamazoo', 'Kalamazoo'), ('minneapolis', 'Minneapolis'), ('detroit', 'Detroit'), ('dayton', 'Dayton'), ('des_moines', 'Des Moines'), ('milwaukee', 'Milwaukee'), ('crystal_lake', 'Crystal Lake'), ('munster', 'Munster'), ('cleveland', 'Cleveland'), ('evansville', 'Evansville'), ('ottawa', 'Ottawa'), ('toronto', 'Toronto'), ('brandon', 'Brandon'), ('calgary', 'Calgary'), ('fort_mcmurray', 'Fort Mcmurray'), ('montreal', 'Montreal'), ('saskatoon', 'Saskatoon'), ('vancouver', 'Vancouver'), ('edmonton', 'Edmonton'), ('cambridge', 'Cambridge'), ('scarborough', 'Scarborough'), ('regina', 'Regina'), ('winnipeg', 'Winnipeg'), ('red_deer', 'Red Deer'), ('windsor', 'Windsor')], max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='mandal',
            field=models.CharField(choices=[('group_0', 'Group 0'), ('kishore/kishori', 'Kishore/Kishori'), ('group_2', 'Group 2'), ('group_3', 'Group 3'), ('group_1', 'Group 1')], max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='region',
            field=models.CharField(choices=[('midwest', 'Midwest'), ('canada', 'Canada'), ('southeast', 'Southeast'), ('southwest', 'Southwest'), ('northeast', 'Northeast'), ('west', 'West')], max_length=60, null=True),
        ),
    ]
