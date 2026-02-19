from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from logic.crew import TripCrew
from dotenv import load_dotenv
import os
import traceback 

load_dotenv()

app = FastAPI()

class TripRequest(BaseModel):
    origin: str
    cities: str
    date_range: str
    interests: str

@app.post("/api/plan")
async def create_itinerary(request: TripRequest):
    try:
        crew = TripCrew(
            request.origin, 
            request.cities, 
            request.date_range, 
            request.interests
        )
        result = crew.run()
        return {"status": "success", "itinerary": str(result)}
    except Exception as e:
        traceback.print_exc() 
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)