# ============================================================
#                 📝 LOGGING MIDDLEWARE
# ============================================================


import logging
from langchain.agents.middleware import wrap_tool_call


# Configure logging
logging.basicConfig(
    filename="agent.log",       # Log file name
    level=logging.INFO,         # Log INFO and above
    format="%(asctime)s - %(message)s"
)


@wrap_tool_call
def tool_logger(request, handler):
    """
    Log every tool call made by the AI agent.
    """

    # Get the tool name
    tool_name = request.tool_call["name"]

    # Log before execution
    logging.info(f"Calling Tool: {tool_name}")

    # Execute the tool
    result = handler(request)

    # Log after execution
    logging.info(f"Finished Tool: {tool_name}")

    return result