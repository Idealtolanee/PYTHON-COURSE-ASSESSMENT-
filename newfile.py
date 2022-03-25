Your_rating = float(input("input rating: "))
Rating_1 = 0.0
Rating_2 = 0.4
Rating_3 = 0.6

if Your_rating == Rating_1:
    print("unacceptable performance")
elif Your_rating == Rating_2:
    print("acceptable performance")
elif Your_rating >= Rating_3:
    print("meritorious performance")
else:
    print("")

Raise_factor = 2400.00
Amount_raised = Your_rating * Raise_factor
if Your_rating == Rating_1:
    print(f"The amount of the employee's raise is {Amount_raised}")
elif Your_rating == Rating_2:
    print(f"The amount of the employee's raise is {Amount_raised}")
elif Your_rating >= Rating_3:
     print(f"The amount of the employee's raise is ${Amount_raised}")
else:
    print("invalid rating")