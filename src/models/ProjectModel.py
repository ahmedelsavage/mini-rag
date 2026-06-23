from .BaseDataModel import BaseDataModel
from .db_schemes import Project
from .enums.DataBaseEnums import DataBaseEnums

class ProjectModel(BaseDataModel):
    def __init__(self, db_client):
        super().__init__(db_client)
        self.collection = self.db_client[DataBaseEnums.COLLECTION_PROJECT_NAME.value]

        