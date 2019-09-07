# https://docs.python.org/2/reference/expressions.html#yieldexpr - an iterator can be a generator
# https://docs.python.org/2/library/stdtypes.html#generator-types - generator as a type (this is confusing)
# https://stackoverflow.com/questions/2776829/difference-between-pythons-generators-and-iterators

# https://stackoverflow.com/questions/818828/is-it-possible-to-implement-a-python-for-range-loop-without-an-iterator-variable
# https://stackoverflow.com/questions/522563/accessing-the-index-in-for-loops - how to iterate in general


"""
An object that follows the iterator protocol is known as an iterator.
- Since a protocol is another name for an interface, and since in OO programming an interface IS a type, then it is valid to say that Python has
  iterator types. From my Java days, I have this fixed notion of primitives vs. objects vs. interfaces, but Python only has objects. It is valid to
  say that Python has an "iterator type", but it is a little confusing to me becuase I like my types to be concrete pieces of data. Therefore, I'm
  grouping types that are defined by following a protocol in this "built_in protocols" section

It is not possible to iterate without an iterator in Python. Why? Because for-loops use iterators under the hood. See the link for clarification.
- even using enumerate() to get a convenience index is using an iterator under the hood
"""