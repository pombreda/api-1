Remix Advanced Scripting
===
Details here: https://github.com/canvasnetworks/api/wiki

Public API
===
See: api_example.py

Root
---
Root of the canv.as public api

Available endpoints are:

* /public_api/
* /public_api/users/
* /public_api/posts/
* /public_api/groups/

Posts
---
Posts endpoint of the canv.as public api

Request with an id parameter:

/public_api/posts/1qkx8

POST JSON in the following format:

POST /public_api/posts/
{"ids":["1qkx8","ma6fz"]}

Users
---
Users endpoint of the canv.as public api

Request with an id parameter:

/public_api/users/watermelonbot

POST JSON in the following format:

/public_api/users/
{"ids":["watermelonbot", "jeff"]}

User posts will be returned in pages, ordered newest to oldest. You can request posts beyond the initial range by POSTing JSON in the following format:

/public_api/users/
{"ids":[{"user":"watermelonbot","skip":100},"jeff"}

Groups
---
Groups endpoint of the canv.as public api

Request with an id parameter:
/public_api/funny

POST JSON in the following format:
{"ids":["funny","canvas"]}

Group posts will be returned in pages, ordered newest to oldest. You can request posts beyond the initial range by POSTing JSON in the following format:

/public_api/users/
{"ids":[{"group":"funny","skip":100},"canvas"}
