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
            'answer': '<b>Adhiveshan is a structured way of memorizing mukhpath, or scriptural references or quotations, which is focused on a certain satsang topics or themes.</b> Adhiveshan is NOT a competition, but rather a challenge for ourselves to sacrifice our time to memorize the mukhpath, learn its meaning, and eventually imbibe it in our lives to please our Guru.',
        },
        {
            'question': 'Why do we do Adhiveshans?',
            'answer': 'Adhiveshan has been very dear to the hearts of our Gurus. Starting with Yogi Bapa’s passion for balaks and balikas to memorize mukhpath during their summer vacations to the various Adhiveshans held with Pramukh Swami Maharaj and Mahant Swami Maharaj, memorizing and understanding mukhpath has been an integral way for balaks and balikas to earn the rajipo of our Gurus. <br/><br/> By learning and memorizing various parts of our shastras (scriptures), we are able to ground ourselves in the Akshar Purushottam Darshan and better understand our beliefs and principles. Mukhpath also helps us find solutions to the many problems we may face in life.  <br/><br/> This Adhiveshan will be paired with Summer Shibir 2021 along the theme of Guru Bhakti. We offer this mukhpath as a form of guru bhakti to our gurus Pramukh Swami Maharaj and Mahant Swami Maharaj. <br/><br/> Along with this, this Adhiveshan will also help us gear up for the upcoming Pramukh Swami Maharaj Shatabdi Mahotsav and Aksharsham Mahotsav.',
        },
        {
            'question': 'Which Adhiveshan do I pledge for and which Summer Shibir do I go to?',
            'answer': 'You will pledge for the tiers in the group you currently are in (<b>as of January 2021</b>). For example, if you are in Group 2 in January of 2021, and even if you are graduating and moving to Group 3 in September 2021, you will pledge for Adhiveshan in the Group 2 categories. Anyone in Groups 1-3 ( as of January 2021) will also attend the <b>Bal/Balika Summer Shibir</b>. <br/><br/><b>NOTE</b>: Current 8th graders will pledge for the Kishore/Kishori Adhiveshan',
        },
        {
            'question': 'What does Adhiveshan consist of?',
            'answer': 'Adhiveshan will have three parts, each assessed in different ways and at different times throughout the spring and summer months: <br/> <ul> <li>The first part is the <b>Beginner’s Challenge</b> (traditionally known as Prathmik Mukhpath) which will be assessed at home.</li><li>The second part is the <b>Adhiveshan Rajipo Challenge</b> (traditionally known as Advance Mukhpath), which will be assessed online (in real time - over a video conferencing platform).</li><li>The final part is the <b>Skills Challenge</b> (traditionally known as Talent Competitions), which will be judged through regional online submissions.</li></ul>',
        },
    ],
    'Website/App': [
      {
            'question': "Do I still need to pledge on BKMS if I pledge here?",
            'answer': "Yes. The website is a supporting tool to help balaks and balikas explore the mukhpath so that they can make an informed pledge. The pledge will be done through BKMS and the deadline is March 7th, 2021.",
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
            'question': "How can I edit my pledge",
            'answer': "<p>Go to My Progress page.</p><ul><li>Click on Edit My Pledge.</li><li>Change your pledge.</li><li>Note: This won’t change your pledge on BKMS, which is where all official pledging takes place.</li></ul>",
      },
      {
            'question': "How can I reset my mukhpath progress?",
            'answer': "<p>Go to the Settings page.</p><ul><li>Click on Reset Memorized button</li</ul>",
      },
      {
            'question': "What if I have multiple users in my family but a limited number of devices?",
            'answer': "<p>We recommend that one user stay logged in via the app and another can use the mobile browser to login to the website.</p><p>Alternatively, you can log out each time someone needs to use the account.</p><p>We also recommend that parents print out small sections for kids to review on their own.</p><p>It’s not necessary to print out everything as the books will be provided around March.</p><ul><li>To print, please go to the “My Mukhpath” tab and you will be able to click “Print My Mukhpath” to print the mukhpath that you selected in the 'All Mukhpath' tab.</li></ul>",
      },
    ],
    'Beginner’s Challenge': [
        {
            'question': "What is the Beginner\'s Challenge?",
            'answer': 'The Beginners Challenge contains the core mukhpath of our sanstha, <b>including the Shri Swaminarayan Arti and shlokas we sing in puja</b>. All of the mukhpath comes with translations, so it is important to pay close attention to the meanings and try to introspect on how the values being transmitted in the words can be applied back to our lives. <br/><br/> The Beginners Challenge will be <b>administered at home</b>, wherein you all will complete a worksheet based on the <b>Gujarati transliteration and English translation</b> of the mukhpath. Your parents will aid in ensuring that you have completed the worksheet properly and assist in grading. <br/><br/> <b>NOTE</b>: Group 0 balaks/balikas will be exempt from the Beginner’s Challenge, however parents may choose to review this key mukhpath with their balaks/balikas.',
        },
    ],
    'Adhiveshan Rajipo Challenge': [
        {
            'question': "How is the Adhiveshan Rajipo Challenge structured?",
            'answer': 'The Adhiveshan Rajipo Challenge is broken up into 5 categories: Satsang Diksha, Swamini Vato, Kirtans, Shlokas and Sakhis, and Prasang Manan. <br/><br/> There are 4 tiers that you can choose from in each category: Mahant, Pramukh, Yogi, and Shastriji. <br/><br/> The breakdown for how much mukhpath you must memorize for each tier can be found under the “Edit My Pledge” section or in the FAQ section in your physical booket. You will also find a similar image to the one in your physical booklet below. <br/><br/> <b>NOTE</b>: There is an additional tier called the Ghanshyam tier that is ONLY if you are in Group 0. However, if you are in Group 1, you can select the Ghanshyam tier ONLY for Satsang Diksha (for the other categories, you must pick from the normal 4 tiers).',
        },
        {
            'question': "Is there a minimum number of tiers/categories needed to participate in the Adhiveshan?",
            'answer': 'As per Swamishri’s ruchi (wish), the focus of this Adhiveshan is to learn, understand, and imbibe various satsang shastras in the lives of balaks and balikas. <br/><br/> Thus, there is <b>no mandatory minimum amount</b> of categories you need to pledge to be able to participate in the Adhiveshan. It is recommended that you pledge for 2 or more categories. <br/><br/> Although, you should still strive to pledge for as many categories as you can and push yourselves to strive for higher tiers to make Swamishri extra raji.',
        },
        {
            'question': "Can we choose which items to memorize in each category?",
            'answer': '<b>The Satsang Diksha category is the only category that will have a set number of shlokas for each tier</b>. For example if you choose the Mahant Challenge for the Satsang Diksha category, there will be a pre-set list of 64 shlokas.<br/><br/> For all of the other categories (Swamini Vato, Shloka/Sakhi, Kirtan, Prasang Manan), you will have a choice in creating your own set with the available list of mukhpath</b>. For example, if you are a Group 1 balak or balika who wants to do the Yogi challenge for Kirtans, you will be able to choose any 4 out of a possible list of 15 kirtans listed in the book. ',
        },
    ],
    'Skills Challenge': [
        {
            'question': "What is the Skills Challenge?",
            'answer': 'The Skills Challenge allows you to tie your passions and hobbies back to Satsang. You will have a chance to show your talents in a multitude of fashions included in the mukhpath booklet. You will be able to <b>choose a minimum of 1 and a maximum of 3 skills challenges.</b><br/><br/><b>NOTE:</b> Group 0 balaks/balikas will not participate in Skills Challenge.<br/><br/>More details on the rules and regulations for each of the specific skills challenges will be provided shortly.',
        },
    ],
    'Adhiveshan Pledging': [
        {
            'question': "How can I pledge for Adhiveshan?",
            'answer': 'You will be able to pledge for Adhiveshan through BKMS after the Launch Sabha at the end of January. You will be able to access this link and must submit your final pledges <b>by 3/7/21</b>.<br/><br/>Before this date, please read through the Adhiveshan book or visit the website to take a look at the tiers for your group to make a decision on what mukhpath you will be able to memorize by the summer.<br/><br/>NOTE: If you pledge for Satsang Diksha, you should try to continue with the tier you chose for your Rajipo Challenge from August 2020. If you would like to change it, there will be an opportunity for you to repledge your original Satsang Diksha pledge when you pledge for the other Adhiveshan categories.',
        },
        {
            'question': "Will there be additional material to help me study?",
            'answer': 'Along with the provided book, there will be additional material provided via a website including interactive aids to help memorize the Adhiveshan content. (Please ask you parents prior to creating an account on the website.)<br/><br/>Once you enter your information to sign-up for an account, you will be able to access mukhpath and pledge a tier for each category based on the group/grade you entered. This website is for your <b>personal use</b> in being able to memorize the mukhpath wherever you go! You can bookmark which mukhpath you want to memorize, listen to the audio, or even print it out!<br/><br/><b>NOTE: Pledging on the website does not replace pledging on BKMS. You must register and pledging on BKMS before 3/7/21.</b><br/><br/>As additional content is rolled out for Adhiveshan and SS21, you will be able to see the updates on the website dashboard and your local karyakars will provide you with updates.'
        },
    ],
    'Adhiveshan Timeline': [
        {
            'question': "What are some important dates to keep in mind relating to the Adhiveshan?",
            'answer': "<ul><li>Adhiveshan/Summer Shibir 2021 Launch Sabha: 1/31/2021</li><li>Adhiveshan Pledge and Summer Shibir Registration: 1/31/2021-3/7/2021</li><li>Beginners Challenge Quiz: TBD</li><li>Adhiveshan Rajipo Challenge: TBD</li><li>Skills Challenge Submission Deadline: TBD</li></ul><b>More information on specific dates, judging process, submission process, etc. will be provided to you by your local karyakars. If you have any questions, please contact your local karyakars.</b>",
        },
    ],
    'Summer Shibir': [
      {
            'question': "What is Summer Shibir",
            'answer': 'This summer, a one-day virtual Summer Shibir will be held on the theme of “Guru Bhakti.” Since you memorized mukhpath as a form of guru bhakti, this shibir will revolve around better understanding and loving our guru.<br/><br/>There will be a main Bal/Balika Shibir as well as a separate shibir for Group 0 balaks/balikas. The breakdown is as follows:<br/><br/>Those entering Grades 2-8 in Fall of 2022 will participate in the Bal/Balika Summer Shibir. Those entering Group 0 - Grade 1 in Fall of 2022 will participate in the Group 0 Shibir. <br/><br/> NOTE: This is the same breakdown as Adhiveshan.<br/><br/>More information on Summer Shibir 2021 will be provided at a later time.'
      }
    ]
}

