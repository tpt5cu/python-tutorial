from flask import Flask, make_response, send_file, send_from_directory
import os, zipfile

#import email
#from email.mime.multipart import MIMEMultipart
#from email.mime.application import MIMEApplication
#from email.mime.image import MIMEImage

app = Flask(__name__)

# Doesn't work as far as I can tell
@app.route("/getmultipart")
def multipart():
    #message = MIMEMultipart()
    #with open(os.path.join(os.path.dirname(__file__), "my.json")) as f:
    #    my_json = MIMEApplication(f.read(), "json")
    #with open(os.path.join(os.path.dirname(__file__), "my.png")) as f:
    #    my_png = MIMEImage(f.read())
    #message.attach(my_json)
    #message.attach(my_png)
    #response = make_response(message.as_string())
    msg = """HTTP/1.1 200 OK
--sample_boundary
Content-Type: text/css; charset=utf-8
Content-Location: http://localhost:2080/file.css

body
{
 background-color: yellow;
}
--sample_boundary
Content-Type: application/x-javascript; charset=utf-8
Content-Location: http://localhost:2080/file.js

alert("Hello from a javascript!!!");

--sample_boundary
Content-Type: text/html; charset=utf-8
Content-Base: http://localhost:2080/

<html>
<head>
    <link rel="stylesheet" href="http://localhost:2080/file.css">
</head>
<body>
 Hello from a html
    <script type="text/javascript" src="http://localhost:2080/file.js"></script>
</body>
</html>
--sample_boundary--"""
    response = make_response(msg)
    response.mimetype = "multipart/mixed"
    return response

@app.route("/zipfile")
def get_zip():
    """ The server throws an exception if the ZipFile tries to read nonexistent files """
    with zipfile.ZipFile(os.path.join(os.path.dirname(__file__), "my.zip"), 'w', zipfile.ZIP_DEFLATED) as z:
        z.write(os.path.join(os.path.dirname(__file__), "my.json"), "some.json")
        z.write(os.path.join(os.path.dirname(__file__), "my.png"), "some.png")
    return send_from_directory(os.path.dirname(__file__), "my.zip")
    