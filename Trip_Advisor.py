def calculate_cost(flight, hotel, car, duration=7):
    total_cost = flight + hotel * duration + car * duration
    return total_cost

def get_most_expensive_city(paris_cost, london_cost, dubai_cost, mumbai_cost):
    cities = ["paris", "london", "dubai", "mumbai"]
    costs = [paris_cost, london_cost, dubai_cost, mumbai_cost]
    most_expensive_city = cities[costs.index(max(costs))]
    return most_expensive_city

def suggest_destinations(budget, paris_cost, london_cost, dubai_cost, mumbai_cost):
    affordable_destinations = []
    if budget >= paris_cost:
        affordable_destinations.append("paris")
    if budget >= london_cost:
        affordable_destinations.append("london")
    if budget >= dubai_cost:
        affordable_destinations.append("dubai")
    if budget >= mumbai_cost:
        affordable_destinations.append("mumbai")
    return affordable_destinations

choice = input("Enter the city you want to visit: ").lower()

paris_cost = calculate_cost(flight=200, hotel=20, car=28.5)
london_cost = calculate_cost(flight=250, hotel=30, car=17.1)
dubai_cost = calculate_cost(flight=370, hotel=15, car=80)
mumbai_cost = calculate_cost(flight=450, hotel=10, car=70)

if choice == "paris":
    print("The cost of visiting Paris for one week is:", paris_cost)
elif choice == "london":
    print("The cost of visiting London for one week is:", london_cost)
elif choice == "dubai":
    print("The cost of visiting Dubai for one week is:", dubai_cost)
elif choice == "mumbai":
    print("The cost of visiting Mumbai for one week is:", mumbai_cost)
else:
    print("Please choose a city from the following: Paris, London, Dubai, Mumbai")

most_expensive_city = get_most_expensive_city(paris_cost, london_cost, dubai_cost, mumbai_cost)
print("The most expensive city to visit is:", most_expensive_city)

budget = int(input("What is your budget? "))

affordable_destinations = suggest_destinations(budget, paris_cost, london_cost, dubai_cost, mumbai_cost)
if affordable_destinations:
    print(f"With a budget of {budget}, you can consider visiting:")
    for city in affordable_destinations:
        print(city.capitalize())
else:
    print("Unfortunately, your budget does not allow you to visit any of the listed destinations.")

