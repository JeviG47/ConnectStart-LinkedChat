import os
import requests


def scrape_linkedin_url(linkedin_url: str):
    """Scrapes Linkedin information of the person's profile"""
    headers = {"Authorization": f'Bearer {os.environ.get("PROXYCURL_API_KEY")}'}
    api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"

    response = requests.get(api_endpoint, params={"url": linkedin_url}, headers=headers)
    data = response.json()
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
        and k not in ["people_also_viewed", "certifications"]
    }
    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    return data
