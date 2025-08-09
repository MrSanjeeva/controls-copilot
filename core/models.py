from typing import List, Literal
from pydantic import BaseModel

Verdict = Literal["Compliant", "Partial", "Gap"]


class Citation(BaseModel):
    policy_section_id: str
    score: float


class Finding(BaseModel):
    regulation_section_id: str
    verdict: Verdict
    confidence: float
    reason: str
    citations: List[Citation]
