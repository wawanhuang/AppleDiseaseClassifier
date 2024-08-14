<<<<<<< HEAD
import numpy as np
import streamlit as st
import tensorflow as tf
from tensorflow.keras.preprocessing import image

def show_prediction():
    # Load the model
    model = tf.keras.models.load_model('sequential_model.keras')

    # Streamlit app
    st.title("Apple Leaf Disease Prediction")

    # Upload an image
    uploaded_file = st.file_uploader("Choose an image...", type="jpg")

    def predict(image_path):
        IMG_SIZE = 150
        img = image.load_img(image_path, target_size=(IMG_SIZE, IMG_SIZE))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        predictions = model.predict(img_array)
        return predictions

    if uploaded_file is not None:
        image_path = uploaded_file.name
        with open(image_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.image(image_path, caption='Uploaded Image.', use_column_width=True)
        st.write("")
        st.write("Classifying...")
        predictions = predict(image_path)
        class_names = ['Apple Scab', 'Black Rot', 'Apple Rust', 'Healthy Apple']
        predicted_class = class_names[np.argmax(predictions)]
        st.write(f"Prediction: {predicted_class}")
=======
import numpy as np
import streamlit as st
import tensorflow as tf
from tensorflow.keras.preprocessing import image

def show_prediction():
    # Load the model
    model = tf.keras.models.load_model('sequential_model.keras')

    # Streamlit app
    st.title("Apple Leaf Disease Prediction")

    # Upload an image
    uploaded_file = st.file_uploader("Choose an image...", type="jpg")

    def predict(image_path):
        IMG_SIZE = 150
        img = image.load_img(image_path, target_size=(IMG_SIZE, IMG_SIZE))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        predictions = model.predict(img_array)
        return predictions

    if uploaded_file is not None:
        image_path = uploaded_file.name
        with open(image_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.image(image_path, caption='Uploaded Image.', use_column_width=True)
        st.write("")
        st.write("Classifying...")
        predictions = predict(image_path)
        class_names = ['Apple Scab', 'Black Rot', 'Apple Rust', 'Healthy Apple']
        predicted_class = class_names[np.argmax(predictions)]
        st.write(f"Prediction: {predicted_class}")
>>>>>>> 73c409eb196f8dcdb619d4a3f46fbef3f0dcf375
