import urllib

def read_text():
    quotes = open("/Users/Ken/Desktop/Udacity_Programming_Python/Exercise/Ex4/Ex4_movie_quotes.txt")
    contents_of_files = quotes.read()
    print contents_of_files
    quotes.close()
    check_profanity(contents_of_files)
    
def check_profanity(text):
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q=+text")
    output = connection.read()
    print output
    connection.close()


read_text()



