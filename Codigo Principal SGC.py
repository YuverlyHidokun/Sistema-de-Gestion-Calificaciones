#LIBRERIAS
from prettytable import PrettyTable  #Tablas
import getpass  #Cifrar contraseña
from os import system

#CONSTANTES
USUARIOS = ['docente@esfot.edu.ec', 'a']
CONTRASENAS = ['Docente2023*', 'a']

#VARIABLES
aux = True

# Agregar variables para rastrear los algoritmos
algoritmo_ordenamiento = None
algoritmo_busqueda = None


#FUNCIONES
#Función Iniciar Sesion
def iniciarSesion():
  print('\t\tSistema de Gestión de Calificaciones\n')
  while True:
    usuario = input("Ingrese su nombre de usuario: ")
    contrasena = getpass.getpass("Ingrese su contraseña: ")
    system('clear')
    # Verificar si el usuario y la contraseña coinciden con alguna credencial válida
    for i in range(len(USUARIOS)):
      if USUARIOS[i] == usuario and CONTRASENAS[i] == contrasena:
        print(f'Inicio de sesión exitoso.\n\n\t¡Bienvenido, {usuario} !\n')
        return
    print('Nombre de usuario o contraseña incorrectos.\nIntente de nuevo.\n')


#Función Menú Principal
def menu():
  while True:
    print('******** Modulo del docente ********')
    print('Menú Principal')
    print('\t1.- Registrar datos.')
    print('\t2.- Ordenar calificaciones')
    print('\t3.- Buscar calificación.')
    print('\t4.- Salir del sistema.')
    opcion = input('Ingrese una opción: ')
    system('clear')
    if opcion in ['1', '2', '3', '4']:
      return opcion
    else:
      print('\nOpción incorrecta, intente de nuevo.\n')


#Función Menú Ordenamiento
def menuDeOrden():
  while True:
    print('******** MENÚ DE ORDEN ********')
    print('\t1.- Burbuja.')
    print('\t2.- Heap Sort.')
    print('\t3.- Merge Sort.')
    print('\t4.- Quick Sort.')
    print('\t5.- Shell Sort.')
    opcion = input('Ingrese una opción: ')
    if opcion in ['1', '2', '3', '4', '5']:
      return opcion
    else:
      print('\nOpción incorrecta, intente de nuevo.\n')


#Función Menú Busqueda
def menuDeBusqueda():
  while True:
    print('******** MENÚ DE BUSQUEDA ********')
    print('\t1.- Lineal.')
    print('\t2.- Binaria.')
    print('\t3.- Interpolación.')
    print('\t4.- Valor Mínimo')
    print('\t5.- Búsqueda Secuencial Mejorada')
    opcion = input('Ingrese una opción: ')
    if opcion in ['1', '2', '3', '4', '5']:
      return opcion
    else:
      print('\nOpción incorrecta, intente de nuevo.\n')


#Función para validar de palabras
def validarPalabras(mensaje):
  while True:
    frase = input(mensaje)
    if not any(char.isdigit() for char in frase):
      return frase
    else:
      print("\nEntrada inválida. Ingrese un palabras sin números.\n")


#Función para validar numeros
def validarNumerosEnteros(mensaje, inicio, fin):
  while True:
    entrada = input(mensaje)
    if entrada.isdigit():
      numero = int(entrada)
      if numero in range(inicio, fin):
        return numero
      else:
        print("\nNúmero fuera de rango. Intente de nuevo.\n")
    else:
      print("\nEntrada inválida. Ingrese un número válido.\n")


#Funcion para validar numeros decimales
def validarNumero(mensaje, inicio, fin):
  while True:
    entrada = input(mensaje)
    try:
      numero = float(entrada)
      if inicio <= numero <= fin:
        return numero
      else:
        print("\nNúmero fuera de rango. Intente de nuevo.\n")
    except ValueError:
      print("\nEntrada inválida. Ingrese un número válido.\n")


#Función para registrar Profesor
def regProfe():
  print('******** Datos profesor *********\n')
  nombreProfesor = validarPalabras('Ingrese su nombre (Docente): ')
  apellidoProfesor = validarPalabras('Ingrese su apellido (Docente): ')
  universidad = validarPalabras('Ingrese la universidad: ')
  semestre = validarNumerosEnteros('Ingrese el semestre: ', 1, 6)
  materia = validarPalabras('Ingrese la materia a impartir: ')
  return nombreProfesor, apellidoProfesor, universidad, semestre, materia


