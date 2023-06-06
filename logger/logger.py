import logging
from logging import getLogger, StreamHandler, Logger, Formatter
from logging import DEBUG, INFO, WARNING, ERROR, CRITICAL
from typing import Optional


class LoggingFactory:
    NAME = __name__
    FORMAT = Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    LEVEL: int = DEBUG
    HANDLER = StreamHandler()
    LOG: Optional[Logger] = None

    def __init__(self,
                 name: str = None,
                 level: int = None,):
        """
        This function is used to initialize the logger.
        :param name: Name of the logger
        :param level: Level of the logger. This can be DEBUG, INFO, WARNING, ERROR, CRITICAL
        """
        self.LOG = getLogger(name if name is not None else self.NAME)
        self.HANDLER.setFormatter(self.FORMAT)
        self.LOG.setLevel(level if level is not None else self.LEVEL)
        self.LOG.addHandler(self.HANDLER)

    @classmethod
    def generate_logger(cls, **kwargs) -> Logger:
        instance = cls(**kwargs)
        return instance.LOG

    @staticmethod
    def log_header(string: str = None, padding_vals: int = 3, padding_charachter: str = '=') -> str:
        length_of_string = len(string)
        padding_length = padding_vals + length_of_string + padding_vals
        padding = padding_charachter * padding_length
        prepadding_string = string.upper().rjust(padding_vals + length_of_string)
        log_header = '\n' + padding + '\n' + prepadding_string + '\n' + padding + '\n'
        return log_header


if __name__ == "__main__":
    log = LoggingFactory.generate_logger(name="TEST", level=DEBUG)
    log.info(LoggingFactory.log_header("TEST"))