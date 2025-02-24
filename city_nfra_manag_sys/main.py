from vehicle_registration import Vehicle

vehicles = []

while True:
    action = input("Enter action (register, update, display, exit): ").lower()
    if action == 'exit':
        break
    try:
        if action == 'register':
            name_of_owner = input("Enter name of owner: ")
            registration_number = input("Enter registration number: ")
            vehicle_type = input("Enter type of vehicle: ") 
            new_vehicle = Vehicle(registration_number, vehicle_type, name_of_owner)
            vehicles.append(new_vehicle)
            print("Vehicle registered.")

        elif action == 'update':
            registration_number = input("Enter registration number to update: ")
            for vehicle in vehicles:
                new_name = input("Update name of owner: ")
                vehicle.owner = new_name
                print(f"Owner: {vehicle.owner}.")
                break
            else:
                print("Vehicle not found.")

        elif action == 'display':
            if not vehicles:
                print("No vehicles registered.")
            else:
                for vehicle in vehicles:
                  vehicle.display_Register()#method call
    except Exception as e:
        print(f"Error Occurred: {e}")