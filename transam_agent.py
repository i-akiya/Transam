from smolagents import CodeAgent, ToolCallingAgent, OpenAIServerModel
from src.nci_tools import nci_concept
from src.transam_ui import TransamUI
from src.doc_retriever_tools import RetrieverTool
import os
import argparse

# config work dir from commadline parameter.
parser = argparse.ArgumentParser(description="Launch the Transam BC Agent")
parser.add_argument(
    "--work_dir",
    type=str,
    required=True,
    help="Working directory for Transam BC Agent"
)


args = parser.parse_args()
if args.work_dir:
    os.environ['TRANSAM_WORK_DIR'] = args.work_dir

model = OpenAIServerModel(
    model_id="local-model",
    api_base="http://localhost:1234/v1",
    api_key="not-needed",
)

# Document Retriever Tool
# Read and merge all files in "ddd" directory into src_doc
docs_directory = f"{os.environ['TRANSAM_WORK_DIR']}/rag_docs"
merged_content = ""
for filename in os.listdir(docs_directory):
    if filename.endswith(".md"):
        with open(os.path.join(docs_directory, filename), 'r') as file:
            merged_content += file.read() + "\n"

src_doc = merged_content

retriever_tool = RetrieverTool(src_doc)
doc_retriever_agent = CodeAgent(
    tools=[retriever_tool],
    model=model,
    name="doc_retrieval_tool",
    description="Document retrieval tool.",
)

bc_agent = ToolCallingAgent(
    tools=[nci_concept],
    model=model,
    name="nci_concept_search_agent",
    description="Agent to search and retrieve NCI concepts from NCI API."
)


manager_agent = CodeAgent(
    tools=[],
    model=model,
    managed_agents=[bc_agent, doc_retriever_agent],
    additional_authorized_imports = ['yaml'],
    max_steps=20,
    planning_interval=4,
    stream_outputs=True
)


if __name__ == "__main__":
    TransamUI(manager_agent).launch()
