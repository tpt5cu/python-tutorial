- https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data
# Attributes
- files: a MultiDict that contains all of the uploaded files. Since multiple form values can have the same form name (i.e. key), the "getlist(\<key>)"
  method is the ONLY way to get ALL of the values that correspond to the \<key>, as opposed to just the first value