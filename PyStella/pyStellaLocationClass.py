class pyStellaLocationClass:

    def __init__(self, request_server=None):
        self.__latitude__ = 0
        self.__longitude__ = 0
        self.__elevation__ = 0
        self.__name__ = ''
        self.requestServer = request_server

    def set(self, latitude, longitude, elevation=0):
        self.__latitude__ = latitude
        self.__longitude__ = longitude
        self.__elevation__ = elevation

        r = self.requestServer.post(service='location/setlocationfields',
                                    data={'latitude': str(latitude), 'longitude': str(longitude),
                                          'altitude': str(elevation)})

    def get_all_location(self):
        r = self.requestServer.get(service='location/list')
        return r
