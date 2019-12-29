# Available caching extension packages
## requests-cache
- Very easy to use because it ignores all cache headers
- Can simply monkey-patch on top of requests (e.g. can use requests.get without an explicit session and the cache will "just work")
- I can set an explicit timeout after which the cache will expire so that even if a duplicate request occurs, a real request will be sent
## CacheControl
- Officially endorsed by the Requests package
- Provides decently low-level control for handling caching, but it's not overwhelming
- Understands how to use cache headers and HTTP status codes
- Requires using a requests.Session for my requests
- There are numerous storage mediums available:
    - In-memory thread-safe dict
        - Since gunicorn runs multiple processes, the cache won't be shared across those processes, and each process will end up having a duplicate
          cache
    - FileCache: a directory called .webcache will be created, and a file will be stored for each cached request
        - The files are thread-safe, but not (explicitly) multi-process safe!
    - RedisCache
## httpcache
- deprecated

- I should come back to this after the real refactor is done