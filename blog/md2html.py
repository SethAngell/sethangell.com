from collections import deque
import re

def text_file_to_stack(path: str) -> deque:

    # Variable creation
    md_stack = deque()
    md_post = open(path, "r")

    # Push each line onto a deque
    for line in md_post:
        md_stack.append(line.strip("\n"))

    return md_stack

def str_to_stack(md_post: str) -> deque:
    # Variable creation
    md_stack = deque()
    md_post = md_post.split("\n")

    # Push each line onto a deque
    for line in md_post:
        md_stack.append(line.strip("\n"))

    return md_stack

def md_stripper(md_line: str) -> str:
    style_stack = deque()
    text_stack = deque()
    formatted_list = []
    style_symbols = ("\\", "_", "[")
    char_pointer = 0

    while char_pointer < len(md_line):
        if md_line[char_pointer] not in style_symbols:
            text_stack.append(md_line[char_pointer])
        else:
            if md_line[char_pointer] == "\\":
                text_stack.append(md_line[char_pointer + 1])
                char_pointer += 1
            else:
                if (char_pointer + 1 != len(md_line)) and (
                        md_line[char_pointer] + md_line[char_pointer + 1] == "__"):
                    if len(style_stack) % 2 == 0:
                        style_stack.append("<b class=\"blog_text\">")
                        text_stack.append("%({})%")
                        char_pointer += 1
                    else:
                        style_stack.append("</b>")
                        text_stack.append("%({})%")
                        char_pointer += 1
                else:
                    if (md_line[char_pointer] == "_"):
                        if len(style_stack) % 2 == 0:
                            style_stack.append("<i class=\"blog_text\">")
                            text_stack.append("%({})%")
                        else:
                            style_stack.append("</i>")
                            text_stack.append("%({})%")
                    else:
                        if (md_line[char_pointer] == "["):
                            link_search = char_pointer
                            md_url = ""
                            while md_line[link_search] != '(':
                                link_search += 1
                            link_search += 1
                            while md_line[link_search] != ')':
                                md_url += md_line[link_search]
                                link_search += 1
                            text_stack.append("%({})%")
                            style_stack.append(f'<a href=\"https://{md_url}\" class=\"blog_text\">')
                            char_pointer += 1
                            while md_line[char_pointer] != "]":
                                text_stack.append(md_line[char_pointer])
                                char_pointer += 1
                            text_stack.append("%({})%")
                            style_stack.append("</a>")
                            char_pointer = link_search
        char_pointer += 1

    while len(text_stack) != 0:
        current_char = text_stack.pop()
        if current_char != "%({})%":
            formatted_list.insert(0, current_char)

    return "".join(formatted_list)

def remove_blank_lines(preprocessed_article: deque) -> deque:
    preprocessed_article.append("You've popped the whole stack")
    current_section = preprocessed_article.popleft()
    while current_section != "You've popped the whole stack":
        if len(current_section) == 0:
            current_section = preprocessed_article.popleft()
        else:
            preprocessed_article.append(current_section)
            current_section = preprocessed_article.popleft()
    return preprocessed_article

# TODO: Add recursion(?) for nested lists
def section_to_div(sections: deque) -> deque:
    html_conversion_dict = {
        "#":    ("<h1 class=\"blog_text\">", "</h1>"),
        "##":   ("<h2 class=\"blog_text\">", "</h2>"),
        "###":  ("<h3 class=\"blog_text\">", "</h3>"),
        "p":    ("<p class=\"blog_text\">", "</p>"),
        "*":    ("<li class=\"blog_text\">", "</li>"),
        "n":    ("<li class=\"blog_text\">", "</li>"),
    }
    md_symbol_set = ("#", "##", "###", "*",)
    stopping_set = ('<h1', '<h2',"<h3", "<p ", "<ol", "<ul")

    def md_type_identifier(chunk_to_parse: str) -> str:
        parsed_string = chunk_to_parse.split(" ")
        if parsed_string[0] in md_symbol_set:
            md_symbol = parsed_string.pop(0)
            return f'{html_conversion_dict[md_symbol][0]}{md_style_to_html(" ".join(parsed_string))}{html_conversion_dict[md_symbol][1]}'
        else:
            if re.search("^[0-9]+[.]", chunk_to_parse):
                parsed_string.pop(0)
                return f'<li class=\"blog_text\">{md_style_to_html(" ".join(parsed_string))}</li>'
            else:
                return f'<p class=\"blog_text\">{md_style_to_html(" ".join(parsed_string))}</p>'


    current_section = sections.popleft()
    while current_section[0:3] not in stopping_set:
        if current_section[0] == "*":
            sections.append("<ul class=\"blog_text\">")
            while current_section[0] == "*":
                sections.append(md_type_identifier(current_section))
                current_section = sections.popleft()
            sections.append("</ul>")
        else:
            if re.search("^[0-9]+[.]", current_section):
                sections.append("<ol class=\"blog_text\">")
                while re.search("^[0-9]+[.]", current_section):
                    sections.append(md_type_identifier(current_section))
                    current_section = sections.popleft()
                sections.append("</ol>")
            else:
                if current_section[0:3] == "```":
                    sections.append("<div class=\"code_snippet\">")
                    current_section = sections.popleft()
                    while current_section[0:3] != "```":
                        sections.append(f'<p class=\"code\">{current_section}</p>')
                        current_section = sections.popleft()
                    sections.append("</div>")
                    current_section = sections.popleft()

                else:
                   sections.append(md_type_identifier(current_section))
                   current_section = sections.popleft()
    sections.appendleft(current_section)

    return sections

