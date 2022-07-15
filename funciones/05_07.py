def deudapendiente(deuda,cantidad):
    if (deuda >= cantidad):
        deuda = deuda - cantidad
        return deuda

deuda = deudapendiente(80000, 13000)

print(deuda)