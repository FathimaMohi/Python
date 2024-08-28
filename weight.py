def calculate_bmi(weight, height):
  bmi = weight / (height ** 2)
  if bmi < 18.5:
    return "Underweight"
  elif bmi < 24.9:
    return "Normal Weight"
  elif bmi < 29.9:
    return "Overweight"
  else:
    return "Obesity"
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))
bmi = calculate_bmi(weight, height)
print("Your BMI is:", round(weight / (height ** 2), 2))
print("Your weight category is:", bmi)
