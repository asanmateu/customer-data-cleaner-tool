# Import necessary modules...
from states import state_countries, aus_states, usa_states, cad_states, jpn_states
from errors import ERROR_TYPE
from lengths import LIMITS


# Function to validate and clean states for required countries...
def state_cleaner(data):
    """ Note an error if country requires state and the state input is invalid.

    Notes:
        Use AFTER country column is clean.
    """

    countries = [*map(lambda x: x.title(), data['Country'])]
    states = [*map(lambda x: x.lower(), data['State'])]

    for i, row in data.iterrows():
        reference_country = countries[i]
        reference_state = states[i]

        # If country is in state countries check if the input state is valid otherwise not error...
        if reference_country in state_countries:
            if ((reference_country == 'United States') and (reference_state not in usa_states.keys())) or \
                    ((reference_country == 'Canada') and (reference_state not in cad_states.keys())) or \
                    ((reference_country == 'Australia') and (reference_state not in aus_states.keys())) or \
                    ((reference_country == 'Australia') and (reference_state not in jpn_states.keys())):
                row['ERROR'] = str(row['ERROR']) + ERROR_TYPE['state_error']

        # If length exceeds the limit note an error...
        if len(str(row['State'])) > LIMITS['state']:
            row['ERROR'] = str(row['ERROR']) + ERROR_TYPE['state_length']

    return data
