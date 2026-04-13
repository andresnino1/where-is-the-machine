import anvil.secrets
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
def register_store(store_name, store_address, state, store_contact_person, store_phone, store_email):
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