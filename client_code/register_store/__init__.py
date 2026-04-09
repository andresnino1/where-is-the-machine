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

# display the name of the stores found in the db in data_grid

class register_store(register_storeTemplate):
  def __init__(self, new_store_name=None, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.input_store_name.text = new_store_name
    self.button_register_store.visible = False
    self.data_grid_store_name.visible=False
    self.store_name_repeating_panel.items=[]

    # Any code you write here will run before the form opens.
  def input_store_name_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    store_name = self.input_store_name.text.strip()
    if len(store_name) > 1:
      self.search_store(store_name) # function search the store name in database



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
    
# ========================================= Search Store Function ===========================
  
  def search_store(self, store_name, **event_args):
    query_store = app_tables.stores.search(store=q.ilike(f"%{store_name}%"))
    self.store_name_repeating_panel.items = [(r['store'],r) for r in query_store]

    # If there is NOT an store in de database the REGISTER STORE BUTTON IS ENABLED
    if [(r['store'],r) for r in query_store] == []:
      self.store_name_repeating_panel.items=['Store Is Not In Data Base']




