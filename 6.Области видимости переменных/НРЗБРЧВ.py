translated_text = None


def translate(text):
    new = text.replace("-", "")
    new = new.replace(",", "")
    new = new.replace(".", "")
    new = new.replace("а", "")
    new = new.replace("е", "")
    new = new.replace("ё", "")
    new = new.replace("и", "")
    new = new.replace("о", "")
    new = new.replace("у", "")
    new = new.replace("ы", "")
    new = new.replace("э", "")
    new = new.replace("ю", "")
    new = new.replace("я", "")
    new = new.replace("А", "")
    new = new.replace("Е", "")
    new = new.replace("Ё", "")
    new = new.replace("И", "")
    new = new.replace("О", "")
    new = new.replace("У", "")
    new = new.replace("Ы", "")
    new = new.replace("Э", "")
    new = new.replace("Ю", "")
    new = new.replace("Я", "")
    new = ' '.join(new.split())
    global translated_text
    translated_text = new
