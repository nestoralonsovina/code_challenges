class Test:
    @staticmethod
    def assert_equals(a, b):
        try:
            assert a == b
            print(str(a) + " are equal " + str(b))
        except AssertionError:
            print(str(a) + " does not equal " + str(b))
