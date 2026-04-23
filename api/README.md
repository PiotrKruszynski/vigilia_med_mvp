# API Template

Minimalny szablon Pythona do wklejania do folderu `api` w nowych projektach.

## Co dostajesz

- neutralny pakiet `src/app`, bez nazw specyficznych dla starego projektu
- `uv` + `pyproject.toml` jako główny punkt konfiguracji
- `pytest` z coverage
- `ruff`, `ty`, `tox` i `pre-commit`
- ustrukturyzowane logowanie JSON na stdout
- opcjonalne logowanie do pliku przez zmienną środowiskową

## Szybki start po skopiowaniu

1. Skopiuj katalog do `<projekt>/api`.
2. Zmień metadane w `pyproject.toml`, jeśli chcesz mieć własną nazwę pakietu.
3. Jeśli chcesz domenową nazwę modułu, zmień `src/app` na własną i popraw importy.
4. Utwórz środowisko na Pythonie 3.14 i zainstaluj zależności: `uv sync --dev --python 3.14`
5. Uruchom testy: `uv run pytest`
6. Sprawdź lint i typy: `uv run ruff check .` oraz `uv run ty check`

## Uruchamianie

- `uv run app`
- `uv run python -m app`

## Zmienne środowiskowe

- `APP_NAME` - nazwa pokazywana w logach startowych, domyślnie `api`
- `LOG_LEVEL` - poziom logowania, domyślnie `INFO`
- `LOG_FILE_PATH` - jeśli ustawione, logi będą zapisywane także do wskazanego pliku

## Struktura

- `src/app/main.py` - punkt wejścia aplikacji
- `src/app/utils/logging_config.py` - konfiguracja logowania
- `src/app/utils/log_around.py` - przykładowy dekorator z logowaniem
- `tests/` - minimalne testy startowe
