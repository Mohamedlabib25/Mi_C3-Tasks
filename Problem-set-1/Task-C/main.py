import os
import uuid
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from task_A import compute_time_differences

app = FastAPI()

# Get node ID (unique identifier for each instance)
node_id = str(uuid.uuid4())

@app.post("/compute-differences")
async def compute_differences(request: Request):
    """API endpoint that receives plain text, processes it, and returns time differences."""
    text_input = await request.body()
    decoded_text = text_input.decode("utf-8").splitlines()

    result = compute_time_differences(decoded_text)


    if isinstance(result, str) and "Invalid" in result:
        raise HTTPException(status_code=400, detail=result)

    # Convert string result to JSON array
    json_array = result.strip().split("\n")
    
    # Return response with node ID
    return JSONResponse(content={"id": node_id, "result": json_array})
