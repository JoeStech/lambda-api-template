import requests

payload = {
    "foo": "bar"
}
        

r = requests.post('', json=payload)

print(r.text)