from typing import Optional
from fastapi import FastAPI
from joblib import load
import pandas as pd

from src.DataModel import DataModel

app = FastAPI()


@app.get("/")
def read_root():
   return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
   return {"item_id": item_id, "q": q}

@app.post("/predict")
def make_predictions(LdataModel:list):
   rta={}
   model = load("assets/modelo.joblib")

   print(LdataModel)
   i=1
   for x in LdataModel:
      df = pd.DataFrame(x, columns=x.keys(), index=[0])
      df.columns = ['Serial No.','GRE Score','TOEFL Score','University Rating','SOP',"LOR",'CGPA','Research']
      result = model.predict(df)
      rta[i]=result[0]
      i+=1 
   print(rta)
   return rta