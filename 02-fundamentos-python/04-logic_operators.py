
# and
age = 18
licensed = False

if age >= 18 and licensed:
    print("Puedes manejar")


# or
is_student = False
membershipt = False

if is_student or membershipt:
    print("Obtiene precio especial")
    
# not

is_admin = True

if not is_admin:
    print("Acceso denegado")
    
# Short Circuiting
name = False
print(name and name.upper())



