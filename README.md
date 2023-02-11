# AffinityAnswers-Task
A python program that indicates the degree of profanity for every sentence stored in a text file.


# Assumptions


1. The slurs are categorised into 5 profanity levels (1 being the least and 5 being the most inappropriate).
2. Some words such as 'bad', 'slur', 'profain', 'hate', etc. have been assummed to be slurs.
3. The text file stores the user name and the tweet in each line (eg. UserName: Tweet)


The program consists of two functions, tweet_prepare and prof_deg.


# The tweet_prepare function


This function takes a line as the parameter and returns a tuple of user name and the tweet.


The following actions are performed on the line:
  1. White spaces are stripped off at both the ends.
  2. Dots(.) are removed(if any).
  3. Everything is converted to lower case
  4. The line is split from the colon(:) giving 2 strings:
    i.  First string contains the user name.
    ii. Second string contains the Tweet which is furter split into single words.


# The prof_deg function


The prof_deg function takes two parameters:
  1. The Tweet
  2. A dictionary containing profanity levels as keys and a list of racial slurs as values.
  
  
Following are the actions performed:
  1. A variable, prof_deg stores the degree of profanity for the sentence(initialized to 0).
  2. For each word the slur words are matched at each profanity level from 1 to 5.
  3. When a match is found, prof_deg is updated if profanity level is greater than prof_deg.


The function returns the variable prof_deg.


# Snapshots


![image](https://user-images.githubusercontent.com/69196090/218255552-a46cc030-8e51-4126-a06f-5f4ea9bd0e16.png)


![image](https://user-images.githubusercontent.com/69196090/218255571-c54ff5cb-cc60-4f88-a7a3-f49dd0ab2e68.png)
