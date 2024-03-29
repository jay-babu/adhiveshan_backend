# Generated by Django 3.1.4 on 2021-01-13 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_auto_20210112_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mukhpathitem',
            name='gujurati_content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='mukhpathitem',
            name='transliteration_content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='center',
            field=models.CharField(choices=[('delaware', 'Delaware'), ('virginia_beach', 'Virginia Beach'), ('warrington', 'Warrington'), ('south_boston', 'South Boston'), ('washington_dc', 'Washington Dc'), ('long_island', 'Long Island'), ('springfield', 'Springfield'), ('westchester', 'Westchester'), ('clifton', 'Clifton'), ('boston', 'Boston'), ('westborough', 'Westborough'), ('robbinsville', 'Robbinsville'), ('edison', 'Edison'), ('harrisburg', 'Harrisburg'), ('philadelphia', 'Philadelphia'), ('allentown', 'Allentown'), ('new_haven', 'New Haven'), ('cherry_hill', 'Cherry Hill'), ('northern_virginia', 'Northern Virginia'), ('richmond', 'Richmond'), ('hilltop', 'Hilltop'), ('syracuse', 'Syracuse'), ('atlantic_city', 'Atlantic City'), ('hartford', 'Hartford'), ('new_york', 'New York'), ('downingtown', 'Downingtown'), ('jersey_city', 'Jersey City'), ('albany_ny', 'Albany Ny'), ('roanoke', 'Roanoke'), ('lansdale', 'Lansdale'), ('parsippany', 'Parsippany'), ('scranton', 'Scranton'), ('calhoun', 'Calhoun'), ('savannah', 'Savannah'), ('atlanta', 'Atlanta'), ('chattanooga', 'Chattanooga'), ('huntsville', 'Huntsville'), ('montgomery', 'Montgomery'), ('raleigh', 'Raleigh'), ('nashville', 'Nashville'), ('tampa', 'Tampa'), ('albany_ga', 'Albany Ga'), ('melbourne', 'Melbourne'), ('miami', 'Miami'), ('myrtle_beach', 'Myrtle Beach'), ('columbia_sc', 'Columbia Sc'), ('knoxville', 'Knoxville'), ('orangeburg', 'Orangeburg'), ('columbia_tn', 'Columbia Tn'), ('birmingham', 'Birmingham'), ('mobile', 'Mobile'), ('memphis', 'Memphis'), ('augusta', 'Augusta'), ('greenville', 'Greenville'), ('greensboro', 'Greensboro'), ('dothan', 'Dothan'), ('florence', 'Florence'), ('gainesville', 'Gainesville'), ('orlando', 'Orlando'), ('perry', 'Perry'), ('charlotte', 'Charlotte'), ('jacksonville', 'Jacksonville'), ('beaumont', 'Beaumont'), ('denver', 'Denver'), ('jackson', 'Jackson'), ('corpus_christi', 'Corpus Christi'), ('houston', 'Houston'), ('oklahoma_city', 'Oklahoma City'), ('midland', 'Midland'), ('lubbock', 'Lubbock'), ('new_orleans', 'New Orleans'), ('panama', 'Panama'), ('dallas', 'Dallas'), ('little_rock', 'Little Rock'), ('clear_lake', 'Clear Lake'), ('san_antonio', 'San Antonio'), ('austin', 'Austin'), ('salt_lake_city', 'Salt Lake City'), ('san_francisco', 'San Francisco'), ('seattle', 'Seattle'), ('portland', 'Portland'), ('bakersfield', 'Bakersfield'), ('sacramento', 'Sacramento'), ('phoenix', 'Phoenix'), ('san_jose', 'San Jose'), ('tucson', 'Tucson'), ('fresno', 'Fresno'), ('san_diego', 'San Diego'), ('los_angeles', 'Los Angeles'), ('kalamazoo', 'Kalamazoo'), ('wichita', 'Wichita'), ('lexington', 'Lexington'), ('st_louis', 'St Louis'), ('cincinnati', 'Cincinnati'), ('cleveland', 'Cleveland'), ('munster', 'Munster'), ('crystal_lake', 'Crystal Lake'), ('des_moines', 'Des Moines'), ('kansas_city', 'Kansas City'), ('dayton', 'Dayton'), ('chicago', 'Chicago'), ('louisville', 'Louisville'), ('detroit', 'Detroit'), ('bloomington', 'Bloomington'), ('pittsburgh', 'Pittsburgh'), ('columbus', 'Columbus'), ('minneapolis', 'Minneapolis'), ('iowa_city', 'Iowa City'), ('sterling_heights', 'Sterling Heights'), ('milwaukee', 'Milwaukee'), ('evansville', 'Evansville'), ('indianapolis', 'Indianapolis'), ('brandon', 'Brandon'), ('ottawa', 'Ottawa'), ('red_deer', 'Red Deer'), ('toronto', 'Toronto'), ('edmonton', 'Edmonton'), ('regina', 'Regina'), ('vancouver', 'Vancouver'), ('montreal', 'Montreal'), ('saskatoon', 'Saskatoon'), ('scarborough', 'Scarborough'), ('cambridge', 'Cambridge'), ('winnipeg', 'Winnipeg'), ('calgary', 'Calgary'), ('windsor', 'Windsor'), ('fort_mcmurray', 'Fort Mcmurray')], max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='mandal',
            field=models.CharField(choices=[('group_2', 'Group 2'), ('kishore/kishori', 'Kishore/Kishori'), ('group_1', 'Group 1'), ('group_0', 'Group 0'), ('group_3', 'Group 3')], max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='region',
            field=models.CharField(choices=[('west', 'West'), ('southwest', 'Southwest'), ('canada', 'Canada'), ('midwest', 'Midwest'), ('southeast', 'Southeast'), ('northeast', 'Northeast')], max_length=60, null=True),
        ),
    ]
