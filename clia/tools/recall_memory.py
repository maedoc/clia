from __future__ import annotations
import os
import re
from pathlib import Path
from typing import Any, Dict

from clia.tooling import Tool


def recall_memory() -> str:
    # Determine memory file location
    config_dir = Path.home() / ".config" / "clia"
    memory_file = config_dir / "MEMORIES.md"
    
    if not memory_file.exists():
        return "No memories found."
    
    try:
        with open(memory_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract memories section using regex
        match = re.search(r"## CLIA Memories\n(.*?)(?=\n## |\Z)", content, re.DOTALL)
        
        if match:
            memories_section = match.group(1).strip()
            if memories_section:
                # Extract bullet points
                memories = [line[2:].strip() for line in memories_section.split('\n') if line.startswith("- ")]
                if memories:
                    return ", ".join(memories)
        
        return "No memories found."
    
    except Exception as e:
        return f"ERROR: Failed to read memories: {e}"


def create_tool() -> Tool:
    def recall_memory_handler(args: Dict[str, Any]) -> str:
        return recall_memory()
    
    return Tool(
        name="recall_memory",
        description="Retrieve previously saved memories. Returns all facts that have been saved using save_memory.",
        schema='{}',
        handler=recall_memory_handler,
    )