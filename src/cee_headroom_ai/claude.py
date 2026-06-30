"""Route Claude (Anthropic) API calls through the headroom optimization proxy."""

import os

DEFAULT_PROXY_PORT = 8787
DEFAULT_PROXY_URL = f"http://localhost:{DEFAULT_PROXY_PORT}"


def proxy_base_url() -> str:
    """Base URL of the local headroom proxy, overridable via HEADROOM_PROXY_URL."""
    return os.environ.get("HEADROOM_PROXY_URL", DEFAULT_PROXY_URL)


def get_client(**kwargs):
    """Return an anthropic.Anthropic client pointed at the headroom proxy.

    Start the proxy first with `cee-headroom claude-proxy` (or `headroom proxy`).
    Any kwargs are forwarded to anthropic.Anthropic(...).
    """
    import anthropic

    kwargs.setdefault("base_url", proxy_base_url())
    return anthropic.Anthropic(**kwargs)
