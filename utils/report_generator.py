import pandas as pd
import xlsxwriter
from datetime import datetime
import os

def generate_weekly_report(week, oportunidades, amenazas, tendencias, pipeline):
    """
    Genera un reporte semanal en Excel con todos los datos relevantes.
    
    Args:
        week (str): Semana del reporte
        oportunidades (pd.DataFrame): DataFrame de oportunidades
        amenazas (pd.DataFrame): DataFrame de amenazas
        tendencias (pd.DataFrame): DataFrame de tendencias
        pipeline (pd.DataFrame): DataFrame de pipeline
    
    Returns:
        str: Ruta del archivo generado
    """
    # Crear directorio de output si no existe
    if not os.path.exists('output'):
        os.makedirs('output')
    
    # Nombre del archivo
    filename = f'output/reporte_semanal_{week}_{datetime.now().strftime("%Y%m%d")}.xlsx'
    
    # Crear Excel writer
    writer = pd.ExcelWriter(filename, engine='xlsxwriter')
    
    # Filtrar datos por semana
    oportunidades_sem = oportunidades[oportunidades['Semana'] == week]
    amenazas_sem = amenazas[amenazas['Semana'] == week]
    tendencias_sem = tendencias[tendencias['Semana'] == week]
    pipeline_sem = pipeline[pipeline['Semana'] == week]
    
    # Escribir cada DataFrame en una hoja diferente
    oportunidades_sem.to_excel(writer, sheet_name='Oportunidades', index=False)
    amenazas_sem.to_excel(writer, sheet_name='Amenazas', index=False)
    tendencias_sem.to_excel(writer, sheet_name='Tendencias', index=False)
    pipeline_sem.to_excel(writer, sheet_name='Pipeline', index=False)
    
    # Obtener el objeto workbook y el formato
    workbook = writer.book
    
    # Formato para títulos
    header_format = workbook.add_format({
        'bold': True,
        'text_wrap': True,
        'valign': 'top',
        'fg_color': '#D7E4BC',
        'border': 1
    })
    
    # Aplicar formato a cada hoja
    for sheet_name in writer.sheets:
        worksheet = writer.sheets[sheet_name]
        
        # Formato para los encabezados
        for col_num, value in enumerate(pd.DataFrame(writer.sheets[sheet_name]).columns.values):
            worksheet.write(0, col_num, value, header_format)
        
        # Autoajustar columnas
        worksheet.autofit()
    
    # Guardar el archivo
    writer.close()
    
    return filename
