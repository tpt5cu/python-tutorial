"""
https://scikit-learn.org/stable/modules/preprocessing.html#standardization-or-mean-removal-and-variance-scaling
"""


import numpy as np
from sklearn import preprocessing


"""
scale() ALWAYS returns a numpy.ndarray. Therefore, if I feed it a pandas DataFrame I need to convert the ndarray back into a DataFrame
"""


def scale_by_feature():
    """
    When axis=0 (default) for sklearn.preprocessing.scale(), the standardization is done on a per-feature basis. For example, 50, 27, 1000, and 1 are
    standardized together as a feature. This is NOT what I want for a time series.
    """
    # 4 pieces of training data, each with 3 features
    data = [
        [50, 1, 6],
        [27, 45, 0],
        [1000, 19, 0.5],
        [1, 356.6, 8]
    ]
    # axis=0 (default) will independently standardize EACH feature, NOT each vector
    s_data = preprocessing.scale(data)
    print(data)
    print(s_data)


def scale_by_vector():
    """
    When axis=1, each vector will be standardized across its own values. For example, 1000, 19, and 0.5 will be standardized together, regardless of
    the values in the other vectors.
    """
    # 4 pieces of training data, each with 3 features
    data = [
        [50, 1, 6],
        [27, 45, 0],
        [1000, 19, 0.5],
        [1, 356.6, 8]
    ]
    # axis=1 will standardized within each vector
    s_data = preprocessing.scale(data, axis=1)
    print(data)
    print(s_data)


def scale_high_spread_series():
    """
    If I were to standardize a time series like this, the standard score of the outlier is about 5. This is an example of how standardizing each
    individual time series does NOT guarantee that all the standard score time series will collectively have a range that is close to [-1, 1].
    Increasing the value of the outlier does not change its standard deviation very much at all. However, adding more data points that are distinct
    from the outlier markedly increases the standard score of the outlier. Thus, across 2880 observations for a time series, I could see how a single
    outlier have a standard score of 30 (which is crazy high).
    """
    data = [1, 356.6, 8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    s_data = preprocessing.scale(data, axis=0)
    print(s_data)
    #[-0.20008944  5.09803183 -0.09579572 -0.20008944 -0.20008944 -0.20008944
    #-0.20008944 -0.20008944 -0.20008944 -0.20008944 -0.20008944 -0.20008944
    #-0.20008944 -0.20008944 -0.20008944 -0.20008944 -0.20008944 -0.20008944
    #-0.20008944 -0.20008944 -0.20008944 -0.20008944 -0.20008944 -0.20008944
    #-0.20008944 -0.20008944 -0.20008944]



if __name__ == "__main__":
    #scale_by_feature()
    #scale_by_vector()
    scale_high_spread_series()