from RPA_APP.rpa.procedures import RPAFundamentus
from RPA_APP.config import EMAIL_FUNDAMENTUS


def bot_fundamentus():
    """Function to init RPA's"""

    # >>>>>>>>>Fundamentus RPA>>>>>>>>>
    # >>>>>>>>>Parameters from robocorp storage>>>>>>>>>
    email = EMAIL_FUNDAMENTUS
    # <<<<<<<<<Parameters from robocorp storage<<<<<<<<<

    # >>>>>>>>>RPA's Procedure>>>>>>>>>
    print("=-=" * 24)
    print("Initiating Fundamentus RPA")
    result_fundamentus = RPAFundamentus.fundamentus_extraction(email=email)
    print(">" * 45)
    print(result_fundamentus)
    print("<" * 45)
    print("=-=" * 24)
    # <<<<<<<<<RPA's Procedure<<<<<<<<<
    # <<<<<<<<<Fundamentus RPA<<<<<<<<<
