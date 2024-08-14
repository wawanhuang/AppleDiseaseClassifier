<<<<<<< HEAD
import os
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from tensorflow.keras.preprocessing.image import ImageDataGenerator

def show_eda():
    # Streamlit app title
    st.title("Exploratory Data Analysis on Apple Leaf Disease Dataset")

    # Path to dataset
    sample_path = 'sample/'  # Change this to your actual sample images directory

    # Image parameters
    IMG_SIZE = 150

    # Load data
    datagen = ImageDataGenerator()
    data = datagen.flow_from_directory(sample_path, target_size=(IMG_SIZE, IMG_SIZE), batch_size=32, class_mode='sparse', shuffle=True)

    # Function to plot sample images with class names
    def plot_image_samples_with_labels(data):
        st.header("Sample Images with Class Labels")
        fig, axes = plt.subplots(1, 4, figsize=(20, 20))
        axes = axes.flatten()
        for img, label, ax in zip(data[0][0], data[0][1], axes):
            ax.imshow(img.astype('uint8'))
            class_name = list(data.class_indices.keys())[int(label)]
            ax.set_title(class_name)
            ax.axis('off')
        plt.tight_layout()
        st.pyplot(fig)

    # Function to plot class distribution
    def plot_class_distribution(data):
        st.header("Class Distribution")
        labels, counts = np.unique(data.classes, return_counts=True)
        fig, ax = plt.subplots()
        ax.bar(labels, counts)
        ax.set_xticks(labels)
        ax.set_xticklabels(list(data.class_indices.keys()), rotation=45)
        st.pyplot(fig)

    # Plot sample images with class names and class distribution
    if st.button('Show Sample Images with Class Names'):
        plot_image_samples_with_labels(data)

    if st.button('Show Class Distribution'):
        plot_class_distribution(data)
=======
import os
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from tensorflow.keras.preprocessing.image import ImageDataGenerator

def show_eda():
    # Streamlit app title
    st.title("Exploratory Data Analysis on Apple Leaf Disease Dataset")

    # Path to dataset
    sample_path = 'sample/'  # Change this to your actual sample images directory

    # Image parameters
    IMG_SIZE = 150

    # Load data
    datagen = ImageDataGenerator()
    data = datagen.flow_from_directory(sample_path, target_size=(IMG_SIZE, IMG_SIZE), batch_size=32, class_mode='sparse', shuffle=True)

    # Function to plot sample images with class names
    def plot_image_samples_with_labels(data):
        st.header("Sample Images with Class Labels")
        fig, axes = plt.subplots(1, 4, figsize=(20, 20))
        axes = axes.flatten()
        for img, label, ax in zip(data[0][0], data[0][1], axes):
            ax.imshow(img.astype('uint8'))
            class_name = list(data.class_indices.keys())[int(label)]
            ax.set_title(class_name)
            ax.axis('off')
        plt.tight_layout()
        st.pyplot(fig)

    # Function to plot class distribution
    def plot_class_distribution(data):
        st.header("Class Distribution")
        labels, counts = np.unique(data.classes, return_counts=True)
        fig, ax = plt.subplots()
        ax.bar(labels, counts)
        ax.set_xticks(labels)
        ax.set_xticklabels(list(data.class_indices.keys()), rotation=45)
        st.pyplot(fig)

    # Plot sample images with class names and class distribution
    if st.button('Show Sample Images with Class Names'):
        plot_image_samples_with_labels(data)

    if st.button('Show Class Distribution'):
        plot_class_distribution(data)
>>>>>>> 73c409eb196f8dcdb619d4a3f46fbef3f0dcf375
