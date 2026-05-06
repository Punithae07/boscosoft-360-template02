import re

html_template = """      <section class="soft-gradient-section relative overflow-hidden pt-32 pb-20">
        <div class="hero-grid absolute inset-0"></div>
        <div class="relative z-10 max-w-5xl mx-auto px-8 text-center" data-aos="fade-up">
          <div class="eyebrow-pill mb-6">
            <span class="material-symbols-outlined text-sm text-violet-700">domain</span>
            <span class="text-label-md font-semibold text-slate-700">Industries</span>
          </div>
          <h1 class="font-display-xl text-3xl sm:text-4xl lg:text-5xl font-black text-slate-950 mb-6">Industry-Focused <span class="gradient-text">Dynamics 365 CRM Solutions</span></h1>
          <p class="text-xl text-slate-600 leading-relaxed max-w-3xl mx-auto mb-4">
            Bosco Soft helps organizations across industries implement Dynamics 365 CRM solutions tailored to their workflows, customer journeys, service models, and growth plans.
          </p>
        </div>
      </section>

      <!-- Industries Intro Section -->
      <section class="py-16 bg-white relative z-10 text-center">
        <div class="max-w-4xl mx-auto px-8" data-aos="fade-up">
          <h2 class="font-headline-md text-3xl font-bold text-slate-950 mb-6">CRM Solutions Designed Around the Way Your Industry Works</h2>
          <p class="text-body-lg text-slate-600 mb-4">Every industry has its own challenges. A healthcare organization may need better patient engagement. An education institution may need student lifecycle management. A nonprofit may need donor visibility. A manufacturing company may need dealer coordination and after-sales support. A sales-driven business may need pipeline control and performance reporting.</p>
          <p class="text-body-lg text-slate-600 mb-4">Bosco Soft helps you configure Dynamics 365 around your industry realities, so your CRM platform supports better execution, clearer data, improved service, and long-term growth.</p>
          <p class="text-body-lg text-slate-600">We do not just deploy technology. We align Dynamics 365 with your business model, customer relationships, operational workflows, and reporting needs.</p>
        </div>
      </section>

      <section class="py-16 bg-white relative z-10">
        <div class="max-w-7xl mx-auto px-8">
          <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
            {industries_html}
          </div>
        </div>
      </section>

      <!-- Industries Page CTA Section -->
      <section class="py-24 bg-gradient-to-br from-violet-900 to-slate-900 relative overflow-hidden text-center">
        <div class="absolute inset-0 bg-[url('assets/dash02.jpg')] bg-cover bg-center opacity-10 mix-blend-overlay"></div>
        <div class="relative z-10 max-w-4xl mx-auto px-8" data-aos="fade-up">
          <h2 class="font-display-xl text-3xl md:text-5xl font-bold text-white mb-6">Need a Dynamics 365 Solution Tailored to Your Industry?</h2>
          <p class="text-xl text-violet-100 mb-10 max-w-2xl mx-auto">Bosco Soft can help you design and implement a CRM platform that fits your customer journey, team structure, workflows, and growth goals.</p>
          <div class="flex flex-col sm:flex-row items-center justify-center gap-4">
            <a href="contact.html" class="rounded-full bg-white px-8 py-4 font-bold text-violet-900 shadow-lg transition hover:-translate-y-1 hover:shadow-xl w-full sm:w-auto">Book an Industry Consultation</a>
            <a href="contact.html" class="rounded-full border border-violet-200/30 bg-violet-800/30 px-8 py-4 font-bold text-white backdrop-blur-sm transition hover:bg-violet-800/50 w-full sm:w-auto">Talk to Our CRM Experts</a>
          </div>
        </div>
      </section>
"""

