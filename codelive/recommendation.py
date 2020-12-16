def main():
    print("Welcome to the CSC110 Book Recommender. Type the word in the left column to do the action on the right. ")
    print("recommend: recommend books for a paricular user")
    print("averages : output the average ratings of all books in the system ")
    print("quit     : exit the program")
    print("next task?")
    load_file()
def load_file():
    data={''}
    ratings_file= open("ratings.txt", "r")
    ratings_small_file= open("ratings-small.txt", "r")
    read_rating= ratings_file.readlines()
    read_rating_small= ratings_small_file.readlines()

    for i in range(1, len(read_rating_small)-1):
        return(read_rating_small[i])
        i+=3




main()






