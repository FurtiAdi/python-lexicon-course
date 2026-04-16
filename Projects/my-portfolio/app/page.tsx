"use client";

import { motion } from "framer-motion";
import { TypeAnimation } from "react-type-animation";

export default function Portfolio() {
  return (
    <main className="bg-gradient-to-br from-black via-gray-900 to-black text-white min-h-screen font-sans overflow-x-hidden">
      <Navbar />
      <Hero />
      <Projects />
      <Skills />
      <About />
      <Contact />
    </main>
  );
}



function Navbar() {
  return (
    <nav className="fixed top-0 w-full z-50 backdrop-blur-xl bg-white/5 border-b border-white/10 px-8 py-4 flex justify-between">
      <h1 className="font-bold text-lg tracking-wide">JunDEV</h1>
      <div className="space-x-6 text-sm">
        <a href="#about" className="hover:text-purple-400">About</a>
        <a href="#projects" className="hover:text-purple-400">Projects</a>
        <a href="#skills" className="hover:text-purple-400">Skills</a>
        <a href="#contact" className="hover:text-purple-400">Contact</a>
      </div>
    </nav>
  );
}


function Hero() {
  return (
    <section className="h-screen flex flex-col justify-center items-center text-center px-4">
      <motion.div
        initial={{ opacity: 0, scale: 0.8 }}
        animate={{ opacity: 1, scale: 1 }}
        className="w-50 h-50 rounded-full border-4 border-purple-500 mb-6 shadow-lg overflow-hidden"
      >
        <img
          src="/furti.png"
          alt="Fortuna"
          className="w-full h-full object-cover"
        />
      </motion.div>

      <motion.h1
        initial={{ opacity: 0, y: 40 }}
        animate={{ opacity: 1, y: 0 }}
        className="text-5xl md:text-7xl font-bold"
      >
        Fortuna Eyob 
      </motion.h1>

      <div className="mt-4 text-xl text-purple-400">
        <TypeAnimation
          sequence={[
            "Junior Developer",
            1500,
            "Python & AI Developer",
            1500,
            "Fullstack Developer",
            1500,
          ]}
          repeat={Infinity}
        />
      </div>

      <p className="mt-6 max-w-xl text-gray-400">
        Building modern, user-friendly applications with a passion for AI.
      </p>

      <div className="mt-8 flex gap-4">
        <a 
          href="/cv_eng.pdf"
          download
          className="px-6 py-3 rounded-xl bg-gradient-to-r from-purple-500 to-indigo-500">
          CV Eng version
        </a>
        <a 
          href="/cv_swed.pdf"
          download
          className="px-6 py-3 rounded-xl border border-white/20">
          CV Swed version
        </a>
      </div>
    </section>
  );
}

function Projects() {
  const projects = [
    {
      title: "Titanic ML",
      desc: "Machine learning prediction model using Python & Scikit-Learn",
      img: "https://images.unsplash.com/photo-1518837695005-2083093ee35b",
      github: "https://github.com/helben2002/TitanicCapstoneProject",
      demo: "#",
    },
    {
      title: "TutorBridge",
      desc: "Student-tutor platform with dynamic UI",
      img: "https://images.unsplash.com/photo-1522202176988-66273c2fd55f",
      github: "https://github.com/FurtiAdi/Tutorbridge-webapp",
      demo: "https://furtiadi.github.io/Tutorbridge-webapp/",
    },
    {
      title: "Discussion Forum",
      desc: "Threaded discussion forum with posts, nested replies, PHP templating, MySQL integration, and responsive UI.",
      img: "https://images.unsplash.com/photo-1516321318423-f06f85e504b3",
      github: "https://github.com/FurtiAdi/DiscussionForum",
      demo: "#",
    },
  ];


 return (
    <section id="projects" className="px-6 py-20 max-w-6xl mx-auto">
      <h2 className="text-4xl font-bold text-center mb-10">Projects</h2>

      <div className="grid md:grid-cols-2 gap-8">
        {projects.map((p, i) => (
          <div
            key={i}
            className="group bg-white/5 rounded-xl overflow-hidden border border-white/10 hover:scale-[1.02] transition"
          >
            <div className="relative overflow-hidden">
              <img
                src={`${p.img}?auto=format&fit=crop&w=800&q=80`}
                alt={p.title}
                className="w-full h-56 object-cover group-hover:scale-110 transition duration-500"
              />

              <div className="absolute inset-0 bg-black/70 opacity-0 group-hover:opacity-100 flex items-center justify-center gap-4 transition">
                <a
                  href={p.github}
                  target="_blank"
                  className="px-4 py-2 bg-purple-600 rounded-lg"
                >
                  GitHub
                </a>
                <a
                  href={p.demo}
                  target="_blank"
                  className="px-4 py-2 border border-white/30 rounded-lg"
                >
                  Live Demo
                </a>
              </div>
            </div>

            <div className="p-6">
              <h3 className="text-xl font-bold">{p.title}</h3>
              <p className="text-gray-400 mt-2">{p.desc}</p>
            </div>
          </div>
        ))}
      </div>
    </section>
  );
}

