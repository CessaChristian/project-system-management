from flask import jsonify


def _error_response(error: str, status_code: int, details=None):
    payload = {"error": error}
    if details is not None:
        payload["details"] = details
    return jsonify(payload), status_code


def ok(data=None, message="ok", status_code=200):
    if data is not None:
        return jsonify({"data": data}), status_code
    return jsonify({"message": message}), status_code


def created(data=None, message="created"):
    return ok(data=data, message=message, status_code=201)


def bad_request(error="bad_request", details=None):
    return _error_response(error, 400, details)


def unauthorized(error="unauthorized", details=None):
    return _error_response(error, 401, details)


def forbidden(error="forbidden", details=None):
    return _error_response(error, 403, details)


def not_found(error="not_found", details=None):
    return _error_response(error, 404, details)


def conflict(error="conflict", details=None):
    return _error_response(error, 409, details)


def method_not_allowed(error="method_not_allowed", details=None):
    return _error_response(error, 405, details)


def server_error(error="internal_server_error", details=None):
    return _error_response(error, 500, details)