from plz_plot.core import plot_plz_data
from plz_plot.io import get_plz_dataframe
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

from cartopy import crs

df = get_plz_dataframe()

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(1, 1, 1, projection=crs.Mercator())


df['inhabitants_per_area'] = df['inhabitants'] / df['area']
df = df.query('inhabitants > 0 and area > 0')

plot = plot_plz_data(
    df['inhabitants_per_area'],
    ax=ax,
    norm=LogNorm(),
)

ax.set_extent([4, 16, 47, 56], crs.PlateCarree())

ax.set_title('Inhabitants per Square Kilometer')

fig.colorbar(plot, ax=ax)
fig.tight_layout()
fig.savefig('example.png', dpi=300)