# TODO: Add condition for href links

def md_style_to_html(line_to_style: str) -> str:
    style_stack = deque()
    text_stack = deque()
    formatted_list = []
    style_symbols = ("\\", "_", "[")
    char_pointer = 0


    while char_pointer < len(line_to_style):
        if line_to_style[char_pointer] not in style_symbols:
            text_stack.append(line_to_style[char_pointer])
        else:
            if line_to_style[char_pointer] == "\\":
                text_stack.append(line_to_style[char_pointer+1])
                char_pointer+=1
            else:
                if (char_pointer + 1 != len(line_to_style)) and (line_to_style[char_pointer]+line_to_style[char_pointer+1] == "__"):
                    if len(style_stack) % 2 == 0:
                        style_stack.append("<b>")
                        text_stack.append("%({})%")
                        char_pointer+=1
                    else:
                        style_stack.append("</b>")
                        text_stack.append("%({})%")
                        char_pointer+=1
                else:
                    if (line_to_style[char_pointer] == "_"):
                        if len(style_stack) % 2 == 0:
                            style_stack.append("<i>")
                            text_stack.append("%({})%")
                        else:
                            style_stack.append("</i>")
                            text_stack.append("%({})%")
                    else:
                        if (line_to_style[char_pointer] == "["):
                            link_search = char_pointer
                            md_url = ""
                            while line_to_style[link_search] != '(':
                                link_search+=1
                            link_search += 1
                            while line_to_style[link_search] != ')':
                                md_url+=line_to_style[link_search]
                                link_search+=1
                            text_stack.append("%({})%")
                            style_stack.append(f'<a href=\"https://{md_url}\" class=\"blog_text\">')
                            char_pointer+=1
                            while line_to_style[char_pointer] != "]":
                                text_stack.append(line_to_style[char_pointer])
                                char_pointer+=1
                            text_stack.append("%({})%")
                            style_stack.append("</a>")
                            char_pointer = link_search
        char_pointer+=1

    while len(text_stack) != 0:
        current_char = text_stack.pop()
        if current_char != "%({})%":
            formatted_list.insert(0, current_char)
        else:
            formatted_list.insert(0, style_stack.pop())

    return "".join(formatted_list)

def sections_to_html_string(html_sections: deque) -> str:
    html_string = ""
    while len(html_sections) != 0:
        html_string += html_sections.popleft()
    return html_string

def on_save_attribute_extraction(md_post: str, title: str) -> dict:
    if len(title) == 0:
        sectioned_post = md_post.split("\n")

        blog_preview = md_stripper(sectioned_post[1])[:100]

        raw_title = sectioned_post.pop(0).split(" ")
        raw_title.pop(0)
        cleaned_title = " ".join(raw_title)

        sectioned_post = "\n".join(sectioned_post)

        attribute_dict = {
            "title": cleaned_title,
            "preview": blog_preview,
            "body": sectioned_post
        }
    else:
        sectioned_post = md_post.split("\n")

        blog_preview = md_stripper(sectioned_post[0])[:100]
        sectioned_post = "\n".join(sectioned_post)

        attribute_dict = {
            "title": title,
            "preview": blog_preview,
            "body": sectioned_post
        }

    return attribute_dict

def sanitized_html_for_site(raw_md_post: str) -> str:
    sectioned_md_post = str_to_stack(raw_md_post)
    condensed_md_post = remove_blank_lines(sectioned_md_post)
    converted_md_post = section_to_div(condensed_md_post)
    html_string = sections_to_html_string(converted_md_post)

    return html_string


# test_stack = text_file_to_stack("SampleHeaderPost_1.txt")
# test_stack = text_file_to_stack("ComfortablyClueless.txt")
# test_stack = remove_blank_lines(test_stack)
# test_stack = section_to_div(test_stack)
# test_html = open("test.html", "w+")
# while len(test_stack) != 0:
#     test_html.write(test_stack.popleft())
