# Under API v. 1

## Rating
### Get ratings

REQUEST:

`GET /api/1/rating/{app}/{key}/{sessionid}/`
* app - application name (blog, event etc.)
* key - primary key fro app model (id)
* sessionid - user session cookies from browser

RESPONSE:

`{"is_vote": bool, "value": float, "total": int}`
* is_vote - voted current user to this app.key
* value - average rating current app.key
* total = totaly votes from this app.key

### Set and update rating

REQUEST:

`POST /api/1/vote/`
params:

* app - application name (blog, event etc.)
* key - primary key fro app model (id)
* vote - integer vote number (0..10) if > 10 then vote set 0
* sessionid - user session cookies from browser

RESPONSE:

`{"is_vote": bool, "value": float, "total": int}`
* is_vote - voted current user to this app.key
* value - average rating current app.key
* total = totaly votes from this app.key

`{"error": "error string"}`


## Comments
### Get comments

REQUEST:

`GET /api/1/comment/{app}/{key}/{sessionid}/{offset}/`
* app - application name (blog, event etc.)
* key - primary key fro app model (id)
* sessionid - user session cookies from browser
* offset = offset in query select on database

RESPONSE:

`{"user": bool, "content": float, "datetime": str}`
* is_vote - voted current user to this app.key
* value - average rating current app.key
* total = totaly votes from this app.key

### Send comments

REQUEST:

`POST /api/1/send/`
params:

* app - application name (blog, event etc.)
* key - primary key fro app model (id)
* content - text content (must be not empty and less 250 chars)
* sessionid - user session cookies from browser

RESPONSE:

`{"success": "Comment success append"}`

`{"error": "error string"}`


### Send messages

REQUEST:

`POST /api/1/messages/`
params:

* login - getter login
* content - message content 
* sessionid - user session cookies from browser

RESPONSE:

`{"success": "Message success append"}`

`{"error": "error string"}`