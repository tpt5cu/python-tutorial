import pathlib
from matplotlib import pyplot as plt


# savefig(fname, dpi=None, facecolor='w', edgecolor='w',
#   orientation='portrait', papertype=None, format=None,
#   transparent=False, bbox_inches=None, pad_inches=0.1,
#   frameon=None, metadata=None)
def save_image_to_file():
    plt.plot([1, 2, 3], [.5, 1, 1.5])
    path = pathlib.Path('~/Desktop/myimg.png').resolve()
    plt.savefig(str(path))


if __name__ == '__main__':
    save_image_to_file()
