from abc import ABC, abstractmethod

class WebAPI(ABC):
    def __init__(self, apikey=None):
        self.apikey = apikey

    def _download_url(self, url):
        # TODO: Implement web API request code in a way that supports all types of web APIs
        pass

    def set_apikey(self, apikey):
        self.apikey = apikey

    @abstractmethod
    def load_data(self):
        pass

    @abstractmethod
    def transclude(self, message):
        pass

def test_api(message, apikey, webapi):
    webapi.set_apikey(apikey)
    webapi.load_data()
    result = webapi.transclude(message)
    print(result)

if __name__ == "__main__":
    class MyAPI(WebAPI):
        def __init__(self, zip, ccode, apikey=None):
            super().__init__(apikey)
            self.zip = zip
            self.ccode = ccode

        def load_data(self):
            # TODO: Load data for MyAPI using zip and ccode
            pass

        def transclude(self, message):
            # TODO: Transclude message using data loaded from MyAPI
            return message.replace("@myapi", "some data from MyAPI")

    # Example usage
    myapi = MyAPI("90210", "US", "MY_APIKEY")
    test_api("Testing MyAPI: @myapi", "MY_APIKEY", myapi)
