- https://flask-login.readthedocs.io/en/latest/
- https://stackoverflow.com/questions/12179593/flask-post-error-405-method-not-allowed
- https://machinesaredigging.com/2013/10/29/how-does-a-web-session-work/ - server-side sessions overview
- http://www.rodsonluo.com/client-session-vs-server-session - sever vs. client-based sessions
- https://phillbarber.blogspot.com/2014/02/client-side-vs-server-side-session.html - more detailed server vs. client-based session comparison

# @flask_login.login_required
- This decorator will ensure that the current user is 1) logged-in and 2) authenticated before calling the actual view. If they are not, it calls the
  LoginManager.unauthorized callback

# LoginManager.unauthorized 
- If 1) we don't register a callback with LoginManager.unauthorized_handler(), then the following will happen when this function is called
 - See docs

# Cause of 405 in omf
- It's got nothing to do with Flask-Login. It's because I'm submitting a GET request to a POST-only route. And that's because I'm using "showFileMenu"
  LMAO

# User and User.cu()
- Flask Login creates "User" objects based on a class that I implement
    - Every User object has 4 methods that can be used to examine the state of the User object
- The User object is reloaded upon each request by getting the user ID from the Flask session object
- We call User.cu() a lot, which really returns `flask_login.current_user.username`

## Sessions in Flask background
- Flask has an object called "session" that allows me to store arbitrary information about every specific user. The information on this "session"
  object is unique to each user and lasts across multiple requests. Each session object is associated with a specific user by by storing a
  cryptographically signed cookie on the user. "Cryptographically signed" means the user can examine the contents of the cookie, but cannot modify
  it unless they know the secret key that was used to create it in the first place.