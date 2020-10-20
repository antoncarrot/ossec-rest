DJANGO_DB_NAME = 'ossec'


class OssecRouter:
    route_app_label = 'ossec_data'

    def db_for_read(self, model, **hints):
        if model._meta.app_label == self.route_app_label:
            return DJANGO_DB_NAME
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == self.route_app_label:
            return DJANGO_DB_NAME
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == self.route_app_label or obj2._meta.app_label == self.route_app_label:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == self.route_app_label:
            return db == DJANGO_DB_NAME
        return None
