"""
https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html
"""

import numpy as np
from sklearn import preprocessing


def normalize_by_feature():
    """
    MinMaxScaler() transforms the data per-feature. In this data, there are 4 training examples, each with 3 dimensions. Each feature is a
    cross-cutting column. Feature 1 has max 1000, feature 2 has max = 356.6, feature 3 has max = 8
    """
    data = [
        [50, 1, 6],
        [27, 45, 0],
        [1000, 19, 0.5],
        [1, 356.6, 8]
    ]
    #[[0.04904905 0.         0.75      ]
    #[0.02602603 0.12373453 0.        ]
    #[1.         0.05061867 0.0625    ]
    #[0.         1.         1.        ]]
    # MinMaxScaler must be fit to the data before it can transform it. Do both at once with fit_transform()
    normalized_data = preprocessing.MinMaxScaler().fit_transform(data)
    print(normalized_data)


def normalize_by_vector():
    """
    Make sure to use two tranposes to normalize across each vector.
    - Proof: 0.01850925 = (19 - 0.5)/(1000 - 0.5)
    """
    data = [
        [50, 1, 6],
        [27, 45, 0],
        [1000, 19, 0.5],
        [1, 356.6, 8]
    ]
    #[[1.         0.         0.10204082]
    #[0.6        1.         0.        ]
    #[1.         0.01850925 0.        ]
    #[0.         1.         0.01968504]]
    ary = np.array(data)
    ary_t = ary.T
    normalized_data = preprocessing.MinMaxScaler().fit_transform(ary_t)
    normalized_data = normalized_data.T
    print(normalized_data)


if __name__ == "__main__":
    #normalize_by_feature()
    normalize_by_vector()


