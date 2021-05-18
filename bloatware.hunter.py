import os
import subprocess
import time
from datetime import date
from datetime import datetime
def inicio():
 os.system ("echo off")
 os.system ("color 1A")
 os.system ("cls")
 os.system ("title = Blotware.hunter 1.0")
def configuracion_inicial():
 global continuar
 continuar = False
 archivo_configuracion = open("configbh.ini",'r',-1,None,None,None)
 archivo_configuracion.readline()
 global adb_ubicacion
 adb_ubicacion = archivo_configuracion.readline()
def conectar():
 os.system (adb_ubicacion + " kill-server")
 os.system (adb_ubicacion + " devices")
 bucle_infinito = False
 while bucle_infinito == False:
  dispositivos_sin_filtrar = (subprocess.getoutput(adb_ubicacion + " devices"))
  os.system("cls")
  if len(dispositivos_sin_filtrar) != 25 and not("unauthorized" in dispositivos_sin_filtrar):
   dispositivo_id = dispositivos_sin_filtrar[25:37]
   os.system("cls")
   print ("Dispositivo con ID: " + dispositivo_id + " Conectado.")
   print ("Mostrando paquetes.....")
   aplicaciones_sin_filtrar = subprocess.getoutput(adb_ubicacion + " shell pm list packages")
   print ("--------------------------------------------------------------")
   time.sleep(1.5)
   aplicaciones_sin_filtrar = aplicaciones_sin_filtrar.replace("package:","")
   linea = "";
   aplicaciones_filtradas = []
   aplicaciones_filtradas = aplicaciones_sin_filtrar.split("\n")
   contador = 0
   for linea in aplicaciones_filtradas:
    print (str(contador) + ": " + linea)
    contador = contador + 1
   print ("--------------------------------------------------------------")
   print ("(Para salir cierre la ventana)")
   print ("Escribe numero a eliminar :",end=" ")
   try:
    num_aplicacion = int(input())
   except:
    print ("--------------------------------------------------------------")
    print ("No es un numero....")
    time.sleep(1)
    continue
   if num_aplicacion > len(aplicaciones_filtradas) or num_aplicacion < 0:
    print ("Opcion no valida....")
    time.sleep(3)
    continue
   print ("(Borrar aplicaciones del sistema puede hacer el dispositivo inservible.)")
   print ("Confirmar....(enter).",end="")
   input()
   print ("")
   exito_pregunta = subprocess.getoutput(adb_ubicacion + " shell pm uninstall -k --user 0 " + aplicaciones_filtradas[num_aplicacion])
   time.sleep(0.1)
   registro = "Paquete " + str(aplicaciones_filtradas[num_aplicacion]) + " Eliminado con exito."
   registrar_cadena(registro,dispositivo_id)
   if exito_pregunta == "Success":
     print ("Paquete : " + aplicaciones_filtradas[num_aplicacion] + " eliminado con exito.")
     time.sleep(0.5)
   else:
     print ("Error de borrado.....(puede ser que falta ejecutar como administrador o se desconecto),CERRANDO.")
     time.sleep(1)
     exit
   time.sleep(0.1)
  else:
   if len(dispositivos_sin_filtrar) == 25:
    print ("Error, dispositivo no detectado.Saliendo....")
    break
   elif "unauthorized" in dispositivos_sin_filtrar:
    print ("Error, de autorizacion.Saliendo....(Debe aparecer un mensaje de autorizacion en el telefono.")
    break
   else:
    print ("Error no indentificable....Saliendo.")
   time.sleep(3)
   break
   exit
def registrar_cadena(cadena,id_dispositivo):
 archivo_log = open("logbh.log","a")
 registrador = "Id del dispositivo : " + id_dispositivo + " Accion : " + cadena + " Fecha : "+ str(datetime.now()) + "\n"
 archivo_log.write(registrador)
inicio()
configuracion_inicial()
intro = """
Hola Este es un programa en python sobre windows para ELIMINAR el bloatware:
(El bloatware son las aplicaciones predeterminadas en android)
--------------------------------------------------------------
Este programa tiene cuatro requerimientos para funcionar:

-Dispositivo android conectado con privilegios de depuracion USB.
(Entras a modo desarrollador tocando 7 veces la version del software)

-Drivers android correspondientes a su dispositivo.
(Descargados por internet o instalados por el propio dispositivo)
  
-Drivers ADB (Android Debug Brigde).
(Sacados de internet....)

-Software ADB
(Sacados de internet....)
--------------------------------------------------------------
Licencia MIT.
Creado por: Luis Carlos Dena Cardenas.En 2021.
--------------------------------------------------------------
Para continuar escriba...."continuar" o para salir cierre la ventana:
"""
print (intro)
while continuar != True:
 print ("?:", end=" ")
 entrada = str(input())
 if entrada == "continuar":
  continuar = True
  os.system ("cls")
  conectar()
 else:
  os.system ("cls")
  intro = """
  --------------------------------------------------------------
  ¡ERROR NO SE ESCRIBIO LA PALABRA CORRECTA!
  --------------------------------------------------------------
  Para continuar escriba...."continuar" o para salir cierre la ventana:
  """
  print (intro)
