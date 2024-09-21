from bson import ObjectId
from configs.mongodb import database


class DatabaseProvider:
    def __init__(self, collection_name):
        self.collection = database[collection_name]

    def get_all(self):
        cursors = self.collection.find()
        for data in cursors:
            data["_id"] = str(data["_id"])
            yield data

    def get_by_id(self, document_id):
        data = self.collection.find_one({"_id": ObjectId(document_id)})
        if data:
            data["_id"] = str(data["_id"])
            return data
        return None

    def create(self, data):
        result = self.collection.insert_one(data)
        return str(result.inserted_id)

    def update(self, document_id, data):
        result = self.collection.update_one(
            {"_id": ObjectId(document_id)},
            {"$set": data}
        )
        return result.modified_count

    def delete(self, document_id):
        result = self.collection.delete_one({"_id": ObjectId(document_id)})
        return result.deleted_count
