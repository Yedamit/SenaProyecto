
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
    """
    Convierte a python
    """
    n = None
    for i in range(len(arr) - 1, -1, -1):
        node = LinkedList(arr[i], n)
        n = node
    return n
     
#01:05 p. m. 19/05/2023

# --- cara

def heap_sort(input_list, field):
    """
    Alguna llave
    """
    range_start = int((input_list.size()-2)/2)
    for start in range(range_start, -1, -1):
        sift_down(input_list, field, start, input_list.size()-1)

    range_start = int(input_list.size()-1)
    for end_index in range(range_start, 0, -1):
        swap(input_list, end_index, 0)
        sift_down(input_list, field, 0, end_index - 1)
    return input_list


def swap(input_list, a, b):
    """
    Algun elemento
    """
    a_value = input_list.index(a)
    b_value = input_list.index(b)
    input_list.set_index(a, b_value)
    input_list.set_index(b, a_value)


def sift_down(input_list, field, start_index, end_index):
    """
    todo
    """
    root_index = start_index
    while True:
        child = root_index * 2 + 1
        if child > end_index:
            break
        if child + 1 <= end_index and input_list.index(child)[field] < input_list.index(child + 1)[field]:
            child += 1
        if input_list.index(root_index)[field] < input_list.index(child)[field]:
            swap(input_list, child, root_index)
            root_index = child
        else:
            break
        

# busqueda Binaria


def text_binary_search(input_list, field, query):
    """
    configuracion
    """
    low = 0
    high = input_list.size() -1
    query = make_text_searchable(query)
    while low <= high:
         mid = math.floor((low + high) /2) 
         if make_text_searchable(input_list.index(mid)[field]) > query:
            high = mid - 1
         elif  make_text_searchable(input_list.index(mid)[field]) > query:  
            low  = mid + 1
         else:
             return mid
    return -1        


def make_text_searchable(text):
    """
    movera los espacios
    """
    return text.lower ().replace(".", "")

# Numero de cuenta


def generate_account_number():
    
    """
    genera un unico nimero
    """
    prefix = "17172424"
    result = ""
    for _ in range(0, 8):
         random_number = random.randint(1,9)
         result += str(random_number)
    return prefix + result

# transaction
def perform_transaction(sender_number, receiver_number, amount):
     """
     dar 2 cuentas     
     """

     users = get_data()


     if sender_number not in users:
          print("si no cncuentra el numero de la cuenta: " + sender_number )

          return
     if receiver_number not in users:
        print("no se cnecontro con este numero: " + receiver_number)
        return
     
     if users[sender_number]["balance"] < amount:
          print ("el salndo no es sificiente")

     users[sender_number]["balance"] -= amount
     users[receiver_number]["balance"] += amount

     set_data(users)

     print("transferencia", amount, "$ de la cuenta",
           users[sender_number]["full_name"], "to", users[receiver_number]["Nombre completo"])
     
     
# Actulizar informacion


def update_information(account_number):


    """
   dar info 
    """

    users = get_data()
    
    print_horizontal_line()
    print("► 1 . Nombre Completo")
    print_horizontal_line()
    print("► 2 . Genero")

    print_horizontal_line()
    print("► 3 . Ciudad")

    print_horizontal_line()
    print("► 4 . Numero de Telefono")
    print_horizontal_line()
    command = int(input("Que vas a cambiar?"))

    print_horizontal_line()
    if command == 1:
        new_game = input(" nuevo nombre completo: ")
        users[account_number]["Nombre completo"] = new_game
    if command == 2:
        new_gender = input(" nuevo Genero: ")
        users[account_number]["Genero"] = new_gender
    if command == 3:
        new_city = input(" nueva ciudad: ")
        users[account_number]["ciudad"] = new_city
    if command == 4:
        new_phone_number = input(" nuevo numero de telefono: ")
        users[account_number]["Numero_Telfono"] = new_phone_number   

    set_data(users)
    clean_terminal_screen()
    display_account_information_by_given_account_number(account_number)


 




# crear un nuevo usuario

def create_new_user(full_name, balance, gender, city, phone_numer):



    """
    crear usuario con nueva informacion
    """
    users = get_data()
    date = datetime.today().srttime('%Y-%m-%d')
    account_number = generate_account_number() 
    users[account_number] = {
        "Nombre Completo" : full_name,
        "Genero" : gender,
        "saldo" : balance,
        "fecha cracion cuenta" : date,
        "ciudad" : city,
        "numero de telefono" : phone_numer
    }

    set_data(users) 
    display_account_information_by_given_account_number(account_number)
    

    
    


