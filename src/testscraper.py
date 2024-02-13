from urllib.request import urlopen

url = "https://store.human-i-t.org/categories/laptop/?utm_campaign=20377544399&utm_source=google&utm_medium=cpc&utm_content=675857210156&utm_term=cheap+laptops&hsa_acc=9247694287&hsa_cam=20377544399&hsa_grp=152824510033&hsa_ad=675857210156&hsa_src=g&hsa_tgt=kwd-12171621&hsa_kw=cheap+laptops&hsa_mt=b&hsa_net=adwords&hsa_ver=3&gad_source=1&gclid=Cj0KCQiAj_CrBhD-ARIsAIiMxT8EPDktS1X8He2U2Agg3lypk-CFRF78w3Nnfv4IMrHH2palqlEOEtkaAqIsEALw_wcB&page=2"
page = urlopen(url)



html_code = page.read()
html = html_code.decode()


laptops_start  = html.find('''<ul class="productGrid">''')

laptops = html[laptops_start+1:laptops_start+1000]

print(laptops)