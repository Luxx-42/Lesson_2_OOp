from event_manag_sys import Event

def create_event_with_input():
    event_name = input("Enter the event name: ")
    event_date = input("Enter the event date (YYYY-MM-DD): ")
    return Event(event_name, event_date)

def main():

    print("Let's create an event!")
    event = create_event_with_input()
    
    while True:

        print(f"\nCurrent event: {event.name} on {event.date}")
        print(f"Current participant count: {event.get_participant_count()}")
        
        action = input("Would you like to add participants? (yes/no/exit): ").lower()

        if action == 'yes':
            while True:
                try:
                    num = int(input("How many participants to add? "))
                    if num < 0:
                        print("Please enter a positive number.")
                        continue
                    event.add_participant(num)
                    print(f"{num} participant(s) added!")
                    break
                except ValueError:
                    print("Please enter a valid number.")
        elif action == 'no':
            continue 
        elif action == 'exit':
            print(f"\nFinal details for {event.name}:")
            print(f"Date: {event.date}")
            print(f"Total participants: {event.get_participant_count()}")
            break  
        else:
            print("wrong input. Please enter 'yes', 'no', or 'exit'")


if __name__ == "__main__":
    main()                                                                 
    