import urllib
from urllib import parse
from urllib import request


url = 'http://127.0.0.1:5000/catchassert'
data = urllib.parse.urlencode({'name' : 'joe', 'age'  : '10'})
data = data.encode('ascii')
req = urllib.request.Request(url, data)
response = urllib.request.urlopen(req)
text=response.read().decode("utf-8", "strict")
print(text)