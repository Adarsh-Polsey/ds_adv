import pandas as pd
import numpy as np
import joblib
import streamlit as st

import os

print(os.path.dirname(os.path.abspath(__file__)))
def func():
    model=joblib.load(open("linear_regression_model.joblib"))
    st.title("Sales prediction app")

    TV=st.number_input("TV adv budget",min_value=0.0)
    Radio=st.number_input("Radio adv budget",min_value=0.0)
    Newspaper=st.number_input("Newspaper adv budget",min_value=0.0)


    if st.button('predict sales'):
        input=np_array[[TV,Radio,Newspaper]]
        prediction=model.predict(input_data)[0]
        st.success(f"predict sales:{prediction:.2f}")
    
