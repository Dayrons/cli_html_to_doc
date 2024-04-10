# Herramienta CLI para generar reportes

## Descripcion

Crea reportes automatizados mediante plantillas jinja2 con solo algunos comandos

## Instalacion

Si trabajas mendiante entorno virtual luego de crearlo en el proyecto

ejecuta el siguiente comando
```bash
pip install -r requirenment.txt
```
## Configuracion
El siguiente comando te pedira la ruta donde estaran ubicadas tus plantillas y la ruta donde se estaran exportando los documentos

```bash
python src/script.py config
```
o puedes ejecutar el comando ya indicando ambos parametros

```bash
python src/script.py config --path_templates ruta/a/tus/plantillas --path_export ruta/a/tu/directorio_de_exportacion
```