industries_data = [
    {
        "color": "rose", "icon": "fa-heart-pulse",
        "title": "Healthcare and Life Sciences",
        "desc": "Improve patient engagement, care coordination, service communication, and operational visibility with secure and structured CRM workflows.",
        "use_cases": ["Patient and enquiry management", "Appointment and follow-up workflows", "Service request tracking", "Referral management", "Communication automation", "Department-wise reporting", "Patient engagement dashboards"],
        "value": "Better coordination, faster response, stronger patient relationships, and improved operational visibility."
    },
    {
        "color": "sky", "icon": "fa-graduation-cap",
        "title": "Education and EdTech",
        "desc": "Manage student enquiries, admissions, engagement, communications, and alumni relationships through a connected CRM experience.",
        "use_cases": ["Student enquiry management", "Admissions pipeline tracking", "Counselling and follow-up workflows", "Parent and student communication", "Course or program interest tracking", "Alumni engagement", "Student lifecycle dashboards"],
        "value": "Improved admissions efficiency, better engagement, stronger communication, and complete lifecycle visibility."
    },
    {
        "color": "emerald", "icon": "fa-hands-holding-circle",
        "title": "Nonprofits and NGOs",
        "desc": "Improve donor engagement, fundraising coordination, program visibility, beneficiary tracking, and reporting transparency.",
        "use_cases": ["Donor and supporter management", "Fundraising campaign tracking", "Volunteer coordination", "Beneficiary data management", "Grant and program tracking", "Impact reporting dashboards", "Automated donor communication"],
        "value": "Better stakeholder engagement, improved reporting, stronger donor relationships, and more efficient operations."
    },
    {
        "color": "indigo", "icon": "fa-scale-balanced",
        "title": "Professional Services",
        "desc": "Help consulting, legal, accounting, and advisory firms manage client relationships, opportunities, projects, and service delivery with better visibility.",
        "use_cases": ["Client relationship management", "Opportunity and proposal tracking", "Project pipeline visibility", "Engagement history", "Follow-up automation", "Resource and task coordination", "Client service dashboards"],
        "value": "Stronger client relationships, improved pipeline management, better service tracking, and more organized delivery."
    },
    {
        "color": "amber", "icon": "fa-industry",
        "title": "Manufacturing",
        "desc": "Connect sales, dealers, customers, operations, and after-sales service through a CRM platform designed for better coordination and visibility.",
        "use_cases": ["Dealer and distributor management", "B2B sales pipeline tracking", "Customer enquiry management", "Service request and warranty tracking", "Demand and opportunity visibility", "After-sales support workflows", "Sales and operations dashboards"],
        "value": "Improved coordination, stronger customer service, better channel visibility, and more reliable sales tracking."
    },
    {
        "color": "violet", "icon": "fa-store",
        "title": "Retail and E-commerce",
        "desc": "Create better customer engagement, personalized communication, omnichannel visibility, and customer loyalty through connected CRM workflows.",
        "use_cases": ["Customer profile management", "Enquiry and complaint tracking", "Loyalty and retention workflows", "Order-related communication", "Campaign follow-ups", "Customer segmentation", "Sales and service reporting"],
        "value": "More personalized customer experiences, improved service response, higher retention, and better sales visibility."
    },
    {
        "color": "blue", "icon": "fa-building-columns",
        "title": "Banking, Financial Services, and Insurance",
        "desc": "Strengthen customer relationships, lead management, service workflows, compliance visibility, and data-driven decision-making with a secure CRM platform.",
        "use_cases": ["Lead and customer lifecycle management", "Relationship manager workflows", "Policy or product enquiry tracking", "Service request management", "Compliance-related activity tracking", "Renewal and reminder workflows", "Customer and portfolio dashboards"],
        "value": "Improved relationship management, better process control, stronger customer visibility, and more efficient follow-ups."
    },
    {
        "color": "orange", "icon": "fa-helmet-safety",
        "title": "Real Estate and Construction",
        "desc": "Track leads, projects, site visits, property enquiries, customer communication, and sales pipelines across multiple locations and teams.",
        "use_cases": ["Property enquiry management", "Site visit scheduling", "Lead assignment and follow-up", "Project-wise sales pipeline tracking", "Customer document tracking", "Broker and partner coordination", "Sales performance dashboards"],
        "value": "Better lead conversion, improved customer communication, stronger project visibility, and more organized sales management."
    },
    {
        "color": "cyan", "icon": "fa-plane-departure",
        "title": "Travel, Hospitality, and Leisure",
        "desc": "Deliver more personalized customer experiences by managing enquiries, bookings, preferences, service interactions, and loyalty engagement.",
        "use_cases": ["Customer enquiry and booking workflows", "Guest preference tracking", "Service request management", "Feedback and complaint tracking", "Personalized follow-up communication", "Loyalty and retention campaigns", "Customer experience dashboards"],
        "value": "Better customer engagement, improved service consistency, stronger retention, and more informed guest experiences."
    },
    {
        "color": "purple", "icon": "fa-microchip",
        "title": "Technology and SaaS Companies",
        "desc": "Support growth with CRM systems that manage sales pipelines, customer onboarding, support requests, renewals, and customer success workflows.",
        "use_cases": ["B2B lead and opportunity tracking", "Demo request management", "Customer onboarding workflows", "Subscription renewal follow-ups", "Support ticket visibility", "Customer success tracking", "SaaS performance dashboards"],
        "value": "Better sales execution, improved onboarding, stronger retention, and clearer customer success visibility."
    },
    {
        "color": "emerald", "icon": "fa-chart-line",
        "title": "Sales-Driven Organizations",
        "desc": "Empower sales teams with better lead tracking, pipeline visibility, activity management, forecasting, automation, and performance reporting.",
        "use_cases": ["Lead capture and qualification", "Sales pipeline management", "Opportunity tracking", "Sales activity planning", "Follow-up reminders", "Quote and proposal tracking", "Sales dashboards and forecasting"],
        "value": "Faster follow-ups, stronger pipeline control, better forecasting, and improved sales productivity."
    },
    {
        "color": "sky", "icon": "fa-headset",
        "title": "Customer Service and Contact Centers",
        "desc": "Deliver faster resolutions, improve agent productivity, and create more consistent customer service experiences with unified case management.",
        "use_cases": ["Case and ticket management", "SLA tracking", "Escalation workflows", "Customer communication history", "Knowledge support workflows", "Service dashboards", "Agent performance reporting"],
        "value": "Faster service response, improved accountability, better customer satisfaction, and stronger operational visibility."
    },
    {
        "color": "indigo", "icon": "fa-map-location-dot",
        "title": "Multi-Location and Franchise Businesses",
        "desc": "Maintain visibility and control across multiple branches, locations, franchise units, and regional teams while enabling local customer engagement.",
        "use_cases": ["Location-wise lead and customer tracking", "Franchise communication workflows", "Regional reporting dashboards", "Branch performance visibility", "Standardized sales and service processes", "Escalation and support workflows", "Role-based access by location"],
        "value": "Consistent operations, better management visibility, improved branch accountability, and scalable customer engagement."
    },
    {
        "color": "amber", "icon": "fa-gears",
        "title": "Process-Intensive Enterprises",
        "desc": "Optimize complex workflows, approvals, service requests, internal coordination, and data-driven decision-making with structured CRM and automation.",
        "use_cases": ["Multi-step approval workflows", "Cross-department process tracking", "Task and escalation automation", "Internal request management", "Data validation and governance", "Performance dashboards", "Process improvement reporting"],
        "value": "Reduced manual effort, better process control, improved visibility, and stronger operational efficiency."
    }
]