#Función para registrar Alumnos
def registrarDatosAlumnos(arreglo, n):
  arreglo.append([])
  arreglo[n].append(n + 1)
  print(f'\n******** ESTUDIANTE {n+1} ********\n')
  nombreEstudiante = validarPalabras(
      f'Ingrese el nombre del estudiante {n+1}: ')
  arreglo[n].append(nombreEstudiante)
  apellidoEstudiante = validarPalabras(
      f'Ingrese el apellido del estudiante {n+1}: ')
  arreglo[n].append(apellidoEstudiante)
  correoEstudiante = input(f'Ingrese el correo del estudiante {n+1}: ')
  arreglo[n].append(correoEstudiante)
  notaUnoEstudiante = validarNumero(
      f'Ingrese la primera nota del estudiante {n+1}: ', 0, 21)
  arreglo[n].append(notaUnoEstudiante)
  notaDosEstudiante = validarNumero(
      f'Ingrese la segunda nota del estudiante {n+1}: ', 0, 21)
  arreglo[n].append(notaDosEstudiante)
  promedioEstudiante = (notaUnoEstudiante + notaDosEstudiante) / 2
  arreglo[n].append(promedioEstudiante)


#Función crear la tabla
def crearTabla(arreglo):
  tab = PrettyTable()
  tab.field_names = [
      'N°', 'Estudiante', 'Apellido', 'Correo', 'Nota 1', 'Nota 2', 'Promedio'
  ]
  for i in range(len(arreglo)):
    tab.add_row(arreglo[i])
  return tab


#Función archivo calificaciones
def archivoCalificaciones(institucion, periodo, asignatura, tab, promedioTotal,
                          aprobados, suspenso, reprobados, nombreProf,
                          apellidoProf):

  arch = open('BDD/calificaciones.txt', 'w')
  arch.write(" " * 27 + f'COLEGIO o UNIVERSIDAD {institucion}\n')
  arch.write(" " * 28 + 'Reporte de calificaciones\n')
  arch.write('\n')
  arch.write(f'Año electiva o semestre: {periodo}\n')
  arch.write(f'Materia: {asignatura}\n\n')
  arch.write(str(tab))
  arch.write('\n\n')
  arch.write('Resumen\n')
  arch.write(f'Promedio del curso: {promedioTotal}\n')
  arch.write(f'Aprobados (14 - 20): {aprobados}\n')
  arch.write(f'Suspenso (08,01 - 13,99): {suspenso}\n')
  arch.write(f'Reprobados (00 - 08): {reprobados}\n')
  arch.write('\n\n\n')
  arch.write(" " * 27 + '____________________________\n')
  arch.write(" " * 27 + 'Docente\n')
  arch.write(" " * 27 + f'{nombreProf}\n')
  arch.write(" " * 27 + f'{apellidoProf}')
  arch.close()
  return arch


# Implementación del algoritmo de Burbuja (Bubble Sort)
def bubbleSort(arreglo):
  n = len(arreglo)
  for i in range(n - 1):
    for j in range(0, n - i - 1):
      if arreglo[j][6] > arreglo[j + 1][6]:
        arreglo[j], arreglo[j + 1] = arreglo[j + 1], arreglo[j]


# Implementación del algoritmo de Inserción (Insertion Sort)
def insertionSort(arreglo):
  for i in range(1, len(arreglo)):
    key = arreglo[i]
    j = i - 1
    while j >= 0 and arreglo[j][6] > key[6]:
      arreglo[j + 1] = arreglo[j]
      j -= 1
    arreglo[j + 1] = key


# Implementación del algoritmo de Shell Sort
def shellSort(arreglo):
  n = len(arreglo)
  gap = n // 2
  while gap > 0:
    for i in range(gap, n):
      temp = arreglo[i]
      j = i
      while j >= gap and arreglo[j - gap][6] > temp[6]:
        arreglo[j] = arreglo[j - gap]
        j -= gap
      arreglo[j] = temp
    gap //= 2


