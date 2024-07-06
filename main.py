# Importing Dependencies

import mysql.connector as ms
import configparser
import datetime
from tabulate import tabulate

# Establishing Connection
from connection import *
flag = is_connected()
print(flag)

