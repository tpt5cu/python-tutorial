# https://stackoverflow.com/questions/40180737/how-to-get-data-from-pickle-files-into-a-pandas-dataframe


import pandas as pd
import os 


def pickle_to_dataframe():
    """
    This operation seems quite slow for some reason. pandas will return whatever object was originally serialized into the pickle file. If that object
    happens to be a DataFrame (which I hope it is), then I'll get a DataFrame! The nice thing is that pandas will figure out the compression algorithm
    and decompress the file for me.
    """
    data = pd.read_pickle(os.path.join(os.path.dirname(__file__), "delicious-pickle.pkl.gz"))
    print(data)


if __name__ == "__main__":
    pickle_to_dataframe()
