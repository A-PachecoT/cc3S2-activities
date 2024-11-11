from dataclasses import dataclass

@dataclass
class KeyPair:
    public_key: bytes
    private_key: bytes
    algorithm: str
    key_size: int 