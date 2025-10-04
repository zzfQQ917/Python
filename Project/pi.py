import math

while True:
    def circumference():
        pi = math.pi
        return pi

    def area():
        radius = int(input("Which amount of the radius would you like to put?"))
        utilization = circumference()
        equation = (radius * radius) * utilization
        print(f"This is the result of your area calculation: {equation}")

    ask = input("Want to calculate the area? ( Yes / No ): ")
    if ask == "Yes":
        area()
        question = input("Want to continue the program? ( Yes / No ): ")
        if question == "Yes":
            continue
        else:
            print("Ok, quit the program. ")
            break
    else:
        print("Ok, quit the program. ")
        break

