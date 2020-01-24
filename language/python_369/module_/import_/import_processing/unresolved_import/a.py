# https://stackoverflow.com/questions/744373/circular-or-cyclic-imports-in-python - extremely helpful
# https://stackoverflow.com/questions/710551/use-import-module-or-from-module-import - tangentally helpful


'''
This is a conceptual explanation of one system Python uses to handle imports. I informally call this import style "unresolved imports" because
circular import traps aren't possible but the imported objects are incomplete!

When "import b" from module "a" is encountered:
1) Python locates the desired module, "b". Before it begins executing the code in b (which in my old view was the only thing that any import statement
   ever did), it adds b to the global symbol table of a. Now Python sees that there is a variable "b" in the global symbol table of "a", but Python
   does not know anything about "b"
2) Now Python executes the code in b
3) If b also perform "import a", then "a" is added to the global symbol table of "b"
4) Now Python executes the code in a
5) But wait! Python has once again encoutered "import b"! Won't this cause an infinite loop? No, because Python recognizes that "b" is already in the
   global symbol table of a, so it doesn't need to once again execute the code in b
    - However, there is a price to pay for this ability to handle circular imports. Python effectively "skipped over" the second instance of "import
      b", but as a result "b" is an incomplete object! No symbols inside of b are actually available through b because the code in b hasn't executed
      yet. That's why "b.say_hello_from_b()" causes an AttributeError
6) Python finishes executing the code in a, but doesn't execute the __main__ section yet because __name__ != __main__. Control instead returns to b.py
   because "import a" has finished
   - __name__ == "a" the when imports are being resolved
   - __name__ == "__main__" always in the main entry point script (which happens to be a.py), but since we put the if-statement at the end of the
     file, the module doesn't do any "real work" until all the imports are finished
        - Thus, executing a module in Python in a sensible way is entirely dependent on placing the if-statement after the initial imports!
7) The rest of the code in b.py is executed
8) Control returns to a.py right after the very first "import b" statement. Now __name__ == __main__ as it did when this whole process started
9) The code in a finishes executing, and all of the symbols defined in a are now available in the __main__ namespace
10) Python encounters the __main__ section and executes it
    - Everything on b is visible because the imports are all done
    - Everything on b is visible inside of any function because the functions always execute after the import process is finished
    - This explains why "True" is printed twice
        - It is printed the first time when "import a" in b.py executes
        - It is printed the second time after "import b" in a.py finishes for real
'''
import b
print('b' in globals()) # True
#b.say_hello_from_b() # AttributeError: module 'b' has no attribute 'say_hello_from_b'
#print(__name__)


def say_hello_from_a():
    print('Hello from a.py')


if __name__ == '__main__':
    print('__main__ is a.py')
    say_hello_from_a()
    b.say_hello_from_b()
    