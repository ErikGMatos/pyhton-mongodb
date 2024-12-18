
from bson.objectid import ObjectId
from pymongo.database import Database

from src.models.repository.interfaces.orders_repository import \
    OrdersRepositoryInterface


class OrdersRepository(OrdersRepositoryInterface):
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

    def edit_registry(self, object_id: str) -> None:
        collection = self.__db_connection.get_collection(
            self.__collection_name)
        collection.update_one(
            {"_id": ObjectId(object_id)},  # Filtros
            {"$set": {"itens.doce.quantidade": 67}}  # Edicao
        )

    def edit_many_registries(self) -> None:
        collection = self.__db_connection.get_collection(
            self.__collection_name)
        collection.update_many(
            {"itens.refrigerante": {"$exists": True}},  # Filtros
            {"$set": {"itens.refrigerante.quantidade": 99}}  # Edicao
        )

    def edit_registry_with_increment(self, object_id: str) -> None:
        collection = self.__db_connection.get_collection(
            self.__collection_name)
        collection.update_one(
            {"_id": ObjectId(object_id)},  # Filtros
            {"$inc": {"itens.doce.quantidade": 100}}  # Edicao
        )

    def delete_registry(self, object_id: str) -> None:
        collection = self.__db_connection.get_collection(
            self.__collection_name)
        collection.delete_one({"_id": ObjectId(object_id)})

    def delete_many_registry(self) -> None:
        collection = self.__db_connection.get_collection(
            self.__collection_name)
        collection.delete_many({"itens.refrigerante": {"$exists": True}})
