'''
Add a transformer block and perform the following:
    Remove rows where the passenger count is equal to 0 or the trip distance is equal to zero.
    Create a new column lpep_pickup_date by converting lpep_pickup_datetime to a date.
    Rename columns in Camel Case to Snake Case, e.g. VendorID to vendor_id.
    Add three assertions:
        vendor_id is one of the existing values in the column (currently)
        passenger_count is greater than 0
        trip_distance is greater than 0
'''

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    print(f'Preprosessing: rows with zero passengers:{data["passenger_count"].isin([0]).sum()}')
    print(f'Preprosessing: rows with zero trip_distance:{data["trip_distance"].isin([0]).sum()}')
    data = data[(data["passenger_count"] > 0) & (data["trip_distance"] > 0)]
    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date
    columns_list = list(data.columns)
    c = 0
    for n, column_name in enumerate(columns_list):
        if column_name.endswith('ID'):
            columns_list[n] = column_name.replace('ID', '_id')
            c += 1
    print(f'Whera replased {c} columns namen')
    data.columns = columns_list
    data.columns = data.columns.str.lower()


    print(data['vendor_id'].unique())

    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
    assert None not in output['vendor_id'].unique(), 'The unexisting values in the column'
    assert output["passenger_count"].isin([0]).sum() == 0, 'There are rides with zero passengers'
    assert output["trip_distance"].isin([0]).sum() == 0, 'There are rides with zero trip distance'

