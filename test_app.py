import streamlit as st

st.set_page_config(page_title="AgroIntel - Test", layout="wide")

def main():
    st.title("🌾 AgroIntel - Prueba de Despliegue")
    st.write("Si puedes ver este mensaje, la aplicación se ha desplegado correctamente.")
    
    st.info("Esta es una versión de prueba para verificar el despliegue.")

if __name__ == "__main__":
    main()
