- http://flask.pocoo.org/docs/1.0/patterns/fileuploads/#uploading-files
- https://stackoverflow.com/questions/6884991/how-to-delete-dir-created-by-python-tempfile-mkdtemp
- https://stackoverflow.com/questions/41543951/how-to-change-downloading-name-in-flask

# secure_filename()

- Always use this function to sanitize the user-input filename, which could literally be anything. 

# send_file() vs. send_from_directory()

- send_file() is not safe. It does not sanitize user filenames. If the file isn't found, the server throws an error.
- Always use send_from_directory() if I can. This function ensures the filename has no "../" to escape the directory, and it raises 404 if the file
  isn't found. 

# curl commands

- $ curl http://127.0.0.1:5000/unsafe -F "file-form-param=@/Users/austinchang/tutorials/python/libraries/flask/files/badfile.txt;filename=../../important.txt"
      - This command will overwrite important.txt which is outside of the root of the web server! A hacker could overwrite any file on my system! They
      could overwrite my bash_profile to execute whatever code they wanted whenever I start a terminal.
- $ curl http://127.0.0.1:5000/safe -F "file-form-param=@/Users/austinchang/tutorials/python/libraries/flask/files/badfile.txt;filename=../../important.txt"
      - This route protects against the filename exploit.
- $ curl http://127.0.0.1:5000/sendfile -F filename="../../multi-file-response/my.json"
      - This route allows the client to access any file on the server file system!
- $ curl http://127.0.0.1:5000/sendfromdirectory -F filename="../../multi-file-response/my.json"
      - This route is safe.