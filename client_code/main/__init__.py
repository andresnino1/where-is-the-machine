from ._anvil_designer import mainTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

# notas to do
# implementar en el formulario que los campos no este activos si el serial existe
# esto para que no haya la opcion de agregar el mismo serial


class main(mainTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.label_password_e
      

    # Any code you write here will run before the form opens.

  def button_login_click(self, **event_args):
    """This method is called when the button is clicked"""
    momentary_password = self.input_login_password.text.strip()
    is_password_ok = anvil.server.call('check_password', momentary_password)

    if is_password_ok:
      anvil.open_form('register_machine')
    else:
      
    

