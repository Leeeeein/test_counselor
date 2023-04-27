import re

import re

def remove_special_characters(text):
    """
    删除中英文字符串中的特殊字符
    """
    # 定义正则表达式，匹配中英文、数字、空格和常用标点符号
    pattern = re.compile('[^\u4e00-\u9fa5a-zA-Z0-9 \u0020，。！？、；：“”‘’（）《》【】——…]+')
    cleaned_text = re.sub(r'[^\u4e00-\u9fa5a-zA-Z0-9]+', ' ', text)

    return cleaned_text

def split_string(text, separator=','):
    """
    根据指定的分隔符将字符串分成多个字符串
    """
    # 使用split()函数按照分隔符分割字符串
    split_text = text.split(separator)
    return split_text

