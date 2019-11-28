- https://flask.palletsprojects.com/en/1.1.x/api/#response-objects
- https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response
- https://werkzeug.palletsprojects.com/en/0.16.x/wrappers/#werkzeug.wrappers.BaseResponse - The werkzeug BaseResponse documents most of the
  interesting attributes


# Flask response vs Werkzeug BaseResponse
- The Flask response implements the JSON mixin while the BaseResponse does not

# Constructor kwargs
- status: an integer for the http status code

# Attributes
- data: a descriptor that references the request body
- status: the full HTTP status text (with status code appended) e.g. "FOUND 302"
    - This is almost always redundant and can be ignored
- status_code: an integer with the HTTP status code
- headers: a Headers object