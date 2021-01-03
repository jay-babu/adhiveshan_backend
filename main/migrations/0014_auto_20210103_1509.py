# Generated by Django 3.1.4 on 2021-01-03 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20210103_1250'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_onboarded',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='center',
            field=models.CharField(choices=[('lansdale', 'Lansdale'), ('philadelphia', 'Philadelphia'), ('cherry_hill', 'Cherry Hill'), ('virginia_beach', 'Virginia Beach'), ('allentown', 'Allentown'), ('westchester', 'Westchester'), ('downingtown', 'Downingtown'), ('atlantic_city', 'Atlantic City'), ('washington_dc', 'Washington Dc'), ('new_haven', 'New Haven'), ('new_york', 'New York'), ('northern_virginia', 'Northern Virginia'), ('springfield', 'Springfield'), ('delaware', 'Delaware'), ('hilltop', 'Hilltop'), ('albany_ny', 'Albany Ny'), ('jersey_city', 'Jersey City'), ('roanoke', 'Roanoke'), ('harrisburg', 'Harrisburg'), ('south_boston', 'South Boston'), ('scranton', 'Scranton'), ('parsippany', 'Parsippany'), ('boston', 'Boston'), ('robbinsville', 'Robbinsville'), ('hartford', 'Hartford'), ('edison', 'Edison'), ('westborough', 'Westborough'), ('syracuse', 'Syracuse'), ('warrington', 'Warrington'), ('richmond', 'Richmond'), ('long_island', 'Long Island'), ('clifton', 'Clifton'), ('charlotte', 'Charlotte'), ('albany_ga', 'Albany Ga'), ('florence', 'Florence'), ('birmingham', 'Birmingham'), ('perry', 'Perry'), ('gainesville', 'Gainesville'), ('melbourne', 'Melbourne'), ('nashville', 'Nashville'), ('atlanta', 'Atlanta'), ('dothan', 'Dothan'), ('savannah', 'Savannah'), ('chattanooga', 'Chattanooga'), ('jacksonville', 'Jacksonville'), ('orangeburg', 'Orangeburg'), ('orlando', 'Orlando'), ('tampa', 'Tampa'), ('greenville', 'Greenville'), ('myrtle_beach', 'Myrtle Beach'), ('raleigh', 'Raleigh'), ('columbia_sc', 'Columbia Sc'), ('huntsville', 'Huntsville'), ('augusta', 'Augusta'), ('mobile', 'Mobile'), ('columbia_tn', 'Columbia Tn'), ('greensboro', 'Greensboro'), ('miami', 'Miami'), ('memphis', 'Memphis'), ('montgomery', 'Montgomery'), ('calhoun', 'Calhoun'), ('knoxville', 'Knoxville'), ('corpus_christi', 'Corpus Christi'), ('jackson', 'Jackson'), ('oklahoma_city', 'Oklahoma City'), ('houston', 'Houston'), ('little_rock', 'Little Rock'), ('austin', 'Austin'), ('new_orleans', 'New Orleans'), ('midland', 'Midland'), ('beaumont', 'Beaumont'), ('lubbock', 'Lubbock'), ('denver', 'Denver'), ('panama', 'Panama'), ('san_antonio', 'San Antonio'), ('dallas', 'Dallas'), ('clear_lake', 'Clear Lake'), ('tucson', 'Tucson'), ('los_angeles', 'Los Angeles'), ('san_jose', 'San Jose'), ('bakersfield', 'Bakersfield'), ('seattle', 'Seattle'), ('salt_lake_city', 'Salt Lake City'), ('san_francisco', 'San Francisco'), ('san_diego', 'San Diego'), ('phoenix', 'Phoenix'), ('sacramento', 'Sacramento'), ('portland', 'Portland'), ('fresno', 'Fresno'), ('des_moines', 'Des Moines'), ('detroit', 'Detroit'), ('minneapolis', 'Minneapolis'), ('kansas_city', 'Kansas City'), ('cincinnati', 'Cincinnati'), ('chicago', 'Chicago'), ('bloomington', 'Bloomington'), ('evansville', 'Evansville'), ('lexington', 'Lexington'), ('pittsburgh', 'Pittsburgh'), ('st_louis', 'St Louis'), ('indianapolis', 'Indianapolis'), ('wichita', 'Wichita'), ('louisville', 'Louisville'), ('cleveland', 'Cleveland'), ('kalamazoo', 'Kalamazoo'), ('crystal_lake', 'Crystal Lake'), ('iowa_city', 'Iowa City'), ('dayton', 'Dayton'), ('munster', 'Munster'), ('sterling_heights', 'Sterling Heights'), ('columbus', 'Columbus'), ('milwaukee', 'Milwaukee'), ('saskatoon', 'Saskatoon'), ('calgary', 'Calgary'), ('cambridge', 'Cambridge'), ('ottawa', 'Ottawa'), ('montreal', 'Montreal'), ('vancouver', 'Vancouver'), ('scarborough', 'Scarborough'), ('edmonton', 'Edmonton'), ('winnipeg', 'Winnipeg'), ('regina', 'Regina'), ('toronto', 'Toronto'), ('fort_mcmurray', 'Fort Mcmurray'), ('windsor', 'Windsor'), ('red_deer', 'Red Deer'), ('brandon', 'Brandon')], max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('female', 'Female'), ('male', 'Male')], max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='mandal',
            field=models.CharField(choices=[('group_2', 'Group 2'), ('group_1', 'Group 1'), ('group_3', 'Group 3'), ('kishore/kishori', 'Kishore/Kishori'), ('group_0', 'Group 0')], max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='region',
            field=models.CharField(choices=[('southeast', 'Southeast'), ('southwest', 'Southwest'), ('midwest', 'Midwest'), ('canada', 'Canada'), ('northeast', 'Northeast'), ('west', 'West')], max_length=60, null=True),
        ),
    ]
