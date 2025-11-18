from __future__ import annotations
import os
from pathlib import Path
from typing import Any, Dict

from clia.tooling import Tool
from clia.utils import truncate


def save_memory(fact: str) -> str:
    if not fact:
        return "ERROR: 'fact' argument is required"
    
    # Determine memory file location
    config_dir = Path.home() / ".config" / "clia"
    config_dir.mkdir(parents=True, exist_ok=True)
    memory_file = config_dir / "MEMORIES.md"
    
    # Read existing content or create new file
    if memory_file.exists():
        with open(memory_file, 'r', encoding='utf-8') as f:
            content = f.read()
    else:
        content = ""
    
    # Add the new fact to the memories section
    if "## CLIA Memories" not in content:
        # Create the section if it doesn't exist
        content += "\n## CLIA Memories\n\n"
    
    # Add the fact as a new bullet point
    content += f"- {fact}\n"
    
    # Write back to file
    try:
        with open(memory_file, 'w', encoding='utf-8') as f:
            f.write(content)
        return f"Memory saved successfully: {fact}"
    except Exception as e:
        return f"ERROR: Failed to save memory: {e}"


def create_tool() -> Tool:
    def save_memory_handler(args: Dict[str, Any]) -> str:
        fact = args.get("fact")
        return save_memory(fact)
    
    return Tool(
        name="save_memory",
        description="Save information for recall in future sessions. Store key facts or details that should be remembered across interactions.",
        schema='{"fact": "The specific fact or piece of information to remember"}',
        handler=save_memory_handler,
    )
