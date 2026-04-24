from ._anvil_designer import row_template_machinesTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class row_template_machines(row_template_machinesTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.link_serial.text=self.item['serial']
    self.type.text=self.item['type_link']['model']
    self.current_location.text=self.item['current_location']
    self.current_status.text=self.item['current_status']
    
    print("imprimiendo self item:")
    repairs = self.item[]
    print(self.item['repairs_link'])
    # print(self.item['repairs']['issue'])
    # Any code you write here will run before the form opens.

  @handle("link_serial", "click")
  def link_serial_click(self, **event_args):
    """This method is called when the link is clicked"""
    print(self.item['serial'])
