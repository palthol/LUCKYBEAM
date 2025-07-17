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

@cli.group()
def preset():
    """Manage and use search presets."""
    pass

@preset.command(name="run")
@click.argument('name')
@click.option('-r', '--recursive', is_flag=True, help='Search subdirectories')
def preset_run(name, recursive):
    """Search using a preset."""
    cfg = load_config()
    # Combine built-in and custom presets, with custom taking precedence
    all_presets = PRESETS.copy()
    all_presets.update(cfg.get('presets', {}))

    if name not in all_presets:
        click.echo(f"Error: Preset '{name}' not found.", err=True)
        return

    p = all_presets[name]
    run_search(p['keywords'], recursive, p.get('extensions', []), p.get('regex', False))

@preset.command(name="list")
def preset_list():
    """List available presets."""
    cfg = load_config()
    names = set(PRESETS) | set(cfg.get('presets', {}))
    for name in sorted(names):
        click.echo(name)

@preset.command(name="add")
@click.argument('name')
@click.option('--keyword', '-k', multiple=True, required=True, help="Keyword to search for. Can be used multiple times.")
@click.option('--ext', '-e', multiple=True, help="File extension to filter by. Can be used multiple times.")
@click.option('--regex', is_flag=True, default=False, help="Treat keywords as regex patterns.")
def preset_add(name, keyword, ext, regex):
    """Add or update a custom preset."""
    cfg = load_config()
    presets = cfg.setdefault('presets', {})
    presets[name] = {
        "keywords": list(keyword),
        "extensions": list(ext),
        "regex": regex
    }
    save_config(cfg)
    click.echo(f"Preset '{name}' saved.")

@preset.command(name="rm")
@click.argument('name')
def preset_rm(name):
    """Remove a custom preset."""
    cfg = load_config()
    presets = cfg.get('presets', {})
    if name in presets:
        del presets[name]
        save_config(cfg)
        click.echo(f"Preset '{name}' removed.")
    elif name in PRESETS:
        click.echo(f"Error: Cannot remove built-in preset '{name}'.", err=True)
    else:
        click.echo(f"Error: Custom preset '{name}' not found.", err=True)