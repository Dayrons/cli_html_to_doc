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
@click.option('--file_input', prompt='Nombre del template', help='Nombre del template con el que se generara el reporte(template.html)')
@click.option('--file_output', prompt='Nombre del salida', help='Nombre de exportacion del archivo(reporte.pdf)')
@click.option('--variables', default="{}", prompt='Variables para la plantilla', help='Variables para la plantilla en formato JSON.')
def generate_report(file_input, file_output, variables):
    
    if not Config.select().count():
        click.echo("No has configurado la ruta de las plantillas y la ruta de exportación. Ejecuta el comando config para configurarlas.")
        return

    for config in configs:
        try:

            template_path = os.path.join(config.path_templates, file_input)
            
            export_path = os.path.join(config.path_export, file_output)
            
            env = Environment(loader=FileSystemLoader('/'))
            template = env.get_template(template_path)

            
            variables_dict = json.loads(variables)
            html = template.render(variables_dict)

            
            pdfkit.from_string(html, export_path)
            click.echo(f"Archivo PDF generado con éxito: {export_path}")
            
        except Exception as e:
            click.echo(f"Error al generar el archivo PDF: {str(e)}")
            


@main.command()
@click.option('--template_path', prompt='Ruta de la plantilla', help='Ruta de la plantilla HTML.',callback=prompt_if_config)
@click.option('--pdf_output', prompt='Salida del PDF', help='Ruta del archivo PDF de salida.',callback=prompt_if_config)
def config():
    pass      

if __name__ == '__main__':
    if not Config.table_exists():
        Config.create_table()
    main()