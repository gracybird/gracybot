import imp 
import sys 

"""
Allow for the dynamic import of modules into the bot.

Modules provide additional slash commands to extend functionality.

Access to each module is controlled by role.
"""
  
# dynamic import  
def dynamic_imp(name, class_name): 
      
    # find_module() method is used 
    # to find the module and return 
    # its description and path 
    try: 
        fp, path, desc = imp.find_module(name) 
          
    except ImportError: 
        print ("module not found: " + name) 
          
    try: 
    # load_modules loads the module  
    # dynamically ans takes the filepath 
    # module and description as parameter 
        example_package = imp.load_module(name, fp, 
                                          path, desc) 
          
    except Exception as e: 
        print(e) 
          
    try: 
        myclass = imp.load_module("% s.% s" % (name, 
                                               class_name),  
                                  fp, path, desc) 
          
    except Exception as e: 
        print(e) 
          
    return example_package, myclass 
      
#  Driver code 
if __name__ == "__main__": 
    mod, modCl = dynamic_imp("GFG", "addNumbers") 
    modCl.addNumbers(1, 2) 