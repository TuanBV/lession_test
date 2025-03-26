"""
    Main program
"""
import os
import base64
import time
from log import logger
from fastapi import FastAPI, Request
from constants import APP_ENV, CONTRACT_APP, CONTRACT_SERVER
from dto import FileRequest, SuccessResponse, FailResponse

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

@app.post("/aoi/showSerialpaso/", response_model=SuccessResponse)
def show_serial(request: FileRequest):
    """
        Create a new account
    """
    base_directory = 'C:\\'

    # Get data from request
    data = request.dict()
    try:
        # Check has folder
        if data['app_env'] not in APP_ENV.keys() or \
            data['contract_server'] not in CONTRACT_SERVER.keys() or \
            data['contract_app'] not in CONTRACT_APP.keys():
            # Write log error
            logger.error("Not found folder")
            return FailResponse(status='false', message='Seal Info response false')
        # Create directory
        target_path = os.path.join(base_directory, CONTRACT_APP[data['contract_app']],
                                    APP_ENV[data['app_env']],
                                    CONTRACT_SERVER[data['contract_server']]
                                )
        # If data['file'] is base64 then decode data['file'] to get file name
        # file_name = base64.decode(data['file'])

        # Get path of file
        target_file = os.path.join(target_path, f"{data['file']}.html")

        # Check file exists
        if os.path.exists(target_file):
            # Open file
            with open(target_file, "rb") as f:
                # Encode data of file
                encoded_content = base64.b64encode(f.read()).decode("utf-8")
            # Write log
            logger.info("Seal Info response successfully")

            # Return
            return SuccessResponse(status='true',
                file= f"{data['file']}.html",
                content= encoded_content,
                message='Seal Info response successfully'
            )
    except Exception as e:
        # Write log error
        logger.error("Error in show_serial: %s", str(e))
        # return
        return FailResponse(status='false', message='Seal Info response false')
