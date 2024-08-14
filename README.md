# APPLE DISEASE CLASSIFICATION TOOL

## About the Project

This project aims to build a classification model to assist farmers in identifying diseases in apple plants at an early stage, thus reducing the risk of crop failure. The model is designed to classify four categories: **Apple Scab, Black Rot, Cedar Apple Rust**, and **Healthy Apple**. The classification is performed using a **Convolutional Neural Network (CNN)**.

## Project Background

Apple diseases can significantly impact the yield and quality of apple production. Early detection is crucial for effective management and control. This project leverages machine learning, specifically CNN, to develop a model that can classify different apple diseases based on image data. The objective is to provide farmers with a tool that can quickly and accurately identify diseases, helping to mitigate potential losses.

## About the Dataset

The dataset used for this project includes images of apple leaves categorized into four classes: **Apple Scab, Black Rot, Cedar Apple Rust**, and **Healthy**. The images were preprocessed and augmented to improve the model's performance. The dataset was sourced from [Kaggle](https://www.kaggle.com/datasets/tushar5harma/plant-village-dataset-updated).

## Exploratory Data Analysis (EDA) Conclusion

The analysis of the dataset reveals several key insights:

- **Image Dimensions**: Most images are 150x150 pixels, which was set as the input size for the CNN model.
- **Class Distribution**: The dataset is balanced, with each class having a similar number of images.
- **Color Distribution**: Different diseases exhibit distinct color distributions, which are leveraged by the CNN model for classification.
- **Data Augmentation**: Techniques such as rotation, flipping, and zooming were applied to increase the diversity of the training data.

## Model Conclusion

The model employed for this classification task is a Convolutional Neural Network (CNN) with the following architecture:

- **Input Layer**: 150x150 pixel images with 3 color channels (RGB).
- **Convolutional Layers**: Multiple layers with ReLU activation and MaxPooling.
- **Fully Connected Layers**: Dense layers for final classification.
- **Output Layer**: Softmax activation for multi-class classification.

The model achieved the following results:

- **Training Accuracy**: 95%
- **Validation Accuracy**: 92%
- **Test Accuracy**: 90%

These scores indicate a strong capability of the model to accurately classify the diseases based on the input images.

## Recommendations

- **Model Deployment**: Deploy the model as a mobile application for easy accessibility by farmers in the field.
- **Further Data Collection**: Expand the dataset by including more images from different apple varieties and regions.
- **Model Improvement**: Experiment with different CNN architectures and hyperparameters to further improve accuracy.

## How to Use

1.  **Clone the Repository**: Clone the repository to your local machine.

    ```bash
    git clone [https://github.com/FTDS-assignment-bay/p2-ftds032-rmt-g7-wawanhuang.git]
    ```

2.  **Install Dependencies**: Install the necessary dependencies by running:

    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Jupyter Notebook**: Open and run the provided Jupyter Notebook to explore the data and perform the analysis.

    ```bash
    jupyter notebook P2G7_wawan.ipynb
    ```

4.  **Model Deployment**: Use the saved model file to deploy the model in a production environment.

## Future Work

- **Model Generalization**: Test the model on apple leaf images from different climates and regions to ensure generalization.
- **Additional Classes**: Expand the model to classify more types of apple diseases.
- **User Interface**: Develop a user-friendly interface for non-technical users to easily upload images and receive diagnoses.

## Acknowledgments

This project was developed as part of the Data Science program at Hacktiv8. Special thanks to mentors and colleagues for their guidance and support.
