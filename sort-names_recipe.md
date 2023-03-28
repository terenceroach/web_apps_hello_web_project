POST sort-names Route Design Recipe

_Copy this design recipe template to test-drive a plain-text Flask route._

## 1. Design the Route Signature

_Include the HTTP method, the path, and any query or body parameters._

```
# sort-names route
POST /sort-names
  names list, comma separated string
```

## 2. Create Examples as Tests

_Go through each route and write down one or more example responses._

_Remember to try out different parameter values._

_Include the status code and the response body._

```python
# POST /sort-names
#  Parameters:
#    names: ["Joe,Alice,Zoe,Julia,Kieran"]
#  Expected status_code (200 OK):
"""
"Alice,Joe,Jilia,Kieran,Zoe"
"""

# POST /submit
#  Parameters: none
#  Expected response (400 Bad Request):
"""
Please provide a list of names
"""
```

## 3. Test-drive the Route

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
"""
POST /sort-names
  Parameters:
    names: ["Joe,Alice,Zoe,Julia,Kieran"]
  Expected response (200 OK):
  "Alice,Joe,Jilia,Kieran,Zoe"
"""
def test_post_sort-names(web_client):
    response = web_client.post('/sort-names', data={'names': ["Joe,Alice,Zoe,Julia,Kieran"]})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Alice,Joe,Jilia,Kieran,Zoe"

"""
POST /sort-names
  Parameters:
    nnone
  Expected response (400 Bad Request):
  "Please provide a list of names"
"""
def test_post_sort-names(web_client):
    response = web_client.post('/sort-names')
    assert response.status_code == 400
    assert response.data.decode('utf-8') == "Please provide a list of names"
```