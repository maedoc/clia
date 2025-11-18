from __future__ import annotations

from clia.commands import Command, CommandOutcome, CommandRegistry
from clia.tools.recall_memory import create_tool as create_recall_tool

if False:  # pragma: no cover - type checking aid
    from clia.cli import AgentCLI


class MemoryCommand(Command):
    name = "memory"
    description = "Show saved memories"
    usage = "/memory"

    def __init__(self, registry: CommandRegistry) -> None:
        self._registry = registry

    def execute(self, agent: "AgentCLI", argument: str) -> CommandOutcome:
        # Create and call the recall_memory tool
        tool = create_recall_tool()
        result = tool.handler({})
        
        if result == "No memories found.":
            print("No memories found.")
        else:
            print("Saved memories:")
            print(result)
        
        return CommandOutcome.CONTINUE


def register(registry: CommandRegistry) -> None:
    registry.register(MemoryCommand(registry))