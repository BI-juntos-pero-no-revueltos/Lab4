from typing import Optional
from fastapi import FastAPI
from joblib import load
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error as mse

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

   i=1
   for x in LdataModel:
      df = pd.DataFrame(x, columns=x.keys(), index=[0])
      df.columns = ['Serial No.','GRE Score','TOEFL Score','University Rating','SOP',"LOR",'CGPA','Research','Admission Points']
      result = model.predict(df)
      rta[i]=result[0]
      i+=1 
   return rta

@app.post("/train")
def train_model(LdataModel:list):
   rta={}
   model = load("assets/modelo.joblib")

   i=1
   for x in LdataModel:
      df = pd.DataFrame(x, columns=x.keys(), index=[0])
      df.columns = ['Serial No.','GRE Score','TOEFL Score','University Rating','SOP',"LOR",'CGPA','Research','Admission Points']
      X = df.drop('Admission Points', axis = 1)
      y = df['Admission Points']
      model=model.fit(X,y)
      i+=1 
   
   r2=model.score(X,y)
   print(r2)

   y_true = y
   y_predicted = model.predict(X)

   RMSE=np.sqrt(mse(y_true, y_predicted))
   print(RMSE)
   return rta