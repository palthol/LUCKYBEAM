# src/lbeam/cli.py
import click
from .search import run_search
from .presets import PRESETS
from .config import load_config, save_config

@click.group()
@click.version_option(__import__("lbeam").__version__)
def cli():
    """lbeam: fast, preset‑driven file finder."""
    pass

@cli.command()
@click.argument('keywords', nargs=-1, required=True)
@click.option('-r', '--recursive', is_flag=True, help='Search subdirectories')
@click.option('--ext', '-e', multiple=True, help='Filter by file extension')
@click.option('--regex', is_flag=True, help='Treat keywords as regex patterns')
def search(keywords, recursive, ext, regex):
    """Search by keywords."""
    run_search(keywords, recursive, list(ext), regex)

@cli.command()
@click.argument('preset', type=click.Choice(list(PRESETS.keys())))
@click.option('-r', '--recursive', is_flag=True, help='Search subdirectories')
def preset(preset, recursive):
    """Search using a preset."""
    cfg = load_config()
    p = cfg.get('presets', {}).get(preset, PRESETS[preset])
    run_search(p['keywords'], recursive, p.get('extensions', []), p.get('regex', False))

@cli.command('list-presets')
def list_presets():
    """List available presets."""
    cfg = load_config()
    names = set(PRESETS) | set(cfg.get('presets', {}))
    for name in sorted(names):
        click.echo(name)

@cli.command()
@click.argument('key')
@click.argument('value')
def config(key, value):
    """Set a config value."""
    cfg = load_config()
    cfg.setdefault('presets', {})[key] = value  # simple example
    save_config(cfg)
    click.echo(f"Set config {key} = {value}")
