import re
import glob
import html
from pathlib import Path


def preprocess_tweet_file(old_path: Path, new_path: Path):
    with old_path.open("r", encoding="utf8") as fp:
        old_lines = fp.readlines()
    # 去重
    lines = list(map(lambda x: " ".join(x.split(" ")[1:]), old_lines))
    lines = list(set(lines))
    # html 转义
    lines = list(map(lambda x: html.unescape(x), lines))
    # 规则替换
    for i in range(len(lines)):
        lines[i] = re_sub_by_rules(lines[i])
    # 去重
    lines = list(set(lines))
    # 去空
    lines = list(filter(lambda x: len(x.strip()) != 0, lines))
    # 删除开头末尾的空格
    lines = list(map(lambda x: x.strip() + "\n", lines))
    with new_path.open("w", encoding="utf8") as fp:
        fp.writelines(lines)


def re_sub_by_rules(line: str) -> str:
    # 一些正则替换
    re_rules = [
        # 省略号
        (r"\.{3,}", "..."),
        # 省略号2
        (r"\.{2}", "."),
        # hashtag 取消井号
        (r"#(\w+)", r" "),
        # 去除电话号码 xxx-xxx-xxx
        (r"(\d+-){2,}\d+", " "),
        # 删除 @ 人
        (r"\B@.+?\b", " "),
        # 中文引号转化
        (r"’", "'"),
        (r"[“”]", '"'),
        # 删除邮箱
        (r"([^\x00-\x20\x22\x28\x29\x2c\x2e\x3a-\x3c\x3e\x40\x5b-\x5d\x7f-\xff]+|\x22([^\x0d\x22\x5c\x80-\xff]|\x5c[\x00-\x7f])*\x22)(\x2e([^\x00-\x20\x22\x28\x29\x2c\x2e\x3a-\x3c\x3e\x40\x5b-\x5d\x7f-\xff]+|\x22([^\x0d\x22\x5c\x80-\xff]|\x5c[\x00-\x7f])*\x22))*\x40([^\x00-\x20\x22\x28\x29\x2c\x2e\x3a-\x3c\x3e\x40\x5b-\x5d\x7f-\xff]+|\x5b([^\x0d\x5b-\x5d\x80-\xff]|\x5c[\x00-\x7f])*\x5d)(\x2e([^\x00-\x20\x22\x28\x29\x2c\x2e\x3a-\x3c\x3e\x40\x5b-\x5d\x7f-\xff]+|\x5b([^\x0d\x5b-\x5d\x80-\xff]|\x5c[\x00-\x7f])*\x5d))*", " "),
        # 删除 url 和 www 网址
        (r"((([A-Za-z]{3,9}:(?:\/\/)?)(?:[-;:&=\+\$,\w]+@)?[A-Za-z0-9.-]+|(?:www.|[-;:&=\+\$,\w]+@)[A-Za-z0-9.-]+)((?:\/[\+~%\/.\w_-]*)?\??(?:[-\+=&;%@.\w_]*)#?(?:[.\!\/\\w]*))?)", " "),
        # 去除非 ascii
        (r"[^\x00-\x7F]+", " "),
        # 数字
        (r"-?\d+(\.\d*)*%?", " "),
        # hyphen
        (r"-", " "),
        # 多个空白符变一个
        (r"\s+", " ")
    ]
    ret = line
    for pattern, repl in re_rules:
        ret = re.sub(pattern, repl, ret)
    return ret
