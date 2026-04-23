from ._anvil_designer import RowTemplate1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class RowTemplate1(RowTemplate1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.serial.text=self.item['serial']
    self.type.text=self.item['type_link']['model']
    self.current_location.text=self.item['current_location']
    self.current_status.text=self.item['current_status']
    # print("imprimiendo self item:")
    # print(self.item)
    # Any code you write here will run before the form opens.
