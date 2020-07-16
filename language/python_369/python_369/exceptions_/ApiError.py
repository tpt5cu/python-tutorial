class ApiError(Exception):

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload
        print(self.message)
        raise Exception(self.message + ' ' + str(self.status_code))

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        print(rv['message'])
        return rv