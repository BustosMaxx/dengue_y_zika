import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import plotly.express as px

def deforestacion_bosques():

     # DEFORESTACIÓN ####################################################################################
    deforestacion = pd.read_csv("..//data//raw//perdida-anual-bosque-nativo-X-region-forestal-2020.csv",
                           sep=";")
    deforest = deforestacion.melt(id_vars = ["período"], var_name="bosque_nativo", value_name="perdida")
    


if __name__ == '__main__':
    deforestacion_bosques()

