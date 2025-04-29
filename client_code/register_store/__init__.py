from ._anvil_designer import register_storeTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

# TODO
# Al completar la busqueda por nombre en el menu dropdown no se filtra
# y salen otras opciones tambien - se debe arreglar esto

class register_store(register_storeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.button_register_store.visible = False

    # Any code you write here will run before the form opens.
  def input_store_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    search_store = self.input_store.text.strip()

    if len(search_store) > 1:
      results = app_tables.stores.search(store=q.ilike(f"%{search_store}%"))
      self.dropdown_store.items = [(r["store"], r) for r in results]
      # print ([(r['store'],r) for r in results])
      self.dropdown_store.visible = True
      self.button_register_store.visible = False

      if [(r["store"], r) for r in results] == []:
        self.dropdown_store.visible = False
        self.button_register_store.visible = True

    else:
      self.dropdown_store.items = []
      self.dropdown_store.visible = False

  def dropdown_store_show(self, **event_args):
    self.dropdown_store.items = [
      (r["store"], r) for r in app_tables.stores.search()
    ]
    # self.dropdown_machine_type.include_placeholder=True
    # self.dropdown_machine_type.placeholder="Chose Machine Model"
    # self.dropdown_machine_type.selected_value=""
    """This method is called when the DropDown is shown on the screen"""

  def dropdown_store_change(self, **event_args):
    """This method is called when an item is selected"""
    row = self.dropdown_store.selected_value
    print(row["store"])

  def button_register_store_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass
    # find_serial = app_tables.machines.get(serial=self.input_serial.text)
    # if find_serial is not None:
    #   # Machine exists in database

    #   print("serial si existe")
    # else:
    #   # Machine is not in database -- need to be registered
    #   anvil.server.call(
    #     "register_machine",
    #     self.input_serial.text,
    #     self.dropdown_machine_type.selected_value,
    #   )

  def link_home_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('register_machine')

  def link_new_store_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('register_store')



