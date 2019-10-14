from flask_restplus import reqparse

parser = reqparse.RequestParser()


class ArgsMixIn(object):
    def __init__(self, *args, **kwargs):

        self.reqparse = parser.copy()
        super(ArgsMixIn, self).__init__(*args, **kwargs)

    def _get_args(self, args={}, strict=True, **kwargs):

        for k, v in args.items():
            self.reqparse.add_argument(k, **v)
        args = {k: v for k, v in self.reqparse.parse_args(strict=strict).items()}
        for k, v in kwargs.items():
            args[k] = v
        return args

    def parse_args(self, args={}, strict=True, enable_pg=False, **kwargs):
        if enable_pg:
            args.setdefault('pgsize', self._set_args(dest='pgsize', type=int, default=10))
            args.setdefault('pgnum', self._set_args(dest='pgnum', type=int, default=1))
            # args.setdefault('pgsort', self.set_args(dest='pgsort', location='args', default='-id'))

        for k, v in args.items():
            self.reqparse.add_argument(k, **v)
        args = {k: v for k, v in self.reqparse.parse_args(strict=strict).items()}
        for k, v in kwargs.items():
            args[k] = v
        return args

    @staticmethod
    def _set_args(init={}, **kw):
        if init:
            for k, v in kw.items():
                init[k] = v
        else:
            init = kw
        return init
