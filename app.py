import numpy as np
import pandas as pd
import tensorflow as tf
from fastapi import FastAPI
import json
from typing import Optional
from pydantic import BaseModel


#chargement du modèle
model = tf.keras.models.load_model('meta_learner_model.h5')

# Création d'une nouvelle instance FastAPI
app = FastAPI()

class request_body(BaseModel):
    with open('data.txt', 'r') as file:
        contenu_variable = file.read()
        contenu_variable = contenu_variable.replace(",", " ")
    print(contenu_variable)



