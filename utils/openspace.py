class Openspace :
    # creat class Openspace 
    def __init__(self, tables, number_of_tables=6):
    
        """ creat constructor"""
        self.tables=tables
        self.number_of_tables=number_of_tables
    def __str__(self):
         """dunder str method"""
         return  f" return tables: {self.tables}, number of tables:   {self.number_of_tables}"
    
    def organize(names):
        """ randomly assign people to Seat 
        objects in the different Table objects"""
        self.tables = [table() for _ in range(0,7)]
        ???????????????


    def display():
        """display different tables and there 
        occupants in a nice and readable way """

    def store(filename):
        """ store repartition in an excel file"""

