http://flask.pocoo.org/docs/1.0/quickstart/
https://codingdose.info/2018/05/12/change-flask-root-folder/
http://flask.pocoo.org/docs/1.0/api/#flask.Request
http://flask.pocoo.org/docs/1.0/api/#response-objects
http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response

https://stackoverflow.com/questions/13598363/how-to-dynamically-select-template-directory-to-be-used-in-flask
http://jinja.pocoo.org/docs/2.10/api/

# Run the application

- $ export FLASK_APP=< my application file >
- $ flask run

# Static files

- Flask serves static files relative to the "static" directory by default.
- All paths to static files are relative to the "static" directory (e.g. "static/mycss.css")
- Everything in the static folder is publically accessable via "/static/< filename >" by default.

# Templates

- Flask searches for HTML templates inside of the "templates" folder at the base of the Flask application by default

# Configure templates, static files, etc.

- Simple configuration can be done via the Flask() constructor which allows me to specify a custom templates folder and a custom static folder
- I can do more complex folder configuration by using the jinja.ChoiceLoader()

# Sessions and cookies

- These should be a completely separate tutorial