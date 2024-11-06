"""
Demostración Completa de Logging en Python
----------------------------------------
Este script muestra diferentes técnicas de logging usando la biblioteca 'rich'
para una mejor visualización y formato.

Características principales:
- Logging básico y avanzado
- Formateo de colores y estilos
- Manejo de archivos de log
- Logging estructurado
- Manejo de excepciones

Autor: André Pacheco
Fecha: 2024-11-06
"""

# Imports básicos
import logging  # Para implementar el sistema de registro (logging) en la aplicación
import sys
import time
import json
import os
from datetime import datetime, timezone
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler
from pathlib import Path  # Para manejar rutas del sistema de archivos de forma multiplataforma

# Rich imports para UI mejorada
from rich.logging import RichHandler  # Para dar formato visual mejorado a los logs
from rich.console import Console      # Para crear una consola con estilos y colores
from rich import print as rprint      # Para imprimir texto con formato enriquecido
from rich.traceback import install    # Para mejorar la visualización de trazas de error
from rich.table import Table         # Para crear tablas con formato enriquecido
from rich.panel import Panel         # Para crear paneles con bordes y títulos
from rich.progress import track      # Para mostrar barras de progreso animadas
from rich.markdown import Markdown

# Instalamos el manejador de trazas de rich
install(show_locals=True)

# Creamos la consola para salida enriquecida
console = Console()

def delay_with_spinner(seconds=1, message="Procesando..."):
    """Función para crear pausas visuales entre demostraciones"""
    for _ in track(range(seconds * 10), description=message):
        time.sleep(0.1)

class CustomJsonFormatter(logging.Formatter):
    """
    Formateador personalizado que genera logs en formato JSON
    Útil para procesamiento posterior o integración con herramientas de análisis
    """
    def format(self, record):
        # Limpiamos el mensaje antes de crear el registro JSON
        if isinstance(record.msg, str):
            # Guardamos el mensaje original
            original_msg = record.msg
            # Removemos los marcadores de rich
            clean_msg = original_msg.replace('[/]', '')
            for color in ['green', 'red', 'yellow', 'cyan', 'dim cyan', 'bold red on white']:
                clean_msg = clean_msg.replace(f'[{color}]', '')
        else:
            clean_msg = record.msg
            
        log_record = {
            'marca_tiempo': datetime.now(timezone.utc).isoformat(),
            'nivel': record.levelname,
            'mensaje': clean_msg,
            'modulo': record.module,
            'funcion': record.funcName,
            'linea': record.lineno
        }
        return json.dumps(log_record, ensure_ascii=False)

    def format_all(self):
        """Retorna todos los logs en un formato JSON válido"""
        return json.dumps(self.logs, ensure_ascii=False, indent=2)

def setup_logs_directory():
    """Crea el directorio de logs si no existe"""
    logs_dir = Path(__file__).parent / 'logs'
    logs_dir.mkdir(exist_ok=True)
    return logs_dir

class ColoredMessageHandler(RichHandler):
    """Handler personalizado que aplica colores automáticamente según el nivel"""
    
    LEVEL_COLORS = {
        "DEBUG": "cyan",
        "INFO": "green",
        "WARNING": "yellow",
        "ERROR": "red",
        "CRITICAL": "bold red on white"
    }
    
    def emit(self, record):
        # Aplicar color según el nivel
        color = self.LEVEL_COLORS.get(record.levelname, "white")
        if isinstance(record.msg, str):
            record.msg = f"[{color}]{record.msg}[/{color}]"
        super().emit(record)

