import requests
import json
import boto3

def tx_token(event, context):
 
 
 page_id = event.get("body", {}).get("page_id") # your page id, ex: '123456789'
 post_id = event.get("body", {}).get("post_id")# your post id, ex: '123456789'
 access_token = 'EAALtZCfEGouUBO0ZC9VXCLGSSV1dmHMZBE5W0IMqqZBygbD3YEnyScTn67tPA1uE5BapHRg3rKZAKr7CX85Sr0bZA4oPgXsjQc7YG4cre6yq4QT3mLZCVFq0u8aDsJgXFG6u4aFWZAJJ11ZCzKbvVYAJ4OXRSAcwulKIRpVDrGAdsJUsh1DbuKjcYflxkoH5krP0ZD' # your access token, from https://developers.facebook.com/tools/explorer/
 
 url = f'https://graph.facebook.com/v16.0/{page_id}_{post_id}/comments?access_token={access_token}'

 response = requests.request("GET", url)

 data = json.loads(response.text)
   
   
    
 return {"data": data} 
        