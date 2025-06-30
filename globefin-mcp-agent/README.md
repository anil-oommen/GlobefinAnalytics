# Project Setup

To set up the development environment, follow these steps:

1.  **Create a virtual environment using uv:**
    ```bash
    uv venv
    ```

2.  **Activate the virtual environment:**
    ```bash
    source .venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    uv pip install -e .
    ```

4.  **Run the application:**
    ```bash
    python main.py
    ```

## Sample Settings.json file to add MCP Server command to gemini
```
{
  "theme": "GitHub",
  "selectedAuthType": "oauth-personal",
  "mcpServers": {
    "globefin-mcp-agent": {
      "command": "uv",
      "args": [
          "run",
	  "~/Workspace/codebase/local/nextjs-web-app/globefin-mcp-agent/main.py"
      ],
      "env": {}
    }
  }
}

```

## Sample Gemini Query 

### ONE
```
what was the exchange rate of SGD to INR in 2020

'The exchange rate of SGD to INR in 2020 was 53.7054.'
```

### TWO
```
how much change has been there to the exchange rate between USD to INR in the past 5 years

'The exchange rate of USD to INR changed from 74.0996 in 2020 to 83.6693 in 2024. This is a change of approximately 9.5697.'

```

## Adding Dependencies

To add new dependencies to the project, use `uv add`. For example:

```bash
uv add "mcp[cli]" pandas pyarrow
```