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
    info_api=anvil.server.startup_data
    self.info_serial.text=info_api["info_serial"]
    self.info_type.text=info_api["info_type"]
    self.info_current_location.text=info_api["info_current_location"]


    
    # Any code you write here will run before the form opens.

 