from fastapi import FastAPI
from config import TaskModel

app = FastAPI(debug=True)

@app.get('/task/{model}')
async def model(model : TaskModel):
    if model is TaskModel.gpt:
        return {'SUCCESS' : {'model' : model}}
    elif model is TaskModel.deepseek:
        return {'SUCCESS' : {'model' : model}}
    
@app.get('/config/{model}')
async def config_model(model, lang : str, version : float = 1.0):
    return {'model' : model, 'version' : version, 'lang' : lang}