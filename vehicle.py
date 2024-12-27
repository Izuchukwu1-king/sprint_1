


class Vehicle:
  '''
   Imagine I want to list these vehicles on Craigslist
"Parent class is always the more generic of 
 the two classes that I'm working with"
  '''
def __init__(self, make,model,color,year,mileage):

        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.mileage = mileage
  def honk(self):


    def drive(self, miles_driven):


     return "HOOOOOOOOOONk!"
    #self.mileage = self.mileage + miles_driven OR
    self.mileage += miles_driven
    return self.mileage


def __repr__(self):
        return f'''A{self.color} {self.year} 
        {self.make} {self.model} with{self.mileage}miles'''
    
    
if __name__ == '__main__':
          my_vehicle = Vehicle('Toyota', 'Camry','gray',2015,60000)

          

          #print(my_vehicle.make)
          #print(my_vehicle.model)
          #print(my_vehicle.color)
          #print(my_vehicle.year)
          #print(my_vehicle.mileage)
          # OR run a method, I can call a method
          #print(my_vehicle.honk())
          #print(my_vehicle.make)



# Imagine I want to list these vehicles on Craigslist
class Convertible(Vehicle):
  '''
  This is the class docstring
  '''

  def __init__(self, make,model,color,year,mileage,top_down =True):
        super().__init__(make, model, color, year, mileage)
        #self.make = make
        #self.model = model
        #self.color = color
        #self.year = year
        #self.mileage = mileage
        self.top_down = top_down

  
  def change_top_status(self):
      if self.top_down:
        self.top_down= True
        return "Top is now up!"
                     
      else:
        self.top_down= False
        return "Top is now down!"

            
            

  def __repr__(self):
        return f'''A{self.color} {self.year} 
        {self.make} {self.model} with {self.mileage} miles'''
        
    
if __name__ == '__main__':
   my_vehicle = Convertible('Toyota', 'Camry','gray',2015,60000)

   print(my_vehicle.make)
   print(my_vehicle.mileage)
   print(my_vehicle.honk())
   print(my_vehicle.drive(1234))
   print(my_vehicle.mileage)

   print(my_vehicle)

   print(my_vehicle.top_down)
   print(my_vehicle.change_top_status)
   print(my_vehicle.top_down)

