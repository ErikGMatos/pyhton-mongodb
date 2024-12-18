from src.errors.types.http_bad_request_error import HttpBadRequestError
from src.errors.types.http_not_found_error import HttpNotFoundError
from src.errors.types.http_unprocessable_entity_error import \
    HttpUnprocessableEntityError
from src.main.http_types.http_response import HttpResponse


def error_handler(error: Exception) -> HttpResponse:
    if isinstance(error, (HttpBadRequestError, HttpNotFoundError, HttpUnprocessableEntityError)):
        return HttpResponse(
            body={
                "errors": [
                    {
                        "title": error.name,
                        "detail": error.message
                    }
                ]
            },
            status_code=error.status_code
        )

    return HttpResponse(
        body={
            "errors": [
                {
                    "title": "Server Error",
                    "detail": str(error)
                }
            ]
        },
        status_code=500
    )
