"""Exceptions for `covid19pyclient`."""
from .endpoints import STATES
from .endpoints import TYPES


class NoValidStateError(Exception):
    def __init__(self, state: str) -> None:
        self.state = state
        self.message = f"{self.state!r} is no valid abbreviation of a german federal state. Pick one of these: {STATES}"
        super().__init__(self.message)


class NoValidTypeError(Exception):
    def __init__(self, state: str) -> None:
        self.state = state
        self.message = f"{self.state!r} is no valid epidemiological metric. Pick one of these: {TYPES}"
        super().__init__(self.message)
