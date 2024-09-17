from abc import ABC, abstractmethod

class GameObject:
    def __init__(self,id,name,x,y):
        self.Id=id# тип protected
        self.Name=name
        self.X=x
        self.Y=y
    def get_id(self):
        return self.Id
    def getname(self):
        return self.Name
    def getx(self):
        return self.X
    def gety(self):
        return self.Y

class Unit(GameObject):
    def __init__(self, id, name, x, y, alive,health):
        GameObject.__init__(self,id,name,x,y)
        self.alive=alive
        self.health = health
    def is_alive(self):
        return self.alive
    def get_hp(self):
        return self.health
    def receive_damage(self,damage):
        self.health-=damage


# Интерфейс Attacker
class Attacker(ABC):
    @abstractmethod
    def attack(self, unit) -> None:
        pass

# Интерфейс Moveable
class Moveable(ABC):
    @abstractmethod
    def move(self, x, y) -> None:
        pass


class Archer(Unit,Attacker,Moveable):
    def __init__(self,id,name,x,y,alive,health,damage_power):
        Unit.__init__(self,id,name,x,y,alive,health)
        self.Power=damage_power
    def attack(self,unit):
        unit.receive_damage(self.Power)
    def move(self, x, y):
        self.X=x
        self.Y=y

class Building(GameObject):
    def __init__(self,id,name,x,y,build):
        super().__init__(id,name,x,y)
        self.Build=build
    def is_built(self):
        return self.Build

class Fort(Building,Attacker):
    def __init__(self,id,name,x,y,build,damage):
        super().__init__(id,name,x,y,build)
        self.Damage=damage
    def attack(self,unit):
        unit.receive_damage(self.Damage)

class  MobileHouse(Building,Moveable):
    def move(self, x, y):
        self.X=x
        self.Y=y


a=Archer(1,"Star man",12,2,True,100,12)
b=Unit(23,"K",1,2,True,64)
a.attack(b)
print(b.health)


