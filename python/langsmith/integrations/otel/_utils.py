"""Public utilities for setting LangSmith OpenTelemetry attributes."""

from langsmith._internal.otel._attribute_utils import (
    safe_attribute_value,
    set_langsmith_metadata_attribute,
)

__all__ = ["safe_attribute_value", "set_langsmith_metadata_attribute"]
