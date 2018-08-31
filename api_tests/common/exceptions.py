"""Exceptions"""
from jsonschema.exceptions import ValidationError


class JsonValidationError(ValidationError):
    pass
