import requests
import json
import boto3


def format_json(dictionary):
  
  response =  dictionary

  
  json_body =json.dumps(response, indent=2)
  
  return json_body




def coment_id_post(event, context):
 try:
  
  queryStringParameters = event['queryStringParameters']
  page_id = queryStringParameters["page_id"] # your page id, ex: '123456789'
  post_id = queryStringParameters["post_id"]# your post id, ex: '123456789'
  access_token = 'EAAWDC4qJVk8BO8Jd3HL6rExKr2PpUMWBeGJUc5iDgGiTYZC7twtZAlNsCD2ZBCVSIqfAZB3Oa6lThS35zZCbppfdYG9SigLTvwQHb7ubqV63sa54odI9t6Sx0lVQks3SVBZAPR2FCwVKVnZA9po3c1oO1tfiAnGgZBpmAZAumYK5UZAtzB4M0bJIDhkqSS1G58wtoZD' # your access token, from https://developers.facebook.com/tools/explorer/
  new_list=[]
  
  url = f'https://graph.facebook.com/v16.0/{page_id}_{post_id}/comments?access_token={access_token}'

  response = requests.request("GET", url)

  data = json.loads(response.text)

  for data_post in data.get("data"):
        nueva_data = {
            "user_id": data_post.get("from", {}).get("id", ""),
            "from": data_post.get("from", {}).get("name", ""),
            "message": data_post.get("message", "")
        }
        new_list.append(nueva_data)
  
  json_body =format_json(new_list)
  
  return {
  "statusCode": 200,
  "headers": {
    "Content-Type": "application/json",
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Headers': 'Content-Type,Authorization',
    'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
  },
  "body": json_body
  }
 except Exception as error_general:
  
  print(error_general)
  
  return {"data": "error"} 

#------------------------------------------------- full posts ------------------------------
def full_post(event, context):
 try:
  queryStringParameters = event['queryStringParameters'] 
  page_id = queryStringParameters["page_id"] # your page id, ex: '123456789'
  access_token = 'EAAWDC4qJVk8BO8Jd3HL6rExKr2PpUMWBeGJUc5iDgGiTYZC7twtZAlNsCD2ZBCVSIqfAZB3Oa6lThS35zZCbppfdYG9SigLTvwQHb7ubqV63sa54odI9t6Sx0lVQks3SVBZAPR2FCwVKVnZA9po3c1oO1tfiAnGgZBpmAZAumYK5UZAtzB4M0bJIDhkqSS1G58wtoZD' # your access token, from https://developers.facebook.com/tools/explorer/
  new_list=[]
  
  url = f'https://graph.facebook.com/v16.0/{page_id}/feed?pretty=0&limit=100&access_token={access_token}'

  response = requests.request("GET", url)

  data = json.loads(response.text)

  for data_post in data.get("data"):
        nueva_data = {
            "user_id": data_post.get("from", {}).get("id", ""),
            "from": data_post.get("from", {}).get("name", ""),
            "message": data_post.get("message", "")
        }
        new_list.append(nueva_data)
  
  json_body =format_json(new_list)
  
  return {
  "statusCode": 200,
  "headers": {
    "Content-Type": "application/json",
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Headers': 'Content-Type,Authorization',
    'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
  },
  "body": json_body
  }
  
 except Exception as error_general:
  
  print(error_general)
  
  return {"data": "error"} 



def raction_post(event, context):
 try:
  
  
  queryStringParameters = event['queryStringParameters']
  post_id = queryStringParameters["post_id"]# your post id, ex: '123456789'
  page_id = queryStringParameters["page_id"] # your page id, ex: '123456789'
  access_token = 'EAAWDC4qJVk8BO8Jd3HL6rExKr2PpUMWBeGJUc5iDgGiTYZC7twtZAlNsCD2ZBCVSIqfAZB3Oa6lThS35zZCbppfdYG9SigLTvwQHb7ubqV63sa54odI9t6Sx0lVQks3SVBZAPR2FCwVKVnZA9po3c1oO1tfiAnGgZBpmAZAumYK5UZAtzB4M0bJIDhkqSS1G58wtoZD' # your access token, from https://developers.facebook.com/tools/explorer/
  new_list=[]
  

  url = f'https://graph.facebook.com/v16.0/{page_id}_{post_id}?fields=reactions.summary(total_count)&access_token={access_token}'
  
  response = requests.request("GET", url)
   
  print(response)
  data = json.loads(response.text)
  print(data)
   
  # Acceder a la información dentro del diccionario
  summary_info = data.get('reactions', {}).get('summary', {})
  total_count = summary_info.get('total_count')

  # Crear un nuevo diccionario con los valores de 'summary' y 'total_count'
  nuevo_diccionario = {'summary': summary_info, 'total_reaction': total_count}

     
     
  
  json_body =format_json(nuevo_diccionario)
  
  return {
  "statusCode": 200,
  "headers": {
    "Content-Type": "application/json",
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Headers': 'Content-Type,Authorization',
    'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
  },
  "body": json_body
  }
  
 except Exception as e:
  
  print(e)
  
 

 #---------------- facebook
 
#  def enviar_mensaje(token_de_pagina, id_del_usuario, mensaje):
#     url = f"https://graph.facebook.com/v13.0/me/messages?access_token={token_de_pagina}"
#     payload = {
#         "recipient": {"id": id_del_usuario},
#         "message": {"text": mensaje}
#     }
#     response = requests.post(url, json=payload)
#     if response.status_code == 200:
#         print("Mensaje enviado con éxito")
#     else:
#         print(f"Error al enviar mensaje: {response.text}")

# if __name__ == "__main__":
#     token_de_pagina = "TU_TOKEN_DE_PAGINA"
#     id_del_usuario = "ID_DEL_USUARIO"
#     mensaje = "Hola, ¿cómo estás?"

#     enviar_mensaje(token_de_pagina, id_del_usuario, mensaje)