import pickle
import streamlit as st
model1=pickle.load(open("Insurance.pkl","rb"))
def mydeploy():
    st.title("Insurance Prediction")
    age=st.number_input("enter your age")
    pred=st.button("predict bought insurance")
    if pred:
        x=model1.predict([[age]])
        st.write(x[0])
mydeploy()