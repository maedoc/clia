from __future__ import annotations

from clia.commands import Command, CommandOutcome
from clia.tooling import Tool

if False:  # pragma: no cover - type checking aid
    from clia.cli import AgentCLI


class ShCommand(Command):
    name = "sh"
    description = "Run a shell command"
    usage = "/sh <command>"

    def execute(self, agent: "AgentCLI", argument: str) -> CommandOutcome:
        if not argument:
            print("Usage: /sh <command>")
            return CommandOutcome.CONTINUE

        tool = agent.tool_registry.get_tool("run_shell")
        if not tool:
            print("ERROR: 'run_shell' tool not found")
            return CommandOutcome.CONTINUE

        result = tool.handler({"command": argument})
        print(result)
        return CommandOutcome.CONTINUE


def register(registry) -> None:
    registry.register(ShCommand())
