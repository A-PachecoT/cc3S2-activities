from typing import Dict, Any, Optional
from dataclasses import dataclass
from datetime import datetime


@dataclass
class VersionMetadata:
    timestamp: datetime
    description: str
    metadata: Dict[str, Any]


class VersionManager:
    def __init__(self):
        self.versions: Dict[int, VersionMetadata] = {}
        self.current_version = -1

    def create_version(
        self, description: str = "", metadata: Dict[str, Any] = None
    ) -> int:
        """Crea una nueva versión y devuelve su ID"""
        self.current_version += 1
        self.versions[self.current_version] = VersionMetadata(
            timestamp=datetime.now(), description=description, metadata=metadata or {}
        )
        return self.current_version

    def get_version_metadata(self, version: int) -> Optional[VersionMetadata]:
        """Recupera los metadatos de una versión específica"""
        return self.versions.get(version)

    def get_current_version(self) -> int:
        """Devuelve el número de la versión actual"""
        return self.current_version

    def version_exists(self, version: int) -> bool:
        """Comprueba si una versión existe"""
        return version in self.versions
