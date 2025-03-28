from fastapi import FastAPI
from config import TaskModel

app = FastAPI(debug=True)

@app.get('/task/p{model}')
async def root(model : TaskModel):
    if model is TaskModel.id_task:
        return {'SUCCESS' : 'you us id task'}
    elif model is TaskModel.name_task:
        return {'SUCCESS' : 'you us name task'}