def basic_logging_demo():
    """
    Demostración de Logging Básico
    -----------------------------
    Muestra los diferentes niveles de logging con formato enriquecido
    """
    console.rule("[bold blue]Demostración de Logging Básico")
    
    logger = logging.getLogger('demo_basica')
    logger.setLevel(logging.DEBUG)
    
    handler = ColoredMessageHandler(
        console=console,
        show_time=True,
        markup=True,
        rich_tracebacks=True
    )
    logger.addHandler(handler)
    
    # Ahora los mensajes se colorearán automáticamente
    logger.debug('Mensaje de depuración: usado para información detallada')
    logger.info('Mensaje informativo: operaciones normales del sistema')
    logger.warning('Mensaje de advertencia: algo inesperado pero no crítico')
    logger.error('Mensaje de error: un problema serio ha ocurrido')
    logger.critical('Mensaje crítico: el sistema no puede continuar')

class PlainLogFormatter(logging.Formatter):
    """Formateador para archivos de texto plano que elimina las marcas de Rich"""
    def format(self, record):
        if isinstance(record.msg, str):
            # Limpiamos el mensaje de marcas Rich
            msg = record.msg.replace('[/]', '')
            for color in ['green', 'red', 'yellow', 'cyan', 'dim cyan', 'bold red on white']:
                msg = msg.replace(f'[{color}]', '')
            record.msg = msg
        return super().format(record)

