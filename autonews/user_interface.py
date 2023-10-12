import textwrap

def get_author_and_text():
    author = input("Please input the author's name: ")

    print("Please input the text you want summarized. Input 'END' in a new line to finish.")
    user_input_lines = []
    while True:
        line = input()
        if line == 'END':
            break
        user_input_lines.append(line)

    user_input_text = "\n".join(user_input_lines)
    return author, user_input_text

def print_summarized_text(summarized_text):
    decorated_text = "\n" + "="*30 + " Summarized Text " + "="*30 + "\n"
    wrapped_text = "\n".join(textwrap.wrap(summarized_text, width=80))
    decorated_text += wrapped_text + "\n" + "="*80 + "\n"
    print(decorated_text)
