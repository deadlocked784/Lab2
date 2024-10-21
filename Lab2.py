import numpy as np

def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")
       
def get_user_input():
    numbers = input()
    split = [int(num) for num in numbers.split(",")]
    return split

def calc_average_temperature(temperature): 
    return np.average(temperature)

def calc_min_max_temperature(temperature):
    mintemp = min(temperature)
    maxtemp = max(temperature)
    templist = [int(mintemp), int(maxtemp)]
    return templist

def calc_median_temperature(temperature):
    return np.median(temperature)

def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    print(calc_average_temperature(num_list))
    print(calc_min_max_temperature(num_list))
    print(calc_median_temperature(num_list))

if __name__ == "__main__":
    main()