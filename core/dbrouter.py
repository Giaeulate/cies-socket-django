
class SocketDB:

    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'core':
            return 'socket_db'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'core':
            return 'socket_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'core':
            return db == 'socket_db'
        return None
