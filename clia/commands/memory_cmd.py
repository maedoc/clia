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
            agent._display_tool_result("recall_memory", recall_tool.handler({}))
        else:
            agent._display_tool_result("recall_memory", "ERROR: recall_memory tool not found.")
        return CommandOutcome.CONTINUE

def register(registry: CommandRegistry) -> None:
    registry.register(MemoryCommand())