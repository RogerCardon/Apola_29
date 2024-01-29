from pydantic import BaseModel
from typing import Optional, List


class Mission_Information(BaseModel):
    missions: List[str]
    mission_labels: List[str]
    missions_labels_str: Optional[str]
