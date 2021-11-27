#  FEUP - Master in Data Science and Engineering
#  Ana Catarina Mesquita
#  Filipe Dória
#  Guilherme Salles

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import webbrowser

#Load ./datasets
df_country = pd.read_csv('./datasets/countries_of_the_world.csv')
df2015 = pd.read_csv('./datasets/yearly/wh-2015.csv')
df2016 = pd.read_csv('./datasets/yearly/wh-2016.csv')
df2017 = pd.read_csv('./datasets/yearly/wh-2017.csv')
df2018 = pd.read_csv('./datasets/yearly/wh-2018.csv')
df2019 = pd.read_csv('./datasets/yearly/wh-2019.csv')


#Standartize columns
df2015.columns = ['country', 'region', 'happiness_rank', 'happiness_score', 'standart_error', 'economy', 'family',
                  'health', 'freedom', 'trust_perp_corruption', 'generosity', 'dystopia_residual']
df2016.columns = ['country', 'region', 'happiness_rank', 'happiness_score', 'low_ci', 'upper_ci', 'economy', 'family',
                  'health', 'freedom', 'trust_perp_corruption', 'generosity', 'dystopia_residual']
df2017.columns = ['country', 'happiness_rank', 'happiness_score', 'whisker_hi', 'whisker_lo', 'economy', 'family',
                  'health', 'freedom', 'generosity', 'trust_perp_corruption', 'dystopia_residual']
df2018.columns = ['happiness_rank', 'country', 'happiness_score', 'economy', 'social_support',
                  'health', 'freedom', 'generosity', 'trust_perp_corruption']
df2019.columns = ['happiness_rank', 'country', 'happiness_score', 'economy', 'social_support',
                  'health', 'freedom', 'generosity', 'trust_perp_corruption']

#regression graph
sns.regplot(x='trust_perp_corruption',y ='happiness_score', data=df2019)
plt.savefig('./outputs/output-image5.png')

#Histogram for Happiness Index
f, (ax1) = plt.subplots(1, 1, figsize=(7, 5), sharex=True)

happy_2019= df2019['happiness_score']
happy_2019.hist(density=False, histtype='stepfilled', bins=16)
ax1.set_ylabel("Counts")
ax1.set_title("Happiness Index distribution on 2019")

plt.savefig('./outputs/output-image.png')



#Plot grph of top 5 hapiness country in 2019
df10_h= df2019.nlargest(10, 'happiness_score')

f, (ax1) = plt.subplots(1, 1, figsize=(7, 5), sharex=True)

x = df10_h['happiness_score']
y1 = df10_h['country']
plot1=sns.barplot(x=x, y=y1, ax=ax1) #palette
ax1.set_ylabel("Countries")
ax1.set_title("Top 10 Countries with highest happiness index on 2019")
plt.savefig('./outputs/output-image1.png')


#Generate data for the next graphs
portugal15 = df2015[df2015['country']=="Portugal"]
portugal16 = df2016[df2016['country']=="Portugal"]
portugal17 = df2017[df2017['country']=="Portugal"]
portugal18 = df2018[df2018['country']=="Portugal"]
portugal19 = df2019[df2019['country']=="Portugal"]

p_h_15= float(portugal15['happiness_score'])
p_h_16= float(portugal16['happiness_score'])
p_h_17= float(portugal17['happiness_score'])
p_h_18= float(portugal18['happiness_score'])
p_h_19= float(portugal19['happiness_score'])

avg_h_15= df2015['happiness_score'].mean()
avg_h_16= df2016['happiness_score'].mean()
avg_h_17= df2017['happiness_score'].mean()
avg_h_18= df2018['happiness_score'].mean()
avg_h_19= df2019['happiness_score'].mean()

p_c_15= float(portugal15['trust_perp_corruption'])
p_c_16= float(portugal16['trust_perp_corruption'])
p_c_17= float(portugal17['trust_perp_corruption'])
p_c_18= float(portugal18['trust_perp_corruption'])
p_c_19= float(portugal19['trust_perp_corruption'])

avg_c_15= df2015['trust_perp_corruption'].mean()
avg_c_16= df2016['trust_perp_corruption'].mean()
avg_c_17= df2017['trust_perp_corruption'].mean()
avg_c_18= df2018['trust_perp_corruption'].mean()
avg_c_19= df2019['trust_perp_corruption'].mean()