def custom_logger_demo():
    """
    Demostración de Logger Personalizado
    ---------------------------------
    Muestra cómo configurar un logger con múltiples handlers
    """
    console.rule("[bold blue]Demostración de Logger Personalizado")
    
    logs_dir = setup_logs_directory()
    logger = logging.getLogger('logger_personalizado')
    logger.setLevel(logging.DEBUG)
    
    console_handler = RichHandler(
        console=console,
        rich_tracebacks=True,
        show_time=True,
        show_path=True,
        markup=True
    )
    
    file_handler = logging.FileHandler(logs_dir / 'registro_personalizado.log')
    file_handler.setFormatter(PlainLogFormatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    
    console_handler.setLevel(logging.WARNING)
    file_handler.setLevel(logging.DEBUG)
    
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    
    # Mensajes con colores
    logger.debug('Mensaje de debug (solo archivo)')
    logger.info('Mensaje informativo (solo archivo)')
    logger.warning('[yellow]Mensaje de advertencia (consola + archivo)[/yellow]')
    logger.error('[red]Mensaje de error (consola + archivo)[/red]')
    logger.critical('[bold red on white]Mensaje crítico (consola + archivo)[/bold red on white]')

def advanced_logging_demo():
    """
    Demostración de Logging Avanzado
    ------------------------------
    Muestra características avanzadas como:
    - Rotación de archivos
    - Logging estructurado
    - Tablas formateadas
    """
    console.rule("[bold blue]Demostración de Logging Avanzado")
    
    logs_dir = setup_logs_directory()
    logger = logging.getLogger('logger_avanzado')
    logger.setLevel(logging.DEBUG)
    
    # Handlers avanzados
    rotating_handler = RotatingFileHandler(
        logs_dir / 'registro_rotativo.log',    # Nuevo archivo cada 10KB
        maxBytes=10*1024,
        backupCount=5
    )
    
    timed_handler = TimedRotatingFileHandler(
        logs_dir / 'registro_diario.log',      # Nuevo archivo cada día
        when='midnight',
        interval=1,
        backupCount=7
    )
    
    # Crear un manejador personalizado para JSON
    class JsonFileHandler(logging.FileHandler):
        def __init__(self, filename):
            super().__init__(filename, mode='w')  # 'w' mode to overwrite file
            self.formatter = CustomJsonFormatter()
            self.logs = []

        def emit(self, record):
            log_entry = json.loads(self.formatter.format(record))
            self.logs.append(log_entry)
            # Escribir la lista completa como JSON cada vez
            with open(self.baseFilename, 'w', encoding='utf-8') as f:
                json.dump(self.logs, f, ensure_ascii=False, indent=2)
    
    json_handler = JsonFileHandler(logs_dir / 'registro.json')
    console_handler = RichHandler(console=console, rich_tracebacks=True)
    
    for handler in [rotating_handler, timed_handler, json_handler, console_handler]:
        logger.addHandler(handler)
    
    # Tabla de ejemplo actualizada
    tabla = Table(show_header=True, header_style="bold magenta")
    tabla.add_column("Hora")
    tabla.add_column("Nivel")
    tabla.add_column("Mensaje")
    
    hora_actual = datetime.now().strftime("%H:%M:%S")
    tabla.add_row(
        hora_actual,
        "INFO",  # Rich coloreará esto automáticamente
        "Sistema iniciado correctamente",
        style="green"
    )
    tabla.add_row(
        hora_actual,
        "ADVERTENCIA",
        "Uso alto de memoria",
        style="yellow"
    )
    tabla.add_row(
        hora_actual,
        "ERROR",
        "Fallo en conexión a base de datos",
        style="red"
    )
    
    console.print(tabla)
    
    # Usar el ColoredMessageHandler para estos mensajes también
    handler = ColoredMessageHandler(
        console=console,
        rich_tracebacks=True,
        markup=True
    )
    logger.addHandler(handler)
    
    # Ahora los mensajes sin marcadores manuales
    logger.info('Mensaje de prueba de logging avanzado')
    logger.error('Error con contexto completo')

def exception_logging_demo():
    """
    Demostración de Logging de Excepciones
    -----------------------------------
    Muestra cómo manejar y registrar excepciones
    """
    console.rule("[bold blue]Demostración de Logging de Excepciones")
    
    logger = logging.getLogger('logger_excepciones')
    logger.setLevel(logging.DEBUG)
    
    # Cambiamos RichHandler por ColoredMessageHandler
    handler = ColoredMessageHandler(
        console=console,
        rich_tracebacks=True,
        tracebacks_show_locals=True,
        show_time=True,
        markup=True
    )
    logger.addHandler(handler)
    
    try:
        console.print(Panel.fit(
            "[yellow]Intentando división por cero...[/yellow]",
            title="Prueba de Excepción"
        ))
        resultado = 1 / 0
    except Exception as e:
        # Removemos los marcadores de formato manual
        logger.exception("Ha ocurrido un error en el cálculo")

def generate_markdown_banner():
    """Genera un banner en formato Markdown"""
    markdown = Markdown(
        """
# 🚀 Python Logging Demo
### Demostración Completa de Logging en Python
### Por André Pacheco

## 🛠 Características
- **Logging Básico**: Niveles y formateo
- **Logging Avanzado**: Rotación y estructurado
- **Rich UI**: Colores y estilos mejorados
- **Manejo de Excepciones**: Trazas detalladas

## ℹ️ Información
- **Versión**: 1.0.0
- **Fecha**: 2024-11-06
- **Estado**: Inicializando...

---
Presione Ctrl+C en cualquier momento para salir
"""
    )
    return markdown

def show_header():
    """Muestra un header atractivo y centrado con la descripción del proyecto"""
    banner = generate_markdown_banner()
    console.print(
        Panel(
            banner,
            title="[bold blue]Logging Demo[/bold blue]",
            subtitle="[yellow]Documentación y Ejemplos[/yellow]",
            border_style="blue",
            padding=(1, 2),
        ),
        justify="center"
    )
    console.print()  # Línea en blanco para mejor espaciado

def main():
    """Función principal que ejecuta todas las demostraciones"""
    logging.getLogger().handlers = []
    
    console.clear()
    show_header()  # Añadimos el header al inicio
    delay_with_spinner(2, "Inicializando demostraciones...")
    
    basic_logging_demo()
    delay_with_spinner(1, "Preparando siguiente demostración...")
    
    custom_logger_demo()
    delay_with_spinner(1, "Cargando características avanzadas...")
    
    advanced_logging_demo()
    delay_with_spinner(1, "Configurando manejo de excepciones...")
    
    exception_logging_demo()
    
    console.print("\n[bold green]¡Todas las demostraciones completadas![/bold green]", justify="center")

if __name__ == "__main__":
    main()
