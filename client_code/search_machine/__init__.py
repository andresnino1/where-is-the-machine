from ._anvil_designer import search_machineTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

# notas to do
# cuando se busca le nombre del store, aparece la lista de las maquinas
# asignadas al store desde el inicio, pero si yo registro una maquina
# pero aun no se a que store pertenece, se registra a optopol anz
# pero luego al mover la ubicacion despues de estar registrada o de que
# entre a reparacion 

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
    self.input_store.text = ""
    self.drop_down_store.items=[]

  @handle("input_store", "change")
  def input_store_change(self, **event_args):
    self.info_card_2.visible=False
    self.info_card.visible=True
    self.repeating_panel_machines.visible=False
    self.repeating_panel_repairs.visible=False
    self.input_serial.text=""
    self.drop_down_store.items=[]

  @handle("input_store", "lost_focus")
  @handle("input_store", "pressed_enter")
  def input_store_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    store_name = self.input_store.text.strip()
    self.search_store(store_name) # function search the store name in database

  @handle("drop_down_store", "change")
  def drop_down_store_change(self, **event_args):
    self.repeating_panel_machines.visible=True
    store_name = self.drop_down_store.selected_value
    
    if store_name:
      machines_in_store = app_tables.machines.search(store_link=store_name) # list of all devices in the store
      is_workshop = store_name["is_workshop"] # check if the store is label like workshop
      if is_workshop:
        machines_in_workshop_location = app_tables.machines.search(current_location_link=store_name) # list of all devices currently located in the workshop location
        self.repeating_panel_machines.items=machines_in_workshop_location # this is workshop and will show all the devices at workshop"
      else:
        if machines_in_store:
          self.repeating_panel_machines.items=machines_in_store # if there is machines in the store, display them in repeating panel
        else:
          print ('the store doesnt have devices registered')



# =============== SEARCH SERIAL FUNCTION =====================

  def search_machine_serial(self, serial_search, **event_args):

    machines_list = app_tables.machines.get(serial=serial_search) # search the serial in database
    
    # IF serial DOESN'T EXIST
    if machines_list is None:
      self.info_card_2.visible=True
      self.info_card.visible=False
      self.message_1.text = "Machine is not in Data Base"

    # If serial number exists, the machine_list return an object with the complete row information
    # andt this is send to repeating_panel
    # the data sent is now in row_template_machines and row_template_repairs
    # the data will be display in the repeating panels using self.item[<column name>]
    else:
      self.info_card.visible=True
      self.repeating_panel_machines.visible=True
      self.repeating_panel_repairs.visible=True
      self.repeating_panel_machines.items=[machines_list]
      self.repeating_panel_repairs.items=machines_list['repairs_link']
     

  # ========================= Search Store Function ===========================

  def search_store(self, store_name, **event_args):
    query_store = app_tables.stores.search(store=q.ilike(f"%{store_name}%"))
    items = [(r['store'],r) for r in query_store]

    if items:
      self.drop_down_store.items = items
      self.drop_down_store_change()
    else:
      self.drop_down_store.items = []
      self.repeating_panel_machines.visible=False

    # if items:
    #   self.drop_down_store.selected_value = items[0][1]

    # Check if there is the store in the database
    # if items:
    #   if len(items) ==1:
    #     print('there is store in database')
    #     self.drop_down_store_change()
    #   else:
    #     self.drop_down_store.selected_value=items[0][1]
    # else:  
    #   print('no store to show')

    # If there is an EXACT MATCH in the query the function dropdown_store_chage is trigger manualy
    # To ensure the unique value in the list is selected.

 

