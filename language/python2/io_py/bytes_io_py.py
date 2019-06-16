"""
https://docs.python.org/2/library/stdtypes.html#bltin-file-objects (has links to useful high-level file operation packages)
https://docs.python.org/2/library/stdtypes.html#bltin-file-objects
https://stackoverflow.com/questions/29324037/convert-bytesio-into-file (very, very helpful)
"""


import io


def file_to_bytesio():
    """
    A Flask FileStorage object needs a stream as an argument, so I need to convert my file into a stream. An _io.BytesIO instance is/isn't a stream? I
    don't understand streams well in Python at all
    """
    file_path = "/Users/austinchang/tutorials/python/language/testCsv.csv"
    byte_io_path = "./bytes-io.txt"
    text_io_path = "./text-io.txt"
    with open(file_path) as f:
        b_io = io.BytesIO(f.read())
        t_io = io.TextIOWrapper(b_io)
        print(type(b_io))
        print(type(t_io))
        with open(byte_io_path, "w") as b_path:
            b_path.write(b_io.read())
        with open(text_io_path, "w") as t_path:
            # This doesn't write anything because b_io has already been read so presumably there's nothing left to read!
            t_path.write(t_io.read())

if __name__ == "__main__":
    file_to_bytesio()