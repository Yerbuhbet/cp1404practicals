from silver_service_taxi import SilverServiceTaxi


def test_silver_service_taxi():
    # Create a SilverServiceTaxi with a fanciness level of 2
    luxury_taxi = SilverServiceTaxi("Hummer", 200, 2)
    print(luxury_taxi)  # Initial state

    # Start a new fare and drive 18 km
    luxury_taxi.start_fare()
    luxury_taxi.drive(18)

    # Calculate fare
    fare = luxury_taxi.get_fare()
    print(f"Fare for 18 km: ${fare:.2f}")
    assert fare == 48.78, f"Test failed, fare is ${fare}, expected $48.78"


def main():
    test_silver_service_taxi()


if __name__ == "__main__":
    main()
