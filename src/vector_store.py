import chromadb
import load_dotenv
import os
import chromadb.utils.embedding_functions as embedding_functions

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
    
    def get_embedding_function(self):
        
        OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
        openai_ef = embedding_functions.OpenAIEmbeddingFunction(
                        api_key=OPENAI_API_KEY,
                        model_name="text-embedding-3-small"
                    )
        return openai_ef
    
    def get_vector_store_collection(self):
        client_connection = self.get_vector_store_connection()
        embedding_functions = self.get_embedding_function()
        return client_connection.get_collection(
            name="emarket_metadata", 
            embedding_function=embedding_functions,
            metadata={"hnsw:space": "cosine"},)
    
    def query_vector_store(self, q, n_results=10):
        collection = self.get_vector_store_collection()
        return collection.query(query_texts=[q], n_results=n_results)
    
    def parse_vector_store_response(self, response):
        return {
            "distances": response[0]["distances"],
            "ids": response[0]["ids"],
            "metadatas": response[0]["metadata"],
            "content": response[0]["text"],
        }
    
    