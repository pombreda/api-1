import json

import requests

# root documentations
url = 'https://canv.as/public_api/'
response = requests.get(url)
data = json.loads(response.text)

print "Root documentation"
print "=================="
print data['documentation']
print

# simple user example
url = 'https://canv.as/public_api/users/jeff'
response = requests.get(url)
data = json.loads(response.text)
postids = [x['id'] for x in data['posts']]

print "Simple User Example"
print "==================="
print "Username: " + data['user']
print "API Url: " + data['api_url']
print "Post IDs: {0}".format(postids)
print

# slightly more complex user example
url = 'https://canv.as/public_api/users/'
payload = {'ids': [{'user': 'jeff', 'skip': 10}]}
headers = {'content-type': 'application/json'}
response = requests.post(url, data=json.dumps(payload), headers=headers)
data = json.loads(response.text)
postids = [x['id'] for x in data['users'][0]['posts']]

print "User Paging Example"
print "==================="
print "Next Page of Post IDs: {0}".format(postids)
print

# simple posts example
url = 'https://canv.as/public_api/posts/1qkx8'
response = requests.get(url)
data = json.loads(response.text)

print "Simple Posts Example"
print "===================="
print "Caption: " + data['caption']
print "Replies: {0}".format(len(data['replies']))
print

# slightly more complex posts example
watermelonbot_reply_ids = [x['id'] for x in data['replies'][:5]]
url = 'https://canv.as/public_api/posts/'
payload = {'ids': watermelonbot_reply_ids}
headers = {'content-type': 'application/json'}
response = requests.post(url, data=json.dumps(payload), headers=headers)
data = json.loads(response.text)

print "Posts Example"
print "============="
print "Urls..."
for post in data['posts']:
    print " ... " + post['url']
print

# simple group example
url = 'https://canv.as/public_api/groups/funny'
response = requests.get(url)
data = json.loads(response.text)

print "Group Example"
print "============="
print "New posts in group: " + data['group']
for post in data['posts']:
    print " ... Title: " + post['title'] + " Url: " + post['url']
print

