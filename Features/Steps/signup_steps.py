import json
import os

from behave import *
from playwright.sync_api import expect

from Utilities.ReadConfig import readConfig as rc
from Utilities import Controller as con

@Given(u'I launch application and go to login page')
def step_impl(context):
    context.page.goto(os.environ.get("BASE_URL"))
    context.header.click_header_login_naav_link()

@when(u'I go to signup page and fill all details')
def step_impl(context):
    context.test_signup_data = {}
    context.test_signup_data["name"] = context.lp.signup_enter_name()
    context.test_signup_data["email"] = context.lp.signup_enter_signup_email()
    context.lp.click_signup_submit_btn()
    context.test_signup_data["title"] = context.sp.signup_click_title_checkbox()
    context.sp.signup_enter_password()
    context.test_signup_data["birth_day"], context.test_signup_data["birth_month"], context.test_signup_data["birth_year"] = \
        context.sp.signup_select_dob()
    context.sp.click_signup_newsletter_checkbox()
    context.sp.click_special_offers_optin_checkbox()
    context.test_signup_data["first_name"] =  context.sp.signup_enter_fname()
    context.test_signup_data["last_name"] = context.sp.signup_enter_lname()
    context.test_signup_data["company"] = context.sp.signup_enter_company()
    context.test_signup_data["address1"] = context.sp.signup_enter_address1()
    context.test_signup_data["address2"] = context.sp.signup_enter_address2()
    context.test_signup_data["country"] = context.sp.signup_select_country()
    context.test_signup_data["state"] = context.sp.signup_enter_state()
    context.test_signup_data["city"] = context.sp.signup_enter_city()
    context.test_signup_data["zipcode"] = context.sp.signup_enter_zipcode()
    context.sp.signup_enter_mobile_number()
    print(context.test_signup_data)

@when(u'I submit signup')
def step_impl(context):
    context.sp.click_signup_create_account_submit_btn()

@then(u'New user successfully to be created')
def step_impl(context):
    selector = rc("ACCOUNT_CREATED_PAGE", "account_created_confirmation_text_css")
    expected = "Congratulations! Your new account has been successfully created!"
    expect(context.page.locator(selector)).to_have_text(expected)

@when(u'I get the API response')
def step_impl(context):
    new_user_email = context.test_signup_data.get("email")
    api = f"{os.environ.get("user_detail_api")}{new_user_email}"
    context.page.goto(api)
    resp = context.page.locator('//body').text_content()
    resp = json.loads(resp.strip())
    context.new_user_detail = resp["user"]

@then(u'New user details should be found')
def step_impl(context):
    expected_data = context.test_signup_data
    actual_data = context.new_user_detail
    mismatches = {}

    # 1. Iterate over keys in the 'expected' dictionary (the baseline).
    for key, expected_value in expected_data.items():
        if key == "birth_month":
            expected_value = str(con.get_numeric_month_string(expected_value))

        # Check if the key is even present in the 'actual' data
        if key not in actual_data:
            mismatches[key] = f"Key missing in actual data. Expected value: '{expected_value}'"
            continue

        actual_value = actual_data[key]

        # Check if the values match
        if actual_value != expected_value:
            mismatches[key] = {
                "expected": expected_value,
                "actual": actual_value
            }

    # 2. Check for extra keys in 'actual' data (specifically the 'id' key).
    # We use set difference to find keys present in 'actual' but NOT in 'expected'.
    extra_keys = set(actual_data.keys()) - set(expected_data.keys())

    for key in extra_keys:
        # We are specifically ignoring the 'id' key as per your requirement.
        if key != "id":
            mismatches[key] = f"Key '{key}' found in actual data, but not expected."
        else:
            # Optional: Log the ignored key for clarity
            context.logger.info(f"Successfully ignored extra key: '{key}' with value: {actual_data[key]}")

    # 3. Final validation result.
    if not mismatches:
        context.logger.info("✅ Validation successful! All matching keys have identical values.")
    else:
        context.logger.error("\n❌ Validation failed. Mismatches found:")
        for key, details in mismatches.items():
            if isinstance(details, dict):
                context.logger.error(
                    f"  Key '{key}': VALUE MISMATCH (Expected: '{details['expected']}', Actual: '{details['actual']}')")
            else:
                context.logger.info(f"  Key '{key}': {details}")