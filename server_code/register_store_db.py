import anvil.secrets
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

# TODO chequear la funcionalidad de registro de clientes en la base de datos
# por ahora estuve chequeando que el sistema verificara si el nombre del store existe o no
# El sistema esta dejando registrar stores con nombres iguales si uno esta en minuscula o mayuscula
# hacer que el store sea unico asi esta en mayucula o minusculas

@anvil.server.callable
def register_store(store_name, store_address, state, store_phone, store_email,  store_contact_person):
  if not(is_store_in_db(store_name)):
    # print('store was not in db and now is register')
    app_tables.stores.add_row(store=store_name, store_address=store_address, state=state, store_phone=store_phone, store_email=store_email, contact_person=store_contact_person)
    return "ok"
  else:
    # print('store was already in db, so it was no register again')
    return "store is already in data base"
    
  

# ================ FUNCTION THAT CHECK IF THE STORE NAME IS ALREADY IN THE DB =============
def is_store_in_db(store_name):
  store_exists = any(app_tables.stores.search(store=store_name))
  if store_exists:
    # print('Store is in the DB')
    return(True)
  else:
    # print('Store is Not in DB')
    return(False)
