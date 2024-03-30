import os
from fastapi import HTTPException, Security, status
from fastapi.security import APIKeyHeader

api_key_header  = APIKeyHeader(name="X-API-Key", auto_error=False)

def verify_api_key(api_key_header: str = Security(api_key_header)) -> str:
    api_key = os.getenv("API_KEY") # key for a single app 

    if not api_key:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="API key not set in environment variables",
        )
    
    if api_key_header != api_key:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API key",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    return api_key_header