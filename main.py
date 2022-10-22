import json

import requests

r = requests.get("https://cataas.com/cat?json=true")
data = json.loads(r.text)

print(data["url"])