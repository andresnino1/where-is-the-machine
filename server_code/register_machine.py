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

@anvil.server.callable
def copy_type(s):
  machine_row = app_tables.machines.get(serial=s)
  id = machine_row.
  print(id)
  
  

  
       

  
