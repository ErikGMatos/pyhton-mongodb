
from bson.objectid import ObjectId
from pymongo.database import Database


class OrdersRepository:
    def __init__(self, db_connection: Database):
        self.__collection_name = "orders"
        self.__db_connection = db_connection

    def insert_document(self, document: dict) -> None:
        collection = self.__db_connection.get_collection(
            self.__collection_name)
        collection.insert_one(document)

    def insert_list_of_documents(self, list_of_documents: list) -> None:
        collection = self.__db_connection.get_collection(
            self.__collection_name)
        collection.insert_many(list_of_documents)

    def select_many(self, doc_filter: dict) -> list:
        collection = self.__db_connection.get_collection(
            self.__collection_name)
        data = collection.find(doc_filter)
        return data

    def select_one(self, doc_filter: dict) -> list:
        collection = self.__db_connection.get_collection(
            self.__collection_name)
        data = collection.find_one(doc_filter)
        return data

    def select_many_with_properties(self, doc_filter: dict) -> list:
        collection = self.__db_connection.get_collection(
            self.__collection_name)
        data = collection.find_one(
            doc_filter,  # filtro de busca
            {"_id": 0, "cupom": 0}  # opcao de retorno
        )
        return data

    def select_if_property_exists(self, doc_filter: str) -> dict:
        collection = self.__db_connection.get_collection(
            self.__collection_name)
        query = {doc_filter: {"$exists": True}}
        data = collection.find(query, {"_id": 0, "cupom": 0})
        return data

    def select_by_object_id(self, object_id: str) -> dict:
        collection = self.__db_connection.get_collection(
            self.__collection_name)
        data = collection.find_one({"_id": ObjectId(object_id)})
        return data
