from ._anvil_designer import search_machineTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

# notas to do
# implementar en el formulario que los campos no este activos si el serial existe
# esto para que no haya la opcion de agregar el mismo serial


class search_machine(search_machineTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.



  @handle("input_serial", "pressed_enter")
  def input_serial_pressed_enter(self, **event_args):
    serial_search = self.input_serial.text.strip()
    if serial_search != "":
      self.search_machine_serial(serial_search) # function that search machine serial


# =============== SEARCH SERIAL FUNCTION =====================

def search_machine_serial(self, serial_search, **event_args):

  query_serial = app_tables.machines.search(serial=serial_search) # search the serial in database

  # IF serial DOESN'T EXIST - then the fields are enabled to register the new machine
  if [(s['serial'],s) for s in query_serial] == []:
    print("Machine is not in DB")
    # IF serial exists, the fields are DISABLED, so the user can not register a duplicated
  else:
    print("Machine IS IN db")