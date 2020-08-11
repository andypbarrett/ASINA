# An example of plotting 925 hPa air temperature for the ASINA page

import xarray as xr

from plotting import asina_contourf

import matplotlib.pyplot as plt

FILEPATH = '../data/NCEP.air_temperature.925hPa.july2020.anomaly.nc'

def main():

    ds = xr.open_dataset(FILEPATH)

    fig, ax = asina_contourf(ds.air.isel(time=0),
                             title='July 2020 Air Temperature\nDifference from Average')
    fig.savefig('example_air_temperature_anomaly.png')
    

if __name__ == "__main__":
    main()
