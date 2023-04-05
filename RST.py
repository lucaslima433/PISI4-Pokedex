import requests
import base64

with open('input/images.jpeg', 'rb') as f:
    imagem_bytes = f.read()

imagem_base64 = base64.b64encode(imagem_bytes).decode('utf-8')

payload = {
    'body': imagem_base64
}

url = 'https://yhdf1b8upg.execute-api.us-east-1.amazonaws.com/pikomonstage'
response = requests.post(url, json=payload)

print("Status Code:", response.status_code)

if response.text == '[]':
    print("Pokemon não reconhecido")
else:
    print("Pokemon:", response.text.replace('["', "").replace('"]', ""))