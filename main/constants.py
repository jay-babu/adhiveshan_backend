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

# KM Only
BRONZE = 'bronze'
SILVER = 'silver'
GOLD = 'gold'
PLATINUM = 'platinum'

# REQUIRED_PER_KM_MODULE num of mukhpath items need to be
# memorized per module for kishore mandal.
REQUIRED_PER_KM_MODULE = 4

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


FAQ = {
    'General': [
        {
            'question': 'What is Adhiveshan?',
            'answer': 'Adhiveshan is a structured way of memorizing mukhpath which is sometimes focused on a certain satsang topic or theme. Adhiveshan is NOT a competition, but rather a challenge for ourselves to sacrifice our time to memorize the mukhpath, learn its meaning, and eventually imbibe it in our lives to please our Mahant Swami Maharaj.',
        },
        {
            'question': 'Why do we do Adhiveshans?',
            'answer': 'Adhiveshan has been very dear to the hearts of our Gurus. Starting with Yogi Bapa’s passion for balaks and balikas to memorize mukhpath during their summer vacations to the various Adhiveshans held with Pramukh Swami Maharaj and Mahant Swami Maharaj, mukhpath has been an integral way for balaks and balikas to earn the raajipo of our Gurus. By learning and memorizing various parts of our Shastras, we are able to ground ourselves in the Akshar Purushottam Upasana and find solutions to the many problems we may face in life. Along with this, this Adhiveshan will also help us gear up for the upcoming Pramukh Swami Maharaj Shatabdi Mahotsav and Aksharsham Mahotsav.',
        },
        {
            'question': 'Which Adhiveshan do I pledge for and which Summer Shibir do I go to?',
            'answer': 'You will pledge for the tiers in the group you currently are in (as of January 2021). For example, if you are in Group 2 in January of 2021, and even if you are graduating and moving to Group 3 in September 2021, you will pledge for Adhiveshan in the Group 2 categories. Anyone in Groups 1-3 will also attend the Bal/Balika summer shibir.\nAdditionally, current 8th graders will pledge for the Kishore/Kishori Adhiveshan and will join the Kishore/Kishori Shibir.\nThose currently in Group 0 will pledge for the Group 0 adhiveshan, even if they are graduating and moving to Group 1 in September 2021; those currently in Group 0 will join the Bal/Balika Group 0 shibir.',
        },
        {
            'question': 'What does Adhiveshan consist of?',
            'answer': 'Adhiveshan will have three parts, each assessed in different ways and at different times. The first part is the Beginner’s Challenge (Prathmik Mukhpath) which will be assessed at home. The second part is the Adhiveshan Raajipo Challenge (Main Mukhpath), which will be assessed online (in real time - over Zoom). The final part is the Skills Challenge (Talent Competitions), which will be judged through regional online submissions.',
        },
    ],
    'Beginner’s Challenge (Prathmik Mukhpath)': [
        {
            'question': "What is the Beginner\'s Challenge (Prathmik Mukhpath)?",
            'answer': "The Beginner's Challenge contains the core mukhpath of our sanstha. All of the mukhpath comes with translations, so it is important to pay close attention to the meanings and try to introspect on how the values being transmitted in the words can be applied back to our lives. The Beginner's Challenge will be administered at home, wherein you all will complete a worksheet. Your parents will aid in ensuring that you have completed the worksheet properly and assist in grading.",
        },
    ],
    "Adhiveshan Raajipo Challenge (Advanced Mukhpath)": [
        {
            'question': "How is the Adhiveshan Raajipo Challenge (Advanced Mukhpath) structured?",
            'answer': "The Raajipo Challenge is broken up into 5 categories: Satsang Diksha, Swamini Vato, Kirtans, Shlokas and Sakhis, and Prasang Manan. There are 4 tiers (Mahant, Pramukh, Yogi, and Shastri).\nNOTE: There is an additional tier called the Ghanshyam tier that is ONLY if you are in Group 0. However, if you are in Group 1, you can select the Ghanshyam tier ONLY for Satsang Diksha (for the other categories, you must pick from the normal 4 tiers).\nThe breakdown for each tier and each group is found in the appendix on the last page.",
        },
        {
            'question': "Is there a minimum number of tiers/categories needed to participate in the Adhiveshan?",
            'answer': "As per Swamishri’s ruchi, the focus of this Adhiveshan is to learn, understand, and imbibe various satsang shastras in the lives of balaks and balikas. Thus, there is no mandatory minimum amount of categories you need to pledge to be able to participate in the Adhiveshan. Although, you should still strive to pledge for as many categories as you can and push yourselves to strive for higher tiers to make Swamishri extra raaji.",
        },
        {
            'question': "Can we choose which items to memorize in each category?",
            'answer': "The Satsang Diksha category is the only category that will have a set number of shlokas for each tier. For example if you choose the Mahant Challenge for the Satsang Diksha category, there will be a pre-set list of 64 shlokas. For all of the other categories (Swamini Vato, Shloka/Sakhi, Kirtan, Prasang Manan), you will have a choice in creating your own set with the available list of mukhpath. For example, if you are a group 1 balak or balika who wants to do the Yogi challenge for Kirtans, you will be able to choose any 4 out of a possible list of 15 kirtans listed in the book.",
        },
    ],
    "Skills Challenge (Talent Competitions)": [
        {
            'question': "What is the Skills Challenge (Talent Competition)?",
            'answer': "The Skills Challenge allows you to tie your passions and hobbies back to Satsang. You will have a chance to show your talents in a multitude of fashions included in the mukhbath booklet. You will be able to choose a minimum of 1 and a maximum of 3 categories. More details on the rules and regulations for each of the specific skills challenges are listed in the book.",
        },
    ],
    "Adhiveshan Pledging": [
        {
            'question': "How can I pledge for Adhiveshan?",
            'answer': "You will be able to pledge for Adhiveshan through BKMS after the Launch Sabha at the end of January. You will be able to access this link until 3/7/21. By this date, you must submit their pledges. Before this date, please read through the Mukhpath book and take a look at the possible tiers for your group and make a decision on what mukhpath you will be able to memorize by the summer.\nNOTE: If you pledge for Satsang Diksha, you should try to continue with the tier you chose for your Raajipo Challenge from August 2020. If you would like to change it, there will be an opportunity for you to repledge your original Satsang Diksha pledge when you pledge for the other Adhiveshan categories.",
        },
        {
            'question': "Will there be additional material to help me study?",
            'answer': "Along with this book, there will be additional material provided via a website including interactive aids to help memorize the Adhiveshan content. The website will also contain small interactive quizzes to aid in memorization and self-evaluation. Details for this website will come soon.",
        },
    ],
    "Adhiveshan Timeline": [
        {
            'question': "What are some important dates to keep in mind relating to the Adhiveshan?",
            'answer': "SS21 Adhiveshan Launch Sabha: 1/31/2021\nAdhiveshan Pledge and Summer Shibir registration: 1/31/2021-3/7/2021\nBeginner's Challenge Quiz: To be held at home - Time soon to come\nTalent Competition Submission Deadline: Time soon to come\nAdhiveshan Raajipo Challenge: Time soon to come",
        },
    ],
}
