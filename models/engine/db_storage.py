def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()
