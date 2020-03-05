# Links
- https://networkx.github.io/documentation/networkx-1.11/reference/classes.graph.html - NetworkX v1.11
- https://networkx.github.io/documentation/stable/reference/classes/graph.html - Networkx v2.4 (latest)
- https://networkx.github.io/documentation/stable/release/migration_guide_from_1.x_to_2.0.html - migration guide
# Workspace organization
- The directory hierarchy is the way it is because v2.4 and v1.11 probably have slightly different package structures
- Regardless of the version, almost everything is directly available on the networkx package object because __init__.py imports EVERYTHING
    - Why do data science packages like to do this all of the time?
# Installation
- $ `pip install networkx==1.11`
- $ `pip install networkx==2.4`
