
def check_params_urls(url):
    contador = 0
    for i in url:
        if i == "=":
            contador +=1

    print(f"La URL {url} contiene {contador} parámetros")

query = "https://github.com/ronnyg2121?tab=repositories"
check_params_urls(query)