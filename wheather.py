import streamlit as st
import pickle
st.subheader("Wheather Predition")
pn=st.number_input("Enter Precipitation")
maxt=st.number_input("Enter maximum Temprature")
mint=st.number_input("Enter minimum tempreture")
wind=st.number_input("Enter wind speed")
button=st.button("Predict")

if button:
    model=pickle.load(open("wp.pkl","rb"))
    res=model.predict([[pn,maxt,mint,wind]])[0]
    st.markdown(f"""
    Wheather Condition : {res}        
    """)