import anvil.secrets
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import anvil.secrets



# ==================== REGISTER A MACHINE IN DB ==========================
@anvil.server.callable
def register_machine(serial, machine_type, store_name):
  if not(is_serial_in_db(serial)):
    # los campos type_link y store_link son campos relacionados entre tablas
    # y se debe obtener TODA LA FILA con GET buscando el modelo y nombre de la tienda
    # luego se agrega la nueva fila ADD_ROW pasando los parametros de las tablas que estan relacionadas 
    type = app_tables.machine_type.get(model=str(machine_type)) # este es un link a tabla MACHINE TYPE (debe ser string)
    store= app_tables.stores.get(store=str(store_name)) # este es un link a tabla STORES (debe ser string)
    print(type)
    print(store)
    app_tables.machines.add_row(serial=serial, type_link=type, store_link=store)
    print('registro exitoso')
    return('ok')
  else:
    print('machine was not registered')
    return('fail')

# ================ FUNCTION THAT CHECK IF THE MACHINE IS ALREADY IN THE DB =============
def is_serial_in_db(serial):
  query_serial = app_tables.machines.search(serial=serial)
  if [(s['serial'],s) for s in query_serial] == []:
    print('machine is not in the DB')
    return(False)
  else:
    print('machine is already in DB')
    return(True)


# ================ FUNCTION THAT SHOW MACHINE INFORMATION API ===========================
# Esta funcion usa la clase anvil.server.AppResponder que envia el diccionario "data" con la 
# informacion para ser mostrada en el formulaio "machine_information"
# la API con la ruta <url app>/machine/xxxx sera la ruta a la que se dirigira 

@anvil.server.route("/machine/:serial")
def get_machine(serial):
  query_serial = app_tables.machines.get(serial=serial)
  if query_serial is not None:
    responter_data = anvil.server.AppResponder(data={"info_serial":query_serial["serial"], "info_type":query_serial["type"], "info_current_location":query_serial["store"]})
    return responter_data.load_form('machine_information')
  else:
    return anvil.server.HttpResponse(404, "No Serial Number")
    


# ================== FUNCTION TO LOGIN ============================
# This function is a momentary login until the user login is implemented

@anvil.server.callable
def check_password(password):
  momentary_password = anvil.secrets.get_secret('momentary_password')
  if momentary_password == password:
    return True
  else:
    return False
  
  
  



# # =============== FUNCTION THAT CHECK IF THE STORE IS ALREADY IN THE DB ==============
# def is_store_in_db(store):
#   query_store = app_tables.stores.search(store=store)
#   if [(r['store'],r) for r in query_store] == []:
#     print("store is not in DB")
#     return(False)
#   else:
#     print('store is already in DB')
#     return(True)


  
  
    
  #query_serial = app_tables.machines.search(serial=serial_search)
  


# this function converts the string data column to a link row data
# esta funcion convierte la columna con valores de texto y crea una columna nueva
# con valores con link a una tabla



@anvil.server.callable
def migratedata():
  for row in app_tables.transfers.search():
    string_value = row['serial'] # columna que tiene el valor string en la tabla original
    if string_value:
      linked_row = app_tables.machines.get(serial=string_value) # encontrar el valor en la tabla a donde estaran los links
      if not linked_row:
        linked_row = app_tables.machines.add_row(serial=string_value) # si no existe el valor se crea una fila con el nuevo texto como link
      row['serial_link'] = linked_row  # en esta columna se guardaran los textos convertirdos a links
  print('migration finished')

# this function remove the .0 extra zero in a column
@anvil.server.callable
def clean_zeros():
  for row in app_tables.transfers.search():  # Replace with your actual table name
        value = row['serial']  # Replace with your actual column name
        
        if isinstance(value, str) and value.endswith(".0"):
            row['serial'] = value[:-2]  # Remove last two characters
  print('end of cleaning')


  
       

  
