import tempfile, os, time, pathlib


def delete_file():
    with tempfile.NamedTemporaryFile(dir=pathlib.Path(__file__).parent, delete=False) as f:
        filename = f.name
    time.sleep(2)
    os.remove(filename)


if __name__ == '__main__':
    delete_file()