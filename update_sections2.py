import re

with open('c:/Users/SANJI BI/OneDrive/Documents/ssp/boscosoft-360/template2/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Services Snapshot Section
content = content.replace('Key Services Snapshot', 'Our Dynamics 365 Services')
content = content.replace('Our Dynamics 365 Services\n            <span class="gradient-text">Our Dynamics 365 Services</span>', 'Our Dynamics 365 Services')
content = content.replace('Focused capabilities for planning, building, integrating, training, and scaling your Dynamics 365 CRM ecosystem.', 'Bosco Soft provides end-to-end Dynamics 365 services to help businesses plan, implement, customize, integrate, automate, and optimize their CRM and Microsoft business applications.')

# Replace Service Card descriptions
content = content.replace('Strategy, roadmap, process mapping, and CRM advisory for the right\n              implementation path.', 'Make smarter platform decisions with expert guidance on CRM strategy, process mapping, module selection, solution architecture, and implementation planning.')
content = content.replace('End-to-end deployment of sales, service, and operational CRM\n              modules.', 'Deploy Dynamics 365 with confidence through structured setup, configuration, security planning, testing, user readiness, and go-live support.')
content = content.replace('Tailored entities, forms, views, workflows, security roles, and\n              user experiences.', 'Adapt Dynamics 365 to your business processes with custom tables, forms, views, dashboards, business rules, workflows, and role-based user experiences.')

content = content.replace('Workflow Automation with Power Automate', 'Workflow Automation')
content = content.replace('Automated approvals, notifications, follow-ups, and low-code\n              process orchestration.', 'Use Power Automate and Dynamics 365 workflows to reduce manual work, automate approvals, trigger notifications, route records, and improve process consistency.')

content = content.replace('Clean data modeling, relationships, governance, and scalable CRM\n              foundations.', 'Build a secure, scalable, and well-structured business data foundation with Microsoft Dataverse table design, relationships, governance, and access planning.')

content = content.replace('Interactive dashboards, KPI reporting, and insight layers for\n              faster decisions.', 'Turn CRM and operational data into clear dashboards, executive reports, performance metrics, and decision-ready insights.')

content = content.replace('Copilot Studio and Intelligent Bot Solutions', 'Copilot Studio and AI-Assisted Experiences')
content = content.replace('AI assistants, conversational flows, and service automation built\n              for CRM data.', 'Create intelligent conversational experiences, support bots, self-service journeys, and AI-powered agents connected with business workflows.')

content = content.replace('System Integration and Migration', 'Integration and Migration')
content = content.replace('Connect ERP, legacy systems, marketing tools, and migrate data\n              with care.', 'Connect Dynamics 365 with Microsoft 365, Teams, Outlook, Azure, APIs, third-party tools, legacy applications, and existing business data sources.')

content = content.replace('Role-based enablement, adoption support, issue resolution, and\n              continuous improvement.', 'Improve adoption with administrator training, user training, documentation, troubleshooting, enhancements, and continuous optimization.')

# Add a CTA button to Services section if it doesn't exist
if 'Explore Our Services' not in content:
    services_cta = '''
        <div class="mt-12 text-center">
            <button class="rounded-full bg-gradient-to-b from-[#6f4dcc] to-[#56329f] px-9 py-4 font-headline-md text-body-md font-bold text-white shadow-xl shadow-violet-900/20 transition-all duration-300 hover:-translate-y-1">
                Explore Our Services
            </button>
        </div>
      </section>
      <!-- Industries Section -->'''
    content = content.replace('      </section>\n      <!-- Industries Section -->', services_cta)

# 2. Industries Section
content = content.replace('15 Verticals,\n                <span class="gradient-text">One CRM Platform</span>', 'Industry-Focused <span class="gradient-text">Dynamics 365 Solutions</span>')
content = content.replace('We help businesses across industries implement Dynamics 365\n                solutions that fit their workflows, service models, and growth\n                plans.', 'Every industry has different customer journeys, service models, data needs, compliance expectations, and operational workflows. Bosco Soft helps organizations configure Dynamics 365 around the way their industry works.')

# I will replace the industries track entirely to contain the 14 industries
industries_html = '''
                <div class="industry-track">
'''
industries = [
    "Healthcare and Life Sciences", "Education and EdTech", "Nonprofits and NGOs",
    "Professional Services", "Manufacturing", "Retail and E-commerce",
    "Banking, Financial Services, and Insurance", "Real Estate and Construction",
    "Travel, Hospitality, and Leisure", "Technology and SaaS Companies",
    "Sales-Driven Organizations", "Customer Service and Contact Centers",
    "Multi-Location and Franchise Businesses", "Process-Intensive Enterprises"
]
for ind in industries:
    industries_html += f'''
                  <article class="industry-card glass-card overflow-hidden rounded-[28px] border border-white/80 shadow-sm flex items-center justify-center bg-white/50 min-h-[120px] p-6 text-center">
                    <h3 class="text-lg font-bold text-slate-950">
                      {ind}
                    </h3>
                  </article>'''

industries_html += '''
                </div>'''

content = re.sub(r'<div class="industry-track">.*?</div>\n              </div>', industries_html + '\n              </div>', content, flags=re.DOTALL)

if 'View Industry Solutions' not in content:
    industry_cta = '''
            <div class="mt-10 text-center">
                <button class="rounded-full border border-violet-200 bg-white/70 px-9 py-4 font-headline-md text-body-md font-bold text-slate-800 shadow-lg shadow-violet-100/40 backdrop-blur-xl transition-all duration-300 hover:-translate-y-1 hover:bg-white">
                    View Industry Solutions
                </button>
            </div>
          </div>
        </div>
      </section>'''
    content = re.sub(r'          </div>\n        </div>\n      </section>', industry_cta, content, count=1)


# 3. Implementation Approach
content = content.replace('Process-led Planning with\n            <span class="gradient-text">Intelligent Delivery</span>', 'A Structured Implementation Approach\n            <span class="gradient-text">Designed to Reduce Risk</span>')
content = content.replace('Our Implementation Approach combines process-led planning with\n            intelligent Dynamics 365 delivery. We follow a connected strategy of\n            analytics, design, deployment, and support.', 'A successful Dynamics 365 project needs more than software configuration. It requires business alignment, clear requirements, strong data design, testing discipline, user training, and post-launch optimization.')

# Steps
content = content.replace('Stakeholder workshops, process mapping, and business\n                    requirement capture.', 'We understand your current systems, business processes, customer journeys, reporting gaps, pain points, and transformation goals.')

content = content.replace('Audit</h4>', 'Design</h4>')
content = content.replace('Review current systems, data readiness, and integration\n                    needs.', 'We define the solution architecture, data model, workflows, security structure, integrations, dashboards, and delivery roadmap.')

content = content.replace('Implement</h4>', 'Configure and Customize</h4>')
content = content.replace('Configure modules, build automations, and integrate Dynamics\n                    365 with your ecosystem.', 'We build the Dynamics 365 environment, configure modules, create custom components, automate workflows, and prepare integrations.')

content = content.replace('>Train</h4>', '>Test and Validate</h4>')
content = content.replace('Enable users, coaches, and administrators with tailored\n                    training and support materials.', 'We test business flows, user roles, automation, data quality, reports, integrations, and readiness before launch.')

content = content.replace('>Support</h4>', '>Train and Launch</h4>')
content = content.replace('Ongoing maintenance, change management, and solution\n                    enhancement planning.', 'We support administrators and end users with training, documentation, go-live readiness, and transition assistance.')

# Add a 6th step to this layout
step6 = '''
              <div class="flex gap-4 items-start">
                <div class="wire-point flex h-14 w-14 items-center justify-center rounded-full bg-white text-violet-700 font-bold shadow-lg">
                  6
                </div>
                <div>
                  <h4 class="font-bold text-slate-950">Support and Optimize</h4>
                  <p class="mt-2 text-sm text-slate-600">
                    After launch, we help monitor adoption, resolve issues, refine processes, plan enhancements, and improve platform performance.
                  </p>
                </div>
              </div>
            </div>
'''
content = content.replace('transition assistance.\n                  </p>\n                </div>\n              </div>\n            </div>', 'transition assistance.\n                  </p>\n                </div>\n              </div>' + step6)

# Update CTA for Implementation
content = content.replace('Our Implementation Approach</h4>', 'A clean delivery model for enterprise CRM success.</h3>') # Fix context if needed
if 'Start Your Implementation Journey' not in content:
    impl_cta = '''
        <div class="mt-12 text-center">
            <button class="rounded-full bg-gradient-to-b from-[#6f4dcc] to-[#56329f] px-9 py-4 font-headline-md text-body-md font-bold text-white shadow-xl shadow-violet-900/20 transition-all duration-300 hover:-translate-y-1">
                Start Your Implementation Journey
            </button>
        </div>
      </section>
      <!-- Implementation Approach -->'''
    content = content.replace('      </section>\n\n      <!-- Implementation Approach -->', impl_cta)

with open('c:/Users/SANJI BI/OneDrive/Documents/ssp/boscosoft-360/template2/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
