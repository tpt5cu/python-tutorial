"""
https://stackoverflow.com/questions/38466523/python-how-to-handle-the-valueerror-unsupported-pickle-protocol-4-error
https://stackoverflow.com/questions/29587179/load-pickle-filecomes-from-python3-in-python2
"""

"""
Higher versions of the pickle protocol require higher versions of Python to open. pickle protocol 4 was added in Python 3.4. Solutions to this error
are:
    1) Use an up-to-date version of Python
    2) Create the pickle with a lower protocol by specifying the protocol in the pickle.dump() function when the pickle is created.
        - If I didn't create the pickle, then I have no choice but to use a higher version of Python.
        - I could also open the Python 3 pickle in binary mode, then write the bytes with a Python 2 pickle. Is that even useful? Don't think so.
"""