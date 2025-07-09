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
    self.button_register_customer.visible = False
    self.dropdown_machine_type.visible = False
    self.input_customer.visible = False
    self.label_type.visible = False
    self.label_customer.visible = False
    self.drop_down_customer.visible = False
    self.button_register_machine.visible = False
    self.label_message.visible = False
  

  def input_serial_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    serial_search = self.input_serial.text.strip()
    

    if len(serial_search) > 2:
      self.search_machine_serial(serial_search) # function that search machine serial
      

    else:
      # si el serial es menor que 2 digitos mantiene todos los campos ocultos
        self.label_type.visible = False
        self.dropdown_machine_type.visible = False
        self.label_customer.visible = False
        self.input_customer.visible = False
        self.drop_down_customer.visible = False
        self.button_register_customer.visible = False
        self.button_register_machine.visible = False
        self.label_message.visible = False

  def link_new_store_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('register_store')

  def dropdown_machine_type_change(self, **event_args):
  #   """This method is called when an item is selected"""
  #   row = self.dropdown_machine_type.selected_value
  #   # print(row["model"])
    pass

  def dropdown_machine_type_show(self, **event_args):
  #   """This method is called when the DropDown is shown on the screen"""
  #   self.dropdown_machine_type.items = [(r["model"],r) for r in app_tables.machine_type.search()]
  #   self.dropdown_machine_type.include_placeholder=True
  #   self.dropdown_machine_type.placeholder="Chose Machine Model"
  #   #self.dropdown_machine_type.selected_value=""
    pass

  def input_customer_change(self, **event_args):
  #   """This method is called when the text in this text box is edited"""
    pass

  def button_register_machine_click(self, **event_args):
  #   """This method is called when the button is clicked"""
    pass

  def home_link_click(self, **event_args):
  #   """This method is called when the link is clicked"""
  #   open_form('register_machine')
    pass


# ===================================== SEARCH SERIAL FUNCTION ============================================
    
  def search_machine_serial(self, serial_search, **event_args):
    
    query_serial = app_tables.machines.search(serial=serial_search) # search the serial in database
    self.label_type.visible = False
    self.dropdown_machine_type.visible = False
    self.label_customer.visible = False
    self.input_customer.visible = False
    self.drop_down_customer.visible = False
    self.button_register_customer.visible = False
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
      self.label_customer.visible = True
      self.input_customer.visible = True
      self.drop_down_customer.visible = True
      self.button_register_customer.visible = True
      self.button_register_machine.visible = True
      self.label_message.visible = False


      def input_customer_change(self, **event_args):
        """This method is called when the text in this text box is edited"""
        query = self.input_customer.text.strip()

        if len(query) > 1:
          results = app_tables.stores.search(store=q.ilike(f"%{query}%"))
          self.drop_down_customer.items = [(r['store'],r) for r in results]
          self.drop_down_customer.visible = True
          self.button_register_machine.visible = True
          self.button_register_customer.visible = False

          if [(r['store'],r) for r in results] == []:
            self.drop_down_customer.visible = False
            self.button_register_machine.visible = False
            self.button_register_customer.visible = True

        else:
          self.drop_down_customer.items = []
          self.drop_down_customer.visible = False

      def button_register_machine_click(self, **event_args):
        """This method is called when the button is clicked"""
        find_serial = app_tables.machines.get(serial=self.input_serial.text)
        if find_serial is not None:
          # Machine exists in database

          print ('serial si existe')
        else:
          # Machine is not in database -- need to be registered
          anvil.server.call('register_machine', self.input_serial.text, self.dropdown_machine_type.selected_value)


    else:
      # serial existe, se deshabilitan los capos para que
      # no se puede agregar un duplicado
      print ([(s['serial'],s) for s in query_serial]) # imprime columna serial
      print("serial existe")
      self.label_message.visible = True
      self.label_message.background = "yellow"
      self.label_message.text = "This Machine is already in the Data Base"
      self.label_type.visible = False
      self.dropdown_machine_type.visible = False
      self.label_customer.visible = False
      self.input_customer.visible = False
      self.drop_down_customer.visible = False
      self.button_register_customer.visible = False
      self.button_register_machine.visible = False
      print("serial existe 2")


  




  
  # def search_machine_serial(self, serial_search):
  #   #query_serial = app_tables.machines.search(serial=serial_search) # search the serial in database
  #   #return query_serial
  #   print ("funcion search machine serial working")
    


      
      