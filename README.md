#🫀 Classification of Arrhythmia

This project implements a machine learning pipeline to classify various types of cardiac arrhythmias using ECG data. The trained model is deployed as a web application for real-time prediction. This repository includes scripts for data preprocessing, model training, deployment using Flask, and a Dockerfile for containerization.

🚀 Technologies Used

    Python: Core language for all processing and development

    Pandas, NumPy: Data manipulation and numerical operations

    Matplotlib: Visualizations

    Scikit-learn: ML tools (imputation, scaling, PCA, SVM)

    Imbalanced-learn: RandomOverSampler to handle class imbalance

    Flask: Lightweight web framework for app deployment

    Pickle: Model and object serialization

    Docker: Containerized deployment

    HTML: Frontend templates

⚙️ How It Works

    Data Preprocessing

        Missing values are imputed using the mean strategy.

        Outlier corrections (e.g., unrealistic height values) are applied.

    Class Imbalance Handling

        RandomOverSampler is used to balance class distribution.

    Feature Engineering

        StandardScaler is used for scaling.

        PCA is applied to retain 98% of the variance.

    Model Training

        A Kernel SVM (RBF) classifier is trained on the preprocessed dataset.

    Model Persistence

        The trained model, PCA, and scaler are saved using pickle:

            final_model.pkl

            scaler.pkl

            pca.pkl

    Web Deployment

        A Flask app loads the pickled model, PCA, and scaler to predict arrhythmia classes from uploaded CSV files via a user-friendly interface.

🧪 How to Use
📁 Prerequisites

    Python 3.7+

    Docker (optional, for containerized deployment)

Deployment Without Docker

    Clone the repository:

    bash
    git clone https://github.com/ADRSH99/Classification-of-Arrhythmia-.git
    cd Classification-of-Arrhythmia-

Install dependencies:

    bash
    pip install -r requirements.txt

Ensure the following files are in the root directory:

    final_model.pkl

    scaler.pkl

    pca.pkl

    data/arrhythmia.csv (dataset for reference or testing)
    
Run the Flask app:

    bash
    python app.py

    Open your browser and go to http://127.0.0.1:5000 to access the arrhythmia classification web app.

Deployment Using Docker

    Clone the repository:

    bash
    git clone https://github.com/ADRSH99/Classification-of-Arrhythmia-.git
    cd Classification-of-Arrhythmia-

    Build the Docker image:

    bash
    docker build -t arrhythmia-classification .

Run the Docker container:

    bash
    docker run -p 5000:5000 arrhythmia-classification

    Access the app at http://localhost:5000 in your web browser.

🧠 Model Overview

    Algorithm: Kernelized SVM (RBF Kernel)

    Preprocessing:

        Mean imputation for missing values

        Oversampling for class balance

        Standard scaling

        PCA (retain 98% variance)

    Classes: 16 types of arrhythmias including:

        Normal

        Ischemic changes

        Myocardial infarction variants

        Tachycardia

        Bradycardia

    Input Features: ~280+ ECG-based features

References

    Dataset: Arrhythmia dataset (arrhythmia.csv)

    Machine learning techniques: Imputation, oversampling, PCA, SVM

    Deployment: Flask web framework and Docker containerization