industries_html_parts = []
for idx, item in enumerate(industries_data):
    delay = f' data-aos-delay="{100 * (idx % 3)}"' if idx % 3 != 0 else ''
    color = item["color"]
    
    use_cases_lis = "".join([f'<li class="flex items-start gap-2"><i class="fa-solid fa-check text-{color}-500 mt-1 shrink-0 text-xs"></i> <span>{uc}</span></li>' for uc in item["use_cases"]])

    block = f"""
            <div class="glass-card flex flex-col rounded-[24px] p-8 border-none bg-gradient-to-br from-slate-50 to-white shadow-lg hover:shadow-xl hover:-translate-y-1 transition-all duration-300" data-aos="fade-up"{delay}>
              <i class="fa-solid {item['icon']} text-3xl text-{color}-500 mb-4"></i>
              <h3 class="text-xl font-bold text-slate-900 mb-3">{item['title']}</h3>
              <p class="text-slate-600 text-sm leading-relaxed mb-4">{item['desc']}</p>
              
              <div class="mb-4">
                  <p class="font-bold text-slate-800 text-xs uppercase tracking-wider mb-2">Use Cases</p>
                  <ul class="space-y-1.5 text-sm text-slate-600">
                    {use_cases_lis}
                  </ul>
              </div>
              
              <div class="mt-auto pt-4 border-t border-slate-100">
                  <p class="font-bold text-{color}-700 text-xs uppercase tracking-wider mb-1">Business Value</p>
                  <p class="text-slate-600 text-sm font-medium">{item['value']}</p>
              </div>
            </div>
"""
    industries_html_parts.append(block)

final_main = html_template.replace("{industries_html}", "".join(industries_html_parts))

with open('industries.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace Title & Meta
html = re.sub(r'<title>.*?</title>', '<title>Dynamics 365 CRM Solutions by Industry | Bosco Soft Technologies</title>', html, flags=re.DOTALL)

if '<meta name="description"' not in html and '<meta\n      name="description"' not in html:
    html = html.replace('<title>', '<meta name="description" content="Bosco Soft delivers industry-focused Microsoft Dynamics 365 CRM solutions for healthcare, education, nonprofits, professional services, manufacturing, retail, BFSI, real estate, travel, SaaS, sales teams, contact centers, and process-intensive enterprises."/>\n    <title>')
else:
    html = re.sub(r'<meta[^>]*name="description"[^>]*>', '<meta name="description" content="Bosco Soft delivers industry-focused Microsoft Dynamics 365 CRM solutions for healthcare, education, nonprofits, professional services, manufacturing, retail, BFSI, real estate, travel, SaaS, sales teams, contact centers, and process-intensive enterprises."/>', html, flags=re.IGNORECASE)

# Replace <main>
html = re.sub(r'<main>.*?</main>', f'<main>\n{final_main}\n    </main>', html, flags=re.DOTALL)

with open('industries.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Updated industries.html')
