# Regions
WEST = 'west'
NORTHEAST = 'northeast'
SOUTHWEST = 'southwest'
SOUTHEAST = 'southeast'
MIDWEST = 'midwest'
CANADA = 'canada'
REGIONS = {
    WEST,
    NORTHEAST,
    SOUTHWEST,
    SOUTHEAST,
    MIDWEST,
    CANADA,
}

ALBANY_GA = "albany_ga"
ALBANY_NY = "albany_ny"
ALLENTOWN = "allentown"
ATLANTA = "atlanta"
ATLANTIC_CITY = "atlantic_city"
AUGUSTA = "augusta"
AUSTIN = "austin"
BAKERSFIELD = "bakersfield"
BEAUMONT = "beaumont"
BIRMINGHAM = "birmingham"
BLOOMINGTON = "bloomington"
BOSTON = "boston"
CALGARY = "calgary"
CALHOUN = "calhoun"
CAMBRIDGE = "cambridge"
CHARLOTTE = "charlotte"
CHATTANOOGA = "chattanooga"
CHERRY_HILL = "cherry_hill"
CHICAGO = "chicago"
CINCINNATI = "cincinnati"
CLEAR_LAKE = "clear_lake"
CLEVELAND = "cleveland"
CLIFTON = "clifton"
COLUMBIA_SC = "columbia_sc"
COLUMBIA_TN = "columbia_tn"
COLUMBUS = "columbus"
CORPUS_CHRISTI = "corpus_christi"
CRYSTAL_LAKE = "crystal_lake"
DALLAS = "dallas"
DAYTON = "dayton"
DELAWARE = "delaware"
DETROIT = "detroit"
DOTHAN = "dothan"
EDISON = "edison"
EDMONTON = "edmonton"
EVANSVILLE = "evansville"
FLORENCE = "florence"
FRESNO = "fresno"
GAINESVILLE = "gainesville"
GREENSBORO = "greensboro"
GREENVILLE = "greenville"
HARRISBURG = "harrisburg"
HARTFORD = "hartford"
HOUSTON = "houston"
HUNTSVILLE = "huntsville"
INDIANAPOLIS = "indianapolis"
JACKSON = "jackson"
JACKSONVILLE = "jacksonville"
JERSEY_CITY = "jersey_city"
KANSAS_CITY = "kansas_city"
KNOXVILLE = "knoxville"
LANSDALE = "lansdale"
LITTLE_ROCK = "little_rock"
LONG_ISLAND = "long_island"
LOS_ANGELES = "los_angeles"
LOUISVILLE = "louisville"
LUBBOCK = "lubbock"
MELBOURNE = "melbourne"
MEMPHIS = "memphis"
MIAMI = "miami"
MILWAUKEE = "milwaukee"
MINNEAPOLIS = "minneapolis"
MONTGOMERY = "montgomery"
MUNSTER = "munster"
NASHVILLE = "nashville"
NEW_HAVEN = "new_haven"
NEW_ORLEANS = "new_orleans"
NEW_YORK = "new_york"
NORTHERN_VIRGINIA = "northern_virginia"
OKLAHOMA_CITY = "oklahoma_city"
ORANGEBURG = "orangeburg"
ORLANDO = "orlando"
PARSIPPANY = "parsippany"
PERRY = "perry"
PHILADELPHIA = "philadelphia"
PHOENIX = "phoenix"
PITTSBURGH = "pittsburgh"
PORTLAND = "portland"
RALEIGH = "raleigh"
RICHMOND = "richmond"
ROANOKE = "roanoke"
ROBBINSVILLE = "robbinsville"
SACRAMENTO = "sacramento"
SALT_LAKE_CITY = "salt_lake_city"
SAN_ANTONIO = "san_antonio"
SAN_DIEGO = "san_diego"
SAN_FRANCISCO = "san_francisco"
SAN_JOSE = "san_jose"
SAVANNAH = "savannah"
SCARBOROUGH = "scarborough"
SCRANTON = "scranton"
SEATTLE = "seattle"
SOUTH_BOSTON = "south_boston"
SPRINGFIELD = "springfield"
ST_LOUIS = "st_louis"
STERLING_HEIGHTS = "sterling_heights"
SYRACUSE = "syracuse"
TAMPA = "tampa"
TORONTO = "toronto"
TUCSON = "tucson"
VIRGINIA_BEACH = "virginia_beach"
WARRINGTON = "warrington"
WASHINGTON_DC = "washington_dc"
WESTBOROUGH = "westborough"
WESTCHESTER = "westchester"
WINDSOR = "windsor"
WINNIPEG = "winnipeg"

