from ._anvil_designer import row_template_store_nameTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class row_template_store_name(row_template_store_nameTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Taking the Items of the repeating panel with the store names
    self.store_name_in_panel.text=self.item  
