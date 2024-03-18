import base64
class Codec:
    def __init__(self):
        self.mapUrl = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        splitUrl = longUrl.rsplit("/", 2)
        strEnc = "/".join(str(element) for element in splitUrl[1:])
        encUrl = base64.b64encode(strEnc.encode("utf-8"))[:6]
        self.mapUrl[encUrl.decode("utf-8")] = longUrl
        return "http://tinyurl.com/" + encUrl.decode("utf-8")

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        idUrl = shortUrl.split("/")[-1]
        return self.mapUrl[idUrl]
        
    
codec = Codec()
url = "https://leetcode.com/problems/design-tinyurl"
codec.decode(codec.encode(url))