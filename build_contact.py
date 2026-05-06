import re

html_template = """      <!-- Hero Banner -->
      <section class="soft-gradient-section relative overflow-hidden pt-32 pb-20">
        <div class="hero-grid absolute inset-0"></div>
        <div class="absolute left-1/2 top-28 h-72 w-72 -translate-x-1/2 rounded-full bg-violet-300/30 blur-3xl"></div>
        <div class="relative z-10 max-w-4xl mx-auto px-8 text-center" data-aos="fade-up">
          <div class="eyebrow-pill mb-6">
            <span class="material-symbols-outlined text-sm text-violet-700">forum</span>
            <span class="text-label-md font-semibold text-slate-700">Get in Touch</span>
          </div>
          <h1 class="font-display-xl text-3xl sm:text-4xl lg:text-5xl font-black text-slate-950 mb-6">Let’s Build Your <span class="gradient-text">Dynamics 365</span> Success Story</h1>
          <p class="text-xl text-slate-600 leading-relaxed max-w-2xl mx-auto">
            Talk to Bosco Soft’s Dynamics 365 experts about CRM implementation, customization, automation, reporting, integration, and long-term support.
          </p>
        </div>
      </section>

      <section class="py-20 bg-white relative z-10">
        <div class="max-w-7xl mx-auto px-8">
          <div class="grid lg:grid-cols-2 gap-16">
            
            <div data-aos="fade-right">
              <h2 class="text-3xl font-bold text-slate-900 mb-6">Ready to Start or Improve Your Dynamics 365 Journey?</h2>
              <p class="text-lg text-slate-600 leading-relaxed mb-6">
                Whether you are planning a new Dynamics 365 CRM implementation, improving an existing system, replacing disconnected tools, automating manual processes, building dashboards, or exploring AI-assisted customer experiences, Bosco Soft Technologies is ready to help.
              </p>
              <p class="text-lg text-slate-600 leading-relaxed mb-10">
                Our team will understand your goals, review your current challenges, and guide you toward the right Dynamics 365 solution for your business.
              </p>
              
              <h3 class="text-2xl font-bold text-slate-900 mb-6">How Can We Help?</h3>
              <p class="font-semibold text-slate-700 mb-4">You can contact us for:</p>
              <ul class="space-y-4 mb-12">
                <li class="flex items-start gap-4">
                  <div class="mt-1 flex h-6 w-6 shrink-0 items-center justify-center rounded-full bg-violet-100 text-violet-600"><i class="fa-solid fa-check text-xs"></i></div>
                  <span class="text-slate-700 font-medium">New Microsoft Dynamics 365 CRM implementation</span>
                </li>
                <li class="flex items-start gap-4">
                  <div class="mt-1 flex h-6 w-6 shrink-0 items-center justify-center rounded-full bg-violet-100 text-violet-600"><i class="fa-solid fa-check text-xs"></i></div>
                  <span class="text-slate-700 font-medium">CRM strategy and consulting</span>
                </li>
                <li class="flex items-start gap-4">
                  <div class="mt-1 flex h-6 w-6 shrink-0 items-center justify-center rounded-full bg-violet-100 text-violet-600"><i class="fa-solid fa-check text-xs"></i></div>
                  <span class="text-slate-700 font-medium">Sales and service process optimization</span>
                </li>
                <li class="flex items-start gap-4">
                  <div class="mt-1 flex h-6 w-6 shrink-0 items-center justify-center rounded-full bg-violet-100 text-violet-600"><i class="fa-solid fa-check text-xs"></i></div>
                  <span class="text-slate-700 font-medium">Dynamics 365 customization and configuration</span>
                </li>
                <li class="flex items-start gap-4">
                  <div class="mt-1 flex h-6 w-6 shrink-0 items-center justify-center rounded-full bg-violet-100 text-violet-600"><i class="fa-solid fa-check text-xs"></i></div>
                  <span class="text-slate-700 font-medium">Workflow automation with Power Automate</span>
                </li>
                <li class="flex items-start gap-4">
                  <div class="mt-1 flex h-6 w-6 shrink-0 items-center justify-center rounded-full bg-violet-100 text-violet-600"><i class="fa-solid fa-check text-xs"></i></div>
                  <span class="text-slate-700 font-medium">Power BI dashboards and reporting</span>
                </li>
                <li class="flex items-start gap-4">
                  <div class="mt-1 flex h-6 w-6 shrink-0 items-center justify-center rounded-full bg-violet-100 text-violet-600"><i class="fa-solid fa-check text-xs"></i></div>
                  <span class="text-slate-700 font-medium">Dataverse data architecture and governance</span>
                </li>
                <li class="flex items-start gap-4">
                  <div class="mt-1 flex h-6 w-6 shrink-0 items-center justify-center rounded-full bg-violet-100 text-violet-600"><i class="fa-solid fa-check text-xs"></i></div>
                  <span class="text-slate-700 font-medium">Copilot Studio and AI-assisted experiences</span>
                </li>
                <li class="flex items-start gap-4">
                  <div class="mt-1 flex h-6 w-6 shrink-0 items-center justify-center rounded-full bg-violet-100 text-violet-600"><i class="fa-solid fa-check text-xs"></i></div>
                  <span class="text-slate-700 font-medium">System integration and modernization</span>
                </li>
                <li class="flex items-start gap-4">
                  <div class="mt-1 flex h-6 w-6 shrink-0 items-center justify-center rounded-full bg-violet-100 text-violet-600"><i class="fa-solid fa-check text-xs"></i></div>
                  <span class="text-slate-700 font-medium">Data migration from legacy systems</span>
                </li>
                <li class="flex items-start gap-4">
                  <div class="mt-1 flex h-6 w-6 shrink-0 items-center justify-center rounded-full bg-violet-100 text-violet-600"><i class="fa-solid fa-check text-xs"></i></div>
                  <span class="text-slate-700 font-medium">User training and post-go-live support</span>
                </li>
                <li class="flex items-start gap-4">
                  <div class="mt-1 flex h-6 w-6 shrink-0 items-center justify-center rounded-full bg-violet-100 text-violet-600"><i class="fa-solid fa-check text-xs"></i></div>
                  <span class="text-slate-700 font-medium">Existing Dynamics 365 improvement or rescue projects</span>
                </li>
              </ul>

              <div class="glass-card rounded-[24px] p-8 border-none bg-gradient-to-br from-slate-50 to-white shadow-lg bg-slate-50">
                <h3 class="font-bold text-slate-900 mb-4">Direct Contact</h3>
                <div class="space-y-3 text-slate-600">
                  <p class="flex items-center gap-3"><i class="fa-solid fa-envelope text-violet-600"></i> info@boscosofttech.com</p>
                  <p class="flex items-center gap-3"><i class="fa-solid fa-phone text-violet-600"></i> +91 98765 43210</p>
                </div>
              </div>
            </div>

            <div data-aos="fade-left">
              <div class="glass-card rounded-[32px] p-8 lg:p-12 shadow-xl border border-slate-200 bg-white">
                <h2 class="text-2xl font-bold text-slate-900 mb-2">Book a Consultation</h2>
                <p class="text-slate-600 text-sm mb-8">Share a few details about your Dynamics 365 requirement. Our team will get in touch to understand your needs and recommend the next best step.</p>
                
                <form class="space-y-6">
                  <div class="space-y-2">
                    <label class="text-sm font-semibold text-slate-700">Full Name</label>
                    <input type="text" class="w-full rounded-xl border-slate-200 focus:border-violet-600 focus:ring-violet-600 bg-slate-50/50" placeholder="John Doe" />
                  </div>
                  <div class="grid grid-cols-2 gap-6">
                    <div class="space-y-2">
                      <label class="text-sm font-semibold text-slate-700">Business Email</label>
                      <input type="email" class="w-full rounded-xl border-slate-200 focus:border-violet-600 focus:ring-violet-600 bg-slate-50/50" placeholder="john@company.com" />
                    </div>
                    <div class="space-y-2">
                      <label class="text-sm font-semibold text-slate-700">Phone Number</label>
                      <input type="tel" class="w-full rounded-xl border-slate-200 focus:border-violet-600 focus:ring-violet-600 bg-slate-50/50" placeholder="+1 (555) 000-0000" />
                    </div>
                  </div>
                  <div class="grid grid-cols-2 gap-6">
                    <div class="space-y-2">
                      <label class="text-sm font-semibold text-slate-700">Company Name</label>
                      <input type="text" class="w-full rounded-xl border-slate-200 focus:border-violet-600 focus:ring-violet-600 bg-slate-50/50" placeholder="Acme Corp" />
                    </div>
                    <div class="space-y-2">
                      <label class="text-sm font-semibold text-slate-700">Country / Region</label>
                      <input type="text" class="w-full rounded-xl border-slate-200 focus:border-violet-600 focus:ring-violet-600 bg-slate-50/50" placeholder="United States" />
                    </div>
                  </div>
                  <div class="space-y-2">
                    <label class="text-sm font-semibold text-slate-700">Service Interest</label>
                    <select class="w-full rounded-xl border-slate-200 focus:border-violet-600 focus:ring-violet-600 bg-slate-50/50">
                      <option>Dynamics 365 Consulting</option>
                      <option>Dynamics 365 Implementation</option>
                      <option>CRM Customization</option>
                      <option>Workflow Automation</option>
                      <option>Power BI Reporting</option>
                      <option>Dataverse Data Design</option>
                      <option>Copilot Studio</option>
                      <option>Integration / Migration</option>
                      <option>Training and Support</option>
                      <option>Not Sure Yet</option>
                    </select>
                  </div>
                  <div class="space-y-2">
                    <label class="text-sm font-semibold text-slate-700">Brief Requirement / Message</label>
                    <textarea rows="4" class="w-full rounded-xl border-slate-200 focus:border-violet-600 focus:ring-violet-600 bg-slate-50/50" placeholder="Tell us a little about your project..."></textarea>
                  </div>
                  
                  <button type="button" class="w-full rounded-full bg-violet-600 px-6 py-4 font-bold text-white shadow-lg shadow-violet-600/30 transition-all hover:bg-violet-700 hover:-translate-y-0.5 mt-4">
                    Submit Your Requirement
                  </button>
                  <p class="text-xs text-slate-500 text-center mt-4">
                    <i class="fa-solid fa-lock text-slate-400 mr-1"></i> We respect your privacy. Your information will be used only to respond to your enquiry.
                  </p>
                </form>
              </div>
            </div>

          </div>
        </div>
      </section>

      <!-- Contact Page CTA Block -->
      <section class="py-24 bg-gradient-to-br from-violet-900 to-slate-900 relative overflow-hidden text-center">
        <div class="absolute inset-0 bg-[url('assets/dash01.jpg')] bg-cover bg-center opacity-10 mix-blend-overlay"></div>
        <div class="relative z-10 max-w-4xl mx-auto px-8" data-aos="fade-up">
          <h2 class="font-display-xl text-3xl md:text-5xl font-bold text-white mb-6">Build a CRM Platform That Works for Your Business</h2>
          <p class="text-xl text-violet-100 mb-10 max-w-2xl mx-auto">With Bosco Soft as your Dynamics 365 partner, you can move from scattered processes to a connected, automated, and insight-driven Microsoft CRM platform.</p>
          <div class="flex flex-col sm:flex-row items-center justify-center gap-4">
            <a href="contact.html" class="rounded-full bg-white px-8 py-4 font-bold text-violet-900 shadow-lg transition hover:-translate-y-1 hover:shadow-xl w-full sm:w-auto">Get in Touch</a>
            <a href="contact.html" class="rounded-full border border-violet-200/30 bg-violet-800/30 px-8 py-4 font-bold text-white backdrop-blur-sm transition hover:bg-violet-800/50 w-full sm:w-auto">Book a Consultation</a>
          </div>
        </div>
      </section>
"""

with open('contact.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace Title & Meta
html = re.sub(r'<title>.*?</title>', '<title>Contact Bosco Soft Dynamics 365 Experts | Book a CRM Consultation</title>', html, flags=re.DOTALL)

if '<meta name="description"' not in html and '<meta\n      name="description"' not in html:
    html = html.replace('<title>', '<meta name="description" content="Contact Bosco Soft Technologies to discuss Microsoft Dynamics 365 CRM implementation, customization, automation, Power BI reporting, Dataverse, Copilot Studio, integration, migration, training, and support."/>\n    <title>')
else:
    html = re.sub(r'<meta[^>]*name="description"[^>]*>', '<meta name="description" content="Contact Bosco Soft Technologies to discuss Microsoft Dynamics 365 CRM implementation, customization, automation, Power BI reporting, Dataverse, Copilot Studio, integration, migration, training, and support."/>', html, flags=re.IGNORECASE)

# Replace <main>
html = re.sub(r'<main>.*?</main>', f'<main>\n{html_template}\n    </main>', html, flags=re.DOTALL)

with open('contact.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Updated contact.html')
