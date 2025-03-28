from fastapi import FastAPI
from config import AIModedl

app = FastAPI(debug=True)

@app.get('/task/{model}')
async def model(model : AIModedl):
    if model is AIModedl.gpt:
        return {'SUCCESS' : {'model' : model}}
    elif model is AIModedl.deepseek:
        return {'SUCCESS' : {'model' : model}}
    
@app.get('/config/{model}')
async def config_model(model : AIModedl, lang : str, version : float = 1.0):
    return {'model' : model, 'version' : version, 'lang' : lang}