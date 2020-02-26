import matplotlib as mpl


def examine_default_rcparams_values():
    '''
    matplotlib defines an "rcParams" object in its __init__.py file. This handy object contains (all of?) the default values for matplotlib. This
    matters because often in the documentation I come across documentation like "default: :rc:`figure.figsize`". This documentation is referencing
    this dictionary
    - This object is configured from a matplotlibrc file
        - matplotlib searches a variety of locations for such a file. In this environment, the file is located at:
            - /Users/austinchang/.pyenv/versions/3.6.9/envs/venv3.6.9-matplotlib/lib/python3.6/site-packages/matplotlib/mpl-data/matplotlibrc
        - If the matplotlibrc file does not exist anywhere that matplotlib looked (or it was found, but it didn't set a required setting), a set of
          default fallback values are defined in:
            - /Users/austinchang/.pyenv/versions/3.6.9/envs/venv3.6.9-matplotlib/lib/python3.6/site-packages/matplotlib/rcsetup.py as "defaultParams"
    - See /Users/austinchang/.pyenv/versions/3.6.9/envs/venv3.6.9-matplotlib/lib/python3.6/site-packages/matplotlib/__init__.py for the gory details
    '''
    # By default, a figure is 6.4 inches wide and 4.8 inches tall
    print(mpl.rcParams['figure.figsize']) # [6.4, 4.8]


if __name__ == '__main__':
    examine_default_rcparams_values()