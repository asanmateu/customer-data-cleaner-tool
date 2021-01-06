# Import prod connection modules
from connection import query_read_only_prod
from myutils import strip_df


def query_company_number(designer_id: int):
    """Takes designer id and retrieves active company number details for the desired
    designer ready for validation. """

    return


def query_customer_groups(designer_id: int):
    """Takes designer id and retrieves active customer group name and code details for the desired
    designer ready for validation. """

    query = f"select customer_group_name, customer_group_code from joor_web.customer_groups " \
            f"where account_id = {designer_id} and deleted = FALSE;"

    # Extract df with designer's active customer groups...
    customer_groups = query_read_only_prod(query)

    # Remove whitespaces...
    customer_groups = strip_df(customer_groups)

    # Set customer group data in dictionary format..-
    customer_groups_dict = dict(zip(customer_groups['customer_group_name'].astype(str),
                                    customer_groups['customer_group_code'].astype(str)))

    return customer_groups_dict


def query_price_types(designer_id: int):
    """ Take designer id and call prod to make a query that retrieves active price types
    for the specific designer id.

    Returns:
        pandas DataFrame with desired columns.

    """
    query = f"select c.code as wholesale_currency, pt.name as price_label, cx.code as retail_currency, pt.created " \
            f"from joor_web.price_types pt join joor_web.currencies c on c.id = pt.currency_id " \
            f"join joor_web.currencies cx on cx.id = pt.retail_currency_id " \
            f"where pt.designer_id = {designer_id};"

    # Extract price type data from specific designer id...
    price_types = query_read_only_prod(query)

    # Remove whitespaces...
    price_types = strip_df(price_types)

    # Sort extracted DataFrame by creation data to ease default...
    price_types = price_types.sort_values(by='created', ascending=True).reset_index(drop=True)

    # Store first creation as default value
    default_price_tuple = tuple(price_types.iloc[0][:3])

    # Separate into two dictionaries: wholesale and retail
    wholesale_prices_dict = dict(zip(price_types['price_label'], price_types['wholesale_currency']))
    retail_prices_dict = dict(zip(price_types['price_label'], price_types['retail_currency']))

    return default_price_tuple, wholesale_prices_dict, retail_prices_dict


def query_sales_reps(designer_id: int):
    """ Take designer id and call prod to make a query that retrieves account users
    for the specific designer id.

    Returns:
        pandas DataFrame with desired columns.
    """
    # Query with f-string to insert designer id and close as string...
    query = f"select id, code, display_name from joor_web.accounts_users where account_id = {designer_id};"
    sales_reps = query_read_only_prod(query)

    # Remove whitespaces...
    sales_reps = strip_df(sales_reps)

    # Extract unique values...
    unique_sales_reps = sales_reps.drop_duplicates(subset=['code', 'display_name'])
    sales_reps_dict = dict(zip(unique_sales_reps['display_name'].astype(str), unique_sales_reps['code'].astype(str)))

    return sales_reps_dict


def query_payment_methods(designer_id: int):
    """ Take designer id and call prod to make a query that retrieves active payment methods
    for the specific designer id.

    Returns:
        pandas DataFrame with desired columns.

   """
    query = f'select dpm.code, pm.payment_name from joor_web.designer_payment_methods dpm join' \
            f' joor_web.payment_methods pm on pm.id = dpm.payment_method_id where ' \
            f'dpm.designer_id = {designer_id} and dpm.deleted = 0;'

    # Extract DataFrame with designer's active payment methods...
    payment_methods = query_read_only_prod(query)

    # Remove whitespaces...
    payment_methods = strip_df(payment_methods)

    # Divide duplicates and unique values into dictionaries to ease validation...
    duplicate_payment_methods = payment_methods[payment_methods.duplicated(subset=['code', 'payment_name'], keep=False)]
    duplicate_payment_dict = dict(zip(duplicate_payment_methods['payment_name'].astype(str),
                                      duplicate_payment_methods['code'].astype(str)))

    unique_payment_methods = payment_methods.drop_duplicates(subset=['code', 'payment_name'])
    unique_payment_dict = dict(zip(unique_payment_methods['payment_name'].astype(str),
                                   unique_payment_methods['code'].astype(str)))

    # Return dataframe with data from call to prod by running query...
    return duplicate_payment_dict, unique_payment_dict


def query_shipping_methods(designer_id: int):
    """ Take designer id and call prod to make a query that retrieves active shipping methods
    for the specific designer id.

   Returns:
       panda DataFrame with desired columns.

   """

    query = f"select dsm.code, sm.shipping_name from joor_web.designer_shipping_methods dsm " \
            f"join joor_web.shipping_methods sm on sm.id = dsm.shipping_method_id where " \
            f"dsm.designer_id = {designer_id} and dpm.deleted = 0;"

    # Extract DataFrame with designer's active payment methods...
    shipping_methods = query_read_only_prod(query)

    # Remove whitespaces...
    shipping_methods = strip_df(shipping_methods)

    # Divide duplicates and unique values into dictionaries to ease validation...
    duplicate_shipping_methods = shipping_methods[shipping_methods.duplicated(subset=['code', 'shipping_name'], keep=False)]
    duplicate_shipping_dict = dict(zip(duplicate_shipping_methods['shipping_name'].astype(str),
                                       duplicate_shipping_methods['code'].astype(str)))

    unique_shipping_methods = shipping_methods.drop_duplicates(subset=['code', 'shipping_name'])
    unique_shipping_dict = dict(zip(unique_shipping_methods['shipping_name'].astype(str),
                                    unique_shipping_methods['code'].astype(str)))

    # Return dataframe with data from call to prod by running query...
    return duplicate_shipping_dict, unique_shipping_dict
