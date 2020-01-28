import requests
import pytest # have to install via command "pip3 install -U pytest"
import json

def test_health_check():
    r = requests.get('http://localhost:8085')
    assert(r.status_code == 404)

def test_helloworld():
    r = requests.get("http://localhost:8085/hello-world").text
    data = json.loads(r)
    print(data['content']+"wtf")
    assert(data['content']=="Fail, Stranger!")
# 1. Add two more tests here of your choice. I will explain the API.
#    Make sure to verify the necessary info, e.g., status code, response data.
# 2. Add "pytest" as integration testing script as part of Github Actions CI workflow (you've done this before!)
