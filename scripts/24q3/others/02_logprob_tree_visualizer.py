import argparse
import json
import os
from typing import Any, Dict, List

from graphviz import Digraph
from openai import OpenAI


def parse_completion(completion_data: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Parse the completion data and extract token information."""
    choices = completion_data.get("choices", [])
    if not choices:
        return []

    token_data = []
    for choice in choices:
        logprobs = choice.get("logprobs", {}).get("content", [])
        for logprob in logprobs:
            token_info = {
                "token": logprob.get("token"),
                "logprob": logprob.get("logprob"),
                "top_logprobs": [
                    {"token": tlp.get("token"), "logprob": tlp.get("logprob")}
                    for tlp in logprob.get("top_logprobs", [])
                ],
            }
            token_data.append(token_info)

    return token_data


def create_tree_structure(token_data: List[Dict[str, Any]], depth: int = 5, branch_factor: int = 3):
    """Create a tree structure of interesting alternative paths."""
    tree = {"token": "START", "children": [], "is_chosen": False, "logprob": 0}

    def add_branches(node, level, path):
        if level >= depth or level >= len(token_data):
            return

        chosen_token = token_data[level]["token"]
        chosen_node = {
            "token": chosen_token,
            "children": [],
            "is_chosen": True,
            "logprob": token_data[level]["logprob"],
        }
        node["children"].append(chosen_node)

        alternatives = sorted(token_data[level]["top_logprobs"], key=lambda x: x["logprob"], reverse=True)[
            : branch_factor - 1
        ]

        for alt in alternatives:
            if alt["token"] != chosen_token:
                alt_node = {"token": alt["token"], "children": [], "is_chosen": False, "logprob": alt["logprob"]}
                node["children"].append(alt_node)

        add_branches(chosen_node, level + 1, path + [chosen_token])

    add_branches(tree, 0, [])
    return tree


def visualize_tree_graphviz(tree: Dict[str, Any], output_file: str):
    """Visualize the tree structure using Graphviz."""
    dot = Digraph(comment="LogProb Tree")
    dot.attr(rankdir="TB", size="8,8")

    def add_node(node, parent_id=None):
        node_id = str(id(node))
        label = f"{node['token']}\\n{node['logprob']:.2f}"
        color = "lightgreen" if node["is_chosen"] else "lightblue"
        dot.node(node_id, label, style="filled", fillcolor=color)

        if parent_id:
            dot.edge(parent_id, node_id)

        for child in node["children"]:
            add_node(child, node_id)

    add_node(tree)
    dot.render(output_file, format="png", cleanup=True)


def get_completion_from_api(prompt: str, model: str, api_key: str) -> Dict[str, Any]:
    """Get completion data from the OpenAI API."""
    client = OpenAI(api_key=api_key)
    completion = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        logprobs=True,
        top_logprobs=20,
    )
    return completion.model_dump()


def save_completion_data(completion_data: Dict[str, Any], output_file: str):
    """Save the completion data to a JSON file."""
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(completion_data, f, ensure_ascii=False, indent=2)


def main():
    parser = argparse.ArgumentParser(description="Visualize logprob tree from OpenAI API completion.")
    parser.add_argument("prompt", help="Prompt to send to the API")
    parser.add_argument("--model", default="gpt-4o-mini", help="Model to use for completion")
    parser.add_argument("--output", default="logprob_tree", help="Output file for visualization (without extension)")
    parser.add_argument("--save-data", default="completion_data.json", help="File to save raw completion data")
    parser.add_argument("--depth", type=int, default=5, help="Depth of the tree visualization")
    parser.add_argument("--branch-factor", type=int, default=3, help="Number of alternative branches to show")
    args = parser.parse_args()

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY environment variable is not set")

    completion_data = get_completion_from_api(args.prompt, args.model, api_key)
    save_completion_data(completion_data, args.save_data)

    token_data = parse_completion(completion_data)
    tree = create_tree_structure(token_data, depth=args.depth, branch_factor=args.branch_factor)
    visualize_tree_graphviz(tree, args.output)

    print(f"Tree visualization saved to {args.output}.png")
    print(f"Raw completion data saved to {args.save_data}")


if __name__ == "__main__":
    main()
    # python logprob_tree_visualizer.py "What can you do?" --model "gpt-4o-mini" --output "tree_visualization.png" --save-data "completion_data.json" --depth 10 --branch-factor 5
