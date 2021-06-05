from complexNumbers import ComplexNumbers as Comp

# - Criar um número complexo;
num1 = Comp().createComplexNumber(1, 2)
num2 = Comp().createComplexNumber(3, 4)
print(f"Os numero complexos que foram criados foram: {num1} e {num2}")

# - Divisão dois números complexos.
print(f"Devisão: {Comp().divisionTwoComplexNumbers(num1, num2):.2f}")

# - Multiplicação dois números complexos;
print(f"Multiplicação: {Comp().multiplyingTwoComplexNumbers(num1, num2)}")

# - Conjugado de um número complexo;
print(f"Conjugado: {Comp().conjugateNumber(num1)}")
print(f"Conjugado: {Comp().conjugateNumber(num2)}")

# - Destruir um número complexo.
del(num1, num2) 
