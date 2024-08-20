# 🚗 Car Price Predictor

## 1️⃣ Description

**Car Price Predictor** is a machine learning tool designed to help both buyers and sellers determine the estimated market value of used cars. By analyzing a range of factors such as make, model, year, mileage, and more, this tool provides reliable price estimates, ensuring transparency and fairness in the used car market.

## 2️⃣ Tech Stack

- **Selenium**: For data scraping from Cars24.com.
- **Python**: Core programming language used for data processing and model development.
- **Pandas**: For data manipulation and analysis.
- **Scikit-Learn (sklearn)**: For building and training the machine learning model.
- **Flask**: Backend framework for creating a web application.
- **Bootstrap**: For designing a responsive and user-friendly frontend.
- **Render**: Platform used for deploying the web application.

## 3️⃣ Design

The design of the Car Price Predictor consists of the following components:

- **Data Collection**: Using Selenium, relevant data is scraped from online car listing.
- **Data Processing**: The collected data is cleaned and pre-processed using Pandas.
- **Model Training**: A machine learning model is developed using Scikit-Learn, trained on the processed data to predict car prices.
- **Web Application**: A Flask-based backend serves the model, while Bootstrap is used for designing an intuitive and responsive frontend where users can input car details and get price estimates.
- **Deployment**: The complete application is deployed on Render, making it accessible to users via the web.

## 4️⃣ Features

- **Accurate Price Prediction**: Provides reliable estimates of used car prices based on multiple factors.
- **User-Friendly Interface**: A simple and intuitive web interface allows users to input car details and receive instant price predictions.
- **Scalable and Deployable**: The application is deployed on Render, ensuring scalability and accessibility.

## 5️⃣ How to Run the Project

### Prerequisites

Ensure you have Python 3.x installed on your system. You'll also need `pip` for installing required Python packages.

### Steps to Run

1. **Clone the repository** to your local machine:
   ```bash
   git clone https://github.com/chirag-dudhrejia/car_price_predictor.git
  
2. Open the project folder:
   ```bash
   cd car_price_predictor
   
3. Create a virtual environment:
   ```bash
   python -m venv venv

4. Activate the virtual environment:
    
   * On Windows:
     ```bash
     .\venv\Scripts\activate

   * On macOS/Linux:
     ```bash
     source venv/bin/activate

5. Install the required packages:
   ```bash
   pip install -r requirements.txt
   
6. Run the Flask application:
   ```bash
   flask run

7. **Access the application** by opening your browser and navigating to **http://127.0.0.1:5000**.

