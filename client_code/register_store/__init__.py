from ._anvil_designer import register_storeTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

# TODO
# buscar el store por si ya existe y indicar que existe 
# al dar enter en el nombre de estor o perder foco del campo
# que se ejecute la busqueda y se indique en un mensaje
# que el store ya existe y deshabilitar el boton de registro
# para evitar error de usuario al darle click
# esta busqueda de STORE es necesaria ya que si se da click en el
# link del menu NEW STORE no se ha hecho una busqueda del store con anterioridad
# si el store no existe.. registrar el nuevo store en la base de datos STORES

class register_store(register_storeTemplate):
  def __init__(self, new_sotre_name=None, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.input_store.text = new_sotre_name
    self.button_register_store.visible = False

    # Any code you write here will run before the form opens.
  def input_store_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    search_store = self.input_store.text.strip()
    self.input_store_code.text = ""
    self.dropdown_state.selected_value = None


  def button_register_store_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass
 
  def link_home_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('register_machine')

  def link_new_store_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('register_store')

  def dropdown_state_show(self, **event_args):
    states = ["ACT", "NSW", "VIC", "QLD", "SA", "TAZ", "WA", "NT"]
    self.dropdown_state.items = states
    self.dropdown_state.include_placeholder=True
    self.dropdown_state.placeholder="Select State"
    


