import pandas as pd
from pathlib import Path


def get_trips(year, selected_columns=None):
    if year == 2015:
        folder_path = Path('../data/input/mtmc/2015/')
        with open(folder_path / 'wege.csv', 'r') as trips_file:
            df_trips = pd.read_csv(trips_file,
                                   dtype={'HHNR': int},
                                   delimiter=',',
                                   usecols=selected_columns,
                                   na_values=[-99])
    else:
        raise Exception('Year not well defined')
    return df_trips


def get_zp(year, selected_columns=None):
    if year == 2015:
        folder_path = Path('../data/input/mtmc/2015/')
        with open(folder_path / 'zielpersonen.csv', 'r', encoding='latin1') as zielpersonen_file:
            if selected_columns is None:
                df_zp = pd.read_csv(zielpersonen_file)
            else:
                df_zp = pd.read_csv(zielpersonen_file,
                                    dtype={'HHNR': int},
                                    usecols=selected_columns)
    else:
        raise Exception('Year not well defined')
    return df_zp


def get_hh(year, selected_columns=None):
    if year == 2015:
        folder_path_2015 = Path('../data/input/mtmc/2015/')
        with open(folder_path_2015 / 'haushalte.csv', 'r', encoding='latin1') as haushalte_file:
            df_hh = pd.read_csv(haushalte_file,
                                dtype={'HHNR': int},
                                usecols=selected_columns)
    return df_hh


def get_hhp(year, selected_columns=None):
    if year == 2015:
        folder_path_2015 = Path('../data/input/mtmc/2015/')
        with open(folder_path_2015 / 'haushaltspersonen.csv', 'r') as haushaltspersonen_file:
            df_hhp = pd.read_csv(haushaltspersonen_file,
                                 delimiter=',',
                                 usecols=selected_columns,
                                 na_values=[-99])
    else:
        raise Exception('Year not well defined')
    return df_hhp
