# Generated by Django 3.1.4 on 2021-01-10 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_auto_20210110_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='center',
            field=models.CharField(choices=[('edison', 'Edison'), ('northern_virginia', 'Northern Virginia'), ('roanoke', 'Roanoke'), ('robbinsville', 'Robbinsville'), ('harrisburg', 'Harrisburg'), ('albany_ny', 'Albany Ny'), ('westchester', 'Westchester'), ('scranton', 'Scranton'), ('philadelphia', 'Philadelphia'), ('westborough', 'Westborough'), ('cherry_hill', 'Cherry Hill'), ('richmond', 'Richmond'), ('springfield', 'Springfield'), ('jersey_city', 'Jersey City'), ('hilltop', 'Hilltop'), ('boston', 'Boston'), ('parsippany', 'Parsippany'), ('downingtown', 'Downingtown'), ('lansdale', 'Lansdale'), ('syracuse', 'Syracuse'), ('new_york', 'New York'), ('virginia_beach', 'Virginia Beach'), ('hartford', 'Hartford'), ('delaware', 'Delaware'), ('allentown', 'Allentown'), ('long_island', 'Long Island'), ('new_haven', 'New Haven'), ('warrington', 'Warrington'), ('south_boston', 'South Boston'), ('washington_dc', 'Washington Dc'), ('clifton', 'Clifton'), ('atlantic_city', 'Atlantic City'), ('columbia_sc', 'Columbia Sc'), ('miami', 'Miami'), ('greenville', 'Greenville'), ('dothan', 'Dothan'), ('orangeburg', 'Orangeburg'), ('melbourne', 'Melbourne'), ('raleigh', 'Raleigh'), ('huntsville', 'Huntsville'), ('atlanta', 'Atlanta'), ('albany_ga', 'Albany Ga'), ('savannah', 'Savannah'), ('charlotte', 'Charlotte'), ('augusta', 'Augusta'), ('knoxville', 'Knoxville'), ('nashville', 'Nashville'), ('florence', 'Florence'), ('memphis', 'Memphis'), ('perry', 'Perry'), ('columbia_tn', 'Columbia Tn'), ('montgomery', 'Montgomery'), ('orlando', 'Orlando'), ('chattanooga', 'Chattanooga'), ('calhoun', 'Calhoun'), ('greensboro', 'Greensboro'), ('birmingham', 'Birmingham'), ('tampa', 'Tampa'), ('jacksonville', 'Jacksonville'), ('gainesville', 'Gainesville'), ('mobile', 'Mobile'), ('myrtle_beach', 'Myrtle Beach'), ('austin', 'Austin'), ('little_rock', 'Little Rock'), ('beaumont', 'Beaumont'), ('oklahoma_city', 'Oklahoma City'), ('san_antonio', 'San Antonio'), ('midland', 'Midland'), ('corpus_christi', 'Corpus Christi'), ('dallas', 'Dallas'), ('jackson', 'Jackson'), ('lubbock', 'Lubbock'), ('panama', 'Panama'), ('clear_lake', 'Clear Lake'), ('houston', 'Houston'), ('new_orleans', 'New Orleans'), ('denver', 'Denver'), ('san_jose', 'San Jose'), ('seattle', 'Seattle'), ('phoenix', 'Phoenix'), ('bakersfield', 'Bakersfield'), ('los_angeles', 'Los Angeles'), ('sacramento', 'Sacramento'), ('san_diego', 'San Diego'), ('salt_lake_city', 'Salt Lake City'), ('fresno', 'Fresno'), ('san_francisco', 'San Francisco'), ('tucson', 'Tucson'), ('portland', 'Portland'), ('bloomington', 'Bloomington'), ('iowa_city', 'Iowa City'), ('sterling_heights', 'Sterling Heights'), ('pittsburgh', 'Pittsburgh'), ('evansville', 'Evansville'), ('detroit', 'Detroit'), ('dayton', 'Dayton'), ('cincinnati', 'Cincinnati'), ('indianapolis', 'Indianapolis'), ('des_moines', 'Des Moines'), ('kalamazoo', 'Kalamazoo'), ('minneapolis', 'Minneapolis'), ('columbus', 'Columbus'), ('chicago', 'Chicago'), ('wichita', 'Wichita'), ('kansas_city', 'Kansas City'), ('munster', 'Munster'), ('lexington', 'Lexington'), ('louisville', 'Louisville'), ('st_louis', 'St Louis'), ('cleveland', 'Cleveland'), ('milwaukee', 'Milwaukee'), ('crystal_lake', 'Crystal Lake'), ('regina', 'Regina'), ('saskatoon', 'Saskatoon'), ('brandon', 'Brandon'), ('vancouver', 'Vancouver'), ('toronto', 'Toronto'), ('winnipeg', 'Winnipeg'), ('edmonton', 'Edmonton'), ('ottawa', 'Ottawa'), ('windsor', 'Windsor'), ('scarborough', 'Scarborough'), ('fort_mcmurray', 'Fort Mcmurray'), ('cambridge', 'Cambridge'), ('red_deer', 'Red Deer'), ('montreal', 'Montreal'), ('calgary', 'Calgary')], max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('female', 'Female'), ('male', 'Male')], max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='mandal',
            field=models.CharField(choices=[('group_3', 'Group 3'), ('group_0', 'Group 0'), ('group_2', 'Group 2'), ('group_1', 'Group 1'), ('kishore/kishori', 'Kishore/Kishori')], max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='region',
            field=models.CharField(choices=[('southeast', 'Southeast'), ('midwest', 'Midwest'), ('southwest', 'Southwest'), ('canada', 'Canada'), ('west', 'West'), ('northeast', 'Northeast')], max_length=60, null=True),
        ),
    ]