import urllib.request

try:
    site = urllib.request.urlopen("http://www.pudim.com.br")
except urllib.error.URLError:
    print("0 site Pudim não está acessível no momento.")
else:
    print("Consegui acessar o site Pudim com sucesso!")
