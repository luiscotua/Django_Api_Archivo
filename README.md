# Django_Api_Archivo
Repositorio de proyecto con Django REST framework para la administración de archivos .csv mediante un CRUD. La API permiter Listar, Descargar, Añadir y Eliminar un archivo .csv ademas permite consultar este por filtros y ordenamiento.

## Dependencias
Revisar el fichero `requirements.txt` el cual tienen todas las librerias y demas configuraciones usados en el proyecto

```
 django==2.2
 djangorestframework==3.11.0
 Markdown==3.2.1
 django-filter==2.2.0
 django-widget-tweaks==1.4.5
 httpie==2.2
 django-rest-auth==0.9.5
```
#### Recuerden generar y aplicar migraciones.
```
python manage.py makemigrations
python manage.py migrate
```
#### Correr el servidor a través del comando
 ```
 python manage.py runserver
 ```
## Credenciales de acceso a la API
La API cuenta con autenticacion por Token, las credenciales de acceso son:
```
Nombre Usuario: usuario
Contraseña: prueba2020
Token: a3a5bac09f4563547d8fc0fe039af1982226be5a
```
## Administrar API
Para acceder a la API Roo se utiliza la siguiente url `http://127.0.0.1:8000/api/` la cual listará las viws que gestiona esta API y que son:
```
"users": "http://127.0.0.1:8000/api/users/",
"groups": "http://127.0.0.1:8000/api/groups/",
"clasificadores": "http://127.0.0.1:8000/api/clasificadores/"
```
En cada unas de estas vistas se puede realizar la gestion del CRUD, solo es acceder a ellas.

## Administrar archivos .csv
#### Listar
Para ver el contenido del archivo .csv con id 2, se usa la url `http://127.0.0.1:8000/clasificadordata/2`, si se quiere acceder a otro archivo solo es cambiar el id.

#### Filtrar
Para filtar o buscar un dato en especifico en el contenido del archivo .csv se utilizan las siguientes url. Por nombre, `http://127.0.0.1:8000/clasificadordata/2?filtrar=luis`, o por el campo año `http://127.0.0.1:8000/clasificadordata/2?filtrar=23`, esto teniendo en ceunta la estructura del archivo .csv que se esta usando.
 
#### Ordenar
Para ordenar el contenido del archivo se ha de tener en cuenta los atributos de este y se pasan por la url así: por el nombre `http://127.0.0.1:8000/clasificadordata/2?ordenar=nombre` o por edad `http://127.0.0.1:8000/clasificadordata/2?ordenar=edad`,todo de manera ascendente. Si se desea ordenar de manera descentente, `http://127.0.0.1:8000/clasificadordata/2?ordenar=edad&des=true`

