# Copied from Internet
import base64
import hmac
import hashlib
import json

from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

SECRET_KEY = ""


def getSignature(base64Header,base64Payload,secret):
    block = base64Header.decode('utf-8') + "." + base64Payload.decode('utf-8')
    digest = hmac.new(bytes(secret,'utf-8'),block.encode('utf-8'), digestmod = hashlib.sha256).digest()
    signature = base64.urlsafe_b64encode(digest)
    return signature.decode('utf-8')[: -1]


def encodeJWT(data,key,algorithm):
    payload = data
    header = {
        "alg": algorithm,
        "typ": "JWT"
    }
    base64Header = base64.b64encode(json.dumps(header).encode("utf-8"))
    base64Payload = base64.b64encode(json.dumps(payload).encode("utf-8"))
    sig = getSignature(base64Header,base64Payload,key)
    encodedJWT = base64Header.decode("utf-8")+"."+base64Payload.decode("utf-8")+"."+sig
    return encodedJWT


def decodeJWT(access_token,key):
  header = access_token.split('.')[0]
  payload = access_token.split('.')[1]
  decodedPayload = base64.b64decode(payload)
  sig = getSignature(header.encode('utf-8'),payload.encode('utf-8'),key)
  res = {
    "payload": decodedPayload.decode('utf-8'),
    "verified": (sig==access_token.split('.')[2])
  }
  if(sig==access_token.split('.')[2]):
    return res
  else:
    return "Couldn't Verify Signature"


class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=403, detail="Invalid authentication scheme.")
            if not self.verify_jwt(credentials.credentials):
                print(credentials.credentials)
                raise HTTPException(status_code=403, detail="Invalid token or expired token.")
            return credentials.credentials
        else:
            raise HTTPException(status_code=403, detail="Invalid authorization code.")

    def verify_jwt(self, jwtoken: str) -> bool:
        isTokenValid: bool = False

        try:
            decoded = decodeJWT(jwtoken, SECRET_KEY)
            payload = json.loads(decoded["payload"])["sub"]
            # payload = decodeJWT(jwtoken)
        except:
            payload = None
        if payload:
            isTokenValid = True
        return isTokenValid