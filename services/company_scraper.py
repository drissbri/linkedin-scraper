from selenium import webdriver
from time import sleep
from services.scraping_utils import options, service, search_for_company_name, search_for_company_industry, search_for_company_about, add_session_cookie


def scrape_linkedin_company(linkedin_id):
    """Scraping linkedIn company data"""
    try:
        # Setup Selenium WebDriver
        driver = webdriver.Chrome(service=service,options=options)

        # Load cookies from the file
        add_session_cookie(driver)

        print(f'Scraping data for company id: {linkedin_id}')

        # LinkedIn URL for the company
        company_url = f"https://www.linkedin.com/company/{linkedin_id}/"

        # Navigate to the LinkedIn company
        driver.get(company_url)

        if "/unavailable" in driver.current_url or "Page not found" in driver.page_source:
            driver.quit()
            print(f"Company profile for {linkedin_id} not found (404)")
            return {"error": f"Company profile for {linkedin_id} not found."}
        
        sleep(1)

        # Scrape name,about form the LinkedIn company
        try:
            name = search_for_company_name(driver)
            if not name:
                driver.quit()
                print("scraping failed due to session token not setup or expired")
                return {"error": "Your Linkedin session token is not set up correctly or has expired"}
            industry = search_for_company_industry(driver)
            about = search_for_company_about(driver)
        except Exception as e:
            print(f"Error scraping details for company {linkedin_id} : {e}")
            return {"error": f"Error searching for details for company {linkedin_id}"}

        driver.quit()

        print(f"finished feching details for company {linkedin_id} successfully")
        return {
            "linkedin_id": linkedin_id,
            "name": name,
            "industry": industry,
            "about": about,
        }
    except Exception as e:
        print(f"Error feching details for comapny {linkedin_id} : {e}")
        return {"error": f"Error feching company details for {linkedin_id}"}