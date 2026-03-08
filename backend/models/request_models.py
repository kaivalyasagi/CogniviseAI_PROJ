from pydantic import BaseModel

class AnalysisRequest(BaseModel):

    user_id: str
    topic: str
    first_attempt: str
    final_attempt: str
