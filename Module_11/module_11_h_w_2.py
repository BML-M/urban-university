class Introspection:
    def __init__(self, obj):
        self.obj = obj

    def introspection_info(self):
        obj_type = type(self.obj).__name__
        attributes = [attr for attr in dir(self.obj) if not callable(getattr(self.obj, attr))]
        methods = [method for method in dir(self.obj) if callable(getattr(self.obj, method))]
        module = self.obj.__class__.__module__

        return {'type': obj_type, 'attributes': attributes, 'methods': methods, 'module': module}

# Пример использования
number_info = Introspection(42)
print(number_info.introspection_info())