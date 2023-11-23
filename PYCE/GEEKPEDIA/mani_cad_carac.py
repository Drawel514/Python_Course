"""MANIPULCAION DE CADENAS DE CARACTERES"""

"""ASIGNACION ( OPERADOR: += ):consiste en asiganr una cadena de caracteres a otra """

mensaje = "Oh muerte"
mensaje += " "
mensaje += "Yo sere tu muerte;"
mensaje += " "
mensaje += "Y sere tu destruccion"
print(mensaje)


""" CONCATENACION ( OPERADOR: + ): Es una operacion que consiste en unir dos cadenas o mas, para formar una cadena de mayor tamaño. """

p_m = "Los cielos cuentan la gloria de Dios "
s_m = "y el firmamento anuncia la obra de sus manos "
t_m = "SALMOS 19:1"
print(p_m + s_m + t_m)


"""LA BUSQUEDA ( Metodo: find ): Consiste en localizar dentro de una cadena, una subcadena mas pequeña a un caracter."""

mensaje = "Jesus is King"
B_SubCadena = mensaje.find("King")

print(B_SubCadena)
"""Este imprime la posicion en la cual inicia la subcadena"""


"""LA ESTRACCION( Posicion a extraer[inicial : final] ): Se trata de sacar fuera de una cadena, una porcion de la misma segun su posicion dentro de ella."""

Texto = "Nada es verdad, todo esta permitido"
Extract_Text = Texto[0:14]
print(Extract_Text)




"""LA COMPARACION ( OPERADOR: ==): Se utiliza para comparar dos cadenas de caracteres."""

"""EJEMPLO:1"""
masseg1 = "ELOHIM"
masseg2 = "SHADAY"
comparacion = masseg1==masseg2
print (comparacion)

"""EJEMPLO:2"""
masseg1 = "ELOHIM"
masseg2 = "ELOHIM"
comparacion = masseg1==masseg2
print (comparacion)








 




