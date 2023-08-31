# STRINGS EN PYTHON.

my_first_string = "BIENVENIDO A, " # Primer string a imprimir.
my_second_string = 'VAMOS A HACER LO SIGUIENTE' # Segundo string a imprimir.

# PROBAREMOS CON ESTAS DOS SENTENCIAS DE CARACTERES.

#print(my_first_string, my_second_string)
#print('Entonces, compadre, ' + my_first_string + ' ' + my_second_string)

print(f'Entonces, compadre, {my_second_string} para no perder la mente en nuestra cabecita')

# PROBAREMOS CON OTRO STRING, QUE ESTE ES EL TERCERO DE ELLAS.

my_third_string = 'MALO'

# LO SEPARAREMOS POR 4 LETRAS CONSECUTIVAS POR LETRAS DEL ALFABETO COMO VARIABLES A ASOCIARSE:

a,b,c,d = my_third_string

# SE IMPRIME POR LÍNEAS CADA LETRA ASOCIADA.

print(a)
print(b)
print(c)
print(d)

# SE IMPRIME EN CONJUNTO LA SENTENCIA COMPLETA EN LETRAS.

print(f'{a}{b}{c}{d}')

# ESTO SERÍA INFINITO.

print(f'No, no estoy, {my_third_string}, porqué {my_third_string}')

# VAMOS A PRACTICAR CON ALGUNOS DE LOS STRINGS QUE SE ESTABLECERÁN EN MAYÚSCULAS O EN MINÚSCULAS.

print(my_first_string.upper()) # SERÁ SU STRING EN MAYÚSCULAS.
print(my_first_string.capitalize()) # SE ORDENA PRIMERO EN MAYÚSCULA Y LUEGO CON MINÚSCULAS.
print(my_first_string.lower()) # SU STRING SERÁ EN MINÚSCULAS (NINGUNA MAYÚSCULA).
print(len(my_first_string)) # CANTIDAD DE CARACTERES EN UN STRING.
print(my_first_string.find('f')) # ENCUENTRA UNA LETRA EN DONDE SE UBICA LA CADENA DE CARACTERES 'STRING'.

# HACEMOS LO MISMO PERO PROBAREMOS CON EL SEGUNDO STRING.

print(my_second_string.upper()) # SERÁ SU STRING EN MAYÚSCULAS.
print(my_second_string.capitalize()) # SE ORDENA PRIMERO EN MAYÚSCULA Y LUEGO CON MINÚSCULAS.
print(my_second_string.lower()) # SU STRING SERÁ EN MINÚSCULAS (NINGUNA MAYÚSCULA).
print(len(my_second_string)) # CANTIDAD DE CARACTERES EN UN STRING.
print(my_second_string.find('f')) # ENCUENTRA UNA LETRA EN DONDE SE UBICA LA CADENA DE CARACTERES 'STRING'.

# EL ÚLTIMO, PERO ESTA VEZ CON EL TERCER STRING.

print(my_third_string.upper()) # SERÁ SU STRING EN MAYÚSCULAS.
print(my_third_string.capitalize()) # SE ORDENA PRIMERO EN MAYÚSCULA Y LUEGO CON MINÚSCULAS.
print(my_third_string.lower()) # SU STRING SERÁ EN MINÚSCULAS (NINGUNA MAYÚSCULA).
print(len(my_third_string)) # CANTIDAD DE CARACTERES EN UN STRING.
print(my_third_string.find('c')) # ENCUENTRA UNA LETRA EN DONDE SE UBICA LA CADENA DE CARACTERES 'STRING'.