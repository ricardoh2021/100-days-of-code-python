# Write your code here 👇

#Print from 1 to 100. Use range(1,10)
for x in range(1,101):
  if x%3 == 0 and x%5 == 0:
    print("FizzBuzz")
  elif x%3 == 0:
    print("Fizz")
  elif x%5 == 0:
    print("Buzz")
  else:
    print(x)
  