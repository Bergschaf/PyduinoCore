from location import Range
from typing import Callable


class PyduinoError(Exception):
    def __init__(self, message: str, range: Range):
        self.message = message
        self.range = range

    def __repr__(self):
        return f"{self.message} at {self.range}"


class PyduinoSyntaxError(PyduinoError):
    """
    Wrong syntax
    """
    pass


class PyduinoNameError(PyduinoError):
    """Invalid or not existing name"""
    pass


class PyduinoTypeError(PyduinoError):
    """Invalid or incomplatible type"""
    pass


class PyduinoValueError(PyduinoError):
    """Invalid value"""
    pass


class PyduinoErrorHandling:
    Instance = None

    def __init__(self):
        self.errors = []
        if PyduinoErrorHandling.Instance is None:
            PyduinoErrorHandling.Instance = self
        else:
            raise RuntimeError("ErrorHandling is a singleton")

    @staticmethod
    def add_error(error: PyduinoErrorHandling):
        PyduinoErrorHandling.Instance.errors.append(error)

    @staticmethod
    def error_handling(function: Callable):
        """
        Decorator for error handling
        """
        def wrapper(*args, **kwargs):
            try:
                return function(*args, **kwargs)
            except PyduinoError as e:
                PyduinoErrorHandling.add_error(e)
                return None

        return wrapper
