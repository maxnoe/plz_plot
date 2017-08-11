import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable
from cartopy import crs
import numpy as np

from .io import load_plz_records


def plot_plz_data(
        data,
        cmap=None,
        vmin=None,
        vmax=None,
        ax=None,
        projection=None,
        norm=None
        ):

    recs = load_plz_records()

    if ax is None:
        ax = plt.axes(projection=projection or crs.Mercator())
        ax.set_extent([4, 16, 47, 56], crs.PlateCarree())

    norm = norm or Normalize()
    norm.vmin = vmin or data.min()
    norm.vmax = vmax or data.max()
    cmap = plt.get_cmap(cmap)

    mappable = ScalarMappable(cmap=cmap, norm=norm)
    mappable.set_array(data.values)

    for rec in recs:

        try:
            val = data.loc[rec.attributes['plz']]
        except KeyError:
            val = np.nan

        ax.add_geometries(
            rec.geometry,
            crs=crs.Mercator(),
            linewidth=0,
            color=cmap(norm(val)),
        )

    return mappable
