from langgraph.graph import StateGraph
from agent.nodes import (
    retrieve_node,
    draft_answer_node,
    final_answer_node
)

def build_graph():
    graph = StateGraph(dict)

    graph.add_node("retrieve", retrieve_node)
    graph.add_node("draft", draft_answer_node)
    graph.add_node("final", final_answer_node)

    graph.set_entry_point("retrieve")
    graph.add_edge("retrieve", "draft")
    graph.add_edge("draft", "final")

    return graph.compile()
