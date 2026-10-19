seat_type=input("Enter the seat type: AC/Non-AC/Sleeper: ").lower()

match seat_type:
    case "ac":
        print("You have selected AC seat")
    case "non-ac":
        print("You have selected Non-AC seat")
    case "sleeper":
        print("You have selected Sleeper seat")
    case _:
        print("Invalid seat type selected")
