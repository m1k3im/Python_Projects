
earth_weight = 5.976*10**24
g = 6.67408*10**-11  # Gravitational constant
other_obj_weight = float(input("Enter the mass of the second object without degrees of tens:\n"))*10**int(input("Enter the degree of ten:\n",))
distance = int(input("Enter the distance between objects in kilometers:\n"))*10**3

# For example
# Moon weight = 7.36 × 10^22 Kg
# Distance between = 384.400 Km


def math_gravitation(other_object_weight, distance_between):
    return (g * earth_weight * other_object_weight) / (distance_between**2)


final_force = math_gravitation(other_obj_weight, distance)
print("The gravitational force between the Earth and a given object is ~", final_force, "Newtons")  # Final Result
