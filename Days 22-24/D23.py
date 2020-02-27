from functools import wraps, partial


def make_html(element):
    def dec(func):
        @wraps(func)
        def f_wrapper(*args, **kwargs):
            return '<' + element + '>' + func(*args, **kwargs) + '</' + element + '>'

        return f_wrapper

    return dec


@make_html('p')
@make_html('strong')
def get_text(text=None):
    return text


if __name__ == '__main__':
    test = 'this is a string'
    print(get_text(text=test))
