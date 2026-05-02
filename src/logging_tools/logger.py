from functools import wraps
from datetime import datetime, timezone
from typing import Callable
import inspect
import json


ALLOWED_LEVELS = ("INFO", "DEBUG", "ERROR")


class ConsoleLogger:
    def write(self, message: str):
        print(message)


class FileLogger:
    def __init__(self, filepath: str):
        self.filepath = filepath

    def write(self, message: str):
        with open(self.filepath, "a", encoding="utf-8") as file:
            file.write(message + "\n")


class TextFormatter:
    def format(self, timestamp: str, level: str, func_name: str, message: str):
        return f"[{timestamp}] [{level}] {func_name}: {message}"


class JsonFormatter:
    def format(self, timestamp: str, level: str, func_name: str, message: str):
        data = {
            "timestamp": timestamp,
            "level": level,
            "function": func_name,
            "message": message
        }
        return json.dumps(data, ensure_ascii=False)


def _prepare_level(level: str) -> str:
    level = level.upper()

    if level not in ALLOWED_LEVELS:
        raise ValueError(f"Unknown log level: {level}")

    return level


def _get_timestamp():
    return datetime.now(timezone.utc).isoformat()


def _write_log(logger, formatter, level, func_name, message):
    timestamp = _get_timestamp()
    formatted = formatter.format(timestamp, level, func_name, message)
    logger.write(formatted)


def log(level: str = "INFO", logger=None, formatter=None):
    """
    Logging decorator with configurable log level, logger and formatter.
    """
    level = _prepare_level(level)

    if logger is None:
        logger = ConsoleLogger()

    if formatter is None:
        formatter = TextFormatter()

    def decorator(func: Callable):
        if inspect.iscoroutinefunction(func):
            @wraps(func)
            async def async_wrapper(*args, **kwargs):
                func_name = func.__name__

                if level != "ERROR":
                    _write_log(logger, formatter, level, func_name, "called")

                    if level == "DEBUG":
                        _write_log(logger, formatter, level, func_name, f"args={args}, kwargs={kwargs}")

                try:
                    result = await func(*args, **kwargs)

                    if level != "ERROR":
                        _write_log(logger, formatter, level, func_name, f"returned {result}")

                    return result

                except Exception as e:
                    _write_log(logger, formatter, "ERROR", func_name, f"raised {type(e).__name__}: {e}")
                    raise

            return async_wrapper

        @wraps(func)
        def sync_wrapper(*args, **kwargs):
            func_name = func.__name__

            if level != "ERROR":
                _write_log(logger, formatter, level, func_name, "called")

                if level == "DEBUG":
                    _write_log(logger, formatter, level, func_name, f"args={args}, kwargs={kwargs}")

            try:
                result = func(*args, **kwargs)

                if level != "ERROR":
                    _write_log(logger, formatter, level, func_name, f"returned {result}")

                return result

            except Exception as e:
                _write_log(logger, formatter, "ERROR", func_name, f"raised {type(e).__name__}: {e}")
                raise

        return sync_wrapper

    return decorator