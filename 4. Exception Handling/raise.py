class YourException(Exception):
  def __init__(self, message):
    self.message = message
 
try:
  raise YourException(" Error in Message")
 
except YourException as err:
  print("Message:", err.message)