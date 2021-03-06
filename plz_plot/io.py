from cartopy.io.shapereader import Reader
from pkg_resources import resource_filename
import pandas as pd

PATH = resource_filename('plz_plot', 'resources/plz-5stellig')


def load_plz_records(path=PATH):

    reader = Reader(path)
    recs = list(reader.records())

    return recs


def get_plz_dataframe(path=PATH):
    recs = load_plz_records(path)
    df = pd.DataFrame([r.attributes for r in recs]).set_index('plz')

    df.rename(
        columns={'qkm': 'area', 'einwohner': 'inhabitants'},
        inplace=True,
    )
    df['names'] = (
        df['note']
        .str.rstrip('\x00')
        .str.split(' ')
        .apply(lambda l: ' '.join(l[1:]))
    )
    df.drop('note', axis=1, inplace=True)

    return df


def get_plz_geometries(path=PATH):
    recs = load_plz_records(path)
    return [r.geometry for r in recs]
