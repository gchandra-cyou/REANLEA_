import inspect
import itertools as it


def filtered_locals(caller_locals):
    result = caller_locals.copy()
    ignored_local_args = ["self", "kwargs"]
    for arg in ignored_local_args:
        result.pop(arg, caller_locals)
    return result

def digest_config(obj, kwargs, caller_locals={}):
    """
    Sets init args and CONFIG values as local variables
    The purpose of this function is to ensure that all
    configuration of any object is inheritable, able to
    be easily passed into instantiation, and is attached
    as an attribute of the object.
    """

    # Assemble list of CONFIGs from all super classes
    classes_in_hierarchy = [obj.__class__]
    static_configs = []
    while len(classes_in_hierarchy) > 0:
        Class = classes_in_hierarchy.pop()
        classes_in_hierarchy += Class.__bases__
        if hasattr(Class, "CONFIG"):
            static_configs.append(Class.CONFIG)

    # Order matters a lot here, first dicts have higher priority
    caller_locals = filtered_locals(caller_locals)
    all_dicts = [kwargs, caller_locals, obj.__dict__]
    all_dicts += static_configs
    obj.__dict__ = merge_dicts_recursively(*reversed(all_dicts))

def merge_dicts_recursively(*dicts):
    result = dict()
    all_items = it.chain(*[d.items() for d in dicts])
    for key, value in all_items:
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = merge_dicts_recursively(result[key], value)
        else:
            result[key] = value
    return result
