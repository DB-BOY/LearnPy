# -*- coding: utf-8 -*-
import hmac

message = b'Hello, world!'
key = b'secret'
h = hmac.new(key, message, digestmod='MD5')
print(h)
print(h.hexdigest())
