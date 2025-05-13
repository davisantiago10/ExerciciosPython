import requests
url = "https://www.pudim.com.br/"
try:
    op = requests.get(url).status_code
except:
    print('O site não está acessível')
else:
    print('O site está acessível')
