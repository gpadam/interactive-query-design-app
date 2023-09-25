from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def primary_color_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    query = anvil.server.call('query_generator', 
                                self.title.text,
                                self.KQ.text)
    if query:
      self.result1.visible = True
      self.result1.text = query[0]
      self.result2.visible = True
      self.result2.text = query[1]
      self.result3.visible = True
      self.result3.text = query[2]
