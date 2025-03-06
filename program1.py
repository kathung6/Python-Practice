# Function: converts celsius temperature to fahrenheit
# input: C temp
# return: rounded fahrenheit temp
def fahrenheit(C):
    nine_by_five = 9/5
    #converts celsius to fahrenheit, float type
    c_to_fahrenheit = float(((nine_by_five) * C) + 32)
    #rounds to the nearest tenth
    rounded_f = round(c_to_fahrenheit, 2)
    return rounded_f
    
#creates a list of celsius temps from 0-100
celsius_temps = list(range(0,101))

try:
    #prints each celsius temp and it's converted F temp
    for C in celsius_temps:
        converted = fahrenheit(C)
        #aligns the columns to be evenly spaced
        print("        ",C,"      ",converted)
except ValueError:
    print("error")