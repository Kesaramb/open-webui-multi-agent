import { useState, useEffect } from "react";
import { motion } from "framer-motion";

// Simple Icon Set (Emoji + SVG blend for portability)
const Check = () => (
  <svg viewBox="0 0 24 24" className="h-5 w-5" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M20 6L9 17l-5-5"/></svg>
);

const Section = ({ id, className = "", children }) => (
  <section id={id} className={`mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 ${className}`}>{children}</section>
);

const Pill = ({ label }) => (
  <span className="inline-flex items-center gap-2 rounded-full border border-white/10 bg-white/5 px-3 py-1 text-xs font-medium text-white/90 backdrop-blur">
    <span className="h-1.5 w-1.5 rounded-full bg-emerald-400 animate-pulse" />{label}
  </span>
);

const Flywheel = () => (
  <div className="relative mx-auto h-64 w-64">
    <div className="absolute inset-0 rounded-full border border-cyan-400/40 animate-[spin_18s_linear_infinite]"/>
    <div className="absolute inset-4 rounded-full border border-emerald-400/40 animate-[spin_22s_linear_infinite_reverse]"/>
    <div className="absolute inset-8 rounded-full border border-amber-400/40 animate-[spin_26s_linear_infinite]"/>
    <div className="absolute inset-0 grid place-items-center text-center">
      <div>
        <p className="text-xs uppercase tracking-widest text-white/60">Flywheel</p>
        <h4 className="text-lg font-semibold text-white">Attention → System → Income</h4>
      </div>
    </div>
  </div>
);

const Nav = () => {
  const [scrolled, setScrolled] = useState(false);
  useEffect(() => {
    const onScroll = () => setScrolled(window.scrollY > 10);
    window.addEventListener("scroll", onScroll);
    return () => window.removeEventListener("scroll", onScroll);
  }, []);
  return (
    <div className={`sticky top-0 z-50 w-full transition-all ${scrolled ? "bg-black/70 backdrop-blur border-b border-white/10" : "bg-transparent"}`}>
      <Section className="flex items-center justify-between py-3">
        <a href="#home" className="flex items-center gap-2">
          <img src="/logo.jpg" alt="BrandFactory" className="h-8 w-auto rounded" />
          <span className="font-semibold tracking-tight text-white">BrandFactory</span>
        </a>
        <nav className="hidden items-center gap-6 text-sm text-white/80 md:flex">
          <a href="#os" className="hover:text-white">OS</a>
          <a href="#flow" className="hover:text-white">Flow</a>
          <a href="#systems" className="hover:text-white">Systems</a>
          <a href="#cases" className="hover:text-white">Case Studies</a>
          <a href="#team" className="hover:text-white">Team</a>
        </nav>
        <div className="flex items-center gap-3">
          <a href="#contact" className="rounded-xl border border-white/15 px-4 py-2 text-sm text-white/90 hover:bg-white/10">Book a Call</a>
          <a href="/workspace" className="rounded-xl bg-gradient-to-r from-cyan-500 to-emerald-400 px-4 py-2 text-sm font-semibold text-black hover:brightness-110">Try OS Demo</a>
        </div>
      </Section>
    </div>
  );
};

