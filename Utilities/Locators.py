from Utilities.ReadConfig import readConfig as rc

# Basic info locators
basic_info_section = "basic_info"

def get_dashboard_url():
    return rc(basic_info_section, "dashboard_url")

# Login Page locators

login_page_section = "login_page"

def get_login_page_username_field_locator():
    return rc(login_page_section, "username_input_field_xpath")

def get_login_page_password_field_locator():
    return rc(login_page_section, "password_input_field_xpath")

def get_login_page_submit_login_btn_locator():
    return rc(login_page_section, "submit_btn_xpath")

def get_login_page_forgot_pass_link_locator():
    return rc(login_page_section, "forgot_password_link_xpath")

def get_login_page_required_field_err_msg_locator():
    return rc(login_page_section, "field_required_err_msg_xpath")

def get_login_page_invalid_creds_err_msg_locator():
    return rc(login_page_section, "invalid_creds_err_msg_xpath")