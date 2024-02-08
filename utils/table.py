
# creat a calss Seat
class Seat:

    def __init__(self, free = True, occupant: str):
        """" creat constructor"""
        self.free=free
        self.occupant=occupant
    def set_occupant(self, name):
        """ assign seat to people """
        
        self.name=name
        # creat instance of table to use its function
        instance_table_class=table()
        # check whether is a empty spot , assign next colleague and remove that from list
     
        if  instance_table_class.has_free_spot() is True :
            instance_table_class.assign_seat(name)
            self.remove_occupant()
            return True
        
    def remove_occupant(self,name):
        """ remove someone from a seat and 
            return the name of 
            of the person occupying the seat before"""
        if self.set_occupant() is True:  
        # Remove the element from the list
            with open("new_colleagues.cvs", "r") as file:
                content = file.read()
                if name in content:
                       updated_content = content.replace(name, "")

                       # Update the file with the updated contents
                with open("new_colleagues.cvs", "w") as file:
                          file.write(updated_content)
  

class table:
    def __init__(self, capacity : int, seats):
        """Creat constructor"""
        self.capacity=capacity 
        self.seats=seats
   ## def __str__(self):
   ##"""dunder str method"""
   ## return  f" return capacity: {self.capacity}, seats:   {self.seats}"
    def has_free_spot(self):
        """ returns true if there is a capacity"""
        if self.left_capacity() != 0:
            return True
        else:
            return False
    def assign_seat(self, name):
        """ that places someone at the table"""
       
        if self.left_capacity() != 0 :
             
             
            

             
          
             

        
             

    def left_capacity(self):
        """ return  the left capacity"""
        new_capacity= 4 - self.capacity
        return new_capacity
    


        