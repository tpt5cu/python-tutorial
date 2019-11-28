# https://docs.python.org/2/glossary.html#term-generator - official definition
# https://docs.python.org/2/reference/expressions.html#yieldexpr - generator implementation


'''
- A "generator function" is a function that when invoked returns an iterator (that iterator is known as a "generator"). This returned generator then
  controls the execution of the generator function
- A call to the "generator function" always returns a NEW generator. It does NOT execute any part of the generator function itself. Only calls to the
  actual generator will execute the generator function
- A generator (NOT the "generator function") executes until it encounters a yield expression, at which point it returns the value and stops executing
    - If the generator is called for the first time, it will "resume" at the beginning of the generator function
    - If the generator is called any time after the first time, it will resume at the last yield expression that it previously stopped at
- The next invocation of the generator function will resume execution AT the last yield expression, NOT the line after the last yield expression
    - If next() was used to resume a generator, the result of the starting (i.e. current) yield expression always evaluates to None
    - If send(<arg>) was used to resume a generator, the result of the starting (i.e. current) yield expression is whatever <arg> was
- The generator will continue executing until it finds the NEXT yield expression, at which point it returns the value and the process will repeat
  until StopIteration is raised
'''


def basic_generator():
    '''
    This single yield expression must be contextualized in such a way that the function will loop back to it upon subsequent calls to next() or
    send().
    '''
    my_list = [1, 2, 3, 4, 5]
    count = 0
    # Here, the first next() call executes but any subsequent next() call will raise StopIteration because the generator will exit without yielding
    # another value. The count += 1 statement is irrelevant
    #yield my_list[count]
    #count += 1
    while True:
        try:
            # Without this try-except, the generator will eventually raise an IndexError. I could put an assignment statement here, but I'm actually
            # ignoring the result of the yield expression, which will always be None given how this generator is called
            yield my_list[count] 
            count += 1
        except:
            raise StopIteration


def use_basic_generator():
    gen = basic_generator()
    for item in gen:
        print(item)


def modifiable_generator():
    '''Even though this generator function doesn't have any parameters, the send() function can still modify its state'''
    print('Generator starting...')
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    count = 0
    while True:
        try:
            # If send(<arg>) is called, then the "skip" variable will be <arg>. If it isn't called, then the "skip" variable will be None. In this
            # way, I can modify the state of a generator during execution if I want, or I can let it be.
            skip = yield my_list[count]
            if skip is not None:
                count = skip
            else:
                count += 1
        except:
            raise StopIteration


def modify_generator_state():
    '''
    send(<arg>) does several things:
    - it sets the value of the CURRENT yield expression to <arg>
    - With this value accounted for, the generator continues executing as normal
    - send() returns a value through exactly the same execution process as next()!
    - That's it! Just keep in mind a generator almost always start and end on the SAME yield expression (except for of course the very first call to the
      generator)
    '''
    gen = modifiable_generator() # initial generator call. Returns a new generator that has NOT started anything yet.
    # Skip numbers 5 - 8
    # enumerate() is NOT causing the generator to execute all at once, it's merely wrapping the generator
    for idx, val in enumerate(gen): # The generator's next() method is implicitly being called by the for-loop
        print("outer: " + str(val))
        if idx == 3:
            print("inner: " + str(gen.send(8)))


def exception_handling_generator():
    '''If I expect to use throw() with a generator, the generator function must be written to handle such exceptions'''
    print('Generator starting...')
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    count = 0
    while True:
        try:
            yield my_list[count] # Any <gen>.throw() exception is raised right here
            count += 1 # When the exception is raised, execution goes directly to the except expression and skips this line
        except ZeroDivisionError as e:
            print("Caught zero divsion error")
        # Uncomment these lines to cause a RuntimeError!
        #except GeneratorExit as e:
        #    yield "whoo!"
        except:
            raise StopIteration


def raise_generator_exception():
    '''
    Provided that the generator handles the raised exception, it handles the exception and then the yields the next value as normal.
    - If an exception is passed into the generator, and the generator does not catch the exception, the exception propagates to the caller as normal.
      Therefore, passing in a random exception to a generator is not helpful at all
    '''
    gen = exception_handling_generator()
    for idx, val in enumerate(gen):
        print("outer: " + str(val))
        # Raise after reaching value 5 (index 4)
        if idx == 4:
            print(gen.throw(ZeroDivisionError)) # This is 5 because count +=1 didn't execute on this run of the generator function


def close_generator():
    '''
    <gen>.close() raises GeneratorExit at the point where the generator was paused (i.e. the last yield expression). It does not return anything
    - Two things will cause <gen>.close() to return to the caller without incident:
      - It raises StopIteration by virtue of being already closed OR existing normally
      - It raises GeneratorExit because it didn't catch the GeneratorExit
    - If the generator yields a value, a RuntimeError is raised
    '''
    gen = exception_handling_generator()
    for idx, val in enumerate(gen):
        print("outer: " + str(val))
        if idx == 7:
            print(gen.close())
    #gen.next() # StopIteration. The generator is closed!


if __name__ == "__main__":
    #use_basic_generator()
    #modify_generator_state()
    #raise_generator_exception()
    close_generator()