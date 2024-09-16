"""DEFAULT VARIABLES"""
from robocorp import vault, storage


secrets = vault.get_secret("Fundamentus")
locators = storage.get_json("Fundamentus Extraction")


# >>>>>>>>>EMAIL CONFIGS>>>>>>>>>
# SMTP_HOST = "smtp.gmail.com"
SMTP_HOST = secrets["SMTP_HOST"]
# SMTP_PORT = 587
SMTP_PORT = secrets["SMTP_PORT"]
# SMTP_USER = "rickpincelli@gmail.com"
SMTP_USER = secrets["SMTP_USER"]
# SMTP_PASWORD = "aqjl azga tfeq wszb"
SMTP_PASWORD = secrets["SMTP_PASWORD"]
# <<<<<<<<<EMAIL CONFIGS<<<<<<<<<

# >>>>>>>>>FUNDAMENTUS RPA CONFIGS>>>>>>>>>
EMAIL_FUNDAMENTUS = locators["email_fundamentus"]
# <<<<<<<<<FUNDAMENTUS RPA CONFIGS<<<<<<<<<
