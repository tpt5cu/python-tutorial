- https://werkzeug.palletsprojects.com/en/0.16.x/test/#werkzeug.test.EnvironBuilder
# Summary
- This class shows all of the arguments that can be passed to test_request_context
# Constructor parameters
- data: a dictionary of data to send with the request context
# Submitting files
## Submitting a real file
```
test_request_context(data=
{
    '<form name>': ('<real filepath>', ['<filename>'])
}
```
- \<real filepath> MUST be a real, preferably absolute, filepath. This file will be opened in 'rb', the that file object will be passed to a
  FileStorage initializer 
- /Users/austinchang/.pyenv/versions/3.6.9/envs/venv3.6.9/lib/python3.6/site-packages/werkzeug/datastructures.py
- \<filename> is optional. It is not used to read a real file. If it is provided, it will be used as the `<FileStorage>.filename` attribute. If
  it is not provided, then it will take on the value of \<real filepath>
## Submitting an in-memory string as a file
```
test_request_context(data=
{
    '<form name>': (<BytesIO object>, ['<filename>')
}
```
- A BytesIO object can be submitted instead of a \<real filepath> because a \<FileStorage> instance is always constructed with a file object that is
  open in read-binary mode
```
file = open(<real filepath>, 'rb')
FileStorage(file)
# or
FileStorage(<BytesIO object>)
```