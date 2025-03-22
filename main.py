import streamlit as st
import pickle
st.subheader("Taxi Uber Ride Prediction")
ppw=st.number_input("Priceperweek")
pop=st.number_input("Population")
mon=st.number_input("Monthlyincome")
appm=st.number_input("Averageparkingpermonth")
button=st.button("Predict")

if button:
    model=pickle.load(open("taxi.pkl","rb"))
    res=model.predict([[ppw,pop,mon,appm]])[0]
    st.markdown(f"""
    Wheather Condition : {res}        
    """)
