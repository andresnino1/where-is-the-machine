from ._anvil_designer import Machines_In_Repeating_PanelTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Machines_In_Repeating_Panel(Machines_In_Repeating_PanelTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    self.serial.text = self.item["serial"]
    self.type.text = self.item["type"]

    # Any code you write here will run before the form opens.
