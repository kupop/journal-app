from typing import datetime, uuid

class PersistedJournal:
  def __init__(self, patientId: uuid, documentType: str, version: int, savedTimeStamp: datetime):
    self.patientId = patientId
    self.documentType = documentType
    self.version = version
    self.savedTimeStamp = savedTimeStamp