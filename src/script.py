import click
import pdfkit
from jinja2 import Environment, FileSystemLoader
import json
from models.config import Config
import os



@click.group()
def main():
    pass

@main.command()
@click.option('--template', prompt='Nombre del template', help='Nombre del template con el que se generara el reporte(template.html)')
@click.option('--file_output', prompt='Nombre del salida', help='Nombre de exportacion del archivo(reporte.pdf)')
@click.option('--variables', default="{}", prompt='Variables para la plantilla', help='Variables para la plantilla en formato JSON.')
def generate_report(template, file_output, variables):
    
    if not Config.select().count():
        click.echo(click.style("No has configurado la ruta de las plantillas y la ruta de exportación. Ejecuta el comando config para configurarlas.", fg='red'))
        return

    try:
            config = Config.get(Config.id==1)
            export_path = os.path.join(config.path_export, file_output)
            
            env = Environment(loader=FileSystemLoader(config.path_templates))
            template = env.get_template(template)


            variables_dict = json.loads(variables)
            html = template.render(variables_dict)

            
            pdfkit.from_string(html, export_path)
            click.echo(click.style(f"Archivo PDF generado con éxito: {export_path}", fg='green'))
            
    except Exception as e:
        click.echo(click.style(f"Error al generar el archivo PDF: {str(e)}", fg='red'))
        
@main.command()
@click.option('--path_templates', prompt='Ruta de la plantillas', help='Ruta de las plantillas html para los reportes')
@click.option('--path_export', prompt='Ruta de exportacion', help='Ruta del directorio donde se exportaran los PDF')
def config(path_templates, path_export):
    if  Config.select().count() >0:
        config = Config.get(Config.id==1)
        config.path_templates = path_templates
        config.path_export = path_export
        config.save()
        click.echo(click.style("Configuración actualizada con éxito.", fg='green'))
        return
    
    
    Config.create(path_templates=path_templates, path_export=path_export)
    click.echo(click.style("Configuración guardada con éxito.", fg='green'))    

if __name__ == '__main__':
    if not Config.table_exists():
        Config.create_table()
    main()