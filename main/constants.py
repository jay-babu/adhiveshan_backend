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
