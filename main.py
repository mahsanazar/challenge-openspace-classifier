import random


from utils.openspace import Openspace
from utils.table import table

with open ('new_colleagues.csv', "r") as file:
    content=file.read()
random_occupant= Openspace(4 ) #  number of tables is 4 and lines_list is the list of names that must be occupied
random_occupant.organize(content)
random_occupant.display()
random_occupant.store(content)