# Implementación del algoritmo de Selección (Selection Sort)
def selectionSort(arreglo):
  for i in range(len(arreglo)):
    min_idx = i
    for j in range(i + 1, len(arreglo)):
      if arreglo[j][6] < arreglo[min_idx][6]:
        min_idx = j
    arreglo[i], arreglo[min_idx] = arreglo[min_idx], arreglo[i]


# Implementación del algoritmo de Fusión (Merge Sort)
def mergeSort(arreglo):
  if len(arreglo) > 1:
    mid = len(arreglo) // 2
    left_half = arreglo[:mid]
    right_half = arreglo[mid:]

    mergeSort(left_half)
    mergeSort(right_half)
    i = j = k = 0
    while i < len(left_half) and j < len(right_half):
      if left_half[i][6] < right_half[j][6]:
        arreglo[k] = left_half[i]
        i += 1
      else:
        arreglo[k] = right_half[j]
        j += 1
        k += 1

    while i < len(left_half):
      arreglo[k] = left_half[i]
      i += 1
      k += 1

    while j < len(right_half):
      arreglo[k] = right_half[j]
      j += 1
      k += 1


# Implementación del algoritmo Rápido (Quick Sort)
def quickSort(arreglo):
  if len(arreglo) <= 1:
    return arreglo
  else:
    pivot = arreglo[0]
    lesser = [x for x in arreglo[1:] if x[6] <= pivot[6]]
    greater = [x for x in arreglo[1:] if x[6] > pivot[6]]
    return quickSort(lesser) + [pivot] + quickSort(greater)


def guardarArchivoOrdenamiento(nombreProfesor, apellidoProfesor, algoritmo,
                               calificacionesOrdenadas, universidad):
  archivo = open('BDD/ordenamiento.txt',
                 'w')  # Ruta relativa al directorio actual
  # Cabecera
  archivo.write(" " * 27 + f"COLEGIO o UNIVERSIDAD {universidad}\n")
  archivo.write(" " * 27 + "REPORTE DE CALIFICACIONES\n")
  archivo.write("-" * 85 + "\n")
  archivo.write(f"Calificaciones Ordenadas\nALGORITMO: {algoritmo}\n")
  archivo.write("-" * 85 + "\n")

  # Contenido de calificaciones ordenadas
  for i, calificacion in enumerate(calificacionesOrdenadas):
    archivo.write(f"N°-{i + 1} |{calificacion}|-"
                  )  # Agrega las calificaciones ordenadas aquí
  archivo.write("\n")

  # Pie de página
  archivo.write(" " * 44 + "_" * 37 + "\n")
  archivo.write(" " * 53 + "Docente\n")
  archivo.write(" " * 56 + "_" * 12 + " " * 2 + "_" * 11 + "\n")
  archivo.write(" " * 62 + nombreProfesor + " " * 2 + apellidoProfesor + "\n")

  archivo.close()


def buscarCalificacion(datosEstudiantes, calificacion, algoritmo):
  resultados = []
  if algoritmo == '1':  # Busqueda lineal
    for estudiante in datosEstudiantes:
      if estudiante[6] == calificacion:
        resultados.append(estudiante)
  elif algoritmo == '2':  # Busqueda binaria
    datosEstudiantes.sort(
        key=lambda x: x[6])  # Ordena los datos por calificacion
    resultados = binaria(datosEstudiantes, calificacion)
  elif algoritmo == '3':  # Búsqueda por Interpolación
    datosEstudiantes.sort(
        key=lambda x: x[6])  # Ordena los datos por calificacion
    resultados = interpolacion(datosEstudiantes, calificacion)
  elif algoritmo == '4':  # Búsqueda por Valor minimo o por anchura)
    resultados = anchura(datosEstudiantes, calificacion)

  return resultados


# Modificada la función busquedaBinaria
def binaria(arr, x):
  low = 0
  high = len(arr) - 1
  resultados = []

  while low <= high:
    mid = (low + high) // 2
    if arr[mid][6] == x:
      resultados.append(arr[mid])
      # Moverse a la izquierda y derecha para buscar más estudiantes con la misma calificación
      left = mid - 1
      right = mid + 1
      while left >= 0 and arr[left][6] == x:
        resultados.append(arr[left])
        left -= 1
      while right < len(arr) and arr[right][6] == x:
        resultados.append(arr[right])
        right += 1
      return resultados
    elif arr[mid][6] < x:
      low = mid + 1
    else:
      high = mid - 1

  return resultados


