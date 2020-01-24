# https://realpython.com/async-io-python/


import asyncio


async def this_is_a_coroutine_function():
    '''
    The "async def" syntax creates a "native coroutine."
    - A native coroutine may use return, yield, and/or await, but all of these are optional
        - Using await or return creates a "coroutine function." In order to invoke a coroutine function, I must await its results
        - Using yield creates an asynchronous generator
    '''
    return 'Alice in Wonderland'


async def invoke_coroutine_function():
    '''
    The coroutine function (this_is_a_coroutine_function()) must be awaited
    - In order to use await, this scope must be asynchronous. Thus, this scope also must be a native coroutine
    '''
    print(await this_is_a_coroutine_function())


#if __name__ == '__main__':
async def main():
    '''
    The coroutine function (invoke_coroutine_function()) must be awaited
    - In order to use await, this scope must be asynchronous. Thus, this scope also must be a native coroutine
    - async can only be used with functions, therefore a native coroutine must be invoked from another native coroutine
    '''
    await invoke_coroutine_function()


if __name__ == '__main__':
    '''
    asyncio.run() is the main entry point for asynchronous programs. It manages the asyncio event loop
    - Only one asyncio event loop can run in a thread at a time
    - Ideally, it is only called one time
    - The async/await syntax does not require the asyncio package, but running an asynchronous program requires asyncio.run(), so the packages MUST be
      imported for any asynchronous program
    '''
    asyncio.run(main())