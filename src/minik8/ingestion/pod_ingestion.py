import yaml
from pathlib import Path
from pydantic import BaseModel, field_validator
from typing import Dict


class PodIngestion(BaseModel):
    file_path: Path

    @field_validator("file_path")
    @classmethod
    def validate_path(cls, v: Path) -> Path:
        if not v.exists():
            raise ValueError(f"File does not exist: {v}")
        if not v.is_file():
            raise ValueError(f"Path is not a file: {v}")
        return v

    def load_pod_manifest(self) -> Dict:
        with self.file_path.open("r") as f:
            pod_data_from_manifest = yaml.safe_load(f)
        return pod_data_from_manifest


# Get the directory of the current file
current_dir = Path(__file__).resolve().parent

# Go up two levels and then into the manifests folder
manifest_path = current_dir.parents[1] / "manifests" / "simple-pod.yaml"

pod = PodIngestion(file_path=manifest_path)
print(pod.load_pod_manifest())
