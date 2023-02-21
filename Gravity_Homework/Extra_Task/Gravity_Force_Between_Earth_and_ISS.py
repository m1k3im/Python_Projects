import urllib.request
import json


req = urllib.request.Request("https://api.wheretheiss.at/v1/satellites/25544")  # api input
response = urllib.request.urlopen(req)
obj = json.loads(response.read())  # write api parameters


altitude = (obj['altitude'])*10**3+(6371*10**3)  # counting the distance between Earth and ISS
earth_weight = 5.972*10**24
g = 6.67408*10**-11  # Gravitational constant

# Function to calculate gravity force


def math_gravitation(other_object_weight, distance_between):
    return (g * earth_weight * other_object_weight) / (distance_between**2)


force = math_gravitation(420*10**3, altitude)  # Count the force
print("The force between The ISS and The Earth is ~", round(force), "Newtons at the moment")  # Final Result
