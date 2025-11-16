from hvac.api.system_backend import health


class Hero: # template
    # instace variabel
    def __init__(self,InputName,health, InputPower, InputArmor ):
        self.name = InputName
        self.health = health
        self.power = InputPower
        self.armor = InputArmor

hero1 = Hero("quincy",100,12,122)


print(hero1.__dict__)