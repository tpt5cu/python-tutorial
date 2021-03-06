- https://stackoverflow.com/questions/3304708/whats-the-c-escape-sequence-for-blanks
- https://stackoverflow.com/questions/7605198/how-does-b-work-when-using-regular-expressions
- https://regex101.com/ - super helpful
# Performance
- The compiled versions of the most recent patterns passed to re.match(), re.search() or re.compile() are cached, so programs that use only a few
  regular expressions at a time needn’t worry about compiling regular expressions. 
# Character classes
- `\w`: alphanumeric characters and underscore, i.e. `[a-zA-Z0-9_]` 
- `\W`: non-alphanumeric character and not the underscore, i.e. `[^a-zA-Z0-9_]`
- `\s`: any whitespace character, i.e. `[ \t\n\r\f\v]`
    - The space character does not need to be escaped. It can be entered in a regex as is like a regular character
- `\b`: the boundary between a `\w` and `\W` character, or vice versa. Also the boundary between a `\w` character and the beginning or end of a string
    - The end of a word is defined to be a whitespace character or a non-alphanumeric, non-underscore character.
    - E.g. `\bfoo\b` matches "foo", "foo." "(foo)", but not "foo3"
    - `\b` does not consume any character. It is an assertion that can be true or false
# Optional
- `colou?r` matches `color` or `colour`
- `Feb(ruary)?` matches `February` or `Feb`