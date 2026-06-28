# ============================================================
#              ✅ HUMAN APPROVAL MIDDLEWARE
# ============================================================


from langchain_core.messages import ToolMessage
from langchain.agents.middleware import wrap_tool_call

@wrap_tool_call
def human_approval(request, handler):
    """
    Ask the user for approval before the AI
    executes any tool.
    """

    # Name of the tool the AI wants to use
    tool_name = request.tool_call["name"]

    # Ask for permission
    confirm = input(
        f"\nAgent wants to use '{tool_name}'. Approve? (y/n): "
    )

    # If permission is denied
    if confirm.lower() not in ["y", "yes"]:

        return ToolMessage(
            content="Tool call denied by user.",
            tool_call_id=request.tool_call["id"]
        )

    # Otherwise continue normally
    return handler(request)