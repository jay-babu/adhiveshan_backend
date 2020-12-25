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
CENTERS = {
    'cherry_hill',
    'edison',
    'philadelphia',
    'robbinsville',
}

CHERRY_HILL = 'cherry_hill'
EDISON = 'edison'
PHILADELPHIA = 'philadelphia'
ROBBINSVILLE = 'robbinsville'
BOSTON = 'boston'
ATLANTA = 'atlanta'
HOUSTON = 'houston'
CHINO_HILLS = 'chino_hills'
CHICAGO = 'chicago'
TORONTO = 'toronto'

REGIONS_CENTERS = {
    NORTHEAST: {
        BOSTON,
        CHERRY_HILL,
        EDISON,
        PHILADELPHIA,
        ROBBINSVILLE,
    },
    SOUTHEAST: {
        ATLANTA
    },
    SOUTHWEST: {
        HOUSTON
    },
    WEST: {
        CHINO_HILLS,
    },
    MIDWEST: {
        CHICAGO,
    },
    CANADA: {
        TORONTO,
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