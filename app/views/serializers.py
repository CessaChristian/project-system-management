def serialize_user(user, roles=None):
    return {
        "id": user["id"],
        "nik": user["nik"],
        "is_active": user["is_active"],
        "roles": roles or [],
    }
def serialize_permission(permission):
    return {"code": permission["code"]}


def serialize_role_permissions(role_name: str, permissions):
    return {
        "role": role_name.upper(),
        "permissions": permissions,
    }
