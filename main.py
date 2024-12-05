# Theme Park Task
class Attraction:
    def __init__(self, name, capacity, status):
        self._name = name
        self._capacity = capacity
        self._status = status
    
    def get_details(self):
        print("Attraction: " + self._name + ", Capacity: " +str(self._capacity))
    
    def start(self):
        if self._status == "Open":
            print("The attraction '" +self._name+ "' is starting.")
        else:
            print("The attraction is closed.")
    
    def open_attraction(self):
        self._status = "Open"
    
    def close_attraction(self):
        self._status = "Closed"
    
class ThrillRide(Attraction):
    def __init__(self, name, capacity, status, min_height):
        super().__init__(name, capacity, status)
        self._min_height = min_height
    
    def start(self):
        if self._status == "Open":
            print("Thrill Ride " +self._name+ " is now starting. Hold on tight!")
        else:
            print(f"Thrill ride {self._name} is closed.")
    
    def is_eligible(self, height):
        if height >= self._min_height:
            print(f"This person is eligible to ride {self._name}.")
        else:
            print(f"This person is too short to ride {self._name}.")
    
class FamilyRide(Attraction):
    def __init__(self, name, capacity, status, min_age):
        super().__init__(name, capacity, status)
        self._min_age = min_age
    
    def start(self):
        if self._status == "Open":
            print("Family Ride " +self._name+ " is now starting. Enjoy the fun!")
        else:
            print(f"Family Ride {self._name} is closed.")
    
    def is_eligible(self, age):
        if age >= self._min_age:
            print(f"This person is eligible to ride {self._name}.")
        else:
            print(f"This person is not eligible to ride {self._name}")

class Staff:
    def __init__(self, name, role):
        self._name = name
        self._role = role
    
    def work(self):
        print(f"Staff {self._name} is performing their role: {self._role}")

class Manager(Staff):
    def __init__(self, name, role):
        super().__init__(name, role)
        self._team = []
    
    def add_staff(self, staff):
        self._team.append(staff)
    
    def get_team_summary(self):
        for workers in self._team:
            print(workers._name + "("+workers._role+")")
        
    
class Visitor:
    def __init__(self, name, age, height):
        self._name = name
        self._age = age
        self._height = height
        self._ride_history = []
    
    def ride(self, attraction):
        if isinstance(attraction, ThrillRide) == True:
            eligible = attraction.is_eligible(self._height)
            self._ride_history.append(attraction)
        elif isinstance(attraction, FamilyRide) == True:
            eligible = attraction.is_eligible(self._age)
            self._ride_history.append(attraction)
        return eligible

    def view_history(self):
        for ride in self._ride_history:
            print(ride._name)
    




dragon = ThrillRide("Dragon Coaster", 20, "Open", 140)
merry = FamilyRide("Merry-Go-Round", 30, "Open", 4)
alex = Visitor("Alex", 20, 160)
jessica = Visitor("Jessica", 2, 120)

alex.ride(dragon)
alex.ride(merry)

jessica.ride(dragon)
jessica.ride(merry)

thrills = ThrillRide("Smiler", 40, "Open", 150)
family = FamilyRide("Tea Cups", 30, "Open", 5)

thrills.start()
family.start()
dragon.start()
merry.start()

worker = Staff("Worker", "Janitor")
boss = Manager("Boss", "Manager")
boss.get_team_summary()
boss.add_staff(worker)
boss.get_team_summary()

alex.view_history()