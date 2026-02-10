# This is a header comment that should be removed with --header

"""This is a module docstring that should be removed with tidy docstrings."""
import logging
logging.basicConfig(level=logging.DEBUG)
class LoggerWrapper:
    def __init__(self, logger: logging.Logger) -> None:
        self.logger = logger
    def trace(self, message: str) -> None:
        self.logger.debug(message)
    def success(self, message: str) -> None:
        self.logger.info(message)
    def info(self, message: str) -> None:
        self.logger.info(message)
    def warning(self, message: str) -> None:
        self.logger.warning(message)
    def exception(self, message: str) -> None:
        self.logger.exception(message)
    def critical(self, message: str) -> None:
        self.logger.critical(message)
log = LoggerWrapper(logging.getLogger("log"))
logger = logging.getLogger(__name__)
custom_logger = logging.getLogger("custom")
class DummyObject:
    def print(self, message: str) -> None:
        pass
obj = DummyObject()
def example_function():
    """This is a function docstring that should be removed with tidy docstrings."""
    print(
        "This should be removed with tidy prints"
    )  # This inline comment should be removed with tidy comments
    x = 5  # type: int  # This comment should be preserved by default, removed with --inline
    y = 10  # noqa: E501  # This comment should be preserved by default, removed with --inline
    z = 15  # pragma: no cover  # This comment should be preserved by default, removed with --inline
    assert x > 0, (
        "x must be positive"
    )  # This assert should be removed with tidy asserts
    assert y is not None  # This assert should be removed with tidy asserts
    log.trace("This is a trace log")
    log.info("This is an info log")
    log.warning("This is a warning log")
    log.success("This is a success log")
    log.exception("This is an exception log")
    log.critical("This is a critical log")
    logger.info("Logger info message")
    logging.warning("Logging warning message")
    x = logger.info("This should not be removed")
    logger.debug("This should not be removed").strip()
    custom_logger.info("This should not be removed")
    print("Another print to remove")
    obj.print("This should not be removed")  # This comment should be removed
    return x + y + z
class ExampleClass:
    """This is a class docstring that should be removed with tidy docstrings."""
    def method(self):
        """This is a method docstring that should be removed with tidy docstrings."""
        assert True  # This assert should be removed with tidy asserts
        log.info("Method log message")
        return 42
print("Third print to remove")  # Final inline comment to remove
