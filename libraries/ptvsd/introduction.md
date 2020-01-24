- https://github.com/microsoft/ptvsd
# Installation
- $ pip install ptvsd
# CLI usage
- $ `<python> -m ptvsd --host localhost --port 5678 <file>`
    - E.g. `/Users/austinchang/.pyenv/versions/venv3.6.9-ptvsd/bin/python -m ptvsd --host localhost --port 5678 /Users/austinchang/pycharm/omf/omf/web.py`
    - Run with debugging enabled, but don't wait for the debugger to attach (i.e. code immediately begins executing)
    - This works with `web.py` and it reproduces the error I've been getting, which is great
- $ `<python> -m ptvsd --host localhost --port 5678 --wait <file>`
    - E.g. $ `/Users/austinchang/.pyenv/versions/venv3.6.9-ptvsd/bin/python -m ptvsd --host localhost --port 5678 --wait /Users/austinchang/pycharm/omf/omf/web.py`
    - Wait for the debugger to attach before running my code
    - This is slow to start. In fact, it doesn't even work with `web.py`
## Debugging a module
- Just use -m <file> in the above commands instead of the filename
# Diagnosing the 'module not found' error
- The following tests assume I have the venv3.6.9-ptvsd virtual environment activated and that I'm in the correct directory
    - It appears the error occurs when VSCode runs the debugger, but not from within the /Users/austinchang/pycharm/omf/omf directory
- These commands work:
    - $ `python -m ptvsd --host localhost --port 5678 -m web`
    - $ `python -m ptvsd --host localhost --port 5678 web.py`
    - $ `python -m ptvsd --host localhost --port 5678 /Users/austinchang/pycharm/omf/omf/web.py`
    - $ `/Users/austinchang/.pyenv/versions/venv3.6.9-ptvsd/bin/python -m ptvsd --host localhost --port 5678 /Users/austinchang/pycharm/omf/omf/web.py`
- These commands don't work: