#PAQUETES

"""
Son directorios donde se almaceneran modulos relacionados entre si.
Sirven para organizar y reutilizar los modulos o codigos

Se crea creando una carpeta que tenga un archivo __init__.py

La carpeta __psycache__ te la crea directamente y automaticamente la carpeta (paquete)
Se puede crear subpaquetes. Haciendo una carpeta dentro de la carpeta con el init anterior. Tienen que tener su propio init

"""

# PAQUETES DISTRIBUIBLES

"""
Permite empaquetar los modelos distribuiles y enviarlos

Hay que crear el paquete y luego instalarlo.

Cuando tengo un script q usa los modulos de un paquete y lo muevo, no lo puedo usar. Los paquetes distribuibles me permiten usarlo en el lugar donde lo mueva

Para esto tengo q crear donde lo quiera usar un file q se llama setup.py

En el archivo de setuo hay que ponerle informacion. 

Para seguir hay que clicker shift con click derecho en la carpeta donde se encuentra el file setup.py. Lo abris con powershell y ahi te aparece el lugar donde esta la carpeta.

En la ventana q power shell hay q escribir: python setup.py sdist
El sdist es para crear un paquete distribuible.

Cuando hago esto me crea: una carpeta dist y otra carpeta q termina en .egg/info.

La carpeta importante es la de dist de distribucion. Archivo comprimido con tar.gz

Abris de vuelta powershell y pones instruccion de: pip3 install ____(nombre del paquete)

Ahi puedo mover el paquete de modulos adonde quiera y va a funcionar siempre.

Para desistalarlo entro a power shell igual q antes y pongo: pip3 uninstall _______(nombre del paquete)

Si desistalo ya no te funciona si moves el modulo a otro lugar
"""