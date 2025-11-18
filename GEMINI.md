# Project Overview: CLIA (Command Line Interface Agent)

CLIA is an interactive command-line interface that empowers a Large Language Model (LLM) to function as a tool-using agent. It facilitates real-time streaming responses and can autonomously invoke registered tools, such as executing shell commands or fetching web content, to accomplish tasks. The agent is designed to be flexible, supporting local Ollama instances by default, but also capable of connecting to OpenAI or Mistral API endpoints.

**Key Technologies:**
*   **Python 3.9+**: The core programming language.
*   **`requests`**: For making HTTP requests.
*   **`beautifulsoup4`**: For parsing HTML content (likely for web fetching tools).
*   **`ddgs`**: For DuckDuckGo search functionality.
*   **LLM Providers**: Ollama, OpenAI, Mistral.

**Architecture Highlights:**
The project is structured to separate concerns, with distinct modules for CLI entry, conversation logic, LLM client interactions, command handling, tool management, and individual tool implementations.

*   `agent_cli.py`: The main entry point for the CLI application, handling argument parsing.
*   `clia/cli.py`: Manages the conversation loop, response streaming, and orchestration of tool usage.
*   `clia/clients.py`: Provides HTTP client implementations for interacting with various LLM providers (Ollama, OpenAI, Mistral).
*   `clia/commands/`: Contains the framework and handlers for various slash commands available within the CLI.
*   `clia/approval.py`: Manages the persistence and prompting for tool approval.
*   `clia/tooling.py`: Defines the `Tool` dataclass and manages the tool registry.
*   `clia/utils.py`: A collection of shared helper functions, including HTML stripping and content truncation.
*   `clia/tools/`: Houses the implementations of specific tools the agent can use, such as `run_shell`, `read_url`, `search_internet`, `bc_calc`, and `file_edit`.

## Building and Running

### Requirements

*   Python 3.9+
*   `requests` Python package
*   `beautifulsoup4` Python package
*   `ddgs` Python package (required for DuckDuckGo search; optional if using Google only)
*   Access to an LLM provider (Ollama, OpenAI, or Mistral).

### Installation

To set up the project, follow these steps:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Usage

Start the agent with the default model (e.g., `llama3`):

```bash
python3 agent_cli.py
```

You can customize the agent's behavior using various command-line flags, such as specifying a model, temperature, shell timeout, or request timeout. For example:

```bash
python3 agent_cli.py "help me summarize this repo" --model llama3.1 --temperature 0.2
```

### Configuration

The agent's behavior can be configured via `~/.config/clia/config.ini` (or a custom path specified by `--config-dir`). CLI flags always take precedence over configuration file settings.

## Development Conventions

### Code Compilation

To check that the script compiles correctly, use:

```bash
python3 -m compileall agent_cli.py
```

### Further Development

As the project evolves, consider implementing automated tests and linting to maintain code quality and consistency.

## Key Files and Directories

*   `.gitignore`: Specifies intentionally untracked files to ignore.
*   `agent_cli.py`: The primary entry point for the command-line interface.
*   `README.md`: Provides a comprehensive overview and documentation for the project.
*   `requirements.txt`: Lists all Python dependencies required for the project.
*   `.venv/`: The Python virtual environment directory, containing installed packages.
*   `clia/`: The main source directory for the CLIA application.
    *   `__init__.py`: Python package initialization file.
    *   `approval.py`: Handles the logic for tool approval.
    *   `cli.py`: Core CLI logic, conversation flow, and tool orchestration.
    *   `clients.py`: Manages API interactions with different LLM providers.
    *   `ollama.py`: Specific client implementation for Ollama.
    *   `tooling.py`: Defines and registers the tools available to the agent.
    *   `utils.py`: Contains utility functions used across the project.
    *   `commands/`: Directory for various CLI commands.
    *   `tools/`: Directory containing implementations of the agent's tools (e.g., `run_shell`, `read_url`, `search_internet`, `bc_calc`, `file_edit`).
*   `docs/`: Contains project documentation, including a system prompt example and a user guide.
    *   `system-prompt-example.txt`: An example template for system prompts.
    *   `user-guide.md`: A guide for users of the CLIA.
