import re

html_template = """      <!-- Hero Banner -->
      <section class="soft-gradient-section relative overflow-hidden pt-32 pb-20">
        <div class="hero-grid absolute inset-0"></div>
        <div class="absolute left-1/2 top-28 h-72 w-72 -translate-x-1/2 rounded-full bg-violet-300/30 blur-3xl"></div>
        <div class="relative z-10 max-w-5xl mx-auto px-8 text-center" data-aos="fade-up">
          <div class="eyebrow-pill mb-6">
            <span class="material-symbols-outlined text-sm text-violet-700">widgets</span>
            <span class="text-label-md font-semibold text-slate-700">Our Services</span>
          </div>
          <h1 class="font-display-xl text-3xl sm:text-4xl lg:text-5xl font-black text-slate-950 mb-6">Microsoft Dynamics 365 Services for <span class="gradient-text">CRM Transformation and Business Growth</span></h1>
          <p class="text-xl text-slate-600 leading-relaxed max-w-3xl mx-auto">
            End-to-end Dynamics 365 consulting, implementation, customization, automation, integration, reporting, training, and support from an official Microsoft Dynamics 365 CRM Implementation Partner.
          </p>
        </div>
      </section>

      <!-- Services Intro Section -->
      <section class="py-16 bg-white relative z-10 text-center">
        <div class="max-w-4xl mx-auto px-8" data-aos="fade-up">
          <h2 class="font-headline-md text-3xl font-bold text-slate-950 mb-6">Build, Launch, and Scale Dynamics 365 with Confidence</h2>
          <p class="text-body-lg text-slate-600 mb-4">Bosco Soft provides complete Dynamics 365 services designed to help organizations adopt Microsoft CRM successfully and continue improving it over time.</p>
          <p class="text-body-lg text-slate-600 mb-4">From early-stage consulting and solution planning to advanced customization, workflow automation, Power BI dashboards, system integration, data migration, user training, and post-go-live support, we help you get the most from your Dynamics 365 investment.</p>
          <p class="text-body-lg text-slate-600">Our services are designed for businesses that want a CRM platform that is not only technically correct, but also practical, user-friendly, scalable, and aligned with real business outcomes.</p>
        </div>
      </section>

      <!-- Services Grid -->
      <section class="py-12 bg-white relative z-10">
        <div class="max-w-7xl mx-auto px-8">
          <div class="grid md:grid-cols-2 lg:grid-cols-2 gap-8">
            {services_html}
          </div>
        </div>
      </section>

      <!-- Services Page Closing CTA -->
      <section class="py-24 bg-gradient-to-br from-violet-900 to-slate-900 relative overflow-hidden text-center">
        <div class="absolute inset-0 bg-[url('assets/dash01.jpg')] bg-cover bg-center opacity-10 mix-blend-overlay"></div>
        <div class="relative z-10 max-w-4xl mx-auto px-8" data-aos="fade-up">
          <h2 class="font-display-xl text-3xl md:text-5xl font-bold text-white mb-6">Need Help Planning or Improving Your Dynamics 365 CRM?</h2>
          <p class="text-xl text-violet-100 mb-10 max-w-2xl mx-auto">Whether you are starting from scratch, replacing a legacy CRM, automating workflows, improving reporting, or optimizing an existing Dynamics 365 environment, Bosco Soft can help.</p>
          <div class="flex flex-col sm:flex-row items-center justify-center gap-4">
            <a href="contact.html" class="rounded-full bg-white px-8 py-4 font-bold text-violet-900 shadow-lg transition hover:-translate-y-1 hover:shadow-xl w-full sm:w-auto">Book a Consultation</a>
            <a href="contact.html" class="rounded-full border border-violet-200/30 bg-violet-800/30 px-8 py-4 font-bold text-white backdrop-blur-sm transition hover:bg-violet-800/50 w-full sm:w-auto">Request a CRM Assessment</a>
          </div>
        </div>
      </section>
"""

