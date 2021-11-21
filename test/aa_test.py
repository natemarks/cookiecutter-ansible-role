"""Test variou executions of the cookiecutter
"""
import logging
import os
import pytest
import testinfra # pylint: disable=W0611
from cookiecutter.main import cookiecutter

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger()

PROJECT_DIR = os.getcwd()


@pytest.mark.parametrize(
    "role_name,expected", [("fff", "FFF"), ("ggg", "GGG")]
)
class TestClass: # pylint: disable=R0903
    """Table test the cookiecutter options"""

    def test_(self, host, tmp_path, role_name, expected): # pylint: disable=R0201
        """Iterate on different cookiecutter json overrides"""
        os.chdir(tmp_path)
        log.info("tmpdir: %s", str(tmp_path))
        # cookiecutter(PROJECT_DIR, extra_context={"role_name": role_name})
        cookiecutter(
            PROJECT_DIR, no_input=True, extra_context={"role_name": role_name}
        )
        assert role_name.upper() == expected
        assert host.file(str(tmp_path) + "/" + role_name + "_role").exists
