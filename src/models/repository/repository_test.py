# pylint: disable-all
import pytest

from src.models.repository.orders_repository import OrdersRepository

# db_connection_handler = DBConnectionHandler()
# db_connection_handler.connect_to_db()
# conn = db_connection_handler.get_db_connection()


@pytest.mark.skip(reason="Interaction with db")
def test_insert_document():
    orders_repository = OrdersRepository(conn)
    my_doc = {"alguma": "coisa", "valor": 5}
    orders_repository.insert_document(my_doc)


@pytest.mark.skip(reason="Interaction with db")
def test_insert_list_of_documents():
    orders_repository = OrdersRepository(conn)
    my_doc = [{"elem1": "aqui1"}, {"elem2": "aqui12"}, {"elem3": "aqui3"}]
    orders_repository.insert_list_of_documents(my_doc)


@pytest.mark.skip(reason="Interaction with db")
def test_select_many():
    orders_repository = OrdersRepository(conn)
    doc_filter = {"cupom": True}
    response = orders_repository.select_many(doc_filter)
    print()
    print(response)
    for doc in response:
        print()
        print(doc)
        print()


@pytest.mark.skip(reason="Interaction with db")
def test_select_one():
    orders_repository = OrdersRepository(conn)
    doc_filter = {"cupom": True}
    response = orders_repository.select_one(doc_filter)
    print()
    print(response)
    # for doc in response:
    #     print()
    #     print(doc)
    #     print()


@pytest.mark.skip(reason="Interaction with db")
def test_select_many_with_properties():
    orders_repository = OrdersRepository(conn)
    doc_filter = {"cupom": True}
    response = orders_repository.select_many_with_properties(doc_filter)
    print(response)


@pytest.mark.skip(reason="Interaction with db")
def test_select_if_property_exists():
    orders_repository = OrdersRepository(conn)
    doc_filter = "address"
    response = orders_repository.select_if_property_exists(doc_filter)
    print(response)
    for doc in response:
        print(doc)
        print()


@pytest.mark.skip(reason="Interaction with db")
def test_select_many_with_multiple_filter():
    orders_repository = OrdersRepository(conn)
    doc_filter = {"cupom": True, "itens.refrigerante": {
        "$exists": True}}  # Selmelhante a uma busca AND em SQL
    response = orders_repository.select_many(doc_filter)
    print()
    print(response)
    for doc in response:
        print()
        print(doc)
        print()


@pytest.mark.skip(reason="Interaction with db")
def test_select_many_with_or_filter():
    orders_repository = OrdersRepository(conn)
    doc_filter = {
        "$or": [
            {"address": {"$exists": True}},
            {"itens.doce.tipo": "chocolate"}
        ]
    }  # Selmelhante a uma busca OR em SQL
    response = orders_repository.select_many(doc_filter)
    print()
    print(response)
    for doc in response:
        print()
        print(doc)
        print()


@pytest.mark.skip(reason="Interaction with db")
def test_selct_by_object_id():
    orders_repository = OrdersRepository(conn)
    object_id = "676088f7722215e9728d4a7c"
    response = orders_repository.select_by_object_id(object_id)
    print(response)


@pytest.mark.skip(reason="Interaction with db")
def test_edit_registry():
    orders_repository = OrdersRepository(conn)
    object_id = "67608c25722215e9728d4a7d"
    orders_repository.edit_registry(object_id)


@pytest.mark.skip(reason="Interaction with db")
def test_edit_many_registries():
    orders_repository = OrdersRepository(conn)
    orders_repository.edit_many_registries()


@pytest.mark.skip(reason="Interaction with db")
def test_edit_registry_with_increment():
    orders_repository = OrdersRepository(conn)
    object_id = "67608c25722215e9728d4a7d"
    orders_repository.edit_registry_with_increment(object_id)


@pytest.mark.skip(reason="Interaction with db")
def test_delete_registry():
    orders_repository = OrdersRepository(conn)
    object_id = "676088a8722215e9728d4a7b"
    orders_repository.delete_registry(object_id)


@pytest.mark.skip(reason="Interaction with db")
def test_delete_many_registries():
    orders_repository = OrdersRepository(conn)
    orders_repository.delete_many_registry()
