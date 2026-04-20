from ._anvil_designer import register_machineTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

#TODO
# 

class register_machine(register_machineTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.button_register_store.visible = False
    self.dropdown_machine_type.visible = False
    self.input_store.visible = False
    self.label_type.visible = False
    self.label_store.visible = False
    self.dropdown_store.visible = False
    self.button_register_machine.visible = False
    self.label_message.visible = False
    self.label_udi.visible = False
    self.input_udi.visible = False
    
  
# ======================  Input Serial Change Function ==============================

  def input_serial_change(self, **event_args):
    self.label_type.visible = False
    self.dropdown_machine_type.visible = False
    self.label_store.visible = False
    self.input_store.visible = False
    self.dropdown_store.visible = False
    self.button_register_store.visible = False
    self.button_register_machine.visible = False
    self.label_message.visible = False
    self.label_udi.visible = False
    self.input_udi.visible = False

# ======================  Input Serial Pressed Enter ==============================
  
  def input_serial_pressed_enter(self, **event_args):
    serial_search = self.input_serial.text.strip()
    if serial_search != "":
      self.search_machine_serial(serial_search) # function that search machine serial
    
# ======================  Input Serial Lost Focus ============================== 
  def input_serial_lost_focus(self, **event_args):
    serial_search = self.input_serial.text.strip()
    if serial_search != "":
      self.search_machine_serial(serial_search) # function that search machine serial


# ================ DropDown Machine Type Show Function ==================

  def dropdown_machine_type_show(self, **event_args):
    self.dropdown_machine_type.items = [(r["model"],r) for r in app_tables.machine_type.search()]
    self.dropdown_machine_type.include_placeholder=True
    self.dropdown_machine_type.placeholder="Select a Machine Model"

  
  # ================ DropDown Mahine Type Change Function ==============
  
  def dropdown_machine_type_change(self, **event_args):
    #   """This method is called when an item is selected"""
    machine_type = self.dropdown_machine_type.selected_value
    if machine_type is None:
      print("select machine type")
      self.label_store.visible=False
      self.input_store.visible=False
      self.dropdown_store.visible=False
      self.button_register_store.visible=False
      self.button_register_machine.visible=False
          
    else:
      self.label_store.visible=True
      self.input_store.visible=True
      self.dropdown_store.visible=True
      return(print(machine_type["model"]))
    


  
# =================== Input Store Change Function ==========================
  
  def input_store_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    store_name = self.input_store.text.strip()
    self.button_register_machine.visible=False
  
    if len(store_name) > 1:
      self.search_store(store_name) # function search the store name in database
      
  
# ================ DropDown Store Change Function ==============

  def dropdown_store_change(self, **event_args):
    #   """This method is called when an item is selected"""
    store_name = self.dropdown_store.selected_value
    self.button_register_machine.visible=False
    if store_name:
      # if there is a store in the database the register machine button is enabled
      self.button_register_machine.visible=True
      print(store_name["store"])     
      

# ===================================== SEARCH SERIAL FUNCTION ============================================
    
  def search_machine_serial(self, serial_search, **event_args):
    
    query_serial = app_tables.machines.search(serial=serial_search) # search the serial in database
      
    # IF serial DOESN'T EXIST - then the fields are enabled to register the new machine
    if [(s['serial'],s) for s in query_serial] == []:
      self.label_udi.visible = True
      self.input_udi.visible = True
      self.label_type.visible = True
      self.dropdown_machine_type.visible = True
      self.label_store.visible = False
      self.input_store.visible = False
      self.dropdown_store.visible = False
      self.button_register_store.visible = False
      self.button_register_machine.visible = False
      self.label_message.visible = False

      # IF serial exists, the fields are DISABLED, so the user can not register a duplicated
    else:
      self.label_message.visible = True
      self.label_message.background = "yellow"
      self.label_message.text = "This Machine is already in the Data Base"
      self.label_type.visible = False
      self.dropdown_machine_type.visible = False
      self.label_udi.visible = False
      self.input_udi.visible = False
      self.label_store.visible = False
      self.input_store.visible = False
      self.dropdown_store.visible = False
      self.button_register_store.visible = False
      self.button_register_machine.visible = False

# ========================================= Search Store Function ===========================
  
  def search_store(self, store_name, **event_args):
    query_store = app_tables.stores.search(store=q.ilike(f"%{store_name}%"))
    self.dropdown_store.items = [(r['store'],r) for r in query_store]
    self.dropdown_store.visible = True
    self.button_register_machine.visible = False
    self.button_register_store.visible = False

    # If there is NOT an store in de database the REGISTER STORE BUTTON IS ENABLED
    if [(r['store'],r) for r in query_store] == []:
      self.dropdown_store.visible = False
      self.button_register_machine.visible = False
      self.button_register_store.visible = True

    # If there is an EXACT MATCH in the query the function dropdown_store_chage is trigger manualy
    # To ensure the unique value in the list is selected.
    if len([(r['store'],r) for r in query_store]) ==1:
      self.dropdown_store_change()


  # =============== Button Register Machine Click Function ==============

  def button_register_machine_click(self, **event_args):
    """This method is called when the button is clicked"""
    serial=self.input_serial.text.strip()
    udi=self.input
    machine_type=self.dropdown_machine_type.selected_value
    store_name = self.dropdown_store.selected_value # return the row from stores table

    new_machine = anvil.server.call('register_machine', serial, machine_type["model"], store_name["store"])
    if new_machine == 'ok':
      self.label_serial.visible=False
      self.input_serial.visible=False
      self.label_type.visible=False
      self.dropdown_machine_type.visible=False
      self.label_store.visible=False
      self.input_store.visible=False
      self.dropdown_store.visible=False
      self.button_register_store.visible=False
      self.button_register_machine.visible=False
      self.label_message.visible = True
      self.label_message.background = "green"
      self.label_message.text = "Machine Successfuly Registered !!"
    else:
      self.label_serial.visible=False
      self.input_serial.visible=False
      self.label_message.visible = True
      self.label_message.background = "red"
      self.label_message.text = "Machine Not Registered - Try Again!!"
      
        
  def new_store_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('register_store')


  def home_link_click(self, **event_args):
    #   """This method is called when the link is clicked"""
    open_form('register_machine')


  def button_register_store_click(self, **event_args):
    """This method is called when the button is clicked"""
    new_store_name = self.input_store.text
    open_form('register_store', new_store_name)



 
 





  
    


      
      