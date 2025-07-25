from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from web3 import Web3
import json, os

app = FastAPI()
w3 = Web3(Web3.HTTPProvider(os.getenv("RPC_URL", "http://localhost:8545")))

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_credentials=True,
    allow_methods=["*"], allow_headers=["*"]
)

@app.get("/")
def root(): return {"message": "GBTNetwork RPC Server Live", "chainId": 999}

@app.get("/balance/{address}")
def get_balance(address: str):
    try:
        balance = w3.eth.get_balance(address)
        return {"address": address, "balance": w3.fromWei(balance, 'ether')}
    except Exception as e:
        return {"error": str(e)}

@app.get("/chain-id")
def chain_id(): return {"chainId": w3.eth.chain_id}
