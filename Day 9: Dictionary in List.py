country = input() # Add country name
visits = int(input()) # Number of visits
list_of_cities = eval(input()) # create list from formatted string
# 2 Dictionaries inside a List
travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]


# Write the function that will allow new countries to be added to the travel_log. 
def add_new_country(name, times, cities):
  new_country = {}
  new_country["country"] = name
  new_country["visits"] = times
  new_country["cities"] = cities
  travel_log.append(new_country)
# Call function
add_new_country(country, visits, list_of_cities) 
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")
