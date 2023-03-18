class Printer(object):
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    @classmethod
    def warning(cls, text=""):
        print(f"{cls.WARNING}{text}{cls.ENDC}")

    @classmethod
    def error(cls, text=""):
        print(f"{cls.FAIL}{text}{cls.ENDC}")

    @classmethod
    def success(cls, text=""):
        print(f"{cls.OKGREEN}{text}{cls.ENDC}")

    @classmethod
    def info(cls, text=""):
        print(f"{cls.OKCYAN}{text}{cls.ENDC}")
