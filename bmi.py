def calculate_bmi(height, weight):
 print("Height = " + str(height))
 print("Weight = " + str(weight))

 bmi = weight/(height * height)
 
 classification = "Under Weight"  if bmi < 18.5 else ("Over Weight" if bmi > 25.0  else "Normal Weight")

 print("Your BMI is : " + str(bmi))
 print("You are "+classification)
 
 if bmi < 18.5 : return -1
 elif bmi > 25.0: return 1
 else: return 0

print(calculate_bmi(1.73, 120))
