import requests, json


base_url = 'https://sdw-2023-prd.up.railway.app'
listaID = ['1670','1671','1672']
api_key =  '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'
nomes = []
noticias =[]

def consulta_usuario(user):
    global consulta
    consulta = requests.get(f'{base_url}/users/{user}')
    return consulta.json() if consulta.status_code == 200 else None

users = [user for id in listaID if (user := consulta_usuario(id)) is not None]
print(json.dumps(users, indent=2))

def gerar_news():
    i=0
    for nome in nomes:
        texto = f'Invista hoje {nome}, garanta o futuro de amanha'
        noticias.append(texto)
    
        users[i]['news'].append(
    {
      "description": texto
    })
        i +=1

    return texto


def update_user():
    i= 0
    for id in listaID:
        response = requests.put(f"{base_url}/users/{id}", json=users[i])
        i +=1


    return print(True if response.status_code == 200 else False)




for user in  listaID:
    consulta_usuario(user)
    nomes.append(consulta.json()['name'])
    
gerar_news()    
update_user()
print('sistema finalizado')
