#fatorial
def fatorial(n):
  if n == 0:
    return 1
  else:
    return n * fatorial(n-1)


#exponenciação
def potencia(base, expoente):
  if expoente == 0:
    return 1
  else:
    return base * potencia(base,expoente-1)

print(fatorial(3))
print(fatorial(5))
print(potencia(2,2))
print(potencia(2,4))
