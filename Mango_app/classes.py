# pest_model.py

# This is our Pest class, which is like a blueprint for creating pest objects.
class Pest:
    def __init__(self, key, name, scientific_name, affects, image, description='', life_cycle=''):

        self.key = key
        self.name = name
        self.scientific_name = scientific_name
        self.affects = affects
        self.image = image
        self.description = description
        self.life_cycle = life_cycle

    @classmethod 
    #Why I used Classmethod ? because I wanted to combine both the pest_data and pest_description data. Classmethod helps me to change the attributes of a class itself not the object so that I don't create new instances
    
    def from_data(cls, data, description_data):
        pest_description = {}
        
       
        for description in description_data:
            if description['key'] == data['key']: 
                pest_description = description
                break  
        
        return cls(
            key=data['key'], 
            name=data['name'], 
            scientific_name=data['scientific_name'], 
            affects=data['affects'],  
            image=data['image'], 
            description=pest_description.get('description', ''),  
            life_cycle=pest_description.get('life_cycle', '') 
        )


class Protect_Against_Pest(Pest):
    pass

class Diseases():
    pass

class Protect_Against_Diseases(Diseases):
    pass