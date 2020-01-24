- https://docs.pytest.org/en/latest/getting-started.html
- https://docs.pytest.org/en/latest/fixture.html
- https://stackoverflow.com/questions/36456920/is-there-a-way-to-specify-which-pytest-tests-to-run-from-a-file
- https://docs.pytest.org/en/latest/capture.html
# Running tests
- $ `pytest`
    - pytest automatically searches for files named either 1) "test_*.py" or 2) "*_test.py" and searches those files for any tests
- $ `pytest <filename>`
    - Run the tests only inside of <file name>
- $ `pytest -q`
    - Run in less-verbose mode
- $ `pytest <filename> -k <matching strings>`
    - Run tests that match the pattern inside of the file
- $ `pytest <filename>::<test name>`
    - Run a specific test inside of a file
- $ `pytest -s`
    - Print all stdout to the console. Normally, only failing tests have their stdout captured
- pytest is smart. I can hide my test.py files inside of arbitrarily named directories underneath of where $ pytest $ is run, and pytest will find
  them