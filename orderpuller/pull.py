"""code for pulling data from site"""


import requests.auth import HTTPBasicAuth 


def getReport():
    # we probably want to get these credentials from a config or something
    r = requests.post('https:htpbin.org/post', auth=HTTPBasicAuth('innocent', 'blahblah'))
    return r.data