export default function BrandFactoryLanding() {
  return (
    <div className="min-h-screen bg-[#07090B] text-white">
      <Nav />

      {/* HERO */}
      <Section id="home" className="relative overflow-hidden pt-20 pb-24">
        <div className="pointer-events-none absolute inset-0 -z-10 bg-[radial-gradient(ellipse_at_top,_var(--tw-gradient-stops))] from-cyan-500/10 via-transparent to-transparent"/>
        <div className="grid items-center gap-12 md:grid-cols-2">
          <div>
            <Pill label="Human + AI Media OS" />
            <h1 className="mt-4 text-4xl font-extrabold leading-tight sm:text-5xl">
              We Build Digital Systems That <span className="text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 to-emerald-400">Think, Learn, and Sell</span>
            </h1>
            <p className="mt-5 max-w-xl text-lg text-white/80">
              A new era where humans, AI agents, and media work as one — engineered to multiply your brand's intelligence, not just its reach.
            </p>
            <div className="mt-7 flex flex-wrap items-center gap-3">
              <a href="#os" className="rounded-xl bg-white px-5 py-3 text-sm font-semibold text-black hover:brightness-95">Explore BrandFactory OS</a>
              <a href="#agents" className="rounded-xl border border-white/15 px-5 py-3 text-sm text-white/90 hover:bg-white/10">Meet the Agents</a>
            </div>
            <ul className="mt-6 space-y-2 text-sm text-white/70">
              <li className="flex items-center gap-2"><Check/> 90‑minute daily sprint → systemized growth</li>
              <li className="flex items-center gap-2"><Check/> Attention → System → Income flywheel</li>
              <li className="flex items-center gap-2"><Check/> Built with Ollama · OpenWebUI · HuggingFace</li>
            </ul>
          </div>
          <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.6 }} className="grid place-items-center">
            <Flywheel />
          </motion.div>
        </div>
      </Section>

      {/* CORE PROMISE */}
      <Section id="promise" className="py-20">
        <div className="rounded-3xl border border-white/10 bg-white/5 p-8 md:p-12">
          <div className="grid items-center gap-10 md:grid-cols-2">
            <div>
              <h2 className="text-2xl font-bold sm:text-3xl">From Idea to Income — in 90 Minutes a Day</h2>
              <p className="mt-3 text-white/80">We don't do projects. We build compounding systems — media, automation, and AI workflows that create recurring revenue loops for your brand.</p>
              <div className="mt-6 grid grid-cols-1 gap-4 sm:grid-cols-2">
                {[
                  ["Systemized Content Engines", "Operate at industrial cadence with quality control."],
                  ["Agent Workflows", "Specialized bots for research, writing, design, posting."],
                  ["Revenue Loops", "Courses, SaaS, affiliate, sponsorship networks."],
                  ["Insight Memory", "Learn from every post, ad, and conversation."],
                ].map(([title, desc]) => (
                  <div key={title} className="rounded-2xl border border-white/10 bg-black/30 p-4">
                    <h4 className="font-semibold">{title}</h4>
                    <p className="mt-1 text-sm text-white/70">{desc}</p>
                  </div>
                ))}
              </div>
            </div>
            <div className="grid place-items-center">
              <Flywheel />
            </div>
          </div>
        </div>
      </Section>

      {/* FLOW STATE SECTION */}
      <Section id="flow" className="py-20">
        <div className="mx-auto max-w-4xl text-center">
          <Pill label="Flow State x AI Precision" />
          <h2 className="mt-4 text-3xl font-bold sm:text-4xl">Where Flow Meets Intelligence</h2>
          <p className="mx-auto mt-3 max-w-2xl text-white/80">
            We don't replace human creativity — we amplify it. Our agents handle the noise so humans can stay inside the creative current where time dissolves and breakthroughs happen.
          </p>
        </div>
        <div className="mt-10 grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
          {[{
            title: "Creative Autonomy",
            desc: "Humans remain the architects — AI expands every path from one insight.",
          },{
            title: "Cognitive Leverage",
            desc: "1 hour of deep work now returns 10 hours of traditional output.",
          },{
            title: "Seamless Flow Systems",
            desc: "Writing, design, and automation connected into a single stream.",
          }].map(({title, desc}) => (
            <div key={title} className="rounded-2xl border border-white/10 bg-white/5 p-6">
              <h4 className="mt-3 text-lg font-semibold">{title}</h4>
              <p className="mt-1 text-sm text-white/70">{desc}</p>
            </div>
          ))}
        </div>
        <div className="mt-10 grid place-items-center">
          <a href="#os" className="rounded-xl bg-gradient-to-r from-cyan-500 to-emerald-400 px-5 py-3 text-sm font-semibold text-black hover:brightness-110">Experience AI that fuels your flow →</a>
        </div>
      </Section>

      {/* OS LAYERS */}
      <Section id="os" className="py-20">
        <div className="mx-auto max-w-4xl text-center">
          <Pill label="BrandFactory OS" />
          <h2 className="mt-4 text-3xl font-bold sm:text-4xl">The 3 Engines of BrandFactory OS</h2>
          <p className="mx-auto mt-3 max-w-2xl text-white/80">A human–AI operating system that prototypes, learns, and scales — on repeat.</p>
        </div>
        <div className="mt-10 grid gap-6 md:grid-cols-3">
          {[{
            title: "Innovation Center",
            desc: "Prototype new content systems and business DNA.",
            points: ["Hypothesis design","Rapid prototyping","Attention mapping"],
          },{
            title: "Learning Center",
            desc: "Run real-time market feedback loops and adapt.",
            points: ["Data loops","E-E-A-T/STEPPS analyses","Iteration rituals"],
          },{
            title: "Mutation & Automation",
            desc: "Scale what works through AI and agent workflows.",
            points: ["n8n swarms","Autopublishing","Quality gates"],
          }].map(({title, desc, points}) => (
            <div key={title} className="rounded-2xl border border-white/10 bg-white/5 p-6">
              <h4 className="text-lg font-semibold">{title}</h4>
              <p className="mt-1 text-sm text-white/70">{desc}</p>
              <ul className="mt-4 space-y-2 text-sm text-white/70">
                {points.map(p => (
                  <li key={p} className="flex items-center gap-2"><Check/> {p}</li>
                ))}
              </ul>
            </div>
          ))}
        </div>
        <div className="mt-10 grid place-items-center">
          <a href="#systems" className="rounded-xl border border-white/15 px-5 py-3 text-sm text-white/90 hover:bg-white/10">See how it works</a>
        </div>
      </Section>

      {/* SYSTEMS / AGENTS */}
      <Section id="systems" className="py-20">
        <div className="mx-auto max-w-4xl text-center">
          <Pill label="Agent Stack" />
          <h2 className="mt-4 text-3xl font-bold sm:text-4xl">Specialized Agents, Orchestrated</h2>
          <p className="mx-auto mt-3 max-w-2xl text-white/80">Each agent is a force multiplier — research, writing, design, distribution, analytics — choreographed by your OS.</p>
        </div>
        <div className="mt-10 grid gap-6 sm:grid-cols-2 lg:grid-cols-4">
          {["Research Maven","SERP Sensei","Storycrafter","Canvasmatic Designer","Autoposter","A/B Orchestrator","Sponsorship Scout","Revenue Mapper"].map((name) => (
            <div key={name} className="rounded-2xl border border-white/10 bg-white/5 p-5">
              <h4 className="mt-2 font-semibold">{name}</h4>
              <p className="mt-1 text-xs text-white/70">Plug-and-play worker that learns from outcomes and feeds the memory graph.</p>
            </div>
          ))}
        </div>
      </Section>

      {/* CASE STUDIES */}
      <Section id="cases" className="py-20">
        <div className="mx-auto max-w-4xl text-center">
          <Pill label="Proof of Work" />
          <h2 className="mt-4 text-3xl font-bold sm:text-4xl">Systems We've Engineered</h2>
        </div>
        <div className="mt-10 grid gap-6 md:grid-cols-2">
          {[{
            title: "Manifestics.com",
            desc: "Future‑Self OS: generate 'future you' profiles (Google SERP, LinkedIn, IMDb‑style) and track intention → action loops.",
          },{
            title: "LifeatDubai.com",
            desc: "City‑vertical media engine: automated question streams, social syndication, and SEO flywheels for Dubai life & work.",
          },{
            title: "GeeksAroundGlobe.com",
            desc: "AI‑assisted journalism and Geek Profiles; 10M+ reach flywheel.",
          },{
            title: "TrendingAmerican.com",
            desc: "Mass‑curiosity infotainment: viral US culture news with agent‑driven research & distribution.",
          }].map(({title, desc}) => (
            <div key={title} className="group overflow-hidden rounded-3xl border border-white/10 bg-gradient-to-br from-white/5 to-white/[0.03] p-6">
              <div className="flex items-center justify-between">
                <h4 className="text-lg font-semibold">{title}</h4>
                <span className="text-xs text-white/50">Case Study</span>
              </div>
              <p className="mt-2 text-sm text-white/70">{desc}</p>
              <div className="mt-4 flex flex-wrap gap-2 text-[11px] text-white/70">
                <Pill label="E-E-A-T" />
                <Pill label="STEPPS" />
                <Pill label="Lean Loops" />
              </div>
            </div>
          ))}
        </div>
      </Section>

      {/* TEAM */}
      <Section id="team" className="py-20">
        <div className="mx-auto max-w-4xl text-center">
          <Pill label="Humans x Agents" />
          <h2 className="mt-4 text-3xl font-bold sm:text-4xl">Meet the Builders of the New Digital World</h2>
          <p className="mx-auto mt-3 max-w-2xl text-white/80">Creators, coders, and cognitive engineers — building alongside agent swarms.
          </p>
        </div>
        <div className="mt-10 grid gap-6 sm:grid-cols-2 lg:grid-cols-4">
          {["Strategy","Systems","Content","Automation"].map((track) => (
            <div key={track} className="rounded-2xl border border-white/10 bg-white/5 p-6">
              <h4 className="font-semibold">{track}</h4>
              <ul className="mt-3 space-y-2 text-sm text-white/70">
                <li className="flex items-center gap-2"><Check/> SOPs + DNA Playbooks</li>
                <li className="flex items-center gap-2"><Check/> Agent Orchestration</li>
                <li className="flex items-center gap-2"><Check/> Feedback Loops</li>
              </ul>
            </div>
          ))}
        </div>
      </Section>

      {/* PRICING / OFFER (Optional minimal) */}
      <Section id="offer" className="py-14">
        <div className="rounded-3xl border border-white/10 bg-white/5 p-8 text-center">
          <h3 className="text-2xl font-bold">Start with a 30‑Day Pilot Sprint</h3>
          <p className="mt-2 text-white/75">We design your OS, deploy core agents, and ship a working flywheel. Keep it if it prints value.</p>
          <div className="mt-6 flex flex-wrap items-center justify-center gap-3 text-sm text-white/80">
            <span className="rounded-xl border border-white/15 px-3 py-1">Strategy + DNA</span>
            <span className="rounded-xl border border-white/15 px-3 py-1">Content Engine</span>
            <span className="rounded-xl border border-white/15 px-3 py-1">Agent Stack</span>
            <span className="rounded-xl border border-white/15 px-3 py-1">Automation</span>
          </div>
          <div className="mt-6">
            <a href="#contact" className="rounded-xl bg-white px-5 py-3 text-sm font-semibold text-black hover:brightness-95">Book a Discovery Call</a>
          </div>
        </div>
      </Section>

      {/* CONTACT */}
      <Section id="contact" className="py-20">
        <div className="mx-auto max-w-3xl rounded-3xl border border-white/10 bg-white/5 p-8">
          <h3 className="text-2xl font-bold">Let's Build Your Digital Factory</h3>
          <p className="mt-2 text-white/75">Tell us your goal. We'll map the fastest path from insight → system → income.</p>
          <form className="mt-6 grid gap-4 sm:grid-cols-2">
            <input className="w-full rounded-xl border border-white/10 bg-black/40 px-4 py-3 text-sm outline-none placeholder:text-white/40" placeholder="Full Name" />
            <input className="w-full rounded-xl border border-white/10 bg-black/40 px-4 py-3 text-sm outline-none placeholder:text-white/40" placeholder="Email" />
            <input className="w-full rounded-xl border border-white/10 bg-black/40 px-4 py-3 text-sm outline-none placeholder:text-white/40 sm:col-span-2" placeholder="Company / Project" />
            <textarea rows={4} className="w-full rounded-xl border border-white/10 bg-black/40 px-4 py-3 text-sm outline-none placeholder:text-white/40 sm:col-span-2" placeholder="What outcome should this system create?" />
            <div className="sm:col-span-2">
              <button type="button" className="w-full rounded-xl bg-gradient-to-r from-cyan-500 to-emerald-400 px-5 py-3 text-sm font-semibold text-black hover:brightness-110">Send</button>
            </div>
          </form>
        </div>
      </Section>

      {/* FOOTER */}
      <footer className="border-t border-white/10">
        <Section className="flex flex-col items-start justify-between gap-6 py-10 md:flex-row md:items-center">
          <div className="flex items-center gap-2">
            <img src="/logo.jpg" alt="BrandFactory" className="h-8 w-auto rounded" />
            <span className="font-semibold tracking-tight text-white">BrandFactory</span>
          </div>
          <p className="text-sm text-white/60">Insight → Structure → System → Income.</p>
          <div className="text-sm text-white/60">© {new Date().getFullYear()} BrandFactory</div>
        </Section>
      </footer>

      <style jsx global>{`
        @keyframes spin { to { transform: rotate(360deg); } }
      `}</style>
    </div>
  );
}
