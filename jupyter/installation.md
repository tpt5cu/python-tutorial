- https://jakevdp.github.io/blog/2017/12/05/installing-python-packages-from-jupyter/ - Jupyter with pip
- https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-pip
- https://ipython.readthedocs.io/en/latest/install/kernel_install.html - installation instructions

# Installing with pip in a Jupyter Notebook
- `pip install jupyter`

## What is a Jupyter kernel?
- A Jupyter kernel is a set of files that point Jupyter to some means of executing code within a notebook
    - For Python kernels, this will point to a particular installation of Python
- Run $ jupyter kernelspec list $ to display the list of available kernels
    - Each kernel in this list is a directory that contains a kernel.json file
        - This file specifies the executable the kernel itself should use

## Jupyter's kernels are disconnected from Jupyter's shell
- Sometimes, the installation of Python that was used to launch the Jupyter server is completely different from the Python kernel that is exposed to
  the user
    - Thus, just running $ pip install \<package> $ in a Jupyter terminal will install the package to the Jupyter-shell-Python site-packages
      directory. The installed package won't be available in any Jupyter Notebooks

## Solutions
- Use the %pip IPython magic command to run the pip installer within the current Python kernel
    - Unfortunately, the OMF can't be installed with pip

# Using Python 2 and Python 3 kernels

## Running Jupyter with Python 3 and adding Python 2
- Python 2 must be installed on the machine
- The Python 2 pip version must be 9.0 or higher
    - $ `python2 -m pip --version`
- Install ipykernel on Python 2's pip
    - $ `python2 -m pip install ipykernel`
        - It works with tornado 3.2
        - Might need to run it with sudo
- Run ipykernel
    - $ `python2 -m ipykernel install --user`

## Running Jupyter with Python 2 and adding Python 3
- Haven't need to do this yet

## Version compatibility
- in2lytics runs Python 3.6.6, IPython 7.5.0, Jupyter 4.4.0
    - IPython 6 and higher only work with Python 3.3.0 and above