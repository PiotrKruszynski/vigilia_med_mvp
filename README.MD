# Vigilia MED MVP

Repo zawiera backendowe API w katalogu `api`, przygotowane jako szablon Pythona oparty o `uv`.

## Wymagania

- `uv`
- Python `3.14` zarządzany przez `uv`

## Szybki start

1. Przejdź do katalogu `api`:
   ```bash
   cd api
   ```
2. Utwórz środowisko i zainstaluj zależności:
   ```bash
   uv sync --dev --python 3.14
   ```
3. Uruchom aplikację:
   ```bash
   uv run app
   ```
4. Uruchom testy:
   ```bash
   uv run pytest
   ```

## Struktura

- `api/` - backendowy szablon aplikacji Python

## Przydatne komendy

- `uv run python -m app`
- `uv run ruff check .`
- `uv run ty check`
