from dataclasses import dataclass


@dataclass
class IncomingJournal:
    socialSecurityNumber: int
    documentType: str
    version: int
    createdTimeStamp: str
    savedTimeStamp: str
