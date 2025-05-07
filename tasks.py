from invoke import task

@task
def clean(c):
    """Remove build artifacts and lock files."""
    c.run("rm -rf build/ dist/ *.egg-info __pycache__")
    c.run("rm -f requirements.txt dev-requirements.txt")

@task
def compile(c):
    """Compile requirements.txt from requirements.in with hashes."""
    c.run("pip-compile requirements.in --generate-hashes --output-file=requirements.txt")

@task
def sync(c):
    """Sync the virtual environment to requirements.txt."""
    c.run("pip-sync requirements.txt")

@task(clean)
def build(c):
    """Build source and wheel distributions."""
    c.run("python -m build")
    
@task
def install(c, path="dist/*.whl"):
    """Install a wheel file without installing its dependencies."""
    c.run(f"pip install --no-deps {path}")
