- https://flask-login.readthedocs.io/en/latest/
- https://stackoverflow.com/questions/12179593/flask-post-error-405-method-not-allowed

# @flask_login.login_required
- This decorator will ensure that the current user is 1) logged-in and 2) authenticated before calling the actual view. If they are not, it calls the
  LoginManager.unauthorized callback

# LoginManager.unauthorized 
- If 1) we don't register a callback with LoginManager.unauthorized_handler(), then the following will happen when this function is called
 - See docs

# Cause of 405 in omf
- It's got nothing to do with Flask-Login. It's because I'm submitting a GET request to a POST-only route. And that's because I'm using "showFileMenu"
  LMAO