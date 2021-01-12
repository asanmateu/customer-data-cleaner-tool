from addtypes import valid_types
from errors import ERROR_TYPE
from alerts import ALERT_TYPE
from columns import ERROR, ALERT, ADDRESS_TYPE, ADDRESS_1, ADDRESS_2, ADDRESS_CODE, STORE_NAME, CUSTOMER_CODE
from lengths import LIMITS


def address_type_cleaner(data):
    """ Clean valid address types. Make sure that there is only one B and one S per customer
    code unless there are unique address codes. Address 1 cannot be empty, if it is notes error.

    Notes:
        Run before doing any other work on addresses. Make sure store_cleaner has been run.
    """
    address_types = [*map(lambda x: x.lower(), data[ADDRESS_TYPE])]

    # # Iterate over input address type list and populate empty list with clean values ...
    for i, row in data.iterrows():
        reference_address_type = address_types[i]
        if reference_address_type not in valid_types.keys():
            data[ERROR].iloc[i] = str(row[ERROR]) + f"{reference_address_type}" + ERROR_TYPE['address_type_error']
        else:
            data[ADDRESS_TYPE].iloc[i] = valid_types[reference_address_type]

    return data


def address_cleaner(data):
    """ Address 1 cannot be empty, if it is notes error. """

    for i, row in data.iterrows():
        # If address 1 is empty then note an error...
        if row[ADDRESS_1] == "":
            data[ERROR].iloc[i] = str(row[ERROR]) + ERROR_TYPE['address_error']

        # If Address 1 exceeds the character limit then note an alert and remove the value...
        if len(str(row[ADDRESS_1])) > LIMITS['address_1']:
            data[ALERT].iloc[i] = str(row[ALERT]) + ALERT_TYPE['address1_length']
            data[ADDRESS_1].iloc[i] = ""

    return data


def address_code_cleaner(data):
    """ Make sure that there is only one B and one S per customer code unless there are
    unique address codes. Only note error on extra ones. """

    # Separate rows that are unique in terms of the subsets specified from the duplicates...
    uniques = data.drop_duplicates(subset=[CUSTOMER_CODE, STORE_NAME, ADDRESS_TYPE, ADDRESS_CODE])
    duplicates = data.iloc[list(set(data.index) - set(uniques.index))]

    # Note error if connections has a second B or S address type without unique address code...
    for i in range(len(duplicates)):
        index = duplicates.index[i]
        data[ERROR].iloc[index] = str(data[ERROR].iloc[index]) + ERROR_TYPE['address_code_error']

        # If address code exceeds the character limit then note an error...
        if len(data[ADDRESS_CODE].iloc[i]) > LIMITS['address_code']:
            data[ERROR].iloc[i] = str(data[ERROR].iloc[i]) + ERROR_TYPE['address_code_length']

    return data