KIB_EXCHANGE = {
    # settlements_kib_section
    'settlement_title': {'type': 'css', 'locator': 'div[data-test="column-header-settlement"]'},
    'settlement_cell': {'type': 'css', 'locator': '[data-test="settlement"]'},
    'territory_code_title': {'type': 'css', 'locator': 'div[data-test="column-header-territoryCode"]'},
    'territory_code_cell': {'type': 'css', 'locator': '[data-test="territoryCode"]'},
    'uploading_to_oracle_date_title': {'type': 'css',
                                       'locator': 'div[data-test="column-header-uploadingToOracleDate"]'},
    'uploading_to_oracle_date_cell': {'type': 'css', 'locator': '[data-test="uploadingToOracleDate"]'},


    # sku_kib_section
    'product_kib_title': {'type': 'css', 'locator': 'div[data-test="column-header-productKib"] div'},
    'product_kib_cell': {'type': 'css', 'locator': '[data-test="sku-data-item-name"]'},
    'product_kib_label': {'type': 'css', 'locator': '.side-panel__content > div > div:nth-child(1) h5'},
    'product_kib_value': {'type': 'css', 'locator': '.side-panel__content > div > div:nth-child(1) div'},
    'sku_kib_title': {'type': 'css', 'locator': 'div[data-test="column-header-skuKib"] div'},
    'sku_kib_cell': {'type': 'css', 'locator': '[data-test="sku-data-item-skuId"]'},
    'sku_kib_label': {'type': 'css', 'locator': '.side-panel__content > div > div:nth-child(2) h5'},
    'sku_kib_value': {'type': 'css', 'locator': '.side-panel__content > div > div:nth-child(2) div'},
    'upload_to_oracle_title': {'type': 'css', 'locator': 'div[data-test="column-header-uploadToOracle"] div'},
    'upload_to_oracle_cell': {'type': 'css', 'locator': '[data-test="sku-data-item-upload-date-to-oracle"]'},
    'upload_to_oracle_label': {'type': 'css', 'locator': '.side-panel__content > div > div:nth-child(3) h5'},
    'upload_to_oracle_value': {'type': 'css', 'locator': '.side-panel__content > div > div:nth-child(3) div'},


    # prices_kib_section
    'prices_kib_day_title': {'type': 'css', 'locator': 'div[data-test="column-header-day"]'},
    'prices_kib_day_cell': {'type': 'xpath', 'locator': '//a[@data-test="item-id-1"]/div[2]/div'},
    'prices_kib_region_cell': {'type': 'xpath', 'locator': '//a[@data-test="item-id-1"]/div[3]/div'},
    'prices_kib_comment_title': {'type': 'css', 'locator': 'div[data-test="column-header-comment"]'},
    'prices_kib_comment_cell': {'type': 'xpath', 'locator': '//a[@data-test="item-id-1"]/div[4]/div'},
    'prices_kib_editor_title': {'type': 'css', 'locator': 'div[data-test="column-header-editor"]'},
    'prices_kib_editor_cell': {'type': 'xpath', 'locator': '//a[@data-test="item-id-1"]/div[5]/div'},
    'prices_kib_editions_title': {'type': 'css', 'locator': 'div[data-test="column-header-editions"]'},
    'prices_kib_editions_cell': {'type': 'xpath', 'locator': '//a[@data-test="item-id-1"]/div[6]/div'},


    # kib_sku_compliance
    'kib_sku_analog_code_title': {'type': 'css', 'locator': 'div[data-test="column-header-analogCode"]'},
    'kib_sku_analog_code_cell': {'type': 'xpath', 'locator': '(//span[@data-test="item-analog-code"])[1]'},
    'kib_sku_analog_title': {'type': 'css', 'locator': 'div[data-test="column-header-analog"]'},
    'kib_sku_analog_cell': {'type': 'xpath', 'locator': '(//span[@data-test="item-analog"])[1]'},
    'kib_sku_title': {'type': 'css', 'locator': 'div[data-test="column-header-SKUKiB"]'},
    'kib_sku_cell': {'type': 'xpath', 'locator': '(//span[@data-test="item-sku-kib"])[1]'},
    'kib_sku_product_title': {'type': 'css', 'locator': 'div[data-test="column-header-productKiB"]'},
    'kib_sku_product_cell': {'type': 'xpath', 'locator': '(//span[@data-test="item-product-kib"])[1]'},
    'coefficient_title': {'type': 'css', 'locator': 'div[data-test="column-header-coefficient"]'},
    'kib_sku_coefficient_cell': {'type': 'xpath', 'locator': '(//span[@data-test="item-coefficient"])[1]'},
    'pc_title': {'type': 'css', 'locator': 'div[data-test="column-header-pc"]'},
    'kib_sku_pc_cell': {'type': 'xpath', 'locator': '(//span[@data-test="item-pc"])[1]'},
    'social_goods_title': {'type': 'css', 'locator': 'div[data-test="column-header-socialGoods"]'},
    'social_goods_cell': {'type': 'xpath', 'locator': '(//span[@data-test="item-social-goods"])[1]'},
    'monita_title': {'type': 'css', 'locator': 'div[data-test="column-header-monita"]'},
    'monita_cell': {'type': 'xpath', 'locator': '(//span[@data-test="item-monita"])[1]'},
    'exchange_participation_title': {'type': 'css', 'locator': 'div[data-test="column-header-exchangeParticipation"]'},
    'exchange_participation_cell': {'type': 'xpath',
                                    'locator': '(//span[@data-test="item-exchange-participation"])[1]'},
    'created_title': {'type': 'css', 'locator': 'div[data-test="column-header-created"]'},
    'created_cell': {'type': 'xpath', 'locator': '(//span[@data-test="item-created"])[1]'},


    # settlements_correspondence_kib_section
    'area_code_title': {'type': 'css', 'locator': 'div[data-test="column-header-areaCode"]'},
    'area_code_cell': {'type': 'xpath', 'locator': '(//div[@data-test="item-area-code"])[1]/div'},
    'kib_locality_title': {'type': 'css', 'locator': 'div[data-test="column-header-localityKib"]'},
    'kib_locality_cell': {'type': 'xpath', 'locator': '(//div[@data-test="item-locality-kib"])[1]/div'},
    'area_code_bristol_title': {'type': 'css', 'locator': 'div[data-test="column-header-areaCodeBristol"]'},
    'area_code_bristol_cell': {'type': 'xpath', 'locator': '(//div[@data-test="item-area-code-bristol"])[1]/div'},
    'region_bristol_title': {'type': 'css', 'locator': 'div[data-test="column-header-regionBristol"]'},
    'region_bristol_cell': {'type': 'xpath', 'locator': '(//div[@data-test="item-region-bristol"])[1]/div'},
    'locality_bristol_title': {'type': 'css', 'locator': 'div[data-test="column-header-localityBristol"]'},
    'locality_bristol_cell': {'type': 'xpath', 'locator': '(//div[@data-test="item-locality-bristol"])[1]/div'},
    'has_exchange_title': {'type': 'css', 'locator': 'div[data-test="column-header-participationInExchange"]'},
    'has_exchange_cell': {'type': 'xpath', 'locator': '(//div[@data-test="item-participation-in-exchange"])[1]/div'},
    'sc_kib_changes_title': {'type': 'css', 'locator': 'div[data-test="column-header-changes"]'},
    'sc_kib_changes_cell': {'type': 'xpath', 'locator': '(//div[@data-test="item-changes"])[1]/div'},
}
