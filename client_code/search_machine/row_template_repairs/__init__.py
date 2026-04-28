from ._anvil_designer import row_template_repairsTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class row_template_repairs(row_template_repairsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    self.date.text = self.item['date']
    self.issue.text = self.item['issue']
    self.repair_status.text = self.item['repair_status']
    