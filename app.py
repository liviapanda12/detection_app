import numpy as np
import pandas as pd
import tensorflow as tf
from fastapi import FastAPI, HTTPException
import json
from pydantic import BaseModel


#chargement du modèle
model_meta = tf.keras.models.load_model('modele/rna_model.h5')

# Création d'une nouvelle instance FastAPI
app = FastAPI()
'''
with open('data.txt', 'r') as file:
        contenu_variable = file.read()
        contenu_variable = contenu_variable.replace(" ", "")
        print(contenu_variable)
'''

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

@app.post("/predict/")
async def predict(data: request_body):
   df = pd.DataFrame([data.dict().values()], columns=data.dict().keys())
   pred = model_meta.predict(df)
   return {"prediction": int(pred)}