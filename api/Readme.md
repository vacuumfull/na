# Under API v. 1

## Rating

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


## Comments

REQUEST:

`GET /api/1/comment/{app}/{key}/{sessionid}/{offset}/`
* app - application name (blog, event etc.)
* key - primary key fro app model (id)
* sessionid - user session cookies from browser
* offset = offset in query select on database
