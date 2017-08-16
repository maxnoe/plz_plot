from plz_plot.core import plot_plz_data
from plz_plot.io import get_plz_dataframe
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from cartopy import feature

from cartopy import crs

df = get_plz_dataframe()

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(1, 1, 1, projection=crs.Mercator())

ax.set_extent([4, 16, 47, 56], crs.PlateCarree())

land = feature.NaturalEarthFeature(
    'physical', 'land', '10m',
    facecolor=feature.COLORS['land'],
)
countries = feature.NaturalEarthFeature(
    'cultural', 'admin0_countries', '10m',
    facecolor='none',
    edgecolor='k',
)

ax.add_feature(land)
ax.add_feature(countries)


df['inhabitants_per_area'] = df['inhabitants'] / df['area']

plot = plot_plz_data(
    df['inhabitants_per_area'],
    ax=ax,
    norm=LogNorm(),
    vmin=1e1,
    vmax=10e4,
)
plot.set_edgecolor('lightgray')
plot.set_linewidth(0.2)

ax.set_title('Inhabitants per Square Kilometer')

fig.colorbar(plot, ax=ax)
fig.tight_layout()
fig.savefig('example.png', dpi=300)
