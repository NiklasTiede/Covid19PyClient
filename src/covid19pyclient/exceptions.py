"""Exceptions for `covid19pyclient`."""
from .valid_parameters import AGS
from .valid_parameters import STATES
from .valid_parameters import TYPES


class NoValidTypeError(Exception):
    def __init__(self, state: str) -> None:
        self.state = state
        self.message = f"{self.state!r} is no valid epidemiological metric. Pick one of these: {TYPES}"
        super().__init__(self.message)


class NoValidStateError(Exception):
    def __init__(self, state: str) -> None:
        self.state = state
        self.message = f"{self.state!r} is no valid abbreviation of a german federal state. Pick one of these: {STATES}"
        super().__init__(self.message)


class NoValidDistrictError(Exception):
    def __init__(self, state: str) -> None:
        self.state = state
        self.message = f"{self.state!r} is no valid 5-digit Community Identification Number (Amtlicher Gemeindeschlüssel). Pick one of these: {AGS}"
        super().__init__(self.message)
