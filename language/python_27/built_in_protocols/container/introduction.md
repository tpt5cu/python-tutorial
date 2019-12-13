- https://rszalski.github.io/magicmethods/
- https://docs.python.org/2.7/reference/datamodel.html#emulating-container-types
# Introduction
- Containers are either sequences, mappings, or something else. Therefore, the container "protocol" is broader than either of those two built-in types. 
# Immutable container protocol
- Implement __len__ and __getitem__
# Mutable containers protocol
- Implement __setitem__ and __delitem__ as well as all immutable container functions
# Iterable containers
- Must follow the iterable protocol