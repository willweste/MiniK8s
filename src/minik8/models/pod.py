from pydantic import BaseModel
from container import PodSpec


class Pod(BaseModel):
    spec: PodSpec