REGIONS_CENTERS = {
    NORTHEAST: {
        ALBANY_NY,
        ALLENTOWN,
        ATLANTIC_CITY,
        BOSTON,
        CHERRY_HILL,
        CLIFTON,
        DELAWARE,
        EDISON,
        HARRISBURG,
        HARTFORD,
        JERSEY_CITY,
        LANSDALE,
        LONG_ISLAND,
        NEW_HAVEN,
        NEW_YORK,
        NORTHERN_VIRGINIA,
        PARSIPPANY,
        PHILADELPHIA,
        RICHMOND,
        ROANOKE,
        ROBBINSVILLE,
        SCRANTON,
        SOUTH_BOSTON,
        SPRINGFIELD,
        SYRACUSE,
        VIRGINIA_BEACH,
        WARRINGTON,
        WASHINGTON_DC,
        WESTBOROUGH,
        WESTCHESTER,
    },
    SOUTHEAST: {
        ALBANY_GA,
        ATLANTA,
        AUGUSTA,
        BIRMINGHAM,
        CALHOUN,
        CHARLOTTE,
        CHATTANOOGA,
        COLUMBIA_SC,
        COLUMBIA_TN,
        DOTHAN,
        FLORENCE,
        GAINESVILLE,
        GREENSBORO,
        GREENVILLE,
        HUNTSVILLE,
        JACKSONVILLE,
        KNOXVILLE,
        MELBOURNE,
        MEMPHIS,
        MIAMI,
        MONTGOMERY,
        NASHVILLE,
        ORANGEBURG,
        ORLANDO,
        PERRY,
        RALEIGH,
        SAVANNAH,
        TAMPA,
    },
    SOUTHWEST: {
        AUSTIN,
        BEAUMONT,
        CLEAR_LAKE,
        CORPUS_CHRISTI,
        DALLAS,
        HOUSTON,
        JACKSON,
        LITTLE_ROCK,
        LUBBOCK,
        NEW_ORLEANS,
        OKLAHOMA_CITY,
        SAN_ANTONIO,
    },
    WEST: {
        BAKERSFIELD,
        FRESNO,
        LOS_ANGELES,
        PHOENIX,
        PORTLAND,
        SACRAMENTO,
        SAN_DIEGO,
        SAN_FRANCISCO,
        SAN_JOSE,
        SEATTLE,
        TUCSON,
        SALT_LAKE_CITY,
    },
    MIDWEST: {
        BLOOMINGTON,
        CHICAGO,
        CINCINNATI,
        CLEVELAND,
        COLUMBUS,
        CRYSTAL_LAKE,
        DAYTON,
        DETROIT,
        EVANSVILLE,
        INDIANAPOLIS,
        KANSAS_CITY,
        LOUISVILLE,
        MILWAUKEE,
        MINNEAPOLIS,
        MUNSTER,
        PITTSBURGH,
        ST_LOUIS,
        STERLING_HEIGHTS,
    },
    CANADA: {
        CALGARY,
        CAMBRIDGE,
        EDMONTON,
        SCARBOROUGH,
        TORONTO,
        WINDSOR,
        WINNIPEG,
    },
}

CENTERS_REGIONS = {center: region for region, centers in REGIONS_CENTERS.items() for center in centers}

# Side
MALE = 'male'
FEMALE = 'female'
GENDERS = {
    MALE,
    FEMALE,
}

# Mandals
GROUP_0 = 'group_0'
GROUP_1 = 'group_1'
GROUP_2 = 'group_2'
GROUP_3 = 'group_3'
KISHORE_KISHORI = 'kishore/kishori'
MANDALS = {
    GROUP_0,
    GROUP_1,
    GROUP_2,
    GROUP_3,
    KISHORE_KISHORI,
}

# Modules
SATSANG_DIKSHA = 'satsang_diksha'
SWAMINI_VATO = 'swamini_vato'
SHLOK_SAKHI = 'shlok_sakhi'
KIRTAN = 'kirtan'
PRASANG_MANAN = 'prasang_manan'
MAHIMA = 'mahima'
SEVA = 'seva'
SAMARPAN = 'samarpan'
BHAKTI = 'bhakti'
AHNIK = 'ahnik'
MODULE_TYPES = [
    (SATSANG_DIKSHA, 'Satsang Diksha'),
    (SWAMINI_VATO, 'Swamini Vato'),
    (SHLOK_SAKHI, 'Shlok/Sakhi'),
    (KIRTAN, 'Kirtan'),
    (PRASANG_MANAN, 'Prasang Manan'),
    (MAHIMA, 'Mahima'),
    (SEVA, 'Seva'),
    (SAMARPAN, 'Samarpan'),
    (BHAKTI, 'Bhakti'),
    (AHNIK, 'Ahnik'),
]

# Tiers
GHANSHYAM = 'ghanshyam'
MAHANT = 'mahant'
PRAMUKH = 'pramukh'
YOGI = 'yogi'
SHASTRI = 'shastri'
TIERS = [
    (GHANSHYAM, 'Ghanshyam'),
    (MAHANT, 'Mahant'),
    (PRAMUKH, 'Pramukh'),
    (YOGI, 'Yogi'),
    (SHASTRI, 'Shastri'),
]

