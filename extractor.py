import os
import shutil

parent_Dir = os.getcwd()
#Obtener directorio actual donde se ejecuta el script
data = '/home/lowiz/Documents/example/'
#directorio donde esta la informacion
dir_Name_Extraidos = "Archivos_Extraidos"
#nombre de la carpeta para los datos extraidos
path_Extraidos = os.path.exists(dir_Name_Extraidos)
#variable para verificar la existencia de la carpeta
path_Final = parent_Dir+'/'+dir_Name_Extraidos
#varibale para el directorio final
dir_Extraidos = ''
#inicializacion de nombre de la carpeta para el bucle
carpetas = os.listdir(data)
#crear la lista donde esta la informacion

def crearDirExtraidos():
	path_Extraidos = os.path.join(parent_Dir, dir_Name_Extraidos)
	#unimos la direccion de la carpeta a crear
	os.mkdir(path_Extraidos)
	#hacemos la carpeta

def moverArchivos():
    try:
        for carpeta in carpetas:
            print('')
            print('Entrando en carpeta: ',carpeta)
            dir_Name = carpeta
	        #nombre de la carpeta
            directorio_A_Entrar = os.path.join(data, dir_Name)
	        #unimos la direccion de la carpeta a entrar
            os.chdir(directorio_A_Entrar)
            archivos = os.listdir()
            bandera = False
            #bandera para saber si encontro o no archivo especificado en la carpeta en curso
            for archivo in archivos:
                 if archivo.endswith('.pdf'):
                    #archivo de interes
                    bandera = True
                    print('Copiando archivo: ', archivo)
                    shutil.copy(archivo, path_Final)
                    os.chdir(path_Final)
                    print('Renombrando',archivo,' a: ',dir_Name)
                    os.rename(archivo, dir_Name)
            if bandera == False:
                print('No se encontraron archivos del formato especificado')
    except IOError:
        print('Ocurrio un error leyendo: ', path_Final)

if path_Extraidos == False:
    crearDirExtraidos()

moverArchivos()


