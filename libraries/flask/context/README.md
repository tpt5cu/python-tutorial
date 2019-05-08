http://flask.pocoo.org/docs/1.0/appcontext/

https://stackoverflow.com/questions/15083967/when-should-flask-g-be-used

http://flask.pocoo.org/docs/1.0/reqcontext/ - technical explanation
http://flask.pocoo.org/docs/1.0/api/#flask.Request - useful documentation

# Why are contexts useful?

- A context only exists for the lifetime of a client's request to the Flask web server. Each request has its own unique contexts that disappear when
  the request ends.
- Sometimes, different functions need to share the same data during a request. Flask could have made this shared data available to each endpoint
  function by making each endpoint function take extra arguments, like "request" and "app_context", but instead Flask has global variables that make
  this shared data available.

# Application context

- The application context stores application-level data that is independent of any request.
- When a request comes in to the Flask web server, a request context is always pushed. An application context is always pushed along with that request
  context
- It might be more accurate to call this the "Request context that concerns application-level data"
    - With that name, it makes more sense to group "g" inside of this context.

## current_app

- Available as "from flask import current_app"
- current_app is a proxy for the app that is returned from Flask(__name__)
- current_app is app == False, but current_app._get_current_object() is app == True
- This object is useful when I can't import the object returned from Flask(__name__), or when I don't want to import it.

## g

- Available as "from flask import g"
- g is NOT the same as current_app at all
    - It does not have any configuration data about the app
- g is useful because it is a global namespace where I can store data that needs to be shared across functions during the lifetime of a request.
    - I could just use a global variable instead, but that would break in a threaded environment. Different threads would be accessing the same global
      data and the global data would get messed up.
- I suppose I could store data on the request object instead of g, but the request object does not support item assignment. There is probably a design
  reason for this, but I don't know what it is.
- Maybe g was moved to the application context simply to make it more accessible. After all, the request context is popped before the application context.

# Request context

- The request context is available as "from flask import request".
- The request context has useful information like files, form, method, headers, cookies, etc.
- It makes sense to store this type of information in a global request object that every endpoint function can access as needed.