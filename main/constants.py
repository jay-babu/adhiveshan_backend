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
# Bal
SATSANG_DIKSHA = 'satsang_diksha'
SWAMINI_VATO = 'swamini_vato'
SHLOKA_SAKHI = 'shloka_sakhi'
KIRTAN = 'kirtan'
PRASANG_MANAN = 'prasang_manan'
# Keep in order as presented in website.
BAL_ONLY_MODULES = [
    SWAMINI_VATO,
    SHLOKA_SAKHI,
    KIRTAN,
    PRASANG_MANAN
]

# Kishore
ANTARDRASHTI = 'antardrashti'
PRAPTINO_VICHAR = 'praptino_vichar'
RAJIPANO_VICHAR = 'rajipano_vichar'
SANKHYA_VICHAR = 'sankhya_vichar'
GUN_GRAHAN_SAMBANDHNO_MAHIMA = 'gun_grahan_sambandhno_mahima'
ATMA_VICHAR = 'atma_vichar'
PRARTHANA = 'prarthana'
UPASANA_SWARUPNISHTHA = 'upasana_swarupnishtha'
AKSHAR_PURUSHOTTAM_SIDDHANT = 'akshar_purushottam_siddhant'
SARVOPARI = 'sarvopari'
DIVYA_SAKAR = 'divya_sakar'
SARVA_KARTA = 'sarva_karta'
PRAGAT = 'pragat'
AGNA = 'agna'
ASHRO = 'ashro'
SEVA = 'seva'
VISHWAS_SHRADDHA = 'vishwas_shraddha'
NIYAM_DHARMA = 'niyam_dharma'
BHAKTI = 'bhakti'
SHURVIRTA_HIMMAT = 'shurvirta_himmat'
SMRUTI = 'smruti'
SUKH = 'sukh'
KATHA_VARTA = 'katha_varta'
SATSANG_READING = 'satsang_reading'
SAMP_SURADHBHAV_EKTA = 'samp_suradhbhav_ekta'
KSHAMA = 'kshama'
SAHAN = 'sahan'
NIRMANIPANU = 'nirmanipanu'
DIVYABHAV_NIRDOSHBUDDHI = 'divyabhav_nirdoshbuddhi'
SATPURUSHNO_MAHIMA = 'satpurushno_mahima'
DRADH_PRITI = 'dradh_priti'
SATSANG = 'satsang'
KUSANG = 'kusang'
SWABHAV = 'swabhav'
ABHAV_AVGUN = 'abhav_avgun'
AHNIK = 'ahnik'
CHOSAR_PADS = 'chosar_pads'
FAGVA = 'fagva'
KISHORE_ONLY_MODULES = [
    ANTARDRASHTI,
    PRAPTINO_VICHAR,
    RAJIPANO_VICHAR,
    SANKHYA_VICHAR,
    GUN_GRAHAN_SAMBANDHNO_MAHIMA,
    ATMA_VICHAR,
    PRARTHANA,
    UPASANA_SWARUPNISHTHA,
    AKSHAR_PURUSHOTTAM_SIDDHANT,
    SARVOPARI,
    DIVYA_SAKAR,
    SARVA_KARTA,
    PRAGAT,
    AGNA,
    ASHRO,
    SEVA,
    VISHWAS_SHRADDHA,
    NIYAM_DHARMA,
    BHAKTI,
    SHURVIRTA_HIMMAT,
    SMRUTI,
    SUKH,
    KATHA_VARTA,
    SATSANG_READING,
    SAMP_SURADHBHAV_EKTA,
    KSHAMA,
    SAHAN,
    NIRMANIPANU,
    DIVYABHAV_NIRDOSHBUDDHI,
    SATPURUSHNO_MAHIMA,
    DRADH_PRITI,
    SATSANG,
    KUSANG,
    SWABHAV,
    ABHAV_AVGUN,
    AHNIK,
    CHOSAR_PADS,
    FAGVA,
]

BAL_AND_KISHORE_MODULES = [
    SATSANG_DIKSHA
]

MODULE_ICON_LINKS = {
    SATSANG_DIKSHA: 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/Logos/Satsang%20Diksha%20300.png',
    SWAMINI_VATO: 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/Logos/Swamini%20Vato%20300.png',
    SHLOKA_SAKHI: 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/Logos/Shloka%20Sakhi%20300.png',
    KIRTAN: 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/Logos/Kirtans%20300.png',
    PRASANG_MANAN: 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/Logos/Prasang%20Manan%20300.png',

    ANTARDRASHTI: 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/KM%20Module%20Photos/1antardrashti.jpg',
    PRAPTINO_VICHAR: 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/KM%20Module%20Photos/2praptinovichar.png',
    RAJIPANO_VICHAR: 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/KM%20Module%20Photos/3raajipano%20vichar.jpg',
    SANKHYA_VICHAR: 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/KM%20Module%20Photos/4sankhyanovichar.JPG',
    GUN_GRAHAN_SAMBANDHNO_MAHIMA: 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/KM%20Module%20Photos/5gungrahan.jpg',
    ATMA_VICHAR: 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/KM%20Module%20Photos/6atmanovichar.jpg',
    PRARTHANA: 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/KM%20Module%20Photos/7prarthana.jpg',
    UPASANA_SWARUPNISHTHA: 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/KM%20Module%20Photos/8upasanaswarupnishtha.jpg',
    AKSHAR_PURUSHOTTAM_SIDDHANT: 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/KM%20Module%20Photos/9aksharpurushottamsiddhant.jpg',
    SARVOPARI: 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/KM%20Module%20Photos/10sarvopari.jpg',
    DIVYA_SAKAR: 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/KM%20Module%20Photos/11divyasakar.jpg',
    SARVA_KARTA: 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/KM%20Module%20Photos/12sarvakarta.jpg',
    PRAGAT: 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/KM%20Module%20Photos/13pragat.jpg',
    AGNA: 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/KM%20Module%20Photos/14agna.jpg',
    ASHRO: 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/KM%20Module%20Photos/15ashro.PNG',
    SEVA: 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/KM%20Module%20Photos/16seva.jpg',
    VISHWAS_SHRADDHA: 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/KM%20Module%20Photos/17vishwas.jpg',
    NIYAM_DHARMA: 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/KM%20Module%20Photos/18niyamdharam.jpg',
    BHAKTI: 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/KM%20Module%20Photos/19bhakti.jpg',
    SHURVIRTA_HIMMAT: 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/KM%20Module%20Photos/20shurvirtahimmat.jpg',
    SMRUTI: 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/KM%20Module%20Photos/21smruti.jpg',
    SUKH: 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/KM%20Module%20Photos/22sukh.jpg',
    KATHA_VARTA: 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/KM%20Module%20Photos/23kathavarta.jpg',
    SATSANG_READING: 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/KM%20Module%20Photos/24satsangreading.jpg',
    SAMP_SURADHBHAV_EKTA: 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/KM%20Module%20Photos/25samp.jpg',
    KSHAMA: 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/KM%20Module%20Photos/26kshama.jpg',
    SAHAN: 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/KM%20Module%20Photos/27sahan.jpg',
    NIRMANIPANU: 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/KM%20Module%20Photos/28nirmanipanu.jpg',
    DIVYABHAV_NIRDOSHBUDDHI: 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/KM%20Module%20Photos/29divyabhav.PNG',
    SATPURUSHNO_MAHIMA: 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/KM%20Module%20Photos/30satpurushnomahima.jpg',
    DRADH_PRITI: 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/KM%20Module%20Photos/31dradhpriti.jpg',
    SATSANG: 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/KM%20Module%20Photos/32satsang.jpg',
    KUSANG: 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/KM%20Module%20Photos/33kusang.jpg',
    SWABHAV: 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/KM%20Module%20Photos/34swabhav.jpg',
    ABHAV_AVGUN: 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/KM%20Module%20Photos/35abhavavgun.jpg',
    AHNIK: 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/KM%20Module%20Photos/36ahnik.PNG',
    CHOSAR_PADS: 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/KM%20Module%20Photos/37chosarpads.jpg',
    FAGVA: 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/KM%20Module%20Photos/38fagva.PNG',
}

# Tiers
GHANSHYAM = 'ghanshyam'
MAHANT = 'mahant'
PRAMUKH = 'pramukh'
YOGI = 'yogi'
SHASTRI = 'shastri'

# KM Only
BRONZE = 'bronze'
SILVER = 'silver'
GOLD = 'gold'
PLATINUM = 'platinum'

TIERS = [
    (GHANSHYAM, 'Ghanshyam'),
    (MAHANT, 'Mahant'),
    (PRAMUKH, 'Pramukh'),
    (YOGI, 'Yogi'),
    (SHASTRI, 'Shastri'),

    # KM Only
    (BRONZE, 'Bronze'),
    (SILVER, 'Silver'),
    (GOLD, 'Gold'),
    (PLATINUM, 'Platinum'),
]

REQUIRED_PER_KM_MODULE = {
    ANTARDRASHTI: 4,
    PRAPTINO_VICHAR: 4,
    RAJIPANO_VICHAR: 4,
    SANKHYA_VICHAR: 4,
    GUN_GRAHAN_SAMBANDHNO_MAHIMA: 4,
    ATMA_VICHAR: 4,
    PRARTHANA: 4,
    UPASANA_SWARUPNISHTHA: 4,
    AKSHAR_PURUSHOTTAM_SIDDHANT: 4,
    SARVOPARI: 4,
    DIVYA_SAKAR: 4,
    SARVA_KARTA: 4,
    PRAGAT: 4,
    AGNA: 4,
    ASHRO: 4,
    SEVA: 4,
    VISHWAS_SHRADDHA: 4,
    NIYAM_DHARMA: 4,
    BHAKTI: 4,
    SHURVIRTA_HIMMAT: 4,
    SMRUTI: 4,
    SUKH: 4,
    KATHA_VARTA: 4,
    SATSANG_READING: 4,
    SAMP_SURADHBHAV_EKTA: 4,
    KSHAMA: 4,
    SAHAN: 4,
    NIRMANIPANU: 4,
    DIVYABHAV_NIRDOSHBUDDHI: 4,
    SATPURUSHNO_MAHIMA: 4,
    DRADH_PRITI: 4,
    SATSANG: 4,
    KUSANG: 4,
    SWABHAV: 4,
    ABHAV_AVGUN: 4,
    AHNIK: 7,
    CHOSAR_PADS: 4,
    FAGVA: 1,
}

GROUP_0_PLEDGES = {
    SATSANG_DIKSHA: {GHANSHYAM: 20},
    SWAMINI_VATO: {GHANSHYAM: 5},
    SHLOKA_SAKHI: {GHANSHYAM: 2},
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
    SHLOKA_SAKHI: {
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
    SHLOKA_SAKHI: {
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
    SHLOKA_SAKHI: {
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

KM_MODULES = 'km_modules'
KISHORE_KISHORI_PLEDGES = {
    SATSANG_DIKSHA: {
        MAHANT: 64,
        PRAMUKH: 100,
        YOGI: 200,
        SHASTRI: 315
    },
    KM_MODULES: {
        BRONZE: 5,
        SILVER: 10,
        GOLD: 15,
        PLATINUM: 20,
    },
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


BAL_FAQ = {
    'General': [
        {
            'question': 'What is Adhiveshan?',
            'answer': '<b>Adhiveshan is a structured way of memorizing Mukhpāṭh, or scriptural references or quotations, which is focused on a certain satsang topics or themes.</b> Adhiveshan is NOT a competition, but rather a challenge for ourselves to sacrifice our time to memorize the Mukhpāṭh, learn its meaning, and eventually imbibe it in our lives to please our Guru.',
        },
        {
            'question': 'Why do we do Adhiveshans?',
            'answer': 'Adhiveshan has been very dear to the hearts of our Gurus. Starting with Yogi Bapa’s passion for balaks and balikas to memorize Mukhpāṭh during their summer vacations to the various Adhiveshans held with Pramukh Swāmi Mahārāj and Mahant Swāmi Mahārāj, memorizing and understanding Mukhpāṭh has been an integral way for balaks and balikas to earn the Rājipo of our Gurus. <br/><br/> By learning and memorizing various parts of our shastras (scriptures), we are able to ground ourselves in the Akshar Purushottam Darshan and better understand our beliefs and principles. Mukhpāṭh also helps us find solutions to the many problems we may face in life.  <br/><br/> This Adhiveshan will be paired with Summer Shibir 2021 along the theme of Guru Bhakti. We offer this Mukhpāṭh as a form of guru bhakti to our gurus Pramukh Swāmi Mahārāj and Mahant Swāmi Mahārāj. <br/><br/> Along with this, this Adhiveshan will also help us gear up for the upcoming Pramukh Swāmi Mahārāj Shatabdi Mahotsav and Aksharsham Mahotsav.',
        },
        {
            'question': 'Which Adhiveshan do I pledge for and which Summer Shibir do I go to?',
            'answer': 'You will pledge for the tiers in the group you currently are in (<b>as of January 2021</b>). For example, if you are in Group 2 in January of 2021, and even if you are graduating and moving to Group 3 in September 2021, you will pledge for Adhiveshan in the Group 2 categories. Anyone in Groups 1-3 ( as of January 2021) will also attend the <b>Bal/Balika Summer Shibir</b>. <br/><br/><b>NOTE</b>: Current 8th graders will pledge for the Kishore/Kishori Adhiveshan',
        },
        {
            'question': 'What does Adhiveshan consist of?',
            'answer': 'Adhiveshan will have three parts, each assessed in different ways and at different times throughout the spring and summer months: <br/> <ul> <li>The first part is the <b>Beginner’s Challenge</b> (traditionally known as Prāthmik Mukhpāṭh) which will be assessed at home.</li><li>The second part is the <b>Adhiveshan Rājipo Challenge</b> (traditionally known as Advance Mukhpāṭh), which will be assessed online (in real time - over a video conferencing platform).</li><li>The final part is the <b>Skills Challenge</b> (traditionally known as Talent Competitions), which will be judged through regional online submissions.</li></ul>',
        },
    ],
    'Website/App': [
      {
            'question': "Do I still need to pledge on BKMS if I pledge here?",
            'answer': "Yes. The website is a supporting tool to help balaks and balikas explore the Mukhpāṭh so that they can make an informed pledge. The pledge will be done through BKMS and the deadline is March 7th, 2021.",
      },
      {
            'question': "How can I change my password?",
            'answer': "<p>Go to the Settings Page</p><ul><li>Click on the 'Change Password' button.</li><li>Enter your current password.</li><li>Enter a new password.</li><li>Click 'Change Password' button to submit your new password.</li></ul>",
      },
      {
            'question': "What if I forgot my password?",
            'answer': "<p>Go to the login page.</p><ul><li>Click on 'Forgot Password?'</li><li>Enter your email address that you used to create an account.</li><li>Instructions to reset the password will then be sent to your email.</li><li>Follow the instructions sent to your email.</li></ul>",
      },
      {
            'question': "How can I edit my pledge?",
            'answer': "<p>Go to My Progress page.</p><ul><li>Click on Edit My Pledge.</li><li>Change your pledge.</li><li>Note: This won’t change your pledge on BKMS, which is where all official pledging takes place.</li></ul>",
      },
      {
            'question': "How can I reset my Mukhpāṭh progress?",
            'answer': "<p>Go to the Settings page.</p><ul><li>Click on Reset Memorized button</li</ul>",
      },
      {
            'question': "What if I have multiple users in my family but a limited number of devices?",
            'answer': "<p>We recommend that one user stay logged in via the app and another can use the mobile browser to login to the website.</p><p>Alternatively, you can log out each time someone needs to use the account.</p><p>We also recommend that parents print out small sections for kids to review on their own.</p><p>It’s not necessary to print out everything as the books will be provided around March.</p><ul><li>To print, please go to the “My Mukhpāṭh” tab and you will be able to click “Print My Mukhpāṭh” to print the Mukhpāṭh that you selected in the 'All Mukhpāṭh' tab.</li></ul>",
      },
      {
            'question': "How can I see the guided tutorials again for All Mukhpāṭh and My Mukhpāṭh pages?",
            'answer': "<p>Reset the tutorials to see them again. Go to the Settings tab, and click on the “Reset Tutorial” option.</p>",
      },
      {
            'question': "What if I used the wrong email to create an account?",
            'answer': "<p>You need to delete the account and recreate a new one with the right email if you have used the wrong email. To delete an account:</p><ul><li>Go to the Settings Page.</li><li>Click on Delete Account button.</li><li>Note: This will delete all of the data associated with your account.</li></ul>",
      },
      {
            'question': "What if I want to change my demographic info (name, mandal, group, etc)?",
            'answer': "<p>Unfortunately, there is no way to change demographic information except for your password. If something needs to be changed, please delete your account and create a new account.</p><ul><li>Go to the Settings Page</li><li>Click on Delete Account button</li><li>Note: This will remove all your activities on application.</li><li>Go to login page</li><li>Click on Create Account Button and create new account by selecting right group</li></ul>",
      },
      {
            'question': "Why do I see the wrong ‘bhai’ or ‘ben’ after my name?",
            'answer': "<p>You may find the wrong designation after your name if you selected the wrong group while creating your account. In that case, you should:</p><ul><li>Go to the Settings page</li><li>Click on Delete Account Button</li><li>Go to login page</li><li>Click on Create Account Button and create new account by selecting right group</li></ul>",
      },
      {
            'question': "What should I do if I find a bug? Is there any way I can reach out?",
            'answer': "<p>Go to the Settings page</p><ul><li>Click on the ‘Report Issue’ button and fill out the form with as much as details you can provide.</li></ul>",
      },
      {
            'question': "Can I bookmark more Mukhpāṭh cards than I pledged for?",
            'answer': "<p>Yes, you are free to bookmark as many items as you wish; however, we recommend only bookmarking items you are comfortable being tested on once the proctoring date comes.</p>",
      },
    ],
    'Beginner’s Challenge': [
        {
            'question': "What is the Beginner\'s Challenge?",
            'answer': 'The Beginners Challenge contains the core Mukhpāṭh of our sanstha, <b>including the Shri Swāminārāyaṇ Arti and shlokas we sing in puja</b>. All of the Mukhpāṭh comes with translations, so it is important to pay close attention to the meanings and try to introspect on how the values being transmitted in the words can be applied back to our lives. <br/><br/> The Beginners Challenge will be <b>administered at home</b>, wherein you all will complete a worksheet based on the <b>Gujarati transliteration and English translation</b> of the Mukhpāṭh. Your parents will aid in ensuring that you have completed the worksheet properly and assist in grading. <br/><br/> <b>NOTE</b>: Group 0 balaks/balikas will be exempt from the Beginner’s Challenge, however parents may choose to review this key Mukhpāṭh with their balaks/balikas.',
        },
    ],
    'Adhiveshan Rājipo Challenge': [
        {
            'question': "How is the Adhiveshan Rājipo Challenge structured?",
            'answer': 'The Adhiveshan Rājipo Challenge is broken up into 5 categories: Satsang Diksha, Swāmini Vāto, Kirtans, Shlokas and Sakhis, and Prasang Manan. <br/><br/> There are 4 tiers that you can choose from in each category: Mahant, Pramukh, Yogi, and Shastriji. <br/><br/> The breakdown for how much Mukhpāṭh you must memorize for each tier can be found under the “Edit My Pledge” section or in the FAQ section in your physical booket. You will also find a similar image to the one in your physical booklet below. <br/><br/> <b>NOTE</b>: There is an additional tier called the Ghanshyam tier that is ONLY if you are in Group 0. However, if you are in Group 1, you can select the Ghanshyam tier ONLY for Satsang Diksha (for the other categories, you must pick from the normal 4 tiers).',
        },
        {
            'question': "Is there a minimum number of tiers/categories needed to participate in the Adhiveshan?",
            'answer': 'As per Swāmishri’s ruchi (wish), the focus of this Adhiveshan is to learn, understand, and imbibe various satsang shastras in the lives of balaks and balikas. <br/><br/> Thus, there is <b>no mandatory minimum amount</b> of categories you need to pledge to be able to participate in the Adhiveshan. It is recommended that you pledge for 2 or more categories. <br/><br/> Although, you should still strive to pledge for as many categories as you can and push yourselves to strive for higher tiers to make Swāmishri extra raji.',
        },
        {
            'question': "Can we choose which items to memorize in each category?",
            'answer': '<b>The Satsang Diksha category is the only category that will have a set number of shlokas for each tier</b>. For example if you choose the Mahant Challenge for the Satsang Diksha category, there will be a pre-set list of 64 shlokas.<br/><br/> For all of the other categories (Swāmini Vāto, Shloka/Sakhi, Kirtan, Prasang Manan), you will have a choice in creating your own set with the available list of Mukhpāṭh</b>. For example, if you are a Group 1 balak or balika who wants to do the Yogi challenge for Kirtans, you will be able to choose any 4 out of a possible list of 15 kirtans listed in the book. ',
        },
        {
          'question': "What if I have already started or want to memorize the Satsang Diksha shlokas in Sanskrit?",
          'answer': "<ol><li>If you have only memorized the Sanskrit shlokas, you will be tested in Sanskrit.  You do not need to memorize them in Gujarati, but still need to  explain the meaning in English (paraphrasing is allowed).</li><li>If you have memorized in Sanskrit and in either English or Gujarati and would like to be tested in Sanskrit, we  can do that as well. Please contact your local karyakar and notify them that you would like to be tested in Sanskrit. They will ask for your Full name, Center, Contact Number and BKMS ID.</li></ol>"
        },
    ],
    'Skills Challenge': [
        {
            'question': "What is the Skills Challenge?",
            'answer': 'The Skills Challenge allows you to tie your passions and hobbies back to Satsang. You will have a chance to show your talents in a multitude of fashions included in the Mukhpāṭh booklet. You will be able to <b>choose a minimum of 1 and a maximum of 3 skills challenges.</b><br/><br/><b>NOTE:</b> Group 0 balaks/balikas will not participate in Skills Challenge.<br/><br/>More details on the rules and regulations for each of the specific skills challenges will be provided shortly.',
        },
    ],
    'Adhiveshan Pledging': [
        {
            'question': "How can I pledge for Adhiveshan?",
            'answer': 'You will be able to pledge for Adhiveshan through BKMS after the Launch Sabha at the end of January. You will be able to access this link and must submit your final pledges <b>by 3/7/21</b>.<br/><br/>Before this date, please read through the Adhiveshan book or visit the website to take a look at the tiers for your group to make a decision on what Mukhpāṭh you will be able to memorize by the summer.<br/><br/>NOTE: If you pledge for Satsang Diksha, you should try to continue with the tier you chose for your Rājipo Challenge from August 2020. If you would like to change it, there will be an opportunity for you to repledge your original Satsang Diksha pledge when you pledge for the other Adhiveshan categories.',
        },
        {
            'question': "Will there be additional material to help me study?",
            'answer': 'Along with the provided book, there will be additional material provided via a website including interactive aids to help memorize the Adhiveshan content. (Please ask you parents prior to creating an account on the website.)<br/><br/>Once you enter your information to sign-up for an account, you will be able to access Mukhpāṭh and pledge a tier for each category based on the group/grade you entered. This website is for your <b>personal use</b> in being able to memorize the Mukhpāṭh wherever you go! You can bookmark which Mukhpāṭh you want to memorize, listen to the audio, or even print it out!<br/><br/><b>NOTE: Pledging on the website does not replace pledging on BKMS. You must register and pledging on BKMS before 3/7/21.</b><br/><br/>As additional content is rolled out for Adhiveshan and SS21, you will be able to see the updates on the website dashboard and your local karyakars will provide you with updates.'
        },
    ],
    'Adhiveshan Timeline': [
        {
            'question': "What are some important dates to keep in mind relating to the Adhiveshan?",
            'answer': "<ul><li>Adhiveshan/Summer Shibir 2021 Launch Sabha: 1/31/2021</li><li>Adhiveshan Pledge and Summer Shibir Registration: 1/31/2021-3/7/2021</li><li>Beginners Challenge Quiz: TBD</li><li>Adhiveshan Rājipo Challenge: TBD</li><li>Skills Challenge Submission Deadline: TBD</li></ul><b>More information on specific dates, judging process, submission process, etc. will be provided to you by your local karyakars. If you have any questions, please contact your local karyakars.</b>",
        },
    ],
    'Summer Shibir': [
      {
            'question': "What is Summer Shibir",
            'answer': 'This summer, a one-day virtual Summer Shibir will be held on the theme of “Guru Bhakti.” Since you memorized Mukhpāṭh as a form of guru bhakti, this shibir will revolve around better understanding and loving our guru.<br/><br/>There will be a main Bal/Balika Shibir as well as a separate shibir for Group 0 balaks/balikas. The breakdown is as follows:<br/><br/>Those entering Grades 2-8 in Fall of 2022 will participate in the Bal/Balika Summer Shibir. Those entering Group 0 - Grade 1 in Fall of 2022 will participate in the Group 0 Shibir. <br/><br/> NOTE: This is the same breakdown as Adhiveshan.<br/><br/>More information on Summer Shibir 2021 will be provided at a later time.'
      }
    ]
}

KISHORE_FAQ = {
  'Adhiveshan Overview': [
    {
      'question': "What is this year’s shibir theme and how does it relate to Adhiveshan?",
      'answer': "This year’s shibir theme is Guru Bhakti. Understanding how to perform guru bhakti the same way our gurus have will be the primary focus of the shibir. One way to perform guru bhakti is to memorize and learn Mukhpāṭh with the thought of raajipano vichar. Thus, this adhiveshan is a way to show our guru bhakti and earn our guru’s Rājipo."
    },
    {
      'question': "What is Adhiveshan?",
      'answer': "Adhiveshan has been very dear to the hearts of our Gurus. Starting with Yogi Bapa’s passion for balaks and kishores to memorize Mukhpāṭh during their summer vacations to the various adhiveshans held with Pramukh Swāmi Mahārāj and Mahant Swāmi Mahārāj, Mukhpāṭh has been integral way for kishores and kishoris to earn the Rājipo of their gurus. Adhiveshan is a structured way of memorizing Mukhpāṭh which is often focused on a certain Satsang topic or theme. Adhiveshan is NOT a competition, but rather a challenge for ourselves to spend time memorizing the Mukhpāṭh, learning its meaning, and eventually imbibing it in our lives to please our gurus."
    },
    {
      'question': "How is the Adhiveshan structured?",
      'answer': "All components of adhiveshan will take place virtually this year. There will be four components to adhiveshan: the Prāthmik Mukhpāṭh, the Rājipo Challenge, the Guru Bhakti Challenge, and Skills Competitions."
    },
    {
      'question': "How will Adhiveshan testing work?",
      'answer': "Due to the current situation with the COVID-19 pandemic, Adhiveshan will also take place over a virtual setting. Weeks prior to the shibir, karyakars will join individual calls to test kishores and kishoris on their Mukhpāṭh as it is traditionally done during an in-person adhiveshan."
    },
  ],
     'Website/App': [
      {
            'question': "Do I still need to pledge on BKMS if I pledge here?",
            'answer': "Yes. The website is a supporting tool to help kishores and kishoris explore the Mukhpāṭh so that they can make an informed pledge. The pledge will be done through BKMS and the deadline is March 7th, 2021.",
      },
      {
            'question': "How can I change my password?",
            'answer': "<p>Go to the Settings Page</p><ul><li>Click on the 'Change Password' button.</li><li>Enter your current password.</li><li>Enter a new password.</li><li>Click 'Change Password' button to submit your new password.</li></ul>",
      },
      {
            'question': "What if I forgot my password?",
            'answer': "<p>Go to the login page.</p><ul><li>Click on 'Forgot Password?'</li><li>Enter your email address that you used to create an account.</li><li>Instructions to reset the password will then be sent to your email.</li><li>Follow the instructions sent to your email.</li></ul>",
      },
      {
            'question': "How can I edit my pledge?",
            'answer': "<p>Go to My Progress page.</p><ul><li>Click on Edit My Pledge.</li><li>Change your pledge.</li><li>Note: This won’t change your pledge on BKMS, which is where all official pledging takes place.</li></ul>",
      },
      {
            'question': "How can I reset my Mukhpāṭh progress?",
            'answer': "<p>Go to the Settings page.</p><ul><li>Click on Reset Memorized button</li</ul>",
      },
      {
            'question': "What if I have multiple users in my family but a limited number of devices?",
            'answer': "<p>We recommend that one user stay logged in via the app and another can use the mobile browser to login to the website.</p><p>Alternatively, you can log out each time someone needs to use the account.</p><p>We also recommend that parents print out small sections for kids to review on their own.</p><p>It’s not necessary to print out everything as the books will be provided around March.</p><ul><li>To print, please go to the “My Mukhpāṭh” tab and you will be able to click “Print My Mukhpāṭh” to print the Mukhpāṭh that you selected in the 'All Mukhpāṭh' tab.</li></ul>",
      },
      {
            'question': "How can I see the guided tutorials again for All Mukhpāṭh and My Mukhpāṭh pages?",
            'answer': "<p>Reset the tutorials to see them again. Go to the Settings tab, and click on the “Reset Tutorial” option.</p>",
      },
      {
            'question': "What if I used the wrong email to create an account?",
            'answer': "<p>You need to delete the account and recreate a new one with the right email if you have used the wrong email. To delete an account:</p><ul><li>Go to the Settings Page.</li><li>Click on Delete Account button.</li><li>Note: This will delete all of the data associated with your account.</li></ul>",
      },
      {
            'question': "What if I want to change my demographic info (name, mandal, group, etc)?",
            'answer': "<p>Unfortunately, there is no way to change demographic information except for your password. If something needs to be changed, please delete your account and create a new account.</p><ul><li>Go to the Settings Page</li><li>Click on Delete Account button</li><li>Note: This will remove all your activities on application.</li><li>Go to login page</li><li>Click on Create Account Button and create new account by selecting right group</li></ul>",
      },
      {
            'question': "Why do I see the wrong ‘bhai’ or ‘ben’ after my name?",
            'answer': "<p>You may find the wrong designation after your name if you selected the wrong group while creating your account. In that case, you should:</p><ul><li>Go to the Settings page</li><li>Click on Delete Account Button</li><li>Go to login page</li><li>Click on Create Account Button and create new account by selecting right group</li></ul>",
      },
      {
            'question': "What should I do if I find a bug? Is there any way I can reach out?",
            'answer': "<p>Go to the Settings page</p><ul><li>Click on the ‘Report Issue’ button and fill out the form with as much as details you can provide.</li></ul>",
      },
      {
            'question': "Can I bookmark more Mukhpāṭh cards than I pledged for?",
            'answer': "<p>Yes, you are free to bookmark as many items as you wish; however, we recommend only bookmarking items you are comfortable being tested on once the proctoring date comes.</p>",
      },
    ],
  'Prāthmik Mukhpāṭh': [
    {
      'question': 'What is Prāthmik Mukhpāṭh?',
      'answer': "The Prāthmik Mukhpāṭh contains core Mukhpāṭh that kishores and kishoris encounter on a daily basis. All of the Mukhpāṭh comes with translations, so it is important to pay close attention, understand the meanings, and try to introspect on how the values being transmitted in the words can be applied back to our lives. The Prāthmik Mukhpāṭh for this year includes the Shri Swāminārāyaṇ Arti and the two puja shlokas provided in Satsang Diksha. Kishores and kishoris will be tested on the Prāthmik Mukhpāṭh, just like both Mukhpāṭh challenges."
    }
  ],
  'Rājipo Challenge': [
    {
      'question': "What is the Rājipo Challenge and how is it structured?",
      'answer': "The Adhiveshan Rājipo Challenge is one that kishore and kishoris have been working on since August 2020: the Satsang Diksha Rājipo Challenge. The Rājipo Challenge for the adhiveshan will test memorization and understanding of Satsang Diksha as well as encourage kishores and kishoris to further memorize Satsang Diksha as it is Swāmishri’s inner wish. The tiering will work exactly the same as the current Rājipo Challenge."
    },
    {
      'question': "Should the current Rājipo Challenge (Satsang Diksha) be continued?",
      'answer': "Kishores and kishoris are encouraged to continue on with their Satsang Diksha Rājipo Challenge pledge. However, kishores and kishoris will have the opportunity to re-pledge beginning January 31st, 2021 if they’d like. The pledging will occur in the same fashion as it had been previously, with the four tiers being the same (Mahant, Pramukh, Yogiji, Shastri). Final pledging closes March 7th, 2021."
    },
    {
      'question': "What if I have already started or want to memorize the Satsang Diksha shlokas in Sanskrit?",
      'answer': "<ol><li>If you have only memorized the Sanskrit shlokas, you will be tested in Sanskrit.  You do not need to memorize them in Gujarati, but still need to  explain the meaning in English (paraphrasing is allowed).</li><li>If you have memorized in Sanskrit and in either English or Gujarati and would like to be tested in Sanskrit, please contact your local karyakar and notify them that you would like to be tested in Sanskrit. They will ask for your Full name, Center, Contact Number and BKMS ID.</li></ol>"
    },
  ],
  'Guru Bhakti Challenge': [
    {
      'question': 'What is the Guru Bhakti Challenge?',
      'answer': "The Adhiveshan Guru Bhakti Challenge exists in the form of topic-based modules with relevant Mukhpāṭh items in each module. The Guru Bhakti Challenge will have four tiers that delegates can choose to achieve: Bronze, Silver, Gold, and Platinum. The distinction between these tiers is solely based on the number of modules a delegate completes — 5 for bronze, 10 for silver, 15 for gold, and 20 for platinum. Specifically, each module will consist of Swāmini Vāto, Vachanamrut Quotations, Shloks/Sakhis, Satsang Diksha shloks, Kirtans, Prasangs, or other Mukhpāṭh organized under a unifying Satsang topic. In order to consider a module completed, a kishore or kishori must memorize any 4 out of the 10 items of Mukhpāṭh within the module. We hope that this freedom in selecting Mukhpāṭh will incentivize kishores and kishoris to memorize according to their personal interests."
    }
  ],
  'Skill Competitions': [
    {
      'question': "What are the Skills Competitions?",
      'answer': "The Skills Competitions allow kishores and kishoris to tie their passions and hobbies back to Satsang. Kishores and kishoris will have a chance to show their talents in a multitude of manners. There is an enormous pool of skills to choose from and no limit, so feel free to try something new! More information regarding the skills competitions will come in a future installment."
    },
    {
      'question': "How will the Skills Competitions work?",
      'answer': "Due to the current situation with the COVID-19 pandemic, the Skills Competitions will also take place over a virtual setting. We will request kishores and kishoris to submit their performance, art, recordings, etc. to a centralized, regional link prior to the shibir. This will allow for judges to assess each submission individually and offer awards in time for the awards ceremony."
    },
  ],
  'Pledging': [
    {
      'question': "How will kishores and kishoris be able to pledge for Adhiveshan?",
      'answer': "Kishores and kishoris will be able to pledge for Adhiveshan via BKMS after the Launch Sabha on January 31st, 2021. They will be able to access this link until March 7th, 2021. By this final date, kishores and kishoris must submit their pledges."
    },
    {
      'question': "Is there a minimum amount of Mukhpāṭh needed to participate in the Adhiveshan?",
      'answer': "As per Swāmishri’s ruchi, the focus of this Adhiveshan is to learn, understand, and imbibe various Satsang Mukhpāṭh in the lives of kishores and kishoris. Thus, outside of the Prāthmik Mukhpāṭh, there is no mandatory minimum amount of Mukhpāṭh that a particular kishore or kishori needs to pledge to be able to participate in the Adhiveshan. Although, karyakars should encourage kishores and kishoris to pledge for as much Mukhpāṭh as they can based on their time and ability."
    },
    {
      'question': "Can a kishore or kishori change their pledge mid-way?",
      'answer': "Kishores and kishoris will not be able to change their pledge after they have submitted their pledge. That being said, they will have from January 31st, 2021 (launch sabha day) to March 7th to select their pledge. Karyakars should encourage and follow-up with kishores and kishoris during these 5 weeks to take a glance at the Adhiveshan book and make a careful decision on what they will be able to memorize by the summer."
    },
    {
      'question': "Will a booklet and material be provided?",
      'answer': "All Mukhpāṭh content will be available via a website and mobile app. The website and mobile app will also include interactive aids and quizzes to help memorize the Mukhpāṭh. A hard-copy of the Mukhpāṭh booklet will be provided to kishores and kishoris sometime in March."
    },
  ],
  'Summer Shibir Overview': [
    {
      'question': "How will Summer Shibir be structured? Will it be virtual?",
      'answer': "Due to the current situation with the COVID-19 pandemic, Summer Shibir 2021 will take place on a virtual platform. The Kishore-Kishori shibir will take place over two days during one weekend. The shibir will happen toward the end of the summer. There will still be traditional programming, which includes common sessions, and group goshthis, but it will all take place over a virtual setting."
    },
  ],
  'Upcoming Dates': [
    {
      'question': "What are some important dates to keep in mind relating to the Adhiveshan?",
      'answer': """
        <ion-grid class="ion-text-center">
          <ion-row>
            <ion-col size="6">
              <ion-text>
                Pledging and Registration
              </ion-text>
            </ion-col>
            <ion-col size="6">
              <ion-text>
                January 31st to March 7th, 2021
              </ion-text>
            </ion-col>
          </ion-row>
          <ion-row>
            <ion-col size="6">
              <ion-text>
                Adhiveshan Testing
              </ion-text>
            </ion-col>
            <ion-col size="6">
              <ion-text>
                July-August
              </ion-text>
            </ion-col>
          </ion-row>
          <ion-row>
            <ion-col size="6">
              <ion-text>
                Skills Competition Submission Deadline
              </ion-text>
            </ion-col>
            <ion-col size="6">
              <ion-text>
                July-August
              </ion-text>
            </ion-col>
          </ion-row>
          <ion-row>
            <ion-col size="6">
              <ion-text>
                Local Award Ceremony
              </ion-text>
            </ion-col>
            <ion-col size="6">
              <ion-text>
                August-September 2021
              </ion-text>
            </ion-col>
          </ion-row>
        </ion-grid>
      """
    },
    {
      'question': "When is the Kishore-Kishori Shibir?",
      'answer': "The Kishore/Kishori Summer Shibir 2021 will take place in early September of this year."
    },
  ],
  'Miscellaneous': [
    {
      'question': "When and how will kishores and kishoris receive awards?",
      'answer': "After adhiveshan testing is complete, centers will hold local awards ceremonies to recognize the achievements of kishores and kishoris. These will be scheduled by local centers to provide flexibility. Details about the distribution of awards and the local awards ceremony will be provided by the regional karyakar team."
    },
    {
      'question': "Who is eligible to participate in the Adhiveshan and Summer Shibir?",
      'answer': "High schoolers and college students will be participating in this year's Virtual Summer Shibir and Virtual Adhiveshan. It is important to note that graduating eighth graders as well as graduating college seniors will have the opportunity to participate in both the Kishore Adhiveshan and Summer Shibir - 8th graders will not take part in either the Bal/Balika Shibir or Adhiveshan."
    },
  ],
}

# Skills Challenge for BM
BAL_SKILLS_CHALLENGE = {
    'Story/Speech-Based Competitions': {
        'Mono-acting': """<div class="skills-html">
<h2 class="static-content-title">Rules</h2>
<ul> 
	<li>
    Participants can choose to enact any one scene of their choice, or select one from the
    list below.
	</li>
	<li>Each participant will have 4 to 7 minutes to enact the scene.</li>
	<li>The act must be memorized. Notes will not be allowed</li>
  <li>
    Participants may perform in either Gujarati or English, whichever suits them best. No
    bonus points will be given for performing in Gujarati.
	</li>
	<li>
    Participants must record their drama in good lighting and on a good camera (either on
    a smartphone or webcam). Audio must be clear. Participants are encouraged to use
    props  
  </li>
  <li>
    You will take on the role of one person from the scene (for most scenes this is provided),
    and enact the scene from that person's point of view.
  </li>
  <li>
    Balaks must choose the bal characters and balikas must choose the balika character list.
  </li>
  <li>
    Mono-acting will be judged on: accurate portrayal of the incident, acting, tone,
    emotion, facial expressions, memorization, props/costume/creativity.
  </li>
  <li>
    Scripts for the sample scenes below can be downloaded from <a href="https://baps.box.com/s/dzllyk7qr1f8ia7583x9lxtwew96yl0r" target="_blank">here</a>.
  </li>
</ul>
<h2 class="static-content-title">Sample Scenes</h2>
<ion-grid class="ion-text-center">
  <ion-row class="header-row">
    <ion-col size="2">
      <ion-text>#</ion-text>
    </ion-col>
    <ion-col size="5">
      <ion-text>Bal Characters</ion-text>
    </ion-col>
    <ion-col size="5">
      <ion-text>Balika Characters</ion-text>
    </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        1
      </ion-text>
    </ion-col>
      <ion-col size="5">
        <ion-text>
          Krishna
        </ion-text>
      </ion-col>
      <ion-col size="5">
        <ion-text>
          Jivuba
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        2
      </ion-text>
    </ion-col>
      <ion-col size="5">
        <ion-text>
          Joban Pagi
        </ion-text>
      </ion-col>
      <ion-col size="5">
        <ion-text>
          Jamkuba
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        3
      </ion-text>
    </ion-col>
      <ion-col size="5">
        <ion-text>
          Arjun
        </ion-text>
      </ion-col>
      <ion-col size="5">
        <ion-text>
          Suvasinibhabhi
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        4
      </ion-text>
    </ion-col>
      <ion-col size="5">
        <ion-text>
          Sagram Vaghri
        </ion-text>
      </ion-col>
      <ion-col size="5">
        <ion-text>
          Mirabai
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        5
      </ion-text>
    </ion-col>
    <ion-col size="5">
      <ion-text>
        Shravan
      </ion-text>
    </ion-col>
    <ion-col size="5">
      <ion-text>
        Sitaji
      </ion-text>
    </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        6
      </ion-text>
    </ion-col>
      <ion-col size="10">
        <b>Pick Your Own!</b>
    </ion-col>
  </ion-row>
</ion-grid>
<div>""",
        'Storytelling': """<div class="skills-html">
<h2 class="static-content-title">Rules</h2>
<ul>
	<li>
    Participants must speak on one of Yogiji Maharaj’s Bodh Katha. Participants can choose
    any bodh katha from the book, 101 Tales of Wisdom  
  </li>
  <ul>
    <li>
      If you do not have the book, a short version can be found at
      <a href="http://www.swaminarayan.org/yogijimaharaj/talesofwisdom/" target="_blank">http://www.swaminarayan.org/yogijimaharaj/talesofwisdom/.</a>
    </li>
  </ul>
	<li>
    Participants must tell the story in its entirety, as well as provide a manan, or reflection,
    on the importance of the story.
  </li>
	<li>
    Participants should take between 5 to 7 minutes for their story and manan or reflection.	</li>
	<li>
    The story must be memorized. Notes will not be allowed.
  </li>
  <li>
    Participants may perform in either Gujarati or English, whichever suits them best. We
    suggest that you perform in the language that you are most comfortable and fluent in.
  </li>
  <li>
    Participants must record their story in good lighting and on a good camera (either on a
    smartphone or webcam). Balaks should wear a jhabo-lengho and balikas should wear a
    punjabi.
  </li>
  <li>
    Recording should be done in a single take with no edits. Video stitching will result in
    disqualification.
  </li>
  <li>
    Storytelling will be judged on: storytelling ability, content, manan/personal reflection,
    gestures, organization, flow, confidence, tone, time.
  </li>
</ul>
<h2 class="static-content-title">Sample Story List</h2>
<ion-grid class="ion-text-center">
  <ion-row class="header-row">
    <ion-col size="2">
      <ion-text>#</ion-text>
    </ion-col>
    <ion-col size="10">
      <ion-text>Bodh Katha</ion-text>
    </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        1
      </ion-text>
    </ion-col>
      <ion-col size="10">
        <ion-text>
          Lindyo
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        2
      </ion-text>
    </ion-col>
      <ion-col size="10">
        <ion-text>
          A Quiver of Arrows
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        3
      </ion-text>
    </ion-col>
      <ion-col size="10">
        <ion-text>
          Tukaram and Naradji
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        4
      </ion-text>
    </ion-col>
      <ion-col size="10">
        <ion-text>
          The Sesame Seed Scholar
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        5
      </ion-text>
    </ion-col>
      <ion-col size="10">
        <ion-text>
          The Lazy Man
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        6
      </ion-text>
    </ion-col>
      <ion-col size="10">
        <ion-text>
          <b>Pick your Own!</b>
        </ion-text>
      </ion-col>
  </ion-row>
</ion-grid>
<div>""",
        'Satsang Diksha Nirupan': """<div class="skills-html">
<h2 class="static-content-title">Rules</h2>
<ul>
	<li>
    Participants will select a Satsang Diksha shloka and perform a nirupan on that shloka.
    Sample shlokas related to a theme are provided for guidance.
  </li>
  <li>The nirupan should done in this order:</li>
  <ul>
	  <li>Begin by reciting the Satsang Diksha Shloka that you have chosen</li>
	  <li>
	    Explain the meaning of the shloka and how it relates with the theme given in the
      table
	  </li>
    <li>
      Use at least one prasang of Pramukh Swami Maharaj or Mahant Swami Maharaj
      that relates to the theme and the meaning of the shloka
    </li>
    <li>
      Provide your manan or personal reflection of the shloka and how you can imbibe
      it in your life
    </li>
  </ul>
  <li>
    Participants should take between 5 to 7 minutes for their nirupan.  
  </li>
	<li>
    Participants may use a notecard to help them with the nirupan.
	</li>
  <li>
    Participants may perform in either Gujarati or English, whichever suits them best. No
    bonus points will be given for performing in Gujarati.
  </li>
  <li>
    Participants must record their nirupan in good lighting and on a good camera (either on
    a smartphone or webcam). Balaks should wear a jhabo-lengho and balikas should wear
    a punjabi.
  </li>
  <li>
    Parents may help in preparation of the nirupan.
  </li>
  <li>
    Nirupan will be judged on: messaging, correct explanation of shlok, accurate use of
    mukhpath and prasangs, organization, flow, confidence, tone, time.
  </li>
</ul>
<h2 class="static-content-title">Themes</h2>
<ion-grid class="ion-text-center">
  <ion-row class="header-row">
    <ion-col size="2">
      <ion-text>#</ion-text>
    </ion-col>
    <ion-col size="5">
      <ion-text>Example Shlokas</ion-text>
    </ion-col>
    <ion-col size="5">
      <ion-text>Theme</ion-text>
    </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        1
      </ion-text>
    </ion-col>
      <ion-col size="5">
        <ion-text>
          Shlokas 79-95 
        </ion-text>
      </ion-col>
      <ion-col size="5">
        <ion-text>
          Importance of a Mandir
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        2
      </ion-text>
    </ion-col>
      <ion-col size="5">
        <ion-text>
         Shlokas 96-115
        </ion-text>
      </ion-col>
      <ion-col size="5">
        <ion-text>
          Akshar-Purushottam Darshan
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        3
      </ion-text>
    </ion-col>
      <ion-col size="5">
        <ion-text>
          Shlokas 209-215
        </ion-text>
      </ion-col>
      <ion-col size="5">
        <ion-text>
          Being an Ideal Child
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        4
      </ion-text>
    </ion-col>
      <ion-col size="5">
        <ion-text>
          Shlokas 216-234
        </ion-text>
      </ion-col>
      <ion-col size="5">
        <ion-text>
          Sang vs. Kusang
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        5
      </ion-text>
    </ion-col>
      <ion-col size="5">
        Shlokas 287-298 
      </ion-col>
      <ion-col>
        Importance of Agna and Upasana
      </ion-col>
  </ion-row>
</ion-grid>
<div>""",
        'Prasang-Varnan': """<div class="skills-html">
<h2 class="static-content-title">Rules</h2>
<ul>
	<li>
    Participants will elaborate on a prasang and provide a manan, or personal reflection, on
    the prasang by using 1 mukhpath references that they had memorized. The prasang can
    be from, but not limited to, the prasang mukhpath section in the Rajipo Challenge.
	</li>
  <li>
    If a prasang is not chosen from the Adhiveshan Rajipo Challenge, please name the
    source in your speech, such as kids.baps.org or Eternal Virtues.
  </li>
	<li>The prasang-varnan should include at least:</li>
  <ul>
	  <li>
      1 key prasang
	  </li>
	  <li>
      1 Mukhpāṭh reference
    </li>
    <li>
      A personal manan (analysis/reflection)
    </li>
  </ul>
  <li>
    Participants should take between 5 to 7 minutes for their prasang-varnan.
  </li>
  <li>
    The prasang-varnan must be memorized. Notes will not be allowed.
  </li>
  <li>
    Participants may perform in either Gujarati or English, whichever suits them best. No
    bonus points will be given for performing in Gujarati.
  </li>
  <li>
    Participants must record their prasang-varnan in good lighting and on a good camera
    (either on a smartphone or webcam). Balaks should wear a jhabo-lengho and balikas
    should wear a punjabi.
  </li>
  <li>
    Prasang-varnan will be judged on: key prasang, manan or personal reflection, accurate
    use of mukhpath, memorization, organization, flow, confidence, tone, time.
  </li> 
  <li>
    Prasangs for the sample list below can be downloaded from <a href="https://baps.box.com/s/xd99qhk1bp3lo40rsxw6img218rqkide" target="_blank">here</a>
  </li>
</ul>
<h2 class="static-content-title">Sample Prasangs</h2>
<ion-grid class="ion-text-center">
  <ion-row class="header-row">
    <ion-col size="2">
      <ion-text>#</ion-text>
    </ion-col>
    <ion-col size="10">
      <ion-text>Prasangs</ion-text>
    </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        1
      </ion-text>
    </ion-col>
      <ion-col size="10">
        <ion-text>
          Satyam (Truth)
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        2
      </ion-text>
    </ion-col>
      <ion-col size="10">
        <ion-text>
          Titiksha (Tolerance)
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        3
      </ion-text>
    </ion-col>
      <ion-col size="10">
        <ion-text>
          Anahamkrutihi (Humility)
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        4
      </ion-text>
    </ion-col>
      <ion-col size="10">
        <ion-text>
          Astikyam (Faith in God)
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        5
      </ion-text>
    </ion-col>
      <ion-col size="10">
        <ion-text>
          Smrutihi (Remembrance)
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        6
      </ion-text>
    </ion-col>
      <ion-col size="10">
        <ion-text>
          <b>Pick Your Own!</b>
        </ion-text>
      </ion-col>
  </ion-row>
</ion-grid>
<div>""",
    },
    'Music-Based Competitions': {
        'Solo Singing': """<div class="skills-html">
<h2 class="static-content-title">Rules</h2>
<ul>
	<li>
    You may perform any kirtan from the Kirtan Muktavali. Select any bhajan that you feel
    you resonate strongly with!
  <li>
    Participants may use any other instruments to accompany them during their
    performance, but they will only be graded on the singing and not the use of
    instruments.
  </li>
	<li>
    Participants must record their singing in good lighting and on a good camera (either on
    a smartphone or webcam). Balaks should wear a jhabo-lengho and balikas should wear
    a punjabi.
  </li>
  <li>
    Participants will have a maximum of 8 minutes 
  </li>
  <li>
    Participants are allowed to cut lines if the selected bhajan is long and exceeds the time
    given.  
  </li>
  <li>
    You will be judged on: sur (melody), tempo/rhythm, and tone/voice, creativity, time.
  </li>
  <li>
    Kirtans can be selected and practiced by using the <a href="https://www.anirdesh.com/kirtan/" target="_blank">Anirdesh Website</a> or Akshar
    Amrutam app.
  </li>
</ul>
<h2 class="static-content-title">Sample Bhajans</h2>
<ion-grid class="ion-text-center">
  <ion-row class="header-row">
    <ion-col size="2">
      <ion-text>#</ion-text>
    </ion-col>
    <ion-col size="5">
      <ion-text>Bhajan Name</ion-text>
    </ion-col>
    <ion-col size="5">
      <ion-text>CD Album</ion-text>
    </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        1
      </ion-text>
    </ion-col>
      <ion-col size="5">
        <ion-text>
          Sant Param Hitkari
        </ion-text>
      </ion-col>
      <ion-col size="5">
        <ion-text>
          Sant Param Hitkari - 2
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        2
      </ion-text>
    </ion-col>
      <ion-col size="5">
        <ion-text>
         Tamari Murti Vina
        </ion-text>
      </ion-col>
      <ion-col size="5">
        <ion-text>
          Prarthana
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        3
      </ion-text>
    </ion-col>
      <ion-col size="5">
        <ion-text>
          Bhulish Hu Jagatni Maya 
        </ion-text>
      </ion-col>
      <ion-col size="5">
        <ion-text>
          Bhakti Vihar
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        4
      </ion-text>
    </ion-col>
      <ion-col size="5">
        <ion-text>
          Jivu Chhu Rasila Tara
        </ion-text>
      </ion-col>
      <ion-col size="5">
        <ion-text>
          Murti Pyari Re
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        5
      </ion-text>
    </ion-col>
      <ion-col size="5">
        Ame Sau Swāmīnā Bālak
      </ion-col>
      <ion-col>
        Bhakti Vihar
      </ion-col>
  </ion-row>
   <ion-row>
    <ion-col size="2">
      <ion-text>
        6
      </ion-text>
    </ion-col>
      <ion-col size="5">
        <ion-text>
          Chho Ji Amāru Jīvan
        </ion-text>
      </ion-col>
      <ion-col size="5">
        <ion-text>
          Namie Narayanswarup
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        7
      </ion-text>
    </ion-col>
      <ion-col size="5">
        <ion-text>
          Vahetu Jīvan Tamāru Gangānī Dhārā
        </ion-text>
      </ion-col>
      <ion-col size="5">
        <ion-text>
          Pramukh Vandana
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        8
      </ion-text>
    </ion-col>
      <ion-col size="5">
        <ion-text>
          Joi Murti Manohar Tari
        </ion-text>
      </ion-col>
      <ion-col size="5">
        <ion-text>
          Murti Manohar Tari
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        9
      </ion-text>
    </ion-col>
      <ion-col size="5">
        <ion-text>
          He Jī Me To Harkhe Nihalyā Nāth
        </ion-text>
      </ion-col>
      <ion-col size="5">
        <ion-text>
          Amrut Ni Heli
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        10
      </ion-text>
    </ion-col>
      <ion-col size="10">
        <ion-text>
          <b>Pick Your Own!</b>
        </ion-text>
      </ion-col>
  </ion-row>
</ion-grid>
<div>""",
        'Musical Instruments': """<div class="skills-html">
<h2 class="static-content-title">Rules</h2>
<ul>
	<li>
    Participants can perform to any bhajan or can showcase their skills by performing solo
    musical pieces.
  </li>  
  <li>
    Participants must specify which instrument they are going to play including, but not
    limited to, piano, tabla, flute, trumpet, violin, harmonium, etc.
  </li>
	<li>
    Participants do not have to memorize the bhajan. They can have sheet music in front of
    them while they play.  
  </li>
	<li>
    Participants will have a maximum of 8 minutes.
	</li>
  <li>
    Participants may have other instrumentalists or singers accompany them during their
    performance, but they will only be graded on their own performance  
  </li>
  <li>
    If participants choose a percussion instrument where the melody cannot be found, such
    as tabla, please have the bhajan audio playing in the background while the participant
    plays.
  </li>
  <li>
    Participants must record their performance in good lighting and on a good camera
    (either on a smartphone or webcam). Balaks should wear a jhabo-lengho and balikas
    should wear a punjabi.
  </li>
  <li>
    You will be judged on: tempo/rhythm, accuracy, tonality, creativity, time.
  </li>
  <li>
    Kirtans can be selected and practiced by using the <a href="https://www.anirdesh.com/kirtan/" target="_blank">Anirdesh Website</a> or Akshar
    Amrutam app.
  </li>
</ul>
<h2 class="static-content-title">Sample Bhajans</h2>
<ion-grid class="ion-text-center">
  <ion-row class="header-row">
    <ion-col size="2">
      <ion-text>#</ion-text>
    </ion-col>
    <ion-col size="5">
      <ion-text>Bhajan Name</ion-text>
    </ion-col>
    <ion-col size="5">
      <ion-text>CD Album</ion-text>
    </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        1
      </ion-text>
    </ion-col>
      <ion-col size="5">
        <ion-text>
          Sant Param Hitkari
        </ion-text>
      </ion-col>
      <ion-col size="5">
        <ion-text>
          Sant Param Hitkari - 2
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        2
      </ion-text>
    </ion-col>
      <ion-col size="5">
        <ion-text>
         Tamari Murti Vina
        </ion-text>
      </ion-col>
      <ion-col size="5">
        <ion-text>
          Prarthana
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        3
      </ion-text>
    </ion-col>
      <ion-col size="5">
        <ion-text>
          Bhulish Hu Jagatni Maya 
        </ion-text>
      </ion-col>
      <ion-col size="5">
        <ion-text>
          Bhakti Vihar
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        4
      </ion-text>
    </ion-col>
      <ion-col size="5">
        <ion-text>
          Jivu Chhu Rasila Tara
        </ion-text>
      </ion-col>
      <ion-col size="5">
        <ion-text>
          Murti Pyari Re
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        5
      </ion-text>
    </ion-col>
      <ion-col size="5">
        Ame Sau Swāmīnā Bālak
      </ion-col>
      <ion-col>
        Bhakti Vihar
      </ion-col>
  </ion-row>
   <ion-row>
    <ion-col size="2">
      <ion-text>
        6
      </ion-text>
    </ion-col>
      <ion-col size="5">
        <ion-text>
          Chho Ji Amāru Jīvan
        </ion-text>
      </ion-col>
      <ion-col size="5">
        <ion-text>
          Namie Narayanswarup
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        7
      </ion-text>
    </ion-col>
      <ion-col size="5">
        <ion-text>
          Vahetu Jīvan Tamāru Gangānī Dhārā
        </ion-text>
      </ion-col>
      <ion-col size="5">
        <ion-text>
          Pramukh Vandana
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        8
      </ion-text>
    </ion-col>
      <ion-col size="5">
        <ion-text>
          Joi Murti Manohar Tari
        </ion-text>
      </ion-col>
      <ion-col size="5">
        <ion-text>
          Murti Manohar Tari
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        9
      </ion-text>
    </ion-col>
      <ion-col size="5">
        <ion-text>
          He Jī Me To Harkhe Nihalyā Nāth
        </ion-text>
      </ion-col>
      <ion-col size="5">
        <ion-text>
          Amrut Ni Heli
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        10
      </ion-text>
    </ion-col>
      <ion-col size="10">
        <ion-text>
          <b>Pick Your Own!</b>
        </ion-text>
      </ion-col>
  </ion-row>
</ion-grid>
<div>""",
    },
    'Writing-Based Competitions': {
        'Poetry': """<div class="skills-html">
<h2 class="static-content-title">Rules</h2>
<ul>
	<li>
    Participants must select from one of the themes below. The categories are provided
    with a small description on what the poem should depict.
  </li>
	<li>
    Although there are many different types of poetic form, please limit to using one poetry
    style/form throughout the poem. Examples are haiku, rhymed poetry, acrostic, free
    verse, ode, etc.
  </li>
  <li>
    Poems must be a maximum of 100 words.
  </li>
  <li>
    Participants must submit their written poem ahead of time.
  </li>
  <li>
    Participants should NOT put their name on their poem. They should only include their
    BKMS ID on the top right of the page.
  </li>
  <li>
    Poems will be judged on: organization, flow, grammar, word choice, content/depth.
  </li>
</ul>
<h2 class="static-content-title">Themes</h2>
<ion-grid class="ion-text-center">
  <ion-row class="header-row">
    <ion-col size="2">
      <ion-text>#</ion-text>
    </ion-col>
    <ion-col size="5">
      <ion-text>Theme</ion-text>
    </ion-col>
    <ion-col size="5">
      <ion-text>Description</ion-text>
    </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        1
      </ion-text>
    </ion-col>
      <ion-col size="5">
        <ion-text>
          Jay ho Akshar-Purushottam!
        </ion-text>
      </ion-col>
      <ion-col size="5">
        <ion-text>
          Write about the glory of Akshar-Purushottam Maharaj
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        2
      </ion-text>
    </ion-col>
      <ion-col size="5">
        <ion-text>
         His Gift to Us
        </ion-text>
      </ion-col>
      <ion-col size="5">
        <ion-text>
          Write about the Satsang Diksha
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        3
      </ion-text>
    </ion-col>
      <ion-col size="5">
        <ion-text>
          What does celebrating Pramukh Swami Maharaj's shatabdi mean to you? (<b>Pick One</b>)
        </ion-text>
      </ion-col>
      <ion-col size="5">
        <ion-text>
      <b> 1.</b> Life and Work
       <b> 2. </b> Virtues
       <b> 3. </b> Pramukh Swami Maharaj with Balaks
       <b> 4. </b> Personal Smruti
    </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        4
      </ion-text>
    </ion-col>
      <ion-col size="5">
        <ion-text>
          What does Mahant Swami Maharaj mean to you? (<b>Pick One</b>)
        </ion-text>
      </ion-col>
      <ion-col size="5">
        <ion-text>
      <b> 1.</b> Life and Work
       <b> 2. </b> Virtues
       <b> 3. </b> Mahant Swami Maharaj with Balaks
       <b> 4. </b> Personal Smruti
    </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        5
      </ion-text>
    </ion-col>
      <ion-col size="5">
        Mandirs
      </ion-col>
      <ion-col>
        Depict what mandir means to you
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        6
      </ion-text>
    </ion-col>
      <ion-col size="5">
        Guru Bhakti
      </ion-col>
      <ion-col>
        Write about what offering Guru Bhakti
        means to you
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        7
      </ion-text>
    </ion-col>
      <ion-col size="5">
        Other
      </ion-col>
      <ion-col>
        Any other Satsang topics that you like
      </ion-col>
  </ion-row>
</ion-grid>
<div>""",
        'Essay-Writing (Group 3)': """<div class="skills-html">
<h2 class="static-content-title">Rules</h2>
<ul>
	<li>
    Participants must select from one of the themes below. The categories are provided
    with a small description on what the essay can be on.
  </li>
  <li>
    Essays must be in 12 point font, Arial or Times New Roman, with double spacing.
  </li>
  <li>
    Essays must be between 500 to 1000 words.
  </li>
  <li>
    Essays must include at least:
  </li>
  <ul>
    <li>
      1 prasang
    </li>
    <li>
      2 scriptural references (Vachnamrut, Swamini Vato, Satsang Diksha, etc.)
    </li>
  </ul>
  <li>
    Essays must include a creative title and page numbers.
  </li>
  <li>
    Participants should NOT put their name on their essay. They should only include their
    BKMS ID on the top right of the page.
  </li>
  <li>
    Essays will be judged on: organization, flow, grammar, content, correct use of
    references.
  </li>
</ul>
<h2 class="static-content-title">Themes</h2>
<ion-grid class="ion-text-center">
  <ion-row class="header-row">
    <ion-col size="2">
      <ion-text>#</ion-text>
    </ion-col>
    <ion-col size="5">
      <ion-text>Theme</ion-text>
    </ion-col>
    <ion-col size="5">
      <ion-text>Description</ion-text>
    </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        1
      </ion-text>
    </ion-col>
      <ion-col size="5">
        <ion-text>
          Jay ho Akshar-Purushottam!
        </ion-text>
      </ion-col>
      <ion-col size="5">
        <ion-text>
          Write about the glory of Akshar-Purushottam Maharaj
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        2
      </ion-text>
    </ion-col>
      <ion-col size="5">
        <ion-text>
         His Gift to Us
        </ion-text>
      </ion-col>
      <ion-col size="5">
        <ion-text>
          Write about the Satsang Diksha
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        3
      </ion-text>
    </ion-col>
      <ion-col size="5">
        <ion-text>
          What does celebrating Pramukh Swami Maharaj's shatabdi mean to you? (<b>Pick One</b>)
        </ion-text>
      </ion-col>
      <ion-col size="5">
        <ion-text>
      <b> 1.</b> Life and Work
       <b> 2. </b> Virtues
       <b> 3. </b> Pramukh Swami Maharaj with Balaks
       <b> 4. </b> Personal Smruti
    </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        4
      </ion-text>
    </ion-col>
      <ion-col size="5">
        <ion-text>
          What does Mahant Swami Maharaj mean to you? (<b>Pick One</b>)
        </ion-text>
      </ion-col>
      <ion-col size="5">
        <ion-text>
      <b> 1.</b> Life and Work
       <b> 2. </b> Virtues
       <b> 3. </b> Mahant Swami Maharaj with Balaks
       <b> 4. </b> Personal Smruti
    </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        5
      </ion-text>
    </ion-col>
      <ion-col size="5">
        Mandirs
      </ion-col>
      <ion-col>
        Depict what mandir means to you
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        6
      </ion-text>
    </ion-col>
      <ion-col size="5">
        Guru Bhakti
      </ion-col>
      <ion-col>
        Write about what offering Guru Bhakti
        means to you
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        7
      </ion-text>
    </ion-col>
      <ion-col size="5">
        Other
      </ion-col>
      <ion-col>
        Any other Satsang topics that you like
      </ion-col>
  </ion-row>
</ion-grid>
<div>""",
    },
    'Art-Based Competitions': {
        'Painting/Illustration': """<div class="skills-html">
<h2 class="static-content-title">Rules</h2>
<ul>
	<li>
    Participants must select from one of the themes below. The categories are provided
    with a small description on what the artwork should depict.
  </li>
  <li>
    Artwork may include painting, drawing, chalk art, oil pastels, etc. This does not include
    photoshop or any multimedia art.
  </li>
  <li>
    The artwork must be 2D and can be prepared on any sized paper or canvas.
  </li>
  <li>
    Participants must submit multiple pictures and a video showing the artwork from
    different angles. Ensure proper lighting when taking pictures and video.  
  </li>
  <li>
    Painting/Illustration will be graded on: creativity, use of theme, visual/artistic elements.
  </li>
</ul>
<h2 class="static-content-title">Themes</h2>
<ion-grid class="ion-text-center">
  <ion-row class="header-row">
    <ion-col size="2">
      <ion-text>#</ion-text>
    </ion-col>
    <ion-col size="5">
      <ion-text>Theme</ion-text>
    </ion-col>
    <ion-col size="5">
      <ion-text>Description</ion-text>
    </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        1
      </ion-text>
    </ion-col>
      <ion-col size="5">
        <ion-text>
          Ghansham - The Miraculous Child
        </ion-text>
      </ion-col>
      <ion-col size="5">
        <ion-text>
          Depict any miraculous incident from Ghanshyam's childhood
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        2
      </ion-text>
    </ion-col>
      <ion-col size="5">
        <ion-text>
          Pramukh Swami Maharaj Shatabdi
        </ion-text>
      </ion-col>
      <ion-col size="5">
        <ion-text>
          Depict the life or work of Pramukh
          Swami Maharaj
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        3
      </ion-text>
    </ion-col>
      <ion-col size="5">
        <ion-text>
          Akshardham/Mandir
        </ion-text>
      </ion-col>
      <ion-col size="5">
        <ion-text>
          Depict what Akshardham or mandir
          means to you
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        4
      </ion-text>
    </ion-col>
      <ion-col size="5">
        <ion-text>
          My Guru: Mahant Swami Maharaj
        </ion-text>
      </ion-col>
      <ion-col size="5">
        <ion-text>
          Depict the life and work of Mahant
          Swami Maharaj        
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        5
      </ion-text>
    </ion-col>
      <ion-col size="5">
        Portraits
      </ion-col>
      <ion-col>
        Depict a portrait of Bhagwan
        Swaminarayan or Guru Parampara
      </ion-col>
  </ion-row>
</ion-grid>
<div>""",
        'Graphic Design': """<div class="skills-html">
<h2 class="static-content-title">Rules</h2>
<ul>
	<li>
    Participants must select from one of the themes below. The categories are provided
    with a small description on what the graphic should depict.
  </li>
  <li>
    The graphic can be made using any photo editing/illustrating tool, such as Photoshop
    or Canva.  
  </li>
  <li>
    The graphic can be in either portrait or landscape orientation.
  </li>
  <li>
    Ensure the graphic is of good quality, such as 1920 pixels by 1080 pixels.
  </li>
  <li>
    Graphic Design will be graded on: creativity, use of theme, visual/artistic elements.  </li>
  </li>
  <li>
    Participants must submit a raw file or their art work.
  </li>
</ul>
<h2 class="static-content-title">Themes</h2>
<ion-grid class="ion-text-center">
  <ion-row class="header-row">
    <ion-col size="2">
      <ion-text>#</ion-text>
    </ion-col>
    <ion-col size="5">
      <ion-text>Theme</ion-text>
    </ion-col>
    <ion-col size="5">
      <ion-text>Description</ion-text>
    </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        1
      </ion-text>
    </ion-col>
      <ion-col size="5">
        <ion-text>
          Ghansham - The Miraculous Child
        </ion-text>
      </ion-col>
      <ion-col size="5">
        <ion-text>
          Depict any miraculous incident from Ghanshyam's childhood
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        2
      </ion-text>
    </ion-col>
      <ion-col size="5">
        <ion-text>
          Pramukh Swami Maharaj Shatabdi
        </ion-text>
      </ion-col>
      <ion-col size="5">
        <ion-text>
          Depict the life or work of Pramukh
          Swami Maharaj
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        3
      </ion-text>
    </ion-col>
      <ion-col size="5">
        <ion-text>
          Akshardham/Mandir
        </ion-text>
      </ion-col>
      <ion-col size="5">
        <ion-text>
          Depict what Akshardham or mandir
          means to you
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        4
      </ion-text>
    </ion-col>
      <ion-col size="5">
        <ion-text>
          My Guru: Mahant Swami Maharaj
        </ion-text>
      </ion-col>
      <ion-col size="5">
        <ion-text>
          Depict the life and work of Mahant
          Swami Maharaj        
        </ion-text>
      </ion-col>
  </ion-row>
</ion-grid>
<div>""",
        'Video Making': """<div class="skills-html">
<h2 class="static-content-title">Rules</h2>
<ul>
	<li>
    Participants can choose from the sample topics or pick one of their choice.
  <li>
    The suggested topics are general and open-ended to allow for creativity.
  </li>
	<li>
    Video length should be 4 to 7 minutes long.
  </li>
	<li>
    This video will also be submitted electronically  
  </li>
  <li>
    Video Making will be graded on: creativity, use of theme, transitions, flow, organization.
  </li>
  <li>
    Participants must submit their video in mp4 format.
  </li>
</ul>
<h2 class="static-content-title">Topics</h2>
<ion-grid class="ion-text-center">
  <ion-row class="header-row">
    <ion-col size="2">
      <ion-text>#</ion-text>
    </ion-col>
    <ion-col size="5">
      <ion-text>Theme</ion-text>
    </ion-col>
    <ion-col size="5">
      <ion-text>Description</ion-text>
    </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        1
      </ion-text>
    </ion-col>
      <ion-col size="5">
        <ion-text>
          What does celebrating Pramukh Swami Maharaj's shatabdi mean to you? (<b>Pick One</b>)
        </ion-text>
      </ion-col>
      <ion-col size="5">
        <ion-text>
      <b> 1.</b> Life and Work
       <b> 2. </b> Virtues
       <b> 3. </b> Pramukh Swami Maharaj with Balaks
       <b> 4. </b> Personal Smruti
    </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        2
      </ion-text>
    </ion-col>
      <ion-col size="5">
        <ion-text>
          What does Mahant Swami Maharaj mean to you? (<b>Pick One</b>)
        </ion-text>
      </ion-col>
      <ion-col size="5">
        <ion-text>
      <b> 1.</b> Life and Work
       <b> 2. </b> Virtues
       <b> 3. </b> Mahant Swami Maharaj with Balaks
       <b> 4. </b> Personal Smruti
    </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        3
      </ion-text>
    </ion-col>
      <ion-col size="5">
        <ion-text>
          Our Sanstha's History
        </ion-text>
      </ion-col>
      <ion-col size="5">
        <ion-text>
          Consider: Timeline Format, One or Two major events, the foundation of BAPS, and the first mandir outside of India
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        4
      </ion-text>
    </ion-col>
      <ion-col size="5">
        <ion-text>
          Mandir
        </ion-text>
      </ion-col>
      <ion-col size="5">
        <ion-text>
          Depict what the importance of Mandir means to you.       
        </ion-text>
      </ion-col>
  </ion-row>
   <ion-row>
    <ion-col size="2">
      <ion-text>
        5
      </ion-text>
    </ion-col>
      <ion-col size="5">
        <ion-text>
          Satsang Diksha
        </ion-text>
      </ion-col>
      <ion-col size="5">
        <ion-text>
          Depict what the Satsang Diksha means to you. 
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        6
      </ion-text>
    </ion-col>
      <ion-col size="5">
        <ion-text>
          Other
        </ion-text>
      </ion-col>
      <ion-col size="5">
        <ion-text>
          Any other satsang related video.
        </ion-text>
      </ion-col>
  </ion-row>
</ion-grid>
<div>""",
        'Graphic Design': """<div class="skills-html">
<h2 class="static-content-title">Rules</h2>
<ul>
	<li>
    Participants must select from one of the themes below. The categories are provided
    with a small description on what the graphic should depict.
  </li>
  <li>
    The graphic can be made using any photo editing/illustrating tool, such as Photoshop
    or Canva.  
  </li>
  <li>
    The graphic can be in either portrait or landscape orientation.
  </li>
  <li>
    Ensure the graphic is of good quality, such as 1920 pixels by 1080 pixels.
  </li>
  <li>
    Graphic Design will be graded on: creativity, use of theme, visual/artistic elements.  </li>
  </li>
  <li>
    Participants must submit a raw file or their art work.
  </li>
</ul>
<ion-grid class="ion-text-center">
  <ion-row class="header-row">
    <ion-col size="2">
      <ion-text>#</ion-text>
    </ion-col>
    <ion-col size="5">
      <ion-text>Theme</ion-text>
    </ion-col>
    <ion-col size="5">
      <ion-text>Description</ion-text>
    </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        1
      </ion-text>
    </ion-col>
      <ion-col size="5">
        <ion-text>
          Ghansham - The Miraculous Child
        </ion-text>
      </ion-col>
      <ion-col size="5">
        <ion-text>
          Depict any miraculous incident from Ghanshyam's childhood
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        2
      </ion-text>
    </ion-col>
      <ion-col size="5">
        <ion-text>
          Pramukh Swami Maharaj Shatabdi
        </ion-text>
      </ion-col>
      <ion-col size="5">
        <ion-text>
          Depict the life or work of Pramukh
          Swami Maharaj
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        3
      </ion-text>
    </ion-col>
      <ion-col size="5">
        <ion-text>
          Akshardham/Mandir
        </ion-text>
      </ion-col>
      <ion-col size="5">
        <ion-text>
          Depict what Akshardham or mandir
          means to you
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        4
      </ion-text>
    </ion-col>
      <ion-col size="5">
        <ion-text>
          My Guru: Mahant Swami Maharaj
        </ion-text>
      </ion-col>
      <ion-col size="5">
        <ion-text>
          Depict the life and work of Mahant
          Swami Maharaj        
        </ion-text>
      </ion-col>
  </ion-row>
</ion-grid>
<div>""",
        'Rangoli Design': """<div class="skills-html">
<h2 class="static-content-title">Rules</h2>
<ul>
	<li>
    Participants can choose any of the suggested topics to design their rangoli.  
  </li>
  <li>
    The suggested topics are general and open-ended to allow for creativity.  </li>
  <li>
    Rangolis can be made from any of the following: colored powder, chalk, colored rice
    grains, paper cut outs, etc. Rangolis should not be simply drawn on paper.
  </li>
  <li>
    Rangolis that are submitted must be new and original designs, not done on prior
    occasions.
  </li>
  <li>
    Participants must submit multiple pictures and a video showing the artwork from
    different angles. Ensure proper lighting when taking pictures and video. The entire
    rangoli design should be visible.
  </li>
  <li>
    Rangoli Design will be graded on: creativity, use of theme, artistic elements.
  </li>
</ul>
<h2 class="static-content-title">Themes</h2>
<ion-grid class="ion-text-center">
  <ion-row class="header-row">
    <ion-col size="2">
      <ion-text>#</ion-text>
    </ion-col>
    <ion-col size="5">
      <ion-text>Theme</ion-text>
    </ion-col>
    <ion-col size="5">
      <ion-text>Description</ion-text>
    </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        1
      </ion-text>
    </ion-col>
      <ion-col size="5">
        <ion-text>
          Bhagwan Swaminarayan
        </ion-text>
      </ion-col>
      <ion-col size="5">
        <ion-text>
          Celebrating Swaminarayan Jayanti
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        2
      </ion-text>
    </ion-col>
      <ion-col size="5">
        <ion-text>
          Aksharbrahmana Vadhamna
        </ion-text>
      </ion-col>
      <ion-col size="5">
        <ion-text>
          Welcoming Gunatitanand Swami to sit
          alongside Harikrishna Maharaj
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        3
      </ion-text>
    </ion-col>
      <ion-col size="5">
        <ion-text>
          Pramukh Swami Maharaj
        </ion-text>
      </ion-col>
      <ion-col size="5">
        <ion-text>
          Celebrating Pramukh Swami Maharaj’s
          Shatabdi Mahotsav
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        4
      </ion-text>
    </ion-col>
      <ion-col size="5">
        <ion-text>
         Divyata na Divada 
        </ion-text>
      </ion-col>
      <ion-col size="5">
        <ion-text>
          Celebrating Diwali with our family      
        </ion-text>
      </ion-col>
  </ion-row>
   <ion-row>
    <ion-col size="2">
      <ion-text>
        5
      </ion-text>
    </ion-col>
      <ion-col size="10">
        <ion-text>
          <b>Pick Your Own!</b>
        </ion-text>
      </ion-col>
  </ion-row>
</ion-grid>
<div>""",
    },
}

# Skills Challenge for KM
KISHORE_SKILLS_CHALLENGE = {
  'Story/Speech-Based Competitions': {
        'Kirtan-Based Short Speech': """<div class="skills-html">
<p>This competition is ideal for a kishore/kishori who is strong in singing as well as public
speaking. Participants will combine the two technical elements to create an engaging and
thought-provoking presentation. Presentations will revolve around a single chosar from the
adhiveshan booklet.
</p>
<p>
This competition requires a thorough understanding of the background of the chosar and the
meaning of the words. Essentially, you will be required to understand the meaning of the
chosar pad, provide a nirupan and your own manan. A cohesive speech will incorporate these
elements in a seamless manner — used to educate anyone who watches. Limited to one
participant per submission. Details on formatting and how to submit videos will be provided.
</p>
<p>Example Video (Syncing to God’s Playlist): <a href="https://www.youtube.com/watch?v=UcgF0tRukJs" target="_blank">Here</a>
</p>
<p>
Example Video (Kishore Sabha): <a href="https://www.youtube.com/watch?v=Dr7RedeTTT0&list=PLZ_xghvSoitg6sY2zThPrWfuEiHirGF1Y&index=17" target="_blank">Here</a>
</p>
<h2 class="static-content-title">Rules</h2>
<ul> 
	<li>
    Maximum of 10-15 minutes in ‘single-take’ format - As this is a speech first, aim for an
    explanation and manan vs singing ration of: 5-10 minutes for explanation and 4-6
    minutes for singing of the entire chosar pad. Points will be deducted on an interval
    basis if a submission is less than 10 minutes or over the 15 minute limit. Notes may be
    utilized so long as they serve as talking points.
	</li>
	<li>
      Use the Prasang behind Chosar as a reference to enhance your explanation (recitation
    of the prasang alone will not be considered a full speech)
  </li>
	<li>Translations are incorporated</li>
  <li>
    Video editing is not required, but preferred (creative elements to enhance the speech)
	</li>
	<li>
    Utilizes a single Chosar pad from the ones listed below
  </li>
  <li>
    Kishores and Kishoris will be judged on time limit, accurate chosar pad understanding,
    incorporation of translations, creativity, ability to sing and speak, and cohesiveness of the
    speech’s components and overall message.
  </li>
</ul>
<h2 class="static-content-title">Approved Chosar Pads</h2><h4>(must choose one from the following list)</h4>
<ion-grid class="ion-text-center">
  <ion-row class="header-row">
    <ion-col size="2">
      <ion-text>#</ion-text>
    </ion-col>
    <ion-col size="10">
      <ion-text>Chosar Pad</ion-text>
    </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        1
      </ion-text>
    </ion-col>
      <ion-col size="10">
        <ion-text>
          Sant Samagam Kije
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        2
      </ion-text>
    </ion-col>
      <ion-col size="10">
        <ion-text>
          Sant Param Hitkari
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        3
      </ion-text>
    </ion-col>
      <ion-col size="10">
        <ion-text>
          Sarve Man Taji
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        4
      </ion-text>
    </ion-col>
      <ion-col size="10">
        <ion-text>
          Sambhal Beni Hari Rijhyani Ritdi
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        5
      </ion-text>
    </ion-col>
      <ion-col size="10">
        <ion-text>
          Bolya Shri Hari Re
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        6
      </ion-text>
    </ion-col>
      <ion-col size="10">
        <ion-text>
          Vali Sahu Sambhalo Re
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        7
      </ion-text>
    </ion-col>
      <ion-col size="10">
        <ion-text>
         Tek Na Mele Re
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        8
      </ion-text>
    </ion-col>
      <ion-col size="10">
        <ion-text>
         Anubhavi Anandma
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        9
      </ion-text>
    </ion-col>
      <ion-col size="10">
        <ion-text>
         Manasno Avatar Mogho Nahi Male Fari
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        10
      </ion-text>
    </ion-col>
      <ion-col size="10">
        <ion-text>
         Sacha Sadhu Re
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        11
      </ion-text>
    </ion-col>
      <ion-col size="10">
        <ion-text>
         Janmya Tyathi Jarur Janjo
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        12
      </ion-text>
    </ion-col>
      <ion-col size="10">
        <ion-text>
         Sant Jan Soi Sada
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        13
      </ion-text>
    </ion-col>
      <ion-col size="10">
        <ion-text>
         Narad Mere Santse Adhik Na Koi
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        14
      </ion-text>
    </ion-col>
      <ion-col size="10">
        <ion-text>
         Dohylu Thavu Haridas Re
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        15
      </ion-text>
    </ion-col>
      <ion-col size="10">
        <ion-text>
         Shidne Rahie Kangal
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        16
      </ion-text>
    </ion-col>
      <ion-col size="10">
        <ion-text>
         Premi Janne Vash Pataliyo
        </ion-text>
      </ion-col>
  </ion-row>
</ion-grid>
<p>Participants can access the meaning of each chosar <a href="https://baps.box.com/s/gwh5auwoiw1ysyffrhqxbhuy0ivpj0at" target="_blank">here</a>
</p>
<p>
Each submission should be in a single-take format, meaning no editing/cutting of the clip. This
competition challenges deep knowledge of the Chosar, creative thinking and speech/singing
skills which can only be fairly judged through a non-edited submission. There can be
images/text on screen to help enhance/highlight certain messages.
</p>
<p>
When recording yourself, you must record their story in good lighting and on a good camera
(either on a smartphone or webcam). Kishores should wear a Jabho-Lengho and Kishoris
should wear a Punjabi. The speech may also be presented with graphics, text, etc.
</p>
<div>""",
        'Creative Storytelling': """<div class="skills-html">
<p>
Participants will choose a prasang/story from their adhiveshan modules and/or from other
books as well. Participants must tell the story in its entirety, as well as provide a manan, or
reflection, on the importance of the story. This challenge tests full knowledge of the prasang,
proper manan and public speaking skills.
</p>
<h2 class="static-content-title">Rules</h2>
<ul>
	<li>
    Participants will have a maximum of 7 minutes.
  </li>
	<li>
    The prasang/story must be memorized, notes will not be allowed.
  </li>
	<li>
    The prasang/story must come from the approved list of published books.
	</li>
</ul>
<p>
Creative elements can be added such as creative visuals, editing, music, graphics, etc.
</p>
<p>
Storytelling will be judged on: storytelling ability, content, Manan/personal reflection, gestures,
organization, flow, confidence, tone, and time. If you decide to include creative elements,
please keep in mind importance will be given to the storytelling aspect of the submission.
While creative elements can be used to enhance your overall submission, they will not be taken
into consideration as heavily as the storytelling ability and accuracy showcased.
</p>
<p>
When recording yourself, you must record their story in good lighting and on a good camera
(either on a smartphone or webcam). Kishores should wear a Jabho-Lengho and Kishoris
should wear a Punjabi. The speech may also be presented with graphics, text, etc.
</p>
<h2 class="static-content-title">Approved Books</h2><h4>(must choose one from the following list)</h4>
<ion-grid class="ion-text-center">
  <ion-row class="header-row">
    <ion-col size="2">
      <ion-text>#</ion-text>
    </ion-col>
    <ion-col size="10">
      <ion-text>Book Name</ion-text>
    </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        1
      </ion-text>
    </ion-col>
      <ion-col size="10">
        <ion-text>
          Yogiji Maharaj’s Bodh Kathas
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        2
      </ion-text>
    </ion-col>
      <ion-col size="10">
        <ion-text>
         108 Prasang Mala
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        3
      </ion-text>
    </ion-col>
      <ion-col size="10">
        <ion-text>
          Pramukh Swami Maharaj’s 100 Inspiring Prasangs
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        4
      </ion-text>
    </ion-col>
      <ion-col size="10">
        <ion-text>
          Mahant Swami Maharaj Epitome of santiliness
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        5
      </ion-text>
    </ion-col>
      <ion-col size="10">
        <ion-text>
          Divine memories 1, 2, 3, 4
        </ion-text>
      </ion-col>
  </ion-row>
</ion-grid>
<p>
Each submission should be in a single-take format, meaning no editing/cutting of the clip. This
competition challenges deep knowledge of the prasang/story, creative thinking and public
speaking skills which can only be fairly judged through a non-edited submission. There can be
images/text on screen to help enhance/highlight certain messages.
</p>
<p>
When recording yourself, you must record their story in good lighting and on a good camera
(either on a smartphone or webcam). Kishores should wear a Jabho-Lengho and Kishoris
should wear a Punjabi. The speech may also be presented with graphics, text, etc.
</p>
<div>""",
        'Vachanamrut Nirupan': """<div class="skills-html">
<p>
Kishores and Kishoris will have the opportunity to perform a Nirupan on any Vachnamrut of
their choice.
</p>
<p>
Example Vachnamrut Nirupan: <a href="https://www.youtube.com/watch?v=ZW50gmS2wlk&ab_channel=BAPSChannel" target="_blank">Here</a>
</p>
<h2 class="static-content-title">Rules</h2>
<ul>
	<li>
    This is a solo presentation that should be recorded audio and video for submission.
  </li>
  <li>This presentation has a time limit of 10-15 minutes.</li>
  <li>
    Platforms such as Google Slides, Powerpoint, or Prezi may be used to assist in the
    nirupan but are not required. Positive grading points will not be given to those that
    decide to use the platforms such as Google Slides, Powerpoint, or Prezi.
  </li>
	<li>
Delegates are required to read the opening paragraph but are not required to read the
entire vachanamrut thereafter
	</li>
  <li>
Delegates should explain the Vachanamrut, analyze the content, relate the Vachanamrut
to other Prasangs and texts, and explain how this Vachanamrut is beneficial to a Kishore
or Kishori’s life.
  </li>
  <li>
You can choose to do it in either Gujarati or English, whichever language you’re most
comfortable with.
  </li>
  <li>
Actually read the Vachanamrut (opening paragraph) and go to the part or topic you
want to do nirupan on. It is not required to read or do nirupan of the vachanamrut in its
entirety.
  </li>
  <li>
To add authenticity to your nirupan, you can read the first stanza in a poetic way
<a href="https://download.baps.org/download.php?file=Data/Sites/1/Media/DownloadableFile/DailySatsang/vachanamrut_2019/vachanamrut_249.mp3" target="_blank">(example)</a>
  </li>
</ul>
<p>
Kishores/Kishoris will be judged on analysis of the Vachanamrut, references to other
prasangs/texts, real life application, speaking ability, accurate information, and timing.
</p>
<h2 class="static-content-title">Vachanamrut List</h2><h4>(suggestions but not limited to)</h4>
<ion-grid class="ion-text-center">
  <ion-row class="header-row">
    <ion-col size="2">
      <ion-text>#</ion-text>
    </ion-col>
    <ion-col size="10">
      <ion-text>Vachanamrut</ion-text>
    </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        1
      </ion-text>
    </ion-col>
      <ion-col size="10">
        <ion-text>
          Gadhada I-3, 6, 16, 21, 67
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        2
      </ion-text>
    </ion-col>
      <ion-col size="10">
        <ion-text>
         Gadhada II-9
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        3
      </ion-text>
    </ion-col>
      <ion-col size="10">
        <ion-text>
          Gadhada III-2, 7, 38
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        4
      </ion-text>
    </ion-col>
      <ion-col size="10">
        <ion-text>
          Panchala 4, 7
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        5
      </ion-text>
    </ion-col>
      <ion-col size="10">
        <ion-text>
         Loya 12
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        6
      </ion-text>
    </ion-col>
      <ion-col size="10">
        <ion-text>
         Vadtal 11
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
  <ion-col size="2">
      <ion-text>
        7
      </ion-text>
    </ion-col>
    <ion-col size="10">
      <ion-text>
        <b>Pick your own!</b>
      </ion-text>
    </ion-col>
  </ion-row>
</ion-grid>
<p>
Each submission should be in a single-take format, meaning no editing/cutting of the clip. This
competition challenges deep knowledge of the Vachanamrut, creative thinking and public
speaking skills which can only be fairly judged through a non-edited submission. There can be
images/text on screen to help enhance/highlight certain messages.
</p>
<p>
When recording yourself, you must record their story in good lighting and on a good camera
(either on a smartphone or webcam). Kishores should wear a Jabho-Lengho and Kishoris
should wear a Punjabi. The speech may also be presented with graphics, text, etc.
</p>
<div>""",
        'Group Presentation': """<div class="skills-html">
<p>
Kishores and Kishoris will have the opportunity to present on the topics listed below in a group
from the same mandal. Groups are limited to a minimum of 3 people and a maximum of 5
people.
</p>
<h2 class="static-content-title">Rules</h2>
<ul>
	<li>
Presentations can be created on platforms such as Google Slides, Powerpoint, Prezi,
etc.
	</li>
  <li>
The presentation can be done in a wide range of creativity such as a musical
presentation, acting, rhymes, TED talk style, etc
  </li>
	<li>The grading will be based on 60% content and 40% creativity.</li>
  <li>
The presentation should include module content, which must include at least 2
references from Vachanamrut, Swamini Vato, Kirtans, etc.
  </li>
  <li>
The presentation should provide a thorough understanding of the topic using
Satsang-based references. Kishores/Kishoris will have 7 minutes to 12 minutes
maximum to present their topic
  </li>
  <li>
Everyone in the group must contribute and participate equally in order to showcase
proper knowledge/research of the theme.
  </li>
  <li>
While the group is required to adhere to the theme, the descriptions are provided to
serve as a guideline.
  </li>
  <li>
The themes of the topics the group must be chosen from the list below:
  </li> 
</ul>
<h2 class="static-content-title">Themes</h2><h4>(required choose one from the list)</h4>
<ion-grid class="ion-text-center">
  <ion-row class="header-row">
    <ion-col size="2">
      <ion-text>#</ion-text>
    </ion-col>
    <ion-col size="5">
      <ion-text>Theme</ion-text>
    </ion-col>
    <ion-col size="5">
      <ion-text>Description (suggestions, but not limited to)</ion-text>
    </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        1
      </ion-text>
    </ion-col>
    <ion-col size="5">
      <ion-text>
     Akshar-Purushottam
      </ion-text>
    </ion-col>
    <ion-col size="5">
    <ion-row>
      <ion-text>
      1. Greatness of the
      Akshar-Purushottam Darshan
      </ion-text>
      <br />
      <ion-text>
      2. What does Akshar Purshottam mean?
      </ion-text>
      <br />
      <ion-text>
      3. The necessity of the
      Aksharbrahma Guru
      </ion-text>
    </ion-row>
    </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        2
      </ion-text>
    </ion-col>
    <ion-col size="5">
      <ion-text>
    His Gift To Us
      </ion-text>
    </ion-col>
    <ion-col size="5">
      <ion-text>
      Satsang Diksha
      </ion-text>
    </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        3
      </ion-text>
    </ion-col>
    <ion-col size="5">
      <ion-text>
    My Guru Mahant
Swami Maharaj
      </ion-text>
    </ion-col>
    <ion-col size="5">
      <ion-text>
      The life of Mahant Swami Maharaj and His divine
qualities
      </ion-text>
    </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        4
      </ion-text>
    </ion-col>
    <ion-col size="5">
      <ion-text>
    Guru Bhakti
      </ion-text>
    </ion-col>
    <ion-col size="5">
      <ion-text>
      The importance of guru bhakti.
My Guru Bhakti
      </ion-text>
    </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        5
      </ion-text>
    </ion-col>
    <ion-col size="5">
      <ion-text>
    Pramukh Swami
Maharaj Shatabdi
      </ion-text>
    </ion-col>
    <ion-col size="5">
      <ion-text>
      Celebrating the 100 year impact of Pramukh
      Swami Maharaj had on others
      Qualities, 
      Work, 
      Life Message     
 </ion-text>
    </ion-col>
  </ion-row>
   <ion-row>
    <ion-col size="2">
      <ion-text>
        6
      </ion-text>
    </ion-col>
    <ion-col size="5">
      <ion-text>
    Mandirs
      </ion-text>
    </ion-col>
    <ion-col size="5">
      <ion-text>
          The importance of Mandirs and the future
          impact of Mandirs: on our world, on our society, and on us as indivudals
 </ion-text>
    </ion-col>
  </ion-row>
</ion-grid>
<div>""",
    },
    'Music-Based Competitions': {
        'Solo Singing': """<div class="skills-html">
<p>
Delegates may select any Kirtan/Chosar Pad they wish to sing for this challenge, more
specifically, it is encouraged that delegates pick a Bhajan that they strongly resonate with.
</p>
<h2 class="static-content-title">Rules</h2>
<ul>
	<li>
  Total Time: maximum 8 minutes. Please include a 7 minutes for singing and 1 minute
verbal explanation/manan of the theme/messaging of the bhajan. You may include a
brief meaning/manan of the Bhajan or its history and/or if the Bhajan holds any personal
significance. While you will not be graded heavily on your speech, you will be able to
showcase your understanding of the bhajan.
</li>
	<li>
  You may choose to cut verse lines from a longer kirtan to fit the time limit. You will not
be penalized for cutting verse lines so long as the overall messaging of the bhajan
remains intact.
</li>
  <li>
  The chosen Bhajan must be on a Sanstha publication in order to qualify. When
submitting, please provide publication details for the chosen bhajan (CD name/track
number and Kirtanavali page reference).
</li>
 <li>
 You may include instruments in your submission but keep in mind, you will be graded
solely on the vocal aspects of your submission.
</li>
 <li>
 All submissions must be raw audio and videos recordings.
 </li>
</ul>
<p>
You will be judged on: sur (melody), tempo/rhythm, and tone/voice, creativity and preparation.
As you will be judged on a unique presentation of the Bhajan, get creative and include
sargams, alaps etc to enhance the overall quality of your submission. You may combine kirtans
to enhance creativity of your submission. The submission will be in video format to verify
authenticity of the participant. Please follow video submission guidelines.
</p>
<p>
When recording yourself, you must record their story in good lighting and on a good camera
(either on a smartphone or webcam). Kishores should wear a Jabho-Lengho and Kishoris
should wear a Punjabi. The submission may also be presented with graphics, text, etc.
</p>
<div>""",
        'Musical Production (Group Singing)': """<div class="skills-html">
<p>
Kishores and Kishoris from the same mandal will have the opportunity to create a full music
production. While there is no limit to the number of participants per group, all participants
must be from the same Mandal.
</p>
<h2 class="static-content-title">Rules</h2>
<ul>
	<li>
  Total Time: maximum 10 minutes. Please include a maximum of 1 minute verbal
explanation of the theme/messaging of the Bhajan. You may include a brief
meaning/manan of the bhajan or its history. While you will not be graded heavily on
your speech, you will be able to showcase your understanding of the bhajan.
</li> 
 <li>
 You may choose to cut verse lines from a longer Kirtan to fit the time limit. You will not
be penalized for cutting verse lines so long as the overall messaging of the bhajan
remains intact.
</li>
	<li>
  The chosen bhajan(s) must be on a sastha publication in order to qualify. When
submitting, please provide publication details for the chosen Bhajan (CD name/track
number and Kirtanavali page reference).
</li>
<li>
While its preferred that you make a cover video as a submission, it is not required. If no
cover video then, each participant must provide a solo video as proof of their
contribution.
</li>
</ul>
<p>
Kishores and Kishoris may combine musical instruments, vocals, and sound effects to create a
music production using production software such as Garageband, Audacity, FL Studio, etc.
</p>
<p>
The produced soundtrack must be exported and submitted as a MP3 file. The soundtrack will
be graded on tone of vocals, creativity, melody, implementation of proper musical instruments,
tempo/rhythm, and sound effects. The submission will be in video format to verify authenticity
of the participants. Please follow video submission guidelines.
</p>
<p>
When recording yourself, you must record their story in good lighting and on a good camera
(either on a smartphone or webcam). Kishores should wear a Jabho-Lengho and Kishoris
should wear a Punjabi. The submission may also be presented with graphics, text, etc.
</p>
<div>""",
    },
    'Writing-Based Competitions': {
        'Research Paper (Case Study)': """<div class="skills-html">
<p>
Participants must select to research one of the themes below. The categories are provided,
with a small description on what the paper should be on.
</p>
<h2 class="static-content-title">Rules</h2>
<ul>
	<li>
Paper must be in 12 point font, Arial or Times New Roman with double margins.
  </li>
	<li>
Paper must be between 3-5 pages and max 2000 words (references not included in
word count).  </li>
<li>
Paper must include at least:
</li>
  <ul>
    <li>
    3 references from Satsang texts (Cited) (Used to answer the why).
    </li>
    <li>
    2 references from anywhere else (Public Data or sources).
    </li>
    <li>
     1 interviewee source (Reach out to a person).
    </li>
  </ul>
<li>
Paper must include a title and page numbers.
</li>
<li>
Participants should NOT put their name on their essay. They should only include their
BKMS ID on the top right of the page.
</li>
<li>
Papers will be judged on: organization, flow, grammar, content, sources, citations
</li>
</ul>
<h2 class="static-content-title">Themes</h2><h4>(required to choose one from the following list)</h4>
<ion-grid class="ion-text-center">
  <ion-row class="header-row">
    <ion-col size="2">
      <ion-text>#</ion-text>
    </ion-col>
    <ion-col size="10">
      <ion-text>Topic</ion-text>
    </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        1
      </ion-text>
    </ion-col>
      <ion-col size="10">
        <ion-text>
The Influence of Local Mandirs on Community Support and
Fundraising.
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        2
      </ion-text>
    </ion-col>
      <ion-col size="10">
        <ion-text>
          The Influence of Pramukh Swami Maharaj’s life & work across the
world.
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        3
      </ion-text>
    </ion-col>
      <ion-col size="10">
        <ion-text>
          The influence of Mahant Swami Maharaj’s life & work across the world.

        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        4
      </ion-text>
    </ion-col>
      <ion-col size="10">
        <ion-text class="md hydrated">
            Truth and Applicability of Satsang Concepts, pick one: <b>1.</b> True Happiness <b>2.</b> Positive Attitude <b>3.</b> Unity <b>4.</b> Addiction-Free Life <b>5.</b> Family Harmony <b>6.</b> Forgiveness <b>7.</b> Tolerance
      </ion-text>
  </ion-row>
</ion-grid>
<div>""",
        'Screenwriting': """<div class="skills-html">
<p>
Anyone interested in productions or musicals will find this challenge interesting. A Kishore or
Kishori must explain the relevant theme of Guru Bhakti through a written play or musical.
Specific insights must be incorporated within the written play or musical.
</p>
<h2 class="static-content-title">Rules</h2>
<ul>
	<li>
Writing must be done on either Google Docs or Microsoft Word and turned in as a PDF
file
  </li>
  <li>
An example script with proper formatting will be provided.
  </li>
  <li>
Competitors will be graded on grammar, sentence structure, readability, format,
creativity, story arch, use of themes.
  </li>
  <li>
Max Length: 2500 words
  </li>
 <li>
 Highlight or bring out a Satsang message or inspiration
 </li>
</ul>
<h2 class="static-content-title">Possible Themes</h2><h4>(not limited to)</h4>
<ion-grid class="ion-text-center">
  <ion-row class="header-row">
    <ion-col size="2">
      <ion-text>#</ion-text>
    </ion-col>
    <ion-col size="5">
      <ion-text>Theme</ion-text>
    </ion-col>
    <ion-col size="5">
      <ion-text>Prasangs</ion-text>
    </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        1
      </ion-text>
    </ion-col>
      <ion-col size="5">
        <ion-text>
          Faith
        </ion-text>
      </ion-col>
      <ion-col size="5">
        <ion-text>
Satyakam Jabali
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        2
      </ion-text>
    </ion-col>
      <ion-col size="5">
        <ion-text>
Respecting
        </ion-text>
      </ion-col>
      <ion-col size="5">
        <ion-text>
         Story of Shravan
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        3
      </ion-text>
    </ion-col>
      <ion-col size="5">
        <ion-text>
          Power of Prayer 
        </ion-text>
      </ion-col>
      <ion-col size="5">
        <ion-text>
Story of Gajendra
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        4
      </ion-text>
    </ion-col>
      <ion-col size="5">
        <ion-text>
          Fearlessness
        </ion-text>
      </ion-col>
      <ion-col size="5">
        <ion-text>
Nachiketa and Yamraj
Dungar Bhakta walking to farm at night
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
  <ion-col size="2">
      <ion-text>
        5
      </ion-text>
    </ion-col>
    <ion-col size="10">
      <ion-text>
        <b>Pick your own!</b>
      </ion-text>
    </ion-col>
  </ion-row>
</ion-grid>
<p>Additional examples can be found <a href="http://www.swaminarayan.org/yogijimaharaj/talesofwisdom/index.htm" target="_blank">here</a></p>
<div>""",
    },
    'Art-Based Talents': {
        'Painting & Illustration': """<div class="skills-html">
<p>
Kishores and Kishoris will have an opportunity to demonstrate their painting and illustration
(physical or digital) to create artwork. Participants must select from one of the themes below to
create a painting/illustration for. The categories are provided, with a small description on what
the artwork should depict.
</p>
<h2 class="static-content-title">Rules</h2>
<ul>
	<li>
Submit a panoramic video of the artwork along with multiple angle photos as well to
capture the full quality of artwork.
  </li>
  <li>
Submit a 1-2 minute video describing the artwork, how you did it, and any unique
features.
  </li>
  <li>
 Artwork may include painting, drawing, chalk art, oil pastels, sculptures, 3D models, etc.
 Participants can illustrate painting digitally through an application (such as Procreate,
sketch) on their iPad or a tablet as well. This does not include Photoshop or any
multimedia art.
   </li>
  <li>
  Delegates must have explored and shown a strong compositional arrangement and
solutions. The subject matter is drawn large taking up the majority of the space.
Delegates have filled all remaining background or surrounding space with at least a
variation of color shifting.
</li>
</ul>
<h2 class="static-content-title">Possible Themes</h2><h4>(not limited to)</h4>
<ion-grid class="ion-text-center">
  <ion-row class="header-row">
    <ion-col size="2">
      <ion-text>#</ion-text>
    </ion-col>
    <ion-col size="5">
      <ion-text>Theme</ion-text>
    </ion-col>
    <ion-col size="5">
      <ion-text>Description</ion-text>
    </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        1
      </ion-text>
    </ion-col>
      <ion-col size="5">
        <ion-text>
My Guru Mahant Swami
Maharaj
        </ion-text>
      </ion-col>
      <ion-col size="5">
        <ion-text>
Depict any incident from Mahant
Swami Maharaj’s life or portrait of
Mahant Swami Maharaj
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        2
      </ion-text>
    </ion-col>
      <ion-col size="5">
        <ion-text>
Pramukh Swami Maharaj
Shatabdi
        </ion-text>
      </ion-col>
      <ion-col size="5">
        <ion-text>
Depict the life or work of Pramukh
Swami Maharaj or portrait of
Pramukh Swami Maharaj
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        3
      </ion-text>
    </ion-col>
      <ion-col size="5">
        <ion-text>
          Guru Bhakti
        </ion-text>
      </ion-col>
      <ion-col size="5">
        <ion-text>
Depict an incident from our Gurus’
lives on the topic of Guru Bhakti
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        4
      </ion-text>
    </ion-col>
      <ion-col size="5">
        <ion-text>
Mandir / Akshardham
        </ion-text>
      </ion-col>
      <ion-col size="5">
        <ion-text>
Depict what Mandir / Akshardham
means to you
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        5
      </ion-text>
    </ion-col>
      <ion-col size="5">
        Guru Parampara
      </ion-col>
      <ion-col>
Creatively depict Guru Parampara.
      </ion-col>
  </ion-row>
   <ion-row>
    <ion-col size="2">
      <ion-text>
        6
      </ion-text>
    </ion-col>
      <ion-col size="5">
        Other
      </ion-col>
      <ion-col>
Depict any Satsang concept
      </ion-col>
  </ion-row>
  <ion-row>
  <ion-col size="2">
      <ion-text>
        7
      </ion-text>
    </ion-col>
    <ion-col size="10">
      <b>Pick your own!</b>
    </ion-col>
  </ion-row>
</ion-grid>
<div>""",
        'Graphic Design': """<div class="skills-html">
<p>
Kishores and Kishoris will have an opportunity to demonstrate their graphic design skill to
create a design. The categories are provided below, with a small description on what the
graphic should depict.
</p>
<h2 class="static-content-title">Rules</h2>
<ul>
	<li>
The graphic can be made using any photo editing/illustrating tool, such as Photoshop,
Illustrator, Canva or any other tool.
  </li>
  <li>
The submission should be original and not heavily influenced by another graphic from
anywhere.
  </li>
  <li>
The graphic can be in either portrait or landscape orientation.
  </li>
  <li>
Please make sure the graphic is of good quality, such as 1920 pixels by 1080 pixels.
  </li>
  <li>
You must also submit the final output (.jpeg) and the editable files of your creation.
  </li>
  <li>
Ensure the color theory is correct, design proximity is neat and typography fits well in
the graphic
  </li>
</ul>
<h2 class="static-content-title">Design Themes</h2><h4>(not limited to)</h4>
<ion-grid class="ion-text-center">
  <ion-row class="header-row">
    <ion-col size="2">
      <ion-text>#</ion-text>
    </ion-col>
    <ion-col size="5">
      <ion-text>Theme</ion-text>
    </ion-col>
    <ion-col size="5">
      <ion-text>Description</ion-text>
    </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        1
      </ion-text>
    </ion-col>
      <ion-col size="5">
        <ion-text>
          Bhagwan Swaminarayan
        </ion-text>
      </ion-col>
      <ion-col size="5">
        <ion-text>
Depict the life and work of
Bhagwan Swaminarayan
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        2
      </ion-text>
    </ion-col>
      <ion-col size="5">
        <ion-text>
          Visualizing the Prasang
        </ion-text>
      </ion-col>
      <ion-col size="5">
        <ion-text>
          Depict any famous Prasangs from
our gurus’ life
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        3
      </ion-text>
    </ion-col>
      <ion-col size="5">
        <ion-text>
          Pramukh Swami Maharaj
        </ion-text>
      </ion-col>
      <ion-col size="5">
        <ion-text>
         Explain the life and work of
Pramukh Swami Maharaj
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        4
      </ion-text>
    </ion-col>
      <ion-col size="5">
        <ion-text>
          My Guru
        </ion-text>
      </ion-col>
      <ion-col size="5">
        <ion-text>
          Explain an introduction of Mahant
Swami Maharaj        
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        5
      </ion-text>
    </ion-col>
      <ion-col size="5">
        <ion-text>
          Satsang Timeline
        </ion-text>
      </ion-col>
      <ion-col size="5">
        <ion-text>
          Depict key moments from our
satsang history (local, national or
global)     
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        6
      </ion-text>
    </ion-col>
      <ion-col size="5">
        <ion-text>
          Other
        </ion-text>
      </ion-col>
      <ion-col size="5">
        <ion-text>
          Depict any Satsang concept
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
  <ion-col size="2">
      <ion-text>
        7
      </ion-text>
    </ion-col>
    <ion-col size="10">
      <ion-text>
        <b>Pick your own!</b>
      </ion-text>
    </ion-col>
  </ion-row>
</ion-grid>
<div>""",
        'Photography': """<div class="skills-html">
<p>
Kishores and Kishoris will have the opportunity to create a photo album containing a topic or
theme which corresponds to the images within the album. For example, the images within the
submitted photo album must correspond to a satsang topic such as: Guru Bhakti, Mahima,
Ahnik, Bhakti, Mandir, Satpurush, Prarthana, Bhagwan’s creation, Samp or any other Satsang
topics.
</p>
<h2 class="static-content-title">Rules</h2>
<ul>
	<li>
Photo albums are to be submitted with a brief description of the theme which
corresponds to the images.
</li>
  <li>
Images must be submitted within a folder or zip file with the image types as either
JPEG or PNG
  </li>
	<li>
    Video length should be 4 to 7 minutes long.
  </li>
	<li>
The photo must be taken by the person submitting
  </li>
  <li>
You can include maximum of five images  
</li>
  <li>
Create a PPT/Slides to capture images and include a description.
  </li>
  <li>
    Photo albums will be judged by consistent themes, quality, moods, creativity,
originality, and uniqueness of concept.
  </li>
  <li>
  Ensure photos are of the same type in an album (types such as minimalism, abstract,
documentary, landscape, portrait, street, etc.)
  </li>
  <li>
    Each participant can make their album stand out by ensuring the photos are
interconnected or complementary
  </li>
</ul>
<h2 class="static-content-title">Possible Topics</h2><h4>(not limited to)</h4>
<ion-grid class="ion-text-center">
  <ion-row class="header-row">
    <ion-col size="2">
      <ion-text>#</ion-text>
    </ion-col>
    <ion-col size="10">
      <ion-text>Theme</ion-text>
    </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        1
      </ion-text>
    </ion-col>
      <ion-col size="10">
        <ion-text>
          Guru Bhakti
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        2
      </ion-text>
    </ion-col>
      <ion-col size="10">
        <ion-text>
          Mahima
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        3
      </ion-text>
    </ion-col>
      <ion-col size="10">
        <ion-text>
          Ahnik
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        4
      </ion-text>
    </ion-col>
      <ion-col size="10">
        <ion-text>
         Bhakti
        </ion-text>
      </ion-col>
  </ion-row>
   <ion-row>
    <ion-col size="2">
      <ion-text>
        5
      </ion-text>
    </ion-col>
      <ion-col size="10">
        <ion-text>
          Mandir
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        6
      </ion-text>
    </ion-col>
      <ion-col size="10">
        <ion-text>
          Satpurush
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
  <ion-col size="2">
      <ion-text>
        7
      </ion-text>
    </ion-col>
    <ion-col size="10">
      <ion-text>
        <b>Pick your own!</b>
      </ion-text>
    </ion-col>
  </ion-row>
</ion-grid>
<div>""",
    },
    'Tech Skills': {
      'Coding Challenge': """<div class="skills-html">
      <p>
        Any Kishore or Kishori interested in showcasing their talents in web/app development, data
        visualization, Artificial Intelligence, Machine Learning, or related topics should pursue this
        challenge. Participants must follow the rules outlined below to build and submit their project.
        Participants will be judged on the authenticity, usability, scalability, impact, and completeness
        of a problem they are solving through an application/code.
      </p>
      <h2 class="static-content-title">Rules</h2>
      <ul>
        <li>
          Participants can use any language of their choice.
        </li>
        <li>
          Participants can use any open source libraries to aid in their development.
        </li>
        <li>
          Submit a ZIP file containing the following <a href="https://github.com/msalia/baps-scraper" target="_blank"> (click here to see a sample submission
package):
</a>
</li>
<ul>
  <li>
    All files required for your project to work.
  </li>
  <li>
    Instructions on how to compile and run your project
  </li>
  <li>
    A video or screen recording showcasing your application. This video will be
used to help reviewers understand your project.
  </li>
  <li>
    A copy of your compiled project, if possible
  </li>
</ul>
<li>
  Your code must be readable by a human. Do not minify your code or submit binaries
that cannot be read by a human.
</li>
</ul>
<h2 class="static-content-title">Possible Topics</h2><h4>(not limited to)</h4>
<ion-grid class="ion-text-center">
  <ion-row class="header-row">
    <ion-col size="2">
      <ion-text>#</ion-text>
    </ion-col>
    <ion-col size="10">
      <ion-text>Topic</ion-text>
    </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        1
      </ion-text>
    </ion-col>
      <ion-col size="10">
        <ion-text>
          An interactive map of all North American (or worldwide) mandirs and centers
        </ion-text>
        <p>
          <a href="https://github.com/msalia/baps-scraper/blob/master/centers.json" target="_blank">Pre-compiled centers data can be found here.</a>
        </p>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        2
      </ion-text>
    </ion-col>
      <ion-col size="10">
        <ion-text>
          A “Today in Satsang History” app or website.
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        3
      </ion-text>
    </ion-col>
      <ion-col size="10">
        <ion-text>
          A family-friendly game app that can be used during Ghar Sabha
        </ion-text>
        <ion-text>
        Satsang Charades, Satsang Quiz App, Satsang Scrabble, Satsang-themed
Settlers of Catan, A game to aid in doing mukhpath, etc.
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        4
      </ion-text>
    </ion-col>
      <ion-col size="10">
        <ion-text>
Auto-Generation of word clouds using Vachanamrut / Swami Ni Vato / Satsang
Diksha words.
        </ion-text>
      </ion-col>
  </ion-row>
   <ion-row>
    <ion-col size="2">
      <ion-text>
        5
      </ion-text>
    </ion-col>
      <ion-col size="10">
        <ion-text>
          Satsang Diksha Study app.
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        6
      </ion-text>
    </ion-col>
      <ion-col size="10">
        <ion-text>
          A collaborative Satsang Journal app or website to save and share manan on
prasangs/katha/daily darshan/etc.
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        7
      </ion-text>
    </ion-col>
      <ion-col size="10">
        <ion-text>
          A website or app to enhance the virtual sunday sabha experience.
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
  <ion-col size="2">
      <ion-text>
        8
      </ion-text>
    </ion-col>
      <ion-col size="10">
        <ion-text>
          <b>Pick your own!</b>
        </ion-text>
      </ion-col>
  </ion-row>
</ion-grid>
      <div>""",
    }
}

# Satsang Diksha Tiers
# Contains set of SD shlokas in ghanshyam tier, indexed by title.
GHANSHYAM_SD_SHLOKAS = {
    "Shloka 1",
    "Shloka 4-5",
    "Shloka 8-9",
    "Shloka 24",
    "Shloka 64-65",
    "Shloka 73",
    "Shloka 76",
    "Shloka 96",
    "Shloka 97",
    "Shloka 98",
    "Shloka 106",
    "Shloka 100",
    "Shloka 212",
    "Shloka 209",
    "Shloka 152",
    "Shloka 128",
    "Shloka 149",
    "Shloka 116",
}

MAHANT_SD_SHLOKS = {
    "Shloka 1",
    "Shloka 2",
    "Shloka 3",
    "Shloka 4-5",
    "Shloka 6",
    "Shloka 7",
    "Shloka 8-9",
    "Shloka 10",
    "Shloka 18",
    "Shloka 19",
    "Shloka 22",
    "Shloka 23",
    "Shloka 24",
    "Shloka 25",
    "Shloka 64-65",
    "Shloka 73",
    "Shloka 96",
    "Shloka 97",
    "Shloka 98",
    "Shloka 99",
    "Shloka 100",
    "Shloka 102-103",
    "Shloka 104",
    "Shloka 105",
    "Shloka 106",
    "Shloka 107",
    "Shloka 108",
    "Shloka 109-110",
    "Shloka 111-114",
    "Shloka 115",
    "Shloka 116",
    "Shloka 131",
    "Shloka 132",
    "Shloka 134",
    "Shloka 135",
    "Shloka 139",
    "Shloka 140",
    "Shloka 141-142",
    "Shloka 145",
    "Shloka 146",
    "Shloka 147-148",
    "Shloka 149",
    "Shloka 150",
    "Shloka 151",
    "Shloka 152",
    "Shloka 164",
    "Shloka 209",
    "Shloka 210",
    "Shloka 212",
    "Shloka 213",
    "Shloka 225",
    "Shloka 256",
    "Shloka 274",
    "Shloka 291",
}

PRAMUKH_SD_SHLOKS = {
    "Shloka 1",
    "Shloka 2",
    "Shloka 3",
    "Shloka 4-5",
    "Shloka 6",
    "Shloka 7",
    "Shloka 8-9",
    "Shloka 10",
    "Shloka 18",
    "Shloka 19",
    "Shloka 22",
    "Shloka 23",
    "Shloka 24",
    "Shloka 25",
    "Shloka 44",
    "Shloka 45",
    "Shloka 46",
    "Shloka 47",
    "Shloka 48",
    "Shloka 59",
    "Shloka 64-65",
    "Shloka 73",
    "Shloka 87-88",
    "Shloka 89",
    "Shloka 90-91",
    "Shloka 92",
    "Shloka 96",
    "Shloka 97",
    "Shloka 98",
    "Shloka 99",
    "Shloka 100",
    "Shloka 102-103",
    "Shloka 104",
    "Shloka 105",
    "Shloka 106",
    "Shloka 107",
    "Shloka 108",
    "Shloka 109-110",
    "Shloka 111-114",
    "Shloka 115",
    "Shloka 116",
    "Shloka 126",
    "Shloka 127",
    "Shloka 128",
    "Shloka 131",
    "Shloka 132",
    "Shloka 134",
    "Shloka 135",
    "Shloka 136",
    "Shloka 137",
    "Shloka 138",
    "Shloka 139",
    "Shloka 140",
    "Shloka 141-142",
    "Shloka 143-144",
    "Shloka 145",
    "Shloka 146",
    "Shloka 147-148",
    "Shloka 149",
    "Shloka 150",
    "Shloka 151",
    "Shloka 152",
    "Shloka 159",
    "Shloka 160",
    "Shloka 164",
    "Shloka 180",
    "Shloka 183",
    "Shloka 184",
    "Shloka 185",
    "Shloka 188",
    "Shloka 195",
    "Shloka 209",
    "Shloka 210",
    "Shloka 212",
    "Shloka 213",
    "Shloka 216",
    "Shloka 225",
    "Shloka 233",
    "Shloka 236",
    "Shloka 252",
    "Shloka 253",
    "Shloka 256",
    "Shloka 274",
    "Shloka 277",
    "Shloka 279",
    "Shloka 287",
    "Shloka 291",
}

YOGI_SD_SHLOKS = {
    "Shloka 1",
    "Shloka 2",
    "Shloka 3",
    "Shloka 4-5",
    "Shloka 6",
    "Shloka 7",
    "Shloka 8-9",
    "Shloka 10",
    "Shloka 11",
    "Shloka 12",
    "Shloka 13",
    "Shloka 17",
    "Shloka 18",
    "Shloka 19",
    "Shloka 22",
    "Shloka 23",
    "Shloka 24",
    "Shloka 25",
    "Shloka 26",
    "Shloka 29",
    "Shloka 31",
    "Shloka 32",
    "Shloka 33-34",
    "Shloka 38",
    "Shloka 44",
    "Shloka 45",
    "Shloka 46",
    "Shloka 47",
    "Shloka 48",
    "Shloka 50",
    "Shloka 59",
    "Shloka 64-65",
    "Shloka 73",
    "Shloka 76",
    "Shloka 81",
    "Shloka 82",
    "Shloka 83",
    "Shloka 84",
    "Shloka 86",
    "Shloka 87-88",
    "Shloka 89",
    "Shloka 90-91",
    "Shloka 92",
    "Shloka 94",
    "Shloka 95",
    "Shloka 96",
    "Shloka 97",
    "Shloka 98",
    "Shloka 99",
    "Shloka 100",
    "Shloka 102-103",
    "Shloka 104",
    "Shloka 105",
    "Shloka 106",
    "Shloka 107",
    "Shloka 108",
    "Shloka 109-110",
    "Shloka 111-114",
    "Shloka 115",
    "Shloka 116",
    "Shloka 117",
    "Shloka 120",
    "Shloka 122",
    "Shloka 123",
    "Shloka 124",
    "Shloka 125",
    "Shloka 126",
    "Shloka 127",
    "Shloka 128",
    "Shloka 129-130",
    "Shloka 131",
    "Shloka 132",
    "Shloka 133",
    "Shloka 134",
    "Shloka 135",
    "Shloka 136",
    "Shloka 137",
    "Shloka 138",
    "Shloka 139",
    "Shloka 140",
    "Shloka 141-142",
    "Shloka 143-144",
    "Shloka 145",
    "Shloka 146",
    "Shloka 147-148",
    "Shloka 149",
    "Shloka 150",
    "Shloka 151",
    "Shloka 152",
    "Shloka 153",
    "Shloka 154",
    "Shloka 156-157",
    "Shloka 158",
    "Shloka 159",
    "Shloka 160",
    "Shloka 161",
    "Shloka 162",
    "Shloka 163",
    "Shloka 164",
    "Shloka 165",
    "Shloka 166",
    "Shloka 167",
    "Shloka 168",
    "Shloka 170",
    "Shloka 171",
    "Shloka 173",
    "Shloka 174",
    "Shloka 175",
    "Shloka 176",
    "Shloka 177",
    "Shloka 178",
    "Shloka 179",
    "Shloka 180",
    "Shloka 181",
    "Shloka 182",
    "Shloka 183",
    "Shloka 184",
    "Shloka 185",
    "Shloka 186",
    "Shloka 187",
    "Shloka 188",
    "Shloka 189",
    "Shloka 192",
    "Shloka 193",
    "Shloka 195",
    "Shloka 200",
    "Shloka 203",
    "Shloka 204",
    "Shloka 205",
    "Shloka 206",
    "Shloka 207",
    "Shloka 209",
    "Shloka 210",
    "Shloka 212",
    "Shloka 213",
    "Shloka 215",
    "Shloka 216",
    "Shloka 223",
    "Shloka 224",
    "Shloka 225",
    "Shloka 233",
    "Shloka 236",
    "Shloka 237-238",
    "Shloka 239",
    "Shloka 240",
    "Shloka 241-242",
    "Shloka 243",
    "Shloka 244",
    "Shloka 245",
    "Shloka 248",
    "Shloka 249",
    "Shloka 250",
    "Shloka 251",
    "Shloka 252",
    "Shloka 253",
    "Shloka 254",
    "Shloka 255",
    "Shloka 256",
    "Shloka 258-259",
    "Shloka 260",
    "Shloka 261",
    "Shloka 262",
    "Shloka 263",
    "Shloka 268",
    "Shloka 274",
    "Shloka 275",
    "Shloka 277",
    "Shloka 279",
    "Shloka 287",
    "Shloka 288-290",
    "Shloka 291",
    "Shloka 293-294",
    "Shloka 295-296",
    "Shloka 297-298",
    "Shloka 309-310",
}

SHASTRI_SD_SHLOKS = {
    "Shloka 1",
    "Shloka 2",
    "Shloka 3",
    "Shloka 4-5",
    "Shloka 6",
    "Shloka 7",
    "Shloka 8-9",
    "Shloka 10",
    "Shloka 11",
    "Shloka 12",
    "Shloka 13",
    "Shloka 14-16",
    "Shloka 17",
    "Shloka 18",
    "Shloka 19",
    "Shloka 20",
    "Shloka 21",
    "Shloka 22",
    "Shloka 23",
    "Shloka 24",
    "Shloka 25",
    "Shloka 26",
    "Shloka 27",
    "Shloka 28",
    "Shloka 29",
    "Shloka 30",
    "Shloka 31",
    "Shloka 32",
    "Shloka 33-34",
    "Shloka 35",
    "Shloka 36",
    "Shloka 37",
    "Shloka 38",
    "Shloka 39",
    "Shloka 40",
    "Shloka 41",
    "Shloka 42",
    "Shloka 43",
    "Shloka 44",
    "Shloka 45",
    "Shloka 46",
    "Shloka 47",
    "Shloka 48",
    "Shloka 49",
    "Shloka 50",
    "Shloka 51",
    "Shloka 52",
    "Shloka 53-54",
    "Shloka 55",
    "Shloka 56-58",
    "Shloka 59",
    "Shloka 60",
    "Shloka 61",
    "Shloka 62",
    "Shloka 63",
    "Shloka 64-65",
    "Shloka 66-67",
    "Shloka 68",
    "Shloka 69",
    "Shloka 70",
    "Shloka 71",
    "Shloka 72",
    "Shloka 73",
    "Shloka 74",
    "Shloka 75",
    "Shloka 76",
    "Shloka 77",
    "Shloka 78",
    "Shloka 79-80",
    "Shloka 81",
    "Shloka 82",
    "Shloka 83",
    "Shloka 84",
    "Shloka 85",
    "Shloka 86",
    "Shloka 87-88",
    "Shloka 89",
    "Shloka 90-91",
    "Shloka 92",
    "Shloka 94",
    "Shloka 93",
    "Shloka 95",
    "Shloka 96",
    "Shloka 97",
    "Shloka 98",
    "Shloka 99",
    "Shloka 100",
    "Shloka 101",
    "Shloka 102-103",
    "Shloka 104",
    "Shloka 105",
    "Shloka 106",
    "Shloka 107",
    "Shloka 108",
    "Shloka 109-110",
    "Shloka 111-114",
    "Shloka 115",
    "Shloka 116",
    "Shloka 117",
    "Shloka 118",
    "Shloka 119",
    "Shloka 120",
    "Shloka 121",
    "Shloka 122",
    "Shloka 123",
    "Shloka 124",
    "Shloka 125",
    "Shloka 126",
    "Shloka 127",
    "Shloka 128",
    "Shloka 129-130",
    "Shloka 131",
    "Shloka 132",
    "Shloka 133",
    "Shloka 134",
    "Shloka 135",
    "Shloka 136",
    "Shloka 137",
    "Shloka 138",
    "Shloka 139",
    "Shloka 140",
    "Shloka 141-142",
    "Shloka 143-144",
    "Shloka 145",
    "Shloka 146",
    "Shloka 147-148",
    "Shloka 149",
    "Shloka 150",
    "Shloka 151",
    "Shloka 152",
    "Shloka 153",
    "Shloka 154",
    "Shloka 155",
    "Shloka 156-157",
    "Shloka 158",
    "Shloka 159",
    "Shloka 160",
    "Shloka 161",
    "Shloka 162",
    "Shloka 163",
    "Shloka 164",
    "Shloka 165",
    "Shloka 166",
    "Shloka 167",
    "Shloka 168",
    "Shloka 169",
    "Shloka 170",
    "Shloka 171",
    "Shloka 172",
    "Shloka 173",
    "Shloka 174",
    "Shloka 175",
    "Shloka 176",
    "Shloka 177",
    "Shloka 178",
    "Shloka 179",
    "Shloka 180",
    "Shloka 181",
    "Shloka 182",
    "Shloka 183",
    "Shloka 184",
    "Shloka 185",
    "Shloka 186",
    "Shloka 187",
    "Shloka 188",
    "Shloka 189",
    "Shloka 190",
    "Shloka 191",
    "Shloka 192",
    "Shloka 193",
    "Shloka 194",
    "Shloka 195",
    "Shloka 196",
    "Shloka 197",
    "Shloka 198",
    "Shloka 199",
    "Shloka 200",
    "Shloka 201-202",
    "Shloka 203",
    "Shloka 204",
    "Shloka 205",
    "Shloka 206",
    "Shloka 207",
    "Shloka 208",
    "Shloka 209",
    "Shloka 210",
    "Shloka 211",
    "Shloka 212",
    "Shloka 213",
    "Shloka 214",
    "Shloka 215",
    "Shloka 216",
    "Shloka 217",
    "Shloka 218-219",
    "Shloka 220",
    "Shloka 221",
    "Shloka 222",
    "Shloka 223",
    "Shloka 224",
    "Shloka 225",
    "Shloka 226",
    "Shloka 227",
    "Shloka 228",
    "Shloka 229",
    "Shloka 230",
    "Shloka 231",
    "Shloka 232",
    "Shloka 233",
    "Shloka 234",
    "Shloka 235",
    "Shloka 236",
    "Shloka 237-238",
    "Shloka 239",
    "Shloka 240",
    "Shloka 241-242",
    "Shloka 243",
    "Shloka 244",
    "Shloka 245",
    "Shloka 246",
    "Shloka 247",
    "Shloka 248",
    "Shloka 249",
    "Shloka 250",
    "Shloka 251",
    "Shloka 252",
    "Shloka 253",
    "Shloka 254",
    "Shloka 255",
    "Shloka 256",
    "Shloka 257",
    "Shloka 258-259",
    "Shloka 260",
    "Shloka 261",
    "Shloka 262",
    "Shloka 263",
    "Shloka 264-265",
    "Shloka 266",
    "Shloka 267",
    "Shloka 268",
    "Shloka 269",
    "Shloka 270",
    "Shloka 271",
    "Shloka 272-273",
    "Shloka 274",
    "Shloka 275",
    "Shloka 276",
    "Shloka 277",
    "Shloka 278",
    "Shloka 279",
    "Shloka 280",
    "Shloka 281",
    "Shloka 282",
    "Shloka 283-284",
    "Shloka 285",
    "Shloka 286",
    "Shloka 287",
    "Shloka 288-290",
    "Shloka 291",
    "Shloka 292",
    "Shloka 293-294",
    "Shloka 295-296",
    "Shloka 297-298",
    "Shloka 299",
    "Shloka 300",
    "Shloka 301",
    "Shloka 302",
    "Shloka 303",
    "Shloka 304",
    "Shloka 305",
    "Shloka 306",
    "Shloka 307",
    "Shloka 308",
    "Shloka 309-310",
    "Shloka 311-314",
    "Shloka 315",
}

SD_SHLOKAS_FOR_TIER = {
    GHANSHYAM: GHANSHYAM_SD_SHLOKAS,
    MAHANT: MAHANT_SD_SHLOKS,
    PRAMUKH: PRAMUKH_SD_SHLOKS,
    YOGI: YOGI_SD_SHLOKS,
    SHASTRI: SHASTRI_SD_SHLOKS,
}


# For Quotes, use background gradient from this list
# Gradients: https://digitalsynopsis.com/design/beautiful-color-ui-gradients-backgrounds/
#   0: "linear-gradient(#42275a, #734b6d)", // Mauve
#   1: "linear-gradient(#de6262, #ffb88c)", // A Lost Memory
#   2: "linear-gradient(#06beb6, #48b1bf)", // Socialive
#   3: "linear-gradient(#dd5e89, #f7bb97)", // Pinky
#   4: "linear-gradient(#614385, #516395)", // Kashmir
#   5: "linear-gradient(#02aab0, #00cdac)", // Green Beach
#   6: "linear-gradient(#d66d75, #e29587)", // Sha La La
#   7: "linear-gradient(#4568dc, #b06ab3)", // Can you feel the love tonight
#   8: "linear-gradient(#36d1dc, #5b86e5)", // Scooter
#   9: "linear-gradient(#141e30, #243b55)", // Royal

BM_STORIES = [
  {
    "title": "Word of the Week",
    "url": "https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/Stories/KM/Word-of-the-Week/word%20of%20the%20week.png",
    "stories": [
      {
        "url": 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/Stories/KM/Word-of-the-Week/Word%20of%20the%20Week%283_21%29.mp4',
        "type": "video"
      },
    ]
  },
  {
    "title": "Quote of the Week",
    "url": "https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/Stories/KM/Quote-of-the-Week/Static%20Image_Quote%20of%20the%20Week.jpg",
    "stories": [
      {
        "url": 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/Stories/KM/Quote-of-the-Week/Quote%20of%20the%20Week%20%284_5%29.jpg',
        "type": "image"
      },
    ]
  },
  {
    "title": "Guidance from Swāmishri",
    "url": "https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/KM%20Module%20Photos/extra5.jpg",
    "stories": [
      {
        "url": "https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/Stories/KM/Insights-from-Swamishri/Insights%20from%20Swamishri%20Final%283_21%29.mp4",
        "type": "video"
      },
      {
        'url': 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/Stories/KM/Insights-from-Swamishri/Insights%20from%20SwamiShri%20%283_8%29.mp4',
        'type': 'video'
      },
      {
        "url": 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/Stories/KM/Insights-from-Swamishri/insight.mp4',
        "type": "video"
      },
    ]
  },
  {
    "title": "Divine Moods",
    "url": "https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/KM%20Module%20Photos/extra2.jpg",
    "stories": [
      {
        'url': 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/Stories/KM/Divine-Moods/Divine%20Moods%20%283_21%29.mp4',
        'type': 'video'
      },
      {
        'url': 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/Stories/KM/Divine-Moods/Divine%20Moods%20%283_15%29.mp4',
        'type': 'video'
      },
      {
        'url': 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/Stories/KM/Divine-Moods/Divine%20Moods%20%283_8%29.mp4',
        'type': 'video'
      },
      {
        "url": 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/Stories/KM/Divine-Moods/yt1s_com_Guruhari_Darshan_1113_Jan_2021_Nenpur_India_1080p_3.mp4',
        "type": "video"
      },
      # {
      #   "url": 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/KM%20Module%20Photos/14agna.jpg',
      #   "quote": "Some Inspiring Quote...\n-Some Great Person",
      #   "type": "quote",
      # }
    ]
  },
  {
    "title": "Swāmishri Blessing the App",
    "url": "https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/Stories/KM/Opening/2021_01_26_0274.JPG",
    "stories": [
      {
        "url": 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/Stories/KM/Opening/2021_01_26_0274.JPG',
        "type": "image"
      },
      {
        "url": 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/Stories/KM/Opening/2021_01_26_0320.JPG',
        "type": "image"
      },
      {
        "url": 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/Stories/KM/Opening/2021_01_26_0286.JPG',
        "type": "image"
      },
      {
        "url": 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/Stories/KM/Opening/2021_01_26_0277.JPG',
        "type": "image"
      },
      {
        "url": 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/Stories/KM/Opening/2021_01_26_0268.JPG',
        "type": "image"
      },
    ]
  },
  {
    "title": "History of Adhiveshan",
    "url": "https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/Stories/KM/History-Adhiveshan/Screen%20Shot%202021-01-25%20at%2011.52.17%20AM.png",
    "stories": [
      {
        "url": 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/Stories/KM/History-Adhiveshan/historyv2.mp4',
        "type": "video"
      },
    ]
  },
  {
    "title": "Swāmishri with Children",
    "url": "https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/KM%20Module%20Photos/quicklink1.jpg",
    "stories": [
      {
        "url": 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/Stories/BM/Memories/2017_06_26_Vicharan__Atlanta_14_001.jpg',
        "type": "image"
      },
      {
        "url": 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/Stories/BM/Memories/2017_06_26_Vicharan__Atlanta_15.jpg',
        "type": "image"
      },
      {
        "url": 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/Stories/BM/Memories/2017_06_26_Vicharan__Atlanta_25.jpg',
        "type": "image"
      },
      {
        "url": 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/Stories/BM/Memories/chicago_MSMBalDin_10.jpg',
        "type": "image"
      },
      {
        "url": 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/Stories/BM/Memories/chicago_MSMBalDin_21.jpg',
        "type": "image"
      },
      {
        "url": 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/Stories/BM/Memories/chicago_MSMBalDin_25.jpg',
        "type": "image"
      },
      {
        "url": 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/Stories/BM/Memories/chicago_MSMBalDin_8.jpg',
        "type": "image"
      },
      {
        "url": 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/Stories/BM/Memories/Houston_MSMBalDin_27.jpg',
        "type": "image"
      },
    ]
  },
]

# For Quotes, use background gradient from this list
# Gradients: https://digitalsynopsis.com/design/beautiful-color-ui-gradients-backgrounds/
#   0: "linear-gradient(#42275a, #734b6d)", // Mauve
#   1: "linear-gradient(#de6262, #ffb88c)", // A Lost Memory
#   2: "linear-gradient(#06beb6, #48b1bf)", // Socialive
#   3: "linear-gradient(#dd5e89, #f7bb97)", // Pinky
#   4: "linear-gradient(#614385, #516395)", // Kashmir
#   5: "linear-gradient(#02aab0, #00cdac)", // Green Beach
#   6: "linear-gradient(#d66d75, #e29587)", // Sha La La
#   7: "linear-gradient(#4568dc, #b06ab3)", // Can you feel the love tonight
#   8: "linear-gradient(#36d1dc, #5b86e5)", // Scooter
#   9: "linear-gradient(#141e30, #243b55)", // Royal

KM_STORIES = [
  {
    "title": "Word of the Week",
    "url": "https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/Stories/KM/Word-of-the-Week/word%20of%20the%20week.png",
    "stories": [
      {
        "url": 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/Stories/KM/Word-of-the-Week/Word%20of%20the%20Week%283_21%29.mp4',
        "type": "video"
      },
    ]
  },
  {
    "title": "Quote of the Week",
    "url": "https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/Stories/KM/Quote-of-the-Week/Static%20Image_Quote%20of%20the%20Week.jpg",
    "stories": [
      {
        "url": 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/Stories/KM/Quote-of-the-Week/Quote%20of%20the%20Week%20%284_5%29.jpg',
        "type": "image"
      },
    ]
  },
  {
    "title": "Insights from Swāmishri",
    "url": "https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/KM%20Module%20Photos/extra5.jpg",
    "stories": [
      {
        "url": "https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/Stories/KM/Insights-from-Swamishri/Insights%20from%20Swamishri%20Final%283_21%29.mp4",
        "type": "video"
      },
      {
        "url": 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/Stories/KM/Insights-from-Swamishri/Insights%20From%20Swamishri%20%283_15%29.mp4',
        "type": "video"
      },
      {
        "url": 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/Stories/KM/Insights-from-Swamishri/Insights%20from%20SwamiShri%20%283_8%29.mp4',
        "type": "video"
      },
      {
        "url": 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/Stories/KM/Insights-from-Swamishri/insight.mp4',
        "type": "video"
      },
    ]
  },
  {
    "title": "Divine Moods",
    "url": "https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/KM%20Module%20Photos/extra2.jpg",
    "stories": [
      {
        'url': 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/Stories/KM/Divine-Moods/Divine%20Moods%20%283_21%29.mp4',
        'type': 'video'
      },
      {
        'url': 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/Stories/KM/Divine-Moods/Divine%20Moods%20%283_15%29.mp4',
        'type': 'video'
      },
      {
        'url': 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/Stories/KM/Divine-Moods/Divine%20Moods%20%283_8%29.mp4',
        'type': 'video'
      },
      {
        "url": 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/Stories/KM/Divine-Moods/yt1s_com_Guruhari_Darshan_1113_Jan_2021_Nenpur_India_1080p_3.mp4',
        "type": "video"
      },
      # {
      #   "url": 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/KM%20Module%20Photos/14agna.jpg',
      #   "quote": "Some Inspiring Quote...\n-Some Great Person",
      #   "type": "quote",
      # }
    ]
  },
  {
    "title": "Swāmishri Blessing the App",
    "url": "https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/Stories/KM/Opening/2021_01_26_0274.JPG",
    "stories": [
      {
        "url": 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/Stories/KM/Opening/2021_01_26_0274.JPG',
        "type": "image"
      },
      {
        "url": 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/Stories/KM/Opening/2021_01_26_0320.JPG',
        "type": "image"
      },
      {
        "url": 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/Stories/KM/Opening/2021_01_26_0286.JPG',
        "type": "image"
      },
      {
        "url": 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/Stories/KM/Opening/2021_01_26_0277.JPG',
        "type": "image"
      },
      {
        "url": 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/Stories/KM/Opening/2021_01_26_0268.JPG',
        "type": "image"
      },
    ]
  },
  {
    "title": "History of Adhiveshan",
    "url": "https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/Stories/KM/History-Adhiveshan/Screen%20Shot%202021-01-25%20at%2011.52.17%20AM.png",
    "stories": [
      {
        "url": 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/Stories/KM/History-Adhiveshan/historyv2.mp4',
        "type": "video"
      },
    ]
  },
]

BM_ANNOUNCEMENTS = [
    {
        'timestamp': '5 Apr, 2021',
        'text': 'For both Rajipo and Gurubhakti challenge:\n\n1. Everything may be memorized in any language: Sanskrit, Gujarati, or English. \n\n 2. While encouraged, you do not need to memorize the translations/meanings for any mukhpath. \n\n 3. You will not be tested on references for any mukhpath.'
    },
    {
        'timestamp': '7 Feb, 2021',
        'text': 'You can now access Satsang Diksha material in Sanskrit by updating the application or going to the website. Remember to notify your local karyakar if you decide to memorize Satsang Diksha in Sanskrit.'
    }
]

KM_ANNOUNCEMENTS = [
    {
        'timestamp': '5 Apr, 2021',
        'text': 'For both Rajipo and Gurubhakti challenge:\n\n1. Everything may be memorized in any language: Sanskrit, Gujarati, or English. \n\n 2. While encouraged, you do not need to memorize the translations/meanings for any mukhpath. \n\n 3. You will not be tested on references for any mukhpath.'
    },
    {
        'timestamp': '7 Feb, 2021',
        'text': 'You can now access Satsang Diksha material in Sanskrit by updating the application or going to the website. Remember to notify your local karyakar if you decide to memorize Satsang Diksha in Sanskrit.'
    }
]

BM_ADHIVESHAN_DATES = {
  'west': '7/10/2021',
  'southeast': '7/17/2021',
  'southwest': '7/24/2021',
  'midwest': '8/7/2021',
  'northeast': '8/7/2021',
  'canada': '8/7/2021',
}

KM_ADHIVESHAN_DATES = {
  'west': '7/17/2021',
  'northeast': '7/31/2021',
  'southeast': '7/10/2021',
  'canada': '7/31/2021',
  'southwest': '7/31/2021',
  'midwest': '7/31/2021',
}

BM_ANNOUNCEMENT_PAGE_CONTENT = {
    'announcements': BM_ANNOUNCEMENTS,
    'stories': BM_STORIES,
    'adhiveshanDates': BM_ADHIVESHAN_DATES
}

KM_ANNOUNCEMENT_PAGE_CONTENT = {
    'announcements': KM_ANNOUNCEMENTS,
    'stories': KM_STORIES,
    'adhiveshanDates': KM_ADHIVESHAN_DATES,
}
