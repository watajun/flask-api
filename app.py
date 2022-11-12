import requests

res = requests.get("https://zipcloud.ibsnet.co.jp/api/search?zipcode=7830060")

# print(res.text["status"])
# print(res.json()["status"])
# print(res.json()["results"][0]["prefcode"])

# 短縮系
json = res.json()
print(json()["results"][0]["prefcode"])
