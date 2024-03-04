def read_one_line():
    df = open("data.txt", "r")
    line = df.readline()
    print(line)
    df.close()


def cannot_read_after_close():
    df = open("data.txt", "r")
    df.readline()
    df.close()
    df.read()  # ERROR, connection to the file no more exist


def read_all_content_all_at_once():
    df = open("data.txt", "r")
    data = df.read()
    print(data)
    df.close()


def read_all_content_line_by_line_using_for():
    df = open("data.txt", "r")
    for line in df:
        print(line)
    df.close()


def read_all_content_line_by_line_using_while():
    df = open("data.txt", "r")
    line = df.readline()  # priming
    while line:
        print(line)
        line = df.readline()  # read next line

    df.close()


def read_all_content_as_list():
    df = open("data.txt", "r")
    lines = df.readlines()
    print(lines)
    df.close()


def read_first_10_line_of_webpage(url):
    import urllib.request
    socket = urllib.request.urlopen(url)
    for i in range(10):
        line = socket.readline()
        print(line)


if __name__ == '__main__':
    ...  # or pass
    # read_one_line()
    # cannot_read_after_close()
    # read_all_content_all_at_once()
    # read_all_content_line_by_line_using_for()  # why empty lines?
    # read_all_content_line_by_line_using_while()  # why empty lines?
    # read_all_content_as_list()
    # read_first_10_line_of_webpage("https://en.wikipedia.org/wiki/Macalester_College")
