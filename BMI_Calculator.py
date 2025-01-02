name=input("Enter the name:")
weight_kg=int(input("Enter his/her weight: "))
height_m=float(input("Enter his/her height: "))
bmi=weight_kg/height_m**2
def bmi_calc(name,weight_kg,height_m):
    print(f"BMI={bmi}")
    if bmi<25:
        return name + " is not overweight"
    else:
        return name + " is overweight"
print(bmi_calc(name, weight_kg, height_m))