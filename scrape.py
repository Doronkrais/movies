from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import pandas as pd

option = webdriver.ChromeOptions()
option.add_argument('headless')
driver = webdriver.Chrome(options=option)


def title(movie_id, driver):
    try:
        titletemp = driver.execute_script(
            "return document.getElementsByClassName('lister-item-header')[{}]"
            ".getElementsByTagName('a')[0].innerText;".format(movie_id))
    except:
        print("title not found")
        titletemp = None
    return titletemp


def rank(movie_id, driver):
    try:
        ranktemp = driver.execute_script(
            "return document.getElementsByClassName('lister-item-header')[{}].getElementsByTagName('span')["
            "0].innerText.slice(0,-1);".format(movie_id))
    except:
        print("rank no found")
        ranktemp = None
    return ranktemp


def year(movie_id, driver):
    try:
        yeartemp = driver.execute_script(
            "return document.getElementsByClassName('lister-item-header')[{}].getElementsByTagName('span')["
            "1].innerText.slice(1,-1);".format(movie_id))
    except:
        print("year not found")
        yeartemp = None
    return yeartemp


def duration(movie_id, driver):
    try:
        durationtemp = driver.execute_script(
            "return document.getElementsByClassName('runtime')[{}].innerText.slice(0,-4);".format(movie_id))
    except:
        ("duration not found")
        durationtemp = None
    return durationtemp


def gener(movie_id, driver):
    try:
        genertemp = driver.execute_script(
            "return document.getElementsByClassName('genre')[{}].innerText;".format(movie_id))
        genertemp = genertemp.split(',')[0]
    except:
        print("gener not found")
        genertemp = None
    return genertemp


def rating(movie_id, driver):
    try:
        ratingtemp = driver.execute_script(
            "return document.getElementsByClassName"
            "('inline-block ratings-imdb-rating')[{}].innerText;".format(movie_id))
    except:
        print("rating not found")
        ratingtemp = None
    return ratingtemp


def director(p_element, driver):
    try:
        directortemp = driver.execute_script(
            "return document.getElementsByTagName('p')[{}]"
            ".getElementsByTagName('a')[0].innerText;".format(p_element))
    except:
        print("director not found")
        directortemp = None
    return directortemp


def star1(p_element, driver):
    try:
        star1temp = driver.execute_script(
            "return document.getElementsByTagName('p')[{}]"
            ".getElementsByTagName('a')[1].innerText;".format(p_element))
    except:
        print("star1 not found")
        star1temp = None
    return star1temp


def star2(p_element, driver):
    try:
        star2temp = driver.execute_script(
            "return document.getElementsByTagName('p')[{}]"
            ".getElementsByTagName('a')[2].innerText;".format(p_element))
    except:
        print("star2 not found")
        star2temp = None
    return star2temp


def star3(p_element, driver):
    try:
        star3temp = driver.execute_script(
            "return document.getElementsByTagName('p')[{}]"
            ".getElementsByTagName('a')[3].innerText;".format(p_element))
    except:
        print("star3 not found")
        star3temp = None
    return star3temp


def star4(p_element, driver):
    try:
        star4temp = driver.execute_script(
            "return document.getElementsByTagName('p')[{}]"
            ".getElementsByTagName('a')[4].innerText;".format(p_element))
    except:
        print("star4 not found")
        star4temp = None
    return star4temp


def votes(p_element, driver):
    try:
        votestemp = driver.execute_script(
            "return document.getElementsByTagName('p')[{}]"
            ".getElementsByTagName('span')[1].innerText;".format(p_element))
    except:
        print("votes not found")
        votestemp = None
    return votestemp


def gross(p_element, driver):
    try:
        grosstemp = driver.execute_script(
            "return document.getElementsByTagName('p')[{}]"
            ".getElementsByTagName('span')[4].innerText.slice(1,-1);".format(p_element))
    except:
        print("gross not found")
        grosstemp = None
    return grosstemp
