from itertools import count
from typing import Annotated

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, StringConstraints

app = FastAPI()


@app.get("/health")
def health() -> dict[str, bool]:
    return {"up": True}


class DepartmentCreate(BaseModel):
    name: Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)]


class Department(BaseModel):
    id: int
    name: str


data: list[Department] = []
next_id = count(start=1)


@app.post("/departments", status_code=201)
def create_department(payload: DepartmentCreate) -> Department:
    for department in data:
        if payload.name.casefold() == department.name.casefold():
            raise HTTPException(status_code=409, detail="Department already exist")

    new_department = Department(id=next(next_id), name=payload.name)
    data.append(new_department)
    return new_department


@app.get("/departments")
def get_departments() -> list[Department]:
    return data


@app.get("/departments/{department_id}")
def get_department(department_id: int) -> Department:
    for department in data:
        if department_id == department.id:
            return department

    raise HTTPException(status_code=404, detail="Department not found")
