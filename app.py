import streamlit as st
import pandas as pd
from datetime import datetime
import os

# Configuración de la página
st.set_page_config(page_title="AgroIntel - Dashboard", layout="wide")

# Función para cargar datos
def load_data():
    try:
        oportunidades = pd.read_csv('data/oportunidades.csv')
        amenazas = pd.read_csv('data/amenazas.csv')
        tendencias = pd.read_csv('data/tendencias.csv')
        pipeline = pd.read_csv('data/pipeline.csv')
        return oportunidades, amenazas, tendencias, pipeline
    except Exception as e:
        st.error(f"Error cargando datos: {str(e)}")
        return pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), pd.DataFrame()

def main():
    st.title("🌾 AgroIntel - Dashboard Inteligencia de Mercado")
    
    # Cargar datos
    oportunidades, amenazas, tendencias, pipeline = load_data()
    
    # Sidebar para filtros
    st.sidebar.title("Filtros")
    selected_week = st.sidebar.selectbox(
        "Seleccionar Semana",
        sorted(oportunidades['Semana'].unique(), reverse=True)
    )
    
    # Layout principal con tabs
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📊 Resumen", 
        "💰 Oportunidades", 
        "⚠️ Amenazas",
        "📈 Tendencias",
        "🎯 Pipeline"
    ])
    
    # Tab Resumen
    with tab1:
        st.header("Resumen Semanal")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric(
                label="Oportunidades Activas",
                value=len(oportunidades[oportunidades['Semana'] == selected_week])
            )
            
        with col2:
            st.metric(
                label="Amenazas Identificadas",
                value=len(amenazas[amenazas['Semana'] == selected_week])
            )
            
        with col3:
            st.metric(
                label="Tendencias Nuevas",
                value=len(tendencias[tendencias['Semana'] == selected_week])
            )
        
        # Generar y mostrar reporte semanal
        if st.button("Generar Reporte Semanal"):
            report_path = generate_weekly_report(
                selected_week,
                oportunidades,
                amenazas,
                tendencias,
                pipeline
            )
            st.success(f"Reporte generado exitosamente: {report_path}")
    
    # Tab Oportunidades
    with tab2:
        st.header("Oportunidades de Mercado")
        filtered_oportunidades = oportunidades[oportunidades['Semana'] == selected_week]
        st.dataframe(filtered_oportunidades)
        
        # Formulario para nueva oportunidad
        with st.expander("Agregar Nueva Oportunidad"):
            with st.form("nueva_oportunidad"):
                col1, col2 = st.columns(2)
                with col1:
                    pais = st.text_input("País")
                    producto = st.text_input("Producto")
                    precio_fob = st.number_input("Precio FOB", min_value=0.0)
                with col2:
                    precio_cif = st.number_input("Precio CIF", min_value=0.0)
                    margen = st.number_input("Margen %", min_value=0.0, max_value=100.0)
                
                if st.form_submit_button("Guardar"):
                    # Calcular riesgo
                    riesgo = calculate_risk_score(pais, producto)
                    
                    # Preparar nueva fila
                    nueva_oportunidad = {
                        'Semana': selected_week,
                        'País': pais,
                        'Producto': producto,
                        'Precio_FOB': precio_fob,
                        'Precio_CIF': precio_cif,
                        'Margen_%': margen,
                        'Riesgo': riesgo
                    }
                    
                    # Agregar a CSV
                    pd.DataFrame([nueva_oportunidad]).to_csv(
                        'data/oportunidades.csv', 
                        mode='a', 
                        header=False, 
                        index=False
                    )
                    st.success("Oportunidad agregada exitosamente!")
    
    # Tab Amenazas
    with tab3:
        st.header("Amenazas Identificadas")
        filtered_amenazas = amenazas[amenazas['Semana'] == selected_week]
        st.dataframe(filtered_amenazas)
        
        # Formulario para nueva amenaza
        with st.expander("Registrar Nueva Amenaza"):
            with st.form("nueva_amenaza"):
                pais = st.text_input("País Afectado")
                amenaza = st.text_input("Amenaza")
                descripcion = st.text_area("Descripción")
                accion = st.text_area("Acción Sugerida")
                
                if st.form_submit_button("Guardar"):
                    # Calcular riesgos
                    riesgo_total = calculate_risk_score(pais, amenaza)
                    
                    # Preparar nueva fila
                    nueva_amenaza = {
                        'Semana': selected_week,
                        'País_Afectado': pais,
                        'Amenaza': amenaza,
                        'Descripción': descripcion,
                        'Riesgo': riesgo_total,
                        'Acción_Sugerida': accion
                    }
                    
                    # Agregar a CSV
                    pd.DataFrame([nueva_amenaza]).to_csv(
                        'data/amenazas.csv', 
                        mode='a', 
                        header=False, 
                        index=False
                    )
                    st.success("Amenaza registrada exitosamente!")
    
    # Tab Tendencias
    with tab4:
        st.header("Tendencias de Mercado")
        filtered_tendencias = tendencias[tendencias['Semana'] == selected_week]
        st.dataframe(filtered_tendencias)
        
        # Formulario para nueva tendencia
        with st.expander("Agregar Nueva Tendencia"):
            with st.form("nueva_tendencia"):
                tendencia = st.text_input("Tendencia")
                productos = st.text_input("Productos Involucrados")
                paises = st.text_input("Países")
                fuente = st.text_input("Fuente")
                notas = st.text_area("Notas")
                
                if st.form_submit_button("Guardar"):
                    # Preparar nueva fila
                    nueva_tendencia = {
                        'Semana': selected_week,
                        'Tendencia': tendencia,
                        'Productos_Involucrados': productos,
                        'Países': paises,
                        'Fuente': fuente,
                        'Fecha_Fuente': datetime.now().strftime('%Y-%m-%d'),
                        'Notas': notas
                    }
                    
                    # Agregar a CSV
                    pd.DataFrame([nueva_tendencia]).to_csv(
                        'data/tendencias.csv', 
                        mode='a', 
                        header=False, 
                        index=False
                    )
                    st.success("Tendencia agregada exitosamente!")
    
    # Tab Pipeline
    with tab5:
        st.header("Pipeline de Oportunidades")
        filtered_pipeline = pipeline[pipeline['Semana'] == selected_week]
        st.dataframe(filtered_pipeline)
        
        # Formulario para nuevo item en pipeline
        with st.expander("Agregar Nuevo Item al Pipeline"):
            with st.form("nuevo_pipeline"):
                oportunidad = st.text_input("Oportunidad")
                etapa = st.selectbox(
                    "Etapa",
                    ["Identificación", "Análisis", "Negociación", "Cierre"]
                )
                pais = st.text_input("País")
                producto = st.text_input("Producto")
                proximo_paso = st.text_area("Próximo Paso")
                fecha_cierre = st.date_input("Fecha Estimada de Cierre")
                margen = st.number_input("Margen Esperado %", min_value=0.0, max_value=100.0)
                
                if st.form_submit_button("Guardar"):
                    # Calcular riesgo
                    riesgo = calculate_risk_score(pais, producto)
                    
                    # Preparar nueva fila
                    nuevo_item = {
                        'Semana': selected_week,
                        'Oportunidad': oportunidad,
                        'Etapa': etapa,
                        'País': pais,
                        'Producto': producto,
                        'Proximo_Paso': proximo_paso,
                        'Fecha_Estimada_Cierre': fecha_cierre.strftime('%Y-%m-%d'),
                        'Margen_Esperado_%': margen,
                        'Riesgo': riesgo
                    }
                    
                    # Agregar a CSV
                    pd.DataFrame([nuevo_item]).to_csv(
                        'data/pipeline.csv', 
                        mode='a', 
                        header=False, 
                        index=False
                    )
                    st.success("Item agregado al pipeline exitosamente!")

if __name__ == "__main__":
    main()
