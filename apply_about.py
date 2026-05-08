import re

# Read original
with open('about.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Read new main
with open('new_main_about.html', 'r', encoding='utf-8') as f:
    new_main = f.read()

# 1. Title & Meta
html = re.sub(r'<title>.*?</title>', '<title>About Boscosoft Dynamics 365 Services | Microsoft CRM Implementation Partner</title>', html, flags=re.DOTALL)
if '<meta name="description"' not in html and '<meta\n      name="description"' not in html:
    html = html.replace('<title>', '<meta name="description" content="Learn about Boscosoft Technologies, an official Microsoft Dynamics 365 CRM Implementation Partner helping businesses modernize CRM, automate workflows, integrate systems, and improve operational visibility."/>\n    <title>')
else:
    html = re.sub(r'<meta[^>]*name="description"[^>]*>', '<meta name="description" content="Learn about Boscosoft Technologies, an official Microsoft Dynamics 365 CRM Implementation Partner helping businesses modernize CRM, automate workflows, integrate systems, and improve operational visibility."/>', html, flags=re.IGNORECASE)

# 2. Replace main
html = re.sub(r'<main>.*?</main>', f'<main>\n{new_main}\n    </main>', html, flags=re.DOTALL)

with open('about.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Applied about.html successfully')
