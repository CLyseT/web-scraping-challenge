
#Dependencies

from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager


def scrape():

    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    
    info = {}

    jpl_url = 'https://spaceimages-mars.com'
    browser.visit(jpl_url)


    filepath = os.path.join("Resources", "mission_to_mars.html")
    with open(filepath) as file:
        html = file.read()

    soup = BeautifulSoup(html, 'html.parser')
    info.result = soup.body.find_all('section', class_ = 'image_and_description_container')
    
    for data in result:
        info.lastest_title = data.find('div', class_='content_title').text
        info.latest_p = data.find('div', class_='article_teaser_body').text

        mars_table_url = 'https://galaxyfacts-mars.com'

    info.table = pd.read_html(mars_table_url)
    info.table_df = table[0]
    info.html_table = table_df.to_html()

    info.Mars_URLs = [{'Title':'Cerberus Hemisphere Enhanced','Image_URL':'https://marshemispheres.com/images/cerberus_enhanced.tif'},
    {'Title':'Schiaparelli Hemisphere Enhanced', 'Image_URL':'https://marshemispheres.com/images/schiaparelli_enhanced.tif'},
    {'Title':'Syrtis Major Hemisphere Enhanced', 'Image_URL': 'https://marshemispheres.com/images/syrtis_major_enhanced.tif'},
    {'Title':'Valles Marineris Hemisphere Enhanced', 'Image_URL':'https://marshemispheres.com/images/valles_marineris_enhanced.tif'}]

    browser.quit()

    return info







