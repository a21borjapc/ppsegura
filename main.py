import requests

import backup


# función para leer el archivo flow.txt
def procesar_data(d):
    if d is not None:
        datos = d.split('|')
        operador = datos[0]
        comando1 = datos[1]
        comando2 = datos[2]
        comando3 = datos[3]
        resultado = operador, comando1, comando2, comando3
    return resultado

# Recuperamos los datos
if __name__ == '__main__':
    # repositorio
    res = requests.get('https://raw.githubusercontent.com/a21borjapc/ppsegura/main/flow.txt')
    #  datos
    datos = procesar_data(res.text)
    # separar partes separadas por :
    isBackup = datos[1].split(':')[1]
    isSent = datos[2].split(':')[1]
    isAuth = datos[3].split(':')[1]
    # imprimimos las acciones detectadas
    print("Backup: ", isBackup)
    print("Enviar?: ", isSent)
    print("Autorizado:",isAuth)

    if int(isBackup) == 1 and int(isAuth) == 1:
        backup.backuptoZip('data')
    else:
        print('El proceso de copia de seguridad esta deshabilitado')
