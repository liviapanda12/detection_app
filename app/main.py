#Importation des modules
import numpy as np
import pandas as pd
import tensorflow as tf
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json


# Création d'une nouvelle instance FastAPI
app = FastAPI()

#Chargement du modèle
model_meta = tf.keras.models.load_model('rna_model1.h5')


#Définir les paramètres de notre objet JSON
class request_body(BaseModel):
   DstPort: int
   Protocol: int
   FlowDuration: int
   TotFwdPkts: int
   TotBwdPkts: int
   TotLenFwdPkts: int
   TotLenBwdPkts: int
   FwdPktLenMean: float
   BwdPktLenMean: float
   FlowBytss: float
   FlowIATMean: float
   FwdIATMean: float
   BwdIATMean: float
   FwdPSHFlags: int
   FwdHeaderLen: int
   BwdHeaderLen: int
   FwdPktss: float
   BwdPktss: float
   PktLenVar: float
   SYNFlagCnt: int
   RSTFlagCnt: int
   PSHFlagCnt: int
   ACKFlagCnt: int
   URGFlagCnt: int
   PktSizeAvg: float
   FwdSegSizeAvg: float
   BwdSegSizeAvg: float
   ActiveMean: float
   ActiveMax: float
   ActiveMin: float
   IdleMean: float
   IdleMax: float
   IdleMin: float

#Page d'acceuil
@app.get("/")
def home():
   return "Hello, bienvenue sur l'API de détection d'intrusion"

#Prédiction des données réçues
@app.post("/predict/")
async def predict(data: request_body):
   df = pd.DataFrame([data.dict()])
   print("la valeur de df", df)
   # Prétraitement des données si nécessaire
   # df = preprocess_data(df)
   pred = model_meta.predict(df)
   pred_def = float(pred[0][0])
   print("type de données de pred", type(pred))
   return pred_def