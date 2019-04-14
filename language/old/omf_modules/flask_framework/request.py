# http://flask.pocoo.org/docs/1.0/api/

"""The request object has many attributes (see class flask.Request in doc):

request.form: This returns an ImmutableMultiDict of the parameters of a submitted form, which is just an immutable
version of the MultiDict. A MultiDict is like a regular Python dictionary, except that a key can have multiple values.
Just using request.form.get(<some key>) or request.form[<some key>] will only return the FIRST value assigned to that
key. The other values can be accessed with request.form.getlist(<some key>) which returns a list of all values assigned
to that key.

request.referrer: The url where the request came from. This header is useful for convenience, but it can be
spoofed so it should never be used for security or critical functionality.
"""