"""一个最小示例：验证这个仓库已经能跑起来。"""


def greet(name: str = "world") -> str:
    """返回一句问候语。"""
    return f"Hello, {name}!"


if __name__ == "__main__":
    print(greet())
    print(greet("GitHub"))
