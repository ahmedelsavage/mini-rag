from .BaseDataModel import BaseDataModel
from .db_schemes import DataChunk
from .enums.DataBaseEnums import DataBaseEnums
from bson.objectid import ObjectId

class ChunkModel(BaseDataModel):
    def __init__(self, db_client):
        super().__init__(db_client)
        self.collection = self.db_client[DataBaseEnums.COLLECTION_CHUNK_NAME.value]

    async def create_chunk(self, chunk: DataChunk):

        result = await self.collection.insert_one(chunk.model_dump()) # == .dict()
        chunk._id = result.inserted_id
        return chunk
        
    async def get_chunk(self, chunk_id: str):
        result = await self.collection.find_one({
            "_id": ObjectId(chunk_id)
        }
        )

        if result is None:
            return None
        
        return DataChunk(**result)