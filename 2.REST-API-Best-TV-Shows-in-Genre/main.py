#Must import the requests lib to work with HTTP GET responses.
#Some options on how it can be downloaded:
#Windows: pip3 install requests
#Linux: sudo pip3 install requests
#pip3 is used if python3 is installed and pip when Python2 is installed.
import sys
import requests

###########INPUT##############
genre_desired = "Drama"
##############################


url = "https://jsonmock.hackerrank.com/api/tvseries"
page_parameter = "?page="

def bestInGenre(genre):
    current_page = 1
    best_show_in_genre = None
    best_show_name_list = []

    while True:
        url_with_current_page_number = url + page_parameter + str(current_page)

        get_response = requests.get(url_with_current_page_number)
        json_response = get_response.json()
        #Checking the parameter to check if it is the one that is related to the movies data
        #print(json_response["data"])
        movies_data = json_response["data"]

        for movie in movies_data:
            movie_genre_list = movie['genre'].split(', ')
            for movie_genre in movie_genre_list:
                if movie_genre.lower() == genre.lower():
                    if (best_show_in_genre == None or best_show_in_genre["imdb_rating"] < movie["imdb_rating"]):
                        best_show_in_genre = movie
                        best_show_name_list = []
                        best_show_name_list.append(best_show_in_genre)
                    elif(best_show_in_genre["imdb_rating"] == movie["imdb_rating"]):
                        best_show_name_list.append(best_show_in_genre)
        if current_page < int(json_response['total_pages']):
            current_page += 1
        else:
            break
    if len(best_show_name_list) > 1:
        best_show_name_list.sort()

    best_show = best_show_name_list[0]

    return best_show




if __name__ == '__main__':

    best_show = bestInGenre(genre_desired)
    print(best_show["name"])

