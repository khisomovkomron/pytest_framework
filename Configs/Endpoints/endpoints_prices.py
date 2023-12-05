PRICES = {

    # Excel
    "download_file": "/file",  # GET (TODO)
    "upload_file": "/file",  # POST

    # Prices
    "get_prices": "/tasks/{task_id}/prices",  # POST
    "get_filter_def": "/prices/_filterdef",  # GET
    "delete_prices": "/prices/batchDelete",  # DELETE (TODO)
    "get_product_categories": "/prices/categories",  # GET (TODO)
    "get_category_with_products": "/prices/products",  # POST (TODO)
    "get_price_details": "/prices/{price_id}/details",  # GET (TODO)
    "get_price_stages": "/prices/{price_id}/stages",  # POST (TODO)
    "get_task_prices": "/prices/{task_id}/prices",  # POST (TODO)
    "send_prices_to_1c": "/prices/{task_id}/prices/send",  # POST (TODO)


}