# Modificada la función interpolacion
def interpolacion(arr, x):
  low = 0
  high = len(arr) - 1
  resultados = []

  while low <= high and x >= arr[low][6] and x <= arr[high][6]:
    if low == high:
      if arr[low][6] == x:
        resultados.append(arr[low])
      return resultados

    pos = low + int(((float(high - low) / (arr[high][6] - arr[low][6])) *
                     (x - arr[low][6])))
    if arr[pos][6] == x:
      resultados.append(arr[pos])
      # Moverse a la izquierda y derecha para buscar más estudiantes con la misma calificación
      left = pos - 1
      right = pos + 1
      while left >= 0 and arr[left][6] == x:
        resultados.append(arr[left])
        left -= 1
      while right < len(arr) and arr[right][6] == x:
        resultados.append(arr[right])
        right += 1
      return resultados

    if arr[pos][6] < x:
      low = pos + 1
    else:
      high = pos - 1

  return resultados


# Función para realizar la búsqueda en anchura (valor mínimo)
def anchura(arr, x):
  resultados = []
  min_calificacion = float('inf')

  for estudiante in arr:
    if estudiante[6] < min_calificacion:
      min_calificacion = estudiante[6]
      resultados = [estudiante]
    elif estudiante[6] == min_calificacion:
      resultados.append(estudiante)

  return resultados


# Función para guardar los resultados en un archivo
def guardarResultados(institucion, algoritmo, calificacion, resultados,
                      nombreProf, apellidoProf):
  algoritmo_nombres = {
      '1': 'Busqueda Lineal',
      '2': 'Busqueda Binaria',
      '3': 'Busqueda por Interpolacion',
      '4': 'Busqueda por Valor Minimo'
  }
  algoritmo_nombre = algoritmo_nombres.get(algoritmo, 'Desconocido')
  archivo_busqueda = open('BDD/busqueda.txt', 'w')
  archivo_busqueda.write(
      f'                       COLEGIO o UNIVERSIDAD {institucion} \n')
  archivo_busqueda.write('                       Reporte de calificaciones\n')
  archivo_busqueda.write('\n')
  archivo_busqueda.write(
      '--------------------------------------------------------------------\n')
  archivo_busqueda.write('Busqueda de Calificaciones\n')
  archivo_busqueda.write(
      f'ALGORITMO: {algoritmo_nombre}\n')  # Usar el nombre del algoritmo
  archivo_busqueda.write(
      '--------------------------------------------------------------------\n')
  archivo_busqueda.write(f'La calificacion a buscar fue de: {calificacion}\n')
  if len(resultados) > 0:
    archivo_busqueda.write('Corresponde al/los estudiante/s:\n')
    for estudiante in resultados:
      archivo_busqueda.write(f'Nombre: {estudiante[1]} {estudiante[2]}\n')
      archivo_busqueda.write(f'Correo: {estudiante[3]}\n')
  else:
    archivo_busqueda.write('No se encontraron resultados.\n')
  archivo_busqueda.write('\n\n\n')
  archivo_busqueda.write(
      '                        ____________________________\n')
  archivo_busqueda.write(
      '                                   Docente           \n')
  archivo_busqueda.write(f'                                {nombreProf} ')
  archivo_busqueda.write(f'{apellidoProf}')
  archivo_busqueda.close()


# Función para mostrar los resultados en la consola
def mostrarResultados():
  with open('BDD/busqueda.txt', 'r') as archivo_busqueda:
    contenido = archivo_busqueda.read()
    print(contenido)


#Función leer archivos
def leerArchivos(arch, direccion):
  arch = open(direccion, 'r')
  documento = arch.read()
  print(documento)
  arch.close()


