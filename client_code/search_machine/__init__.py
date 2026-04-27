from ._anvil_designer import search_machineTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

# notas to do

class search_machine(search_machineTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.info_card_2.visible=False

  @handle("input_serial", "lost_focus")
  @handle("input_serial", "pressed_enter")
  def input_serial_pressed_enter(self, **event_args):
    serial_search = self.input_serial.text.strip()
    if serial_search != "":
      self.search_machine_serial(serial_search) # function that search machine serial

  @handle("input_serial", "change")
  def input_serial_focus(self, **event_args):
    self.info_card_2.visible=False
    self.info_card.visible=True
    self.repeating_panel_machines.visible=False
    self.repeating_panel_repairs.visible=False


# =============== SEARCH SERIAL FUNCTION =====================

  def search_machine_serial(self, serial_search, **event_args):

    machines_list = app_tables.machines.get(serial=serial_search) # search the serial in database
    
    # machines_list return an object with the complete row information
    # and this object is send to repeating panel machines, so when open
    # the form RowTemplate1 the information will be recovered using self.item['name of column']
   
    # IF serial DOESN'T EXIST
    if machines_list == None:
      self.info_card_2.visible=True
      self.info_card.visible=False
      self.message_1.text = "Machine is not in Data Base"

    # If serial number exists, the machine_list is send to repeating_panel
    # the data sent is now in row_template_machines and row_template_repairs
    # the data will be display in the repeating panels using self.item[<column name>]
    else:
      self.info_card.visible=True
      self.repeating_panel_machines.visible=True
      self.repeating_panel_repairs.visible=True
      self.repeating_panel_machines.items=[machines_list]
      self.repeating_panel_repairs.items=machines_list['repairs_link']
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

 
 
