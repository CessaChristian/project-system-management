from threading import Lock


class InMemoryStorage:
    def __init__(self):
        self._lock = Lock()
        self.reset()

    def reset(self):
        self.users = {}
        self.users_by_nik = {}
        self.user_roles = {}
        self.roles = {}
        self.permissions = {}
        self.role_permissions = {}

        # Dummy employee directory source (later can be replaced with PostgreSQL-backed model/repo)
        self.employee_directory = {"00000", "10001", "10002", "20001", "30001"}

        self._id_counters = {
            "users": 1,
        }

    def next_id(self, table_name: str) -> int:
        with self._lock:
            current = self._id_counters.get(table_name, 1)
            self._id_counters[table_name] = current + 1
            return current


db = InMemoryStorage()
