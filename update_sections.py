import re

html = """
      <!-- Problem-Solution Section -->
      <section class="max-w-7xl mx-auto px-8 py-stack-xl mt-20">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
          <div class="space-y-6">
            <span class="eyebrow-pill">
              <i class="fa-solid fa-triangle-exclamation"></i>
              Common Business Challenges
            </span>
            <h2 class="font-headline-lg text-headline-lg text-slate-950 max-w-2xl">
              Is Your Business Ready for a <span class="gradient-text">More Connected CRM Experience?</span>
            </h2>
            <p class="font-body-lg text-on-surface-variant max-w-xl">
              Many organizations struggle to grow because customer data, sales activities, service requests, reports, and workflows are spread across multiple tools, spreadsheets, inboxes, and disconnected systems.
            </p>
            <p class="font-body-lg text-on-surface-variant max-w-xl mb-4">
              This creates common business challenges such as:
            </p>
            <div class="grid gap-4">
              <div class="flex items-start gap-4">
                <span class="flex h-11 w-11 shrink-0 items-center justify-center rounded-2xl bg-rose-100 text-rose-700 text-lg">
                  <i class="fa-solid fa-eye-slash"></i>
                </span>
                <div>
                  <h4 class="font-bold text-primary">Limited visibility</h4>
                  <p class="text-body-md text-on-surface-variant">Into leads, opportunities, and customer interactions</p>
                </div>
              </div>
              <div class="flex items-start gap-4">
                <span class="flex h-11 w-11 shrink-0 items-center justify-center rounded-2xl bg-rose-100 text-rose-700 text-lg">
                  <i class="fa-solid fa-clock-rotate-left"></i>
                </span>
                <div>
                  <h4 class="font-bold text-primary">Manual processes</h4>
                  <p class="text-body-md text-on-surface-variant">Manual follow-ups, approvals, and internal coordination</p>
                </div>
              </div>
              <div class="flex items-start gap-4">
                <span class="flex h-11 w-11 shrink-0 items-center justify-center rounded-2xl bg-rose-100 text-rose-700 text-lg">
                  <i class="fa-solid fa-chart-bar"></i>
                </span>
                <div>
                  <h4 class="font-bold text-primary">Delayed decision-making</h4>
                  <p class="text-body-md text-on-surface-variant">Due to incomplete or outdated reports</p>
                </div>
              </div>
              <div class="flex items-start gap-4">
                <span class="flex h-11 w-11 shrink-0 items-center justify-center rounded-2xl bg-rose-100 text-rose-700 text-lg">
                  <i class="fa-solid fa-users-slash"></i>
                </span>
                <div>
                  <h4 class="font-bold text-primary">Inconsistent experiences</h4>
                  <p class="text-body-md text-on-surface-variant">Inconsistent customer service experiences</p>
                </div>
              </div>
              <div class="flex items-start gap-4">
                <span class="flex h-11 w-11 shrink-0 items-center justify-center rounded-2xl bg-rose-100 text-rose-700 text-lg">
                  <i class="fa-solid fa-handshake-slash"></i>
                </span>
                <div>
                  <h4 class="font-bold text-primary">Poor collaboration</h4>
                  <p class="text-body-md text-on-surface-variant">Between sales, service, operations, and management teams</p>
                </div>
              </div>
              <div class="flex items-start gap-4">
                <span class="flex h-11 w-11 shrink-0 items-center justify-center rounded-2xl bg-rose-100 text-rose-700 text-lg">
                  <i class="fa-solid fa-arrow-trend-down"></i>
                </span>
                <div>
                  <h4 class="font-bold text-primary">Difficulty scaling</h4>
                  <p class="text-body-md text-on-surface-variant">Difficulty scaling processes as the business grows</p>
                </div>
              </div>
            </div>
            
            <div class="mt-6 bg-violet-50 p-6 rounded-2xl border border-violet-100">
                <p class="font-body-lg text-slate-800 mb-4">
                  <strong>Microsoft Dynamics 365 CRM</strong> helps solve these challenges by bringing people, data, processes, and intelligence together in one connected platform.
                </p>
                <p class="font-body-lg text-slate-800">
                  With Boscosoftas your implementation partner, Dynamics 365 becomes more than a CRM system. It becomes a practical business growth platform designed around your workflows, your users, and your goals.
                </p>
            </div>
            
            <button class="mt-4 rounded-full bg-gradient-to-b from-[#6f4dcc] to-[#56329f] px-9 py-4 font-headline-md text-body-md font-bold text-white shadow-xl shadow-violet-900/20 transition-all duration-300 hover:-translate-y-1">
              Request a CRM Assessment
            </button>
          </div>
          <div class="relative hidden lg:block">
            <div class="absolute -left-10 top-10 h-32 w-32 rounded-full bg-rose-200/60 blur-3xl"></div>
            <div class="absolute -right-8 bottom-4 h-36 w-36 rounded-full bg-violet-500/20 blur-3xl"></div>
            <div class="overflow-hidden rounded-[32px] border border-slate-200 shadow-2xl shadow-slate-200/20 bg-white p-4">
              <img
                class="w-full rounded-[28px] object-cover animate-float"
                src="https://images.unsplash.com/photo-1552664730-d307ca884978?auto=format&fit=crop&w=1100&q=80"
                alt="Disconnected systems"
              />
            </div>
          </div>
        </div>
      </section>

      <!-- Why Dynamics 365 Section -->
      <section class="max-w-7xl mx-auto px-8 py-stack-xl mt-10">
        <div class="text-center mb-16">
          <div class="eyebrow-pill mb-5">
            <span class="material-symbols-outlined text-sm text-violet-700">microsoft</span>
            <span class="text-label-md font-semibold">The Platform</span>
          </div>
          <h2 class="font-headline-lg text-headline-lg text-slate-950 mb-4">
            Why <span class="gradient-text">Microsoft Dynamics 365?</span>
          </h2>
          <p class="text-on-surface-variant max-w-3xl mx-auto text-lg">
            Microsoft Dynamics 365 is a connected suite of intelligent business applications that helps organizations manage customer relationships, automate processes, improve team productivity, and make better decisions with real-time data.
          </p>
          <p class="text-on-surface-variant max-w-3xl mx-auto text-lg mt-4">
            For growing businesses, Dynamics 365 offers a flexible foundation for managing sales, customer service, marketing engagement, field service, operations, reporting, and business automation within the broader Microsoft ecosystem.
          </p>
        </div>
        
        <div class="bg-white rounded-[32px] border border-slate-200 shadow-xl shadow-slate-200/40 p-8 md:p-12">
            <h3 class="text-2xl font-bold text-slate-950 mb-8 text-center">With Dynamics 365, your business can:</h3>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
                <div class="bg-violet-50/50 p-6 rounded-2xl border border-violet-100">
                    <i class="fa-solid fa-database text-2xl text-violet-600 mb-4"></i>
                    <p class="font-semibold text-slate-800">Centralize customer, sales, service, and operational data</p>
                </div>
                <div class="bg-violet-50/50 p-6 rounded-2xl border border-violet-100">
                    <i class="fa-solid fa-funnel-dollar text-2xl text-violet-600 mb-4"></i>
                    <p class="font-semibold text-slate-800\">Improve lead management and sales pipeline visibility</p>
                </div>
                <div class="bg-violet-50/50 p-6 rounded-2xl border border-violet-100">
                    <i class="fa-solid fa-headset text-2xl text-violet-600 mb-4\"></i>
                    <p class="font-semibold text-slate-800\">Strengthen customer service and case management</p>
                </div>
                <div class="bg-violet-50/50 p-6 rounded-2xl border border-violet-100\">
                    <i class="fa-solid fa-robot text-2xl text-violet-600 mb-4\"></i>
                    <p class="font-semibold text-slate-800\">Automate repetitive workflows and approval processes</p>
                </div>
                <div class="bg-violet-50/50 p-6 rounded-2xl border border-violet-100\">
                    <i class="fa-solid fa-chart-pie text-2xl text-violet-600 mb-4\"></i>
                    <p class="font-semibold text-slate-800\">Build role-based dashboards and performance reports</p>
                </div>
                <div class="bg-violet-50/50 p-6 rounded-2xl border border-violet-100\">
                    <i class="fa-solid fa-plug text-2xl text-violet-600 mb-4\"></i>
                    <p class="font-semibold text-slate-800\">Connect CRM with Microsoft 365, Outlook, Teams, Power Platform, Azure</p>
                </div>
                <div class="bg-violet-50/50 p-6 rounded-2xl border border-violet-100\">
                    <i class="fa-solid fa-wand-magic-sparkles text-2xl text-violet-600 mb-4\"></i>
                    <p class="font-semibold text-slate-800\">Create AI-assisted user experiences using Copilot Studio</p>
                </div>
                <div class="bg-violet-50/50 p-6 rounded-2xl border border-violet-100\">
                    <i class="fa-solid fa-arrow-up-right-dots text-2xl text-violet-600 mb-4\"></i>
                    <p class="font-semibold text-slate-800\">Scale business applications as processes evolve</p>
                </div>
            </div>
            
            <div class="mt-10 p-6 bg-slate-900 rounded-2xl text-center\">
                <p class="text-white font-body-lg\">
                    When implemented correctly, Dynamics 365 gives leadership better visibility, gives teams better tools, and gives customers a more consistent experience. <strong>Boscosofthelps you make that possible</strong> through structured consulting, implementation, customization, training, and support.
                </p>
            </div>
        </div>
      </section>

      <!-- Why BoscosoftSection -->
      <section class="max-w-7xl mx-auto px-8 py-stack-xl mt-10">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
          <div class="relative order-last lg:order-first">
            <div class="absolute -left-10 top-10 h-32 w-32 rounded-full bg-sky-200/60 blur-3xl"></div>
            <div class="absolute -right-8 bottom-4 h-36 w-36 rounded-full bg-indigo-500/20 blur-3xl\"></div>
            <div class="overflow-hidden rounded-[32px] border border-slate-200 shadow-2xl shadow-slate-200/20 bg-white p-4">
              <img
                class="w-full rounded-[28px] object-cover animate-float"
                src="https://images.unsplash.com/photo-1521791136064-7986c2920216?auto=format&fit=crop&w=1100&q=80"
                alt="BoscosoftTechnologies team"
              />
              <div class="mt-6 rounded-[28px] bg-slate-950/95 p-6 text-white shadow-xl">
                <div class="flex items-center gap-3 text-sky-200 mb-4">
                  <i class="fa-solid fa-award"></i>
                  <span class="font-semibold">Official Microsoft Partner</span>
                </div>
                <p class="text-sm leading-7">
                  We design Dynamics 365 solutions that are usable, scalable, secure, and aligned with the way your organization actually works.
                </p>
              </div>
            </div>
          </div>
          <div class="space-y-6">
            <span class="eyebrow-pill">
              <i class="fa-solid fa-handshake"></i>
              Your Implementation Partner
            </span>
            <h2 class="font-headline-lg text-headline-lg text-slate-950 max-w-2xl">
              Why Choose Boscosoftfor <span class="gradient-text">Dynamics 365?</span>
            </h2>
            <p class="font-body-lg text-on-surface-variant max-w-xl">
              Choosing the right Dynamics 365 partner is not just about technical setup. It is about choosing a team that understands business processes, user adoption, solution architecture, data quality, automation, reporting, and long-term platform success.
            </p>
            <p class="font-body-lg text-on-surface-variant max-w-xl mb-6">
              BoscosoftTechnologies combines Microsoft ecosystem expertise with a practical, business-first implementation approach.
            </p>

            <h3 class="text-xl font-bold text-slate-900 mt-8 mb-4">What Sets Us Apart</h3>
            <div class="grid gap-4">
              <div class="flex items-start gap-4">
                <span class="flex h-8 w-8 shrink-0 items-center justify-center rounded-full bg-violet-600 text-white font-bold">1</span>
                <div>
                  <h4 class="font-bold text-primary">Official Microsoft Dynamics 365 CRM Implementation Partner</h4>
                  <p class="text-sm text-on-surface-variant mt-1">We bring focused experience in implementing and supporting Dynamics 365 CRM solutions for organizations that want reliable delivery and measurable business improvement.</p>
                </div>
              </div>
              <div class="flex items-start gap-4">
                <span class="flex h-8 w-8 shrink-0 items-center justify-center rounded-full bg-violet-600 text-white font-bold">2</span>
                <div>
                  <h4 class="font-bold text-primary">Business-First Consulting Approach</h4>
                  <p class="text-sm text-on-surface-variant mt-1\">We begin with your goals, processes, users, pain points, and reporting needs before recommending features or configurations.</p>
                </div>
              </div>
              <div class="flex items-start gap-4\">
                <span class="flex h-8 w-8 shrink-0 items-center justify-center rounded-full bg-violet-600 text-white font-bold\">3</span>
                <div>
                  <h4 class="font-bold text-primary">End-to-End Dynamics 365 Services</h4>
                  <p class="text-sm text-on-surface-variant mt-1\">From consulting and implementation to customization, automation, integration, reporting, training, and post-go-live support, we manage the full Dynamics 365 journey.</p>
                </div>
              </div>
              <div class="flex items-start gap-4\">
                <span class="flex h-8 w-8 shrink-0 items-center justify-center rounded-full bg-violet-600 text-white font-bold\">4</span>
                <div>
                  <h4 class="font-bold text-primary">Microsoft Ecosystem Expertise</h4>
                  <p class="text-sm text-on-surface-variant mt-1\">We help businesses unlock value across Dynamics 365, Dataverse, Power Automate, Power BI, Microsoft 365, Teams, Outlook, Azure, and Copilot Studio.</p>
                </div>
              </div>
              <div class="flex items-start gap-4\">
                <span class="flex h-8 w-8 shrink-0 items-center justify-center rounded-full bg-violet-600 text-white font-bold\">5</span>
                <div>
                  <h4 class="font-bold text-primary">Practical Customization and Adoption Focus</h4>
                  <p class="text-sm text-on-surface-variant mt-1\">We build solutions that teams can actually use. Our focus is on clean processes, simple user experiences, accurate data, and meaningful dashboards.</p>
                </div>
              </div>
              <div class="flex items-start gap-4\">
                <span class="flex h-8 w-8 shrink-0 items-center justify-center rounded-full bg-violet-600 text-white font-bold\">6</span>
                <div>
                  <h4 class="font-bold text-primary">Long-Term Support Mindset</h4>
                  <p class="text-sm text-on-surface-variant mt-1\">We do not stop at go-live. We support your teams with training, troubleshooting, enhancements, optimization, and ongoing guidance.</p>
                </div>
              </div>
            </div>
            
            <button class="mt-6 rounded-full bg-gradient-to-b from-[#6f4dcc] to-[#56329f] px-9 py-4 font-headline-md text-body-md font-bold text-white shadow-xl shadow-violet-900/20 transition-all duration-300 hover:-translate-y-1\">
              Talk to a Dynamics 365 Expert
            </button>
          </div>
        </div>
      </section>
"""

with open('c:/Users/SANJI BI/OneDrive/Documents/ssp/boscosoft-360/template2/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the existing 'Why Boscosoft for Dynamics 365 Section'
pattern = r'<!-- Why Boscosoft for Dynamics 365 Section -->.*?<!-- Key Services Snapshot Section -->'
content = re.sub(pattern, html + '\n      <!-- Key Services Snapshot Section -->', content, flags=re.DOTALL)

with open('c:/Users/SANJI BI/OneDrive/Documents/ssp/boscosoft-360/template2/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