#Función principal
def main():
  datosEstudiantes = []
  numeroTotalEstudiantes = 0
  aprobados = 0
  suspenso = 0
  reprobados = 0
  promedioCurso = 0
  opcion_ordenamiento = None  # Variable para rastrear el algoritmo de ordenamiento
  opcion_busqueda = None  # Variable para rastrear el algoritmo de búsqueda
  banderaProfe = True

  iniciarSesion()

  while opcion_ordenamiento != '4':
    opcion_ordenamiento = menu()
    if opcion_ordenamiento == '1':
      while True:
        if banderaProfe:
          nombreProfesor, apellidoProfesor, universidad, semestre, materia = regProfe(
          )
          break
        else:
          actualizarDatos = validarPalabras(
              '¿Desea actualizar los datos del profesor (si/no)?: ')
          if actualizarDatos in ['si', 'SI', 'Si', 'sI']:
            banderaProfe = True
            regProfe()
            break
          elif actualizarDatos in ['no', 'NO', 'No', 'nO']:
            break
          else:
            print('\nOpción incorrecta, intente de nuevo.\n')
      banderaProfe = False

      numeroEstudiantesAIngresar = int(
          input('Ingrese los estudiantes a registrar: '))
      for i in range(numeroEstudiantesAIngresar):
        registrarDatosAlumnos(datosEstudiantes, numeroTotalEstudiantes)
        promedioCurso += datosEstudiantes[numeroTotalEstudiantes][6]
        if 0 <= datosEstudiantes[numeroTotalEstudiantes][6] <= 8:
          reprobados += 1
        elif 8 < datosEstudiantes[numeroTotalEstudiantes][6] < 14:
          suspenso += 1
        elif 14 <= datosEstudiantes[numeroTotalEstudiantes][6] <= 20:
          aprobados += 1
        numeroTotalEstudiantes += 1

      tabla = crearTabla(datosEstudiantes)
      archivoUno = archivoCalificaciones(universidad, semestre, materia, tabla,
                                         promedioCurso, aprobados, suspenso,
                                         reprobados, nombreProfesor,
                                         apellidoProfesor)

      leerArchivos(archivoUno, 'BDD/calificaciones.txt')

    elif opcion_ordenamiento == '2':
      if len(datosEstudiantes) == 0:
        print('No existen registros...')
      else:
        opcion_busqueda = menuDeOrden()
        if opcion_busqueda == '1':
          bubbleSort(datosEstudiantes)
          algoritmo_ordenamiento = 'Burbuja'
        elif opcion_busqueda == '2':
          insertionSort(datosEstudiantes)  # Llama a Insertion Sort
          algoritmo_ordenamiento = 'Heap Sort.'  # Actualiza el algoritmo
        elif opcion_busqueda == '3':
          mergeSort(datosEstudiantes)
          algoritmo_ordenamiento = 'Merge Sort'
        elif opcion_busqueda == '4':
          quickSort(datosEstudiantes)
          algoritmo_ordenamiento = 'Quick Sort'
        elif opcion_busqueda == '5':
          shellSort(datosEstudiantes)  # Llama a Shell Sort
          algoritmo_ordenamiento = 'Shell Sort'  # Actualiza el algoritmo
        tabla = crearTabla(datosEstudiantes)
        archivoOrdenamiento = archivoCalificaciones(
            universidad, semestre, materia, tabla, promedioCurso, aprobados,
            suspenso, reprobados, nombreProfesor, apellidoProfesor)
        guardarArchivoOrdenamiento(
            nombreProfesor, apellidoProfesor, algoritmo_ordenamiento,
            [estudiante[6] for estudiante in datosEstudiantes], universidad)
        leerArchivos(archivoOrdenamiento, 'BDD/ordenamiento.txt')
        

    elif opcion_ordenamiento == '3':
      if len(datosEstudiantes) == 0:
        print('No existen registros...')
      else:
        opcion_busqueda = menuDeBusqueda()
        if opcion_busqueda in ['1', '2', '3', '4', '5']:
          # Solicitar al usuario la calificación a buscar
          calificacion = validarNumero('Ingrese la calificación a buscar: ', 0,
                                       21)
          resultados = buscarCalificacion(datosEstudiantes, calificacion,
                                          opcion_busqueda)
          guardarResultados(universidad, opcion_busqueda, calificacion,
                            resultados, nombreProfesor, apellidoProfesor)
          mostrarResultados()

  print('')
  print('Saliendo del sistema....\n')
  print('Muchas gracias.')


main()
