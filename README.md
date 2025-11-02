# Drug Recommender AI Application

A machine learning-powered drug recommendation system that predicts appropriate medication based on patient characteristics.

App link: https://ml-project-6b90.onrender.com

## Overview
This application uses machine learning algorithms to recommend drugs based on patient demographics, cholesterol levels, blood pressure, and sodium-to-potassium ratio. The system achieves high accuracy using various ML models including Bagging Classifier, Decision Tree, Random Forest, KNN, and SVM.

## Features
- **High Accuracy**: Achieves up to 96% accuracy in drug recommendations
- **Multiple ML Models**: Supports various classification algorithms
- **Interactive UI**: Streamlit-based web interface for easy interaction
- **RESTful API**: Flask backend for predictions
- **Comprehensive Analysis**: Data visualization and exploratory data analysis included

## Dataset
The application uses `drug_data_synthetic_v3.csv` containing:
- **Age**: Patient age
- **Sex**: Gender (male/female)
- **BP**: Blood pressure levels (High/Low/Normal)
- **Cholesterol**: Cholesterol levels (High/Low)
- **Na_to_K**: Sodium to Potassium ratio
- **Drug**: Target drug classification

## Installation

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Setup
1. Clone the repository:
```bash
git clone <repository-url>
cd ML-App4-Drug-Recommender-AI-App
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Running the Application

#### Option 1: Using Streamlit (Recommended)
1. Start the Flask backend server:
```bash
python Drug_Prediction_App.py
```

2. In a new terminal, start the Streamlit app:
```bash
streamlit run streamlit_app.py
```

3. Open your browser and navigate to `http://localhost:8501`

#### Option 2: API Usage
Make a POST request to the Flask API:

```bash
curl -X POST http://127.0.0.1:5000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "age": 45,
    "gender": "male",
    "cholesterol": "cholesterolHigh",
    "bp": "bpHigh",
    "na_to_k": 15.0
  }'
```

### Input Parameters
- **Age**: Patient's age (integer)
- **Gender**: male or female
- **Cholesterol Level**: cholesterolHigh or cholesterolLow
- **BP Level**: bpHigh, bpLow, or bpNormal
- **Na_to_K Value**: Sodium to Potassium ratio (float)

### Output
The model predicts one of the following drugs:
- drugA
- drugB
- drugC
- drugX
- drugY

## Model Performance
The application uses an optimized Random Forest model with the following performance metrics:
- **Accuracy**: 95.56%
- **Best Parameters**:
  - max_depth: 6
  - max_features: sqrt
  - min_samples_leaf: 1
  - min_samples_split: 5
  - n_estimators: 20

## Project Structure
```
ML-App4-Drug-Recommender-AI-App/
│
├── README.md
├── requirements.txt
├── Drug Recommender using Machine Learning.ipynb
├── drug_data_synthetic_v3.csv
├── drug-recommender.pkl
├── Drug_Prediction_App.py
└── streamlit_app.py
```

## Technologies Used
- **Python**: Programming language
- **Scikit-learn**: Machine learning library
- **Flask**: Web framework for backend API
- **Streamlit**: Web framework for frontend
- **Pandas**: Data manipulation
- **NumPy**: Numerical computing
- **Matplotlib & Seaborn**: Data visualization
- **Joblib**: Model serialization

## Development
The Jupyter notebook `Drug Recommender using Machine Learning.ipynb` contains:
- Data preprocessing and exploration
- Feature engineering
- Model training with multiple algorithms
- Hyperparameter tuning using GridSearchCV
- Performance evaluation with confusion matrices
- Model comparison and selection

## License
This project is open source and available for educational purposes.

## Contact
For questions or inquiries, please contact Karan Singh.

