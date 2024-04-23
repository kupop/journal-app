from typing import datetime

class IncomingJournal:
  def __init__(self, socialSecurityNumber: int, documentType: str, version: int, timeStamp : datetime, savedTimeStamp: datetime):
    self.socialSecuritynumber = socialSecurityNumber
    self.documentType = documentType
    self.version = version
    self.timeStamp = timeStamp
    self.savedTimeStamp = savedTimeStamp

