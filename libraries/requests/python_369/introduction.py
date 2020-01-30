# https://requests.readthedocs.io/en/master/ - official documentation
# https://requests.readthedocs.io/en/master/api/ - official API
# https://realpython.com/python-requests/ - tutorial
# https://stackoverflow.com/questions/10667960/python-requests-throwing-sslerror - SSL certificates


import requests


def raise_exception_for_unsuccessful_request():
    '''
    An exception must be manually raised for an unsuccessful request
    - No exception will be raised if the request was successful
    - A request can be unsuccessful for many reasons, only some of which take into account an HTTP response code
        - A status code in the range of [200, 400) is considered successful.
    '''
    #try:
    #    response = requests.get('https://www.789fyh5q398h.com/')
    #    print(response.status_code) # "" 
    #    response.raise_for_status()
    #except Exception as e:
    #    print(type(e)) # <class 'requests.exceptions.ConnectionError'>
    #    print(len(e.args)) # 1
    #    # (MaxRetryError("HTTPSConnectionPool(host='www.789fyh5q398h.com', port=443): Max retries exceeded with url: / (Caused by
    #    # NewConnectionError('<urllib3.connection.VerifiedHTTPSConnection object at 0x1105394d0>: Failed to establish a new connection: [Errno 8]
    #    # nodename nor servname provided, or not known'))"),)
    #    print(e.args)
    try:
        response = requests.get('https://www.omf.coop/deleteUser')
        print(response.status_code) # 405
        response.raise_for_status()
    except Exception as e:
        print(type(e)) # <class 'requests.exceptions.ConnectionError'>
        print(len(e.args)) # 1
        print(e.args) # ('405 Client Error: METHOD NOT ALLOWED for url: https://www.omf.coop/deleteUser',)
    #try:
    #    response = requests.get('https://www.omf.coop')
    #    print(response.status_code) # 200
    #    response.raise_for_status()
    #except Exception as e: # Never invoked
    #    print(type(e))
    #    print(len(e.args))
    #    print(e.args)


def decode_request_content():
    '''
    If no encoding is specified on the response object, requests will try to infer the encoding scheme itself
    '''
    response = requests.get('https://www.omf.coop')
    # The raw bytes of the entity body are available as "content"
    print(type(response.content)) # <class 'bytes'>
    print(response.content) # b'<head>...</body>'
    # The decoded byes of the entity body are available as "text"
    print(type(response.text)) # <class 'str'>
    print(response.text) # '<head>...</body>'
    response.encoding = 'utf-16'
    print(response.text) # 格...㹹


def get_json():
    '''Response objects have a json() convenience method that is a little more steamlined than using json.loads()'''
    response = requests.get('https://api.github.com/')
    dict_ = response.json()
    print(type(dict_)) # <class 'dict'>
    print(dict_) # {'current_user_url':...}


def access_headers():
    '''The HTTP spec defines header keys as case-insensitive. Therefore, response.headers is a dict-like object that has case-insensitive keys'''
    response = requests.get('https://api.github.com/')
    #print(response.headers) # {'Server: 'GitHub.com',...}
    response.headers['sErVeR'] = 'foobar'
    print(response.headers) # {'sErVer: 'foobar',...}


def set_user_agent():
    '''
    Any header, such as the User-Agent, can be set on the request object
    - The requests library does not set any headers by default
    - Rejected User-Agents
        - Mozilla/5.0
    - Accepted User-Agents:
        - Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:71.0) Gecko/20100101 Firefox/71.0
        - No User-Agent
            - I don't understand why requests.get() works but creating a custom request does not
    '''
    url = 'https://nominatim.openstreetmap.org/reverse?format=json&lat={}&lon={}&zoom=18&addressdetails=1'.format(38.88358, -77.10193) 
    custom_req = requests.Request('GET', url)
    print(custom_req.headers) # {}
    prepared_custom_req = custom_req.prepare()
    print(prepared_custom_req.headers) # {}
    s = requests.Session()
    # A PreparedRequest object can only be sent from a requests.Session object
    response = s.send(prepared_custom_req)
    print(response.status_code) # 403
    try:
        response = requests.get(
            url=url,
            headers={'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:71.0) Gecko/20100101 Firefox/71.0'}
        )
        response.raise_for_status()
        print(response.status_code) # 200
        print(response.json())
    except Exception as e:
        print(e.args)


if __name__ == '__main__':
    #raise_exception_for_unsuccessful_request()
    #decode_request_content()
    #get_json()
    #access_headers()
    set_user_agent()
