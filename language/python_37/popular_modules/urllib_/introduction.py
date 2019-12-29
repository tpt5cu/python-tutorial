# https://docs.python.org/3/library/urllib.request.html#request-objects - Request object interface
# https://docs.python.org/3/library/urllib.request.html#openerdirector-objects - OpenerDirector object interface
# https://docs.python.org/3/library/urllib.request.html#module-urllib.response - Response object interface


from urllib import request


'''
I have not investigated how caching works with urllib. Instead, I should just use the requests module
    - Seriously, not even the requests module handles caching. It delegates that to a 3rd party library called CacheControl

urlopen()
- urllib.request.urlopen(): open the URL (or Request object) and return a slightly modified http.client.HTTPResponse object (for HTTP and HTTPS URLs)
    - This object is a file-like object that has read(), readline(), info() (returns headers), geturl() (returns the URL), and more
        - Everything that is read is returned as in bytes, not Unicode
- The HTTPResponse works as a context manager

Request()
- urllib.request.Request(): an object that is an abstraction of a URL request
    - add_header(): add a header to the request
        - All headers will be ignored by all handlers except HTTP handlers
- It is possible to spoof headers with this class
- Instances can directly be instantiated

OpenerDirectory
- urllib.request.OpenerDirector: opens URLs (or Request objects) via BaseHandlers that are chained together. It manages the chaining of handlers and
  error recovery
    - open(): open the given URL and handle the response according to the (class instances) or (handlers) that are chained on the OpenerDirector
- Instances are not directly instantiated:
    - urllib.request.install_opener(): install a global OpenerDirector that will be used by any subsequent urlopen() call
        - urlopen() actually just calls the open() method of the currently installed OpenerDirector. This means that if I don't instantiate a global
          OpenerDirector myself, Python automatically creates one when I call urlopen()
    - urllib.request.build_opener(): return an OpenerDirector instance with the (optional) specified handlers chained together
        - By default, several instances of classes are already chained to the front of an OpenerDirector. The order of these objects as specified in
          the documentation makes sense.
'''


