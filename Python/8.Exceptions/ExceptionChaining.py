def func():
    raise IOError

try:
    func()
except IOError as exc:
    raise RuntimeError('Faild To open database') from exc

