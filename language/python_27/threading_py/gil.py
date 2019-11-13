# https://stackoverflow.com/questions/38280094/python-requests-with-multithreading
# https://stackoverflow.com/questions/18188044/is-the-session-object-from-pythons-requests-library-thread-safe
# https://www.peterbe.com/plog/best-practice-with-retries-with-requests - exceptions in worker threads


import threading, time, timeit, urllib, urllib, requests


def fill_list(list, start, end, value):
    for i in range(start, end):
        list[i] = value
        time.sleep(0.5)
    print('List from {} to {} filled with {}'.format(start, end, value))


def spawn_fill_list_threads():
    """
    Due to Python's GIL, the two threads spawned in spawn_fill_list_threads() execute in series, not in parallel
    - 0.5 * 10 = 5 
    - 5 * 2 = 10
    """
    data = [0] * 20
    t0 = threading.Thread(target=fill_list, args=(data, 0, 10, 'A'))
    t1 = threading.Thread(target=fill_list, args=(data, 10, 20, 'B'))
    t0.start()
    t1.start()
    t0.join()
    t1.join()
    print("List has been filled")
    print(data)


session = requests.Session()


def request_urls(use_requests=True):
    data = bytearray()
    #url = 'https://www.google.com'
    url = 'https://www.bing.com'
    if use_requests:
        for _ in range(100):
            #r = requests.get(url)
            p = requests.Request(method='GET', url='https://www.google.com').prepare()
            r = session.send(p)
            data += r.text.encode('ascii', 'ignore')
    else:
        for _ in range(100):
            f = urllib.urlopen(url)
            data += f.read()


def spawn_request_urls_threads(thread_count=10):
    """The GIL is released in the during web requests, since those requests are classified as an I/O operation"""
    threads = []
    for i in range(thread_count):
        t = threading.Thread(target=request_urls)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print("Requests have been sent")


if __name__ == '__main__':
    """
    These benchmarks are inconsistent because I think Google might be rate-limiting me. Google is definitely rate limiting me.

    When the urllib library is used, these are the benchmarks
    - request_urls(): 14.77
    - spawn_request_urls_threads(): 30.56

    When the requests library is used, these are the benchmarks
    - request_urls(): 15.16
    - spawn_request_urls_threads(): 18.24, 19.00
    - spawn_request_urls_threads() with Session object: 44.70, 41.21

    In conclusion, even though "the Response.content property will block until the entire response has been downloaded", requests is fine for my needs.
    Why? Because the bottleneck for me isn't that I'm getting a huge amount of text in each response. My bottleneck is the sheer number of responses
    that I need to send, and the associated waiting time. The Python GIL does release for network requests because those are low-level and understood
    by the GIL as non-blocking I/O.
    """
    #print(timeit.timeit('spawn_fill_list_threads()', setup='from __main__ import spawn_fill_list_threads', number=2))
    #print(timeit.timeit('request_urls()', setup='from __main__ import request_urls', number=1))
    print(timeit.timeit('spawn_request_urls_threads()', setup='from __main__ import spawn_request_urls_threads', number=1))