def calculate_bmi(height,weight):
    print("Height: " + str(height))
    print("Weight: " + str(weight))
    bmi = weight/(height**2)
    print("bmi: " +str(bmi))
    if bmi <18.5:
        print("You are underweight")
    if bmi > 25.0:
        print("You are overweight")
    else:
        print("You are normal weight")
calculate_bmi(weight=57.0, height=1.73)