import logging
import os
from datetime import datetime
from typing import Any, Dict
from langchain_core.callbacks import BaseCallbackHandler

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/agent.log",
    level=logging.INFO,
    format="%(asctime)s | %(message)s"
)
logger = logging.getLogger(__name__)


class ToolLogger(BaseCallbackHandler):
    """Logs every tool call: name, input, output, and timestamp."""

    def on_tool_start(
        self, serialized: Dict[str, Any], input_str: str, **kwargs
    ) -> None:
        tool_name = serialized.get("name", "unknown")
        logger.info(f"[TOOL CALL]   tool={tool_name} | input={input_str}")
        print(f"[LOG] Tool called: [bold]{tool_name}[/bold] | input: {input_str}")

    def on_tool_end(self, output: str, **kwargs) -> None:
        preview = output[:300] + ("..." if len(output) > 300 else "")
        logger.info(f"[TOOL RESULT] output={preview}")

    def on_tool_error(self, error: Exception, **kwargs) -> None:
        logger.error(f"[TOOL ERROR]  {error}")


# Export a single shared instance
tool_logger = ToolLogger()