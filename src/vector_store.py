import chromadb
import load_dotenv
import os
class EVMarketVectorStore:

    def get_vector_store_connection_parameters(self):
        host = os.getenv('DEPLOYMENT_CHROMA_DB_HOST')
        port = os.getenv('DEPLOYMENT_CHROMA_DB_PORT')
        return {
            "host": host,
            "port": port
        }

    def get_vector_store_connection(self):
        connection_parameters = self.get_vector_store_connection_parameters()
        client_connection = chromadb.HttpClient(**connection_parameters)
        return client_connection
    
