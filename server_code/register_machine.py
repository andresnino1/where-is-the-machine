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
@anvil.server.callable
def register_machine(serial, type):
  app_tables.machines.add_row(serial=serial, type_1=type)
  print('registro exitoso')

# this function converts the string data column to a link row data
# esta funcion convierte la columna con valores de texto y crea una columna nueva
# con valores con link a una tabla

@anvil.server.callable
def migratedata():
  for row in app_tables.machines.search():
    string_value = row['type'] # columna que tiene el valor string en la tabla original
    if string_value:
      linked_row = app_tables.machine_type.get(model=string_value) # encontrar el valor en la tabla que tiene el listado de los links a hacer
      if not linked_row:
        linked_row = app_tables.machine_type.add_row(model=string_value)
      row['type_1'] = linked_row
  print('migration finished')

  
  

  
       

  
