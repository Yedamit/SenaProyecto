
# ─── Importar ────────────────────────────────────────────────────────────────────

import math
import json
import os
import random
from datetime import datetime
from os.path import exists

# ─── Constantes ────────────────────────────────────────────────────────────────────

FILE_PATH =  "bank.json"   
# ─── Date Base ────────────────────────────────────────────────────────────────────

def get_data ():
    """
    mira la info del data
    """
    # Si no hay fila vacia
    if not exists(FILE_PATH):
            return {}
    f = open(FILE_PATH, "r")
    data = f.read()
    return json.loads(data)

#convierte string json en objeto de python
    return json.loads(data)

def set_data(data):
      """
Escribe la informacion den el cachivo del data
      """
      f = open(FILE_PATH, "w")
      json_data = json.dumps(data)
      f.write(json_data)



def get_users_as_list():
    """
    Esta funcion carga la informacion del usuario y la convierte en 
      enl diccionario
    """
    result = []
    users = get_data()
    for user_account_number in users:
        user_data = users[user_account_number]
        user_data["account_number"] = user_account_number
        result.append(user_data)
    results_as_ll = list_to_linked_list(result)
    return results_as_ll






# ─── LINKED LIST ────────────────────────────────────────────────────────────────

class LinkedList:
     """""
Modo de lista
     """""
     def __init__(self, _value, _next):
          "Crear modo con valores en el siguiente objetivo"
          self.value= _value
          self.next= _next

     def index(self, index):
          "Igual a a{i},  es a[i] index"
          if index == 0:
               return self.value
          else:
               if self.next == None:
                    return None
               else:
                    return self.next.index(index -1)
               
     def set_index(self, index, value):
          
          "igual a a = valor, es simirar"
          if index == 0:
               return self.value
          else:
               if self.next == None:
                    return None
               else:
                    return self.next.index(index -1)
               
     def set_index(self, index, value):
          "igual a a = valor, es simirar"
          if index == 0:
               self.value = value
          else:
               self.next.set_index(index - 1, value)     
     def size(self):
          "Igual a len (a)  tamaño a"

          if self.next == None:
               return 1
          else:
               return 1 + self.next.size()
          
     def append(self, x):
        """
        nuevo nudo
        """
        if self.next == None:
            self.next = LinkedList(x, None)
        else:
            self.next.append(x)
     

     

     def list_to_linked_list(arr):
          "pasa python a listo de linkeaslsit"

          n = None
          for i in range(len(arr) -1, -1 , -1):
               node = LinkedList(arr[i], n)
               n = node 
          return n
     
#01:05 p. m. 19/05/2023