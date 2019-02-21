#BMI = (weight in kg / height in meters squared )

def gather_info():
    height = float(input("what is your height ? (inches or meters"))
    weight = float(input("what is your height ? (ponnds or imperial"))
    system = input("Are your mesurements in metric or imperial units ?").lower().strip()
    return (height, weight, system)
def calculate_bmi(weight, height, system='metri'):
    if system == 'metric':
        bmi = (weight / (height ** 2))
    else
        bmi = 703 * (weight / (height ** 2) )
    return bmi
while true:
    height, weight , system = gather_info()
    if system.startswitch('i'):
        bmi = calculate_bmi(weight, system='imperial',height=height)
        print(f"your BMI is {bmi}")
        break
    elif system.stattswitch('m')
        bmi = calculate_bmi(weight, height)
        print(f"tour BMI is {bmi}")
        break
    else:
        print("Error: unknown measurements system . pleas provide metric or imperial units")
