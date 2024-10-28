def calculate_bmi(height, weight):
 print("Height = " + str(height))
 print("Weight = " + str(weight))

 bmi = weight/(height * height)
 
 classification = "Under Weight"  if bmi < 18.5 else ("Over Weight" if bmi > 25.0  else "Normal Weight")

 print("Your BMI is : " + str(bmi))
 print("You are "+classification)
 
 return -1 if classification == "Under Weight" else (1 if classification == "Over Weight"  else 0)


calculate_bmi(weight=57, height=1.73)