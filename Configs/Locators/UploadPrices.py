UPLOAD_PRICES = {
    'confirm_btn': {'type': 'css', 'locator': 'button[data-test="confirm"]'},
    'upload_btn': {'type': 'css', 'locator': 'button[data-test="download"]'},
    'download_btn': {'type': 'css', 'locator': '.versatile-header__head-group .vtooltip button'},
    'download_tooltip': {'type': 'xpath', 'locator': '//div[@class="versatile-header__actions"]/div/div'},
    'header_info': {'type': 'css', 'locator': '.versatile-header__info'},
    'all_prices_tab': {'type': 'css', 'locator': '.versatile-header__filters div.tab:nth-child(1)'},
    'without_changes_tab': {'type': 'css', 'locator': '.versatile-header__filters div.tab:nth-child(2)'},
    'new_tab': {'type': 'css', 'locator': '.versatile-header__filters div.tab:nth-child(3)'},
    'close_tab': {'type': 'css', 'locator': '.versatile-header__filters div.tab:nth-child(4)'},
    'up_tab': {'type': 'css', 'locator': '.versatile-header__filters div.tab:nth-child(5)'},
    'down_tab': {'type': 'css', 'locator': '.versatile-header__filters div.tab:nth-child(6)'},
    'start_date_header': {'type': 'css', 'locator': 'div[data-test="column-header-startDate"]'},
    'icon_header': {'type': 'css', 'locator': 'div[data-test="column-header-icon"]'},
    'start_date_cell': {'type': 'css', 'locator': '.vue-recycle-scroller__item-view:nth-child(1) '
                                                  '[data-test="pricing-start-date"] div'},
    'icon_cell': {'type': 'css', 'locator': '.vue-recycle-scroller__item-view:nth-child(1) [data-test="pricing-status"]'},
    'end_date_header': {'type': 'css', 'locator': 'div[data-test="column-header-endDate"]'},
    'end_date_cell': {'type': 'css', 'locator': '.vue-recycle-scroller__item-view:nth-child(1) [data-test="pricing'
                                                '-end-date"] div'},
    'price_list_header': {'type': 'css', 'locator': 'div[data-test="column-header-priceList"]'},
    'price_list_cell': {'type': 'css', 'locator': '.vue-recycle-scroller__item-view:nth-child(1) [data-test="pricing-'
                                                  'price-list"]'},
    'code_header': {'type': 'css', 'locator': 'div[data-test="column-header-code"]'},
    'code_cell': {'type': 'css', 'locator': '.vue-recycle-scroller__item-view:nth-child(1) '
                                            '[data-test="pricing-code"] div'},
    'nomenclature_header': {'type': 'css', 'locator': 'div[data-test="column-header-nomenclature"]'},
    'nomenclature_cell': {'type': 'css', 'locator': '.vue-recycle-scroller__item-view:nth-child(1) [data-test='
                                                    '"pricing-nomenclature"]'},
    'price_header': {'type': 'css', 'locator': 'div[data-test="column-header-price"]'},
    'price_cell': {'type': 'css', 'locator': '.vue-recycle-scroller__item-view:nth-child(1) [data-test="pricing-price"]'},
    'promo_header': {'type': 'css', 'locator': 'div[data-test="column-header-promo"]'},
    'promo_cell': {'type': 'css', 'locator': '.vue-recycle-scroller__item-view:nth-child(1) [data-test="pricing-promo"]'},
    'cause_header': {'type': 'css', 'locator': 'div[data-test="column-header-cause"]'},
    'cause_cell': {'type': 'css', 'locator': '.vue-recycle-scroller__item-view:nth-child(1) '
                                             '[data-test="pricing-cause"] div'},
    'check_all_inp': {'type': 'xpath', 'locator': '(//input[@data-test="check-all-items"]/../span)[1]'},
    'check_first_item_inp': {'type': 'xpath', 'locator': '(//a//label[@class="checkbox"]/span)[1]'},
    'check_second_item_inp': {'type': 'xpath', 'locator': '(//a//label[@class="checkbox"]/span)[2]'},
    'check_third_item_inp': {'type': 'xpath', 'locator': '(//a//label[@class="checkbox"]/span)[3]'},
    'check_fourth_item_inp': {'type': 'xpath', 'locator': '(//a//label[@class="checkbox"]/span)[4]'},
    'check_fiftieth_item_inp': {'type': 'xpath', 'locator': '(//a//label[@class="checkbox"]/span)[5]'},
    'previous_price_txt': {'type': 'css', 'locator': '.side-panel__head > div:nth-of-type(1) h5'},
    'previous_price_value': {'type': 'css', 'locator': '.side-panel__head > div:nth-of-type(1) p'},
    'price_txt': {'type': 'css', 'locator': '.side-panel__head > div:nth-of-type(2) h5'},
    'price_value': {'type': 'css', 'locator': '.side-panel__head > div:nth-of-type(2) p'},
    'info_tab': {'type': 'css', 'locator': 'div[data-test="pricing-item-side-panel"] .tab:nth-child(1)'},
    'calculating_stages_tab': {'type': 'css', 'locator': 'div[data-test="pricing-item-side-panel"] .tab:nth-child(2)'},
    'status_title': {'type': 'css', 'locator': '.side-panel__content > div > div:nth-child(1) h5'},
    'status_value': {'type': 'css', 'locator': '.side-panel__content > div > div:nth-child(1) span:nth-child(2)'},
    'nomenclature_title': {'type': 'css', 'locator': '.side-panel__content > div > div:nth-child(2) h5'},
    'nomenclature_value': {'type': 'css', 'locator': '.side-panel__content > div > div:nth-child(2) div'},
    'start_date_title': {'type': 'css', 'locator': '.side-panel__content > div > div:nth-child(3) h5'},
    'start_date_value': {'type': 'css', 'locator': '.side-panel__content > div > div:nth-child(3) div'},
    'end_date_title': {'type': 'css', 'locator': '.side-panel__content > div > div:nth-child(4) h5'},
    'end_date_value': {'type': 'css', 'locator': '.side-panel__content > div > div:nth-child(4) div'},
    'price_list_title': {'type': 'css', 'locator': '.side-panel__content > div > div:nth-child(5) h5'},
    'price_list_value': {'type': 'css', 'locator': '.side-panel__content > div > div:nth-child(5) div'},
    'code_title': {'type': 'css', 'locator': '.side-panel__content > div > div:nth-child(6) h5'},
    'code_value': {'type': 'css', 'locator': '.side-panel__content > div > div:nth-child(6) div'},
    'promo_title': {'type': 'css', 'locator': '.side-panel__content > div > div:nth-child(7) h5'},
    'promo_value': {'type': 'css', 'locator': '.side-panel__content > div > div:nth-child(7) div'},
    'cause_title': {'type': 'css', 'locator': '.side-panel__content > div > div:nth-child(8) h5'},
    'cause_value': {'type': 'css', 'locator': '.side-panel__content > div > div:nth-child(8) div'},
    'comment_title': {'type': 'css', 'locator': '.side-panel__content > div > div:nth-child(9) h5'},
    'comment_value': {'type': 'css', 'locator': '.side-panel__content > div > div:nth-child(9) div'},
    'uploaded_price_title': {'type': 'css', 'locator': '.side-panel__content > div > div:nth-child(1) h5'},
    'uploaded_price_value': {'type': 'css', 'locator': '.side-panel__content > div > div:nth-child(1) p'},
    'log_margin_title': {'type': 'css', 'locator': '.side-panel__content > div > div:nth-child(2) h5'},
    'log_margin_value': {'type': 'css', 'locator': '.side-panel__content > div > div:nth-child(2) p'},
    'sprice_title': {'type': 'css', 'locator': '.side-panel__content > div > div:nth-child(3) h5'},
    'sprice_value': {'type': 'css', 'locator': '.side-panel__content > div > div:nth-child(3) p'},
    'delete_row_btn': {'type': 'css', 'locator': '.side-panel__foot button'},
    'popup': {'type': 'css', 'locator': '.modal-content'},
    'popup_title': {'type': 'css', 'locator': '.modal-content h5'},
    'popup_text': {'type': 'css', 'locator': '.modal-content > div:nth-of-type(2) div'},
    'popup_confirm_btn': {'type': 'css', 'locator': '.modal-content button[data-test="confirm"]'},
    'popup_cancel_btn': {'type': 'css', 'locator': '.modal-content button[data-test="close"]'},
    'popup_close_btn': {'type': 'css', 'locator': '.modal-content button[data-test="cancel"]'},
    'table_name': {'type': 'css', 'locator': '.modal-body > div > div >div > div:nth-child(1)'},
    'table_size': {'type': 'css', 'locator': '.modal-body > div > div >div > div:nth-child(2)'},
    'uploading_settings_title': {'type': 'css', 'locator': '.modal-body > div:nth-child(2) h4'},
    'default_radio': {'type': 'css', 'locator': 'input[data-test="uploadOption-default"]'},
    'log_margin_radio': {'type': 'css', 'locator': 'input[data-test="uploadOption-logMargin"]'},
    'log_margin_span': {'type': 'xpath', 'locator': '//input[@data-test="uploadOption-logMargin"]/../span[1]'},
    'multiply_regions_radio': {'type': 'css', 'locator': 'input[data-test="uploadOption-multiplyRegions"]'},
    'multiply_regions_span': {'type': 'xpath',
                              'locator': '//input[@data-test="uploadOption-multiplyRegions"]/../span[1]'},
    'ignore_inconsistencies_title': {'type': 'css', 'locator': '.modal-body > div:nth-child(3) h4'},
    'ignore_inconsistencies_checkbox': {'type': 'css', 'locator': 'input[data-test="inconsistenciesIgnored"]'},
    'ignore_inconsistencies_span': {'type': 'xpath',
                                    'locator': '//input[@data-test="inconsistenciesIgnored"]/../span[1]'},
    'cancel_btn': {'type': 'css', 'locator': 'button[data-test="cancel"]'},
    'change_file_btn': {'type': 'css', 'locator': 'span[data-test="openFileDialog"]'},
    'rows_selected_txt': {'type': 'css', 'locator': 'p.advanced-flex-table-bottom-panel__info'},
    'uncheck_all_btn': {'type': 'css', 'locator': 'button[data-test="uncheckAll"]'},
    'process_checked_items_btn': {'type': 'css', 'locator': 'button[data-test="processCheckedItems"]'},
    'deleting_popup_title': {'type': 'css', 'locator': '.modal-header h5'},
    'deleting_popup_txt': {'type': 'css', 'locator': '.modal-body div'},
    'page_title': {'type': 'css', 'locator': 'h1.versatile-header__title'},
    'status_tooltip': {'type': 'xpath', 'locator': '(//div[@data-test="pricing-status"]/../div[2])[1]'},
    'nomenclature_tooltip': {'type': 'xpath', 'locator': '(//span[@data-test="pricing-nomenclature"]/../div)[1]'},
    'promo_tooltip': {'type': 'xpath', 'locator': '(//span[@data-test="pricing-promo"]/../div)[1]'},
    'row_selected': {'type': 'xpath', 'locator': '(//a[@role="button"])[1]'},
    'first_row': {'type': 'xpath', 'locator': '(//a[@role="button"])[1]'},
    'upload_inp': {'type': 'css', 'locator': 'input[data-test="fileDialogControl"]'},
    'header': {'type': 'css', 'locator': 'div.versatile-header__head'},
    'footer': {'type': 'css', 'locator': '.advanced-flex-table-bottom-panel'},
    'footer_info': {'type': 'css', 'locator': '.advanced-flex-table-bottom-panel__info'},
    'footer_uncheck_btn': {'type': 'css', 'locator': 'button[data-test="uncheckAll"]'},
    'footer_delete_btn': {'type': 'css', 'locator': 'button[data-test="processCheckedItems"]'},
    'confirm_deleting_btn': {'type': 'css', 'locator': '.modal-footer button[data-test="confirm"]'},
    'cancel_deleting_btn': {'type': 'css', 'locator': '.modal-footer button[data-test="cancel"]'},
    'empty_data': {'type': 'css', 'locator': '.no-data-block'},
    'empty_data_text': {'type': 'css', 'locator': '.no-data__text'},
    'sceleton': {'type': 'css', 'locator': 'div.skeleton-item'},
    'file_name': {'type': 'css', 'locator': '.modal-body > div:nth-child(1) > div > div > div:nth-child(1)'},
    'table': {'type': 'css', 'locator': '.flex-table__body'},
    'alerts': {'type': 'css', 'locator': '[role="alert"]'},
}
