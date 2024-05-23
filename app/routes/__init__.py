# you can import any variables or functions defined by Python modules into other modules
# .home directs the program to find the module named home in the current directory
# then, import the bp object but rename it as home
from .home import bp as home
from .dashboard import bp as dashboard
from .api import bp as api