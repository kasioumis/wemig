#!/usr/bin/python

# The title of the application as shown by the browser
TITLE = "My title"

# List of comma-separated categories to use with autocompletion
CATEGORIES = """ 
"Banana",
"Apple",
"Orange",
"Mango",
"Grapes"
"""

# List of comma-separated subcategories to use with autocompletion
SUBCATEGORIES = """ 
"Seeds",
"Juice",
"Color",
"Size",
"Weight",
"""

# List of safe IPs to access the application
IPS = ("127.0.0.1",
       "192.168.1.123",)

# The host IP to run the application from
#HOST = "127.0.0.1"
HOST = "0.0.0.0"

# The port to run the application from
PORT = 5000

# Is this a debug application?
#DEBUG = True
DEBUG = False
