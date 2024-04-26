from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from settings import LINKEDIN_ACCEESS_TOKEN, LINKEDIN_ACCEESS_TOKEN_EXP, HEADLESS

# Setting up the options
options = Options()
if not HEADLESS=="False":
    options.add_argument("--headless=new")
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors=yes')
options.add_argument("--log-level=3")

# Setting up service
service = Service(ChromeDriverManager().install(), log_output='nul')

def find_by_xpath_or_None(driver, *xpaths):
    """returns the text inside and elemnt by its xPath"""
    for xpath in xpaths:
        try:
            return driver.find_element(By.XPATH, xpath).text
        except NoSuchElementException:
            #print(f"Element not found : {xpath}")
            continue
    return None


def search_for_candidate_name(driver):
    """search for profile's name in the page"""
    try:
        name = find_by_xpath_or_None(driver, '/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[2]/div[1]/div[1]/span/a/h1','/html/body/div[4]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[2]/div[1]/div[1]/span/a/h1')
        return name
    except Exception as e:
        print(f"Error finding name: {e}")
    return None


def search_for_candidate_headline(driver):
    """search for profile's headline in the page"""
    try:
        headline = find_by_xpath_or_None(driver, '/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[2]/div[1]/div[2]','/html/body/div[4]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[2]/div[1]/div[2]')
        return headline
    except Exception as e:
        print(f"Error finding headline: {e}")
    return None


def search_for_section(driver,section_name,min_index=2,max_index=8) :
    """search for a section's content by section name in the page"""
    try:
        # Initialize variables
        sectionIndex = min_index
        found_elements = {
            'positions': [],
            'institutions': [],
            'dates': []
        }

        # Function to add found elements to the dictionary
        def add_elements(position, institution, date):
            if position: found_elements['positions'].append(position)
            if institution: found_elements['institutions'].append(institution)
            if date: found_elements['dates'].append(date)

        # Loop through sections until "section_title" section is found
        while sectionIndex <= max_index :
            # Check if the section title matches "section_name"
            section_title = find_by_xpath_or_None(driver, f'/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[{sectionIndex}]/div[2]/div/div/div/h2/span[1]')
            if section_title == section_name:
                # Experience
                elementIndex = 1
                if section_name == "Experience" :
                    while True:
                        target_element_position = find_by_xpath_or_None(driver, f'/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[{sectionIndex}]/div[3]/ul/li[{elementIndex}]/div/div[2]/div[1]/div/div/div/div/div/span[1]',f'/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[{sectionIndex}]/div[3]/ul/li[{elementIndex}]/div/div[2]/div[2]/ul/li[1]/div/div[2]/div/a/div/div/div/div/span[1]',f'/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[{sectionIndex}]/div[3]/ul/li[{elementIndex}]/div/div[2]/div[2]/ul/li[1]/div/div[2]/div/a/div/div/div/div/div/span[1]',f'/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[{sectionIndex}]/div[3]/ul/li[{elementIndex}]/div/div[2]/div/div/span[1]/span[1]')
                        target_element_institution = find_by_xpath_or_None(driver, f'/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[{sectionIndex}]/div[3]/ul/li[{elementIndex}]/div/div[2]/div[1]/div/span[1]/span[1]',f'/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[{sectionIndex}]/div[3]/ul/li[{elementIndex}]/div/div[2]/div[1]/a/div/div/div/div/span[1]',f'/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[{sectionIndex}]/div[3]/ul/li[{elementIndex}]/div/div[2]/div[1]/a/div/div/div/div/span[1]')
                        target_element_date = find_by_xpath_or_None(driver, f'/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[{sectionIndex}]/div[3]/ul/li[{elementIndex}]/div/div[2]/div[1]/div/span[2]/span[1]',f'/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[{sectionIndex}]/div[3]/ul/li[{elementIndex}]/div/div[2]/div[1]/a/span[1]/span[1]',f'/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[{sectionIndex}]/div[3]/ul/li[{elementIndex}]/div/div[2]/div/div/span[2]/span[1]')
                        if not target_element_position:
                            break

                        add_elements(target_element_position, target_element_institution, target_element_date)
                        elementIndex += 1
                # Education
                if section_name == "Education" :
                    while True:
                        target_element_position = find_by_xpath_or_None(driver, f'/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[{sectionIndex}]/div[3]/ul/li[{elementIndex}]/div/div[2]/div/a/span[1]/span[1]',f'/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[{sectionIndex}]/div[3]/ul/li[{elementIndex}]/div/div[2]/div/a/span[1]/span[1]')
                        target_element_institution = find_by_xpath_or_None(driver, f'/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[{sectionIndex}]/div[3]/ul/li[{elementIndex}]/div/div[2]/div/a/div/div/div/div/span[1]',f'/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[{sectionIndex}]/div[3]/ul/li[{elementIndex}]/div/div[2]/div/a/div/div/div/div/span[1]')
                        target_element_date = find_by_xpath_or_None(driver, f'/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[{sectionIndex}]/div[3]/ul/li[{elementIndex}]/div/div[2]/div/a/span[2]/span[1]',f'/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[{sectionIndex}]/div[3]/ul/li[{elementIndex}]/div/div[2]/div/a/span[2]/span[1]')

                        if not target_element_position:
                            break

                        add_elements(target_element_position, target_element_institution, target_element_date)
                        elementIndex += 1
                break
            sectionIndex += 1  # Move to the next section
        
        return found_elements
    except Exception as e:
        print(f"Error finding section :{e}")
        return None


def search_for_company_name(driver):
    """search for comapny's name in the page"""
    try:
        company_name = find_by_xpath_or_None(driver, '/html/body/div[5]/div[3]/div/div[2]/div/div[2]/main/div[1]/section/div/div[2]/div[2]/div[1]/div[2]/div/h1')
        return company_name
    except Exception as e:
        print(f"Error finding company name: {e}")
    return None


def search_for_company_industry(driver):
    """search for comapny's industry in the page"""
    try:
        company_industry = find_by_xpath_or_None(driver, '/html/body/div[4]/div[3]/div/div[2]/div/div[2]/main/div[1]/section/div/div[2]/div[2]/div[1]/div[2]/div/div/div[1]', '/html/body/div[5]/div[3]/div/div[2]/div/div[2]/main/div[1]/section/div/div[2]/div[2]/div[1]/div[2]/div/div/div[1]')
        return company_industry
    except Exception as e:
        print(f"Error finding company industry: {e}")
    return None


def search_for_company_about(driver):
    """search for comapny's name in the page"""
    try:
        more_button = driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div/div[2]/div/div[2]/main/div[2]/div/div[1]/section/div/div/div[1]/div/span[3]/span/a')
        more_button.click()
        company_about = find_by_xpath_or_None(driver, '/html/body/div[5]/div[3]/div/div[2]/div/div[2]/main/div[2]/div/div[1]/section/div/div/div[1]/div/span[1]')
        return company_about
    except Exception as e:
        print(f"Error finding company about: {e}")
    return None
    

def add_session_cookie(driver):
    """"load cookies from a file and add it to the driver"""

    cookie = {
        "domain": ".www.linkedin.com",
        "name": "li_at",
        "value": LINKEDIN_ACCEESS_TOKEN,
        "path": "/",
        "secure": True,
        "httpOnly": True,
        "expirationDate":LINKEDIN_ACCEESS_TOKEN_EXP,
    }
    # Add cookies to the driver
    try:
        driver.get("https://www.linkedin.com")
        driver.add_cookie(cookie)
    except Exception as e:
        print(f"Error adding cookies to driver : {e}")
    