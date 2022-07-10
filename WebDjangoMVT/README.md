# Web Django
Esta, es una página web básica de **mascotas**, tiene las siguientes características que permite ingresas datos de los principales modelos (mascota, cliente, veterinario) así como buscar mascotas en base a su nombre y desplegar los datos de las mascotas con nombre similar:

## Modelos:
Mascota:

| Campos | Descripción                                   |
|--------|------------------------------------|
| Nombre | Nombre de la mascota               |
| Edad   | Edad de la mascota                 |
| Tipo   | Tipo de mascota (perro, gato, etc.)|

Cliente:

| Campos | Descripción                                   |
|--------|------------------------------------|
| Nombre | Nombre de la mascota               |
| Apelido   | Edad del cliente                |
| Email   | Email del cliente                 |

Veterinario:

| Campos | Descripción                                   |
|--------|------------------------------------|
| Nombre | Nombre del veterinario               |
| Especialidad   | Especialidad del veterinario (en perros, gatos, etc.)                |

## Templates:
| HTML | Descripción |
|------|-------------|
|inicio.html| Página de inicio |
|**padre.html**| *padre* del resto de páginas|
|cliente.html| Página de cliente
|clienteFormulario.html| Formulario de ingreso de datos del cliente |
|mascota.html| Página de mascota
|mascotaFormulario.html| Formulario de ingreso de datos de mascotas|
|veterinario.html| Página de veterinario|
|veterinarioFormulario.html| Formulario de Ingreso de datos del veterinario
| busquedaMascota.html| Busca las mascotas con un nombre similar al ingresado |
| resultadosBusqueda.html| Muestra el resultados de las búsqueda de las mascotas