def inspect_response_object():
    '''
    ['__abstractmethods__', '__class__', '__del__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__',
    '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__module__', '__ne__',
    '__new__', '__next__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_abc_impl',
    '_checkClosed', '_checkReadable', '_checkSeekable', '_checkWritable', '_check_close', '_close_conn', '_get_chunk_left', '_method',
    '_peek_chunked', '_read1_chunked', '_read_and_discard_trailer', '_read_next_chunk_size', '_read_status', '_readall_chunked', '_readinto_chunked',
    '_safe_read', '_safe_readinto', 'begin', 'chunk_left', 'chunked', 'close', 'closed', 'code', 'debuglevel', 'detach', 'fileno', 'flush', 'fp',
    'getcode', 'getheader', 'getheaders', 'geturl', 'headers', 'info', 'isatty', 'isclosed', 'length', 'msg', 'peek', 'read', 'read1', 're
    '''
    with request.urlopen('https://www.google.com') as f:
        '''
        - getheaders(): return a nice list of tuples
        - headers: return a nicely formatted text output of the headers
        - msg: return the HTTP message associated with the response code
        - read(): return a bytes object of the entire entity body
        - readline(): return a bytes object of the entity body up to a newline
        - readlines(): return a list of bytes objects
        '''
        #print(type(f)) # <class 'http.client.HTTPResponse'>

        # <class 'http.client.HTTPResponse'> [('Date', 'Sat, 28 Dec 2019 20:59:04 GMT'), ('Expires', '-1'), ('Cache-Control', 'private, max-age=0'),
        # ('Content-Type', 'text/html; charset=ISO-8859-1'), ('P3P', 'CP="This is not a P3P policy! See g.co/p3phelp for more info."'), ('Server',
        # 'gws'), ('X-XSS-Protection', '0'), ('X-Frame-Options', 'SAMEORIGIN'), ('Set-Cookie', '1P_JAR=2019-12-28-20; expires=Mon, 27-Jan-2020
        # 20:59:04 GMT; path=/; domain=.google.com'), ('Set-Cookie',
        # 'NID=194=Mguy9iwO9SreBvvdIuvj--uVMsga1AgYdIH__uobZeXon3OZs4JVK3Rc1hHnkp76Xux_jeN2jJXksZ6hO4oFSTj-5D-Gvq7vtHhIr2iCzpRkHHZAvCAo4d-V86avHFY0XTkztvunX09ZqamdP_7Yb_xIUvXTI-lYWO-DLlydhf4;
        # expires=Sun, 28-Jun-2020 20:59:04 GMT; path=/; domain=.google.com; HttpOnly'), ('Alt-Svc', 'quic=":443"; ma=2592000;
        # v="46,43",h3-Q050=":443"; ma=2592000,h3-Q049=":443"; ma=2592000,h3-Q048=":443"; ma=2592000,h3-Q046=":443"; ma=2592000,h3-Q043=":443";
        # ma=2592000'), ('Accept-Ranges', 'none'), ('Vary', 'Accept-Encoding'), ('Connection', 'close')]
        #print(f.getheaders())

        # Date: Sat, 28 Dec 2019 20:59:04 GMT
        # Expires: -1
        # Cache-Control: private, max-age=0
        # Content-Type: text/html; charset=ISO-8859-1
        # P3P: CP="This is not a P3P policy! See g.co/p3phelp for more info."
        # Server: gws
        # X-XSS-Protection: 0
        # X-Frame-Options: SAMEORIGIN
        # Set-Cookie: 1P_JAR=2019-12-28-20; expires=Mon, 27-Jan-2020 20:59:04 GMT; path=/; domain=.google.com
        # Set-Cookie: NID=194=Mguy9iwO9SreBvvdIuvj--uVMsga1AgYdIH__uobZeXon3OZs4JVK3Rc1hHnkp76Xux_jeN2jJXksZ6hO4oFSTj-5D-Gvq7vtHhIr2iCzpRkHHZAvCAo4d-V86avHFY0XTkztvunX09ZqamdP_7Yb_xIUvXTI-lYWO-DLlydhf4; expires=Sun, 28-Jun-2020 20:59:04 GMT; path=/; domain=.google.com; HttpOnly
        # Alt-Svc: quic=":443"; ma=2592000; v="46,43",h3-Q050=":443"; ma=2592000,h3-Q049=":443"; ma=2592000,h3-Q048=":443"; ma=2592000,h3-Q046=":443"; ma=2592000,h3-Q043=":443"; ma=2592000
        # Accept-Ranges: none
        # Vary: Accept-Encoding
        # Connection: close
        #print(f.headers)

        #print(f.geturl()) # https://www.google.com
        #print(f.msg) # OK

        # b'<!doctype html><html itemscope="" itemtype="http://schema.org/WebPage" lang="en"><head><meta content="Search the world\'s information,
        # including webpages, images, videos and more. Google has many special features to help you find exactly what you\'re looking for."
        # name="description"><meta content="noodp" name="robots"><meta content="text/html; charset=UTF-8" http-equiv="Content-Type"><meta
        # content="/images/branding/googleg/1x/googleg_standard_color_128dp.png" itemprop="image"><title>Google</title><script
        # nonce="t0hBoX4VMSv4mi3UdDKPxg==">(function(){window.google={kEI:\'GMIHXtCHBoSa5gKwx5Aw\',kEXPI:\'0,1353746,5663,730,224,4727,378,206,467,1948,539,250,10,290,423,338,175,364,671,483,3,209,69,4,60,315,426,209,10,1129468,143,1197661,34,454,38,329080,1294,12383,4855,32692,8161,7086,867,28684,363,8825,8384,4858,1362,284,4039,4968,773,2256,2814,4824,223,6191,1719,1497,319,1952,16,2044,5766,1,1455,1687,5297,516,1538,920,873,1217,2975,2736,1558,2136,1142,3913,2377,3254,620,2883,21,317,235,2938,975,1,370,2776,520,399,992,1285,8,2796,885,84,610,14,1167,112,2212,202,37,291,149,1103,327,513,517,317,825,277,47,8,48,820,3438,260,52,1135,1,3,2063,606,1839,184,595,1325,378,685,1261,747,429,44,999,103,328,1284,16,84,417,901,1525,1639,608,473,1339,29,719,825,214,3092,137,771,1548,524,7,728,592,1574,1914,791,689,1276,69,3,5331,1,1178,299,1945,588,258,347,234,1041,1041,2459,1058,168,1462,842,1228,1865,1274,108,1246,26,442,559,654,41,439,809,99,2,433,538,542,143,373,11,1149,366,127,626,1121,523,358,1157,10,343,83,507,78,457,1486,533,52,355,428,2,198,288,176,129,819,9,1,841,59,1,2,1,112,13,2,13,6,140,138,333,109,373,603,98,258,523,200,811,189,6,15,272,3,314,255,1,257,8,61,24,223,140,483,217,751,113,176,281,1183,229,5858908,1805894,4194850,2801172,549,333,444,1,2,80,1,900,896,1,8,1,2,2551,1,748,141,59,736,563,1,4265,1,1,1,1,137,1,784,4,2,12,77,8,1,14,5,2,3,3,1,3,5,3,3,3,3,3,1,3,3,3,3,25,12,3,1,1,2,1,3,6,1,2,1,3,11,6,2,6,5,10,7,2,4,2,10,3,2,2,2,25,10,15,2,3365796,20598662\',authuser:0,kscs:\'c9c918f0_GMIHXtCHBoSa5gKwx5Aw\',kGL:\'US\',kBL:\'v77x\'};google.sn=\'webhp\';google.kHL=\'en\';google.jsfs=\'Ffpdje\';})();(function(){google.lc=[];google.li=0;google.getEI=function(a){for(var
        # b;a&&(!a.getAttribute||!(b=a.getAttribute("eid")));)a=a.parentNode;return b||google.kEI};google.getLEI=function(a){for(var
        # b=null;a&&(!a.getAttribute||!(b=a.getAttribute("leid")));)a=a.parentNode;return
        # b};google.https=function(){return"https:"==window.location.protocol};google.ml=function(){return null};google.time=function(){return(new
        # Date).getTime()};google.log=function(a,b,e,c,g){if(a=google.logUrl(a,b,e,c,g)){b=new Image;var
        # d=google.lc,f=google.li;d[f]=b;b.onerror=b.onload=b.onabort=function(){delete
        # d[f]};google.vel&&google.vel.lu&&google.vel.lu(a);b.src=a;google.li=f+1}};google.logUrl=function(a,b,e,c,g){var
        # d="",f=google.ls||"";e||-1!=b.search("&ei=")||(d="&ei="+google.getEI(c),-1==b.search("&lei=")&&(c=google.getLEI(c))&&(d+="&lei="+c));c="";!e&&google.cshid&&-1==b.search("&cshid=")&&"slh"!=a&&(c="&cshid="+google.cshid);a=e||"/"+(g||"gen_204")+"?atyp=i&ct="+a+"&cad="+b+d+f+"&zx="+google.time()+c;/^http:/i.test(a)&&google.https()&&(google.ml(Error("a"),!1,{src:a,glmm:1}),a="");return
        # a};}).call(this);(function(){google.y={};google.x=function(a,b){if(a)var c=a.id;else{do
        # c=Math.random();while(google.y[c])}google.y[c]=[a,b];return!1};google.lm=[];google.plm=function(a){google.lm.push.apply(google.lm,a)};google.lq=[];google.load=function(a,b,c){google.lq.push([[a],b,c])};google.loadAll=function(a,b){google.lq.push([a,b])};}).call(this);google.f={};(function(){document.documentElement.addEventListener("submit",function(b){var
        # a;if(a=b.target){var c=a.getAttribute("data-submitfalse");a="1"==c||"q"==c&&!a.elements.q.value?!0:!1}else
        # a=!1;a&&(b.preventDefault(),b.stopPropagation())},!0);}).call(this);var a=window.location,b=a.href.indexOf("#");if(0<=b){var
        # c=a.href.substring(b+1);/(^|&)q=/.test(c)&&-1==c.indexOf("#")&&a.replace("/search?"+c.replace(/(^|&)fp=[^&]*/g,"")+"&cad=h")};</script><style>#gbar,#guser{font-size:13px;padding-top:1px
        # !important;}#gbar{height:22px}#guser{padding-bottom:7px !important;text-align:right}.gbh,.gbd{border-top:1px solid
        # #c9d7f1;font-size:1px}.gbh{height:0;position:absolute;top:24px;width:100%}@media
        # all{.gb1{height:22px;margin-right:.5em;vertical-align:top}#gbar{float:left}}a.gb1,a.gb4{text-decoration:underline
        # !important}a.gb1,a.gb4{color:#00c !important}.gbi .gb4{color:#dd8e27 !important}.gbf .gb4{color:#900
        # !important}\n</style><style>body,td,a,p,.h{font-family:arial,sans-serif}body{margin:0;overflow-y:scroll}#gog{padding:3px 8px
        # 0}td{line-height:.8em}.gac_m td{line-height:17px}form{margin-bottom:20px}.h{color:#36c}.q{color:#00c}.ts
        # td{padding:0}.ts{border-collapse:collapse}em{font-weight:bold;font-style:normal}.lst{height:25px;width:496px}.gsfi,.lst{font:18px
        # arial,sans-serif}.gsfs{font:17px arial,sans-serif}.ds{display:inline-box;display:inline-block;margin:3px 0
        # 4px;margin-left:4px}input{font-family:inherit}a.gb1,a.gb2,a.gb3,a.gb4{color:#11c
        # !important}body{background:#fff;color:black}a{color:#11c;text-decoration:none}a:hover,a:active{text-decoration:underline}.fl
        # a{color:#36c}a:visited{color:#551a8b}a.gb1,a.gb4{text-decoration:underline}a.gb3:hover{text-decoration:none}#ghead a.gb2:hover{color:#fff
        # !important}.sblc{padding-top:5px}.sblc a{display:block;margin:2px 0;margin-left:13px;font-size:11px}.lsbb{background:#eee;border:solid
        # 1px;border-color:#ccc #999 #999 #ccc;height:30px}.lsbb{display:block}.ftl,#fll a{display:inline-block;margin:0
        # 12px}.lsb{background:url(/images/nav_logo229.png) 0 -261px
        # repeat-x;border:none;color:#000;cursor:pointer;height:30px;margin:0;outline:0;font:15px
        # arial,sans-serif;vertical-align:top}.lsb:active{background:#ccc}.lst:focus{outline:none}</style><script
        # nonce="t0hBoX4VMSv4mi3UdDKPxg=="></script></head><body bgcolor="#fff"><script nonce="t0hBoX4VMSv4mi3UdDKPxg==">(function(){var
        # src=\'/images/nav_logo229.png\';var iesg=false;document.body.onload = function(){window.n && window.n();if (document.images){new
        # Image().src=src;}\nif (!iesg){document.f&&document.f.q.focus();document.gbqf&&document.gbqf.q.focus();}\n}\n})();</script><div id="mngb">
        # <div id=gbar><nobr><b class=gb1>Search</b> <a class=gb1 href="https://www.google.com/imghp?hl=en&tab=wi">Images</a> <a class=gb1
        # href="https://maps.google.com/maps?hl=en&tab=wl">Maps</a> <a class=gb1 href="https://play.google.com/?hl=en&tab=w8">Play</a> <a class=gb1
        # href="https://www.youtube.com/?gl=US&tab=w1">YouTube</a> <a class=gb1 href="https://news.google.com/nwshp?hl=en&tab=wn">News</a> <a
        # class=gb1 href="https://mail.google.com/mail/?tab=wm">Gmail</a> <a class=gb1 href="https://drive.google.com/?tab=wo">Drive</a> <a class=gb1
        # style="text-decoration:none" href="https://www.google.com/intl/en/about/products?tab=wh"><u>More</u> &raquo;</a></nobr></div><div id=guser
        # width=100%><nobr><span id=gbn class=gbi></span><span id=gbf class=gbf></span><span id=gbe></span><a
        # href="http://www.google.com/history/optout?hl=en" class=gb4>Web History</a> | <a  href="/preferences?hl=en" class=gb4>Settings</a> | <a
        # target=_top id=gb_70 href="https://accounts.google.com/ServiceLogin?hl=en&passive=true&continue=https://www.google.com/" class=gb4>Sign
        # in</a></nobr></div><div class=gbh style=left:0></div><div class=gbh style=right:0></div> </div><center><br clear="all" id="lgpd"><div
        # id="lga"><img alt="Google" height="92" src="/images/branding/googlelogo/1x/googlelogo_white_background_color_272x92dp.png"
        # style="padding:28px 0 14px" width="272" id="hplogo"><br><br></div><form action="/search" name="f"><table cellpadding="0" cellspacing="0"><tr
        # valign="top"><td width="25%">&nbsp;</td><td align="center" nowrap=""><input name="ie" value="ISO-8859-1" type="hidden"><input value="en"
        # name="hl" type="hidden"><input name="source" type="hidden" value="hp"><input name="biw" type="hidden"><input name="bih" type="hidden"><div
        # class="ds" style="height:32px;margin:4px 0"><input class="lst" style="color:#000;margin:0;padding:5px 8px 0 6px;vertical-align:top"
        # autocomplete="off" value="" title="Google Search" maxlength="2048" name="q" size="57"></div><br style="line-height:0"><span class="ds"><span
        # class="lsbb"><input class="lsb" value="Google Search" name="btnG" type="submit"></span></span><span class="ds"><span class="lsbb"><input
        # class="lsb" id="tsuid1" value="I\'m Feeling Lucky" name="btnI" type="submit"><script nonce="t0hBoX4VMSv4mi3UdDKPxg==">(function(){var
        # id=\'tsuid1\';document.getElementById(id).onclick = function(){if (this.form.q.value){this.checked = 1;if
        # (this.form.iflsig)this.form.iflsig.disabled = false;}\nelse top.location=\'/doodles/\';};})();</script><input
        # value="AAP1E1EAAAAAXgfQKE3NLYjFYw_EiC9YXV73c9E0Agme" name="iflsig" type="hidden"></span></span></td><td class="fl sblc" align="left"
        # nowrap="" width="25%"><a href="/advanced_search?hl=en&amp;authuser=0">Advanced search</a><a
        # href="/language_tools?hl=en&amp;authuser=0">Language tools</a></td></tr></table><input id="gbv" name="gbv" type="hidden" value="1"><script
        # nonce="t0hBoX4VMSv4mi3UdDKPxg==">(function(){var a,b="1";if(document&&document.getElementById)if("undefined"!=typeof
        # XMLHttpRequest)b="2";else if("undefined"!=typeof ActiveXObject){var
        # c,d,e=["MSXML2.XMLHTTP.6.0","MSXML2.XMLHTTP.3.0","MSXML2.XMLHTTP","Microsoft.XMLHTTP"];for(c=0;d=e[c++];)try{new
        # ActiveXObject(d),b="2"}catch(h){}}a=b;if("2"==a&&-1==location.search.indexOf("&gbv=2")){var
        # f=google.gbvu,g=document.getElementById("gbv");g&&(g.value=a);f&&window.setTimeout(function(){location.href=f},0)};}).call(this);</script></form><div
        # id="gac_scont"></div><div style="font-size:83%;min-height:3.5em"><br></div><span id="footer"><div style="font-size:10pt"><div
        # style="margin:19px auto;text-align:center" id="fll"><a href="/intl/en/ads/">Advertising\xa0Programs</a><a href="/services/">Business
        # Solutions</a><a href="/intl/en/about.html">About Google</a></div></div><p style="color:#767676;font-size:8pt">&copy; 2019 - <a
        # href="/intl/en/policies/privacy/">Privacy</a> - <a href="/intl/en/policies/terms/">Terms</a></p></span></center><script
        # nonce="t0hBoX4VMSv4mi3UdDKPxg==">(function(){window.google.cdo={height:0,width:0};(function(){var
        # a=window.innerWidth,b=window.innerHeight;if(!a||!b){var
        # c=window.document,d="CSS1Compat"==c.compatMode?c.documentElement:c.body;a=d.clientWidth;b=d.clientHeight}a&&b&&(a!=google.cdo.width||b!=google.cdo.height)&&google.log("","","/client_204?&atyp=i&biw="+a+"&bih="+b+"&ei="+google.kEI);}).call(this);})();(function(){var
        # u=\'/xjs/_/js/k\\x3dxjs.hp.en_US.PXQ6TDUi4mU.O/m\\x3dsb_he,d/am\\x3dAAMCbAQ/d\\x3d1/rs\\x3dACT90oHRqO4y1Tn0VIAvndn1UG1WhY4Dyg\';\nsetTimeout(function(){var
        # b=document;var
        # a="SCRIPT";"application/xhtml+xml"===b.contentType&&(a=a.toLowerCase());a=b.createElement(a);a.src=u;google.timers&&google.timers.load&&google.tick&&google.tick("load","xjsls");document.body.appendChild(a)},0);})();(function(){window.google.xjsu=\'/xjs/_/js/k\\x3dxjs.hp.en_US.PXQ6TDUi4mU.O/m\\x3dsb_he,d/am\\x3dAAMCbAQ/d\\x3d1/rs\\x3dACT90oHRqO4y1Tn0VIAvndn1UG1WhY4Dyg\';})();function
        # _DumpException(e){throw e;}\nfunction
        # _F_installCss(c){}\n(function(){google.spjs=false;google.snet=true;google.em=[];google.emw=false;})();(function(){var
        # pmc=\'{\\x22d\\x22:{},\\x22sb_he\\x22:{\\x22agen\\x22:true,\\x22cgen\\x22:true,\\x22client\\x22:\\x22heirloom-hp\\x22,\\x22dh\\x22:true,\\x22dhqt\\x22:true,\\x22ds\\x22:\\x22\\x22,\\x22ffql\\x22:\\x22en\\x22,\\x22fl\\x22:true,\\x22host\\x22:\\x22google.com\\x22,\\x22isbh\\x22:28,\\x22jsonp\\x22:true,\\x22msgs\\x22:{\\x22cibl\\x22:\\x22Clear
        # Search\\x22,\\x22dym\\x22:\\x22Did you mean:\\x22,\\x22lcky\\x22:\\x22I\\\\u0026#39;m Feeling Lucky\\x22,\\x22lml\\x22:\\x22Learn
        # more\\x22,\\x22oskt\\x22:\\x22Input tools\\x22,\\x22psrc\\x22:\\x22This search was removed from your \\\\u003Ca
        # href\\x3d\\\\\\x22/history\\\\\\x22\\\\u003EWeb History\\\\u003C/a\\\\u003E\\x22,\\x22psrl\\x22:\\x22Remove\\x22,\\x22sbit\\x22:\\x22Search
        # by image\\x22,\\x22srch\\x22:\\x22Google
        # Search\\x22},\\x22ovr\\x22:{},\\x22pq\\x22:\\x22\\x22,\\x22refpd\\x22:true,\\x22rfs\\x22:[],\\x22sbpl\\x22:24,\\x22sbpr\\x22:24,\\x22scd\\x22:10,\\x22sce\\x22:5,\\x22stok\\x22:\\x22CvK-05rRUpC3EaVTn_-4OdAVsZI\\x22,\\x22uhde\\x22:false}}\';google.pmc=JSON.parse(pmc);})();</script>
        # </body></html>'
        # print(f.read())
        #print(f.readline())
        print(len(f.readlines())) # 9


if __name__ == '__main__':
    inspect_response_object()