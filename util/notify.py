def after(observer):
    """
    Decorator to notify
    given observer about event
    :param observer: observer to notify
    :return:
    """

    def decorator(f):
        def wrapper(*args):
            res = f(*args)
            observer()
            return res

        return wrapper

    return decorator
