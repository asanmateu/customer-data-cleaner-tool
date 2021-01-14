# Contains countries which require a correct state input for validation...
state_countries = ["Australia", "Canada", "Japan", "United States"]

# Contains valid input states for each country...
# Dictionary with United States valid states:
usa_states = {
    'Alaska': 'AK',
    'Alabama': 'AL',
    'Arkansas': 'AR',
    'American Samoa': 'AS',
    'Arizona': 'AZ',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'District of Columbia': 'DC',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Iowa': 'IA',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Massachusetts': 'MA',
    'Maryland': 'MD',
    'Maine': 'ME',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Missouri': 'MO',
    'Mississippi': 'MS',
    'Montana': 'MT',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Nebraska': 'NE',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'Nevada': 'NV',
    'New York': 'NY',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Puerto Rico': 'PR',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Virginia': 'VA',
    'Virgin Islands': 'VI',
    'Vermont': 'VT',
    'Wisconsin': 'WI',
    'West Virginia': 'WV',
    'Wyoming': 'WY',
    'ak': 'AK',
    'al': 'AL',
    'ar': 'AR',
    'as': 'AS',
    'az': 'AZ',
    'ca': 'CA',
    'co': 'CO',
    'ct': 'CT',
    'dc': 'DC',
    'de': 'DE',
    'fl': 'FL',
    'ga': 'GA',
    'hi': 'HI',
    'ia': 'IA',
    'id': 'ID',
    'il': 'IL',
    'in': 'IN',
    'ks': 'KS',
    'ky': 'KY',
    'la': 'LA',
    'ma': 'MA',
    'md': 'MD',
    'me': 'ME',
    'mi': 'MI',
    'mn': 'MN',
    'mo': 'MO',
    'ms': 'MS',
    'mt': 'MT',
    'nc': 'NC',
    'nd': 'ND',
    'ne': 'NE',
    'nh': 'NH',
    'nj': 'NJ',
    'nm': 'NM',
    'nv': 'NV',
    'ny': 'NY',
    'oh': 'OH',
    'ok': 'OK',
    'or': 'OR',
    'pa': 'PA',
    'pr': 'PR',
    'ri': 'RI',
    'sc': 'SC',
    'sd': 'SD',
    'tn': 'TN',
    'tx': 'TX',
    'ut': 'UT',
    'va': 'VA',
    'vi': 'VI',
    'vt': 'VT',
    'wi': 'WI',
    'wv': 'WV',
    'wy': 'WY'
}

# Dictionary with Canada valid states...
cad_states = {
    'Alberta': 'AB',
    'Northwest Territories': 'NT',
    'Nova Scotia': 'NS',
    'British Columbia': 'BC',
    'Ontario': 'ON',
    'Manitoba': 'MB',
    'Prince Edward Island': 'PE',
    'New Brunswick': 'NB',
    'Quebec': 'QC',
    'Saskatchewan': 'SK',
    'Newfoundland Labrador': 'NL',
    'Yukon': 'YT',
    'Nunavut': 'NU',
    'ab': 'AB',
    'nt': 'NT',
    'ns': 'NS',
    'bc': 'BC',
    'on': 'ON',
    'mb': 'MB',
    'pe': 'PE',
    'nb': 'NB',
    'qc': 'QC',
    'sk': 'SK',
    'nl': 'NL',
    'yt': 'YT',
    'nu': 'NU'
}

# Dictionary with Australia valid states...
aus_states = {
    'Queensland': 'QLD',
    'Tasmania': 'TAS',
    'Victoria': 'VIC',
    'South Australia': 'SA',
    'Northern Territory': 'NT',
    'Western Australia': 'WA',
    'New South Wales': 'NSW',
    'Australian Capital Territory': 'ACT',
    'qld': 'QLD',
    'tas': 'TAS',
    'vic': 'VIC',
    'sa': 'SA',
    'nt': 'NT',
    'wa': 'WA',
    'nsw': 'NSW',
    'act': 'ACT'
}

# Dictionary with Japan's valid states...
jpn_states = {
    'Aichi': 'Aichi',
    'Akita': 'Akita',
    'Aomori': 'Aomori',
    'Chiba': 'Chiba',
    'Ehime': 'Ehime',
    'Fukui': 'Fukui',
    'Fukuoka': 'Fukuoka',
    'Fukushima': 'Fukushima',
    'Gifu': 'Gifu',
    'Gunma': 'Gunma',
    'Hiroshima': 'Hiroshima',
    'Hokkaido': 'Hokkaido',
    'Hyogo': 'Hyogo',
    'Ibaraki': 'Ibaraki',
    'Ishikawa': 'Ishikawa',
    'Iwate': 'Iwate',
    'Kagawa': 'Kagawa',
    'Kagoshima': 'Kagoshima',
    'Kanagawa': 'Kanagawa',
    'Kochi': 'Kōchi',
    'Kōchi': 'Kōchi',
    'KÅ%chi': 'Kōchi',
    'Kumamoto': 'Kumamoto',
    'Kyoto': 'Kyoto',
    'Mie': 'Mie',
    'Miyagi': 'Miyagi',
    'Miyazaki': 'Miyazaki',
    'Nagano': 'Nagano',
    'Nagasaki': 'Nagasaki',
    'Nara': 'Nara',
    'Niigata': 'Niigata',
    'Oita': 'Ōita',
    'Ōita': 'Ōita',
    'ÅŒita': 'Ōita',
    'Okayama': 'Okayama',
    'Okinawa': 'Okinawa',
    'Osaka': 'Osaka',
    'Saga': 'Saga',
    'Saitama': 'Saitama',
    'Shiga': 'Shiga',
    'Shimane': 'Shimane',
    'Shizuoka': 'Shizuoka',
    'Tochigi': 'Tochigi',
    'Tokushima': 'Tokushima',
    'Tokyo': 'Tokyo',
    'Tottori': 'Tottori',
    'Toyama': 'Toyama',
    'Wakayama': 'Wakayama',
    'Yamagata': 'Yamagata',
    'Yamaguchi': 'Yamaguchi',
    'Yamanashi': 'Yamanashi'
}

# Normalise dictionary keys to avoid case sensitivity related issues...
usa_states = {k.lower(): v for k, v in usa_states.items()}
cad_states = {k.lower(): v for k, v in cad_states.items()}
aus_states = {k.lower(): v for k, v in aus_states.items()}
jpn_states = {k.lower(): v for k, v in aus_states.items()}