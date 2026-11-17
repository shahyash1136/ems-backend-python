# Decisions

## Package ya plain app

- **Decision:** `uv init --package` (code `src/ems_backend_python/` mein, `build-system` ke saath).
- **Alternative:** plain app (`uv init --app`), jahan `main.py` root par hota hai aur project install nahi hota.
- **Kyun:** package `.venv` mein install hota hai, toh `from ems_backend_python... import ...` har jagah se same chalta hai: app se, `tests/` se, scripts se, chahe command kisi bhi folder se chalao. Plain app mein imports current folder par depend karte hain, jo tests aur multiple folders aane par dikkat de sakte hain.
- **General rule:** jab project mein tests ya kai folders hon, toh package setup achha default hai, taaki imports chalane ki jagah par depend na karein.

## TODO

- [ ] Jis department mein abhi bhi employees hain, wo delete nahi ho sakta (requirement). Decide karna hai ki ye rule kaun enforce karega: database (foreign key constraint) ya Python (service layer mein check)?
