GET /names Route Design Recipe

_Copy this design recipe template to test-drive a plain-text Flask route._

## 1. Design the Route Signature

_Include the HTTP method, the path, and any query or body parameters._

```
# names route
GET /names?add=<string>
```

## 2. Create Examples as Tests

_Go through each route and write down one or more example responses._

_Remember to try out different parameter values._

_Include the status code and the response body._

```python
# GET /name?add=Eddie
#  Expected response (200 OK):
"""
 Alice, Julia, Karim, Eddie
"""

# GET /name?add=Eddie,Leo
#  Expected response (200 OK):
"""
 Alice, Eddie, Julia, Karim, Leo
"""
```

## 3. Test-drive the Route

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
"""
GET /names
Paramters:
    add: Eddie
  Expected response (200 OK):
  Alice, Eddie, Julia, Karim
"""
def test_get_names(web_client):
    response = web_client.get('/names?add=Eddie')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Alice, Eddie, Julia, Karim'

"""
GET /names
Paramters:
    add: Eddie,Leo
  Expected response (200 OK):
  Alice, Eddie, Julia, Karim, Leo
"""
def test_get_names(web_client):
    response = web_client.get('/names?add=Eddie,Leo')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Alice, Eddie, Julia, Karim, Leo'