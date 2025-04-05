from ._anvil_designer import registerTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


class register(registerTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def dropdown_machine_type_show(self, **event_args):
    self.dropdown_machine_type.items = [(r["model"],r) for r in app_tables.machine_type.search()]
    #self.dropdown_machine_type.include_placeholder=True
    #self.dropdown_machine_type.placeholder="Chose Machine Model"
    #self.dropdown_machine_type.selected_value=""
    """This method is called when the DropDown is shown on the screen"""

  def dropdown_machine_type_change(self, **event_args):
    """This method is called when an item is selected"""
    row = self.dropdown_machine_type.selected_value
    print(row["model"])

  def button_register_machine_click(self, **event_args):
    """This method is called when the button is clicked"""
    find_serial = app_tables.machines.get(serial=self.input_serial.text)
    if find_serial is not None:
      # Machine exists in database
      
      print ('serial si existe')
    else:
      # Machine is not in database -- need to be registered
      anvil.server.call('register_machine', self.input_serial.text, self.dropdown_machine_type.selected_value)

  def input_customer_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    query = self.input_customer.text.strip()

    if len(query) > 1:
      results = app_tables.stores.search(store=q.ilike(f"%{query}%"))
      self.drop_down_customer.items = [(r['store'],r) for r in results]
      self.drop_down_customer.visible = True
    else:
      self.drop_down_customer.items = []
      self.drop_down_customer.visible = False
    
      