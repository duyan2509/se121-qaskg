import json

from neo4j import GraphDatabase
from dotenv import load_dotenv
import os
load_dotenv()
NEO4J_URI = os.getenv("NEO4J_URI")
NEO4J_USERNAME = os.getenv("NEO4J_USERNAME")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")

driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USERNAME, NEO4J_PASSWORD))




def create_graph(tx, head, dependent, rel_type):
    query = """
    MERGE (h:Entity {name: $head})
    MERGE (d:Entity {name: $dependent})
    MERGE (h)-[:RELATION {type: $rel_type}]->(d)
    """
    tx.run(query, head=head, dependent=dependent, rel_type=rel_type)

with open("data/extracted/extracted_data.json", "r", encoding="utf-8") as file:
    data = json.load(file)

with driver.session() as session:
    for filename, content in data.items():
        relations = content["relations"]
        for relation in relations:
            session.execute_write(create_graph, relation["head"], relation["dependent"], relation["relation"])

print("Saved to Neo4j!")
