# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
''''
document.getElementsByClassName('lister-item-header')[0].getElementsByTagName('a')[0].innerText  # title
document.getElementsByClassName('lister-item-header')[0].getElementsByTagName('span')[0].innerText.slice(0, -1)  # rank
document.getElementsByClassName('lister-item-header')[0].getElementsByTagName('span')[1].innerText.slice(1, -1)  # year
document.getElementsByClassName('runtime')[0].innerText.slice(0, -4)  # movie duration
document.getElementsByClassName('genre')[0].innerText
document.getElementsByClassName('inline-block ratings-imdb-rating')[0].innerText  # rating
document.getElementsByTagName('p')[2].getElementsByTagName('a')[4].innerText  # director&stars p=2
document.getElementsByTagName('p')[3].getElementsByTagName("span")[1].innerText  # votes p=3
document.getElementsByTagName('p')[3].getElementsByTagName("span")[4].innerText.slice(1, -1)  # gross
'''''
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import pandas as pd
import scrape

option = webdriver.ChromeOptions()
option.add_argument('headless')
driver = webdriver.Chrome(options=option)


def scrape_imdb(movie_id, p_element, driver):
    title.append(scrape.title(movie_id, driver))
    rank.append(scrape.rank(movie_id, driver))
    year.append(scrape.year(movie_id, driver))
    duration.append(scrape.duration(movie_id, driver))
    gener.append(scrape.gener(movie_id, driver))
    rating.append(scrape.rating(movie_id, driver))
    director.append(scrape.director(p_element, driver))
    star1.append(scrape.star1(p_element, driver))
    star2.append(scrape.star2(p_element, driver))
    star3.append(scrape.star3(p_element, driver))
    star4.append(scrape.star4(p_element, driver))
    p_element += 1
    votes.append(scrape.votes(p_element, driver))
    gross.append(scrape.gross(p_element, driver))


def excel(title,rank,year,duration,gener,rating,director,star1,star2,star3,star4,votes,gross):
    df = pd.DataFrame(
        {"Title": pd.Series(title), "Rank": pd.Series(rank), "Year": pd.Series(year),
         "Duration": pd.Series(duration), "Gener": pd.Series(gener), "Rating": pd.Series(rating),
         "Director": pd.Series(director), "Star1": pd.Series(star1), "Star2": pd.Series(star2),
         "Star3": pd.Series(star3), "Star4": pd.Series(star4), "Votes": pd.Series(votes),
         "Gross": pd.Series(gross)})
    df.to_csv("movies.csv", mode='w', index=False)

title = list()
rank = list()
year = list()
duration = list()
gener = list()
rating = list()
director = list()
star1 = list()
star2 = list()
star3 = list()
star4 = list()
votes = list()
gross = list()
movie_without_all_data = list()
movie_without_all_data_sum = 0


movies_year = 1950
while movies_year <= 2021:
    half = 0
    other_half = 49
    movie_id = 0
    p_element = 2
    driver.get("https://www.imdb.com/search/title/?year={}&title_type=feature&".format(movies_year))
    while half <= 49:
        time.sleep(3)
        scrape_imdb(movie_id, p_element, driver)
        excel(title, rank, year, duration, gener, rating, director, star1, star2, star3, star4, votes, gross)
        print("half: {}".format(half))
        print("other_half: {}".format(other_half))
        print("title: {}".format(title))
        print("rank: {}".format(rank))
        print("year: {}".format(year))
        print("duration: {}".format(duration))
        print("gener: {}".format(gener))
        print("rating: {}".format(rating))
        print("director: {}".format(director))
        print("star1: {}".format(star1))
        print("star2: {}".format(star2))
        print("star3: {}".format(star3))
        print("star4: {}".format(star4))
        print("votes: {}".format(votes))
        print("gross: {}".format(gross))
        print(movies_year)
        movie_id += 1
        p_element += 4
        half += 1
    half = 0
    movie_id = 0
    p_element = 2
    driver.get("https://www.imdb.com/search/title/?title_type=feature&year"
               "={}-01-01,{}-12-31&start=51&ref_=adv_nxt".format(movies_year,movies_year))
    while other_half <= 99:
        scrape_imdb(movie_id, p_element, driver)
        movie_id += 1
        p_element += 4
        other_half += 1
        excel(title, rank, year, duration, gener, rating, director, star1, star2, star3, star4, votes, gross)
        print("half: {}".format(half))
        print("other_half: {}".format(other_half))
        print("title: {}".format(title))
        print("rank: {}".format(rank))
        print("year: {}".format(year))
        print("duration: {}".format(duration))
        print("gener: {}".format(gener))
        print("rating: {}".format(rating))
        print("director: {}".format(director))
        print("star1: {}" .format(star1))
        print("star2: {}".format(star2))
        print("star3: {}".format(star3))
        print("star4: {}".format(star4))
        print("votes: {}".format(votes))
        print("gross: {}".format(gross))
        print(movies_year)
    movies_year +=1
