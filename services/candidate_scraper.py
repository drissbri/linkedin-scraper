from selenium import webdriver
from time import sleep
from services.scraping_utils import options, service, search_for_candidate_name, search_for_candidate_headline, search_for_section, add_session_cookie


def scrape_linkedin_profile(linkedin_id):
    """Scraping linkedIn profile data"""
    try:
        # Setup Selenium WebDriver
        driver = webdriver.Chrome(service=service,options=options)    

        # Load cookies from the file
        add_session_cookie(driver)

        print(f'Scraping data for id: {linkedin_id}')

        # LinkedIn URL for the profile
        profile_url = f"https://www.linkedin.com/in/{linkedin_id}/"

        # Navigate to the LinkedIn profile
        driver.get(profile_url)

        if "/404" in driver.current_url or "Page not found" in driver.page_source:
            driver.quit()
            print(f"Profile for {linkedin_id} not found (404)")
            return {"error": f"Profile for {linkedin_id} not found."}

        sleep(1)

        # Scrape name,experinces,education form the LinkedIn profile
        try:
            name = search_for_candidate_name(driver)
            if name == "null":
                return {"error": "Your Linkedin session token is not set up correctly or has expired"}
            headline = search_for_candidate_headline(driver)
            education = search_for_section(driver,"Education")
            experience = search_for_section(driver,"Experience")
        except Exception as e:
            print(f"Error scraping details for {linkedin_id} : {e}")
            return {"error": "Error searching for details for {linkedin_id}"}
    
        driver.quit()

        print(f"finished feching details for profile {linkedin_id} successfully")
        return {
            "linkedin_id": linkedin_id,
            "name": name,
            "headline": headline,
            "education": education,
            "experience": experience,
        }
    
    except Exception as e:
        print(f"Error feching details for {linkedin_id} : {e}")
        return {"error": "Error feching profile details for {linkedin_id}"}