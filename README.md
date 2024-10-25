**Fraud Call Detection Using Machine Learning**

**Overview**

This project is designed to detect fraudulent calls using machine learning algorithms. The model is trained on features extracted from call data, enabling it to identify potential fraud calls with high accuracy. A Flask-based web application allows real-time fraud detection, making it suitable for practical deployment.

**Project Structure**

*   **Fraud\_detection.ipynb**: Jupyter Notebook for data preprocessing, model training, and evaluation.
    
*   **app.py**: Flask web application to receive call data input and provide fraud predictions.
    
*   **requirements.txt**: File listing all dependencies required for the project.
    

**Setup and Installation**

1. git clone https://github.com/Krishna17-bit/Fraud-call-detection.git
2. cd fraud-call-detection
    
3. pip install -r requirements.txt
    

**Data Processing and Model Training**

1.  **Data Preprocessing**:
    
    *   Load call data and clean it for analysis.
        
    *   Engineer features such as call duration, caller ID patterns, time of day, and frequency.
        
2.  **Model Training**:
    
    *   Use machine learning models such as Logistic Regression, Random Forest, and Neural Networks to identify fraud patterns.
        
    *   Evaluate models using accuracy, precision, recall, and F1 score.
        
3.  **Model Evaluation**:
    
    *   Evaluate the model’s performance on both training and test datasets.
        
    *   Conduct cross-validation to ensure model robustness and prevent overfitting.
        

**Web Application**

*   **Real-Time Fraud Detection**: The web app accepts input features related to a call and predicts whether it is fraudulent or not.
    
*   **Deployment**: Built with Flask, allowing for smooth deployment and easy access.
    

**Usage**

1.  python app.pyOpen your browser and go to http://127.0.0.1:5000 to use the app.
    
2.  **Make Predictions**:Enter call details into the web interface to get a fraud prediction.
    

**Results**

*   The model effectively detects fraudulent calls, with optimized metrics like precision and recall to reduce false positives and negatives.
    

**Key Takeaways**

*   **High Accuracy**: Detects fraud calls with high precision, minimizing false alarms.
    
*   **Real-Time Detection**: The model can be used for real-time fraud detection via the web application.
