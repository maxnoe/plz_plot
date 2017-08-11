import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
from cartopy import crs
import numpy as np

from .io import load_plz_records


def build_patch_collection(recs):
    patches = []
    repeat = np.zeros(len(recs), dtype=int)
    for i, rec in enumerate(recs):
        for geom in rec.geometry:
            repeat[i] += 1
            try:
                patches.append(Polygon(np.array(geom.boundary.xy).T, closed=True))
            except NotImplementedError as e:
                patches.append(Polygon(np.array(geom.boundary[0].xy).T, closed=True))

    return PatchCollection(patches, transform=crs.Mercator()), repeat


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
    col, repeat = build_patch_collection(recs)
    data = np.repeat(data, repeat)

    if ax is None:
        ax = plt.axes(projection=projection or crs.Mercator())
        ax.set_extent([4, 16, 47, 56], crs.PlateCarree())

    col.set_array(data)
    col.set_cmap(cmap)
    col.set_norm(norm)
    col.set_clim(vmin, vmax)

    ax.add_collection(col)

    return col
