# https://stackoverflow.com/questions/21053380/what-does-del-do-exactly


'''del is not part of the descriptor protocol, but given that non-data descriptors can't be deleted, I put these notes here'''


'''
All del does is remove the binding between a variable and a value. Once the binding is gone, Python will eventually garbage collect the value
'''