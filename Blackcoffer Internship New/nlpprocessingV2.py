import nltk
import string
import textstat
import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
nltk.download('averaged_perceptron_tagger')
nltk.download('vader_lexicon')
nltk.download('punkt')
nltk.download('stopwords')

def syllables(word):
    return textstat.syllable_count(word)

def write_text_without_blackcoffer(file_path):
    try:
        # Read the content of the file
        with open(file_path, 'r') as file:
            content = file.read()

        # Find the starting index of "Blackcoffer"
        index_blackcoffer = content.rfind('Blackcoffer')

        # Remove text starting from "Blackcoffer" until the end
        modified_content = content[:index_blackcoffer]

        # Write the modified content back to the file
        with open(file_path, 'w') as file:
            file.write(modified_content)

        return modified_content

    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

def remove_punc(text):
    exclude = string.punctuation
    return text.translate(str.maketrans("","",exclude))



data = pd.read_excel("C:\\Users\\Asfaan Hussain\\Desktop\\INTERNSHALA\\Blackcoffer Internship New\\Output Data Structure.xlsx")
url = data.URL.to_list()
url_id = data.URL_ID.to_list()
url_id = [int(x) if x%int(x) == 0 else x for x in url_id]
df = pd.DataFrame()




for i, j in zip(url_id, url):

    filename = "C:\\Users\\Asfaan Hussain\\Desktop\\INTERNSHALA\\Blackcoffer Internship New\\TextFiles\\{}.txt".format(i)
    with open(filename, "r", encoding="utf-8") as file:
        inputtext = write_text_without_blackcoffer(filename)
        remove_punc(inputtext)
        lines = file.read()
        text = "".join(lines)

    #Removing tags and Source
    lines = text.splitlines()
    new_text = "\n".join(lines)
    print(new_text)

    try:
        # Tokenizing the text into sentences
        sentences = sent_tokenize(text)

        # Tokenizing the text into words
        words = word_tokenize(text)

        # Removing stop words
        filtered_words = [word for word in words if word.lower() not in stopwords.words('english')]

        # Calculating the average sentence length
        avg_sentence_length = sum(len(sent) for sent in sentences) / len(sentences)

        # Calculating the percentage of complex words
        complex_words = [word for word in filtered_words if (syllables(word)) >= 2]
        percentage_complex_words = len(complex_words) / len(filtered_words)

        # Calculating the FOG index
        fog_index = 0.4 * (avg_sentence_length + percentage_complex_words)

        # Calculating the average number of words per sentence
        avg_words_per_sentence = len(words) / len(sentences)

        # Calculating the complex word count
        complex_word_count = len(complex_words)

        # Calculating the word count
        word_count = len(words)

        # Calculating the average syllables per word
        avg_syllables_per_word = sum(syllables(word) for word in words) / len(words)

        #Calculating the average word length
        avg_word_length = sum(len(word) for word in words) / len(words)

        # Calculating personal pronouns
        personal_pronouns = ['i', 'me', 'you', 'he', 'him', 'she', 'her', 'it', 'we', 'us', 'they', 'them']
        personal_pronoun_count = sum(word.lower() in personal_pronouns for word in words)

        # Sentiment Analysis
        sia = SentimentIntensityAnalyzer()

        positive_score = 0
        negative_score = 0
        polarity_score = 0
        subjectivity_score = 0

        for sentence in sentences:
            sentiment = sia.polarity_scores(sentence)
            positive_score += sentiment['pos']
            negative_score += sentiment['neg']
            polarity_score += sentiment['compound']
            subjectivity_score += sentiment['compound']

    except Exception:
        avg_sentence_length = 0
        percentage_complex_words = 0
        fog_index = 0
        avg_words_per_sentence = 0
        complex_word_count = 0
        word_count = 0
        avg_syllables_per_word = 0
        avg_word_length = 0
        personal_pronoun_count = 0
        positive_score = 0
        negative_score = 0
        polarity_score = 0
        subjectivity_score = 0

    # Create a new row as a DataFrame
    new_row = pd.DataFrame(
        {"URL_ID": i,
         "URL": j,
         "Positive Score": round(positive_score, 2),
         "Negative Score": round(negative_score, 2),
         "Polarity Score": round(polarity_score, 2),
         "Subjectivity Score": round(subjectivity_score, 2),
         "Avg Sentence Length": round(avg_sentence_length, 2),
         "Percentage of Complex Words": round(percentage_complex_words, 2),
         "Fog Index": round(fog_index, 2),
         "Avg Number of Words per Sentence": round(avg_words_per_sentence, 2),
         "Complex Word Count": round(complex_word_count, 2),
         "Word Count": round(word_count, 2),
         "Avg Syllables per Word": round(avg_syllables_per_word, 2),
         "Personal Pronouns": round(personal_pronoun_count, 2),
         "avg_word_length": round(avg_word_length, 2)
         }, index=[0])

    # Concatenate the new row to the existing DataFrame
    df = pd.concat([df, new_row])

    print("Positive Score: ", round(positive_score, 2), end='\n')
    print("Negative Score: ", round(negative_score, 2), end='\n')
    print("Polarity Score: ", round(polarity_score, 2), end='\n')
    print("Subjectivity Score: ", round(subjectivity_score, 2), end='\n')
    print("Avg Sentence Length: ", round(avg_sentence_length, 2), end='\n')
    print("Percentage of Complex Words: ", round(percentage_complex_words, 2), end='\n')
    print("Fog Index: ", round(fog_index, 2), end='\n')
    print("Avg Number of Words per Sentence: ", round(avg_words_per_sentence, 2), end='\n')
    print("Complex Word Count: ", round(complex_word_count, 2), end='\n')
    print("Word Count: ", round(word_count, 2), end='\n')
    print("Avg Syllables per Word: ", round(avg_syllables_per_word, 2), end='\n')
    print("Personal Pronouns: ", round(personal_pronoun_count, 2), end='\n')
    print("Avg word length: ", round(avg_word_length, 2), end='\n')
    print("\n\n")



df.to_excel('OutputdataInternship.xlsx', index=False)