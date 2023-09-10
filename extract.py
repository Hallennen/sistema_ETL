import pandas as pd
import requests, json
import openai

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


    return True if response.status_code == 200 else False




for user in  listaID:
    consulta_usuario(user)
    nomes.append(consulta.json()['name'])
    
gerar_news()    
update_user()
    










    # usersid = [i for id in listaID if (user := consulta_usuario(id)) is not None]
    # gerar_news(usersid)
    # # news = gerar_news(user)
    # print(usersid[user]["news"])
    # print(news)








# def update_user(user):
#   response = requests.put(f"{base_url}/users/{user['id']}", json=user)
#   return True if response.status_code == 200 else False

# for user in listaID:
#   success = update_user(user)
#   print(f"User {user['name']} updated? {success}!")


# print(json.dumps(usersid, indent=2))






# users = [user for id in users if (user := get_user(id)) is not None]
# print(json.dumps(users, indent=2))

    



