"""Pantry server user
    needed
    ------
        Define pantry.pantryId and pantry.basket with your own pantry id and basket, if you don't have any, go to https://getpantry.cloud/ to get one.
        
    get
    ---
        Get the data from a pantry basket

        get(PANTRY_ID, BASKET)

    set
    ---
        Set the data from a pantry basket

        set(VARIABLE, VALUE, PANTRY_ID, BASKET)
"""

#Importa http.client per poder conectar-se a internet i json per poder utilitzar les dades formulades en .json
import http.client
import json

#funció per obtenir el contingut
def get():
 conn = http.client.HTTPSConnection("getpantry.cloud")
 payload = ''
 headers = {
   'Content-Type': 'application/json'
 }
 conn.request("GET", "/apiv1/pantry/" + pantryId + "/basket/" + basket, payload, headers)
 res = conn.getresponse()
 data = res.read()
 return json.loads(data.decode("utf-8"))

#funció per reescriure contingut
def set(key, value):

    #definir la conneció
    conn = http.client.HTTPSConnection("getpantry.cloud")

    #definir les 'normes' de la conneció
    payload = json.dumps({
      key: value
    })
    headers = {
      'Content-Type': 'application/json'
    }

    #activar la conneció
    conn.request("PUT", "/apiv1/pantry/" + pantryId + "/basket/" + basket, payload, headers)


 
