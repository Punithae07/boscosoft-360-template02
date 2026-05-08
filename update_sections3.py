import re

with open('c:/Users/SANJI BI/OneDrive/Documents/ssp/boscosoft-360/template2/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the Dark Implementation Section (Lines 1570-1840 approx) with Trust/Proof section
trust_section = '''
      <!-- Trust / Proof Section -->
      <section
        class="py-stack-xl relative overflow-hidden bg-slate-950 text-white"
      >
        <div
          class="absolute left-1/4 top-0 h-[500px] w-[500px] -translate-x-1/2 rounded-full bg-violet-600/30 blur-[120px] animate-float"
        ></div>
        <div
          class="absolute right-0 bottom-0 h-[400px] w-[400px] translate-x-1/3 rounded-full bg-sky-500/20 blur-[100px] animate-float-slow"
        ></div>
        <div class="hero-grid absolute inset-0 opacity-20"></div>

        <div class="max-w-7xl mx-auto px-8 relative z-10">
          <div class="text-center mb-20" data-aos="fade-up">
            <div
              class="eyebrow-pill mb-5 bg-white/10 border-white/20 text-white shadow-xl backdrop-blur-md"
            >
              <span class="material-symbols-outlined text-sm text-violet-300"
                >verified</span
              >
              <span class="text-label-md font-semibold text-white"
                >Why Partner With Us</span
              >
            </div>
            <h2 class="font-headline-lg text-headline-lg text-white mb-4">
              What You Can Expect from
              <span
                class="bg-gradient-to-r from-violet-400 to-sky-400 bg-clip-text text-transparent"
                >Bosco Soft</span
              >
            </h2>
            <p class="text-slate-300 max-w-2xl mx-auto text-lg leading-relaxed">
              When you partner with Boscosoftfor Dynamics 365, you get a team focused on clarity, quality, usability, and long-term business success.
            </p>
          </div>
          
          <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 relative mb-12" data-aos="fade-up" data-aos-delay="100">
            <div class="bg-white/5 border border-white/10 p-6 rounded-2xl backdrop-blur-md">
              <i class="fa-solid fa-comments text-2xl text-violet-400 mb-4"></i>
              <p class="font-semibold text-white">Clear consultation and requirement discovery</p>
            </div>
            <div class="bg-white/5 border border-white/10 p-6 rounded-2xl backdrop-blur-md">
              <i class="fa-solid fa-sitemap text-2xl text-violet-400 mb-4"></i>
              <p class="font-semibold text-white">Structured implementation methodology</p>
            </div>
            <div class="bg-white/5 border border-white/10 p-6 rounded-2xl backdrop-blur-md">
              <i class="fa-solid fa-sliders text-2xl text-violet-400 mb-4"></i>
              <p class="font-semibold text-white">Practical customization aligned with business workflows</p>
            </div>
            <div class="bg-white/5 border border-white/10 p-6 rounded-2xl backdrop-blur-md">
              <i class="fa-solid fa-layer-group text-2xl text-violet-400 mb-4"></i>
              <p class="font-semibold text-white">Strong Microsoft ecosystem alignment</p>
            </div>
            <div class="bg-white/5 border border-white/10 p-6 rounded-2xl backdrop-blur-md">
              <i class="fa-solid fa-database text-2xl text-violet-400 mb-4"></i>
              <p class="font-semibold text-white">Clean data architecture and role-based access planning</p>
            </div>
            <div class="bg-white/5 border border-white/10 p-6 rounded-2xl backdrop-blur-md">
              <i class="fa-solid fa-users text-2xl text-violet-400 mb-4"></i>
              <p class="font-semibold text-white">User-focused design and adoption support</p>
            </div>
            <div class="bg-white/5 border border-white/10 p-6 rounded-2xl backdrop-blur-md">
              <i class="fa-solid fa-chart-line text-2xl text-violet-400 mb-4"></i>
              <p class="font-semibold text-white">Dashboard and reporting visibility for decision-makers</p>
            </div>
            <div class="bg-white/5 border border-white/10 p-6 rounded-2xl backdrop-blur-md">
              <i class="fa-solid fa-headset text-2xl text-violet-400 mb-4"></i>
              <p class="font-semibold text-white">Documentation, training, and reliable post-launch support</p>
            </div>
          </div>
        </div>
      </section>
'''

# First, remove the duplicate 'Our Implementation Approach' Section and Experience Case studies 
pattern = r'<!-- Implementation Approach -->\n      <section\n        class="py-stack-xl relative overflow-hidden bg-slate-950 text-white".*?<!-- Final CTA -->'

content = re.sub(pattern, trust_section + '\n      <!-- Final CTA -->', content, flags=re.DOTALL)


# Update Final CTA
content = content.replace('Ready to make\n              <span\n                class="text-transparent bg-clip-text bg-gradient-to-r from-violet-300 to-sky-300"\n                >Dynamics 365</span\n              >\n              work for your business?', 'Ready to Make Dynamics 365 Work for Your Business?')

content = content.replace('Schedule a personalized demo or consultation with our experts\n              today and start your journey towards intelligent growth.', 'Whether you are planning a new CRM implementation, improving your current Dynamics 365 setup, or building a connected Microsoft business platform, BoscosoftTechnologies is ready to help.<br/><br/>Let us help you turn Dynamics 365 into a scalable, intelligent, and business-ready platform that supports your teams, customers, and growth goals.')

content = content.replace('Request a Demo\n              </button>', 'Book a Consultation\n              </button>')
content = content.replace('Contact Sales\n              </button>', 'Contact Us Today\n              </button>')


with open('c:/Users/SANJI BI/OneDrive/Documents/ssp/boscosoft-360/template2/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
