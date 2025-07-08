# transend-mcp
MCP server that serves structured API context for AI agents. The server will expose endpoints that return JSON/YAML context representations for common Transend workflows (e.g. YMM lookup, inventory check).

## Usage
In root dir

    uv init

Create virtual environment and activate it:

    uv venv
    source .venv/bin/activate

Install dependencies:

    uv add mcp transend

Launch the inspector:

    npx @modelcontextprotocol/inspector uv run server.py