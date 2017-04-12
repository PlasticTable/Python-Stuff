#FAULTY
def is_prime(x):
  if x < 2:
    return False
  else:
    return prime_calc(x, 2)
  
  
def prime_calc(n, a):
  if n % a == 0 and n > a:
    return False
    prime_calc(n, a+1)
  else:
    return True
    prime_calc(n, a+1)


print is_prime(2) #True
print is_prime(4) #False
print is_prime(3) #True
print is_prime(9) #False FAULTY FUNCTION
print is_prime(10) #False
print is_prime(0) #False
