from dataclasses import dataclass
from datetime import datetime

@dataclass
class PersistedJournal:
  patientId: str
  documentType: str
  version: int
  savedTimeStamp: str