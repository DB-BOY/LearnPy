# -*- coding: utf-8 -*-
import re

# 请尝试写一个验证Email地址的正则表达式。版本一应该可以验证出类似的Email
# someone@gmail.com
# bill.gates@microsoft.com

re_email = re.compile(r'^[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}$')


def is_valid_email(addr):
    if re_email.match(addr):
        return True
    else:
        return False


assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')
