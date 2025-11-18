from __future__ import annotations
from typing import Any, Dict
from clia.tooling import Tool
from clia.commands import Command, CommandOutcome, CommandRegistry

class MemoryCommand(Command):
    name = "memory"
    description = "Recall memories."
    usage = "/memory"

    def execute(self, agent: "AgentCLI", argument: str) -> CommandOutcome:
        recall_tool = agent.tools.get("recall_memory")
        if recall_tool:
            agent.display_tool_output(recall_tool.handler({}))
        else:
            agent.display_tool_output("ERROR: recall_memory tool not found.")
        return CommandOutcome.CONTINUE

def register(registry: CommandRegistry) -> None:
    registry.register(MemoryCommand())