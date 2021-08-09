# 3-4.

class DivBlockDecorator:
    def __init__(self, style_class):
        self.style_class = style_class

    def __call__(self, function):
        def wrap(*args: list):
            str_add = f"<div class={self.style_class}>\n"
            str_add_2 = "</div>\n"
            transformation = str_add + function(*args) + str_add_2
            return transformation

        return wrap


def body_decor(function):
    def wrap(*args):
        str_add = "</body>\n"
        str_add_2 = "</body>\n"
        transformation = str_add + function(*args) + str_add_2
        return transformation

    return wrap


def head_decor(title="title"):
    def decor(function):
        def wrap(*args: list):
            str_add = "<head>\n"
            str_add_2 = f"<title>{title}</title>\n"
            str_add_3 = "</head>\n"
            transformation = str_add + str_add_2 \
                             + str_add_3 + function(*args)
            return transformation

        return wrap

    return decor


def html_decor(function):
    def wrap(*args):
        str_add = "<html>\n"
        str_add_2 = "<html>\n"
        transformation = str_add + function(*args) + str_add_2
        return transformation

    return wrap


@html_decor
@head_decor("Users")
@body_decor
@DivBlockDecorator("users_block")
def get_names_page(names_list):
    template_head = "<h3> User names: </h3>\n"
    template = "<p> {} </p>\n"
    str_add = ""
    str_add += template_head
    for x in names_list:
        str_add += template.format(x)
    return str_add


names_list = ["Misha", "Olya", "Vitaliy", "Vita"]
print(get_names_page(names_list))