import string
def get_value(name):
    # return the value of given name
    values = dict()
    for index, letter in enumerate(string.ascii_letters):
        values[letter] = index + 1
    value = 0
    for letter in name:
        if letter in string.ascii_letters:
            value = values[letter] + value
        else:
                break
    return value

def get_name_list(file_name):
    name_list=[]
    #load text file, get all the first names to name_list
    fin = open(file_name)
    for line in fin:
        name = line.strip()
        name_list.append(name)
    return name_list


def who_has_highest_value(name_list):
    # return the name with highest value among the given name_list
    maxName = ''
    maxValue = 0
    for name in name_list:
        if get_value(name) > maxValue:
            maxName = name
            maxValue = get_value(name)
    return maxName    

def get_words(file_name):
    # return a list of words
    word_list=[]
    #load text file, get all the first names to name_list
    fin = open(file_name)
    for line in fin:
        word = line.strip()
        word_list.append(word)
    return word_list


def get_words_with_same_value(word_list, value):
    # return a list of matched words
    matchedWords = [];
    for word in word_list:
        if get_value(word) == value:
            matchedWords.append(word)
    if len(matchedWords) == 0:
        return 'None'
    else:
        return matchedWords


def main():
    print(who_has_highest_value(get_name_list('roster.txt')))
    print(get_words_with_same_value(get_words('words.txt'), get_value('Alden')))

if __name__ == '__main__':
    main();