from ._anvil_designer import row_template_machinesTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

# todo, hay un error cuando el numero de serial no existe en db
# error es 'NoneType' does not support indexing

class row_template_machines(row_template_machinesTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # print(self.item['serial'])
    
    self.link_serial.text=self.item['serial']
    self.type.text=self.item['type_link']['model']
    self.current_location.text=self.item['current_location']
    self.current_status.text=self.item['current_status']
    

  @handle("link_serial", "click")
  def link_serial_click(self, **event_args):
    """This method is called when the link is clicked"""
    print(self.item['serial'])
