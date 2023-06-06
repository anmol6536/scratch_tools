import unittest
from logging import Logger
from logger.logger import LoggingFactory


class TestLoggingFactory(unittest.TestCase):

    def test_generate_logger(self):
        logger = LoggingFactory.generate_logger()
        self.assertIsInstance(logger, Logger)

    def test_log_header(self):
        header = type(LoggingFactory.log_header("Test Header"))
        expected_output = str
        self.assertEqual(header, expected_output)