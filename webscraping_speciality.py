
# installing & importing libraries
# !pip install requests
# !pip install beautifulsoup4
import requests
from bs4 import BeautifulSoup
import pandas as pd

# creating placeholders for data
titles = []
doctor_names = []
address = []
# price = []
urls = []

for i in range(1,100):
    # Generating a request for vezeeta.com
    url = f'https://www.vezeeta.com/ar/%D8%AF%D9%83%D8%AA%D9%88%D8%B1/%D8%B9%D8%B8%D8%A7%D9%85/%D9%85%D8%B5%D8%B1?page={i}'
    response = requests.get(url)
    # print(response.text)

    # Getting HTML code
    html = response.text

    # Let's parse this HTML code
    soup = BeautifulSoup(html, 'html.parser')

    # Doctor titles
    for i in range(10):
        titles.append(soup.find_all('span',
                                    {'class':'DoctorCardSubComponentsstyle__Text-sc-1vq3h7c-14 DoctorCardSubComponentsstyle__TitleText-sc-1vq3h7c-16 gqVrId hEuQjC'})[i].text)
    # print(titles)

    # Doctor names
    for i in range(10):
        doctor_names.append(soup.find_all('h4',
                                    {'class':'DoctorCardSubComponentsstyle__Text-sc-1vq3h7c-14 DoctorCardSubComponentsstyle__DoctorNameText-sc-1vq3h7c-15 gqVrId Wpycp'})[i].text)
    # print(doctor_names)

    # Doctor address
    for i in range(10):
        address.append(soup.find_all('span',
                                    {'class':'DoctorCardstyle__Text-sc-uptab2-4 blwPZf'})[i].text)
    # print(address)

    # # Doctor price
    # for i in range(10):
    #     price.append(soup.find_all('span',
    #                                 {'itemprop':'priceRange'})[i].text)
    # # print(price)

    # Doctor url
    for link in soup.find_all('a', {'class':'CommonStylesstyle__TransparentA-sc-1vkcu2o-2 cTFrlk'}):
        urls.append(link.get('href'))

# creating our dataframe
df = pd.DataFrame({'Title': titles,
                   'Doctor Name': doctor_names,
                   'Address': address,
                   'URL': urls})

df.to_csv('final_doctors.csv')

print('Well Done!')