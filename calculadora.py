print("Bienvenido a la calculadora donde podras hacer las operaciones de suma, resta, multiplicación y división sobre dos digitos")

try:
    opcion=int(input("""
                 1.Sumar
                 2.Restar
                 3.Multiplicar
                 4.Dividir
                 >"""))
except ValueError:
    print("El valor introducido no es correcto, entre 1 y 4.")
    
try:
    num1=int(input("Introduzca el primer numero\n"))
    num2=int(input("Introduzca el segundo numero\n"))

except ValueError:
    print("No ha introducido un valor válido")
resultado=None
match opcion:
    
    case 1:
        from suma import sumar   
        resultado=sumar(num1, num2)
    case 2:
        from resta import restar
        resultado=restar(num1,num2)
    case 3:
        from multiplicar import multiplicar
        resultado=multiplicar(num1,num2)
    case 4:
        from division import dividir
        resultado=dividir(num1,num2)
    case _:
       ("No ha introducido un valor válido")

if resultado is not None:
    print("El resultado de la operacion es: " , resultado)     
