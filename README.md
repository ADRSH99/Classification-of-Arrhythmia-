# Classification-of-Arrhythmia-

This project implements a machine learning pipeline to classify different types of cardiac arrhythmia using ECG data. The classification model is trained on the arrhythmia dataset and deployed as a web application. The repository includes data processing, model training, and deployment scripts, along with a Dockerfile for containerized deployment.

Technologies Used

    Python: Main programming language for data processing, model training, and web app development.

    Pandas, NumPy: For data manipulation and numerical operations.

    Matplotlib: For data visualization.

    Scikit-learn: For machine learning utilities including imputation, scaling, PCA, and SVM classifier.

    Imbalanced-learn: For handling class imbalance using RandomOverSampler.

    Flask: Web framework to build the deployment app.

    Pickle: For saving and loading trained models and preprocessing objects.

    Docker: For containerized deployment.

    HTML: For web app templates.

How It Works

    Data Preprocessing: Missing values are imputed using mean strategy, and erroneous height values are corrected.

    Handling Imbalance: Random oversampling is applied to balance the classes.

    Feature Scaling and Dimensionality Reduction: StandardScaler is applied, followed by PCA retaining 98% variance.

    Model Training: A Kernel SVM with RBF kernel is trained on the processed data.

    Model Saving: The trained model along with scaler and PCA objects are saved using pickle.

    Deployment: The Flask app loads these objects to predict arrhythmia class from user input via a web interface.

How to Deploy
Prerequisites

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

Ensure the following files are present in the root directory:

    final_model.pkl

    scaler.pkl

    pca.pkl

    arrhythmia.csv (in data/ folder)

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

Model Details

    Algorithm: Kernelized Support Vector Machine (SVM) with RBF kernel

    Preprocessing: Mean imputation, random oversampling, standard scaling, PCA (98% variance)

    Classes: 16 classes including Normal, Ischemic changes, Myocardial Infarction types, Tachycardia, Bradycardia, etc.

    Performance: The model is trained and tested on the arrhythmia dataset with balanced classes.

References

    Dataset: Arrhythmia dataset (arrhythmia.csv)

    Machine learning techniques: Imputation, oversampling, PCA, SVM

    Deployment: Flask web framework and Docker containerization
