from dataclasses import dataclass
from datetime import datetime

@dataclass
class EncryptedData:
    id: str
    data: bytes
    algorithm: str
    key_id: str
    created_at: datetime 