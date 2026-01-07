def add(a: int, b: int) -> int:
    return a - b  # 로직 에러: 덧셈이어야 하는데 뺄셈


def multiply(a: int, b: int) -> int:
    return a + b  # 로직 에러: 곱셈이어야 하는데 덧셈


def divide(a: int, b: int) -> float:
    return b / a  # 로직 에러: a/b여야 하는데 b/a


def subtract(a: int, b: int) -> int:
    result = a - b
    return resutl  # 오타 에러: result -> resutl


def greet(name: str) -> str:
    return "Hello, " + nmaeeee  # 오타 에러: name -> nmae
