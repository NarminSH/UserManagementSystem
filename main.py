from fastapi import FastAPI
from app.api.v1 import user, transaction
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]
app.add_middleware(
     CORSMiddleware,
     allow_origins=origins,
     allow_credentials=True,
     allow_methods=["*"],
     allow_headers=["*"],
 )


app.include_router(user.router, prefix="/api", tags=["Users"])
app.include_router(transaction.router, prefix="/api", tags=["Transactions"])


@app.get("/")
def read_root():
    return {"message": "Hello, FASTAPI"}