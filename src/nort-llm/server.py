'''
Here's implemented a server for interacting with user.
'''

from fastapi import FastAPI
from pydantic import BaseModel

class Request(BaseModel):
    username: str | None = None
    prompt: str
    think: bool = False

app = FastAPI()

@app.get("/")
async def root():
    """Simple example of fastapi work."""
    return {"message": "Hello, World!"}

@app.post("/chat/{session_id}")
async def process_request(session_id: int, req: Request):
    """Handling user request and passing it to llm-server."""
    print("User's request is: ", req.prompt)
    print("Session id is: ", session_id)
    return {"status": "Processed."}

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)