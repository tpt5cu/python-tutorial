import inspect

# These imports work fine. I don't understand why.
#from email.mime.multipart import MIMEMultipart
#from email.mime.application import MIMEApplication
#from email.mime.image import MIMEImage

# These imports do not work because ... I don't understand what email/__init__.py is doing
#from email.mime import MIMEMultipart # ImportError: cannot import name "MIMEMultipart"
#from email.mime import MIMEApplication # cannot import name "MIMEApplication"
#from email.mime import MIMEImage # cannot import name "MIMEImage"

# These imports work fine
# How does the import statement work with a LazyImporter object? I assume that this statement alone just imports the Multipart attribute into this
# module's namespace. The Multipart attribute just happens to be a LazyImporter object. This is complex...
from email.mime import Multipart 
from email.mime import MIMEApplication
from email.mime import MIMEImage

# This import works fine
import email

"""
Come back to this. It's complicated. 4/26/19
"""

def inspect_py():
    # This shows me that there is indeed an email.mime module
    for x in inspect.getmembers(email):
        print(x)
    # I don't see a "multipart" module inside of the email.mime module. What I do see is Multipart "LazyImporter" object. This is a custom class in
    # the email package.
    for x in inspect.getmembers(email.mime):
        print(x)

def use_email_bad():
    """
    These don't work because I'm accessing the "multipart" attribute fromt the email.mime module, but the module does not have a "multipart"
    attribute. Instead of a "multipart" attribute, the email.mime module has a "Multipart" attribute. The "Multipart" attribute is an instance of the
    LazyImporter class. The LazyImporter object has a __name__ of email.mime.multipart. 
    """
    mm = email.mime.multipart.MIMEMultipart() # module object has no attribute "multipart"
    #ma = email.mime.application.MIMEApplication("stuff")
    #mi = email.mime.image.MIMEImage

def use_email():
    mm = MIMEMultipart()
    ma = MIMEApplication("stuff")
    mi = MIMEImage

if __name__ == "__main__":
    #inspect_py()
    #use_email_bad()
    use_email()