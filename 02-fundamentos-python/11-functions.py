
# Parametros
# def hello(greet="Hola", name="Invitado"):
#     print(f"{greet}, {name}")
    
# hello("Hola, buenos dias", "Cesar")
# hello("Ciao", "Eduardo")
# hello()
# hello(name='Teddy', greet='Hello')


def big_fuction(*args, **kwargs):
    print(args)
    print(kwargs)
    return kwargs

print(big_fuction(1,2,4,5,6,7, num1=77, num2=100))



