from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

""" 
A blueprint is not a standalone Flask application. A blueprint is a set of operations that can be registered on an application. Blueprints are used to
simply my code by grouping related views and functionality into modular parts. One use for blueprints is to prefix all the URL routes in the blueprint
with some string.

There is a lot more to Blueprints than just this route-prefixing functionality.
"""

# The first 2 parameters to a Blueprint instance are required. If the Blueprint will use templates, then I must specify a template_folder.
# I don't have to do this with Flask() because Flask() has a default value of "templates" for its template_folder parameter 
# The value of the first parameter "name" is not prefixed in front of URLs by default. It is just useful to identify which function goes with which
# rule if I inspect app.url_map
simple_page = Blueprint('simple_page', __name__, template_folder='templates', url_prefix="/yoyo")

"""
"defaults" is a regular old route parameter that merely specifies default value(s) for arguments of a view function.
If the user accesses "/", they will see "/" in their web browser, but Flask will treat it as if they had accessed "/index".
If a user accesses "/index", they will be redirected with a 301 to "/", and Flask will treat the request as "/index" (same as the above)
"""

@simple_page.route('/', defaults={'page': 'index'})
@simple_page.route('/<page>')
def show(page):
    try:
        return render_template('%s.html' % page) # this is just format string substitution
    except TemplateNotFound:
        abort(404)

