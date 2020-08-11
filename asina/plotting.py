import matplotlib.pyplot as plt
import cartopy.crs as ccrs

projection_dict = {
    'central_latitude': 90.0,
    'central_longitude': -45.0,
    'false_easting': 0.0,
    'false_northing': 0.0,
    'true_scale_latitude': 70,
    }
bounds = [-3850000.000, 3750000., -5350000., 5850000.000]

def asina_basemap():
    proj = ccrs.Stereographic(**projection_dict)
    fig = plt.figure(figsize=(7,7))
    ax = fig.add_subplot(projection=proj)
    #ax.set_extent([-180., 180., 50., 90], ccrs.PlateCarree())
    ax.set_extent(bounds, proj)
    ax.coastlines(color='0.7')
    ax.gridlines()
    return fig, ax


def asina_contourf(da, title=None):
    """generates a filled contour of data in da"""

    vmin = -8.
    vmax = 8.
    levels = 17
    
    fig, ax = asina_basemap()
    da.plot.contourf(ax=ax, vmin=vmin, vmax=vmax, levels=levels,
                     extend='both', transform=ccrs.PlateCarree(),
                     cmap='RdBu_r')
    da.plot.contour(ax=ax, vmin=-8., vmax=8, levels=17,
                    colors='0.3', linewidths=1,
                    transform=ccrs.PlateCarree())
    if title:
        ax.set_title(title)
    
    return fig, ax
