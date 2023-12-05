DIRECTORIES = {
    # here will be common locators for all pages:
    'sidepanel_title': {'type': 'css', 'locator': 'h3.side-panel__title'},
    'close_sidepanel_btn': {'type': 'css', 'locator': 'button[data-test="close"]'},
    'sidepanel_head_content': {'type': 'css', 'locator': '.side-panel__head div'},
    'save_table_btn': {'type': 'css', 'locator': 'div.versatile-header__actions button'},
    'first_row': {'type': 'css', 'locator': '.vue-recycle-scroller__item-wrapper > div:nth-child(1) a'},
    'table': {'type': 'css', 'locator': '.vue-recycle-scroller__item-wrapper'},
    'nav_breads': {'type': 'css', 'locator': 'nav.versatile-header__breads'},

    # assortment section locators
    'assortment_title': {'type': 'xpath', 'locator': '(//div[@class="section__header"])[1]'},
    'monitoring_section': {'type': 'xpath', 'locator': '//div[@data-test="section:id1"]/a[1]'},
    'mrc_section': {'type': 'xpath', 'locator': '//div[@data-test="section:id1"]/a[2]'},
    'mcp_section': {'type': 'xpath', 'locator': '//div[@data-test="section:id1"]/a[3]'},
    'margin_limit_section': {'type': 'xpath', 'locator': '//div[@data-test="section:id1"]/a[4]'},
    'price_limit_section': {'type': 'xpath', 'locator': '//div[@data-test="section:id1"]/a[5]'},
    'complex_discounts_section': {'type': 'xpath', 'locator': '//div[@data-test="section:id1"]/a[6]'},
    'production_countries_section': {'type': 'xpath', 'locator': '//div[@data-test="section:id1"]/a[7]'},
    'supply_type_section': {'type': 'xpath', 'locator': '//div[@data-test="section:id1"]/a[8]'},
    'assortment_type_section': {'type': 'xpath', 'locator': '//div[@data-test="section:id1"]/a[9]'},
    'goods_section': {'type': 'xpath', 'locator': '//div[@data-test="section:id1"]/a[10]'},

    # shop section
    'shop_title': {'type': 'xpath', 'locator': '(//div[@class="section__header"])[2]'},
    'competitors_section': {'type': 'xpath', 'locator': '//div[@data-test="section:id2"]/a[1]'},
    'divisions_section': {'type': 'xpath', 'locator': '//div[@data-test="section:id2"]/a[2]'},

    # kib section locators
    'kib_changing_title': {'type': 'xpath', 'locator': '(//div[@class="section__header"])[3]'},
    'settlements_kib_section': {'type': 'xpath', 'locator': '//div[@data-test="section:id3"]/a[1]'},
    'sku_kib_section': {'type': 'xpath', 'locator': '//div[@data-test="section:id3"]/a[2]'},
    'prices_kib_section': {'type': 'xpath', 'locator': '//div[@data-test="section:id3"]/a[3]'},
    'kib_sku_compliance_section': {'type': 'xpath', 'locator': '//div[@data-test="section:id3"]/a[4]'},
    'settlements_correspondence_kib_section': {'type': 'xpath', 'locator': '//div[@data-test="section:id3"]/a[5]'},

    # parameters section locators
    'parameters_title': {'type': 'xpath', 'locator': '(//div[@class="section__header"])[4]'},
    'sprice_section': {'type': 'xpath', 'locator': '//div[@data-test="section:id4"]/a[1]'},
    'exceptions_section': {'type': 'xpath', 'locator': '//div[@data-test="section:id4"]/a[2]'},
    'log_margin_section': {'type': 'xpath', 'locator': '//div[@data-test="section:id4"]/a[3]'},
    'holidays_section': {'type': 'xpath', 'locator': '//div[@data-test="section:id4"]/a[4]'},
    'price_reasons_section': {'type': 'xpath', 'locator': '//div[@data-test="section:id4"]/a[5]'},
    # price lists section locators
    'price_lists_title': {'type': 'xpath', 'locator': '(//div[@class="section__header"])[5]'},
    # sprice_types_section
    'sprice_types_section': {'type': 'xpath', 'locator': '//div[@data-test="section:id5"]/a[1]'},
    'virtual_subunits_section': {'type': 'xpath', 'locator': '//div[@data-test="section:id5"]/a[2]'},
    'price_lists_section': {'type': 'xpath', 'locator': '//div[@data-test="section:id5"]/a[3]'},
    'stores_price_lists_section': {'type': 'xpath', 'locator': '//div[@data-test="section:id5"]/a[4]'},
    'creating_connections_section': {'type': 'xpath', 'locator': '//div[@data-test="section:id5"]/a[5]'},
}
