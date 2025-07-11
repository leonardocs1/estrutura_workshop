from typing import List

import pandas as pd

"""
função para transformar um lista de dataframes em
um único dataframe
"""


def concat_data_frames(data_frame_list: List[pd.DataFrame]) -> pd.DataFrame:
    return pd.concat(data_frame_list, ignore_index=True)
