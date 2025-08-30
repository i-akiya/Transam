from langchain.docstore.document import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.retrievers import BM25Retriever
from smolagents import Tool


class RetrieverTool(Tool):
    name = "retriever"
    description = "Uses lexical search to retrieve the parts of transformers documentation that could be most relevant to answer your query."
    inputs = {
        "query": {
            "type": "string",
            "description": "The query to perform. This should be lexically close to your target documents. Use the affirmative form rather than a question.",
        }
    }
    output_type = "string"

    def __init__(self, source_doc, **kwargs):
        super().__init__(**kwargs)
        rag_docs = [
            Document(page_content=source_doc)
        ]

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=2000,
            chunk_overlap=200,
            add_start_index=True,
            strip_whitespace=True,
            separators=["\n\n", "\n", ".", " ", ""],
        )
        docs_processed = text_splitter.split_documents(rag_docs)

        self.retriever = BM25Retriever.from_documents(docs_processed, k=10)

    def forward(self, query: str) -> str:
        assert isinstance(query, str), "Your search query must be a string"

        docs = self.retriever.invoke(
            query,
        )
        return "\nRetrieved documents:\n" + "".join(
            [f"\n\n===== Document {str(i)} =====\n" + doc.page_content for i, doc in enumerate(docs)]
        )
