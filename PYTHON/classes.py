
class Point():
    def __init__(self,input1,input2) -> None:
        self.x = input1
        self.y = input2

class Flight():
    def __init__(self,capacity) -> None:
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self,name):
        if self.open_seats() == False:
            return False
        
        else:
            self.passengers.append(name)
            return True

    def open_seats(self):
        #print(self.capacity-len(self.passengers))
        seats_available = bool(self.capacity - len(self.passengers))
        #print(seats_available)
        return seats_available

if __name__ == '__main__':
    #p = Point(2,8)
    #print(p.x)
    #print(p.y)

    flight = Flight(3)
    #print("THERE")
    people = ["John", "Mary", "James", "Travis"]
    for person in people:
        success = flight.add_passenger(person)
        print(success)
        if success == True:
            print(f"Added {person} to flight successfully.")
        else:
            print(f"No available seats for {person}")

