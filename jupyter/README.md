- https://realpython.com/jupyter-notebook-introduction/
- https://jupyter-notebook.readthedocs.io/en/stable/security.html
- https://github.com/jupyterhub/jupyterhub/issues/1195
- https://www.codecademy.com/articles/how-to-use-ipython - IPython introduction

# What is Jupyter Notebook?
- Jupyter Notebook is an open-source web application that creates "Notebooks" which can contain code, equations, visualizations, and text. It can run
  with over 100 different kernals, so I wouldn't call it a runtime
- Jupyter itself runs as a web server which can be used through a web browser

## Running Jupyter Notebook
- cd to the desired directory (where the Jupyter files will be created), then $ jupyter notebook
- Jupyter can create folders, Notebooks, text files, terminals
- Nothing will immediately appear in the chosen directory, but content will appear as I work

### Control panel
- This is a JupyterHub feature? I'm guessing it is...

### Notebooks
- Click run or press shift + enter to execute the code in a cell
- Variables and imports are SHARED across different shells
    - However, the earlier cells must be run first! For example, to use an imported namespace in a later cell, I have to import the namespace in an
      earlier cell and run the earlier cell
    - Once an earlier cell has been run, it's state persists across all subsequent cells even if it is deleted
    - The only way to get rid of a cell's effects is to restart the kernel

#### Rich content
- There are 4 types of cells: code, markdown, raw nbconvert, and heading
    - I will primarily use code and markdown cells
- nbconvert is a tool to convert a Notebook into HTML, PDF, LaTeX, Markdown, etc.
    - $ jupyter nbconvert \<filename> --to pdf
        - Convert a Notebook to PDF
    - MAKE SURE I'M RUNNING THE COMMAND INSIDE THE VIRTUALENV
    - Alternatively, I can use the menu inside of the web interface to download a Notebook in whatever format I want
    - Need to install Pandoc later...

### Extensions
- There are four types of extensions: kernel, IPython kernel, Notebook, and Notebook Server
- A Notebook extension is a JavaScript module that can use Jupyter's own JavaScript API and the regular DOM API
    - Google "Jupyter Notebook extensions" for this particular kind of extension
        - There's neat stuff like a Python 2 to 3 converter and a highlighter

### Terminals
- The terminal that runs in the web browser is a full-featured terminal with no restrictions by default
    - Reading the documents shows that indeed, any and all code can be executed in a Jupyter Notebook and terminal!
- Restrictions must be applied at the process and container level, not in the Juypter Notebook
    - rbash: restricted shell
        - $ bash -r
        - There are many ways to get around this, but it's a nice idea
            - It's trivial to $ cp /bin/bash . $. Now I can run a real bash terminal inside of the restricted bash terminal! 
            - I can just do $ bash $ to start a regular bash shell inside of the restricted shell

## UI information
- The "In [< number >]" displays the order in which the cells were run

## What is JupyterLab?
- It's an advanced version of Jupyter Notebook that is basically an IDE

# What is IPython?
- IPython is an alternative Python interpreter than provides more features than the standard interactive Python interpreter. It is used as the
  underlying software for Jupyter Notebooks
    - It's a seriously beefed-up terminal
- Jupyter Notebook is a language agnostic generalization of IPython. It also has some nice cosmetic differences. However, by and large IPython and
  Jupyter Notebook are almost the same thing

## Run IPython
- Install with $ pip install ipython
- Make sure the package is installed, then $ ipython
- Understand what features are available with %quickref (a magic command) 

# What is JupyterHub?
- Each user gets their own unique instance of a Jupyter Notebook server