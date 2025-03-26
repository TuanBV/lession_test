"""
    DTO
"""
from typing import Optional
from pydantic import BaseModel, Field, model_validator
from fastapi import HTTPException

class FileRequest(BaseModel):
    """
        Model request of account
    """
    file: str = Field(..., min_length=1, max_length=128, description="File name")
    app_env: str = Field(..., min_length=1, description="App environment")
    contract_app: str = Field(..., min_length=1, description="Contract app")
    contract_server: str = Field(..., min_length=1, description="Contract server")

    @model_validator(mode='after')
    def validate_model(self):
        """
            Validate data request
        """
        if not self.file or len(self.file) > 128:
            raise HTTPException(status_code=400,
                detail="File field is required and max length is 128 characters")
        if not self.app_env:
            raise HTTPException(status_code=400, detail="App_env field is required")
        if not self.contract_app:
            raise HTTPException(status_code=400, detail="Contract_app field is required")
        if not self.contract_server:
            raise HTTPException(status_code=400, detail="Contract_server field is required")

        return self

class SuccessResponse(BaseModel):
    """
        Response success model
    """
    status: str
    file: str
    content: str
    message: str

class FailResponse(BaseModel):
    """
        Response fail model
    """
    status: str
    FileName: Optional[str] = None
    message: str
