from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import APIRouter, status, Depends, HTTPException
from .. import schemas, database, models, token
from sqlalchemy.orm import Session
from ..hashing import Hash
router = APIRouter(
    prefix='/auth',
    tags = ['Authentication']
)

@router.post('/login', response_model=schemas.Token)
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f'Invalid Credentials')
    if not Hash.verify(user.password, request.password):
        print('__INVALID PWD__')
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail=f'Invalid Credentials')
        
    # TODO: generate a jwt token and return
    
    access_token = token.create_access_token(
        data={"sub": user.email}
    )
    return {"access_token": access_token, "token_type": "bearer"}
    
    
