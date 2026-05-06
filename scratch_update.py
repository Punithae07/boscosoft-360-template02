import re
import os

with open('about.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Meta Title
html = re.sub(r'<title>.*?</title>', '<title>About Bosco Soft Dynamics 365 Services | Microsoft CRM Implementation Partner</title>', html, flags=re.DOTALL)

# 2. Meta Description
if '<meta name="description"' not in html and '<meta\n      name="description"' not in html:
    html = html.replace('<title>', '<meta name="description" content="Learn about Bosco Soft Technologies, an official Microsoft Dynamics 365 CRM Implementation Partner helping businesses modernize CRM, automate workflows, integrate systems, and improve operational visibility."/>\n    <title>')
else:
    html = re.sub(r'<meta[^>]*name="description"[^>]*>', '<meta name="description" content="Learn about Bosco Soft Technologies, an official Microsoft Dynamics 365 CRM Implementation Partner helping businesses modernize CRM, automate workflows, integrate systems, and improve operational visibility."/>', html, flags=re.IGNORECASE)

# 3. Banner H1 & Subheading
old_h1 = r'<h1 class="font-display-xl text-3xl sm:text-4xl lg:text-5xl font-black text-slate-950 mb-6">About Boscosoft <span class="gradient-text">Dynamics 365 Services</span></h1>'
new_h1 = r'<h1 class="font-display-xl text-3xl sm:text-4xl lg:text-5xl font-black text-slate-950 mb-6">About Bosco Soft <span class="gradient-text">Dynamics 365 Services</span></h1>\n          <p class="text-body-lg text-slate-600 max-w-2xl mx-auto">Helping organizations transform customer relationships, business processes, and decision-making with Microsoft Dynamics 365 CRM.</p>'
html = html.replace(old_h1, new_h1)

# Let's save it
with open('about.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Done!')
