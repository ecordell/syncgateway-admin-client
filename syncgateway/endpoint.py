class Endpoint(object):

    def __init__(self, url, database, session):
        self.url = url
        self.database = database
        self.session = session
