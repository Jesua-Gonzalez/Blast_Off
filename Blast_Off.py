

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





