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
GURU_PARAMPARA = 'guru_parampara'
PATRI = 'patri'
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
    GURU_PARAMPARA,
    PATRI,
]

BAL_AND_KISHORE_MODULES = [
    SATSANG_DIKSHA
]

MODULE_ICON_LINKS = {
    SATSANG_DIKSHA: 'https://baps.box.com/shared/static/xq8xia8s7wlzeq03c8ksvgcyzpavh3mg.png',
    SWAMINI_VATO: 'https://baps.box.com/shared/static/eka816vxers5k2wievnqgkqg5ism7rlj.png',
    SHLOKA_SAKHI: 'https://baps.box.com/shared/static/c7ba7xmmj7rp3izl5v2q6dy8fkcfsmid.png',
    KIRTAN: 'https://baps.box.com/shared/static/kvtdw89ew6vez8z6xpvuctnqzkuh6ued.png',
    PRASANG_MANAN: 'https://baps.box.com/shared/static/4p18elsk5vjdy9rxyp65e3ml0lfmvt6a.png',

    ANTARDRASHTI: 'https://baps.box.com/shared/static/0byr2nm02fqt9mfu4bmi4mvl9vt9b315.jpg',
    PRAPTINO_VICHAR: 'https://baps.box.com/shared/static/kx0uqxzclx4c00vp0l2tx8w4c8hfavi9.png',
    RAJIPANO_VICHAR: 'https://baps.box.com/shared/static/0j5z1oujesijt9fx519pjnopghzcpjx9.png',
    SANKHYA_VICHAR: 'https://baps.box.com/shared/static/8nfbae3qrcipnn4xiysuvm3ye2as8cq1.jpg',
    GUN_GRAHAN_SAMBANDHNO_MAHIMA: 'https://baps.box.com/shared/static/ajm5gqckboix2xrvpx44bitbd87bhxqb.jpg',
    ATMA_VICHAR: 'https://baps.box.com/shared/static/fe85cithxizogejsjx6k2cjgeaqr8lqa.jpg',
    PRARTHANA: 'https://baps.box.com/shared/static/pc2ppmhc91aka6ni7pe5eg1mu8k8bnjg.jpg',
    UPASANA_SWARUPNISHTHA: 'https://baps.box.com/shared/static/je14v7dm1nx5e703otrzcrl8jgknjuro.jpg',
    AKSHAR_PURUSHOTTAM_SIDDHANT: 'https://baps.box.com/shared/static/9t8wqu79m0kv9vpfglgim6ve2p7c56ss.jpg',
    SARVOPARI: 'https://baps.box.com/shared/static/gqvymfmf2qslqrfzxl3x14sijt8489kb.jpg',
    DIVYA_SAKAR: 'https://baps.box.com/shared/static/7jt4e8w5zrcr2a4g9kthx39l5sprp42c.jpg',
    SARVA_KARTA: 'https://baps.box.com/shared/static/jdkpom5awa4nj2pou9fmc3rbq42pz7l2.jpg',
    PRAGAT: 'https://baps.box.com/shared/static/9skb19q171eci8h6ty7eta3tpip7f2lf.jpg',
    AGNA: 'https://baps.box.com/shared/static/xx8vntvvq8bvj8g1ji9q2wy92z392bxh.jpg',
    ASHRO: 'https://baps.box.com/shared/static/cqysx181f6ytdoojdbqyj31itfy0i2lz.png',
    SEVA: 'https://baps.box.com/shared/static/8pygl7lmm79jg0yswr7ig0g1efcmn2no.jpg',
    VISHWAS_SHRADDHA: 'https://baps.box.com/shared/static/fwdprjdihpw6torgl99921teqnicyvxl.jpg',
    NIYAM_DHARMA: 'https://baps.box.com/shared/static/ednsd0ue32gzp2x3hki14azr2b7ftttu.jpg',
    BHAKTI: 'https://baps.box.com/shared/static/gexu8q3duebgz0thbegnm5r7sp358syt.jpg',
    SHURVIRTA_HIMMAT: 'https://baps.box.com/shared/static/bmd4bgwz3ch14gkazhqc5qyeodj4k3tt.jpg',
    SMRUTI: 'https://baps.box.com/shared/static/1xxnlbl1udqbqq8ecqi9p6533w8qr1rb.jpg',
    SUKH: 'https://baps.box.com/shared/static/s2svh23asb6wn0hz4x1virku6oayq36q.jpg',
    KATHA_VARTA: 'https://baps.box.com/shared/static/yjp9364xuxeipgnas08m6iwdwk5952cx.jpg',
    SATSANG_READING: 'https://baps.box.com/shared/static/zwcpja4180d2pn1znvqemn83einuhd06.jpg',
    SAMP_SURADHBHAV_EKTA: 'https://baps.box.com/shared/static/tbdjs59tdniiiu94l7az0kf4wz7872oj.png',
    KSHAMA: 'https://baps.box.com/shared/static/88rzxhz5unyv6eu7z6phia1423dhdoek.jpg',
    SAHAN: 'https://baps.box.com/shared/static/tk5zuzwv7jpi5rk4y1yewpjodq2yc31b.jpg',
    NIRMANIPANU: 'https://baps.box.com/shared/static/00mlk26y8m1mmde6yuftli7q6pihr300.jpg',
    DIVYABHAV_NIRDOSHBUDDHI: 'https://baps.box.com/shared/static/vyqk4qkjnoh6z8kqufkmrqbvsx33rxqx.png',
    SATPURUSHNO_MAHIMA: 'https://baps.box.com/shared/static/k4v37q8h7y4gyf1zs6zfsjthqo544enq.jpg',
    DRADH_PRITI: 'https://baps.box.com/shared/static/rvr9wt9psa5r2snxqcxgg3uov6zvajm9.jpg',
    SATSANG: 'https://baps.box.com/shared/static/xvr64pscal7wcw0jk107qln9e5g5mtiy.jpg',
    KUSANG: 'https://baps.box.com/shared/static/anig5kvmry9e2sr60k2udo879n47kcly.jpg',
    SWABHAV: 'https://baps.box.com/shared/static/ple8q8tthvyw8r4boq9kggqvvh1tf0iz.jpg',
    ABHAV_AVGUN: 'https://baps.box.com/shared/static/2uax04lf77486js7bcvbatllchfeqmae.jpg',
    AHNIK: 'https://baps.box.com/shared/static/s1plm3cfs61dimvdwnbkmjhcbelvsaok.png',
    CHOSAR_PADS: 'https://baps.box.com/shared/static/nmv283u8ak14cbexx2ip0lywj1i8kkb3.jpg',
    FAGVA: 'https://baps.box.com/shared/static/ge1hx2xjo344dfecv7zp5zfnl0oc8v2c.png',
    GURU_PARAMPARA: 'https://baps.box.com/shared/static/saj9sb3zfjujo4dgvgy0kzwjcpdgplxk.jpg',
    PATRI: 'https://baps.box.com/shared/static/i39pujukiw5fi0vknjqbs598mi6o28af.jpg',
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
    GURU_PARAMPARA: 7,
    PATRI: 1,
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
            'answer': 'Adhiveshan is a structured way of memorizing mukhpath which is sometimes focused on a certain '
                      'satsang topic or theme. Adhiveshan is NOT a competition, but rather a challenge for ourselves '
                      'to sacrifice our time to memorize the mukhpath, learn its meaning, and eventually imbibe it in '
                      'our lives to please Mahant Swami Maharaj.',
        },
        {
            'question': 'Why do we do Adhiveshans?',
            'answer': 'Adhiveshan has been very dear to the hearts of our Gurus. Starting with Yogi Bapa’s passion '
                      'for balaks and balikas to memorize mukhpath during their summer vacations to the various '
                      'Adhiveshans held with Pramukh Swami Maharaj and Mahant Swami Maharaj, mukhpath has been an '
                      'integral way for balaks and balikas to earn the Rajipo of our Gurus. By learning and '
                      'memorizing various parts of our Shastras, we are able to ground ourselves in the Akshar '
                      'Purushottam Upasana and find solutions to the many problems we may face in life. Along with '
                      'this, this Adhiveshan will also help us gear up for the upcoming Pramukh Swami Maharaj '
                      'Shatabdi Mahotsav and the Aksharsham Mahotsav.',
        },
        {
            'question': 'Which Adhiveshan do I pledge for and which Summer Shibir do I go to?',
            'answer': 'You will pledge for the tiers in the group you currently are in (as of January 2021). For '
                      'example, if you are in Group 2 in January of 2021, and even if you are graduating and moving '
                      'to Group 3 in September 2021, you will pledge for Adhiveshan in the Group 2 categories. Anyone '
                      'in Groups 1-3 will also attend the Bal/Balika summer shibir.\nAdditionally, current 8th '
                      'graders will pledge for the Kishore/Kishori Adhiveshan and will join the Kishore/Kishori '
                      'Shibir.\nThose currently in Group 0 will pledge for the Group 0 adhiveshan, even if they are '
                      'graduating and moving to Group 1 in September 2021; those currently in Group 0 will join the '
                      'Bal/Balika Group 0 shibir.',
        },
        {
            'question': 'What does Adhiveshan consist of?',
            'answer': 'Adhiveshan will have three parts, each assessed in different ways and at different times. The '
                      'first part is the Beginner’s Challenge (Prathmik Mukhpath) which will be assessed at home. The '
                      'second part is the Adhiveshan Rajipo Challenge (Main Mukhpath), which will be assessed online '
                      '(in real time - over Zoom). The final part is the Skills Challenge (Talent Competitions), '
                      'which will be judged through regional online submissions.',
        },
    ],
    'Beginner’s Challenge (Prathmik Mukhpath)': [
        {
            'question': "What is the Beginner\'s Challenge (Prathmik Mukhpath)?",
            'answer': "The Beginner's Challenge contains the core mukhpath of our sanstha. All of the mukhpath comes "
                      "with translations, so it is important to pay close attention to the meanings and try to "
                      "introspect on how the values being transmitted in the words can be applied back to our lives. "
                      "The Beginner's Challenge will be administered at home, wherein you all will complete a "
                      "worksheet. Your parents will aid in ensuring that you have completed the worksheet properly "
                      "and assist in grading.",
        },
    ],
    "Adhiveshan Rajipo Challenge (Advanced Mukhpath)": [
        {
            'question': "How is the Adhiveshan Rajipo Challenge (Advanced Mukhpath) structured?",
            'answer': "The Rajipo Challenge is broken up into 5 categories: Satsang Diksha, Swamini Vato, Kirtans, "
                      "Shlokas and Sakhis, and Prasang Manan. There are 4 tiers (Mahant, Pramukh, Yogi, "
                      "and Shastri).\nNOTE: There is an additional tier called the Ghanshyam tier that is ONLY if you "
                      "are in Group 0. However, if you are in Group 1, you can select the Ghanshyam tier ONLY for "
                      "Satsang Diksha (for the other categories, you must pick from the normal 4 tiers).\nThe "
                      "breakdown for each tier and each group is found in the appendix on the last page.",
        },
        {
            'question': "Is there a minimum number of tiers/categories needed to participate in the Adhiveshan?",
            'answer': "As per Swamishri’s ruchi, the focus of this Adhiveshan is to learn, understand, and imbibe "
                      "various satsang shastras in the lives of balaks and balikas. Thus, there is no mandatory "
                      "minimum amount of categories you need to pledge to be able to participate in the Adhiveshan. "
                      "Although, you should still strive to pledge for as many categories as you can and push "
                      "yourselves to strive for higher tiers to make Swamishri extra raaji.",
        },
        {
            'question': "Can we choose which items to memorize in each category?",
            'answer': "The Satsang Diksha category is the only category that will have a set number of shlokas for "
                      "each tier. For example if you choose the Mahant Challenge for the Satsang Diksha category, "
                      "there will be a pre-set list of 64 shlokas. For all of the other categories (Swamini Vato, "
                      "Shloka/Sakhi, Kirtan, Prasang Manan), you will have a choice in creating your own set with the "
                      "available list of mukhpath. For example, if you are a group 1 balak or balika who wants to do "
                      "the Yogi challenge for Kirtans, you will be able to choose any 4 out of a possible list of 15 "
                      "kirtans listed in the book.",
        },
    ],
    "Skills Challenge (Talent Competitions)": [
        {
            'question': "What is the Skills Challenge (Talent Competition)?",
            'answer': "The Skills Challenge allows you to tie your passions and hobbies back to Satsang. You will "
                      "have a chance to show your talents in a multitude of fashions included in the mukhbath "
                      "booklet. You will be able to choose a minimum of 1 and a maximum of 3 categories. More details "
                      "on the rules and regulations for each of the specific skills challenges are listed in the "
                      "book.",
        },
    ],
    "Adhiveshan Pledging": [
        {
            'question': "How can I pledge for Adhiveshan?",
            'answer': "You will be able to pledge for Adhiveshan through BKMS after the Launch Sabha at the end of "
                      "January. You will be able to access this link until 3/7/21. By this date, you must submit "
                      "their pledges. Before this date, please read through the Mukhpath book and take a look at the "
                      "possible tiers for your group and make a decision on what mukhpath you will be able to "
                      "memorize by the summer.\nNOTE: If you pledge for Satsang Diksha, you should try to continue "
                      "with the tier you chose for your Rajipo Challenge from August 2020. If you would like to "
                      "change it, there will be an opportunity for you to repledge your original Satsang Diksha "
                      "pledge when you pledge for the other Adhiveshan categories.",
        },
    ],
    "Adhiveshan Timeline": [
        {
            'question': "What are some important dates to keep in mind relating to the Adhiveshan?",
            'answer': """<div class="timeline-question">SS21 Adhiveshan Launch Sabha: 1/31/2021\nAdhiveshan Pledge and Summer Shibir registration:
                      1/31/2021-3/7/2021\nBeginner's Challenge Quiz: To be held at home - Time soon to come\nTalent
                      Competition Submission Deadline: Time soon to come\nAdhiveshan Rajipo Challenge: Time soon to
                      come""",
        },
    ],
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
      'question': "How is the Adhiveshan structured? Will it be virtual?",
      'answer': "All components of adhiveshan will take place virtually this year. There will be four components to adhiveshan: the prathmik mukhpath, the Rajipo Challenge, the Guru Bhakti Challenge, and Skills Competitions."
    },
    {
      'question': "How will Adhiveshan testing work? Will it be virtual?",
      'answer': "Due to the current situation with the COVID-19 pandemic, Adhiveshan will also take place over a virtual setting. Weeks prior to the shibir, karyakars will join individual calls to test kishores and kishoris on their mukhpath as it is traditionally done during an in-person adhiveshan."
    },
  ],
  'Prathmik Mukhpath': [
    {
      'question': 'What is prathmik mukhpath?',
      'answer': "The prathmik mukhpath contains core mukhpath that kishores and kishoris encounter on a daily basis. All of the mukhpath comes with translations, so it is important to pay close attention, understand the meanings, and try to introspect on how the values being transmitted in the words can be applied back to our lives. The prathmik mukhpath for this year includes the Shri Swaminarayan Arti and the two puja shlokas provided in Satsang Diksha. Kishores and kishoris will be tested on the prathmik mukhpath, just like both mukhpath challenges."
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
      'question': "How will the Skills Competitions work? Will it be virtual?",
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
                Local Award Ceremonie
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
		Participants can choose to enact any one scene from the list of scenes
		below. However, participants can choose to enact another scene if not
		present from the list.
	</li>
	<li>Each participant will have a maximum of 5 minutes to enact the scene.</li>
	<li>The act must be memorized. Notes will not be allowed.</li>
	<li>
		Participants must record their drama in good lighting and on a good camera
		(either on a smartphone or webcam). Audio must be clear. Participants should
		dress up and use props.
	</li>
	<li>
		You will take on the role of one person from the scene (for most scenes this
		is provided), and enact the scene from that person's point of view.
	</li>
	<li>
		Balaks must choose the bal characters and balikas must choose the balika
		character list.
	</li>
	<li>
		Mono-acting will be judged on: accurate portrayal of the incident, acting,
		tone, emotion, facial expressions, memorization, props/costume/creativity.
	</li>
</ul>
<h2 class="static-content-title">Character List</h2>
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
          Joban Pagi’s Transformation
        </ion-text>
      </ion-col>
      <ion-col size="5">
        <ion-text>
          Jivuba’s Bhakti to Thakorji
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
          Ladudanji’s Four Wishes
        </ion-text>
      </ion-col>
      <ion-col size="5">
        <ion-text>
          Kushalkuvarba
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
          Prahalad’s Bhakti
        </ion-text>
      </ion-col>
      <ion-col size="5">
        <ion-text>
          Gargi’s Debate
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
          Shravan’s Seva
        </ion-text>
      </ion-col>
      <ion-col size="5">
        <ion-text>
          Mirabai’s Bhakti
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
        Characters from any bodh katha
      </ion-col>
  </ion-row>
</ion-grid>
<div>""",
        'Storytelling': """<div class="skills-html">
<h2 class="static-content-title">Rules</h2>
<ul>
	<li>
		Participants will speak on one of Yogiji Maharaj’s Bodh Katha. A sample list is provided below, however participants can choose any bodh katha from the book, 101 Tales of Wisdom.
	</li>
	<li>Participants must tell the story in its entirety, as well as provide a manan, or reflection, on the importance of the story.</li>
	<li>The story must be memorized. Notes will not be allowed.</li>
	<li>
		Participants must record their story in good lighting and on a good camera (either on a smartphone or webcam). Balaks should wear a jhabo-lengho and balikas should wear a punjabi.
	</li>
	<li>
		Storytelling will be judged on: storytelling ability, content, manan/personal reflection, gestures, organization, flow, confidence, tone, etc.
	</li>
</ul>
<h2 class="static-content-title">Bodh Katha</h2>
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
          Tukaram and Naradji
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
          Lindiyo
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
</ion-grid>
<div>""",
        'Satsang Diksha Nirupan': """<div class="skills-html">
<h2 class="static-content-title">Rules</h2>
<ul>
	<li>
		Participants will speak on a theme which is expanded upon in the Satsang Diksha. Participants must select from one of the themes below. Sample shlokas related to the theme are also provided for guidance, however participants may choose shloks outside of the range.
	</li>
	<li>The nirupan should include at least:</li>
  <ul>
	  <li>2 Satsang Diksha Shloks</li>
	  <li>
		1 prasang of Pramukh Swami Maharaj or Mahant Swami Maharaj
	  </li>
  </ul>
  <li>
  Participants will have a maximum of 8 minutes.
  </li>
  The nirupan must be memorized. Notes will not be allowed.
	<li>
		Participants must record their nirupan in good lighting and on a good camera (either on a smartphone or webcam). Balaks should wear a jhabo-lengho and balikas should wear a punjabi.
	</li>
	<li>
Nirupan will be judged on: accurate use of mukhpath and prasangs, organization, flow, confidence, tone, etc.
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
      <ion-text>Example Shlokas</ion-text>
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
          Importance of a Mandir
        </ion-text>
      </ion-col>
      <ion-col size="5">
        <ion-text>
          Shloks 79-95
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
         Akshar-Purushottam Darshan
        </ion-text>
      </ion-col>
      <ion-col size="5">
        <ion-text>
          Shloks 96-115
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
          Sang vs Kusang
        </ion-text>
      </ion-col>
      <ion-col size="5">
        <ion-text>
          Shloks 216-234
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
          Being an Ideal Child
        </ion-text>
      </ion-col>
      <ion-col size="5">
        <ion-text>
          Shloks 209-115
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
        Importance of Agna and Upasana
      </ion-col>
      <ion-col>
        Shloks 287-298
      </ion-col>
  </ion-row>
</ion-grid>
<div>""",
        'Prasang-Varnan Speech': """<div class="skills-html">
<h2 class="static-content-title">Rules</h2>
<ul>
	<li>
    Participants will elaborate on a prasang and provide a manan, or personal reflection, on the prasang by using 2 mukhpath references that they had memorized. The prasang can be from, but not limited to, the prasang mukhpath section in the Rajipo Challenge. However, the personal manan must be different from the one provided.
	</li>
	<li>If a prasang is not chosen from the Rajipo Challenge, please name the source in your speech, such as kids.baps.org or Eternal Virtues.</li>
	<li>The prasang-varnan should include at least:</li>
  <ul>
	  <li>
		1 key prasang
	  </li>
	  <li>
		1 mukhpath reference
    </li>
    <li>
    A personal manan (analysis/reflection)
    </li>
  </ul>
  <li>
  Participants will have a maximum of 8 minutes.
  </li>
  <li>
  The prasang-varnan must be memorized. Notes will not be allowed.
  </li>
  <li>
  Participants must record their prasang-varnan in good lighting and on a good camera (either on a smartphone or webcam). Balaks should wear a jhabo-lengho and balikas should wear a punjabi.
  </li>
</ul>""",
    },
    'Music-Based Competitions': {
        'Solo Singing': """<div class="skills-html">
<h2 class="static-content-title">Rules</h2>
<ul>
	<li>
    You may select 1 of the 20 bhajans provided below to perform during the competition. However, you do have the option to not select one of the 20 bhajans below and can select to perform any kirtan from the Kirtan Muktavali. 
	</li>
  <li>
  Select any bhajan that you feel you resonate strongly with!
  </li>
	<li>The bhajan must be memorized with the meaning and must include a manan (reflection) prior to singing the bhajan. This reflection can either be about the meaning of the bhajan, its history or what the bhajan means to you.</li>
  <ul>
	  <li>If we use the Shri Swaminarayan Aarti as an example, begin by generally explaining the meaning of the Swaminarayan Aarti for around 1 minute. Then, go ahead and sing the entire aarti. (Note: Do not select the aarti to sing.)</li>
  </ul>
  <li>
  You will be judged on: sur (melody), tempo/rhythm, and tone/voice, along with your understanding of the kirtan that is spoken at the beginning.
  </li>
</ul>
<h2 class="static-content-title">Bhajan List</h2>
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
          Tamri Murti Vina
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
        2
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
        3
      </ion-text>
    </ion-col>
      <ion-col size="5">
        <ion-text>
          Hum to Ek Sahajanand Gave
        </ion-text>
      </ion-col>
      <ion-col size="5">
        <ion-text>
          Sahajanand Gave
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
        5
      </ion-text>
    </ion-col>
      <ion-col size="5">
        Terī Sāvarī Sūrat Chhatādār
      </ion-col>
      <ion-col>
        Neh Nibhavana
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
          Rūdā Lāgo Chho
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
        7
      </ion-text>
    </ion-col>
      <ion-col size="5">
        <ion-text>
          Sant Jan Soī Sadā Mohe Bhāve
        </ion-text>
      </ion-col>
      <ion-col size="5">
        <ion-text>
          Sahajanand Gave
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
        9
      </ion-text>
    </ion-col>
      <ion-col size="5">
        <ion-text>
          Thaī Rahyo Chhe Jay Jaykār Re
        </ion-text>
      </ion-col>
      <ion-col size="5">
        <ion-text>
          Vandan Varamvar Yogijine
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        10
      </ion-text>
    </ion-col>
      <ion-col size="5">
        <ion-text>
          Shastriji Maharajno Sang
        </ion-text>
      </ion-col>
      <ion-col size="5">
        <ion-text>
          Shastriji Maharajno Sang
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        11
      </ion-text>
    </ion-col>
      <ion-col size="5">
        <ion-text>
          Āvo Āvo Dharma Dulārā
        </ion-text>
      </ion-col>
      <ion-col size="5">
        <ion-text>
          Shastriji Maharajne Vandana
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        12
      </ion-text>
    </ion-col>
      <ion-col size="5">
        <ion-text>
          Swamiji to Mahapratapi
        </ion-text>
      </ion-col>
      <ion-col size="5">
        <ion-text>
          Yagnapurush Smruti
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        13
      </ion-text>
    </ion-col>
      <ion-col size="5">
        <ion-text>
          Bhakti Kartā Chhute Māro Prān
        </ion-text>
      </ion-col>
      <ion-col size="5">
        <ion-text>
          Almast Jogi
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        14
      </ion-text>
    </ion-col>
      <ion-col size="5">
        <ion-text>
          Vandan Vāramvār Yogījīne
        </ion-text>
      </ion-col>
      <ion-col size="5">
        <ion-text>
          Jogina Jadu
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        15
      </ion-text>
    </ion-col>
      <ion-col size="5">
        <ion-text>
          Guru Parameshwar Re
        </ion-text>
      </ion-col>
      <ion-col size="5">
        <ion-text>
          Sant Saurabh
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        16
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
        17
      </ion-text>
    </ion-col>
      <ion-col size="5">
        <ion-text>
          Māre Swāmīne Rājī Karvāja Chhe
        </ion-text>
      </ion-col>
      <ion-col size="5">
        <ion-text>
          Bal Saragam
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        18
      </ion-text>
    </ion-col>
      <ion-col size="5">
        <ion-text>
          Ghanu Jīvo Ho Jīvan Adhār
        </ion-text>
      </ion-col>
      <ion-col size="5">
        <ion-text>
          Valam Vadhamna
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        19
      </ion-text>
    </ion-col>
      <ion-col size="5">
        <ion-text>
          Ā Dehathī Shu Na Thāy Re
        </ion-text>
      </ion-col>
      <ion-col size="5">
        <ion-text>
          Sadgunna Bhandar
        </ion-text>
      </ion-col>
  </ion-row>
  <ion-row>
    <ion-col size="2">
      <ion-text>
        20
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
</ion-grid>
<div>""",
        'Musical Instruments': """<div class="skills-html">
<h2 class="static-content-title">Rules</h2>
<ul>
	<li>
	Participants may select one of the bhajans below to perform during the competition on a musical instrument. However, participants have the option to not select one of the bhajans below and can select to perform any bhajan from the Kirtan Muktavali.
	</li>
  <li>
  The submission must include a manan (reflection) prior to singing the bhajan. This reflection can either be about the meaning of the bhajan, its history or what the bhajan means to you.
  </li>
  <ul>
	  <li>
      If we use the Shri Swaminarayan Aarti as an example, begin by generally explaining the meaning of the Swaminarayan Aarti for around 1 minute. Then, go ahead and play the aarti on the instrument.
    </li>
  </ul>
	<li>
    Participants do not have to memorize the bhajan. They can have sheet music in front of them while they play.
  </li>
	<li>
    Participants may play on any musical instrument that they know how to play, including but not limited to piano, tabla, flute, trumpet, violin, harmonium, etc.
	</li>
		If participants choose a percussion instrument where the melody cannot be found, such as tabla, please have the bhajan audio playing in the background while the participant plays. 
	</li>
  <li>
  You will be judged on: sur (melody), tempo/rhythm, accuracy, tonality, etc.
  </li>
</ul>
<h2 class="static-content-title">Bodh Katha</h2>
<ion-grid class="ion-text-center">
  <ion-row class="header-row">
    <ion-col size="2">
      <ion-text>#</ion-text>
    </ion-col>
    <ion-col size="10">
      <ion-text>Bhajan Name</ion-text>
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
          Sant Param Hitkari
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
          Tamari Murti Vina
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
         Bhulish Hu Jagatni Maya
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
          Bhav Dharine Bolo Jay Akshar-Purushottam
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
          Ame Sau Swāmīnā Bālak
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
          Ame Sau Swāmīnā Bālak
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
          Vandan Karīe Prabhu Bhāv Dharī
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
          Joi Murti Manohar Tari
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
          He Jī Me To Harkhe Nihalyā Nāth
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
          Vandan Guruji Vandan Prabhuji
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
    Participants must select from one of the themes below. The categories are provided, with a small description on what the poem should depict.
	</li>
	<li>
    Although there are many different types of poetic form, please limit to using one poetry style/form throughout the poem. Some examples are haiku, rhymed poetry, acrostic, free verse, ode, etc.
  </li>
  <li>
    Poems will be judged on: organization, flow, grammar, poetry style, etc.
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
          Pramukh Swami Maharaj
        </ion-text>
      </ion-col>
      <ion-col size="5">
        <ion-text>
          Write about the greatness of Pramukh Swami Maharaj
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
          Write what a guru means to you
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
        Akshardham
      </ion-col>
      <ion-col>
        Depict what Robbinsville Akshardham means to you
      </ion-col>
  </ion-row>
</ion-grid>
<div>""",
        'Essay-Writing (Group 3)': """<div class="skills-html">
<h2 class="static-content-title">Rules</h2>
<ul>
	<li>
    Participants must select from one of the themes below. The categories are provided, with a small description on what the essay should be on.	</li>
	<li>
    Essays must be in 12 point font, Arial or Times New Roman with double margins.
  </li>
  <li>
    Essays must be between 3-5 pages.
  </li>
  <li>
    Essays must include at least:
  </li>
  <ul>
    <li>
      1 prasang, along with a manan
    </li>
    <li>
    2 mukhpath references
    </li>
  </ul>
  <li>
  Essays must include a creative title and page numbers.
  </li>
  <li>
  Participants should NOT put their name on their essay. They should only include their BKMS ID on the top right of the page.
  </li>
  <li>
  Essays will be judged on: organization, flow, grammar, content, imagination, etc.
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
          Write about the greatness of the Akshar-Purushottam Darshan
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
         Need for the Aksharbrahma Guru
        </ion-text>
      </ion-col>
      <ion-col size="5">
        <ion-text>
          Write about the necessity of the Aksharbrahma guru
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
          Write about the importance of guru bhakti
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
          Thank You Pramukh Swami Maharaj!
        </ion-text>
      </ion-col>
      <ion-col size="5">
        <ion-text>
         Write about the impact Pramukh Swami Maharaj had on others
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
        Robbinsville Akshardham
      </ion-col>
      <ion-col>
        Write about the importance of mandirs and the future impact of Robbinsville Akshardham
      </ion-col>
  </ion-row>
</ion-grid>
<div>""",
    },
    'Art-Based Talents': {
        'Painting/Illustration': """<div class="skills-html">
<h2 class="static-content-title">Rules</h2>
<ul>
	<li>
    Participants must select from one of the themes below. The categories are provided, with a small description on what the artwork should depict.
  </li>
  <li>
    Before the Adhiveshan, these pieces of artwork must be submitted electronically.
  </li>
  <li>
    Artwork may include painting, drawing, chalk art, oil pastels, etc. This does not include photoshop or any multimedia art.
  </li>
  <li>
    The artwork must be presented on an 8.5 inches by 11 inches paper or canvas.
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
         Jay Ho Akshar-Purushottam!
        </ion-text>
      </ion-col>
      <ion-col size="5">
        <ion-text>
          Depict the glory of Akshar-Purushottam Maharaj
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
          Depict the life and work of Pramukh Swami Maharaj
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
         Depict an incident from our gurus’ lives on the topic of Guru bhakti
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
        Akshardham
      </ion-col>
      <ion-col>
        Depict what Robbinsville Akshardham means to you
      </ion-col>
  </ion-row>
</ion-grid>
<div>""",
        'Graphic Design (Photoshop)': """<div class="skills-html">
<h2 class="static-content-title">Rules</h2>
<ul>
	<li>
    Participants must select from one of the themes below. The categories are provided, with a small description on what the graphic should depict.
  </li>
  <li>
    The graphic can be made using any photo editing/illustrating tool, such as Photoshop or Canva.
  </li>
  <li>
    The graphic can be in either portrait or landscape orientation.
  </li>
  <li>
    Please make sure the graphic is of good quality, such as 1920 pixels by 1080 pixels.
  </li>
</ul>
<h2 class="static-content-title">Topic List</h2>
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
          Depict the life and work of Bhagwan Swaminarayan
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
          Depict any famous prasangs from our gurus’ life
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
          Explain the life and work of Pramukh Swami Maharaj
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
         Explain an introduction of Mahant Swami Maharaj
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
        Satsang Timeline
      </ion-col>
      <ion-col>
        Depict key moments from our satsang history (local, national or global)
      </ion-col>
  </ion-row>
</ion-grid>
<div>""",
        'Video Making': """<div class="skills-html">
<h2 class="static-content-title">Rules</h2>
<ul>
	<li>
    Participants can choose any 1 suggested topic and prepare a video to submit on that topic in advance of the Adhiveshan.  The suggested topics are general, and will allow you to be creative and think freely!
  </li>
  <li>
    Video length should be maximum 5 minutes long.
  </li>
	<li>
    Video length should be maximum 5 minutes long.
  </li>
	<li>
    This video will also be submitted electronically.	
  </li>
</ul>
<h2 class="static-content-title">Topic List</h2>
<ion-grid class="ion-text-center">
  <ion-row class="header-row">
    <ion-col size="2">
      <ion-text>
        1
      </ion-text>
    </ion-col>
      <ion-col size="10">
        <ion-text>
          Pramukh Swami Maharaj: 
          A Timeless Tribute to a Timeless Guru
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
          About My Guru
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
         Satsang History
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
          Robbinsville Akshardham
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
          Mukhpath in My Life
        </ion-text>
      </ion-col>
  </ion-row>
</ion-grid>
<div>""",
        'Rangoli design': """<div class="skills-html">
<h2 class="static-content-title">Rules</h2>
<ul>
	<li>
    Participants can, but are not limited to, choose any of the suggested topics to design their rangoli. The suggested topics are general, and will allow you to be creative and think freely!
  </li>
  <li>
    Rangolis can be made from any of the following: colored powder, chalk, colored rice grains, paper cut outs, etc. Feel free to experiment with new materials.
  </li>
  <li>
    Rangolis cannot be only drawn/illustrated on paper.
  </li>
  <li>
    Photo submissions should ensure that the rangoli can be seen in good lighting and is taken from the top to see the entirety of the rangoli.
  </li>
  <li>
  Rangolis that are submitted must be new submissions and not done on prior occasions.
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
          Welcoming Gunatitanand Swami to sit alongside Harikrishna Maharaj
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
          Celebrating Pramukh Swami Maharaj’s Shatabdi Mahotsav
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
</ion-grid>
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
    'Shloka 1',
    'Shloka 4-5',
    'Shloka 8-9',
    'Shloka 24',
    'Shloka 64-65',
    'Shloka 73',
    'Shloka 76',
    'Shloka 96',
    'Shloka 97',
    'Shloka 98',
    'Shloka 106',
    'Shloka 100',
    'Shloka 212',
    'Shloka 209',
    'Shloka 152',
    'Shloka 128',
    'Shloka 149',
    'Shloka 116',
}

MAHANT_SD_SHLOKS = {
    'Shloka 1',
    'Shloka 2',
    'Shloka 3',
    'Shloka 4-5',
    'Shloka 6',
    'Shloka 7',
    'Shloka 8-9',
    'Shloka 10',
    'Shloka 18',
    'Shloka 19',
    'Shloka 22',
    'Shloka 23',
    'Shloka 24',
    'Shloka 25',
    'Shloka 96',
    'Shloka 97',
    'Shloka 98',
    'Shloka 99',
    'Shloka 100',
    'Shloka 102-103',
    'Shloka 104',
    'Shloka 105',
    'Shloka 106',
    'Shloka 107',
    'Shloka 108',
    'Shloka 109-110',
    'Shloka 111-114',
    'Shloka 115',
    'Shloka 116',
    'Shloka 131',
    'Shloka 132',
    'Shloka 134',
    'Shloka 135',
    'Shloka 64-65',
    'Shloka 73',
    'Shloka 139',
    'Shloka 140',
    'Shloka 141-142',
    'Shloka 145',
    'Shloka 146',
    'Shloka 147-148',
    'Shloka 149',
    'Shloka 150',
    'Shloka 151',
    'Shloka 152',
    'Shloka 164',
    'Shloka 209',
    'Shloka 210',
    'Shloka 212',
    'Shloka 213',
    'Shloka 256',
    'Shloka 274',
    'Shloka 225',
    'Shloka 291',
}

PRAMUKH_SD_SHLOKS = {
    'Shloka 1',
    'Shloka 2',
    'Shloka 3',
    'Shloka 4-5',
    'Shloka 6',
    'Shloka 7',
    'Shloka 8-9',
    'Shloka 10',
    'Shloka 18',
    'Shloka 19',
    'Shloka 22',
    'Shloka 23',
    'Shloka 24',
    'Shloka 25',
    'Shloka 96',
    'Shloka 97',
    'Shloka 98',
    'Shloka 99',
    'Shloka 100',
    'Shloka 102-103',
    'Shloka 104',
    'Shloka 105',
    'Shloka 106',
    'Shloka 107',
    'Shloka 108',
    'Shloka 109-110',
    'Shloka 111-114',
    'Shloka 115',
    'Shloka 116',
    'Shloka 131',
    'Shloka 132',
    'Shloka 134',
    'Shloka 135',
    'Shloka 64-65',
    'Shloka 73',
    'Shloka 139',
    'Shloka 140',
    'Shloka 141-142',
    'Shloka 145',
    'Shloka 146',
    'Shloka 147-148',
    'Shloka 149',
    'Shloka 150',
    'Shloka 151',
    'Shloka 152',
    'Shloka 164',
    'Shloka 209',
    'Shloka 210',
    'Shloka 212',
    'Shloka 213',
    'Shloka 256',
    'Shloka 274',
    'Shloka 225',
    'Shloka 291',
    'Shloka 44',
    'Shloka 45',
    'Shloka 46',
    'Shloka 47',
    'Shloka 48',
    'Shloka 126',
    'Shloka 127',
    'Shloka 128',
    'Shloka 143-144',
    'Shloka 180',
    'Shloka 185',
    'Shloka 216',
    'Shloka 233',
    'Shloka 252',
    'Shloka 253',
    'Shloka 87-88',
    'Shloka 89',
    'Shloka 90-91',
    'Shloka 92',
    'Shloka 277',
    'Shloka 279',
    'Shloka 236',
    'Shloka 195',
    'Shloka 183',
    'Shloka 184',
    'Shloka 188',
    'Shloka 287',
    'Shloka 159',
    'Shloka 160',
    'Shloka 59',
    'Shloka 136',
    'Shloka 137',
}

YOGI_SD_SHLOKS = {
    'Shloka 1',
    'Shloka 2',
    'Shloka 3',
    'Shloka 4-5',
    'Shloka 6',
    'Shloka 7',
    'Shloka 8-9',
    'Shloka 10',
    'Shloka 18',
    'Shloka 19',
    'Shloka 22',
    'Shloka 23',
    'Shloka 24',
    'Shloka 25',
    'Shloka 96',
    'Shloka 97',
    'Shloka 98',
    'Shloka 99',
    'Shloka 100',
    'Shloka 102-103',
    'Shloka 104',
    'Shloka 105',
    'Shloka 106',
    'Shloka 107',
    'Shloka 108',
    'Shloka 109-110',
    'Shloka 111-114',
    'Shloka 115',
    'Shloka 116',
    'Shloka 131',
    'Shloka 132',
    'Shloka 134',
    'Shloka 135',
    'Shloka 64-65',
    'Shloka 73',
    'Shloka 139',
    'Shloka 140',
    'Shloka 141-142',
    'Shloka 145',
    'Shloka 146',
    'Shloka 147-148',
    'Shloka 149',
    'Shloka 150',
    'Shloka 151',
    'Shloka 152',
    'Shloka 164',
    'Shloka 209',
    'Shloka 210',
    'Shloka 212',
    'Shloka 213',
    'Shloka 256',
    'Shloka 274',
    'Shloka 225',
    'Shloka 291',
    'Shloka 44',
    'Shloka 45',
    'Shloka 46',
    'Shloka 47',
    'Shloka 48',
    'Shloka 126',
    'Shloka 127',
    'Shloka 128',
    'Shloka 143-144',
    'Shloka 180',
    'Shloka 185',
    'Shloka 216',
    'Shloka 233',
    'Shloka 252',
    'Shloka 253',
    'Shloka 87-88',
    'Shloka 89',
    'Shloka 90-91',
    'Shloka 92',
    'Shloka 277',
    'Shloka 279',
    'Shloka 236',
    'Shloka 195',
    'Shloka 183',
    'Shloka 184',
    'Shloka 188',
    'Shloka 287',
    'Shloka 159',
    'Shloka 160',
    'Shloka 59',
    'Shloka 136',
    'Shloka 137',
    'Shloka 138',
    'Shloka 32',
    'Shloka 33-34',
    'Shloka 86',
    'Shloka 122',
    'Shloka 129-130',
    'Shloka 153',
    'Shloka 156-157',
    'Shloka 158',
    'Shloka 167',
    'Shloka 168',
    'Shloka 175',
    'Shloka 192',
    'Shloka 200',
    'Shloka 205',
    'Shloka 207',
    'Shloka 239',
    'Shloka 81',
    'Shloka 82',
    'Shloka 83',
    'Shloka 84',
    'Shloka 204',
    'Shloka 223',
    'Shloka 224',
    'Shloka 261',
    'Shloka 262',
    'Shloka 12',
    'Shloka 13',
    'Shloka 17',
    'Shloka 26',
    'Shloka 29',
    'Shloka 31',
    'Shloka 38',
    'Shloka 50',
    'Shloka 76',
    'Shloka 94',
    'Shloka 95',
    'Shloka 117',
    'Shloka 120',
    'Shloka 123',
    'Shloka 124',
    'Shloka 125',
    'Shloka 133',
    'Shloka 161',
    'Shloka 162',
    'Shloka 163',
    'Shloka 165',
    'Shloka 166',
    'Shloka 170',
    'Shloka 154',
    'Shloka 171',
    'Shloka 173',
    'Shloka 176',
    'Shloka 178',
    'Shloka 174',
    'Shloka 179',
    'Shloka 181',
    'Shloka 182',
    'Shloka 186',
    'Shloka 187',
    'Shloka 189',
    'Shloka 193',
    'Shloka 203',
    'Shloka 177',
    'Shloka 206',
    'Shloka 215',
    'Shloka 240',
    'Shloka 241-242',
    'Shloka 243',
    'Shloka 248',
    'Shloka 249',
    'Shloka 250',
    'Shloka 251',
    'Shloka 244',
    'Shloka 245',
    'Shloka 237-238',
    'Shloka 254',
    'Shloka 255',
    'Shloka 258-259',
    'Shloka 260',
    'Shloka 263',
    'Shloka 268',
    'Shloka 275',
    'Shloka 288-290',
    'Shloka 293-294',
    'Shloka 295-296',
    'Shloka 297-298',
    'Shloka 309-310',
    'Shloka 11',
}

SHASTRI_SD_SHLOKS = {
    'Shloka 1',
    'Shloka 2',
    'Shloka 3',
    'Shloka 4-5',
    'Shloka 6',
    'Shloka 7',
    'Shloka 8-9',
    'Shloka 10',
    'Shloka 18',
    'Shloka 19',
    'Shloka 22',
    'Shloka 23',
    'Shloka 24',
    'Shloka 25',
    'Shloka 96',
    'Shloka 97',
    'Shloka 98',
    'Shloka 99',
    'Shloka 100',
    'Shloka 102-103',
    'Shloka 104',
    'Shloka 105',
    'Shloka 106',
    'Shloka 107',
    'Shloka 108',
    'Shloka 109-110',
    'Shloka 111-114',
    'Shloka 115',
    'Shloka 116',
    'Shloka 131',
    'Shloka 132',
    'Shloka 134',
    'Shloka 135',
    'Shloka 64-65',
    'Shloka 73',
    'Shloka 139',
    'Shloka 140',
    'Shloka 141-142',
    'Shloka 145',
    'Shloka 146',
    'Shloka 147-148',
    'Shloka 149',
    'Shloka 150',
    'Shloka 151',
    'Shloka 152',
    'Shloka 164',
    'Shloka 209',
    'Shloka 210',
    'Shloka 212',
    'Shloka 213',
    'Shloka 256',
    'Shloka 274',
    'Shloka 225',
    'Shloka 291',
    'Shloka 44',
    'Shloka 45',
    'Shloka 46',
    'Shloka 47',
    'Shloka 48',
    'Shloka 126',
    'Shloka 127',
    'Shloka 128',
    'Shloka 143-144',
    'Shloka 180',
    'Shloka 185',
    'Shloka 216',
    'Shloka 233',
    'Shloka 252',
    'Shloka 253',
    'Shloka 87-88',
    'Shloka 89',
    'Shloka 90-91',
    'Shloka 92',
    'Shloka 277',
    'Shloka 279',
    'Shloka 236',
    'Shloka 195',
    'Shloka 183',
    'Shloka 184',
    'Shloka 188',
    'Shloka 287',
    'Shloka 159',
    'Shloka 160',
    'Shloka 59',
    'Shloka 136',
    'Shloka 137',
    'Shloka 138',
    'Shloka 32',
    'Shloka 33-34',
    'Shloka 86',
    'Shloka 122',
    'Shloka 129-130',
    'Shloka 153',
    'Shloka 156-157',
    'Shloka 158',
    'Shloka 167',
    'Shloka 168',
    'Shloka 175',
    'Shloka 192',
    'Shloka 200',
    'Shloka 205',
    'Shloka 207',
    'Shloka 239',
    'Shloka 81',
    'Shloka 82',
    'Shloka 83',
    'Shloka 84',
    'Shloka 204',
    'Shloka 223',
    'Shloka 224',
    'Shloka 261',
    'Shloka 262',
    'Shloka 12',
    'Shloka 13',
    'Shloka 17',
    'Shloka 26',
    'Shloka 29',
    'Shloka 31',
    'Shloka 38',
    'Shloka 50',
    'Shloka 76',
    'Shloka 94',
    'Shloka 95',
    'Shloka 117',
    'Shloka 120',
    'Shloka 123',
    'Shloka 124',
    'Shloka 125',
    'Shloka 133',
    'Shloka 161',
    'Shloka 162',
    'Shloka 163',
    'Shloka 165',
    'Shloka 166',
    'Shloka 170',
    'Shloka 154',
    'Shloka 171',
    'Shloka 173',
    'Shloka 176',
    'Shloka 178',
    'Shloka 174',
    'Shloka 179',
    'Shloka 181',
    'Shloka 182',
    'Shloka 186',
    'Shloka 187',
    'Shloka 189',
    'Shloka 193',
    'Shloka 203',
    'Shloka 177',
    'Shloka 206',
    'Shloka 215',
    'Shloka 240',
    'Shloka 241-242',
    'Shloka 243',
    'Shloka 248',
    'Shloka 249',
    'Shloka 250',
    'Shloka 251',
    'Shloka 244',
    'Shloka 245',
    'Shloka 237-238',
    'Shloka 254',
    'Shloka 255',
    'Shloka 258-259',
    'Shloka 260',
    'Shloka 263',
    'Shloka 268',
    'Shloka 275',
    'Shloka 288-290',
    'Shloka 293-294',
    'Shloka 295-296',
    'Shloka 297-298',
    'Shloka 309-310',
    'Shloka 11',
    'Shloka 14-16',
    'Shloka 20',
    'Shloka 21',
    'Shloka 27',
    'Shloka 28',
    'Shloka 30',
    'Shloka 35',
    'Shloka 36',
    'Shloka 37',
    'Shloka 39',
    'Shloka 40',
    'Shloka 41',
    'Shloka 42',
    'Shloka 43',
    'Shloka 49',
    'Shloka 51',
    'Shloka 52',
    'Shloka 53-54',
    'Shloka 55',
    'Shloka 56-58',
    'Shloka 60',
    'Shloka 61',
    'Shloka 62',
    'Shloka 63',
    'Shloka 66-67',
    'Shloka 68',
    'Shloka 69',
    'Shloka 70',
    'Shloka 71',
    'Shloka 72',
    'Shloka 74',
    'Shloka 75',
    'Shloka 77',
    'Shloka 78',
    'Shloka 79-80',
    'Shloka 85',
    'Shloka 93',
    'Shloka 101',
    'Shloka 118',
    'Shloka 119',
    'Shloka 121',
    'Shloka 155',
    'Shloka 169',
    'Shloka 172',
    'Shloka 190',
    'Shloka 191',
    'Shloka 194',
    'Shloka 196',
    'Shloka 197',
    'Shloka 198',
    'Shloka 199',
    'Shloka 201-202',
    'Shloka 208',
    'Shloka 211',
    'Shloka 214',
    'Shloka 217',
    'Shloka 218-219',
    'Shloka 220',
    'Shloka 221',
    'Shloka 222',
    'Shloka 226',
    'Shloka 227',
    'Shloka 228',
    'Shloka 229',
    'Shloka 230',
    'Shloka 231',
    'Shloka 232',
    'Shloka 234',
    'Shloka 235',
    'Shloka 246',
    'Shloka 247',
    'Shloka 257',
    'Shloka 264-265',
    'Shloka 266',
    'Shloka 267',
    'Shloka 269',
    'Shloka 270',
    'Shloka 271',
    'Shloka 272-273',
    'Shloka 276',
    'Shloka 278',
    'Shloka 280',
    'Shloka 281',
    'Shloka 282',
    'Shloka 283-284',
    'Shloka 285',
    'Shloka 286',
    'Shloka 292',
    'Shloka 299',
    'Shloka 300',
    'Shloka 301',
    'Shloka 302',
    'Shloka 303',
    'Shloka 304',
    'Shloka 305',
    'Shloka 306',
    'Shloka 307',
    'Shloka 308',
    'Shloka 311-314',
    'Shloka 315',
}

SD_SHLOKAS_FOR_TIER = {
    GHANSHYAM: GHANSHYAM_SD_SHLOKAS,
    MAHANT: MAHANT_SD_SHLOKS,
    PRAMUKH: PRAMUKH_SD_SHLOKS,
    YOGI: YOGI_SD_SHLOKS,
    SHASTRI: SHASTRI_SD_SHLOKS,
}


# Announcements
BM_STORIES = [{
    "title": "Memories With Bapa",
    "url": "https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/KM%20Module%20Photos/21smruti.jpg",
    "stories": [
      {
        "url": 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/KM%20Module%20Photos/Mahant_Swami_Maharaj.jpg',
        "type": "image"
      },
      {
        "url": 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/KM%20Module%20Photos/21smruti.jpg',
        "type": "image"
      },
      {
        "url": 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/KM%20Module%20Photos/14agna.jpg',
        "type": "image"
      },
    ]
  },
  {
    "title": "Bapa's Vicharan",
    "url": "https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/KM%20Module%20Photos/21smruti.jpg",
    "stories": [
      {
        "url": 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/KM%20Module%20Photos/Mahant_Swami_Maharaj.jpg',
        "type": "image"
      },
      {
        "url": 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/KM%20Module%20Photos/21smruti.jpg',
        "type": "image"
      },
      {
        "url": 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/KM%20Module%20Photos/14agna.jpg',
        "type": "image"
      },
      {
        "url": 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/KM%20Module%20Photos/14agna.jpg',
        "quote": "Some Inspiring Quote...\n-Some Great Person",
        "type": "quote",
      }
    ]
  },
]

KM_STORIES = [{
    "title": "Memories With Bapa",
    "url": "https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/KM%20Module%20Photos/21smruti.jpg",
    "stories": [
      {
        "url": 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/KM%20Module%20Photos/Mahant_Swami_Maharaj.jpg',
        "type": "image"
      },
      {
        "url": 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/KM%20Module%20Photos/21smruti.jpg',
        "type": "image"
      },
      {
        "url": 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/KM%20Module%20Photos/14agna.jpg',
        "type": "image"
      },
      {
        "url": 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/Stories/IMG_0472.mov',
        "type": "video",
      },
      {
        "url": 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/KM%20Module%20Photos/14agna.jpg',
        "quote": "Some Inspiring Quote...\n-Some Great Person",
        "type": "quote",
      }
    ]
  },
  {
    "title": "Bapa's Vicharan",
    "url": "https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/KM%20Module%20Photos/21smruti.jpg",
    "stories": [
      {
        "url": 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/KM%20Module%20Photos/Mahant_Swami_Maharaj.jpg',
        "type": "image"
      },
      {
        "url": 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/KM%20Module%20Photos/21smruti.jpg',
        "type": "image"
      },
      {
        "url": 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/KM%20Module%20Photos/14agna.jpg',
        "type": "image"
      },
      {
        "url": 'https://pause.sfo2.cdn.digitaloceanspaces.com/Other/Adhiveshan%20Website/KM%20Module%20Photos/14agna.jpg',
        "quote": "Some Inspiring Quote...\n-Some Great Person",
        "type": "quote",
      }
    ]
  },
]

BM_ANNOUNCEMENTS = [
    {
        'timestamp': '12 Jan, 2021',
        'text': 'Jai Swaminarayan balaks and balikas. Welcome to the Adhiveshan website! We are very excited to begin our journey towards Guru Bhakti.'
    },
    {
        'timestamp': '13 Jan, 2021',
        'text': 'Pledging is now live on BKMS! Make sure you contact your karyakars if you are having any issues or problems. Remember that pledges made on the website are not automatically made for you on BKMS!'
    },
    {
        'timestamp': '13 Jan, 2021',
        'text': 'On Saturday, February 6th, please join your parents to attend a special Adhiveshan Sabha. You will be able to hear more about the mahima of Adhiveshan and learn how to use tools such as the website.'
    }
]

KM_ANNOUNCEMENTS = [
    {
        'timestamp': '13 Jan, 2021',
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

