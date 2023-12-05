PROFILE = {
    'profile_popup': {'type': 'css', 'locator': 'div.profile:nth-of-type(3)'},
    'username': {'type': 'css', 'locator': '.profile:nth-of-type(3) .header div'},
    'close_profile_btn': {'type': 'css', 'locator': '.profile:nth-of-type(3) [data-test=close-profile]'},
    'info_tab': {'type': 'css', 'locator': '.tabs > div.tab:nth-child(1)'},
    'files_tab': {'type': 'css', 'locator': '.tabs > div.tab:nth-child(2)'},
    'logout_btn': {'type': 'css', 'locator': 'button[data-test=exit]'},
    'role_header': {'type': 'css', 'locator': '.side-panel-info-item:nth-of-type(1) h5'},
    'role_value': {'type': 'css', 'locator': '.side-panel-info-item:nth-of-type(1) div'},
    'category_header': {'type': 'xpath', 'locator': '//h5[contains(text(), "Категория")]'},
    'category_value': {'type': 'xpath', 'locator': '//h5[contains(text(), "Категория")]/../div'},
    'group_header': {'type': 'xpath', 'locator': '//h5[contains(text(), "Группа")]'},
    'group_value': {'type': 'xpath', 'locator': '//h5[contains(text(), "Группа")]/../div'},
    'subgroup_header': {'type': 'xpath', 'locator': '//h5[contains(text(), "Подгруппа")]'},
    'subgroup_value': {'type': 'xpath', 'locator': '//h5[contains(text(), "Подгруппа")]/../div'},
    'department_header': {'type': 'css', 'locator': '.side-panel-info-item:nth-of-type(2) h5'},
    'department_value': {'type': 'css', 'locator': '.side-panel-info-item:nth-of-type(2) div'},
    'email_header': {'type': 'css', 'locator': '.side-panel-info-item:nth-of-type(3) h5'},
    'email_value': {'type': 'css', 'locator': '.side-panel-info-item:nth-of-type(3) div'},
    'latest_activity_header': {'type': 'css', 'locator': '.files .chapter:nth-child(1) .header'},
    'latest_activity_file': {'type': 'css', 'locator': '.chapter:last-child .file>a'},
}
