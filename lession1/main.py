"""
    Main program
"""
import time
from log import logger
from message import ERR_MESSAGE
from fastapi import FastAPI, HTTPException, Depends, Request
from sqlalchemy.orm import Session
from dto import AccountRequest, AccountResponse
from database import get_db
from models import Account

app = FastAPI()

# Middleware to log requests
@app.middleware("http")
async def log_requests(request: Request, call_next):
    """
        Log request
    """
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time

    logger.info("Method: %s - Url: %s - Status: %d - Execution time: %fs",
        request.method, request.url.path, response.status_code, process_time)
    return response

@app.post("/accounts/", response_model=AccountResponse)
def create_account(account: AccountRequest, db: Session = Depends(get_db)):
    """
        Create a new account
    """
    new_account = Account(**account.dict())
    db.add(new_account)
    db.commit()
    db.refresh(new_account)
    logger.info("Account created: %s", new_account.login)
    return new_account

@app.get("/accounts/{account_id}", response_model=AccountResponse)
def get_account(account_id: int, db: Session = Depends(get_db)):
    """
        Get account by id
    """
    account = db.query(Account).filter(Account.registerID == account_id).first()
    # Check account exists
    if not account:
        raise HTTPException(status_code=404, detail=ERR_MESSAGE.NOT_ACCOUNT)
    return account

@app.get("/accounts/", response_model=list[AccountResponse])
def get_accounts(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
        Get all accounts
    """
    accounts = db.query(Account).offset(skip).limit(limit).all()
    return accounts

@app.put("/accounts/{account_id}", response_model=AccountResponse)
def update_account(account_id: int, account_data: AccountRequest, db: Session = Depends(get_db)):
    """
        Update account by id
    """
    account = db.query(Account).filter(Account.registerID == account_id).first()
    # Check account exists
    if not account:
        raise HTTPException(status_code=404, detail=ERR_MESSAGE.NOT_ACCOUNT)
    # Set value account
    for key, value in account_data.dict().items():
        setattr(account, key, value)
    db.commit()
    db.refresh(account)
    logger.info("Account updated: %d", account_id)
    return account

@app.delete("/accounts/{account_id}")
def delete_account(account_id: int, db: Session = Depends(get_db)):
    """
        Delete account by id
    """
    account = db.query(Account).filter(Account.registerID == account_id).first()
    # Check account exists
    if not account:
        raise HTTPException(status_code=404, detail=ERR_MESSAGE.NOT_ACCOUNT)
    # Delete account
    db.delete(account)
    db.commit()
    logger.info("Account deleted: %d", account_id)
    return {"message": "Account deleted successfully"}
