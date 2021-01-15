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
                      'integral way for balaks and balikas to earn the raajipo of our Gurus. By learning and '
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
                      'second part is the Adhiveshan Raajipo Challenge (Main Mukhpath), which will be assessed online '
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
    "Adhiveshan Raajipo Challenge (Advanced Mukhpath)": [
        {
            'question': "How is the Adhiveshan Raajipo Challenge (Advanced Mukhpath) structured?",
            'answer': "The Raajipo Challenge is broken up into 5 categories: Satsang Diksha, Swamini Vato, Kirtans, "
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
                      "with the tier you chose for your Raajipo Challenge from August 2020. If you would like to "
                      "change it, there will be an opportunity for you to repledge your original Satsang Diksha "
                      "pledge when you pledge for the other Adhiveshan categories.",
        },
        {
            'question': "Will there be additional material to help me study?",
            'answer': "Along with this book, there will be additional material provided via a website including "
                      "interactive aids to help memorize the Adhiveshan content. The website will also contain small "
                      "interactive quizzes to aid in memorization and self-evaluation. Details for this website will "
                      "come soon.",
        },
    ],
    "Adhiveshan Timeline": [
        {
            'question': "What are some important dates to keep in mind relating to the Adhiveshan?",
            'answer': "SS21 Adhiveshan Launch Sabha: 1/31/2021\nAdhiveshan Pledge and Summer Shibir registration: "
                      "1/31/2021-3/7/2021\nBeginner's Challenge Quiz: To be held at home - Time soon to come\nTalent "
                      "Competition Submission Deadline: Time soon to come\nAdhiveshan Raajipo Challenge: Time soon to "
                      "come",
        },
    ],
}

# Skills Challenge
SKILLS_CHALLENGE = {
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
		Participants will speak on one of Yogiji Maharaj’s Bodh Katha. A sample list is provided below, however participants can choose any bodh katha from the book, 101 Tales of Wisdom. If you do not have a book, a short version can be found at: http://www.swaminarayan.org/yogijimaharaj/talesofwisdom/ 
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
    <ion-col size="5">
      <ion-text>Bodh Katha</ion-text>
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
      <ion-col size="5">
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
      <ion-col size="5">
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
      <ion-col size="5">
        <ion-text>
          The Sesame Seed Scholar
        </ion-text>
      </ion-col>
    <ion-row>
      <ion-col size="2">
        <ion-text>
          5
        </ion-text>
      </ion-col>
        <ion-col size="5">
          <ion-text>
            The Lazy Man
          </ion-text>
        </ion-col>
    </ion-row>
  </ion-row>
</ion-grid>
<div>""",
        'Satsang Diksha Nirupan': "",
        'Prasang-Varnan Speech': "",
    },
    'Music-Based Competitions': {
        'Solo Singing': "",
        'Musical Instruments': "",
    },
    'Writing-Based Competitions': {
        'Poetry': "",
        'Essay-Writing (Group 3)': "",
    },
    'Art-Based Talents': {
        'Painting/Illustration': "",
        'Graphic Design (Photoshop)': "",
        'Video Making': "",
        'Rangoli design': "",
    },
}

# Satsang Diksha Tiers
# Contains set of SD shloks in ghanshyam tier, indexed by title.
GHANSHYAM_SD_SHLOKS = {
    'Shloka 1',
    'Shloka 4 & 5',
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
    'Shloka 4 & 5',
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
}

PRAMUKH_SD_SHLOKS = {
    'Shloka 1',
    'Shloka 2',
    'Shloka 3',
    'Shloka 4 & 5',
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
    'Shloka 4 & 5',
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
    'Shloka 4 & 5',
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

SD_SHLOKS_FOR_TIER = {
    GHANSHYAM: GHANSHYAM_SD_SHLOKS,
    MAHANT: MAHANT_SD_SHLOKS,
    PRAMUKH: PRAMUKH_SD_SHLOKS,
    YOGI: YOGI_SD_SHLOKS,
    SHASTRI: SHASTRI_SD_SHLOKS,
}
