def close(self):
    """
    Calls remove() method on the private session attribute or close() on the class Session.
    """
    self.__session.close()
