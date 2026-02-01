URL = 'https://www.youtube.com'

protocol = URL[:URL.index('://')]
web_site_name = URL[URL.index('www.')+4:URL.index('.com')]
domain = URL[URL.rindex(".")+1:]



print(f"Domain extention : {protocol}")
print(f"The web site name : {web_site_name}")
print(f"Your domain extension : {domain}")