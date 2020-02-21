- The directory hierarchy is the way it is because v2.4 and v1.11 probably have slightly different package structures
- Regardless of the version, almost everything is directly available on the networkx package object because __init__.py imports EVERYTHING
    - Why do data science packages like to do this all of the time?
# Installation
- $ `pip install networkx==1.11`
- $ `pip install networkx==2.4`