KISHORE_FAQ = {
  'Adhiveshan Overview': [
    {
      'question': "What is this year’s shibir theme and how does it relate to Adhiveshan?",
      'answer': "This year’s shibir theme is Guru Bhakti. Understanding how to perform guru bhakti the same way our gurus have will be the primary focus of the shibir. One way to perform guru bhakti is to memorize and learn mukhpath with the thought of raajipano vichar. Thus, this adhiveshan is a way to show our guru bhakti and earn our guru’s Rajipo."
    },
    {
      'question': "What is Adhiveshan?",
      'answer': "Adhiveshan has been very dear to the hearts of our Gurus. Starting with Yogi Bapa’s passion for balaks and kishores to memorize mukhpath during their summer vacations to the various adhiveshans held with Pramukh Swami Maharaj and Mahant Swami Maharaj, mukhpath has been integral way for kishores and kishoris to earn the Rajipo of their gurus. Adhiveshan is a structured way of memorizing mukhpath which is often focused on a certain Satsang topic or theme. Adhiveshan is NOT a competition, but rather a challenge for ourselves to spend time memorizing the mukhpath, learning its meaning, and eventually imbibing it in our lives to please our gurus."
    },
    {
      'question': "How is the Adhiveshan structured?",
      'answer': "All components of adhiveshan will take place virtually this year. There will be four components to adhiveshan: the prathmik mukhpath, the Rajipo Challenge, the Guru Bhakti Challenge, and Skills Competitions."
    },
    {
      'question': "How will Adhiveshan testing work?",
      'answer': "Due to the current situation with the COVID-19 pandemic, Adhiveshan will also take place over a virtual setting. Weeks prior to the shibir, karyakars will join individual calls to test kishores and kishoris on their mukhpath as it is traditionally done during an in-person adhiveshan."
    },
  ],
  'Prathmik Mukhpath': [
    {
      'question': 'What is Prathmik Mukhpath?',
      'answer': "The Prathmik Mukhpath contains core mukhpath that kishores and kishoris encounter on a daily basis. All of the mukhpath comes with translations, so it is important to pay close attention, understand the meanings, and try to introspect on how the values being transmitted in the words can be applied back to our lives. The prathmik mukhpath for this year includes the Shri Swaminarayan Arti and the two puja shlokas provided in Satsang Diksha. Kishores and kishoris will be tested on the prathmik mukhpath, just like both mukhpath challenges."
    }
  ],
  'Rajipo Challenge': [
    {
      'question': "What is the Rajipo Challenge and how is it structured?",
      'answer': "The Adhiveshan Rajipo Challenge is one that kishore and kishoris have been working on since August 2020: the Satsang Diksha Rajipo Challenge. The Rajipo Challenge for the adhiveshan will test memorization and understanding of Satsang Diksha as well as encourage kishores and kishoris to further memorize Satsang Diksha as it is Swamishri’s inner wish. The tiering will work exactly the same as the current Rajipo Challenge."
    },
    {
      'question': "Should the current Rajipo Challenge (Satsang Diksha) be continued?",
      'answer': "Kishores and kishoris are encouraged to continue on with their Satsang Diksha Rajipo Challenge pledge. However, kishores and kishoris will have the opportunity to re-pledge beginning January 31st, 2021 if they’d like. The pledging will occur in the same fashion as it had been previously, with the four tiers being the same (Mahant, Pramukh, Yogiji, Shastri). Final pledging closes March 7th, 2021."
    },
  ],
  'Guru Bhakti Challenge': [
    {
      'question': 'What is the Guru Bhakti Challenge?',
      'answer': "The Adhiveshan Guru Bhakti Challenge exists in the form of topic-based modules with relevant mukhpath items in each module. The Guru Bhakti Challenge will have four tiers that delegates can choose to achieve: Bronze, Silver, Gold, and Platinum. The distinction between these tiers is solely based on the number of modules a delegate completes — 5 for bronze, 10 for silver, 15 for gold, and 20 for platinum. Specifically, each module will consist of Swamini Vato, Vachanamrut Quotations, Shloks/Sakhis, Satsang Diksha shloks, Kirtans, Prasangs, or other mukhpath organized under a unifying Satsang topic. In order to consider a module completed, a kishore or kishori must memorize any 4 out of the 10 items of mukhpath within the module. We hope that this freedom in selecting mukhpath will incentivize kishores and kishoris to memorize according to their personal interests."
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
      'question': "Is there a minimum amount of mukhpath needed to participate in the Adhiveshan?",
      'answer': "As per Swamishri’s ruchi, the focus of this Adhiveshan is to learn, understand, and imbibe various Satsang mukhpath in the lives of kishores and kishoris. Thus, outside of the prathmik mukhpath, there is no mandatory minimum amount of mukhpath that a particular kishore or kishori needs to pledge to be able to participate in the Adhiveshan. Although, karyakars should encourage kishores and kishoris to pledge for as much mukhpath as they can based on their time and ability."
    },
    {
      'question': "Can a kishore or kishori change their pledge mid-way?",
      'answer': "Kishores and kishoris will not be able to change their pledge after they have submitted their pledge. That being said, they will have from January 31st, 2021 (launch sabha day) to March 7th to select their pledge. Karyakars should encourage and follow-up with kishores and kishoris during these 5 weeks to take a glance at the Adhiveshan book and make a careful decision on what they will be able to memorize by the summer."
    },
    {
      'question': "Will a booklet and material be provided?",
      'answer': "All mukhpath content will be available via a website and mobile app. The website and mobile app will also include interactive aids to help memorize the mukhpath. The website will also contain small interactive quizzes to aid in memorization and self-evaluation. A hard-copy of the mukhpath booklet will be provided to kishores and kishoris shortly after the launch sabha on January 31st, 2021."
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
    'Story/Speech-Based Challenges': {
        'Mono-acting': """<div class="skills-html">
<p> Do you like to act? Do you like to talk? Mono-Acting is where you get to act out a famous incident from our Hindu shastras (scriptures) and satsang history based on the point-of-view of the main individual.</p>
<h2 class="static-content-title">Things to Keep in Mind</h2>
<ul> 
	<li>
		You will take on the role of one person from the scene (for most scenes this is provided), 
    and enact the scene from that person's point of view.
	</li>
	<li>The act must be memorized. Notes will not be allowed.</li>
	<li>Balaks must choose the bal options and balikas must choose the balika options from the list.</li>
	<li>
		Mono-acting will be judged on: accurate portrayal of the incident, 
    acting, tone, emotion, facial expressions, memorization, props/costume/creativity, etc.
	</li>
	<li>
Topic list, submission details and grading rubric will be provided on the website soon. 	</li>
</ul>
<div>""",
        'Storytelling': """<div class="skills-html">
<p> Storytelling is where you get to narrate a story in vivid detail and include your own personal reflection to the story. It requires confidence and creativity to make the story both interesting and informative!</p>
<h2 class="static-content-title">Things to Keep in Mind</h2>
<ul>
	<li>
    You must vividly and creatively tell the story in its entirety and provide a manan, or reflection to the story.	</li>
	<li>The story must be memorized. Notes will not be allowed.</li>
	<li>No props can be used.</li>
	<li>
		Storytelling will be judged on: storytelling ability, content, creativity, vivid details, manan/personal reflection, organization, flow, confidence, tone, etc.
	</li>
	<li>
Topic list, submission details and grading rubric will be provided on the website soon. 	</li>
</ul>
<div>""",
        'Satsang Diksha Nirupan': """<div class="skills-html">
<p> One of the newest skills challenge is the Satsang Diksha Nirupan. A nirupan is a short commentary on a shastra (scripture). The Satsang Diksha Nirupan is where you get to take a few shlokas from the Satsang Diksha and create an analysis and reflection by tying all the shlokas to a common theme. </p>
<h2 class="static-content-title">Things to Keep in Mind</h2>
<ul>
	<li>
    You will speak on a topic which is expanded upon in the Satsang Diksha. Sample shlokas related to the theme will be provided for guidance. 	</li>
	<li>The nirupan should include at least:</li>
  <ul>
	  <li>2 Satsang Diksha Shloks</li>
	  <li>
		1 prasang of Pramukh Swami Maharaj or Mahant Swami Maharaj
	  </li>
    <li>
    A personal manan (analysis/reflection on how it relates to your life)
    </li>
  </ul>
  <li>
    The nirupan must be memorized. Notes will not be allowed.
  </>
	<li>
		Nirupan will be judged on: accurate use of mukhpath and prasangs, organization, flow, confidence, tone, etc.
	</li>
	<li>
    Topic list, submission details and grading rubric will be provided on the website soon. 	</li>
</ul>
<div>""",
        'Prasang-Varnan': """<div class="skills-html">
<p> The Prasang Varnan competition is similar to the Prasang Manan mukhpath category within the Adhiveshan Rajipo Challenge. You must narrate a prasang, or divine incident of Bhagwan and the Satpurush, in detail and explain what virtues you saw in the prasang and how it relates to your life. </p>
<h2 class="static-content-title">Things to Keep in Mind</h2>
<ul>
	<li>
    You will narrate a prasang and provide a manan, or personal reflection, on the prasang by incorporating at least 1 mukhpath reference that you had memorized.
	</li>
	<li>The prasang-varnan should include at least:</li>
  <ul>
	  <li>
		1 key prasang
	  </li>
	  <li>
		1 mukhpath reference
    </li>
    <li>
    A personal manan (reflection)
    </li>
  </ul>
  <li>
  The prasang-varnan must be memorized. Notes will not be allowed.
  </li>
  <li>
  Prasang-varnan will be judged on: key prasang, accurate use of mukhpath, memorization, organization, vivid details, flow, confidence, tone, etc.
  </li>
  <li>
Topic list, submission details and grading rubric will be provided on the website soon.   </li>
</ul>""",
    },
    'Music-Based Challenges': {
        'Solo Singing': """<div class="skills-html">
<p> Kirtanam, or singing or listening to kirtans while remembering Bhagwan and the Sant, is one of the nine forms of bhakti according to the Shrimad Bhagvat. Solo Singing will develop this type of bhakti by helping you not only memorize and sing one of your favorite kirtans, but also better understand the meaning behind the kirtan. </p>
<h2 class="static-content-title">Things to Keep in Mind</h2>
<ul>
	<li>
    You may select one of the bhajans that will be provided to you </li>
  <li>
    The bhajan must be memorized with the meaning.
  </li>
	<li>Along with the bhajan, you must include a manan (reflection) prior to singing the bhajan. This reflection can either be about the meaning of the bhajan, its history or what the bhajan means to you.</li>
  <li>
    Solo Singing will be judged on: sur (melody), tempo/rhythm, and tone/voice, along with your understanding of the kirtan that is spoken at the beginning, etc.  
  </li>
  <li>
    Bhajan list, submission details and grading rubric will be provided on the website soon.  
  </li>
</ul>
<div>""",
        'Musical Instruments': """<div class="skills-html">
<p> Some of us have been learning and practicing an instrument at school, so why not connect it to satsang? This challenge is to help you learn how to play a kirtan on a musical instrument that you may play, whether that be piano, harmonium, flute, trumpet, violin, tabla, or even shehnai! </p>
<h2 class="static-content-title">Things to Keep in Mind</h2>
<ul>
	<li>
    You can perform your instrument for one of the bhajans from the list that will be provided to you.  
  <li>
    The submission must include a manan (reflection) prior to singing the bhajan. This reflection can either be about the meaning of the bhajan, its history or what the bhajan means to you.
  </li>
	<li>
    You do not have to memorize the bhajan. You can have the music sheet in front of you while you play your instrument.
  </li>
	<li>
    You may play on any musical instrument that you know how to play, including but not limited to piano, tabla, flute, trumpet, violin, harmonium, etc.	</li>
	</li>
  <li>
    If you choose to play an instrument that is not melody-based, such as a percussion instrument like tabla, please have the bhajan audio playing in the background while you play.
  </li>
  <li>
    Musical Instrument will be judged on: sur (melody), tempo/rhythm, accuracy, tonality, etc.
  </li>
  <li>
    Bhajan list, submission details and grading rubric will be provided on the website soon.  </li>
</ul>
<div>""",
    },
    'Writing-Based Challenges': {
        'Poetry': """<div class="skills-html">
<p> Do you like writing? Do you like music? Why not put the two together! Poetry is where you get to use your imagination to convey a concept/message to others using creative language and rhythm. (Fun Fact: Did you know kirtans are also a form of poetry?) </p>
<h2 class="static-content-title">Things to Keep in Mind</h2>
<ul>
	<li>
    You must select from one of the themes that will be provided to you. 
  </li>
	<li>
    Although there are many different types of poetic form, please limit to using one poetry style/form. Some examples are haiku, rhymed poetry, acrostic, free verse, ode, bhajan/kirtan, etc.  </li>
  <li>
    Poems will be judged on: organization, flow, grammar, poetry style, etc.
  </li>
  <li>
    Theme list, submission details and grading rubric will be provided on the website soon.  </li>
</ul>
<div>""",
        'Essay-Writing (Group 3)': """<div class="skills-html">
<p> Writing essays may seem boring at first, but this challenge will help you better understand and study the mukhpath that you memorized. The Essay-Writing challenge is where you get to take all the mukhpath and prasangs you memorized and compile it into one critical-analysis paper. </p>
<p> Note: Group 3 can only participate in this challenge </p>
<h2 class="static-content-title">Things to Keep in Mind</h2>
<ul>
	<li>
    You must select from one of the themes that will be provided to you.
  </li>
  <li>
    Essays must be in 12 point font, Arial or Times New Roman with double line spacing.
  </li>
  <li>
    Essays must be between 3-5 pages.
  </li>
  <li>
    Essays must include at least:
  </li>
  <ul>
    <li>
      1 prasang, along with a manan (reflection)
    </li>
    <li>
    2 mukhpath references
    </li>
  </ul>
  <li>
    Feel free to include more references as needed.
  </li>
  <li>
    Essays must include a creative title and page numbers.
  </li>
  <li>
    Essays will be judged on: organization, flow, grammar, content, imagination, etc.
  </li>
  <li>
    Theme list, submission details and grading rubric will be provided on the website soon.
  </li>
</ul>
<div>""",
    },
    'Art-Based Challenges': {
        'Painting/Illustration': """<div class="skills-html">
<p> If you like art, or at least can draw a stick figure, then this competition is perfect for you! In this challenge, you will draw/illustrate/paint on a satsang concept/theme in a creative way. (Fun Fact: Did you know Mahant Swami Maharaj loves to draw?) </p>
<h2 class="static-content-title">Things to Keep in Mind</h2>
<ul>
	<li>
    You must select from one of the themes that will be provided to you. 
  </li>
  <li>
    Artwork may include painting, drawing, sketching, chalk art, oil pastels, etc. This does not include photoshop or any multimedia art.
  </li>
  <li>
    The artwork must be presented on an 8.5 inches by 11 inches paper or canvas.
  </li>
  <li>
    Theme list, submission details and grading rubric will be provided on the website soon.  </li>
</ul>
<div>""",
        'Graphic Design': """<div class="skills-html">
<h2 class="static-content-title">Things to Keep in Mind</h2>
<p> Do you like art? Are you good with technology? Graphic Design will test your artistic and technological skills by being able to create a satsang-centric graphic using an online photo editing or illustration software. </p>
<ul>
	<li>
    You must select from one of the themes that will be provided to you.
  </li>
  <li>
    The graphic can be made using any photo editing/illustrating tool, such as Photoshop, Photopea or Canva. (Karyakars can provide guidance on the best software to use based on your needs.) 
  </li>
  <li>
    The graphic can be in either portrait or landscape orientation.
  </li>
  <li>
    Please make sure the graphic is of good quality, such as 1920 pixels by 1080 pixels.
  </li>
  <li>
    Feel free to be creative by using various images, texts, shapes, etc.
  </li>
  <li>
    Theme list, submission details and grading rubric will be provided on the website soon.  
  </li>
</ul>
<div>""",
        'Video Making': """<div class="skills-html">
<p> Do you have what it takes to make an informative viral video? Video Making is where you use a video editing software to explain a satsang concept in a creative way. </p>
<h2 class="static-content-title">Things to Keep in Mind</h2>
<ul>
	<li>
    You can choose any 1 suggested topic and prepare a video to submit on that topic in advance of the Adhiveshan. The suggested topics are general, and will allow you to be creative and think freely!  </li>
  <li>
    Videos can be made on any video making platform, such as Movie Maker, iMovie, Final Cut Pro, Adobe Premiere, etc. (Karyakars can provide guidance on the best software to use based on your needs.) 
  </li>
	<li>
    Videos must be in 16:9 ratio.
  </li>
	<li>
   Feel free to be creative by using various images, texts, shapes, music, videos, voice overlay, video templates/effects, etc.	
  </li>
  <li>
    Topic list, submission details and grading rubric will be provided on the website soon. 
  </li>
</ul>
<div>""",
        'Rangoli design': """<div class="skills-html">
<p> Traditionally, rangolis are created at the front of an entrance to a house or any other building during utsavs (Hindu festivals) and special occasions. The Rangoli Design challenge is where you get to create various design patterns using different materials, such as rice grains, flower petals, colored powder, etc. </p>
<h2 class="static-content-title">Things to Keep in Mind</h2>
<ul>
	<li>
    You can, but are not limited to, choose any of the suggested topics to design their rangoli. The suggested topics are general, and will allow you to be creative and think freely!  </li>
  <li>
    Rangolis can be made from any of the following: colored powder, chalk, colored rice grains, paper cut outs, etc. Feel free to experiment with other materials as well.  </li>
  <li>
    Rangolis cannot be only drawn/illustrated on paper.
  </li>
  <li>
    Feel free to be as simple or elaborate with your designs.
  </li>
  <li>
    Rangolis that are submitted must be new submissions and not done on prior occasions.
  </li>
  <li>
    Topic list, submission details and grading rubric will be provided on the website soon.  
  </li>
</ul>
<div>""",
    },
}

# Skills Challenge for KM
KISHORE_SKILLS_CHALLENGE = {
  'Kirtan-based Short Speech': """
    <ul>
      <li>
        This competition is ideal for a kishore/kishori who is strong in singing as well as public speaking. Participants will combine the two technical elements to create an engaging and thought-provoking presentation. Presentations will revolve around a selection of one chosar from the adhiveshan booklet.
      </li>
      <li>
        This competition requires a through understanding of the background behind the chosar and the meaning of the words. A cohesive speech will incorporate these elements in a seamless manner — used to educate anyone who watches.
      </li>
      <li>
        Kishores and kishoris will be judged on time limit, accurate chosar pad understanding, incorporation of translations, creativity, ability to sing and speak, and cohesiveness of the speech’s components and overall message. More information about the judging criteria will be provided later.
      </li>
    </ul>
  """,
  'Creative Storytelling': """
    <ul>
      <li>
        Participants will choose prasangs from their adhiveshan modules and/or prasangs from other books as well. Participants must tell the story in its entirety, as well as provide a manan, or reflection, on the importance of the story.
      </li>
      <li>
        If participants are recording themselves, they must record their story in good lighting and on a good camera (either on a smartphone or webcam). Kishores should wear a jabho-lengho and kishoris should wear a punjabi. The story may also be presented with graphics, animations, etc. with the delegate as the narrator.
      </li>
      <li>
        Creative elements can be added such as creative visuals, editing, music, graphics, etc. Storytelling will be judged on: storytelling ability, content, manan/personal reflection, gestures, organization, flow, confidence, tone, etc. More information about the judging criteria will be provided later.
      </li>
    </ul>
  """,
  'Vachanamrut Nirupan': """
    <ul>
      <li>
        Kishores and kishoris will have the opportunity to perform a nirupan on any given Vachanamrut contained within the adhiveshan booklet. This is a solo presentation that should be recorded for submission. This presentation has a time limit of 6 minutes. Platforms such as Google Slides, Powerpoint, or Prezi may be used to assist in the nirupan but are not required.
      </li>
      <li>
        Delegates should explain the Vachanamrut, analyze the content, relate the Vachanamrut to other prasangs and texts, and explain how this Vachanamrut is beneficial to a kishore or kishori’s life.
      </li>
      <li>
        Kishores/kishoris will be judged on analysis of the Vachanamrut, references to other prasangs/texts, real life application, speaking ability, accurate information, and timing. More information about the judging criteria will be provided later.
      </li>
    </ul>
  """,
  'Group Presentation': """
    <ul>
      <li>
        Kishores and kishoris will have the opportunity to present on the topics listed below in a group. Groups are limited to a minimum of 3 people and a maximum of 5 people. 
      </li>
      <li>
        Kishores/kishoris will be able to create a presentation on the following topics to be recorded for submission. Presentations can be created on platforms such as Google Slides, Powerpoint, Prezi, etc. During the time of the presentation, kishores must be dressed in a jabho lengho and kishoris in punjabis.
      </li>
      <li>
        The presentation should include module content, which includes Vachanamrut references, Swamini Vato, Kirtans, etc. The presentation should provide a thorough understanding of the topic using Satsang-based references.
      </li>
      <li>
        Group presentations will be judged on speaking ability, accurate information, dress code, timing, creativity. More information about the judging criteria will be provided later.
      </li>
    </ul>
  """,
  'Solo Singing': """
    <ul>
      <li>
        Delegates may select any kirtan/chosar pad they wish to sing for this challenge, more specifically, it is encouraged that delegates pick a bhajan that they strongly resonate with.
      </li>
      <li>
        Prior to singing the bhajan, you will need to describe the overall theme/messages contained within this bhajan. This reflection can either be about the meaning of the bhajan, or its history.
      </li>
      <li>
        Kishores and kishoris will be judged on: sur (melody), tempo/rhythm, and tone/voice, along with your understanding of the kirtan that is spoken at the beginning. More information about the judging criteria will be provided later.
      </li>
    </ul>
  """,
  'Music Production (Group Singing)': """
    <ul>
      <li>
        Kishores and kishoris will have the opportunity to create a full music production with a group. Groups are limited to no less than 3 people and no more than 5 people. 
      </li>
      <li>
        Kishores and kishoris may combine musical instruments, vocals, and sound effects to create a music production using production software such as Garageband, Audacity, FL Studio, etc. 
      </li>
      <li>
        The produced soundtrack must be exported and submitted as a MP3 file. The soundtrack will be graded on tone of vocals, melody, implementation of proper musical instruments, tempo/rhythm, and sound effects. More information about the judging criteria will be provided later.
      </li>
    </ul>
  """,
  'Research Paper': """
    <ul>
      <li>
        Kishores and kishoris will have the opportunity to research a Satsang concept in depth using various Satsang scriptures and texts. The research paper will highlight a certain point and texts should be used to support the concept being presented.
      </li>
      <li>
        Kishores and kishoris should create a submission via PDF or Word.
      </li>
      <li>
        Papers will be judged on: organization, flow, grammar, content, sources, and citations. More information about the judging criteria will be provided later.
      </li>
    </ul>
  """,
  'Screenwriting': """
    <ul>
      <li>
        Anyone interested in large productions or musicals will find this challenge interesting. A kishore or kishori must explain the relevant theme of guru bhakti through a written play or musical. Specific insights must be incorporated within the written play or musical. 
      </li>
      <li>
        Writing must be done on either Google Docs or Microsoft Word and turned in as a PDF file. An example script with proper formatting will be provided. Competitors will be graded on grammar, sentence structure, readability, format, creativity, story arch, use of themes. More information about the judging criteria will be provided later.
      </li>
    </ul>
  """,
  'Photography': """
    <ul>
      <li>
        Kishores and kishoris will have the opportunity to create a photo album containing a topic or theme which corresponds to the images within the album. For example, the images within the submitted photo album must correspond to a satsang topic such as: guru bhakti, mahima, mandir, Satpurush, etc.
      </li>
      <li>
        Kishores and kishoris are also welcome to use editing software such as Adobe Lightroom to edit their photos. (Photoshop and Illustrator are not allowed as this would cross the boundary into graphic design)
      </li>
      <li>
        Photo albums are to be submitted with a brief description of the theme which corresponds to the images. Images must be submitted within a folder or zip file with the image types as either JPEG or PNG.
      </li>
      <li>
        Photo albums will be judged by consistent themes, quality, moods, creativity, originality, and uniqueness of concept. More information about the judging criteria will be provided later.
      </li>
    </ul>
  """,
  'Painting and Illustrations': """
    <ul>
      <li>
        Kishores and kishoris will have the opportunity to paint or illustrate a certain incident in the lives of our gurus. These paintings and illustrations must be submitted electronically as a scan.
      </li>
      <li>
        Artwork may include painting, drawing, chalk art, oil pastels, or any form of physical art utensils.
      </li>
      <li>
        Artwork will be judged on creativity, cleanliness, artistic ability, and the content depicted in the artwork. More information about the judging criteria will be provided later.
      </li>
    </ul>
  """,
  'Graphic Design': """
    <ul>
      <li>
        Kishores and kishoris will have the opportunity to create a graphic using an online software platform. The graphic can be made using any photo editing/illustrating tool, such as Photoshop, Illustrator or Canva.
      </li>
      <li>
        The designs must be submitted electronically, as an image.
      </li>
      <li>
        Submissions will be judged on creativity, artistic ability, and content depicted in the graphic. More information about the judging criteria will be provided later.
      </li>
    </ul>
  """,
  'Coding Challenge': """
    <ul>
      <li>
        Any kishore or kishori interested in developing their talents in web/app development, data visualizations, or AI/ML should pick this challenge.
      </li>
      <li>
        Participants may use any language and should submit final code as a .zip file
      </li>
      <li>
        Submissions will be judged on creativity, utility, user-friendliness, and content provided in the coding platform. More information about the judging criteria will be provided later.
      </li>
    </ul>
  """,
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
    "title": "Swamishri Blessing the App",
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
    "title": "Swamishri with Children",
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
  {
    "title": "Quote of the Week",
    "url": "https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/Stories/KM/Quote-of-the-Week/photo_2021-01-22%2015.51.47.jpeg",
    "stories": [
      {
        "url": 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/Stories/KM/Quote-of-the-Week/photo_2021-01-22%2015.51.47.jpeg',
        "type": "image"
      },
    ]
  },
  {
    "title": "Divine Moods",
    "url": "https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/KM%20Module%20Photos/extra2.jpg",
    "stories": [
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
    "title": "Guidance from Swamishri",
    "url": "https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/KM%20Module%20Photos/extra5.jpg",
    "stories": [
      {
        "url": 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/Stories/KM/Insights-from-Swamishri/insight.mp4',
        "type": "video"
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
    "title": "Swamishri Blessing the App",
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
    "title": "Word of the Week",
    "url": "https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/Stories/KM/Word-of-the-Week/word_of_the_week.png",
    "stories": [
      {
        "url": 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/Stories/KM/Word-of-the-Week/Black%20Video_5.mp4',
        "type": "video"
      },
      {
        "url": 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/Stories/KM/Word-of-the-Week/Black%20Video_6.mp4',
        "type": "video"
      },
      {
        "url": 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/Stories/KM/Word-of-the-Week/Black%20Video_7.mp4',
        "type": "video"
      },
    ]
  },
  {
    "title": "Quote of the Week",
    "url": "https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/Stories/KM/Quote-of-the-Week/photo_2021-01-22%2015.51.47.jpeg",
    "stories": [
      {
        "url": 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/Stories/KM/Quote-of-the-Week/photo_2021-01-22%2015.51.47.jpeg',
        "type": "image"
      },
    ]
  },
  {
    "title": "Insights from Swamishri",
    "url": "https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/KM%20Module%20Photos/extra5.jpg",
    "stories": [
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
]

BM_ANNOUNCEMENTS = [
    {
        'timestamp': '31 Jan, 2021',
        'text': 'On Saturday, February 6th, please join your parents to attend a special Adhiveshan Sabha. You will be able to hear more about the mahima of Adhiveshan and learn how to use tools such as the website.'
    },
    {
        'timestamp': '31 Jan, 2021',
        'text': 'Pledging is now live on BKMS till March 7th, 2021. Make sure you contact your karyakars if you are having any issues or problems. Remember that pledges made on the website are not automatically made for you on BKMS!'
    },
    {
        'timestamp': '31 Jan, 2021',
        'text': 'Jai Swaminarayan balaks and balikas. Welcome to the Adhiveshan website! We are very excited to begin our journey towards Guru Bhakti.'
    }
]

KM_ANNOUNCEMENTS = [
    {
        'timestamp': '31 Jan, 2021',
        'text': 'Pledging is now live on BKMS! Make sure you contact your karyakars if you are having any issues or problems. Remember that pledges made on the website are not automatically made for you on BKMS!'
    },
]

BM_ANNOUNCEMENT_PAGE_CONTENT = {
    'announcements': BM_ANNOUNCEMENTS,
    'stories': BM_STORIES
}

KM_ANNOUNCEMENT_PAGE_CONTENT = {
    'announcements': KM_ANNOUNCEMENTS,
    'stories': KM_STORIES
}

