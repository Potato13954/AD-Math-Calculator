

print("welcome to temperature converter")
start = input("Will you convert celcius to farenheit: type 1 or farenheit to celcius: type 2 ")
if start == "1":
    num = float(input("what is your value to convert from celcius to farenheit: "))
    num2 = num * 9/5
    num2 = num + 32
    print("The value of " + str(num) + " farenheit is "  + str(num2) +  " celcius")

if start ==  "2":
    num = float(input("what is your value to convert from farenheit to celcius: "))
    num2 = num - 32
    num3 = num2 * 5/9
    print("The value of " + str(num) + " farenheit is "  + str(num3) +  " celcius")

while start != "1" and start != "2":
    print("error, retry")
    start = input("Will you convert celcius to farenheit: type 1 or farenheit to celcius: type 2 ")
    break;

if start ==  "2":
        num = float(input("what is your value to convert from farenheit to celcius: "))
        num2 = num - 32
        num3 = num2 * 5/9
        print("The value of " + str(num) + " farenheit is "  + str(num3) +  " celcius")

if start == "1":
    num = float(input("what is your value to convert from celcius to farenheit: "))
    num2 = num * 9/5
    num2 = num + 32
    print("The value of " + str(num) + " farenheit is "  + str(num2) +  " celcius")




