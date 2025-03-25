"""
    DTO
"""
import re
from pydantic import BaseModel, Field, model_validator
from fastapi import HTTPException
REGEX_PW = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$"

class AccountRequest(BaseModel):
    """
        Model request of account
    """
    login: str = Field(..., min_length=3, max_length=20)
    password: str = Field(..., min_length=8,max_length=40)
    phone: str = Field(..., min_length=10, max_length=20)

    @model_validator(mode='after')
    def validate_model(self):
        """
            Validate data request
        """
        if len(self.login) < 3 or len(self.login) > 20:
            raise HTTPException(status_code=400, detail="Login must be between 3 and 20 characters")

        if not re.fullmatch(REGEX_PW, self.password) or len(self.password) > 40:
            raise HTTPException(status_code=400, detail="Password must be at least 8 characters,"\
                "Max length of password is 40 characters,"\
                "Including uppercase, lowercase, numbers and special characters"
            )

        if len(self.phone) < 10 or len(self.phone) > 20:
            raise HTTPException(status_code=400,detail="Login must be between 10 and 20 characters")

        return self

class AccountResponse(BaseModel):
    """
        Model request of account
    """
    registerID: int
    login: str
    phone: str
