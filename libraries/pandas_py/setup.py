# https://stackoverflow.com/questions/714063/importing-modules-from-parent-folder/50194143#50194143


'''
If there were one top-level package in this directory, that would be the main package. Since there are several packages in this top-level directory,
each of them is a main package
'''


from setuptools import setup, find_packages
setup(name='myproject', version='1.0', packages=find_packages())