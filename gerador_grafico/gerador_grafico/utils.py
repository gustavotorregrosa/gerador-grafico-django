def transform_to_json(obj):
    if hasattr(obj, 'to_dict') and callable(getattr(obj, 'to_dict')):
        return obj.to_dict()
    else:
        raise AttributeError("Object does not have a callable to_dict method")
    
def transform_list_to_json(obj_list):
    return [transform_to_json(obj) for obj in obj_list]