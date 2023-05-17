
# ─── Importar ────────────────────────────────────────────────────────────────────

import match
import json
import os
import random
from datetime import datetime
from os.path import exist

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

#convierte string json en objeto de python
return json.loads(data)



