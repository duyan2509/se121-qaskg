from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from itext2kg import DocumentDistiller,iText2KG
from schema import LegalDocument
from itext2kg.graph_integration import GraphIntegrator

import os
load_dotenv()
NEO4J_URI = os.getenv("NEO4J_URI")
NEO4J_USERNAME = os.getenv("NEO4J_USERNAME")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")
openai_api_key = os.getenv("OPEN_API_KEY")

openai_llm_model = llm = ChatOpenAI(
    api_key = openai_api_key,
    model="gpt-4o",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

openai_embeddings_model = OpenAIEmbeddings(
    api_key = openai_api_key ,
    model="text-embedding-3-large",
)

document_distiller = DocumentDistiller(llm_model = openai_llm_model)


# chunked text list
documents = ["doc1", "doc2", "doc3"]
IE_query = '''
# DIRECTIVES : 
- Act like an experienced information extractor. 
- You have a chunk of a legal document.
- If you do not find the right information, keep its place empty.
'''

distilled_doc = document_distiller.distill(documents=documents, IE_query=IE_query, output_data_structure=LegalDocument)

itext2kg = iText2KG(llm_model = openai_llm_model, embeddings_model = openai_embeddings_model)

semantic_blocks = [f"{key} - {value}".replace("{", "[").replace("}", "]") for key, value in distilled_doc.items()]

ent_threshold = 0.7
rel_threshold = 0.7
kg = itext2kg.build_graph(sections=semantic_blocks,
                          ent_threshold =ent_threshold,
                          rel_threshold =rel_threshold)

GraphIntegrator(uri=NEO4J_URI, username=NEO4J_USERNAME, password=NEO4J_PASSWORD).visualize_graph(knowledge_graph=kg)
