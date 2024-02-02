import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

# VendorID,lpep_pickup_datetime,lpep_dropoff_datetime,store_and_fwd_flag,RatecodeID,
# PULocationID,DOLocationID,passenger_count,trip_distance,fare_amount,extra,mta_tax,
# tip_amount,tolls_amount,ehail_fee,improvement_surcharge,total_amount,payment_type,
# trip_type,congestion_surcharge

@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    url = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/'

    list_of_month = [10, 11, 12]
    df = pd.DataFrame()

    taxi_dtypes = {
                    'VendorID': pd.Int64Dtype(),
                    'passenger_count': pd.Int64Dtype(),
                    'trip_distance': float,
                    'RatecodeID':pd.Int64Dtype(),
                    'store_and_fwd_flag':str,
                    'PULocationID':pd.Int64Dtype(),
                    'DOLocationID':pd.Int64Dtype(),
                    'payment_type': pd.Int64Dtype(),
                    'fare_amount': float,
                    'extra':float,
                    'mta_tax':float,
                    'tip_amount':float,
                    'tolls_amount':float,
                    'improvement_surcharge':float,
                    'total_amount':float,
                    'congestion_surcharge':float
                }
    parse_dates = ['lpep_pickup_datetime', 'lpep_dropoff_datetime']

    for month_nr in list_of_month:
        print(f'{url}/green_tripdata_2020-{month_nr}.csv.gz')
        df_mnth = pd.read_csv(f'{url}/green_tripdata_2020-{month_nr}.csv.gz',
                        sep=',',      
                        dtype=taxi_dtypes,
                        parse_dates=parse_dates)
        print(len(df_mnth))
        df = pd.concat([df, df_mnth], ignore_index=True)
    print()
    print('Total: ', len(df))
    return df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
