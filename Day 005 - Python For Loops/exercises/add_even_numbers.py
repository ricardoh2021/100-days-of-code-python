target = int(input()) # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

# Write your code here 👇

#within the range 
evenTotal = 0

if 0 < target < 1000:
  for x in range(target + 1):
    if x%2 == 0:
      evenTotal+= x
    
print(evenTotal)
