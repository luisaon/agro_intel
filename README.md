# AgroIntel - Dashboard de Inteligencia de Mercado

## Descripción
AgroIntel es una aplicación web desarrollada con Streamlit para el análisis y seguimiento de oportunidades, amenazas y tendencias en el mercado agrícola internacional.

## Características
- Dashboard interactivo con múltiples vistas
- Seguimiento de oportunidades de mercado
- Monitoreo de amenazas
- Análisis de tendencias
- Pipeline de oportunidades
- Generación de reportes semanales

## Instalación

1. Clonar el repositorio:
```bash
git clone [URL_DEL_REPOSITORIO]
```

2. Instalar dependencias:
```bash
pip install -r requirements.txt
```

## Uso

1. Ejecutar la aplicación:
```bash
streamlit run app.py
```

2. Abrir en el navegador:
- Local: http://localhost:8501
- Red: http://[YOUR-IP]:8501

## Estructura del Proyecto
```
agro_intel/
├── data/
│   ├── oportunidades.csv
│   ├── amenazas.csv
│   ├── tendencias.csv
│   └── pipeline.csv
├── utils/
│   ├── risk_analysis.py
│   └── report_generator.py
├── output/
├── app.py
├── requirements.txt
└── README.md
```

## Contribución
Para contribuir al proyecto:
1. Fork el repositorio
2. Crear una rama para su feature (`git checkout -b feature/AmazingFeature`)
3. Commit sus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abrir un Pull Request

## Licencia
Distribuido bajo la Licencia MIT. Ver `LICENSE` para más información.

## Contacto
[TU NOMBRE/EMPRESA] - [TU EMAIL]
