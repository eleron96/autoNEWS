from api_handler import summarize_text
from file_handler import save_summary
from user_interface import get_author_and_text, print_summarized_text

def main():
    author, user_input_text = get_author_and_text()
    print("\nSending text to OpenAI GPT...")
    summarized_text = summarize_text(user_input_text, author)
    print_summarized_text(summarized_text)
    save_summary(author, summarized_text)

if __name__ == "__main__":
    main()
