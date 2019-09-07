# https://packaging.python.org/guides/installing-using-linux-tools/#installing-pip-setuptools-wheel-with-linux-package-managers
# https://unix.stackexchange.com/questions/354928/bash-sudo-command-not-found

# in2lytics is running Linux debian 9.5, Python 3.6.6, everything in requirements.txt
# It has git, apt-get, Python
# I'm never going to use this Dockerfile on their system. I'm simply trying to recreate a similar environment to install with Jupyter

# in2lytics does a custom install of Python 3.6.6

# - Installing pip for debian via the "python-pip" package DOES install Python 2. Don't install the "python2.7" 
# - Python is executable as "python" or "python2.7". pip is executable as or "/usr/bin/pip2" (I think /usr/bin/pip is broken but I'm not sure)
# - Installing Python 3 according to the official pip instructions makes Python 3 executable as "python3" and pip 3 executable as "pip3"
# - Debian does not come with sudo, wget, but in2lytics has them

# in2lytics missing components
# - "en_US.UTF-8 UTF-8" locale

# Aliases:
# alias pip='sudo /usr/bin/pip2'
# alias python='sudo /usr/bin/python2'

# Linking:
# sudo mv /usr/local/bin/python /usr/local/bin/python.bkp
# sudo mv /usr/local/bin/pip /usr/local/bin/pip.bkp
# sudo ln -s /usr/bin/python /usr/local/bin/python
# sudo ln -s /usr/bin/pip2 /usr/local/bin/pip
#
# Restore
# sudo mv /usr/local/bin/python.bkp /usr/local/bin/python
# sudo mv /usr/local/bin/pip.bkp /usr/local/bin/pip

FROM debian:stable
# None of these come with the default stable Debian Docker build
RUN apt-get -y update && apt-get install -y git python-pip wget sudo locales
RUN sed -i 's/^# *\(en_US.UTF-8\)/\1/' /etc/locale.gen && locale-gen
WORKDIR /home
RUN git clone https://github.com/dpinney/omf.git
WORKDIR /home/omf
# Do I need to do this with sudo on the in2lytics container? (yes)
RUN python install.py
#WORKDIR /home/omf/omf/scratch/GRIP
#ENTRYPOINT ["python"]
#CMD ["-m", "grip"]
# docker run -p 5100:5100 <image name>
# Installation up to this point was successful as show by successful run of grip.py
# Install Python 3 because I need to. This installation isn't consistent with the in2lytics installation
WORKDIR /home
COPY requirements.txt .
RUN apt-get -y install python3-venv python3-pip
RUN pip3 install -r requirements.txt
## Install Python 2 kernel on Python 3 running Jupyter
RUN python2 -m pip install ipykernel && python2 -m ipykernel install --user
ENTRYPOINT ["jupyter"]
CMD ["notebook", "--ip=0.0.0.0", "--port=8888", "--allow-root"]
# docker run -p 8888:8888 <image name>