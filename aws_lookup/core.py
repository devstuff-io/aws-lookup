import fnmatch

from boto3.session import Session


def get_session(*args, **kwargs):
    """
    Optional parameters:

    See the boto3 _documentation

    :param aws_access_key_id: AWS access key ID
    :type aws_access_key_id: string
    :param aws_secret_access_key: AWS secret access key
    :type aws_secret_access_key: string
    :param aws_session_token: AWS temporary session token
    :type aws_session_token: string
    :param region_name: Default region when creating new connections
    :type region_name: string
    :param botocore_session: Use this Botocore session instead of creating a new default one
    :type botocore_session: botocore.session.Session
    :param profile_name: The name of a profile to use. If not given, then the default profile is used.
    :type profile_name: string

    .. _documentation: http://boto3.readthedocs.io/en/latest/reference/core/session.html
    """
    return Session(**kwargs)


def get_services(session=None, with_custom=True, *args, **kwargs):
    """Returns a list of all boto3 services and custom command groups."""
    if session is None:
        session = get_session(*args, **kwargs)
    services = session.get_available_services()
    services.sort()
    return services


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
