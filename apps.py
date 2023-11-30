def divisible (num):
    if (num % 3 == 0):
      print("Fizz")
    
    if (num % 5 == 0):
      print("Buss")

    if (num % 3 == 0 and num % 5 == 0):
      print("FizzBuzz")
    
    else:
       print("neither")
 
#divisible (20)

list = [6, 8, 10, 11, 14, 12, 15, 18, 20, 22, 23, 24, 35, 30, 36, 45, 50]

counter = 0
while (counter < len(list)):
    #print(numbers[counter])
    number = list[counter]
    divisible(number)
    counter = counter + 1