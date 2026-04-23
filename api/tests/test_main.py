from __future__ import annotations

import runpy
from typing import TYPE_CHECKING

import app.main as app_main
from app.utils import logging_config

if TYPE_CHECKING:
    from pathlib import Path

    import pytest
    from pytest_mock import MockerFixture


def test_main_configures_logging_and_logs_startup(monkeypatch: pytest.MonkeyPatch, mocker: MockerFixture) -> None:
    """Ensure the entry point initializes logging and emits a startup record."""
    monkeypatch.setenv("APP_NAME", "vigilia")
    configure_logging = mocker.patch.object(app_main, "configure_logging")
    logger_info = mocker.patch.object(app_main.logger, "info")

    app_main.main()

    configure_logging.assert_called_once_with()
    logger_info.assert_called_once_with("Application started", extra={"app_name": "vigilia"})


def test_python_m_app_runs_main(monkeypatch: pytest.MonkeyPatch) -> None:
    """Ensure ``python -m app`` delegates to the main entry point."""
    called = False

    def fake_main() -> None:
        nonlocal called
        called = True

    monkeypatch.setattr(app_main, "main", fake_main)

    runpy.run_module("app", run_name="__main__")

    assert called


def test_configure_logging_reads_environment(
    monkeypatch: pytest.MonkeyPatch, mocker: MockerFixture, tmp_path: Path
) -> None:
    """Ensure environment variables are passed into dictConfig."""
    log_file = tmp_path / "logs" / "service.log"
    monkeypatch.setenv("LOG_LEVEL", "warning")
    monkeypatch.setenv("LOG_FILE_PATH", str(log_file))
    dict_config = mocker.patch.object(logging_config.logging.config, "dictConfig")

    logging_config.configure_logging()

    config = dict_config.call_args.args[0]

    assert config["root"] == {"handlers": ["console", "file"], "level": "WARNING"}
    assert config["handlers"]["file"]["filename"] == str(log_file)
