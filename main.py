'''Un alumno desea saber cual será su promedio general en las tres materias mas difíciles
que cursa y cual será el promedio que obtendrá en cada una de ellas. Estas materias se
evalúan como se muestra a continuación:
La calificación de Matemáticas se obtiene de la sig. manera:
Examen 90%
Promedio de tareas 10%
En esta materia se pidió un total de tres tareas.
La calificación de Física se obtiene de la sig. manera:
Examen 80%
Promedio de tareas 20%
En esta materia se pidió un total de dos tareas.
La calificación de Química se obtiene de la sig. manera:
Examen 85%
Promedio de tareas 15%
En esta materia se pidió un promedio de tres tareas.'''

cm = float(input("Ingrese calificacion de matematicas: "))
ca1 = float(input("Ingrese calificacion trabajo 1: "))
ca2 = float(input("Ingrese calificacion trabajo 2: "))
ca3 = float(input("Ingrese calificacion trabajo 3: "))
tarea = (ca1+ca2+ca3) / 3
prom1 = (cm * .90) + (tarea * .10)

cf = float(input("Ingrese calificacion de fisica: "))
tf1 = float(input("Ingrese calificacion trabajo 1: "))
tf2 = float(input("Ingrese calificacion trabajo 2: "))
tareaf = (tf1+tf2) / 2
prom2 = (cf * .80) + (tareaf * .20)

cq = float(input("Ingrese calificacion de quimica: "))
q1 = float(input("Ingrese calificacion trabajo 1: "))
q2 = float(input("Ingrese calificacion trabajo 2: "))
q3 = float(input("Ingrese calificacion trabajo 3: "))
tareaq = (q1+q2+q3) / 3
prom3 = (cq * .85) + (tarea * .15)

promgeneral = (prom1+prom2+prom3) / 3

print("Promedio matematicas: ",round(prom1,1))
print("Promedio fisica: ",round(prom2,1))
print("Promedio quimica: ",round(prom3,1))
print("Promedio general: ",round(promgeneral,1))


'''Una fabrica ha sido sometida a un programa de control de contaminación para lo cual
se efectúa una revisión de los puntos IMECA generados por la fabrica. El programa de
control de contaminación consiste en medir los puntos IMECA que emite la fabrica en
cinco días de una semana y si el promedio es superior a los 170 puntos entonces tendrá la
sanción de parar su producción por una semana y una multa del 50% de las ganancias
diarias cuando no se detiene la producción. Si el promedio obtenido de puntos IMECA es
de 170 o menor entonces no tendrá ni sanción ni multa. El dueño de la fabrica desea saber
cuanto dinero perderá después de ser sometido a la revisión.'''

p1 = int(input("Ingresa los puntos de contaminacion dia 1: "))
p2 = int(input("Ingresa los puntos de contaminacion dia 2: "))
p3 = int(input("Ingresa los puntos de contaminacion dia 3: "))
p4 = int(input("Ingresa los puntos de contaminacion dia 4: "))
p5 = int(input("Ingresa los puntos de contaminacion dia 5: "))

promedio = (p1 + p2 + p3 + p4 + p5) / 5


ganancia1 = float(input("Ingresa las ganancias del dia 1: "))
ganancia2 = float(input("Ingresa las ganancias del dia 2: "))
ganancia3 = float(input("Ingresa las ganancias del dia 3: "))
ganancia4 = float(input("Ingresa las ganancias del dia 4: "))
ganancia5 = float(input("Ingresa las ganancias del dia 5: "))


total = ganancia1 + ganancia2 + ganancia3 + ganancia4 + ganancia5

if promedio >= 170:
    multa = total * .5
else:
    multa = 0

print("El promedio de puntos imeca es: ",round(promedio,1))
print("La ganancia total de una semana es: $",total)
print("La perdida de dinero por la revision es: $",total - multa)
