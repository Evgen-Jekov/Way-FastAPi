from fastapi import FastAPI

app = FastAPI(debug=True)

@app.get('/task/{id}')
async def root(id : int):
    return {'msg' : id}