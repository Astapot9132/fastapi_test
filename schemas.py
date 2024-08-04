from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel


class SchemaFileAdd(BaseModel):
    filename: str
    size: int
    extension: str
    uuid: str


class SchemaFile(SchemaFileAdd):
    id: int
