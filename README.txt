Laboratorio 4 - BI

Instrucciones:

Para ejecutar la API implementada se debe correr el siguiente comando en la terminal de uvicorn: uvicorn  src.main:app --reload.

Al hacer esto, se podrá observar el correcto funcionamiento de la API en la dirección web http://127.0.0.1:8000/docs. En ella se 
observan las diferentes opciones/endpoints implementados. El endpoint predict tiene como objetivo realizar la predicción de los 
puntos de admisión con base en los parámetros ingresados en formato JSON (tales), a continuación se propone un escenario de prueba 
para que se verifique esta funcionalidad:

[{
  "serial_no": 479,
  "gre_score": 327,
  "toefl_score": 113,
  "university_rating": 4,
  "sop": 4.0,
  "lor":2.77,
  "cgpa": 8.88,
  "research": 1,
  "admission_points": 84.47
},
{
  "serial_no": 446,
  "gre_score": 301,
  "toefl_score": 92,
  "university_rating": 1,
  "sop": 1.85,
  "lor":1.50,
  "cgpa": 7.71,
  "research": 0,
  "admission_points": 45.08
}]

El segundo endpoint (/train) tiene como objetivo entrenar el modelo de regresión lineal implementado en laboratorios anteriores. Para
esta opción, se debe ingresar los datos de entrenamiento y el programa devulve algumas métricas de dicho modelo despues de el nuevo
entrenamiento. El escenario de prueba para este caso es el siguiente: 


