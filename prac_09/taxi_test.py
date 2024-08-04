from taxi import Taxi

def test_taxi():
    my_taxi = Taxi("Prius 1", 100)
    print("Initial state:", my_taxi)
    my_taxi.drive(40)
    print("After 40km:", my_taxi)
    print("Current fare:", my_taxi.get_fare())
    my_taxi.start_fare()
    my_taxi.drive(100)
    print("After another 100km:", my_taxi)
    print("Current fare:", my_taxi.get_fare())

if __name__ == "__main__":
    test_taxi()
