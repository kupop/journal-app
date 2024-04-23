from typing import datetime

class IncomingJournal:
  def __init__(self, socialSecuritynumber: int, documentType: str, version: int, timeStamp : datetime, savedTimeStamp: datetime):
    self.socialSecuritynumber = socialSecuritynumber
    self.documentType = documentType
    self.version = version
    self.timeStamp = timeStamp
    self.savedTimeStamp = savedTimeStamp

