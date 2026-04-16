from azure.cosmos import CosmosClient

class CosmosService:
    def __init__(self):
        url = "xxx"
        key = "xxxx=="


        self.client = CosmosClient(url, credential=key)
        self.database = self.client.get_database_client("movie-db")
        self.container = self.database.get_container_client("movies")

     # READ with error handling
    def get_items(self):
        try:
            return list(self.container.read_all_items())
        except Exception as e:
            print("Error fetching data:", e)
            return []

    # WRITE with error handling
    def create_item(self, data):
        try:
            return self.container.create_item(body=data)
        except Exception as e:
            print("Error saving data:", e)
            return None