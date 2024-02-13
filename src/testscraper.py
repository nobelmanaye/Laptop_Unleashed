from urllib.request import urlopen


def fetch(url):
    url = "https://store.human-i-t.org/categories/laptop/?utm_campaign=20377544399&utm_source=google&utm_medium=cpc&utm_content=675857210156&utm_term=cheap+laptops&hsa_acc=9247694287&hsa_cam=20377544399&hsa_grp=152824510033&hsa_ad=675857210156&hsa_src=g&hsa_tgt=kwd-12171621&hsa_kw=cheap+laptops&hsa_mt=b&hsa_net=adwords&hsa_ver=3&gad_source=1&gclid=Cj0KCQiAj_CrBhD-ARIsAIiMxT8EPDktS1X8He2U2Agg3lypk-CFRF78w3Nnfv4IMrHH2palqlEOEtkaAqIsEALw_wcB&page=2"
    page = urlopen(url)



    html_code = page.read()
    html = html_code.decode()
    laptops = ""

    laptops_start  = html.find('''<ul class="productGrid">''')
    i = 3
    while True:

        laptops += html[laptops_start:laptops_start+i]
        laptops_start +=i

        if "</li>" in laptops[-10:]:
            print("==================\n"*4)

            print(laptops)
            break
        if len(laptops)> 7000:
            print(laptops)
            break 
    return laptops


def extract_laptop_details_from_string(html_content):
    # Dictionary to hold extracted details
    laptop_details = {
        'name': '',
        'price': '',
        'brand': '',
        'cpu': '',
        'ram': '',
        'storage': '',
    }
    
    # Extracting details based on known markers in the string
    try:
        name_start = html_content.find('data-name="') + len('data-name="')
        name_end = html_content.find('"', name_start)
        laptop_details['name'] = html_content[name_start:name_end].replace('&quot;', '"')
        
        price_start = html_content.find('data-product-price="') + len('data-product-price="')
        price_end = html_content.find('"', price_start)
        laptop_details['price'] = html_content[price_start:price_end]
        
        brand_start = html_content.find('data-product-brand="') + len('data-product-brand="')
        brand_end = html_content.find('"', brand_start)
        laptop_details['brand'] = html_content[brand_start:brand_end]
        
        # Assuming the CPU, RAM, and Storage are part of the product name
        # Splitting by '-' and processing parts to find CPU, RAM, and SSD
        parts = laptop_details['name'].split(' - ')
        for part in parts:
            if 'GHz' in part or 'Ryzen' in part:
                laptop_details['cpu'] = part
            elif 'GB RAM' in part:
                laptop_details['ram'] = part
            elif 'SSD' in part or 'HDD' in part:
                laptop_details['storage'] = part
                
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return laptop_details


def main():
# Assuming html_content is your HTML string variable
    url = "https://store.human-i-t.org/categories/laptop/?utm_campaign=20377544399&utm_source=google&utm_medium=cpc&utm_content=675857210156&utm_term=cheap+laptops&hsa_acc=9247694287&hsa_cam=20377544399&hsa_grp=152824510033&hsa_ad=675857210156&hsa_src=g&hsa_tgt=kwd-12171621&hsa_kw=cheap+laptops&hsa_mt=b&hsa_net=adwords&hsa_ver=3&gad_source=1&gclid=Cj0KCQiAj_CrBhD-ARIsAIiMxT8EPDktS1X8He2U2Agg3lypk-CFRF78w3Nnfv4IMrHH2palqlEOEtkaAqIsEALw_wcB&page=2"
    html_content = fetch(url) # Replace this with your actual HTML content variable
    laptop_details = extract_laptop_details_from_string(html_content)
    print(laptop_details)


if __name__ == "__main__":
    main()