from fastapi import FastAPI, HTTPException

from services.candidate_scraper import scrape_linkedin_profile
from services.company_scraper import scrape_linkedin_company

app = FastAPI()

@app.get("/profile-data/{linkedin_id}")
async def profile_data(linkedin_id: str):
    try:
        profile_infos = scrape_linkedin_profile(linkedin_id)
        return profile_infos
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error fetching profile details")

@app.get("/comapny-data/{linkedin_id}")
async def comapny_data(linkedin_id: str):
    try:
        profile_infos = scrape_linkedin_company(linkedin_id)
        return profile_infos
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error fetching company details")