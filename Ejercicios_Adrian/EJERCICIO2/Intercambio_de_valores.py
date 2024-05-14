def intercambiar_palabras():
    
    A = input("Ingrese la primera palabra (A): ")
    B = input("Ingrese la segunda palabra (B): ")

    print(f"Originalmente, A = {A} y B = {B}")
 
    A, B = B, A

    print(f"Después del intercambio, A = {A} y B = {B}")

intercambiar_palabras()
