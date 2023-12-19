import collections
import logging
import pprint

logging.basicConfig(
    filename="example.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


class LoggingDict(dict):
    def __setitem__(self, key, value):
        logging.info("Setting %r to %r" % (key, value))
        super().__setitem__(key, value)


class LoggingOrderedDict(LoggingDict, collections.OrderedDict):
    pass


def main():
    # Example usage
    my_dict = LoggingOrderedDict()
    my_dict["key1"] = "value1"
    my_dict["key2"] = "value2"
    print(f"==>> my_dict: {my_dict}")


if __name__ == "__main__":
    main()
