import requests

url = 'https://www.nike.com/kr/ko_kr/w/xg/fw/nsw/air-force-1-collection'

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36"
}

r = requests.get(url, headers=headers)


print(r)
print(r.request.headers)
print(r.text)
