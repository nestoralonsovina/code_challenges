class Test:

    @staticmethod
    def assert_equals(a, b):
        try:
            assert a == b
            print(str(a) + " == " + str(b) + " [OK] ")
        except AssertionError:
            print(str(a) + " should equal " + str(b) + " [FAILED] ")

    @staticmethod
    def it(s: str):
        print(s)

    @staticmethod
    def describe(s: str):
        print(s)

