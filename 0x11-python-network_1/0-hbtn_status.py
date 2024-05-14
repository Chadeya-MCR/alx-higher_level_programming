import urllib.request

url = 'https://alx-intranet.hbtn.io/status'

with urllib.request.urlopen(url) as response:
    body = response.read().decode('utf-8')

print("- type: {}".format(type(body)))
print("- content: {}".format(body))

