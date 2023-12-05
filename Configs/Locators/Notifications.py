NOTIFICATIONS = {
    'title': {'type': 'css', 'locator': '.notifications .header div'},
    'quantity': {'type': 'css', 'locator': '.notifications .header div span'},
    'close_btn': {'type': 'css', 'locator': '.notifications [data-test="close-profile"]'},
    'more_info_btn': {'type': 'css', 'locator': '.notifications a'},
    'title_of_notification': {'type': 'css', 'locator': '.notifications div:nth-child(3) > div > span:nth-child(1)'},
    'notification_status': {'type': 'css', 'locator': '.notifications div:nth-child(3) > div > span:nth-child(2)'},
    'notification_date': {'type': 'css', 'locator': '.notifications div:nth-child(3) > div > div> span'},
    'notifications_profile': {'type': 'css', 'locator': '.notifications.profile'},
    'last_notify': {'type': 'xpath', 'locator': '//div[@class="notifications profile"]/div[3]/div[last()]'},
}
