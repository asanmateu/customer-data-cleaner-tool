from queries import query_customer_groups
from alerts import ALERT_TYPE
from designer_id import DESIGNER_ID
from columns import CUSTOMER_GROUP_NAME, CUSTOMER_GROUP_CODE, ALERT


def customer_group_cleaner(data, designer_id: int = DESIGNER_ID):
    """ It will clean customer group values if name in different case scenarios and if it cannot it will
    throw an alert and default both group name and code to none. """

    # Check if columns exist in template provided...
    if (CUSTOMER_GROUP_NAME in data.columns) and (CUSTOMER_GROUP_CODE in data.columns):

        # Unpack customer group dictionary from prod...
        customer_groups_dict = query_customer_groups(designer_id)

        # Initiate row iterations over dataframe...
        for i, row in data.iterrows():

            # Note references for better readability...
            reference_group_name = row[CUSTOMER_GROUP_NAME]
            reference_group_code = row[CUSTOMER_GROUP_CODE]

            # If group name is blank but there is a group code
            if (reference_group_name == "") and (reference_group_code != ""):
                # Set an alert: group name is required...
                data[ALERT].iloc[i] = str(row[ALERT]) + f"{reference_group_code}" +\
                                        ALERT_TYPE['customer_group_name_required']
                # Reset values to no default...
                data[CUSTOMER_GROUP_CODE].iloc[i] = ""

            # If group name is provided but group code is not
            elif (reference_group_name != "") and (reference_group_code == ""):
                # If group name is in existing customer groups dictionary keys rescue code...
                if reference_group_name in customer_groups_dict.keys():
                    data[CUSTOMER_GROUP_CODE].iloc[i] = customer_groups_dict.get(reference_group_name)
                # If group name is not setup then throw and alert and default to none...
                else:
                    data[ALERT].iloc[i] = str(row[ALERT]) + f"{reference_group_name}" +\
                                            ALERT_TYPE['customer_group_setup']
                    data[CUSTOMER_GROUP_NAME].iloc[i] = ""

            # If both group name and code are provided...
            elif (reference_group_name != "") and (reference_group_code != ""):
                # If neither name or code are setup alert and default to none...
                if (reference_group_name not in customer_groups_dict.keys()) and (
                        reference_group_code not in customer_groups_dict.values()):
                    data[ALERT].iloc[i] = str(row[ALERT]) + f"{reference_group_name}: {reference_group_code}" + \
                                            ALERT_TYPE['customer_group_setup']
                    data[CUSTOMER_GROUP_NAME].iloc[i] = ""
                    data[CUSTOMER_GROUP_CODE].iloc[i] = ""
                # If code exists but name does not then note a match alert and default to none...
                elif (reference_group_name not in customer_groups_dict.keys()) and (
                        reference_group_code in customer_groups_dict.values()):
                    data[ALERT].iloc[i] = str(row[ALERT]) + f"{reference_group_name}: {reference_group_code}" + \
                                            ALERT_TYPE['customer_group_setup']
                    data[CUSTOMER_GROUP_NAME].iloc[i] = ""
                    data[CUSTOMER_GROUP_CODE].iloc[i] = ""
                # If group name exists but code is not found then rescue code...
                elif (reference_group_name in customer_groups_dict.keys()) and (
                        reference_group_code not in customer_groups_dict.values()):
                    data[CUSTOMER_GROUP_CODE].iloc[i] = customer_groups_dict.get(reference_group_name)
                # If name and code are both set up but don't match...
                elif customer_groups_dict.get(reference_group_name) != reference_group_code:
                    data[ALERT].iloc[i] = str(row[ALERT]) + f"{reference_group_name}: {reference_group_code}" + \
                                            ALERT_TYPE['customer_group_match']
                    data[CUSTOMER_GROUP_NAME].iloc[i] = ""
                    data[CUSTOMER_GROUP_CODE].iloc[i] = ""

        return data