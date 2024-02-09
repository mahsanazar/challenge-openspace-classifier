from utils.table import table

import random

class Openspace :
    # creat class Openspace 
    def __init__(self,  number_of_tables = 4):
    
        """ creat constructor"""
        
        self.number_of_tables=number_of_tables # it is set on 4 for default value
        self.tables=[]
        self.tables = [ table() for _ in range(0, number_of_tables)] # creat instances of table 
    def __str__(self):
         """dunder str method"""
         return  f" return tables: {self.tables}, number of tables:   {self.number_of_tables}"
    
    def organize(self,names):
        """ randomly assign people to Seat 
        objects in the different Table objects"""
        random.shuffel(names)  # this  line  randomly change order of names
        for one_table in self.tables:# call the assign function  for  each table
             for name in names:
                if one_table.assign(name): 
                    names.remove(name)
                else: # if it cannot assign, we have to move next table  to assign
                    break

    def display(self):
        """display different tables and there 
        occupants in a nice and readable way """
          # print and show the result of each table , iterate over each table instances
        for i , table in enumerate(self.tables):
        # Print the index of each instance along with its value attribute
            print( f"number {i}: Table : {table}")
             for j, seat in enumerate(tables.seats):
                  print(f" seat: {j} : {" Free" if seat.free else seat.occupant}")
                    
            

    def store(self, filename):
        """ store repartition in an excel file"""
        for i , table in enumerate(self.tables):
              for j, seat in enumerate(tables.seats):
                     if seat.occupant():
                         seat.occupant=seat.names.pop(0)
                     else:
                         seat.occupant="empty"
        
                         
                     
                         
                          
                        






        

