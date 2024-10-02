def fibonacci(n):
  """
  funçao que calcula serie de fibonacci ate o n-esimo termo
  
  angs:
     n: numero de termos da serie de fibonacci
  
  returns:
    uma lista contendo os n primeiros termos da serie de fibonacci.
  """
  if n <= 0:
    return []
  elif n == 1:
    return [1]
  else:
    fib_list = [1, 1]
    while len(fib_list) < n:
      next_fib = fib_list[-1] + fib_list[-2]
      fib_list.append(next_fib)
      return fib_list