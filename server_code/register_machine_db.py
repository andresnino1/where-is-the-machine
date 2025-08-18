import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# ==================== REGISTER A MACHINE IN DB ==========================
@anvil.server.callable
def register_machine(serial, type, store):
  
  app_tables.machines.add_row(serial=serial, type_link=type, store_link=store)
  print('registro exitoso')
  return('ok')

# ================ FUNCTION THAT CHECK IF THE MACHINE IS ALREADY IN THE DB =============
def is_serial_in_db(serial):
  query_serial = app_tables.machines.search(serial=serial)
  if [(s['serial'],s) for s in query_serial] == []:
    print('machine is not in the DB')
    return(False)
  else:
    print('machine is already in DB')
    return(True)
    
    
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


  
       

  
