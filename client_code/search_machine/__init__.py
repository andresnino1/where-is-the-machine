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
    self.message_1.visible = False

    # Any code you write here will run before the form opens.


  @handle("input_serial", "lost_focus")
  @handle("input_serial", "pressed_enter")
  def input_serial_pressed_enter(self, **event_args):
    serial_search = self.input_serial.text.strip()
    if serial_search != "":
      self.search_machine_serial(serial_search) # function that search machine serial

  @handle("input_serial", "change")
  def input_serial_focus(self, **event_args):
    self.message_1.visible=False
    self.data_grid_1.visible=True


# =============== SEARCH SERIAL FUNCTION =====================

  def search_machine_serial(self, serial_search, **event_args):

    machines_list = app_tables.machines.search(serial=serial_search) # search the serial in database
    self.repeating_panel_machines.items=machines_list
    # machines_list return an object with the complete row information
    # and this object is send to repeating panel machines, so when open
    # the form RowTemplate1 the information will be recovered using self.item['name of column']
    
    # IF serial DOESN'T EXIST - then the fields are enabled to register the new machine
    if list(machines_list) == []:
      self.data_grid_1.visible=False
      self.message_1.visible=True
      self.message_1.text = "Machine is not in Data Base"
      # self.repeating_panel_machines.items=["No Serial Number in DB"]
      # IF serial exists, the fields are DISABLED, so the user can not register a duplicated



    #   query_store = app_tables.stores.search(store=q.ilike(f"%{store_name}%"))
    # store_list = [r['store'] for r in query_store]
    # self.store_name_repeating_panel.items = store_list
    # self.data_grid_store_name.visible=True

    # # If there is NOT an store in de database the REGISTER STORE BUTTON IS ENABLED
    # if store_list == []:
    #   self.store_name_repeating_panel.items=['Store Is Not In Data Base']
    #   self.data_grid_store_name.visible=True

 
 
