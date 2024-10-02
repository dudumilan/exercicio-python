def fizzbuzz(numero):
  """
  A definição do FizzBuzz é a seguinte:
    1. Se o número é divisível por 3, fale “Fizz”.
    2. Se o número é divisível por 5, fale “Buzz”.
    3. Se o número é divisível por 3 e 5, fale “FizzBuzz”.
    4. Se número não é divisível nem por 3 nem por 5, fale o próprio número

  Entrada: Um número inteiro positivo

  Saída: A string "Fizz", "Buzz", "FizzBuzz" ou o próprio número
  """
  if numero % 3 == 0 and numero % 5 == 0:
    return "FizzBuzz"
  elif numero % 3 == 0:
    return "Fizz"
  elif numero % 5 == 0:
    return "Buzz"
  else:
    return numero