services_data = [
    {
        "color": "violet",
        "icon": "fa-lightbulb",
        "h2": "Dynamics 365 Consulting",
        "h3": "Strategic CRM consulting for smarter platform decisions",
        "desc": "Dynamics 365 delivers the best results when it is implemented with a clear business strategy. Bosco Soft helps you assess your current processes, identify improvement opportunities, and define a practical Dynamics 365 roadmap. We guide your team through important decisions such as module selection, data structure, workflow design, reporting needs, integration priorities, user roles, and implementation phases.",
        "cover_title": "What We Cover",
        "covers": ["CRM readiness assessment", "Business process analysis", "Current system and data review", "Functional requirement gathering", "Solution architecture planning", "Module selection guidance", "Implementation roadmap creation", "Automation and reporting opportunity mapping", "Licensing and adoption considerations"],
        "outcomes_title": "Business Outcomes",
        "outcomes": ["Better clarity before implementation", "Reduced project risk", "Improved stakeholder alignment", "More realistic project scope and timelines", "A CRM roadmap connected to business goals"],
        "cta": "Request Dynamics 365 Consulting"
    },
    {
        "color": "sky",
        "icon": "fa-rocket",
        "h2": "Dynamics 365 Implementation",
        "h3": "Structured implementation for a successful CRM launch",
        "desc": "Bosco Soft designs and implements Dynamics 365 CRM solutions that fit your business processes, user roles, reporting needs, and future growth plans. Our implementation approach focuses on clear configuration, reliable security design, user-friendly workflows, testing discipline, and smooth go-live support. We help you move from planning to launch with confidence.",
        "cover_title": "Our Implementation Services Include",
        "covers": ["Dynamics 365 environment setup", "Module configuration", "Sales, service, and CRM process setup", "Role and security configuration", "Business process mapping", "Data model and table setup", "Workflow and automation configuration", "Dashboard and reporting setup", "Testing and issue resolution", "User readiness planning", "Go-live and transition support"],
        "outcomes_title": "Business Outcomes",
        "outcomes": ["Faster CRM adoption", "Better process control", "Improved user productivity", "Stronger customer data visibility", "A scalable foundation for future enhancements"],
        "cta": "Get Implementation Support"
    },
    {
        "color": "indigo",
        "icon": "fa-sliders",
        "h2": "Dynamics 365 CRM Customization and Configuration",
        "h3": "Adapt Dynamics 365 to the way your business works",
        "desc": "No two businesses operate in exactly the same way. Bosco Soft customizes and configures Dynamics 365 so it reflects your actual processes, data flows, approval rules, reporting needs, and team responsibilities. We focus on practical customization that improves usability without creating unnecessary complexity.",
        "cover_title": "Capabilities",
        "covers": ["Custom tables, fields, forms, and views", "Business rules and validations", "Business process flows", "Workflow configuration", "Role-based access and permissions", "Custom dashboards and charts", "Approval flows and notifications", "Custom user experiences", "Data capture improvements", "Process-specific CRM screens"],
        "outcomes_title": "Business Outcomes",
        "outcomes": ["CRM workflows aligned with your operations", "Better data quality and consistency", "Easier user adoption", "Reduced manual effort", "Improved management visibility"],
        "cta": "Customize Your CRM"
    },
    {
        "color": "fuchsia",
        "icon": "fa-wand-magic-sparkles",
        "h2": "Workflow Automation with Dynamics 365 and Power Automate",
        "h3": "Reduce manual work and improve process consistency",
        "desc": "Manual tasks slow teams down and create room for missed follow-ups, delayed approvals, and inconsistent customer experiences. Bosco Soft helps businesses automate repetitive CRM and operational workflows using Dynamics 365 and Power Automate. We design automations that support real business processes while keeping users informed and in control.",
        "cover_title": "Automation Examples",
        "covers": ["Lead assignment and follow-up workflows", "Opportunity stage updates and reminders", "Service request routing and escalation", "Email notifications and task creation", "Approval workflows", "Customer onboarding workflows", "Renewal and reminder workflows", "Referral and partner workflows", "Internal handoff processes", "Cross-system triggers and updates"],
        "outcomes_title": "Business Outcomes",
        "outcomes": ["Less manual effort", "Faster response times", "Improved process compliance", "Better team accountability", "More consistent customer engagement"],
        "cta": "Automate Your CRM Workflows"
    },
    {
        "color": "emerald",
        "icon": "fa-database",
        "h2": "Dataverse Data Architecture and Design",
        "h3": "Build your CRM on a secure and scalable business data foundation",
        "desc": "Microsoft Dataverse provides the data foundation for Dynamics 365 and Power Platform solutions. Bosco Soft helps organizations design clean, scalable, and secure data structures that support reliable CRM operations, automation, reporting, and integrations. Good data architecture makes your CRM easier to manage, easier to report on, and easier to scale.",
        "cover_title": "Our Dataverse Services Include",
        "covers": ["Data model design", "Table architecture", "Relationship mapping", "Schema setup", "Data validation planning", "Role-based security planning", "Business rules and logic support", "Integration-ready data structures", "Data governance guidance", "Reporting-ready data design"],
        "outcomes_title": "Business Outcomes",
        "outcomes": ["Cleaner and more reliable CRM data", "Stronger security and access control", "Easier reporting and analytics", "Scalable architecture for future applications", "Reduced data duplication and confusion"],
        "cta": "Plan Your CRM Data Architecture"
    },
    {
        "color": "amber",
        "icon": "fa-chart-pie",
        "h2": "Power BI Dashboards and Dynamics 365 Reporting",
        "h3": "Turn CRM and business data into decision-ready insight",
        "desc": "A CRM system becomes more valuable when leaders and teams can clearly see what is happening. Bosco Soft creates dashboards and reports that help organizations track performance, monitor activity, measure outcomes, and make faster decisions. We help connect Dynamics 365 data with Power BI and reporting views that are clear, useful, and aligned with business goals.",
        "cover_title": "Reporting Use Cases",
        "covers": ["Sales pipeline dashboards", "Lead conversion reports", "Opportunity performance analysis", "Customer service dashboards", "Case resolution and SLA metrics", "Workflow status tracking", "Operational dashboards", "Executive summary reports", "Department-specific analytics", "Forecasting and performance visibility"],
        "outcomes_title": "Business Outcomes",
        "outcomes": ["Better management visibility", "Faster decision-making", "Improved sales and service tracking", "Clearer performance accountability", "Data-driven business planning"],
        "cta": "Build Better CRM Dashboards"
    },
    {
        "color": "rose",
        "icon": "fa-robot",
        "h2": "Copilot Studio and AI-Assisted CRM Experiences",
        "h3": "Create intelligent conversations, self-service journeys, and AI-powered support experiences",
        "desc": "Microsoft Copilot Studio helps organizations build AI-assisted agents and conversational experiences that can support users, answer common questions, guide service journeys, and connect with business workflows. Bosco Soft helps businesses plan, design, build, and optimize Copilot Studio solutions that integrate with Dynamics 365 and the wider Microsoft ecosystem.",
        "cover_title": "What We Deliver",
        "covers": ["AI agent and bot strategy", "Conversation flow planning", "FAQ and self-service design", "Dynamics 365 integration", "Customer support and internal helpdesk experiences", "Routing and handoff logic", "Knowledge source planning", "Testing and optimization", "Continuous improvement support"],
        "outcomes_title": "Business Outcomes",
        "outcomes": ["Faster access to information", "Improved customer and employee self-service", "Reduced repetitive support effort", "Smarter service routing", "Enhanced digital experience"],
        "cta": "Explore AI-Assisted CRM Solutions"
    },
    {
        "color": "cyan",
        "icon": "fa-plug-circle-bolt",
        "h2": "Dynamics 365 Integration Services",
        "h3": "Connect Dynamics 365 with your business ecosystem",
        "desc": "A powerful CRM platform should not operate in isolation. Bosco Soft helps connect Dynamics 365 with the systems your teams already use so information can move more smoothly across the organization. We support integration planning and implementation across Microsoft tools, external platforms, APIs, legacy systems, and business applications.",
        "cover_title": "Integration Areas",
        "covers": ["Microsoft 365", "Outlook and Teams", "Power Platform", "Power BI", "Azure services", "APIs and web services", "Third-party applications", "Legacy systems", "Websites and portals", "External databases"],
        "outcomes_title": "Business Outcomes",
        "outcomes": ["Reduced duplicate data entry", "Improved collaboration across systems", "Better process continuity", "More complete customer visibility", "A connected digital business environment"],
        "cta": "Connect Your Business Systems"
    },
    {
        "color": "blue",
        "icon": "fa-server",
        "h2": "Dynamics 365 Data Migration and CRM Modernization",
        "h3": "Move your existing customer and business data into Dynamics 365 with confidence",
        "desc": "Migrating data from spreadsheets, legacy CRMs, databases, or disconnected applications requires careful planning. Bosco Soft helps organizations prepare, clean, map, migrate, and validate business data for Dynamics 365. We help reduce migration risk by focusing on data quality, structure, security, and usability.",
        "cover_title": "Migration Services Include",
        "covers": ["Source data review", "Data mapping and migration planning", "Data cleanup guidance", "Import templates and transformation logic", "Test migration", "Data validation", "Duplicate management support", "Post-migration review", "Legacy CRM modernization support"],
        "outcomes_title": "Business Outcomes",
        "outcomes": ["Smoother transition to Dynamics 365", "Better data quality at launch", "Reduced migration errors", "Improved user confidence", "More reliable reporting from day one"],
        "cta": "Plan Your CRM Migration"
    },
    {
        "color": "teal",
        "icon": "fa-chalkboard-user",
        "h2": "Dynamics 365 Training and Post-Go-Live Support",
        "h3": "Drive adoption with practical training and reliable support",
        "desc": "Technology creates value only when people use it well. Bosco Soft helps administrators, managers, and end users understand how to use Dynamics 365 effectively in their daily work. We provide training, documentation, troubleshooting, enhancement planning, and ongoing support to help your CRM platform continue delivering value after launch.",
        "cover_title": "Support Includes",
        "covers": ["Administrator training", "End-user training", "Role-based user guidance", "Process documentation", "Troubleshooting support", "Configuration refinements", "Workflow enhancements", "Dashboard improvements", "Adoption monitoring support", "Ongoing optimization planning"],
        "outcomes_title": "Business Outcomes",
        "outcomes": ["Improved user adoption", "Fewer process gaps", "Faster issue resolution", "Better internal confidence", "Long-term CRM success"],
        "cta": "Get Dynamics 365 Support"
    }
]

