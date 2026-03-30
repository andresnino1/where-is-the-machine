from ._anvil_designer import machine_informationTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

# notas to do
# leer esta documentacion https://anvil.works/docs/http-apis/creating-http-endpoints#appresponder-object


class machine_information(machine_informationTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    print('hello client')


    
    # Any code you write here will run before the form opens.

 