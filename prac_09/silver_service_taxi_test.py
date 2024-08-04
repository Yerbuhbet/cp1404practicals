from prac_09.silver_service_taxi import SilverServiceTaxi

def test_silver_service_taxi():
    # Create an instance of SilverServiceTaxi
    luxury_taxi = SilverServiceTaxi("Hummer", 200, 2)
    print("Initial state of SilverServiceTaxi:", luxury_taxi)


if __name__ == "__main__":
    test_silver_service_taxi()
