numerosecreto = 333
print("""
      +======================================================================================================================+
      Bienvenido/a a la cueva del mago!
      Para poder desbloquear este camino, deberás utilizar el poder de la adivinación para saber en que número estoy pensando!
      Caso contrario, estarás atrapado hasta que utilices la cabeza!
      +======================================================================================================================+
      """)
numerodeusuario = int(input("Aventurero! Ingresa un número: "))
while numerodeusuario != numerosecreto:
    print("¡Ja, ja! ¡Estás atrapado en mi bucle! Piensa aventurero, te daré una pista, mi número es el mismo, repetido 3 veces...")
    numerodeusuario = int(input("Aventurero! Ingresa un número: "))
if numerodeusuario == numerosecreto:
    print("¡Bien hecho, Junior! Eres libre ahora. Pero cuidate, siempre estoy vigilando!")