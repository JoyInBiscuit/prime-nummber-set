from math import sqrt

start_from = int(input("Start from: "))
end_with = int(input("End with: "))

current_number = start_from
prime_number_set = []

while current_number <= end_with:
  
  current_number_is_prime = True # Let's assume that for a moment.
  divider = 2
  divider_limit = int(sqrt(current_number)) # If 30 is dividable with 5 which will result 6, we don't need to check with 6.
  
  while divider <= divider_limit:
    
    if current_number % divider == 0:
      
      current_number_is_prime = False # Oh no, we assumed wrong.
      break # it's ok. We will just move away to the next number hoping that we can a find a prime.
    divider += 1
    
  if current_number_isprime == True:
    prime_number_set.append(current_number)
    
  current_number += 1
print(len(prime_number_set), "prime numbers found./n"prime_number_set)
