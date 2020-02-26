from matplotlib import pyplot as plt


# plot (*args, scalex=True, scaley=True, data=None, **kwargs)
def basic_line_graph():
    x = [1, 2, 3]
    y = [.5, 1, 1.5]
    plt.plot(x, y)
    plt.show()


if __name__ == '__main__':
    basic_line_graph()