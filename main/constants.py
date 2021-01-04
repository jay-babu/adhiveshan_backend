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

# Centers
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
BRANDON = "brandon"
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
DENVER = "denver"
DES_MOINES = "des_moines"
DETROIT = "detroit"
DOTHAN = "dothan"
DOWNINGTOWN = "downingtown"
EDISON = "edison"
EDMONTON = "edmonton"
EVANSVILLE = "evansville"
FLORENCE = "florence"
FORT_MCMURRAY = "fort_mcmurray"
FRESNO = "fresno"
GAINESVILLE = "gainesville"
GREENSBORO = "greensboro"
GREENVILLE = "greenville"
HARRISBURG = "harrisburg"
HARTFORD = "hartford"
HILLTOP = "hilltop"
HOUSTON = "houston"
HUNTSVILLE = "huntsville"
INDIANAPOLIS = "indianapolis"
IOWA_CITY = "iowa_city"
JACKSON = "jackson"
JACKSONVILLE = "jacksonville"
JERSEY_CITY = "jersey_city"
KALAMAZOO = "kalamazoo"
KANSAS_CITY = "kansas_city"
KNOXVILLE = "knoxville"
LANSDALE = "lansdale"
LEXINGTON = "lexington"
LITTLE_ROCK = "little_rock"
LONG_ISLAND = "long_island"
LOS_ANGELES = "los_angeles"
LOUISVILLE = "louisville"
LUBBOCK = "lubbock"
MELBOURNE = "melbourne"
MEMPHIS = "memphis"
MIAMI = "miami"
MIDLAND = "midland"
MILWAUKEE = "milwaukee"
MINNEAPOLIS = "minneapolis"
MOBILE = "mobile"
MONTGOMERY = "montgomery"
MONTREAL = "montreal"
MUNSTER = "munster"
MYRTLE_BEACH = "myrtle_beach"
NASHVILLE = "nashville"
NEW_HAVEN = "new_haven"
NEW_ORLEANS = "new_orleans"
NEW_YORK = "new_york"
NORTHERN_VIRGINIA = "northern_virginia"
OKLAHOMA_CITY = "oklahoma_city"
ORANGEBURG = "orangeburg"
ORLANDO = "orlando"
OTTAWA = "ottawa"
PANAMA = "panama"
PARSIPPANY = "parsippany"
PERRY = "perry"
PHILADELPHIA = "philadelphia"
PHOENIX = "phoenix"
PITTSBURGH = "pittsburgh"
PORTLAND = "portland"
RALEIGH = "raleigh"
RED_DEER = "red_deer"
REGINA = "regina"
RICHMOND = "richmond"
ROANOKE = "roanoke"
ROBBINSVILLE = "robbinsville"
SACRAMENTO = "sacramento"
SALT_LAKE_CITY = "salt_lake_city"
SAN_ANTONIO = "san_antonio"
SAN_DIEGO = "san_diego"
SAN_FRANCISCO = "san_francisco"
SAN_JOSE = "san_jose"
SASKATOON = "saskatoon"
SAVANNAH = "savannah"
SCARBOROUGH = "scarborough"
SCRANTON = "scranton"
SEATTLE = "seattle"
SOUTH_BOSTON = "south_boston"
SPRINGFIELD = "springfield"
STERLING_HEIGHTS = "sterling_heights"
ST_LOUIS = "st_louis"
SYRACUSE = "syracuse"
TAMPA = "tampa"
TORONTO = "toronto"
TUCSON = "tucson"
VANCOUVER = "vancouver"
VIRGINIA_BEACH = "virginia_beach"
WARRINGTON = "warrington"
WASHINGTON_DC = "washington_dc"
WESTBOROUGH = "westborough"
WESTCHESTER = "westchester"
WICHITA = "wichita"
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
        DOWNINGTOWN,
        EDISON,
        HARRISBURG,
        HARTFORD,
        HILLTOP,
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
        MOBILE,
        MONTGOMERY,
        MYRTLE_BEACH,
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
        DENVER,
        HOUSTON,
        JACKSON,
        LITTLE_ROCK,
        LUBBOCK,
        MIDLAND,
        NEW_ORLEANS,
        OKLAHOMA_CITY,
        PANAMA,
        SAN_ANTONIO,
    },
    WEST: {
        BAKERSFIELD,
        FRESNO,
        LOS_ANGELES,
        PHOENIX,
        PORTLAND,
        SACRAMENTO,
        SALT_LAKE_CITY,
        SAN_DIEGO,
        SAN_FRANCISCO,
        SAN_JOSE,
        SEATTLE,
        TUCSON,
    },
    MIDWEST: {
        BLOOMINGTON,
        CHICAGO,
        CINCINNATI,
        CLEVELAND,
        COLUMBUS,
        CRYSTAL_LAKE,
        DAYTON,
        DES_MOINES,
        DETROIT,
        EVANSVILLE,
        INDIANAPOLIS,
        IOWA_CITY,
        KALAMAZOO,
        KANSAS_CITY,
        LEXINGTON,
        LOUISVILLE,
        MILWAUKEE,
        MINNEAPOLIS,
        MUNSTER,
        PITTSBURGH,
        STERLING_HEIGHTS,
        ST_LOUIS,
        WICHITA,
    },
    CANADA: {
        BRANDON,
        CALGARY,
        CAMBRIDGE,
        EDMONTON,
        FORT_MCMURRAY,
        MONTREAL,
        OTTAWA,
        RED_DEER,
        REGINA,
        SASKATOON,
        SCARBOROUGH,
        TORONTO,
        VANCOUVER,
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
DIVYABHAV_NIRDOSHBUDDHI = 'divyabhav_nirdoshbuddhi'
SAMP_SURADHBHAV_EKTA = 'samp_suradhbhav_ekta'
MODULE_TYPES = [
    (SATSANG_DIKSHA, 'Satsang Diksha'),
    (SWAMINI_VATO, 'Swamini Vato'),
    (SHLOK_SAKHI, 'Shlok/Sakhi'),
    (KIRTAN, 'Kirtan'),
    (PRASANG_MANAN, 'Prasang Manan'),
    (DIVYABHAV_NIRDOSHBUDDHI, 'Divyabhav Nirdoshbuddhi'),
    (SAMP_SURADHBHAV_EKTA, 'Samp Suradhbhav Ekta'),
]

# Tiers
GHANSHYAM = 'ghanshyam'
MAHANT = 'mahant'
PRAMUKH = 'pramukh'
YOGI = 'yogi'
SHASTRI = 'shastri'
KM_DEFAULT = 'km_default'
KM_DEFAULT_VALUE = 4
TIERS = [
    (GHANSHYAM, 'Ghanshyam'),
    (MAHANT, 'Mahant'),
    (PRAMUKH, 'Pramukh'),
    (YOGI, 'Yogi'),
    (SHASTRI, 'Shastri'),
    (KM_DEFAULT, 'KM Default'),
]

GROUP_0_PLEDGES = {
    SATSANG_DIKSHA: {GHANSHYAM: 20},
    SWAMINI_VATO: {GHANSHYAM: 5},
    SHLOK_SAKHI: {GHANSHYAM: 2},
    KIRTAN: {GHANSHYAM: 1},
    PRASANG_MANAN: {GHANSHYAM: 1},
}

GROUP_1_PLEDGES = {
    SATSANG_DIKSHA: {
        GHANSHYAM: 20,
        MAHANT: 64,
        PRAMUKH: 100,
        YOGI: 200,
        SHASTRI: 315
    },
    SWAMINI_VATO: {
        MAHANT: 5,
        PRAMUKH: 10,
        YOGI: 15,
        SHASTRI: 20
    },
    SHLOK_SAKHI: {
        MAHANT: 3,
        PRAMUKH: 5,
        YOGI: 7,
        SHASTRI: 10
    },
    KIRTAN: {
        MAHANT: 2,
        PRAMUKH: 3,
        YOGI: 4,
        SHASTRI: 5
    },
    PRASANG_MANAN: {
        MAHANT: 2,
        PRAMUKH: 3,
        YOGI: 4,
        SHASTRI: 5
    },
}


GROUP_2_PLEDGES = {
    SATSANG_DIKSHA: {
        MAHANT: 64,
        PRAMUKH: 100,
        YOGI: 200,
        SHASTRI: 315
    },
    SWAMINI_VATO: {
        MAHANT: 10,
        PRAMUKH: 15,
        YOGI: 20,
        SHASTRI: 25
    },
    SHLOK_SAKHI: {
        MAHANT: 5,
        PRAMUKH: 8,
        YOGI: 11,
        SHASTRI: 15
    },
    KIRTAN: {
        MAHANT: 3,
        PRAMUKH: 5,
        YOGI: 7,
        SHASTRI: 10
    },
    PRASANG_MANAN: {
        MAHANT: 3,
        PRAMUKH: 5,
        YOGI: 7,
        SHASTRI: 10,
    },
}

GROUP_3_PLEDGES = {
    SATSANG_DIKSHA: {
        MAHANT: 64,
        PRAMUKH: 100,
        YOGI: 200,
        SHASTRI: 315,
    },
    SWAMINI_VATO: {
        MAHANT: 15,
        PRAMUKH: 25,
        YOGI: 35,
        SHASTRI: 50
    },
    SHLOK_SAKHI: {
        MAHANT: 5,
        PRAMUKH: 10,
        YOGI: 15,
        SHASTRI: 20
    },
    KIRTAN: {
        MAHANT: 5,
        PRAMUKH: 8,
        YOGI: 11,
        SHASTRI: 15,
    },
    PRASANG_MANAN: {
        MAHANT: 5,
        PRAMUKH: 8,
        YOGI: 11,
        SHASTRI: 15
    },
}

KISHORE_KISHORI_PLEDGES = {
    SATSANG_DIKSHA: {
        MAHANT: 64,
        PRAMUKH: 100,
        YOGI: 200,
        SHASTRI: 315
    },
    DIVYABHAV_NIRDOSHBUDDHI: {
        KM_DEFAULT: KM_DEFAULT_VALUE
    },
    SAMP_SURADHBHAV_EKTA: {
        KM_DEFAULT: KM_DEFAULT_VALUE
    }
}

PLEDGE_OPTIONS = {
    GROUP_0: GROUP_0_PLEDGES,
    GROUP_1: GROUP_1_PLEDGES,
    GROUP_2: GROUP_2_PLEDGES,
    GROUP_3: GROUP_3_PLEDGES,
    KISHORE_KISHORI: KISHORE_KISHORI_PLEDGES,
}


def get_pledge_options(mandal):
    return PLEDGE_OPTIONS[mandal]


def get_required_mukhpath_items(module, mandal, tier):
    return PLEDGE_OPTIONS[mandal][module][tier]
