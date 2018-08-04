import fnmatch


def filter_objects(objects, pattern, key=None, return_object=False):
    """Returns a list of values filtered from objects.

    :param objects: **required**.
    :type objects: list[dict].

    :param pattern: **required**. Regex.
    :type pattern: str.

    :param key: Object key.
    :type key: str.

    :param return_object: If set to False returns a list of the ``object[key]``
        values matching the pattern. Otherwise, the entire object is returned.
    :type return_object: bool.
    """
    if return_object:
        return [i for i in objects if fnmatch.fnmatch(i[key], pattern)]
    if key:
        return fnmatch.filter([_[key] for _ in objects], pattern)
    return fnmatch.filter(objects, pattern)
