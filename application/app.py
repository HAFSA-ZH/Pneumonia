from flask import Flask, render_template, request
import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image
import os

app = Flask(__name__)
import os
import torch
import torch.nn as nn
from torchvision import models

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

#  chemin absolu vers le dossier pneuamania
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#  chemin du modèle
MODEL_PATH = os.path.join(BASE_DIR, "pneumonia_classifier.pth")

print("Model path utilisé :", MODEL_PATH)

# Charger le modèle
model = models.resnet18(weights=models.ResNet18_Weights.IMAGENET1K_V1)
model.fc = nn.Linear(model.fc.in_features, 2)

model.load_state_dict(torch.load(MODEL_PATH, map_location=device))
model = model.to(device)
model.eval()


# Transformations
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None

    if request.method == "POST":
        if "image" not in request.files:
            return render_template("index.html", prediction="Aucune image envoyée")

        image_file = request.files["image"]

        if image_file.filename == "":
            return render_template("index.html", prediction="Fichier vide")

        image = Image.open(image_file).convert("RGB")
        image = transform(image).unsqueeze(0)

        with torch.no_grad():
            outputs = model(image)
            _, pred = torch.max(outputs, 1)

        prediction = "PNEUMONIA" if pred.item() == 1 else "NORMAL"

    return render_template("index.html", prediction=prediction)


