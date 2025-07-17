import os
import shutil
import tempfile
from click.testing import CliRunner
from lbeam.cli import cli

def test_list_presets(tmp_path):
    runner = CliRunner()
    result = runner.invoke(cli, ["list-presets"])
    assert result.exit_code == 0
    assert "WebDev" in result.output

def test_search_command():
    runner = CliRunner()
    with runner.isolated_filesystem():
        # Create file inside the isolated directory
        with open("dash.txt", "w") as f:
            f.write("dashboard controller")

        result = runner.invoke(cli, ["search", "dashboard", "--ext", ".txt"])
        
        assert result.exit_code == 0
        assert "dash.txt" in result.output


def test_preset_command(): # <-- tmp_path is no longer needed here
    runner = CliRunner()
    with runner.isolated_filesystem():
        # Create files matching WebDev preset
        with open("dash.js", "w") as f:
            f.write("dashboard controller model routes UI")

        # The preset command doesn't take an --ext option
        result = runner.invoke(cli, ["preset", "WebDev"])

        assert result.exit_code == 0
        assert "dash.js" in result.output
 