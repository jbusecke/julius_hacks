import pandas as pd


def convert_monthssince_datetime(da, pos='center'):
    da = da.copy()
    startdate = da.attrs['units'].replace('months since ', '')
    startdate = pd.to_datetime(startdate)
    timedelt = pd.to_timedelta(da.data, unit='M')
    da.data = startdate + timedelt
    del da.attrs['units']
    # This produces irregular dates (sometimes its 15th other times 14th
    # ...need to fix that in the future)
    return da
