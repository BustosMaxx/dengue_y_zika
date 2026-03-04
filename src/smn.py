import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import plotly.express as px

def cargar_stadisticas():
    st.subheader("Estadisticas climaticas 1991 - 2020")
    temp = pd.read_csv(".\\data\\raw\\estadisticas_normales_9120\\Estadísticas-normales-Datos-abiertos-1991-2020.csv",
                       sep=";")
    st.dataframe(temp)
    
    # Ola de calor ################################################################################################
    st.subheader("Olas de calor")
    ola_calor = pd.read_csv(".//data//raw//olas-de-calor.csv",
                           sep=";")
    ola_calor["Fecha de fin"] = pd.to_datetime(ola_calor["Fecha de fin"])
    ola_calor["año"] = ola_calor["Fecha de fin"].dt.year
    # st.dataframe(ola_calor)
    
    # completo con los años que no hubo ola de calor
    years = list(range(1961,2026,1))
    datos_sample = {
        'Duración (días)':np.repeat(["0"],65), 
        'Fecha de inicio':np.repeat(["NaN"],65), 
        'Fecha de fin': np.repeat(["NaN"],65),
        'Temperatura máxima absoluta': np.repeat(["NaN"],65), 
        'Temperatura mínima absoluta': np.repeat(["NaN"],65), 
        'año':years}
    df_datos_sample = pd.DataFrame(datos_sample)
    ola_calor_ext = pd.concat([ola_calor, df_datos_sample])

    # casteo
    ola_calor_ext["Duración (días)"] =  ola_calor_ext["Duración (días)"].astype(int)
    ola_calor_ext["Fecha de fin"] =  pd.to_datetime(ola_calor_ext["Fecha de fin"])
    ola_calor_ext["año"] =  ola_calor_ext["año"].astype(int)


    # fig, ax = plt.subplots(1,1, figsize=(10,6))
    # sns.barplot(data=ola_calor_ext,x="año", y="Duración (días)", estimator="sum")
    # plt.xticks(rotation=45)
    # st.pyplot(fig)
    # plt.close()

    fig = px.bar(ola_calor_ext, x="año", y="Duración (días)")
    st.plotly_chart(fig)


if __name__ == '__main__':
    cargar_stadisticas()

# data\raw\estadisticas_normales_9120\Estadísticas-normales-Datos-abiertos-1991-2020.csv