# headroom-ai (CEE wrapper)

Pip-installable wrapper around [`headroom-ai`](https://pypi.org/project/headroom-ai/), pulled
in with the `[all]` extra so it's ready to use as a shared dependency across CEE projects.

## Install

```bash
pip install .
```

This installs `headroom-ai[all]` along with this package and exposes a `cee-headroom`
console script that forwards to the upstream `headroom` CLI.

## Usage

Any project can depend on this package (e.g. via a git URL in `requirements.txt` or
`pyproject.toml`) to pull in `headroom-ai` with all extras pre-configured:

```bash
cee-headroom --help
```

Or import it directly:

```python
from cee_headroom_ai import headroom_main
```
