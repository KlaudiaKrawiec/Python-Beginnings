import urllib.request
import urllib.parse

data = {}
data['name'] = 'Somebody Here'
data['location'] = 'Northampton'
data['language'] = 'Python'
url_values = urllib.parse.urlencode(data)
print(url_values)  # The order may differ from below.  
url = 'http://api.nbp.pl/api/exchangerates/tables/{A}/'
full_url = url + '?' + url_values
data = urllib.request.urlopen(full_url)




