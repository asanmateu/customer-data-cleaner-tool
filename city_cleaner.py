# Import necessary modules...
from columns import CITY, ERROR, ALERT
from errors import ERROR_TYPE
from alerts import ALERT_TYPE
from lengths import LIMITS


def city_cleaner(data):
    """ Note an error if city input is empty otherwise pass. """

    for i, row in data.iterrows():
        # If city is empty note an error for invalid city input...
        if row[CITY] == '':
            data[ERROR].iloc[i] = str(row[ERROR]) + ERROR_TYPE['city_error']

        # If city length exceeds character limit note an alert and remove the value...
        if len(str(row[CITY])) > LIMITS['city']:
            data[ALERT].iloc[i] = str(row[ALERT]) + f"{row[CITY]}" + ALERT_TYPE['city_length']
            data[CITY].iloc[i] = ""

    return data
