'''
- An Axes object is an _AxesBase object. The _AxesBase class defines the __init__() method and fundamental methods while the Axes class defines fancy
  plotting methods
- Artist <- _AxesBase <- Axes <- Subplot
  - A Figure can have multiple axes. It seems that each axes is associated with a single Subplot. The Subplot methods that I've looked at return Axes
    objects anyway. Therefore, I'm just going to assume that a Subplot is an Axes.
    - According to the Artist tutorial, a Subplot is "a special case of an Axes that lives on a regular rows by columns grid of Subplot instances"
    - According to the Artist tutorial "Subplot is just a subclass of Axes"
'''