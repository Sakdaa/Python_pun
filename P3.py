import string

def word_freq(text):
    # Remove punctuation
    translator = str.maketrans('', '', string.punctuation)
    cleaned_text = text.translate(translator)
    
    # Split text into words
    words = cleaned_text.split()
    
    # Count occurrences of each word
    word_count = {}
    for word in words:
        if len(word) > 1:  # Discard words of length 1 or less
            word_count[word] = word_count.get(word, 0) + 1
    
    return word_count

if __name__ == "__main__":
    # Multi-line text input
    txt = ("Evil is done by oneself; " +
        "by oneself is one defiled. \n " +
        "Evil is left undone by oneself; " +
        "by oneself is one cleansed. \n " +
        "Purity and impurity are one's own doing. \n" +
        "No one purifies another. \n" +
        "No other purifies one.")
        
    # Excerpt from Attavagga: Self, www.accesstoinsight.org

    wf = word_freq(txt)
    print('Count:')
    print(wf)
