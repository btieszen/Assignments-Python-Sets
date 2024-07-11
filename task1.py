#Python Sets Adventure
#You have two sets of flight destinations, one for each airline. Write a Python program to find out:
#1. Destinations that both airlines fly to.
#Destinations unique to your airline.
#Whether there are any destinations that neither airline shares.

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

while True:
        print("Destination Checker:")
        print (f"1: Destinations of our airline: ")
        print(f"2: Destinations of competitors airline: ")
        print(f"3: Destinations only our airlines fly to: ")
        print(f"4: Destinations that niether airlines share:")
        print(f"5: Exit")
        choice =input("Please make a selection ")
        if choice =="1":
            print("Our airline departures are:")
            for flight in (our_routes):
                print(flight)
        elif choice =="2":
            print("Our competitors departures are:")
            for flight in (competitor_routes):
                print(flight)
        elif choice=="3":
            print("Destinations only are airlines depart from:")
            flight=our_routes.difference(competitor_routes)
            print(flight)
        elif choice=="4":
            print("Neither airlines share these departures:")
            flight=our_routes.symmetric_difference(competitor_routes)
            print(flight)
        elif choice =="5":
            print("Goodbye")
            break
        else:
            print("Invalid choice please enter number from 1-5")
        
            
        
        
    





