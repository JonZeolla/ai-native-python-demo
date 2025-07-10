#!/usr/bin/env python3
"""
Test package metadata and imports
"""

import pytest

from ai_native_python_demo import (
    __maintainer__,
    __project_name__,
    __version__,
    __license__,
)


@pytest.mark.unit
def test_package_metadata():
    """Test that package metadata is accessible."""

    assert __maintainer__ == "Jon Zeolla"
    assert __project_name__ == "ai_native_python_demo"
    assert __version__ is not None
    assert isinstance(__version__, str)
    assert __license__ == "MIT"
