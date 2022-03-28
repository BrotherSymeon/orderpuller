"""code for pulling data from site"""


from requests.auth import HTTPBasicAuth 
import requests

def getReport():
    # we probably want to get these credentials from a config or something
    r = requests.post('https://httpbin.org/post', auth=HTTPBasicAuth('innocent', 'blahblah'))
    return r


if __name__ == "__main__":
    r = getReport()
    print(r.json)
