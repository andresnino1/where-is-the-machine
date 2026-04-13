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
def register_store(store_name, store_address, state, store_phone, store_email,  store_contact_person):
  app_tables.stores.add_row(store=store_name, store_address=store_address, state=state, store_phone=store_phone, store_email=store_email, contact_person=store_contact_person)
  print('store register successfuly')
  return('ok')
  