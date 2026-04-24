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

    # print("imprimiendo self item desde template repairs:")
    # self.date.text = self.item['date']
    self.date.text = self.item['date']
    self.issue.text = self.item['issue']
    self.repair_status.text = self.item['repair_status']
    
    # for repair in repairs:
    #   # self.date.text = repair['date']
    #   # self.issue.text = repair['issue']
    #   # self.repair_status.text = repair['repair_status']
    #   print(repair['date'])
    #   print(repair['issue'])
    # Any code you write here will run before the form opens.
