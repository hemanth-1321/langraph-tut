from typing import TypedDict
from langgraph.graph import StateGraph
from IPython.display import Image, display

class AgentState(TypedDict, total=False):
    message: str
    compliment: str

def greeting_node(state: AgentState) -> AgentState:
    """
    simple node that adds a greeting message
    """
    state["message"] = "Hey " + state["message"] + ", how is your day going?"
    return state

def compliment(state: AgentState) -> AgentState:
    state["compliment"] = "You are doing great!"
    return state

# Build the graph
graph = StateGraph(AgentState)
graph.add_node("greeter", greeting_node)
graph.add_node("complimenter", compliment)

# Flow: greeter → complimenter
graph.add_edge("greeter", "complimenter")

# One entry and one finish point
graph.set_entry_point("greeter")
graph.set_finish_point("complimenter")

app = graph.compile()

# Save visualization
png_bytes = app.get_graph().draw_mermaid_png()
with open("graph.png", "wb") as f:
    f.write(png_bytes)

print("✅ Graph saved as graph.png")

# Run the graph
result = app.invoke({"message": "hemanth"})
print(result)
