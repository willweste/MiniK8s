from pydantic import BaseModel
from typing import List, Optional


class ContainerPort(BaseModel):
    containerPort: int


class Container(BaseModel):
    name: str
    image: str
    ports: Optional[List[ContainerPort]] = None


class PodSpec(BaseModel):
    containers: List[Container]
