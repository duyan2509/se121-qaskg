from vncorenlp import VnCoreNLP

# Path to the VnCoreNLP jar file
vncorenlp_path = "path/to/VnCoreNLP-1.1.1.jar"

# Initialize the client (it automatically starts the server locally)
with VnCoreNLP(vncorenlp_path) as vncorenlp:
    text = "Xin chào, tôi tên là AI Assistant."
    annotation = vncorenlp.annotate(text)
    print(annotation)