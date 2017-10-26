# Under API v. 1

## Rating

REQUEST:

`GET /api/1/rating/{app}/{key}/{sessionid}/`
* app - applocation name (blog, event etc.)
* key - primary key fro app model (id)
* sessionid - user session cookies from browser

RESPONSE:

`{"is_vote": bool, "value": float, "total": int}`
* is_vote - voted current user to this app.key
* value - average rating current app.key
* total = totaly votes from this app.key
