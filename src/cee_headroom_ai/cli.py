import sys

from headroom.cli import main as headroom_main


def main() -> None:
    headroom_main()


def claude_proxy() -> None:
    """Start the headroom proxy pre-targeted at the Anthropic/Claude API.

    Equivalent to `headroom proxy`, then point clients at it with
    ANTHROPIC_BASE_URL=http://localhost:8787 (see cee_headroom_ai.claude).
    """
    sys.argv = [sys.argv[0], "proxy", *sys.argv[1:]]
    headroom_main()


if __name__ == "__main__":
    main()
