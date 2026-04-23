import logging
import os

from app.utils.logging_config import configure_logging

logger = logging.getLogger(__name__)


def main() -> None:
    """Entry point for the template application."""
    configure_logging()
    logger.info("Application started", extra={"app_name": os.getenv("APP_NAME", "api")})


if __name__ == "__main__":  # pragma: no cover
    main()
