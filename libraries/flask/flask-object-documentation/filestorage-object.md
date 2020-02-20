- https://werkzeug.palletsprojects.com/en/0.16.x/datastructures/#werkzeug.datastructures.FileStorage

# Attributes
- name: the form key name that was used to submit the file
- filename: the original filename on the client
- stream: a read()-able stream that contains the real contents of the file
    - Once it is read(), it returns b'' for future read()s because the stream has been consumed
    - It is possible to do \<FileStorage>.read() directly
## Unreliable attributes
- Don't use these attributes for validation or something serious: content_type, content_length