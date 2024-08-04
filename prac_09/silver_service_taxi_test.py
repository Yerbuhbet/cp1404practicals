from prac_09.silver_service_taxi import SilverServiceTaxi

def test_silver_service_taxi():
    # Create an instance of SilverServiceTaxi
    luxury_taxi = SilverServiceTaxi("Hummer", 200, 2)
    print("Initial state of SilverServiceTaxi:", luxury_taxi)

    # Start a new fare and simulate a trip
    luxury_taxi.start_fare()
    luxury_taxi.drive(18)  # Simulate driving 18 km
    fare = luxury_taxi.get_fare()
    print(f"Fare for 18 km trip: ${fare:.2f}")
    assert fare == 48.78, f"Test failed, fare calculated as ${fare}, expected $48.78"

if __name__ == "__main__":
    test_silver_service_taxi()
