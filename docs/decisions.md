# Decisions

## Package ya plain app

- **Decision:** `uv init --package` (code `src/ems_backend_python/` mein, `build-system` ke saath).
- **Alternative:** plain app (`uv init --app`), jahan `main.py` root par hota hai aur project install nahi hota.
- **Kyun:** package `.venv` mein install hota hai, toh `from ems_backend_python... import ...` har jagah se same chalta hai: app se, `tests/` se, scripts se, chahe command kisi bhi folder se chalao. Plain app mein imports current folder par depend karte hain, jo tests aur multiple folders aate hi toot jaate hain.
- **General rule:** jis Python project mein tests ya ek se zyada folders honge, use package banao taaki imports chalane ki jagah par depend na karein.

## TODO

- [ ] Department delete hone par uske employees ka kya hoga, ye decide karna hai (block karein, soft-delete, ya employees ko move karein).
