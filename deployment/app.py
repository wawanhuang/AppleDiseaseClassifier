<<<<<<< HEAD
import streamlit as st
import eda
import prediction

# Streamlit app title
st.title("Apple Leaf Disease Detection")

# Sidebar for navigation
st.sidebar.title("Navigation")
option = st.sidebar.selectbox("Choose a page:", ["Exploratory Data Analysis", "Prediction"])

# Display the selected page
if option == "Exploratory Data Analysis":
    eda.show_eda()
elif option == "Prediction":
    prediction.show_prediction()
=======
import streamlit as st
import eda
import prediction

# Streamlit app title
st.title("Apple Leaf Disease Detection")

# Sidebar for navigation
st.sidebar.title("Navigation")
option = st.sidebar.selectbox("Choose a page:", ["Exploratory Data Analysis", "Prediction"])

# Display the selected page
if option == "Exploratory Data Analysis":
    eda.show_eda()
elif option == "Prediction":
    prediction.show_prediction()
>>>>>>> 73c409eb196f8dcdb619d4a3f46fbef3f0dcf375
