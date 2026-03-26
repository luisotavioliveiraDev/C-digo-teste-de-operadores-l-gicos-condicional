

numero = float(input("Digite um numero: ")) #variavel numero (float) ---> variavel real
resultado = (numero%2) #terminando a variavel que da o valor de divisão (%) ---> retorna o resto da divisão
if (resultado == 0): # caso seja resultado seja zero
  print(" seu numero é par") # retorna par
else: # qualquer outro resultado que não seja 0
  print(" seu numero é impar") # retorna impar

base = float(input("digite o numero da base:")) # declarando a variavel
expoente = float(input("digite o numero do expoente:"))
resultado = float (base**expoente) # declarando a variavel de calculo (**) ---> expoenciação
print(resultado)
