

class DanbooruErrors(Exception):
    pass


class DanbooruLoginRateLimitError(DanbooruErrors):
    def __init__(self, msg):
        super(DanbooruLoginRateLimitError, self).__init__(msg)
        self._msg = msg

    def __str__(self):
        return self._msg


class DanbooruAuthenticationFailure(DanbooruErrors):
    def __init__(self, msg):
        super(DanbooruAuthenticationFailure, self).__init__(msg)
        self._msg = msg

    def __str__(self):
        return self._msg


class DanbooruAccessDenied(DanbooruErrors):
    def __init__(self, msg):
        super(DanbooruAccessDenied, self).__init__(msg)
        self._msg = msg

    def __str__(self):
        return self._msg


class DanbooruLimitError(DanbooruErrors):
    def __init__(self, msg):
        super(DanbooruLimitError, self).__init__(msg)
        self._msg = msg

    def __str__(self):
        return self._msg


class DanbooruUnknownError(DanbooruErrors):
    pass



