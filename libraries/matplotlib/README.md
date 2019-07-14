- https://matplotlib.org/3.1.0/tutorials/index.html#introductory - tutorials
- https://matplotlib.org/3.1.0/api/ - go to this page to get the REAL doc for a module instead of the pyplot hack for the module

# Datatype Terminology

- Artist: the superclasses of everything in a figure. A Figure, Axes, and Axis all extend the Artist type. When a figure is rendered, all the Artist
  objects are drawn to the Canvas
    - Artist objects are split into two catagories: primitives and containers
        - Primitives: Line2D, Rectangle, Text, AxesImage, etc.
        - Containers: Axis, Axes, Figure
- Figure: everything in the graph. Includes the x and y axes, the title, the legend, etc.
    - A figure can contain many different axes
- Axes: the region of the figure where the data is plotted. It must contain at least two (yes two, not one) Axis objects
    - An axes object can be assigned to 1 and only 1 figure
- Axis: number-line-looking objects
    - The location of the ticks on the Axis is controlled by a "Locator" object and the tickable strings are controlled by a "Formatter" object

# Data input to plotting functions

- All plotting functions expected either 1) a numpy.array or 2) a numpy.ma.masked_array as input
- Array-like objects such as Pandas objects and numpy.matrix may or may not work as intended

# Non-datatype terminology

- Subplot: a Figure can have multiple axes. It seems that each axes is associated with a single Subplot. The Subplot methods that I've looked at
  return Axes objects anyway. Therefore, I'm just going to assume that a Subplot is an Axes.
  - According to the Artist tutorial, a Subplot is "a special case of an Axes that lives on a regular rows by columns grid of Subplot instances"
  - According to the Artist tutorial "Subplot is just a subclass of Axes"