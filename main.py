from fastapi import FastAPI

app = FastAPI()



@app.get("/")
async def root():
    return {"message": "Hello World"}

print(app)


@app.get("/barber/{barber_id}")
async def read_barber(barber_id: int):
    return {"barber_id": barber_id}