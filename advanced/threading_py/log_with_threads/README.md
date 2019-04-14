- https://stackoverflow.com/questions/9366264/what-does-it-mean-to-join-a-thread
- https://www.blog.pythonlibrary.org/2016/07/28/python-201-a-tutorial-on-threads/

- https://docs.python.org/2.7/library/logging.handlers.html#logging.FileHandler (annoying that it's documented like this)

# Thread join

- In general, a join() operation is used to make a parent thread wait for its child thread to finish. 
    - However, any thread can join() in relation to another thread.
    - It just doesn't make much sense to make a child thread wait until its parent finishes. Why did I create the child thread in the first place?
- A parent thread can perform a join() operation in relationship to one of its child threads. 1 of 2 things can happen.
    - 1) The parent thread finishes before the child thread. join() will make the parent suspend operation until the child thread finishes, at which
         point the child thread will terminate and the parent will resume
    - 2) The child thread finishes before the parent thead. join() will be ignored by the parent, and the parent thread will resume as if there never
         was a join

# Thread yield

- Threads should share CPU time with each other. If they don't, it's possible only a few threads will run while the rest are waiting. yield() (and
  suspend()) solve this problem
- When any thread executes yield(), the executing thread suspends itself and allows some other thread to run.
    - The suspended thread will run again when the CPU becomes available. The CPU could become available if some other thread also ran yield(), or it
      could become available some other way. It doesn't matter.

# Thread suspend and resume

- suspend() is not the same as yield(). 
- A thread can execute a suspend() call on itself or another thread. The suspended thread will not run until an explicit resume() call allows it to
  run again
- Some operating systems don't allows suspend() and resume() because of deadlock. Deadlock occurs when a thread acquires sole access to some data
  (i.e. a lock) and then that same thread is suspended. Now, no thread other thread can touch the data and the lock can't be released until a resume()
  call

To be continued: 4/6/19