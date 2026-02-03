#  Pneumonia Detection Web Application

This project is a **Deep Learning web application** for detecting **Pneumonia from chest X-ray images** using **PyTorch** and **Flask**.

##  Project Overview
- Binary classification: NORMAL / PNEUMONIA
- Model: ResNet18 (Transfer Learning)
- Backend: Flask
- Frontend: HTML 
- Training: PyTorch (Google Colab)

##  Project Structure
pneuamania/
├── pneumonia_classifier.pth
├── application/
│   ├── app.py
│   ├── templates/
│   │   └── index.html
│   ├── static/
├── requirements.txt
├── README.md

## Installation
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

##  Run
cd application
python app.py
Open http://127.0.0.1:5000


