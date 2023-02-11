def prof_deg(tweet, racial_slurs):
    # Degree of profanity is initialized to 0.
    prof_deg = 0
    # Looping through each word in the tweet.
    # And checking for each profanity degree,
    # If the word exists in the list associated to that degree,
    # The variable prof_deg is incremented by that degree.
    for word in tweet:
        for degree in racial_slurs:
            if word in racial_slurs[degree]:
                if degree > prof_deg:
                    prof_deg = degree
    return prof_deg

def tweet_prepare(line):
    # Preparing each tweet to uniformalize as per the requirement.
    line = line.strip().replace('.', '').lower().split(':')
    user_name = line[0]
    # The tweet is broken down to single words and stored in a list.
    tweet = line[1].split(' ')
    return (user_name, tweet)

if __name__ == "__main__":
    # Opening the file containg the tweets.
    file_name = input("Enter the path/to/your/file: ")
    file = open(file_name, "r")
    
    # Racial Slurs stored in a dictionary along with their degree of profanity.
    racial_slurs = {1: ['bad'], 2: ['slur', 'slurs'], 3: ['hate', 'hateful'], 5: ['profanity']}

    for line in file:
        user_name, tweet = tweet_prepare(line)
        profanity = prof_deg(tweet, racial_slurs)
        print(f'{user_name} : {profanity} degree of profanity.')