from flask import Flask
from route_prefix import simple_page

"""
Flask is very flexible in how it allows me to register blueprints on an application.
1) Things like the url prefix can be set directly in the blueprint constructor
2) app.register_blueprint() will override anything set in the blueprint constructor

The same blueprint can be registered on an application more tha once.
However, if the blueprint is set up in certain ways, this won't work.
"""

app = Flask(__name__)

# Register the blueprint on the application without overriding any constructor-provided arguments
app.register_blueprint(simple_page)

# Register the blueprint and override constructor-provided arguments
#app.register_blueprint(simple_page, url_prefix="/wiggidy-wack")

# app.url_map returns the routing Map used by the application. It's useful to inspect URL routing rules. 
print(app.url_map)