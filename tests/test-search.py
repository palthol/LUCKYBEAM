import os
import tempfile
from lbeam.search import run_search
import click
from click.testing import CliRunner
from lbeam.cli import cli

def create_file(tmpdir, name, content):
    path = os.path.join(tmpdir, name)
    with open(path, "w") as f:
        f.write(content)
    return path

def test_run_search_plain(tmp_path, capsys):
    # Create files
    f1 = create_file(tmp_path, "a.txt", "hello dashboard world")
    f2 = create_file(tmp_path, "b.txt", "no match here")
    # Change cwd to tmp_path
    old = os.getcwd()
    os.chdir(tmp_path)
    try:
        run_search(["dashboard"], False, [], False)
        captured = capsys.readouterr()
        assert "a.txt" in captured.out
        assert "b.txt" not in captured.out
    finally:
        os.chdir(old)

def test_run_search_with_extension(tmp_path, capsys):
    create_file(tmp_path, "x.py", "dashboard controller")
    create_file(tmp_path, "y.txt", "dashboard controller")
    old = os.getcwd()
    os.chdir(tmp_path)
    try:
        run_search(["dashboard"], False, [".py"], False)
        captured = capsys.readouterr()
        assert "x.py" in captured.out
        assert "y.txt" not in captured.out
    finally:
        os.chdir(old)

def test_run_search_regex(tmp_path, capsys):
    create_file(tmp_path, "r.txt", "User123Dashboard")
    old = os.getcwd()
    os.chdir(tmp_path)
    try:
        run_search([r"User\d+Dashboard"], False, [], True)
        captured = capsys.readouterr()
        assert "r.txt" in captured.out
    finally:
        os.chdir(old)