services_html_parts = []
for idx, s in enumerate(services_data):
    color = s["color"]
    delay = ' data-aos-delay="100"' if idx % 2 != 0 else ''
    
    cover_lis = "".join([f'<li class="flex items-center gap-2"><i class="fa-solid fa-check text-{color}-500 mt-1 shrink-0"></i> <span>{c}</span></li>' for c in s["covers"]])
    outcomes_lis = "".join([f'<li class="flex items-center gap-2"><i class="fa-solid fa-arrow-right text-{color}-500 mt-1 shrink-0"></i> <span>{o}</span></li>' for o in s["outcomes"]])

    block = f"""
            <!-- Service {idx+1} -->
            <div class="glass-card rounded-[32px] p-8 border-none bg-gradient-to-br from-{color}-50/50 to-white hover:bg-{color}-50 hover:shadow-2xl transition-all duration-300 group flex flex-col h-full" data-aos="fade-up"{delay}>
              <div class="flex items-start gap-6 mb-6">
                <div class="flex h-16 w-16 shrink-0 items-center justify-center rounded-2xl bg-{color}-100 text-{color}-700 group-hover:bg-{color}-600 group-hover:text-white transition-colors">
                  <i class="fa-solid {s['icon']} text-2xl"></i>
                </div>
                <div>
                  <h3 class="text-2xl font-bold text-slate-900 mb-2">{s['h2']}</h3>
                  <p class="font-semibold text-{color}-700 leading-tight">{s['h3']}</p>
                </div>
              </div>
              <p class="text-slate-600 mb-6 flex-grow">{s['desc']}</p>
              
              <div class="grid sm:grid-cols-2 gap-6 mb-8">
                  <div>
                      <h4 class="font-bold text-slate-900 mb-3 text-sm uppercase tracking-wider">{s['cover_title']}</h4>
                      <ul class="space-y-2 text-sm text-slate-600 font-medium">
                        {cover_lis}
                      </ul>
                  </div>
                  <div>
                      <h4 class="font-bold text-slate-900 mb-3 text-sm uppercase tracking-wider">{s['outcomes_title']}</h4>
                      <ul class="space-y-2 text-sm text-slate-600 font-medium">
                        {outcomes_lis}
                      </ul>
                  </div>
              </div>
              
              <div class="mt-auto">
                <a href="contact.html" class="inline-flex items-center gap-2 font-bold text-{color}-700 hover:text-{color}-900 transition-colors group/link">
                  {s['cta']} <i class="fa-solid fa-arrow-right transition-transform group-hover/link:translate-x-1"></i>
                </a>
              </div>
            </div>
"""
    services_html_parts.append(block)

final_main = html_template.replace("{services_html}", "".join(services_html_parts))

with open('services.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace Title & Meta
html = re.sub(r'<title>.*?</title>', '<title>Dynamics 365 Services | Consulting, Implementation, CRM Customization, Automation</title>', html, flags=re.DOTALL)

if '<meta name="description"' not in html and '<meta\n      name="description"' not in html:
    html = html.replace('<title>', '<meta name="description" content="Explore Bosco Soft Dynamics 365 services including CRM consulting, implementation, customization, Power Automate workflows, Dataverse architecture, Power BI dashboards, Copilot Studio, integration, migration, training, and support."/>\n    <title>')
else:
    html = re.sub(r'<meta[^>]*name="description"[^>]*>', '<meta name="description" content="Explore Bosco Soft Dynamics 365 services including CRM consulting, implementation, customization, Power Automate workflows, Dataverse architecture, Power BI dashboards, Copilot Studio, integration, migration, training, and support."/>', html, flags=re.IGNORECASE)

# Replace <main>
html = re.sub(r'<main>.*?</main>', f'<main>\n{final_main}\n    </main>', html, flags=re.DOTALL)

with open('services.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Updated services.html')
