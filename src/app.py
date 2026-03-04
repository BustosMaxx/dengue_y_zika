import streamlit as st
import smn

def main():
    st.title("Contar con datos")
    
    
    
    st.sidebar.header("Navegación")
    menu = ["Start", "Servicio Meteorologico Nacional", "Text", "Get to know us"]
    choice = st.sidebar.selectbox("",menu)
    if choice == "Start":
        st.header("header")
        st.subheader("subheader")
    elif choice == "Servicio Meteorologico Nacional":
        smn.cargar_stadisticas()
    elif choice == "Text":
        pass
    elif choice == "Get to know us":
        st.text("Hola, soy yo")



if __name__ == '__main__':
    main()