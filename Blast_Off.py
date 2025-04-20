

class Astronaut:
    def __init__(self, name, role, experience = 0, **kwargs):   #this class is defined with the name, role, experience and additional info. in kwargs
        self.name = name
        self.role = role
        self.experience = experience
        self.more_attributes_ = kwargs


    def gain_experience(self):
        self.experience = self.experience + 1       #experience earned will be captured on this method overriding the default value of 0


    def get_info(self):
        info = {    "name": self.name,      #this section will store the astronuats info in a dictionary
                    "role": self.role,
                    "experience": self.experience   }
        
        info.update(self.more_attributes_) 
        return info





class Spacecraft:
    def __init__(self, name, capacity):     #this class is defined with the name, capacity, and crew list of onboard astronauts 
        self.name = name
        self.capacity = capacity
        self.crew = [] 
    

    def add_astronaut(self, *astronauts):  #simply add astornauts if amount in crew is less than the capacity
        for astronaut in astronauts:
            if len(self.crew) >= self.capacity:
                print(f"Max Capacity Reached! {astronaut.name}, cannot aboard the mothership.")
            else:
                self.crew.append(astronaut)


    def list_crew(self):
        return [astronaut.name for astronaut in self.crew]
    

    def get_info(self):      #this section will store the spacecraft info in a dictionary
        return { "name": self.name,
                 "capacity": self.capacity,
                 "crew": self.list_crew() }





class Autonomous_Spacecraft(Spacecraft):
    def __init__ (self, name, autonomy_level):      #this class is defined with the name, and autonomy level
        super().__init__(name, capacity=0)          #super helps bridge connecting classes when on inherits the other

        if not isinstance(autonomy_level, int):
            raise ValueError("Error: autonomy_level must be a whole number between 1 and 10.")          #safties incase autonomy level input is not correct

        if autonomy_level < 1 or autonomy_level > 10:
            raise ValueError("Error: autonomy_level must be between 1 and 10.")
        
        self.autonomy_level = autonomy_level            
        self.crew = []          #needed attribute to call this functions later on using get_info(self) + autonomy = 0 since its aka autonomous


    def add_astronaut(self, *astronauts):
        print(f"This is an autonomous spacecraft: {self.name}, and it does not allow passangers to be added.")


    def list_crew(self):
        return [astronaut.name for astronaut in self.crew]


    def get_info(self):
        info = super().get_info()  #obtains class info of the main class
        info["autonomy_level"] = self.autonomy_level  #add to dicitonary the level
        return info