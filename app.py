import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
import time
from windrose import WindroseAxes



def main():
    st.title("Wind Energy Predictions")
    st.markdown("It's a basic dashboard of streamlit")


    @st.cache(persist = True)
    def load_data():
        data = pd.read_csv("T1.csv")
        return data, data.head()

    @st.cache(persist = True)
    def load_windenergy_data(up, down):
        x,_ = load_data()
        y = x['LV ActivePower (kW)']
        #y = y.iloc[int(up):int(down), :]
        em_list = []
        for i in range(up, down):
            em_list.append(y[i])
        return em_list

    if st.checkbox('View data'):
        _, y = load_data()
        st.dataframe(y)


    if st.checkbox('View Wind Speed based on wind Direction '):
        data, _ = load_data()
        ax = WindroseAxes.from_ax()
        ax.bar(data['Wind Direction (°)'], data['Wind Speed (m/s)'], normed=True, opening=0.8, edgecolor='white')
        ax.set_legend()
        plt.title("Wind Direction (°) VS Wind Speed (m/s)")
        st.pyplot()

    if st.checkbox("Wind Energy Prediction"):
        up = st.slider("Lower Limit", 0, 200, 40)
        down = st.slider("Upper Limit", 0, 200, 60)
        aa_gaya = load_windenergy_data(up,down)
        st.area_chart(aa_gaya)
        st.pyplot()




if __name__ == "__main__":
    main()