#Graph for compare POrtugal and average of other countries
data = {'happiness index':  [avg_h_15,avg_h_16,avg_h_17,avg_h_18,avg_h_19,p_h_15,p_h_16,p_h_17,p_h_18,p_h_19],
        'type':['global avg','global avg','global avg','global avg','global avg','Portugal','Portugal','Portugal','Portugal','Portugal'],
        'year': [2015,2016,2017,2018,2019,2015,2016,2017,2018,2019]}
df_avg_happiness = pd.DataFrame(data)

f, (ax1) = plt.subplots(1, 1, figsize=(7, 5), sharex=True)
sns.lineplot(data=df_avg_happiness, x="year", y="happiness index",hue="type", linewidth=3.5)
ax1.set_title("Comparison of Happiness index of Global avg and Portugal over 2015-2019")
ax1.set(ylim=(5, 6))

plt.savefig('./outputs/output-image2.png')


#Graph for list top 10 countries with high corruption
df10= df2019.nlargest(10, 'trust_perp_corruption')
f, (ax1) = plt.subplots(1, 1, figsize=(7, 5), sharex=True)
x = df10['trust_perp_corruption']
y1 = df10['country']
plot1=sns.barplot(x=x, y=y1, palette="rocket", ax=ax1)
ax1.set_ylabel("Countries")
ax1.set_title("Top 10 Countries with highest Perception of corruption on 2019")

plt.savefig('./outputs/output-image3.png')


#Graph for compare Portugal and other countries on corruption perception
data2 = {'corruption index':  [avg_c_15,avg_c_16,avg_c_17,avg_c_18,avg_c_19,p_c_15,p_c_16,p_c_17,p_c_18,p_c_19],
        'type':['global avg','global avg','global avg','global avg','global avg','Portugal','Portugal','Portugal','Portugal','Portugal'],
        'year': [2015,2016,2017,2018,2019,2015,2016,2017,2018,2019]}
df_avg_corruption = pd.DataFrame(data2)

f, (ax1) = plt.subplots(1, 1, figsize=(7, 5), sharex=True)
sns.lineplot(data=df_avg_corruption, x="year", y="corruption index",hue="type", linewidth=3.5)
ax1.set_title("Comparison of Global avg and Portugal on Corruption perception over 2015-2019")
ax1.set(ylim=(0.00, 0.4))
plt.savefig('./outputs/output-image4.png')






page_title_text='Happiness Report'
title_text = 'Happiness Report'

text_section1 = f"Section 1: Happiness index"
text_dev='Developed by Ana Mesquita, Filipe Doria and Guilherme Salles'
text = f"Hello , Welcome to our quick report!"
text_h_hist= 'First let check how the happiness index is distributed around the countries over 2019'
text_h_top10 = 'Below you can see the top 10 countries with high happiness index on the year 2019.'
text_portugal = f"On the chart above, we can see the happiness index of Portugal in comparison with the global average over the years."


text_section2 = 'Section 2: Corruption perception'
text_c_top10 = f"On the chart below we can see the top 10 countries with highest perception of corruption on 2019."
text_c_portugal = f"On the chart above, we can see the perception of corruption of Portugal in comparison with the global average over the years."
text_regression = 'On the chart above we have the data distribution and line showing a linear relation ship between happines and corruption perecption on 2019.'
text_conclusion= 'So, it appear to not have a linear relationshion between the happiness index and the perception of corruption.'
# 2. Combine them together using a long f-string
html = f'''
    <html>
        <head>

        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css">
        <style>body{'background:whitesmoke;'}</style>
        <title>{page_title_text}</title>
        </head>

        <body>
            <h1>{title_text}</h1>
            <p>{text_dev}</p>
            <h2>{text_section1}</h2> 
            <p>{text}</p>
            <p>{text_h_hist}</p>
            <img src='output-image.png' width="700" class="center">
            <p>{text_h_top10}</p>
            <img src='output-image1.png' width="700" class="center">
            {df10_h.to_html()}
            <img src='output-image2.png' width="700" class="center">
            <p>{text_portugal}</p>
            <h2>{text_section2}</h2>
            <p>{text_c_top10}<br>
            <img src='output-image3.png' width="700" class="center"><br>
            <img src='output-image4.png' width="700" class="center">
            <p>{text_c_portugal}<br>
            <img src='output-image5.png' width="700" class="center"><br>
            <p>{text_regression}
            <p>{text_conclusion}
        </body>
    </html>
    '''

#opens a html file to save the previous output
with open(f"./outputs/output_report_extra.html", 'w') as f:
    f.write(html)

#opens the just created html report directly on the users browser
webbrowser.open(f"./outputs/output_report_extra.html")