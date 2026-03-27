from typing import Tuple, List


# Domain keyword mapping
DOMAIN_KEYWORDS = {
    0: ["software", "developer", "programmer", "engineer", "python", "java"],
    1: ["manager", "management", "marketing", "sales", "business"],
    2: ["designer", "ui", "ux", "graphics", "creative"],
    3: ["doctor", "nurse", "medical", "healthcare", "clinic"],
    4: ["finance", "accountant", "bank", "financial", "audit"],
    5: ["lawyer", "legal", "attorney", "law"],
    6: ["teacher", "education", "professor", "school", "university"]
}


def detect_domain(text: str) -> Tuple[int, List[float]]:
    """
    Detect domain from position_title + work_details
    Returns domain_label and one-hot encoded vector
    """

    text = text.lower()

    domain_label = 1  # default → Management

    for domain, keywords in DOMAIN_KEYWORDS.items():
        for keyword in keywords:
            if keyword in text:
                domain_label = domain
                break

    one_hot = [0.0] * 7
    one_hot[domain_label] = 1.0

    return domain_label, one_hot