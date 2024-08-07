from taxi import Taxi

def main():
    test_taxi()

def test_taxi():
    # Create a new taxi object named 'Prius 1' with 100 units of fuel
    my_taxi = Taxi("Prius 1", 100)

    # Drive the taxi 40 km
    my_taxi.drive(40)

    # Print the taxi's details and the current fare
    print(my_taxi)
    print(f"Current fare: ${my_taxi.get_fare():.2f}")

    # Restart the meter (start a new fare)
    my_taxi.start_fare()

    # Drive the car another 100 km
    my_taxi.drive(100)

    # Print the taxi's details and the current fare
    print(my_taxi)
    print(f"Current fare: ${my_taxi.get_fare():.2f}")

if __name__ == "__main__":
    main()
