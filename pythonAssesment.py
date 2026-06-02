import re


def count_specific_word(text, search_word):
    words = text.lower().split()

    count = 0

    for word in words:  # FOR LOOP
        cleaned_word = re.sub(r'[^\w]', '', word)
        # IF/ELSE
        if cleaned_word == search_word.lower():  
            count += 1
        else:
            pass

    return count


def identify_most_common_word(text):

    if text == "":
        return None

    words = re.findall(r'\b\w+\b', text.lower())

    if len(words) == 0:
        return None

    frequency = {}
    # FOR LOOP
    for word in words:  
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    most_common = None
    highest_count = 0

    for word in frequency:
        if frequency[word] > highest_count:
            highest_count = frequency[word]
            most_common = word

    return most_common


def calculate_average_word_length(text):

    words = re.findall(r'\b\w+\b', text)

    if len(words) == 0:
        return 0

    total_length = 0
    # FOR LOOP
    for word in words:  
        total_length += len(word)

    average = total_length / len(words)

    return float(average)


def count_paragraphs(text):

    if text.strip() == "":
        return 1

    paragraphs = re.split(r'\n\s*\n', text.strip())

    return len(paragraphs)


def count_sentences(text):

    if text.strip() == "":
        return 1

    sentences = re.split(r'[.!?]+', text)

    count = 0

    for sentence in sentences:  # FOR LOOP
        if sentence.strip() != "":
            count += 1

    return count


# MAIN PROGRAM

try:
    with open("news_article.txt", "r", encoding="utf-8") as file:
        article = file.read()
except FileNotFoundError:
    article = ""

search_word = input("Enter word to search: ")

print("Word Count:", count_specific_word(article, search_word))
print("Most Common Word:", identify_most_common_word(article))
print("Average Word Length:", calculate_average_word_length(article))
print("Paragraph Count:", count_paragraphs(article))
print("Sentence Count:", count_sentences(article))


# WHILE LOOP REQUIREMENT
counter = 0

while counter < 1:
    counter += 1