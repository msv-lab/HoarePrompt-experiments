lista = []
t = int(input())
for i in range(t):
    hora = input().split(':')
    hora_int = int(hora[0])
    if hora_int == 0:
        completa = f"{12}:{hora[1]} AM"
        lista.append(completa)
    elif hora_int > 0 and hora_int < 12:
        if hora_int > 9:
            completa = f"{hora_int}:{hora[1]} AM"
        else:
            completa = f"0{hora_int}:{hora[1]} AM"
        lista.append(completa)
    elif hora_int == 12:
        completa = f"{hora_int}:{hora[1]} PM"
        lista.append(completa)
    else:
        completa = f"0{hora_int - 12}:{hora[1]} PM"
        lista.append(completa)

for a in range(len(lista)):
    print(lista[a])
