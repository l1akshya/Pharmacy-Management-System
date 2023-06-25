from PIL import Image
from pytesseract import pytesseract
import enum
import re

def image_to_text(path):

    class Os (enum.Enum):
        Mac=0
        Windows=1

    class Language(enum.Enum):
        Eng='eng'

    class image_reader:

        def __init__(self,os:'Os'):
            if os==Os.Mac:
                print("Mac")

            if os==Os.Windows:
                windows_path= r"C:\Program Files\Tesseract-OCR\tesseract.exe"
                pytesseract.tesseract_cmd=windows_path
                print("Windows")

        def extract_text(self,image:str,lang:str)->str:
            img=Image.open(image)
            extracted_text=pytesseract.image_to_string(img, lang=lang)
            return extracted_text
        

    ir=image_reader(Os.Windows)
    text=ir.extract_text(path,lang = 'eng')

    def extract_capital_words(sentence):
        pattern = r'\b[A-Z]+\b'
        capital_words = re.findall(pattern, sentence)
        return capital_words
    capital_words = extract_capital_words(text)

    def delete_single_letter_strings(string_list):
        filtered_list = [string for string in string_list if len(string) > 1]
        return filtered_list

    capital_words=delete_single_letter_strings(capital_words)


    def check_words_in_file(word_list):
        # Read the text file and split it into words
        with open('medicinerepo.txt', 'r') as file:
            text = file.read()
            words_in_file = text.split()

        # Check if words from the list are present in the text file
        present_words = [word for word in word_list if word in words_in_file]
        return present_words

    def list_to_string(string_list):
        if len(string_list) <= 3:
            return string_list[0]
        else:
            return ""

    present_words = check_words_in_file(capital_words)
    search_word=list_to_string(present_words)
    return search_word



