from __future__ import annotations
from ...plugin import Plugin
from .control import ParquetControl
from .parser import ParquetParser


class ParquetPlugin(Plugin):
    """Plugin for Parquet"""

    # Hooks

    def create_parser(self, resource):
        if resource.format == "parq":
            return ParquetParser(resource)

    def detect_resource(self, resource):
        if resource.format == "parq":
            resource.type = "table"
            resource.mediatype = "appliction/parquet"

    def select_Control(self, type):
        if type == "parquet":
            return ParquetControl