function Skills() {
  const skills = [
    "Java",
    "Python",
    "JavaScript",
    "Spring Boot",
    "HTML",
    "CSS",
    "PostgreSQL",
    "REST APIs",
    "CI/CD",
    "Git/GitHub",
  ];

  return (
    <section id="skills" className="px-6 py-20">
      <h2 className="text-4xl font-bold text-center mb-10">Skills</h2>
      <div className="grid grid-cols-2 md:grid-cols-4 gap-6 max-w-5xl mx-auto">
        {skills.map((skill, index) => (
          <motion.div
            key={index}
            whileHover={{ scale: 1.05 }}
            className="bg-white/5 backdrop-blur-lg border border-white/10 p-6 rounded-2xl text-center"
          >
            {skill}
          </motion.div>
        ))}
      </div>
    </section>
  );
}



function About() {
  return (
    <section id="about" className="py-28">
      <div className="max-w-6xl pl-5 pr-24 md:pl-10 md:pr-40 grid md:grid-cols-2 gap-20 items-center">
        
        {/* LEFT SIDE */}
        <div className="max-w-xl">
          <p className="text-purple-400 text-m font-semibold uppercase tracking-[0.25em]">
            About Me
          </p>

          <h2 className="text-5xl md:text-6xl font-bold mb-8 leading-tight">
            Transforming{" "}
            <span className="text-transparent bg-clip-text bg-gradient-to-r from-purple-400 to-indigo-500">
              Ideas
            </span>
          </h2>

          <div className="space-y-2 text-gray-400 text-lg leading-8">
            <p>
              I'm a junior software developer with experience in Java, Python,
              Flutter, HTML, CSS, JavaScript, and PHP.
            </p>

            <p>
              Currently, I'm deepening my knowledge through an intensive Python
              bootcamp focused on artificial intelligence and machine learning.
            </p>

            <p>
              I enjoy building user-friendly applications, collaborating with teams,
              and turning theoretical knowledge into real-world solutions.
            </p>

            <p>
              I'm passionate about continuously improving my fullstack and AI skills
              while working on meaningful and impactful projects.
            </p>
          </div>
        </div>

        {/* RIGHT SIDE IMAGE */}
        <div className="flex justify-center md:justify-end">
          <div className="relative">
            
            {/* Background glow */}
             <div className="absolute w-[260px] h-[380px] bg-gradient-to-br from-purple-500 to-indigo-500 rounded-xl opacity-30 translate-x-8 -translate-y-6"></div>


            {/* Image */}
            <div className="relative w-[260px] h-[380px] rounded-2xl overflow-hidden shadow-2xl border border-white/10">
              <img
                src="/furti.png"
                alt="Fortuna"
                className="w-full h-full object-cover"
              />
            </div>

          </div>
        </div>

      </div>
    </section>
  );
}


function Contact() {
  return (
    <section id="contact" className="px-6 py-20 text-center">
      <h2 className="text-4xl font-bold mb-6">Contact</h2>
      <div className="bg-white/5 backdrop-blur-lg border border-white/10 p-8 rounded-2xl max-w-xl mx-auto">
        <p className="text-gray-300">📍 Stockholm</p>
        <p className="text-gray-300">📞 072-873 70 64</p>
        <p className="text-gray-300">✉️ fortunaeyob21@gmail.com</p>
        <div className="mt-4 flex justify-center gap-6">
          <a href="https://github.com/FurtiAdi" className="hover:text-purple-400">GitHub</a>
          <a href="https://linkedin.com/in/fortunaeyob" className="hover:text-purple-400">LinkedIn</a>
        </div>
      </div>
    </section>
  );
}
