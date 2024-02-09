


class Seat:

    def __init__(self, occupant=None, free=True):
        """" creat constructor"""
        
        self.occupant= occupant
        self.free= free # it is free at first step and not full
   
    def remove_occupant(self):
        """remove occupant"""
        if self.free is False: # chech if seat is occupied 
           name_occupant_not_assigend =self.occupant  # if seat is not empty,  teh name  must be removed from this seat
           self.occupant=None #  it is removed from seat
           return f"{name_occupant_not_assigend} is not assigned  to this seat" 
           # the seat was full , we could not assign occupant 
           
        else:
            return "the seat  can have a occupant"


    def set_occupant(self, name):
        """ set occupant to list"""
        if self.free:
            self.occupant = name # if the seat is occupied, who is on it. 
            self.free = False # shows that the seat is now occupied
            return True
        else: 
            return False
     
    

class table:
    def __init__(self, capacity : int):
        """Creat constructor"""
        self.capacity= 6 # 6 is assined as first value to table 
        self.seats= []
        # with a for loop, we creat a list of seats for each table
        for i in range(0,capacity):
            seat_instance = Seat(i)
            self.seats.append(seat_instance)   
        self.list_assigned_names=[] 
      
    def assign(self, name):
        if self.has_free_spot():  #first, check  whether table has free spots
          
              for seat in self.seats:
                 if seat.free:
                     seat.set_occupant()# if seat is free we  call this function to occupy name to seat 
                     self.list_assigned_names.append(self.name) # name must be added to names of assigned
                     return True
        return self.list_assigned_names # a new assinged list must  be returned for next tables
                                
            
    def has_free_spot(self):
        """ returns true if there is a capacity"""
        # if  empty spots remain, so  the table has capacity
        for seat in self.seats:
            if seat.free:
             return True
                 
            
    
     
    




   

        
        
        
    

        
