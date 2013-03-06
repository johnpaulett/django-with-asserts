VERSION = (0, 0, 1, 'final')


def get_version():
    main = '.'.join(str(x) for x in VERSION[:3])
    sub = VERSION[3] if VERSION[3] != 'final' else ''
    return str(main + sub)
