from abc import ABC, abstractmethod


class VaccineError(Exception, ABC):
    pass


class NotVaccinatedError(VaccineError):

    @abstractmethod
    def __str__(self) -> str:
        return "NotVaccinatedError"


class OutdatedVaccineError(VaccineError):
    def __str__(self) -> str:
        return "OutdatedVaccineError"


class NotWearingMaskError(Exception):
    def __str__(self) -> str:
        return "NotWearingMaskError"
