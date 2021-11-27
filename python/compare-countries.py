import pandas as pd
import csv

## Funtion for compare similar words on list
# it compare words between two lists, and identify the words that are presented on list1, but it isn't found on list2.

def compare_list(wordlist1,wordlist2):
    elements_matched=[]
    elements_notfound = []

    for i in range(len(wordlist1)):
        word_found=1

        for j in range(len(wordlist2)):
            word1_i= wordlist1[i]
            word2_j= wordlist2[j]

            sorted_word1_i = ''.join(sorted(word1_i)).strip()
            sorted_word2_j = ''.join(sorted(word2_j)).strip()

            if sorted_word1_i == sorted_word2_j:
                elements_matched.append(wordlist1[i])
                word_found=1     #Found same word
                break
            else:
                word_found=0

        if word_found == 0: # If after the loop is don't find a match, it store in a different list
            elements_notfound.append(wordlist1[i])

    return(elements_notfound)

#Load all dataset
df = pd.read_csv('./datasets/countries_of_the_world.csv')

df2015 = pd.read_csv('././datasets/yearly/wh-2015.csv')
df2016 = pd.read_csv('./datasets/yearly/wh-2016.csv')
df2017 = pd.read_csv('./datasets/yearly/wh-2017.csv')
df2018 = pd.read_csv('./datasets/yearly/wh-2018.csv')
df2019 = pd.read_csv('./datasets/yearly/wh-2019.csv')

#Get the Countries names from dataset
country_world_list= df['Country'].unique()
countries_happy_list_2015 = df2016['Country'].unique()
countries_happy_list_2016 = df2017['Country'].unique()
countries_happy_list_2017 = df2017['Country'].unique()
countries_happy_list_2018 = df2018['Country or region'].unique()
countries_happy_list_2019 = df2019['Country or region'].unique()

#combine all Country name per year in a list
happines_list_year = [countries_happy_list_2015,countries_happy_list_2016,countries_happy_list_2017,countries_happy_list_2018,countries_happy_list_2019]
year=2015

#Uses the function compare_list to generate an output report of not matching contries
# per year on the Happiness country dataset.
with open('compare-countries-output.txt', 'w',encoding='utf-8') as f:
    year=2015
    #writer = csv.writer(f)
    for list_year in happines_list_year:
        notfoundcountries = compare_list(list_year,country_world_list)
        print(f"Countries to be removed or corrected on year {year}:")
        f.write(f"Countries to be removed or corrected on year {year}:\n")
        for item in notfoundcountries:
            print(f"{item} ")
            f.write(f"{item} \n")
        print(f"{len(notfoundcountries)} total countries")
        f.write(f"{len(notfoundcountries)} total countries\n")
        print(f"_________________________________________________________")
        f.write(f"_________________________________________________________\n")
        year=year+1
