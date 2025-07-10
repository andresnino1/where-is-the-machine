from ._anvil_designer import register_machineTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

#TODO
# - implementar que se debe seleccionar un tipo de machine
# si se deja en blanco debe indicarse con un mensaje
# arreglar la busqueda de STORE y autocompletar el dropdown menu

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
  
# ======================  Input Serial Change Function ==============================
  def input_serial_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    serial_search = self.input_serial.text.strip()
    
    if len(serial_search) > 2:
      self.search_machine_serial(serial_search) # function that search machine serial

    else:
      # si el serial es menor que 2 digitos mantiene todos los campos ocultos
        self.label_type.visible = False
        self.dropdown_machine_type.visible = False
        self.label_store.visible = False
        self.input_store.visible = False
        self.dropdown_store.visible = False
        self.button_register_store.visible = False
        self.button_register_machine.visible = False
        self.label_message.visible = False


# ================ DropDown Machine Type Show Function ==================

  def dropdown_machine_type_show(self, **event_args):
    """This method is called when the DropDown is shown on the screen"""
    self.dropdown_machine_type.items = [(r["model"],r) for r in app_tables.machine_type.search()]
    self.dropdown_machine_type.include_placeholder=True
    self.dropdown_machine_type.placeholder="Select a Machine Model"
    # self.dropdown_machine_type.selected_value=""

  
  # ================ DropDown Mahine Type Change Function ==============
  
  def dropdown_machine_type_change(self, **event_args):
    #   """This method is called when an item is selected"""
    machine_type = self.dropdown_machine_type.selected_value
    if machine_type is None:
      print("select machine type")
      # TODO: Evaluate when the user don't select a machine type
    # return(machine_type)
    print(machine_type)
    


  
# =================== Input Store Change Function ==========================
  
  def input_store_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    store_name = self.input_store.text.strip()
  
    if len(store_name) > 1:
      self.search_store(store_name) # function search the store name in database
      
  
# ================ DropDown Store Change Function ==============

  def dropdown_store_change(self, **event_args):
    #   """This method is called when an item is selected"""
    store_name = self.dropdown_store.selected_value
    # if store_name is None:
    #   print("select machine type")
    #   # TODO: Evaluate when the user don't select a machine type
    print(store_name[store])     



  
# =============== Button Register Machine Click Function ==============
      
  def button_register_machine_click(self, **event_args):
    """This method is called when the button is clicked"""
    find_serial = app_tables.machines.get(serial=self.input_serial.text)
    if find_serial is not None:
      # Machine exists in database

      print ('serial si existe')
    else:
      # Machine is not in database -- need to be registered
      print ('machine is not in database.. call server here')
      # anvil.server.call('register_machine', self.input_serial.text, self.dropdown_machine_type.selected_value)


  def home_link_click(self, **event_args):
  #   """This method is called when the link is clicked"""
  #   open_form('register_machine')
    pass


# ===================================== SEARCH SERIAL FUNCTION ============================================
    
  def search_machine_serial(self, serial_search, **event_args):
    
    query_serial = app_tables.machines.search(serial=serial_search) # search the serial in database
    self.label_type.visible = False
    self.dropdown_machine_type.visible = False
    self.label_store.visible = False
    self.input_store.visible = False
    self.dropdown_store.visible = False
    self.button_register_store.visible = False
    self.button_register_machine.visible = False
    self.label_message.visible = False

    # si el serial es mayor de 2 digitos inicia busqueda de serial
    # con la siguiente condicion

    if [(s['serial'],s) for s in query_serial] == []:
      # serial no existe entonces se habilitan los campos para registar
      # la nueva maquina
      print("SERIAL NO EXISTE")
      self.label_type.visible = True
      self.dropdown_machine_type.visible = True
      self.label_store.visible = True
      self.input_store.visible = True
      self.dropdown_store.visible = True
      self.button_register_store.visible = False
      self.button_register_machine.visible = True
      self.label_message.visible = False

    else:
      # serial existe, se deshabilitan los capos para que
      # no se puede agregar un duplicado
      self.label_message.visible = True
      self.label_message.background = "yellow"
      self.label_message.text = "This Machine is already in the Data Base"
      self.label_type.visible = False
      self.dropdown_machine_type.visible = False
      self.label_store.visible = False
      self.input_store.visible = False
      self.dropdown_store.visible = False
      self.button_register_store.visible = False
      self.button_register_machine.visible = False

# =================== Search Store Function ======================
  
  def search_store(self, store_name, **event_args):
    query_store = app_tables.stores.search(store=q.ilike(f"%{store_name}%"))
    self.dropdown_store.items = [(r['store'],r) for r in query_store]
    self.dropdown_store.visible = True
    self.button_register_machine.visible = True
    self.button_register_store.visible = False

    if [(r['store'],r) for r in query_store] == []:
      self.dropdown_store.visible = False
      self.button_register_machine.visible = True
      self.button_register_store.visible = True


    
    
  def link_new_store_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('register_store')








  
    


      
      