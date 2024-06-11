hora = int(input("digite uma hora(0-23): "))
if 0<= hora < 12:
    print("o horario é manhã.")
elif 12 <= hora <18:
    print("o horario é tarde.")
elif 18 <= hora < 24:
    print("o horario é noite.")        