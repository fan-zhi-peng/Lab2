def calculate_bmi(height,weight):
    print("Height: " + str(height))
    print("Weight: " + str(weight))
    bmi = weight/(height**2)
    print("bmi: " +str(bmi))
    if bmi <18.5:
        print("You are underweight")
        return -1
    if bmi > 25.0:
        print("You are overweight")
        return 1
    else:
        print("You are normal weight")
        return 0
calculate_bmi(weight=57.0, height=1.73)