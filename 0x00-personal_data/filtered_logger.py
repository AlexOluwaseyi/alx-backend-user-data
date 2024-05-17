#!/usr/bin/env python3

"""
Write a function called filter_datum that returns the log message obfuscated:

Arguments:
- fields: a list of strings representing all fields to obfuscate
- redaction: a string representing by what the field will be obfuscated
- message: a string representing the log line
- separator: a string representing by which character is separating all
  fields in the log line (message)

The function should use a regex to replace occurrences of certain field values
filter_datum should be less than 5 lines long and use re.sub to perform
the substitution with a single regex.
"""

import re
from typing import List
import logging

PII_FIELDS = ("name", "email", "phone", "ssn", "password")


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Initializer"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """formatter method"""
        text = super(RedactingFormatter, self).format(record)
        redact = filter_datum(self.fields, self.REDACTION,
                              text, self.SEPARATOR)
        return redact


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Function that redacts or obfuscate PII"""
    for field in fields:
        message = re.sub(field + "=.*?" + separator,
                         field + "=" + redaction + separator,
                         message)
    return message


def get_logger() -> logging.Logger:
    """get_logger function"""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(PII_FIELDS))

    logger.addHandler(handler)

    return logger
