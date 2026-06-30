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

## Wrapping the Claude API

This package routes Claude/Anthropic API calls through headroom's optimization proxy
(context caching, compression) instead of hitting the Anthropic API directly.

1. Start the proxy, pre-targeted at Anthropic:

   ```bash
   cee-headroom-claude-proxy
   ```

   This is a thin alias for `headroom proxy`, which listens on `http://localhost:8787`
   by default.

2. Point your client at the proxy. With the Claude Code CLI:

   ```bash
   ANTHROPIC_BASE_URL=http://localhost:8787 claude
   ```

   Or in Python, using the pre-configured client helper:

   ```python
   from cee_headroom_ai import get_claude_client

   client = get_claude_client()  # base_url defaults to http://localhost:8787
   response = client.messages.create(
       model="claude-sonnet-4-6",
       max_tokens=1024,
       messages=[{"role": "user", "content": "Hello"}],
   )
   ```

   Override the proxy location with the `HEADROOM_PROXY_URL` env var if you run the
   proxy on a different host/port.
