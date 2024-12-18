from src.errors.error_handler import error_handler
from src.main.http_types.http_request import HttpRequest
from src.main.http_types.http_response import HttpResponse
from src.models.repository.interfaces.orders_repository import \
    OrdersRepositoryInterface
from src.models.validators.registry_updater_validator import \
    registry_updater_validator


class RegistryUpdater:
    def __init__(self, orders_repository: OrdersRepositoryInterface):
        self.__orders_repository = orders_repository

    def update(self, http_request: HttpRequest) -> HttpResponse:
        try:
            order_id = http_request.path_params.get("order_id")
            body = http_request.body
            self.__validate_body(body)
            self.__update_order(order_id, body)
            return self.__format_response(order_id)
        except Exception as exception:
            return error_handler(exception)

    def __validate_body(self, body: dict) -> None:
        registry_updater_validator(body)

    def __update_order(self, order_id: str, body: dict) -> None:
        update_fields = body.get("data")
        self.__orders_repository.edit_registry(order_id, update_fields)

    def __format_response(self, order_id: str) -> HttpResponse:
        return HttpResponse(
            body={
                "data": {
                    "order_id": order_id,
                    "type": "Order",
                    "count": 1
                }
            },
            status_code=200
        )
