import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
from cartopy import crs
import numpy as np
from shapely.geometry import MultiLineString

from .io import load_plz_records


def build_patch_collection(recs):
    patches = []
    repeat = np.zeros(len(recs), dtype=int)
    for i, rec in enumerate(recs):
        if rec.geometry.geom_type == 'Polygon':
            iterable_geo = [rec.geometry]
        else:
            iterable_geo = rec.geometry

        for geom in iterable_geo:
            repeat[i] += 1

            if isinstance(geom.boundary, MultiLineString):
                xy = np.array(geom.boundary[0].xy).T
            else:
                xy = np.array(geom.boundary.xy).T

            patches.append(Polygon(xy, closed=True))

    return PatchCollection(patches, transform=crs.Mercator.GOOGLE, zorder=2), repeat


def plot_plz_data(
    data,
    cmap=None,
    vmin=None,
    vmax=None,
    ax=None,
    projection=None,
    norm=None
):
    data = np.asanyarray(data)

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
