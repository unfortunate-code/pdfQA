import sys
from hugchat import hugchat
from extract_text_from_pdf import extract_text_from_pdf

def main(file):
    text = extract_text_from_pdf(file)
    print(text)
    chatbot = hugchat.ChatBot()
    print(chatbot.chat("'" + text + "'\n How many years of experience does the person in this resume have?"))

if __name__ == '__main__':
    main(sys.argv[1])