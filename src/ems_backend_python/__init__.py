import uvicorn


def main() -> None:
    uvicorn.run("ems_backend_python.main:app")
