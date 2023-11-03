# My Solution
target = int(input())

total = 0

for number in range(2, target + 1, 2):
  total += number
  
print(total)


# Course Alternative Solution
target = int(input())

alternative_sum = 0

for number in range(1, target + 1):
  if number % 2 == 0:
    alternative_sum += number

print(alternative_sum)
