import json
import requests
import base64
import time

# Base URL for WordPress REST API
url = "https://lightslategrey-wombat-917497.hostingersite.com/wp-admin/"

# Credentials
user = "meyerD"
password = 'a(mvg(fV7C$xLCtczev$&hAw'
creds = user + ":" + password

# Encode credentials in base64 for Basic Authentication
token = base64.b64encode(creds.encode())

# Headers with Basic Authorization
header = {"Authorization": "Basic " + token.decode('utf-8')}

# Media upload
with open('IMG-20240818-WA0002.jpg', "rb") as img_file:
    media = {
        "file": img_file,
        "caption": "Api Image",
        "description": "Api Python encryption"
    }
    response = requests.post(url + 'media', headers=header, files=media)
    # Check for successful media upload
    if response.status_code == 201:
        ImageUrl = str(json.loads(response.content)['source_url'])
    else:
        print("Error uploading media:", response.status_code, response.content)
        exit()

# Post creation
post = {
    'date': time.strftime("%Y-%m-%dT%H:%M:%S"),
    'title': "API Post",
    'content': f"A simple WordPress API post! <img src='{ImageUrl}' />",
    'status': 'publish'
}

# Create a new post
response = requests.post(url + 'posts', headers=header, json=post)

# Check for successful post creation
if response.status_code == 201:
    print("Post created successfully:", response.json())
else:
    print("Error creating post:", response.status_code, response.content)
