# Notes

## Day 1 Initial Setup

Run `uv init` to initialize the project. This will create two files: `.python-version` and `pyproject.toml`. The `.python-version` file specifies the Python version to use, while `pyproject.toml` contains the project configuration.

Whatever package we install gets added in `pyproject.toml` under `dependencies = [...]`. This is the standard way to manage dependencies in Python projects.

### To install a package, use the following command:

```
uv add fastapi
```

### To install a package for development purposes, use the following command:

The dev dependencies are added under `[dependency-groups]` in `pyproject.toml`. This is useful for packages that are only needed during development, such as testing frameworks or linters.

```
uv add --dev mypy
```

### Initial health route

Install the server to run the app:

```
uv add uvicorn
```

Create `src/ems_backend_python/main.py` with a `/health` route:

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
def health() -> dict[str, bool]:
    return {"up": True}
```

- `dict[str, bool]` means keys are `str` and values are `bool`. `dict` always needs both types, so `dict[str]` is a mypy error.
- Keep the health route small: no DB call, no `try/except`, one return.
- Don't put the HTTP status code in the JSON body. FastAPI sends `200` by default, and that code goes in the response status line, not in the body.

### To run the route, use the following command:

```
uv run uvicorn ems_backend_python.main:app --reload
```

- Uvicorn needs `<module>:<variable>`, not a file name. `uvicorn main.py` gives the error `Import string "main.py" must be in format "<module>:<attribute>"`.
- `--reload` restarts the server whenever a file is saved.

Check the route (`-i` also shows the HTTP status):

```
curl -i localhost:8000/health
```

Output:

```
HTTP/1.1 200 OK
content-type: application/json

{"up":true}
```

FastAPI also generates API docs from the routes and type hints at http://127.0.0.1:8000/docs.
