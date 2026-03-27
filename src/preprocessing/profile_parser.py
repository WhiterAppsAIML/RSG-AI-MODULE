from dataclasses import dataclass
from typing import List


@dataclass
class ProfileInput:
    first_name: str
    last_name: str
    position_title: str
    company_name: str
    work_details: str
    years_of_experience: float
    institution_name: str
    domain_label: int
    domain_onehot: List[float]
    skills_text: str
    experience_tier: str


def parse_flutter_json(data: dict) -> ProfileInput:
    """
    Convert Flutter JSON payload into ProfileInput dataclass
    """

    first_name = data.get("first_name", "")
    last_name = data.get("last_name", "")
    position_title = data.get("position_title", "")
    company_name = data.get("company_name", "")
    work_details = data.get("work_details", "")
    institution_name = data.get("institution_name", "")

    years_of_experience = float(data.get("years_of_experience", 0.0))

    # placeholder values (filled later in pipeline)
    domain_label = -1
    domain_onehot = [0.0] * 7

    skills_text = position_title + " " + work_details

    experience_tier = "fresher"

    return ProfileInput(
        first_name,
        last_name,
        position_title,
        company_name,
        work_details,
        years_of_experience,
        institution_name,
        domain_label,
        domain_onehot,
        skills_text,
        experience_tier,
    )