REQUIRED_MUKHPATH_ITEMS = {
    # GROUP 0
    ('satsang_diksha', 'Group 0', 'ghanshyam'): 20,
    ('swamini_vato', 'Group 0', 'ghanshyam'): 5,
    ('shlok_sakhi', 'Group 0', 'ghanshyam'): 2,
    ('kirtan', 'Group 0', 'ghanshyam'): 1,
    ('prasang_manan', 'Group 0', 'ghanshyam'): 1,

    # GROUP 1
    ('satsang_diksha', 'group_1', 'ghanshyam'): 20,
    ('satsang_diksha', 'group_1', 'mahant'): 64,
    ('satsang_diksha', 'group_1', 'pramukh'): 100,
    ('satsang_diksha', 'group_1', 'yogiji'): 200,
    ('satsang_diksha', 'group_1', 'shastri'): 315,

    ('swamini_vato', 'group_1', 'mahant'): 5,
    ('swamini_vato', 'group_1', 'pramukh'): 10,
    ('swamini_vato', 'group_1', 'yogiji'): 15,
    ('swamini_vato', 'group_1', 'shastri'): 20,

    ('shlok_sakhi', 'group_1', 'mahant'): 3,
    ('shlok_sakhi', 'group_1', 'pramukh'): 5,
    ('shlok_sakhi', 'group_1', 'yogiji'): 7,
    ('shlok_sakhi', 'group_1', 'shastri'): 10,

    ('kirtan', 'group_1', 'mahant'): 2,
    ('kirtan', 'group_1', 'pramukh'): 3,
    ('kirtan', 'group_1', 'yogiji'): 4,
    ('kirtan', 'group_1', 'shastri'): 5,

    ('prasang_manan', 'group_1', 'mahant'): 2,
    ('prasang_manan', 'group_1', 'pramukh'): 3,
    ('prasang_manan', 'group_1', 'yogiji'): 4,
    ('prasang_manan', 'group_1', 'shastri'): 5,

    # GROUP 2
    ('satsang_diksha', 'group_2', 'mahant'): 64,
    ('satsang_diksha', 'group_2', 'pramukh'): 100,
    ('satsang_diksha', 'group_2', 'yogiji'): 200,
    ('satsang_diksha', 'group_2', 'shastri'): 315,

    ('swamini_vato', 'group_2', 'mahant'): 10,
    ('swamini_vato', 'group_2', 'pramukh'): 15,
    ('swamini_vato', 'group_2', 'yogiji'): 20,
    ('swamini_vato', 'group_2', 'shastri'): 25,

    ('shlok_sakhi', 'group_2', 'mahant'): 5,
    ('shlok_sakhi', 'group_2', 'pramukh'): 8,
    ('shlok_sakhi', 'group_2', 'yogiji'): 11,
    ('shlok_sakhi', 'group_2', 'shastri'): 15,

    ('kirtan', 'group_2', 'mahant'): 3,
    ('kirtan', 'group_2', 'pramukh'): 5,
    ('kirtan', 'group_2', 'yogiji'): 7,
    ('kirtan', 'group_2', 'shastri'): 10,

    ('prasang_manan', 'group_2', 'mahant'): 3,
    ('prasang_manan', 'group_2', 'pramukh'): 5,
    ('prasang_manan', 'group_2', 'yogiji'): 7,
    ('prasang_manan', 'group_2', 'shastri'): 10,

    # GROUP 3
    ('satsang_diksha', 'group_3', 'mahant'): 64,
    ('satsang_diksha', 'group_3', 'pramukh'): 100,
    ('satsang_diksha', 'group_3', 'yogiji'): 200,
    ('satsang_diksha', 'group_3', 'shastri'): 315,

    ('swamini_vato', 'group_3', 'mahant'): 15,
    ('swamini_vato', 'group_3', 'pramukh'): 25,
    ('swamini_vato', 'group_3', 'yogiji'): 35,
    ('swamini_vato', 'group_3', 'shastri'): 50,

    ('shlok_sakhi', 'group_3', 'mahant'): 5,
    ('shlok_sakhi', 'group_3', 'pramukh'): 10,
    ('shlok_sakhi', 'group_3', 'yogiji'): 15,
    ('shlok_sakhi', 'group_3', 'shastri'): 20,

    ('kirtan', 'group_3', 'mahant'): 5,
    ('kirtan', 'group_3', 'pramukh'): 8,
    ('kirtan', 'group_3', 'yogiji'): 11,
    ('kirtan', 'group_3', 'shastri'): 15,

    ('prasang_manan', 'group_3', 'mahant'): 5,
    ('prasang_manan', 'group_3', 'pramukh'): 8,
    ('prasang_manan', 'group_3', 'yogiji'): 11,
    ('prasang_manan', 'group_3', 'shastri'): 15,

    # Kishore-Kishori
    ('satsang_diksha', 'kishore/kishori', 'mahant'): 64,
    ('satsang_diksha', 'kishore/kishori', 'pramukh'): 100,
    ('satsang_diksha', 'kishore/kishori', 'yogiji'): 200,
    ('satsang_diksha', 'kishore/kishori', 'shastri'): 315,
}
