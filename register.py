#================================================================
#
#   File name   : register.py
#   Author      : Josiah Tan
#   Created date: 27/09/2020
#   Description : decorator file registering functions (not really math though)
#
#================================================================

#================================================================

import functools
class Register:
  _counter = dict()
  _PLUGINS = dict()
  
  def register(func):
    """
    decorator registers a method (not a function) into PLUGINS and a counter
    parameters:
      -- func: some method 
    returns:
      -- a wrapper
    """
    cls_name = func.__qualname__.split('.')[0]
    if Register._counter.get(cls_name) == None:
      Register._counter[cls_name] = 0
      Register._PLUGINS[cls_name] = {}
    Register._counter[cls_name] += 1
    Register._PLUGINS[cls_name][func.__name__] = func
    @functools.wraps(func)
    def wrapper(inst, *args, **kwargs):      
      return func(inst, *args, **kwargs)
    return wrapper 
  
  @classmethod
  def get_plugins(cls):
    return cls._PLUGINS.get(cls.__name__) 
  @classmethod
  def get_counter(cls):
    return cls._counter.get(cls.__name__)

if __name__ == '__main__':
  class Hello(Register):
    @Register.register
    def foo3(self):
      pass
    @Register.register
    def foo4(self):
      pass
    def print_registered_count():
      print(Hello.get_counter())
  
  class Bye(Register):
    @Register.register
    def bye1(self):
      pass
    @Register.register
    def bye1(self):
      pass
    @Register.register
    def bye1(self):
      pass
  class Bonjour(Hello):
    pass
  

  print(Hello.get_counter())
  print(Hello.get_plugins())

  print(Bye.get_counter())
  print(Bye.get_plugins())

  print(Bonjour.get_counter())
  print(Bonjour.get_plugins())
