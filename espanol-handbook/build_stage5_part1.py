"""
Build Stage 5: Days 41 to 45 (Developing Stronger A1 Skills)
"""
import json

stage5_days = [
    {
        "day": 41,
        "stage": 5,
        "title": "Work, Professions & Workplace",
        "subtitle": "Talking about jobs, careers, work environments, and work schedules",
        "goals": [
            "Name major professions and adjust them for gender (médico/médica, profesor/profesora)",
            "State your profession without an article using SER (*Soy ingeniero*)",
            "Describe where you work using TRABAJAR EN (*en una oficina, en un hospital*)",
            "Discuss working hours and conditions (a tiempo completo, teletrabajo, turno)"
        ],
        "bengaliNote": "Remember from Day 8: when stating your profession with SER in Spanish, you DO NOT use an article! You say *Soy informático* (I am computer scientist), never *Soy un informático* — just like Bangla: 'আমি সফটওয়্যার ইঞ্জিনিয়ার' (not 'আমি একজন...').",
        "vocabulary": [
            {"word": "La profesión / El trabajo", "translation": "The profession / The job, work", "pos": "noun", "gender": "feminine / masculine", "example": "¿Cuál es tu profesión?", "exampleTranslation": "What is your profession?"},
            {"word": "El médico / La médica", "translation": "The doctor / physician", "pos": "noun", "gender": "masculine / feminine", "example": "Mi hermana es médica en un hospital público.", "exampleTranslation": "My sister is a doctor in a public hospital."},
            {"word": "El profesor / La profesora", "translation": "The teacher / professor", "pos": "noun", "gender": "masculine / feminine", "example": "Carmen es profesora de español.", "exampleTranslation": "Carmen is a Spanish teacher."},
            {"word": "El ingeniero / La ingeniera", "translation": "The engineer", "pos": "noun", "gender": "masculine / feminine", "example": "Soy ingeniero de software.", "exampleTranslation": "I am a software engineer."},
            {"word": "El informático / La informática", "translation": "IT specialist / Computer scientist", "pos": "noun", "gender": "masculine / feminine", "example": "Trabaja como informático en una startup.", "exampleTranslation": "He works as an IT specialist at a startup."},
            {"word": "El camarero / La camarera", "translation": "The waiter / The waitress", "pos": "noun", "gender": "masculine / feminine", "example": "El camarero es muy atento.", "exampleTranslation": "The waiter is very attentive."},
            {"word": "La empresa / La oficina", "translation": "The company / The office", "pos": "noun", "gender": "feminine", "example": "Trabajo en una oficina moderna.", "exampleTranslation": "I work in a modern office."},
            {"word": "El teletrabajo (trabajar en remoto)", "translation": "Teleworking / Working remotely", "pos": "noun / phrase", "gender": "masculine", "example": "Hago teletrabajo tres días por semana.", "exampleTranslation": "I telework three days a week."},
            {"word": "El horario laboral", "translation": "Work schedule / hours", "pos": "noun", "gender": "masculine", "example": "Tengo un horario flexible.", "exampleTranslation": "I have a flexible schedule."},
            {"word": "En paro / Desempleado(a)", "translation": "Unemployed / On job search", "pos": "phrase / adjective", "gender": "masculine", "example": "Actualmente no está en paro, tiene trabajo.", "exampleTranslation": "Currently he is not unemployed, he has work."}
        ],
        "sentences": [
            {"spanish": "¿A qué te dedicas? —Soy informático en una empresa internacional.", "english": "What do you do for a living? —I am an IT specialist at an international company."},
            {"spanish": "Mi padre trabaja en un banco y mi madre es enfermera.", "english": "My father works in a bank and my mother is a nurse."},
            {"spanish": "Tengo un horario de nueve a cinco de lunes a viernes.", "english": "I have a schedule from nine to five from Monday to Friday."},
            {"spanish": "¿Trabajas en una oficina o haces teletrabajo?", "english": "Do you work in an office or do you telework?"},
            {"spanish": "Me gusta mi trabajo porque el ambiente laboral es excelente.", "english": "I like my job because the work atmosphere is excellent."},
            {"spanish": "Quiero encontrar un trabajo en España para mejorar mi carrera.", "english": "I want to find a job in Spain to improve my career."}
        ],
        "grammar": {
            "title": "Profession Formulas: 'SER + Profesión' vs. 'TRABAJAR DE / COMO'",
            "explanation": "In Spanish, how you describe your occupation depends on whether it is your primary identity or your current temporary position.",
            "rules": [
                "1. SER + Profession (No article!): *Soy informático*, *Eres médico*, *Es profesora*. Adding 'un/una' is only allowed if qualified by an adjective: *Soy un informático excelente*.",
                "2. TRABAJAR DE / TRABAJAR COMO (Temporary or Current Role): *Trabajo de camarero en verano* (I work as a waiter in summer), *Trabaja como informático*.",
                "3. Asking Occupation: Three natural ways: 1) *¿A qué te dedicas?* (What do you dedicate yourself to? - Most common!), 2) *¿En qué trabajas?* (What do you work in?), 3) *¿Cuál es tu profesión?*.",
                "Gender Agreement: -o -> -a (*el médico / la médica*); consonant -> +a (*el profesor / la profesora*, *el escritor / la escritora*); -ista stays the same for both (*el/la periodista, el/la dentista*)."
            ],
            "structures": [
                "Identity: SER + [Profesión sin artículo] (Soy ingeniero)",
                "Workplace: Trabajar en + [Empresa / Lugar] (Trabajo en una oficina)",
                "Asking: ¿A qué te dedicas? / ¿En qué trabajas?"
            ],
            "examples": [
                {"spanish": "Mi tío es abogado.", "english": "My uncle is a lawyer."},
                {"spanish": "Ella trabaja de dependienta en una tienda de ropa.", "english": "She works as a sales clerk in a clothing store."},
                {"spanish": "Soy estudiante universitario.", "english": "I am a university student."},
                {"spanish": "¿A qué se dedica usted, señor? (formal)", "english": "What do you do for a living, sir?"}
            ],
            "commonMistakes": [
                {"wrong": "Soy un ingeniero", "right": "Soy ingeniero", "explanation": "Do not use an indefinite article with professions after 'ser'."},
                {"wrong": "¿Qué es tu trabajo?", "right": "¿En qué trabajas? / ¿A qué te dedicas?", "explanation": "Ask '¿A qué te dedicas?' for a natural question."}
            ],
            "proTip": "Professions ending in **-ista** (*periodista* = journalist, *dentista* = dentist, *artista* = artist) do NOT change for gender! Only the article changes: *el dentista* (male dentist) vs. *la dentista* (female dentist)."
        },
        "conversation": {
            "title": "Networking at a Coworking Space in Madrid",
            "context": "Sakib meets Lucía in a shared coworking space on Paseo de la Castellana.",
            "dialogue": [
                {"speaker": "Lucía", "role": "Architect", "spanish": "¡Hola! Buenas tardes. ¿Está libre este asiento?", "english": "Hello! Good afternoon. Is this seat free?"},
                {"speaker": "Sakib", "role": "Professional", "spanish": "Sí, claro, está libre. Adelante.", "english": "Yes, of course, it's free. Go ahead."},
                {"speaker": "Lucía", "role": "Architect", "spanish": "Gracias. Veo que trabajas con el ordenador. ¿A qué te dedicas?", "english": "Thanks. I see you work with the computer. What do you do for a living?"},
                {"speaker": "Sakib", "role": "Professional", "spanish": "Soy desarrollador de software. Trabajo en remoto para una empresa tecnológica. ¿Y tú?", "english": "I am a software developer. I work remotely for a tech company. And you?"},
                {"speaker": "Lucía", "role": "Architect", "spanish": "Yo soy arquitecta. Diseño proyectos de viviendas sostenibles en Madrid.", "english": "I am an architect. I design sustainable housing projects in Madrid."},
                {"speaker": "Sakib", "role": "Professional", "spanish": "¡Qué interesante! ¿Y tienes un horario fijo o flexible?", "english": "How interesting! And do you have fixed or flexible hours?"},
                {"speaker": "Lucía", "role": "Architect", "spanish": "Totalmente flexible. Me encanta el teletrabajo porque me permite gestionar mi tiempo.", "english": "Totally flexible. I love remote work because it allows me to manage my time."},
                {"speaker": "Sakib", "role": "Professional", "spanish": "Opino lo mismo. Es una gran ventaja.", "english": "I think the same. It's a huge advantage."}
            ],
            "keyPhrases": [
                {"phrase": "¿A qué te dedicas?", "explanation": "The most natural and elegant way to ask someone's profession in Spanish."},
                {"phrase": "En remoto", "explanation": "'Remotely / remote work'."},
                {"phrase": "Opino lo mismo", "explanation": "'I share the same opinion / I think the same'."}
            ]
        },
        "reading": {
            "title": "El mundo laboral y las nuevas formas de trabajo en España",
            "passage": "El mercado laboral español ha experimentado una transformación profunda en los últimos años. Tradicionalmente, la jornada laboral incluía una pausa larga al mediodía para comer y descansar, terminando a las siete u ocho de la tarde. Hoy en día, muchas empresas adoptan la «jornada continua», con horarios intensivos de ocho a tres, especialmente durante los meses de verano. Además, el auge del teletrabajo y los espacios de trabajo compartido (coworking) han atraído a miles de profesionales internacionales y nómadas digitales a ciudades como Madrid, Barcelona, Valencia y Málaga. Estos profesionales eligen España no solo por sus oportunidades profesionales, sino por su extraordinaria calidad de vida, su clima agradable y su vibrante vida social.",
            "translation": "The Spanish labor market has experienced a profound transformation in recent years. Traditionally, the workday included a long midday break to eat and rest, finishing at seven or eight in the evening. Nowadays, many companies adopt the 'continuous day', with intensive hours from eight to three, especially during the summer months. Furthermore, the rise of remote work and shared workspaces (coworking) has attracted thousands of international professionals and digital nomads to cities like Madrid, Barcelona, Valencia, and Malaga. These professionals choose Spain not only for its career opportunities, but for its extraordinary quality of life, pleasant climate, and vibrant social life.",
            "questions": [
                {"question": "¿Qué es la 'jornada continua' en el trabajo?", "options": ["Trabajar 24 horas seguidas", "Horario intensivo sin pausa larga, por ejemplo de ocho a tres", "No trabajar nunca", "Trabajar solo los domingos"], "answer": 1, "explanation": "Intensive schedule without a long break ('horario intensivo... de ocho a tres')."},
                {"question": "¿Qué ciudades atraen a nómadas digitales y profesionales internacionales?", "options": ["Madrid, Barcelona, Valencia y Málaga", "Solo pueblos desiertos", "Ninguna ciudad española", "Solo el norte frío"], "answer": 0, "explanation": "Madrid, Barcelona, Valencia, and Malaga."},
                {"question": "¿Por qué eligen España estos profesionales?", "options": ["Por la calidad de vida, clima y vida social", "Porque es obligatorio", "Para comprar coches", "Por el frío"], "answer": 0, "explanation": "Quality of life, climate, and social life."}
            ]
        },
        "exercises": [
            {
                "id": "d41-ex1",
                "type": "multiple-choice",
                "prompt": "How do you correctly say 'I am an engineer' in Spanish?",
                "options": ["Soy ingeniero", "Soy un ingeniero", "Estoy ingeniero", "Tengo ingeniero"],
                "correct": 0,
                "explanation": "Spanish drops the article with professions after 'ser': 'Soy ingeniero'."
            },
            {
                "id": "d41-ex2",
                "type": "fill-in",
                "prompt": "Feminine form of 'el profesor': Ella es ______.",
                "options": ["profesora", "profesore", "profesoraa", "profesores"],
                "correct": 0,
                "explanation": "Consonant-ending professions add -a for feminine: 'profesora'."
            },
            {
                "id": "d41-ex3",
                "type": "multiple-choice",
                "prompt": "What does '¿A qué te dedicas?' mean?",
                "options": ["What is your address?", "What do you do for a living / What is your job?", "Where are you going?", "How old are you?"],
                "correct": 1,
                "explanation": "'¿A qué te dedicas?' asks what you do for a living."
            },
            {
                "id": "d41-ex4",
                "type": "translation",
                "prompt": "Translate: 'I work remotely at a tech company.'",
                "options": ["Hago teletrabajo en una empresa tecnológica.", "Soy teletrabajo en una empresa tecnológica.", "Tengo teletrabajo en una empresa tecnológica.", "Voy teletrabajo en una empresa tecnológica."],
                "correct": 0,
                "explanation": "'Hago teletrabajo en una empresa tecnológica' (or trabajo en remoto) is natural and accurate."
            }
        ],
        "speakingChallenge": [
            {"prompt": "State your profession or that you are a student without using an article.", "hint": "Soy [profesión] en...", "sampleAnswer": "Soy desarrollador de software y estudiante de español."},
            {"prompt": "Ask someone what they do for a living.", "hint": "¿A qué te dedicas?", "sampleAnswer": "Mucho gusto, ¿a qué te dedicas profesionalmente?"},
            {"prompt": "Describe your ideal work schedule.", "hint": "Mi horario ideal es...", "sampleAnswer": "Mi horario ideal es flexible y con teletrabajo para tener equilibrio personal."}
        ],
        "dailyRevision": {
            "quickQuestions": [
                "Why don't we use 'un' or 'una' after 'soy' with professions?",
                "How do professions ending in -ista form their feminine? (They don't change!)"
            ],
            "grammarRecall": "Professions: SER + profesión (sin artículo). ¿A qué te dedicas? Trabajar en [oficina/empresa]. -ista = el/la dentista.",
            "vocabRecall": ["La profesión", "El médico", "El profesor", "El ingeniero", "La empresa", "La oficina", "El teletrabajo", "¿A qué te dedicas?"]
        },
        "checklist": [
            "Stated professions without an indefinite article (Soy informático)",
            "Formed feminine professions (-o -> -a, cons -> +a, -ista unchanged)",
            "Asked '¿A qué te dedicas?' with native cadence",
            "Discussed workplaces and remote work (teletrabajo)",
            "Completed all 4 work exercises",
            "Described my career background out loud in Spanish"
        ]
    },
    {
        "day": 42,
        "stage": 5,
        "title": "School, Education & Language Learning",
        "subtitle": "Universities, subjects, exams, passing and failing, and study habits",
        "goals": [
            "Name academic subjects, educational levels, and classroom tools",
            "Talk about exams: aprobar (to pass) vs. suspender (to fail)",
            "Discuss study habits: tomar apuntes (take notes), repasar (review), sacar buenas notas (get good grades)",
            "Talk about language learning strategies and progress"
        ],
        "bengaliNote": "Education (*la educación*) is deeply valued in both Spain and Bangladesh. In Spain, students don't 'win' an exam; they **aprueban** (pass) or **suspenden** (fail). Good grades are called *buenas notas*, and top marks (10/10) are celebrated as *matrícula de honor*!",
        "vocabulary": [
            {"word": "La escuela / El colegio / El instituto", "translation": "The school / Primary school / High school", "pos": "noun", "gender": "feminine / masculine", "example": "Los niños van al colegio.", "exampleTranslation": "Children go to primary school."},
            {"word": "La universidad / La facultad", "translation": "The university / The university faculty/department", "pos": "noun", "gender": "feminine", "example": "Estudio en la Universidad Complutense de Madrid.", "exampleTranslation": "I study at Complutense University of Madrid."},
            {"word": "La asignatura / La materia", "translation": "The school/university subject", "pos": "noun", "gender": "feminine", "example": "Mi asignatura favorita es Historia.", "exampleTranslation": "My favorite subject is History."},
            {"word": "El examen (Los exámenes)", "translation": "The exam (The exams - adds accent in plural!)", "pos": "noun", "gender": "masculine", "example": "Tengo un examen de español el viernes.", "exampleTranslation": "I have a Spanish exam on Friday."},
            {"word": "Aprobar (o -> ue)", "translation": "To pass (an exam)", "pos": "verb", "gender": None, "example": "Quiero aprobar con buena nota.", "exampleTranslation": "I want to pass with a good grade."},
            {"word": "Suspender", "translation": "To fail (an exam)", "pos": "verb", "gender": None, "example": "No quiero suspender el examen.", "exampleTranslation": "I don't want to fail the exam."},
            {"word": "La nota / Sacar buenas notas", "translation": "The grade / To get good grades", "pos": "noun / phrase", "gender": "feminine", "example": "He sacado una nota excelente.", "exampleTranslation": "I have gotten an excellent grade."},
            {"word": "Tomar apuntes / notas", "translation": "To take notes", "pos": "phrase", "gender": None, "example": "Tomo apuntes durante la clase.", "exampleTranslation": "I take notes during the class."},
            {"word": "La biblioteca", "translation": "The library (distinct from librería = bookstore!)", "pos": "noun", "gender": "feminine", "example": "Estudio en silencio en la biblioteca.", "exampleTranslation": "I study in silence in the library."},
            {"word": "El curso / La beca", "translation": "The course, academic year / The scholarship, grant", "pos": "noun", "gender": "masculine / feminine", "example": "Tiene una beca para estudiar en España.", "exampleTranslation": "He/she has a scholarship to study in Spain."}
        ],
        "sentences": [
            {"spanish": "Estoy estudiando mucho para aprobar el examen A1.", "english": "I am studying hard to pass the A1 exam."},
            {"spanish": "¿Cuántas asignaturas tienes este semestre?", "english": "How many subjects do you have this semester?"},
            {"spanish": "Siempre tomo apuntes detallados en mi cuaderno de gramática.", "english": "I always take detailed notes in my grammar notebook."},
            {"spanish": "En la biblioteca universitaria hay un ambiente de estudio excelente.", "english": "In the university library there is an excellent study atmosphere."},
            {"spanish": "He sacado un sobresaliente en la prueba de vocabulario.", "english": "I got an outstanding (A+) on the vocabulary quiz."},
            {"spanish": "Aprender un idioma requiere constancia, paciencia y curiosidad.", "english": "Learning a language requires consistency, patience, and curiosity."}
        ],
        "grammar": {
            "title": "Academic Idioms, False Friends (Biblioteca vs. Librería) & The Spanish Grading Scale",
            "explanation": "The educational system in Spain has unique grading scales and false friend pitfalls you must avoid.",
            "rules": [
                "False Friend Warning (Biblioteca vs. Librería): **La biblioteca** = Library (where you borrow books for free). **La librería** = Bookstore (where you buy books)! Never say 'voy a la librería a estudiar'.",
                "Aprobar vs. Suspender: *Aprobar* (to pass - stem changer o -> ue: *apruebo, apruebas, aprueba...*). *Suspender* (to fail a test: *suspendió el examen*).",
                "Grading Scale in Spain (0 to 10): 0–4.9: *Suspenso* (Fail) | 5.0–6.9: *Aprobado* (Pass) | 7.0–8.9: *Notable* (Good/Very Good) | 9.0–10: *Sobresaliente* (Outstanding/A+) | Top student: *Matrícula de Honor*.",
                "Accent Shift in Examen: *Examen* has no written accent (ends in -n, natural stress on ex-A-men). But plural *Exámenes* REQUIRES an accent because it is proparoxytone (stress on ex-Á-me-nes)!"
            ],
            "structures": [
                "Pass/Fail: Aprobar el examen / Suspender el examen",
                "Grades: Sacar buenas / malas notas / Sacar un diez",
                "Notes: Tomar apuntes en [cuaderno / ordenador]"
            ],
            "examples": [
                {"spanish": "Apruebo todos mis exámenes si estudio con tiempo.", "english": "I pass all my exams if I study with time."},
                {"spanish": "Voy a la biblioteca central a leer.", "english": "I go to the central library to read."},
                {"spanish": "Compré un diccionario en la librería de viejo.", "english": "I bought a dictionary at the second-hand bookstore."},
                {"spanish": "Tengo que preparar tres exámenes finales.", "english": "I have to prepare three final exams."}
            ],
            "commonMistakes": [
                {"wrong": "Estudio en la librería", "right": "Estudio en la biblioteca", "explanation": "'Librería' is a shop that sells books. 'Biblioteca' is the library where you study."},
                {"wrong": "Pasé el examen (anglicism)", "right": "Aprobé el examen", "explanation": "In Spain, 'to pass an exam' is 'aprobar'."}
            ],
            "proTip": "In Spain, university professors are addressed politely by their title: *«Profesor / Profesora»* or simply *«Don / Doña [First Name]»*. But among university peers, everyone calls each other *tú* immediately!"
        },
        "conversation": {
            "title": "After the Spanish Grammar Exam",
            "context": "Sakib and his classmate Carlos discuss their test results outside the classroom.",
            "dialogue": [
                {"speaker": "Carlos", "role": "Classmate", "spanish": "¡Sakib! ¿Has visto las notas del examen en el tablón?", "english": "Sakib! Have you seen the exam grades on the bulletin board?"},
                {"speaker": "Sakib", "role": "Student", "spanish": "Todavía no he mirado. ¿Qué tal te ha ido a ti?", "english": "I haven't looked yet. How did it go for you?"},
                {"speaker": "Carlos", "role": "Classmate", "spanish": "¡He aprobado con un notable! Un ocho sobre diez. ¡Estoy contentísimo!", "english": "I passed with a notable! An eight out of ten. I am super happy!"},
                {"speaker": "Sakib", "role": "Student", "spanish": "¡Enhorabuena, Carlos! Voy a mirar mi nota ahora mismo...", "english": "Congratulations, Carlos! I'm going to look at my grade right now..."},
                {"speaker": "Carlos", "role": "Classmate", "spanish": "¿Y qué has sacado?", "english": "And what did you get?"},
                {"speaker": "Sakib", "role": "Student", "spanish": "¡Un nueve con cinco! ¡Sobresaliente! Valió la pena estudiar tanto en la biblioteca.", "english": "A nine point five! Outstanding! It was worth studying so much in the library."},
                {"speaker": "Carlos", "role": "Classmate", "spanish": "¡Madre mía, eres un genio! Tenemos que celebrarlo con un buen café.", "english": "My goodness, you're a genius! We have to celebrate with a good coffee."}
            ],
            "keyPhrases": [
                {"phrase": "¡Enhorabuena!", "explanation": "Formal, hearty congratulations (synonym of ¡Felicidades!)."},
                {"phrase": "Valió la pena", "explanation": "'It was worth the effort / trouble'."},
                {"phrase": "¡Madre mía!", "explanation": "Ubiquitous Spain interjection: 'My goodness! / Wow!'"}
            ]
        },
        "reading": {
            "title": "La tradición universitaria en España: De Salamanca al presente",
            "passage": "España alberga algunas de las instituciones universitarias más antiguas del mundo occidental. La Universidad de Salamanca, fundada en el año 1218, es la universidad hispanohablante más antigua que existe y una de las más prestigiosas de Europa. Por sus aulas históricas pasaron figuras universales como Miguel de Cervantes, San Juan de la Cruz y Miguel de Unamuno. Hoy en día, el sistema universitario español acoge a más de cien mil estudiantes internacionales cada año a través de programas como Erasmus y cursos de inmersión lingüística. Estudiar en España permite no solo adquirir conocimientos académicos de primer nivel, sino sumergirse en una tradición cultural que valora la libre discusión de ideas y el amor por el conocimiento.",
            "translation": "Spain houses some of the oldest university institutions in the Western world. The University of Salamanca, founded in the year 1218, is the oldest Spanish-speaking university in existence and one of the most prestigious in Europe. Through its historic classrooms passed universal figures like Miguel de Cervantes, Saint John of the Cross, and Miguel de Unamuno. Nowadays, the Spanish university system welcomes more than one hundred thousand international students each year through programs like Erasmus and language immersion courses. Studying in Spain allows one not only to acquire top-tier academic knowledge, but to immerse oneself in a cultural tradition that values the free discussion of ideas and the love of knowledge.",
            "questions": [
                {"question": "¿En qué año fue fundada la Universidad de Salamanca?", "options": ["En 1992", "En 1218", "En 1492", "En 1800"], "answer": 1, "explanation": "In 1218 ('fundada en el año 1218')."},
                {"question": "¿Cuántos estudiantes internacionales acoge España cada año?", "options": ["Solo quinientos", "Más de cien mil estudiantes", "Diez millones", "Ninguno"], "answer": 1, "explanation": "More than 100,000 ('más de cien mil')."},
                {"question": "¿Qué famoso escritor estudió o estuvo vinculado a Salamanca?", "options": ["Shakespeare", "Miguel de Cervantes", "Dante", "Goethe"], "answer": 1, "explanation": "Miguel de Cervantes."}
            ]
        },
        "exercises": [
            {
                "id": "d42-ex1",
                "type": "multiple-choice",
                "prompt": "Where do you go to study in silence for free: biblioteca or librería?",
                "options": ["A la biblioteca", "A la librería", "Al supermercado", "A la farmacia"],
                "correct": 0,
                "explanation": "The library is 'la biblioteca'. ('Librería' is a bookshop)."
            },
            {
                "id": "d42-ex2",
                "type": "fill-in",
                "prompt": "Conjugate APROBAR (o -> ue) for 'yo': Yo ______ (aprobar) todos los exámenes.",
                "options": ["apruebo", "aprobo", "aprueba", "aprobamos"],
                "correct": 0,
                "explanation": "Yo form changes o -> ue: 'apruebo'."
            },
            {
                "id": "d42-ex3",
                "type": "multiple-choice",
                "prompt": "What does 'sobresaliente' mean on a Spanish report card?",
                "options": ["Fail (0-4.9)", "Pass (5-6.9)", "Notable (7-8.9)", "Outstanding / A+ (9-10)"],
                "correct": 3,
                "explanation": "'Sobresaliente' represents top marks (9.0–10)."
            },
            {
                "id": "d42-ex4",
                "type": "translation",
                "prompt": "Translate: 'I always take notes in class.'",
                "options": ["Siempre tomo apuntes en clase.", "Siempre tengo notas en clase.", "Siempre hago apuntes en clase.", "Siempre escribo libro en clase."],
                "correct": 0,
                "explanation": "'Tomar apuntes' is the accurate idiom for taking notes."
            }
        ],
        "speakingChallenge": [
            {"prompt": "Say that you study hard to pass your Spanish exams.", "hint": "Estudio mucho para aprobar...", "sampleAnswer": "Estudio todos los días con constancia para aprobar mi examen de español con buena nota."},
            {"prompt": "Congratulate a classmate on getting a great grade.", "hint": "¡Enhorabuena por tu...", "sampleAnswer": "¡Enhorabuena por tu nota, Carlos! Te lo mereces por estudiar tanto."},
            {"prompt": "Explain the difference between 'biblioteca' and 'librería' in your own words.", "hint": "La biblioteca es para... y la librería es para...", "sampleAnswer": "La biblioteca es para estudiar y leer libros gratis; la librería es una tienda para comprar libros."}
        ],
        "dailyRevision": {
            "quickQuestions": [
                "What is the difference between 'la biblioteca' and 'la librería'?",
                "What verb means 'to pass an exam' in Spanish? (aprobar)"
            ],
            "grammarRecall": "Academic: Aprobar (o->ue) vs. suspender. Tomar apuntes. Biblioteca (library) vs. librería (bookstore). Examen -> Exámenes (accents).",
            "vocabRecall": ["La universidad", "La asignatura", "El examen", "Aprobar", "Suspender", "La nota", "Tomar apuntes", "La biblioteca"]
        },
        "checklist": [
            "Avoided the false friend trap: biblioteca vs. librería",
            "Used 'aprobar' (pass) and 'suspender' (fail) with exams",
            "Understood Spain's 0–10 grading scale (sobresaliente, notable)",
            "Applied the accent shift: examen (singular) vs exámenes (plural)",
            "Completed all 4 education exercises",
            "Congratulated a study partner aloud with '¡Enhorabuena!'"
        ]
    },
    {
        "day": 43,
        "stage": 5,
        "title": "Health, Body Parts & Common Ailments",
        "subtitle": "Anatomy, the verb DOLER (Me duele / Me duelen), pharmacy visits, and remedies",
        "goals": [
            "Name the main parts of the human body (cabeza, ojos, garganta, espalda, estómago)",
            "Master the verb DOLER (to hurt): works identical to GUSTAR (*Me duele* vs. *Me duelen*)",
            "Express common symptoms: tener fiebre, estar resfriado, tener tos, tener gripe",
            "Communicate symptoms at a Spanish pharmacy (*farmacia*)"
        ],
        "bengaliNote": "The verb **DOLER** works on the exact same logic as GUSTAR and Bangla! In English, you say 'My head hurts'. In Bangla, you say: 'আমার মাথা ব্যথা করছে' (To me, the head is painful). In Spanish: *Me duele la cabeza* (The head hurts to me). If plural (like eyes or legs), it becomes *Me duelen*: *Me duelen los ojos*!",
        "vocabulary": [
            {"word": "El cuerpo (humano)", "translation": "The (human) body", "pos": "noun", "gender": "masculine", "example": "Cuidar el cuerpo es esencial.", "exampleTranslation": "Taking care of the body is essential."},
            {"word": "La cabeza / Los ojos / La garganta", "translation": "Head / Eyes / Throat", "pos": "noun", "gender": "mixed", "example": "Me duele la cabeza.", "exampleTranslation": "My head hurts."},
            {"word": "La espalda / El estómago / El brazo / La pierna", "translation": "Back / Stomach / Arm / Leg", "pos": "noun", "gender": "mixed", "example": "Me duele la espalda de estar sentado.", "exampleTranslation": "My back hurts from being seated."},
            {"word": "Doler (o -> ue: me duele / me duelen)", "translation": "To hurt / To cause pain (like gustar)", "pos": "verb", "gender": None, "example": "¿Qué te duele?", "exampleTranslation": "What hurts you?"},
            {"word": "Estar resfriado(a) / acatarrado(a)", "translation": "To have a cold", "pos": "phrase", "gender": "masculine / feminine", "example": "Estoy resfriado, tengo mocos.", "exampleTranslation": "I have a cold, I have a runny nose."},
            {"word": "Tener fiebre / Tener tos", "translation": "To have fever / To have a cough", "pos": "phrase", "gender": None, "example": "Tiene treinta y ocho de fiebre.", "exampleTranslation": "He/she has 38 degrees of fever."},
            {"word": "La gripe", "translation": "The flu / influenza", "pos": "noun", "gender": "feminine", "example": "Tengo gripe y tengo que quedarme en cama.", "exampleTranslation": "I have the flu and have to stay in bed."},
            {"word": "El medicamento / La medicina / La pastilla", "translation": "Medication / Medicine / Pill, tablet", "pos": "noun", "gender": "mixed", "example": "Tomo una pastilla cada ocho horas.", "exampleTranslation": "I take a pill every eight hours."},
            {"word": "El jarabe (para la tos)", "translation": "Syrup (cough syrup)", "pos": "noun", "gender": "masculine", "example": "Un jarabe para calmar la tos.", "exampleTranslation": "A syrup to soothe the cough."},
            {"word": "¡Que te mejores!", "translation": "Get well soon!", "pos": "phrase", "gender": None, "example": "Cuídate mucho, ¡que te mejores pronto!", "exampleTranslation": "Take good care, get well soon!"}
        ],
        "sentences": [
            {"spanish": "Me duele mucho la cabeza, necesito una aspirina.", "english": "My head hurts a lot, I need an aspirin. (Singular -> duele)"},
            {"spanish": "Me duelen los ojos de mirar la pantalla tantas horas.", "english": "My eyes hurt from looking at the screen so many hours. (Plural -> duelen)"},
            {"spanish": "¿Tienes fiebre? —Sí, tengo treinta y ocho con cinco.", "english": "Do you have a fever? —Yes, I have thirty-eight point five."},
            {"spanish": "Estoy resfriado y me duele la garganta al tragar.", "english": "I have a cold and my throat hurts when swallowing."},
            {"spanish": "Tome esta pastilla después de comer con un vaso de agua.", "english": "Take this pill after eating with a glass of water."},
            {"spanish": "Si no mejoras en dos días, tienes que ir al médico.", "english": "If you don't improve in two days, you have to go to the doctor."}
        ],
        "grammar": {
            "title": "The Master Anatomy of DOLER: 'Me duele' vs. 'Me duelen'",
            "explanation": "Like GUSTAR, DOLER changes based on the body part that hurts, NOT based on the person feeling the pain!",
            "rules": [
                "1. Singular Body Part: **Me duele + el / la [parte singular]**. E.g. *Me duele la cabeza* (My head hurts), *Me duele el estómago* (My stomach hurts).",
                "2. Plural Body Parts: **Me duelen + los / las [partes plurales]**. E.g. *Me duelen los pies* (My feet hurt), *Me duelen las piernas* (My legs hurt).",
                "Indirect Object Pronouns: me duele(n) | te duele(n) | le duele(n) | nos duele(n) | os duele(n) | les duele(n).",
                "Definite Articles Required: Always say *Me duele LA cabeza*, NEVER *Me duele mi cabeza*! The pronoun 'me' already shows whose head it is.",
                "Illness expressions: 1) ESTAR resfriado(a) / enfermo(a). 2) TENER fiebre / tos / gripe / dolor de cabeza."
            ],
            "structures": [
                "Singular Pain: [me/te/le/nos/os/les] + DUELE + el/la [parte del cuerpo]",
                "Plural Pain: [me/te/le/nos/os/les] + DUELEN + los/las [partes del cuerpo]",
                "Symptoms: Tener + fiebre / tos / dolor de [parte]"
            ],
            "examples": [
                {"spanish": "A Carlos le duele la muela.", "english": "Carlos has a toothache (tooth hurts him)."},
                {"spanish": "¿Te duelen los oídos?", "english": "Do your ears hurt?"},
                {"spanish": "Nos duelen las piernas después de correr.", "english": "Our legs hurt after running."},
                {"spanish": "Tengo un dolor de cabeza terrible.", "english": "I have a terrible headache."}
            ],
            "commonMistakes": [
                {"wrong": "Mi cabeza duele", "right": "Me duele la cabeza", "explanation": "Spanish uses the indirect object structure 'me duele la cabeza'."},
                {"wrong": "Me duele los ojos", "right": "Me duelen los ojos", "explanation": "Because 'ojos' is plural, the verb must be 'duelen'."}
            ],
            "proTip": "In Spain, you do not need an appointment to consult a pharmacist at the **farmacia**. Spanish pharmacists (*farmacéuticos*) are highly trained healthcare professionals and can recommend over-the-counter remedies for mild ailments right across the counter!"
        },
        "conversation": {
            "title": "At the Neighborhood Pharmacy in Madrid",
            "context": "Sakib visits the local pharmacy on Calle Fuencarral with cold symptoms.",
            "dialogue": [
                {"speaker": "Farmacéutica", "role": "Pharmacist", "spanish": "¡Hola! Buenas tardes. ¿En qué le puedo ayudar?", "english": "Hello! Good afternoon. How can I help you?"},
                {"speaker": "Sakib", "role": "Patient", "spanish": "Buenas tardes. Desde ayer me duele mucho la garganta y tengo tos seca.", "english": "Good afternoon. Since yesterday my throat hurts a lot and I have a dry cough."},
                {"speaker": "Farmacéutica", "role": "Pharmacist", "spanish": "¿Tiene fiebre o dolor de cabeza?", "english": "Do you have a fever or headache?"},
                {"speaker": "Sakib", "role": "Patient", "spanish": "No tengo fiebre, pero sí me duele un poco la cabeza y estoy resfriado.", "english": "I don't have a fever, but my head does hurt a little and I have a cold."},
                {"speaker": "Farmacéutica", "role": "Pharmacist", "spanish": "Le recomiendo estas pastillas para chupar para el dolor de garganta y este jarabe natural para calmar la tos.", "english": "I recommend these lozenges to suck on for the sore throat and this natural syrup to soothe the cough."},
                {"speaker": "Sakib", "role": "Patient", "spanish": "¿Cómo tengo que tomarlas?", "english": "How do I have to take them?"},
                {"speaker": "Farmacéutica", "role": "Pharmacist", "spanish": "Una pastilla cada cuatro horas y una cucharada de jarabe antes de acostarse. Beba mucho líquido caliente.", "english": "One lozenge every four hours and a spoonful of syrup before going to bed. Drink plenty of warm liquids."},
                {"speaker": "Sakib", "role": "Patient", "spanish": "Muchas gracias. ¿Cuánto es en total?", "english": "Thank you very much. How much is it in total?"},
                {"speaker": "Farmacéutica", "role": "Pharmacist", "spanish": "Son ocho euros con cincuenta. ¡Que se mejore pronto!", "english": "That is eight euros and fifty. Get well soon!"}
            ],
            "keyPhrases": [
                {"phrase": "Pastillas para chupar", "explanation": "Throat lozenges to dissolve/suck on."},
                {"phrase": "Tos seca", "explanation": "'Dry cough'."},
                {"phrase": "¡Que se mejore!", "explanation": "Polite formal 'Get well soon!'"}
            ]
        },
        "reading": {
            "title": "El sistema de salud y la figura de la farmacia en España",
            "passage": "El sistema sanitario español es reconocido internacionalmente como uno de los más eficientes del mundo. Se basa en una atención primaria cercana y gratuita para todos los residentes a través de los Centros de Salud de cada barrio. Sin embargo, para dolencias leves cotidianas como resfriados, dolores de garganta o pequeñas molestias estomacales, la primera línea de ayuda es siempre la farmacia de barrio. En España, las farmacias están señalizadas con una cruz verde brillante que parpadea en la calle. Los farmacéuticos escuchan con paciencia los síntomas de los vecinos y recomiendan los medicamentos adecuados. Además, existe una red rotatoria de farmacias de guardia abiertas las veinticuatro horas para atender cualquier urgencia nocturna.",
            "translation": "The Spanish healthcare system is internationally recognized as one of the most efficient in the world. It is based on close, free primary care for all residents through neighborhood Health Centers. However, for everyday mild ailments like colds, sore throats, or slight stomach aches, the first line of help is always the neighborhood pharmacy. In Spain, pharmacies are signaled with a bright green cross blinking on the street. Pharmacists listen patiently to neighbors' symptoms and recommend appropriate medications. Furthermore, there is a rotating network of 24-hour on-duty pharmacies open day and night to assist any nighttime emergency.",
            "questions": [
                {"question": "¿Cuál es la primera línea de ayuda para dolencias leves en España?", "options": ["El hospital de urgencias mayores", "La farmacia de barrio", "Buscar en internet solo", "El dentista"], "answer": 1, "explanation": "The neighborhood pharmacy ('la farmacia de barrio')."},
                {"question": "¿De qué color es la cruz que parpadea en las farmacias españolas?", "options": ["Azul", "Cruz verde brillante", "Negra", "Amarilla"], "answer": 1, "explanation": "Bright green cross ('una cruz verde brillante')."},
                {"question": "¿Qué son las 'farmacias de guardia'?", "options": ["Farmacias cerradas", "Farmacias abiertas las veinticuatro horas para urgencias", "Farmacias para animales", "Solo para médicos"], "answer": 1, "explanation": "24-hour on-duty emergency pharmacies."}
            ]
        },
        "exercises": [
            {
                "id": "d43-ex1",
                "type": "fill-in",
                "prompt": "Choose duele or duelen: Me ______ (hurts) la cabeza hoy.",
                "options": ["duele", "duelen", "dolo", "doler"],
                "correct": 0,
                "explanation": "'La cabeza' is singular, so use 'duele'."
            },
            {
                "id": "d43-ex2",
                "type": "fill-in",
                "prompt": "Choose duele or duelen: Me ______ (hurt) los pies de caminar.",
                "options": ["duelen", "duele", "dolor", "dueleno"],
                "correct": 0,
                "explanation": "'Los pies' is plural, so use 'duelen'."
            },
            {
                "id": "d43-ex3",
                "type": "multiple-choice",
                "prompt": "How do you say 'Get well soon!' in Spanish?",
                "options": ["¡Que te mejores!", "¡Buen viaje!", "¡Buen provecho!", "¡De nada!"],
                "correct": 0,
                "explanation": "'¡Que te mejores!' means 'Get well soon!'."
            },
            {
                "id": "d43-ex4",
                "type": "translation",
                "prompt": "Translate: 'I have a cold and I have a fever.'",
                "options": ["Estoy resfriado y tengo fiebre.", "Soy resfriado y estoy fiebre.", "Tengo resfriado y soy fiebre.", "Hago resfriado y tengo fiebre."],
                "correct": 0,
                "explanation": "'Estar resfriado' (state) and 'tener fiebre' (symptom) are the proper verb pairings."
            }
        ],
        "speakingChallenge": [
            {"prompt": "Say that your throat hurts and you have a cold.", "hint": "Me duele la garganta y...", "sampleAnswer": "Me duele mucho la garganta y estoy bastante resfriado."},
            {"prompt": "Ask a pharmacist for medicine for a headache.", "hint": "Buenos días, me duele la cabeza, ¿tiene...?", "sampleAnswer": "Buenos días, me duele mucho la cabeza, ¿tiene alguna pastilla para el dolor?"},
            {"prompt": "Wish a sick friend to get well soon.", "hint": "¡Que te mejores pronto!", "sampleAnswer": "Descansa mucho amigo, ¡que te mejores muy pronto!"}
        ],
        "dailyRevision": {
            "quickQuestions": [
                "How does the verb DOLER conjugate? (Me duele singular vs. me duelen plural)",
                "Why don't we say 'me duele mi cabeza'?"
            ],
            "grammarRecall": "DOLER: me/te/le/nos/os/les + duele (singular body part) or duelen (plural body parts). Estar resfriado, tener fiebre/tos.",
            "vocabRecall": ["El cuerpo", "La cabeza", "Los ojos", "La garganta", "Doler", "Estar resfriado", "Tener fiebre", "La pastilla", "¡Que te mejores!"]
        },
        "checklist": [
            "Named core human anatomy parts in Spanish",
            "Applied DOLER matching body part count (duele vs. duelen)",
            "Used definite articles with body parts (la cabeza, los ojos)",
            "Expressed common illness symptoms (fiebre, tos, resfriado)",
            "Completed all 4 health exercises",
            "Practiced pharmacy consultation dialogue out loud"
        ]
    },
    {
        "day": 44,
        "stage": 5,
        "title": "Possessive Adjectives & Stressed Possessives",
        "subtitle": "Mi/Tu/Su vs. Nuestro/Vuestro & Stressed Mío, Tuyo, Suyo",
        "goals": [
            "Review short unstressed possessive adjectives: mi/mis, tu/tus, su/sus",
            "Master plural possessives with gender agreement: nuestro/a/os/as and vuestro/a/os/as",
            "Learn stressed possessive pronouns (mío, tuyo, suyo, nuestro) used after nouns",
            "Say 'It is mine / It belongs to me' (*Es mío / Es mía*)"
        ],
        "bengaliNote": "Possessives in Spanish have two distinct forms: 1) Short forms before the noun (*mi casa* = আমার বাড়ি); 2) Stressed long forms after the noun or standing alone (*Esta casa es mía* = এই বাড়িটি আমার). Notice that *nuestro* (our) and *vuestro* (your plural) MUST agree in BOTH gender and number with the item (*nuestro libro, nuestra casa, nuestros amigos, nuestras clases*)!",
        "vocabulary": [
            {"word": "Mi / Mis", "translation": "My (singular / plural)", "pos": "possessive adjective", "gender": None, "example": "Mi libro y mis cuadernos.", "exampleTranslation": "My book and my notebooks."},
            {"word": "Tu / Tus", "translation": "Your (informal singular / plural)", "pos": "possessive adjective", "gender": None, "example": "Tu ciudad y tus amigos.", "exampleTranslation": "Your city and your friends."},
            {"word": "Su / Sus", "translation": "His / Her / Your formal / Their", "pos": "possessive adjective", "gender": None, "example": "Su coche y sus llaves.", "exampleTranslation": "His/her car and his/her keys."},
            {"word": "Nuestro / Nuestra / Nuestros / Nuestras", "translation": "Our (has 4 forms matching gender and number!)", "pos": "possessive adjective", "gender": "variable", "example": "Nuestra casa es muy luminosa.", "exampleTranslation": "Our house is very bright."},
            {"word": "Vuestro / Vuestra / Vuestros / Vuestras", "translation": "Your plural (informal in Spain - 4 forms!)", "pos": "possessive adjective", "gender": "variable", "example": "¿Dónde está vuestro hotel?", "exampleTranslation": "Where is you all's hotel?"},
            {"word": "Mío / Mía / Míos / Mías", "translation": "Mine (stressed possessive)", "pos": "possessive pronoun", "gender": "variable", "example": "Este teléfono es mío.", "exampleTranslation": "This phone is mine."},
            {"word": "Tuyo / Tuya / Tuyos / Tuyas", "translation": "Yours (informal stressed)", "pos": "possessive pronoun", "gender": "variable", "example": "¿Esta chaqueta es tuya?", "exampleTranslation": "Is this jacket yours?"},
            {"word": "Suyo / Suya / Suyos / Suyas", "translation": "His / Hers / Theirs / Yours formal", "pos": "possessive pronoun", "gender": "variable", "example": "Ese libro es suyo.", "exampleTranslation": "That book is his/hers."},
            {"word": "¿De quién es...?", "translation": "Whose is...? (asking ownership)", "pos": "phrase", "gender": None, "example": "¿De quién es este bolígrafo?", "exampleTranslation": "Whose pen is this?"},
            {"word": "La propiedad / Pertenecer", "translation": "The property / To belong to", "pos": "noun / verb", "gender": "feminine", "example": "Me pertenece a mí.", "exampleTranslation": "It belongs to me."}
        ],
        "sentences": [
            {"spanish": "Nuestra profesora de español es muy paciente y amable.", "english": "Our Spanish teacher is very patient and kind. (nuestra: fem sing)"},
            {"spanish": "¿Son vuestros estos abrigos colgados en la entrada?", "english": "Are these coats hanging in the entrance yours? (vuestros: masc plur)"},
            {"spanish": "¿De quién es esta mochila? —Es mía, gracias.", "english": "Whose backpack is this? —It is mine, thank you. (mía: fem sing)"},
            {"spanish": "Mis padres están muy contentos con nuestros progresos.", "english": "My parents are very happy with our progress."},
            {"spanish": "Ese paraguas no es tuyo, es de Carlos.", "english": "That umbrella is not yours, it is Carlos's."},
            {"spanish": "Nuestros sueños son grandes y trabajamos duro para lograrlos.", "english": "Our dreams are big and we work hard to achieve them."}
        ],
        "grammar": {
            "title": "Unstressed vs. Stressed Possessives & 'Nuestro/Vuestro' 4-Way Agreement",
            "explanation": "Spanish possessives must always match the GENDER and NUMBER of the object owned, never the owner!",
            "rules": [
                "Unstressed Possessives (Before the noun): mi/mis, tu/tus, su/sus (only change for number). BUT **nuestro** and **vuestro** change for BOTH gender and number: *nuestro padre*, *nuestra madre*, *nuestros padres*, *nuestras madres*.",
                "Stressed Possessives (After the noun or with SER): mío, tuyo, suyo, nuestro, vuestro. E.g. *Es mío* (It's mine), *¿Es tuya esta cartera?* (Is this wallet yours?).",
                "Asking Ownership: Use **¿De quién es [singular]?** or **¿De quiénes son [plural]?**: *¿De quién es este móvil?* -> *Es de Sakib* / *Es mío*.",
                "Pronoun Accent Reminder: *Tú* (you) has an accent; *tu* (your) does not! *Mí* (prepositional me) has an accent; *mi* (my) does not!"
            ],
            "structures": [
                "Before noun: mi / tu / su / nuestro(a) / vuestro(a) + [Sustantivo]",
                "After SER: [Objeto] + es / son + mío(a) / tuyo(a) / suyo(a) / nuestro(a)",
                "Query: ¿De quién es este / esta [Objeto]?"
            ],
            "examples": [
                {"spanish": "Nuestra ciudad es hermosa.", "english": "Our city is beautiful."},
                {"spanish": "¿Dónde están vuestros amigos?", "english": "Where are your (plural) friends?"},
                {"spanish": "El libro es mío. (Masc)", "english": "The book is mine."},
                {"spanish": "La decisión es tuya. (Fem)", "english": "The decision is yours."}
            ],
            "commonMistakes": [
                {"wrong": "Nuestro casa", "right": "Nuestra casa", "explanation": "'Casa' is feminine, so 'nuestro' must agree: 'nuestra casa'."},
                {"wrong": "Es de mí (meaning it's mine)", "right": "Es mío / Es mía", "explanation": "Say 'Es mío' or 'Es mía'."}
            ],
            "proTip": "In Spanish, a beloved polite way to invite someone into your home: **«Esta es mi casa, y a partir de ahora es vuestra casa»** (This is my house, and from now on it is your house — Mi casa es su casa)!"
        },
        "conversation": {
            "title": "Finding a Lost Item in Class",
            "context": "Sakib and his classmates pack up their bags at the end of class.",
            "dialogue": [
                {"speaker": "Profesora", "role": "Teacher", "spanish": "Chicos, antes de salir, ¿de quién es este paraguas negro que está encima de la mesa?", "english": "Guys, before leaving, whose is this black umbrella on top of the table?"},
                {"speaker": "Carlos", "role": "Classmate", "spanish": "Mío no es, el mío es azul marino.", "english": "It's not mine, mine is navy blue."},
                {"speaker": "Sakib", "role": "Student", "spanish": "A ver... ¡Ah, sí, es mío! Lo he olvidado al entrar. ¡Muchas gracias, profesora!", "english": "Let's see... Ah, yes, it's mine! I forgot it when entering. Thank you very much, professor!"},
                {"speaker": "Profesora", "role": "Teacher", "spanish": "De nada, Sakib. Y estos apuntes de gramática, ¿son vuestros?", "english": "You're welcome, Sakib. And these grammar notes, are they you all's?"},
                {"speaker": "Carlos", "role": "Classmate", "spanish": "Sí, son nuestros apuntes compartidos. Nos los llevamos. ¡Hasta mañana!", "english": "Yes, they are our shared notes. We'll take them. See you tomorrow!"}
            ],
            "keyPhrases": [
                {"phrase": "¿De quién es...?", "explanation": "'Whose is...?' (inquiry of ownership)."},
                {"phrase": "El mío es azul", "explanation": "'Mine is blue' (using stressed possessive with article)."},
                {"phrase": "Son nuestros apuntes", "explanation": "'They are our notes'."}
            ]
        },
        "reading": {
            "title": "La hospitalidad española y el sentido de comunidad",
            "passage": "En la cultura española, compartir las cosas es un valor natural. Existe una frase famosa en todo el mundo hispanohablante: «Mi casa es tu casa». Cuando una persona entra como invitada en un hogar español, los anfitriones no solo ofrecen comida abundante y bebida fresca, sino que hacen sentir al huésped que el espacio le pertenece. Las familias comparten los platos en el centro de la mesa al grito de «¡Venga, esto es de todos!». Sakib experimenta esta cálida generosidad cuando sus amigos madrileños le invitan a sus casas los fines de semana. Para Sakib, descubrir que la hospitalidad española es tan parecida a la cálida bienvenida bengalí ha sido una de las mayores alegrías de su viaje.",
            "translation": "In Spanish culture, sharing things is a natural value. There exists a phrase famous throughout the entire Spanish-speaking world: 'Mi casa es tu casa' (My house is your house). When a person enters as a guest in a Spanish home, hosts not only offer abundant food and fresh drinks, but make the guest feel that the space belongs to them. Families share dishes in the center of the table shouting 'Come on, this is for everyone!'. Sakib experiences this warm generosity when his Madrid friends invite him to their homes on weekends. For Sakib, discovering that Spanish hospitality is so similar to the warm Bengali welcome has been one of the greatest joys of his journey.",
            "questions": [
                {"question": "¿Qué frase famosa resume la hospitalidad española?", "options": ["No toques nada", "Mi casa es tu casa", "Paga la cuenta primero", "Vuelve mañana"], "answer": 1, "explanation": "'Mi casa es tu casa' ('existe una frase famosa...')."},
                {"question": "¿Dónde ponen las familias los platos al comer juntos?", "options": ["En el suelo", "En el centro de la mesa para compartir entre todos", "Cada uno en su habitación", "En la cocina"], "answer": 1, "explanation": "In the center of the table to share ('en el centro de la mesa...')."},
                {"question": "¿A qué se parece la hospitalidad española según Sakib?", "options": ["A la soledad", "A la cálida bienvenida bengalí", "A un examen difícil", "A una oficina fría"], "answer": 1, "explanation": "To the warm Bengali welcome ('a la cálida bienvenida bengalí')."}
            ]
        },
        "exercises": [
            {
                "id": "d44-ex1",
                "type": "fill-in",
                "prompt": "Make 'nuestro' agree with 'casa': ______ (Our) casa es luminosa.",
                "options": ["Nuestra", "Nuestro", "Nuestros", "Nuestras"],
                "correct": 0,
                "explanation": "'Casa' is feminine singular, so use 'Nuestra'."
            },
            {
                "id": "d44-ex2",
                "type": "fill-in",
                "prompt": "Choose the stressed possessive: Esta mochila es ______ (mine).",
                "options": ["mía", "mío", "mi", "mis"],
                "correct": 0,
                "explanation": "'Mochila' is feminine singular, so 'mine' is 'mía'."
            },
            {
                "id": "d44-ex3",
                "type": "multiple-choice",
                "prompt": "How do you ask 'Whose is this phone?' in Spanish?",
                "options": ["¿De quién es este teléfono?", "¿Quién tiene este teléfono?", "¿Dónde es este teléfono?", "¿Cuánto cuesta este teléfono?"],
                "correct": 0,
                "explanation": "'¿De quién es este teléfono?' asks for ownership."
            },
            {
                "id": "d44-ex4",
                "type": "translation",
                "prompt": "Translate: 'Are these books yours?' (informal)",
                "options": ["¿Son tuyos estos libros?", "¿Son tus estos libros?", "¿Son míos estos libros?", "¿Son suyos tus libros?"],
                "correct": 0,
                "explanation": "'¿Son tuyos estos libros?' uses stressed possessive 'tuyos' agreeing with masculine plural libros."
            }
        ],
        "speakingChallenge": [
            {"prompt": "Say that something is yours using 'Es mío' or 'Es mía'.", "hint": "Este libro es...", "sampleAnswer": "Este cuaderno de notas en español es mío."},
            {"prompt": "Say that our class or our school is great using 'Nuestra...'", "hint": "Nuestra escuela es...", "sampleAnswer": "Nuestra escuela de español es fantástica y nuestros profesores son amables."},
            {"prompt": "Ask whose jacket is on the chair.", "hint": "¿De quién es esta chaqueta que...", "sampleAnswer": "Disculpad, ¿de quién es esta chaqueta que está encima de la silla?"}
        ],
        "dailyRevision": {
            "quickQuestions": [
                "Why does 'nuestro' have 4 forms (nuestro, nuestra, nuestros, nuestras)?",
                "What is the difference between 'mi libro' and 'el libro es mío'?"
            ],
            "grammarRecall": "Possessives: mi, tu, su, nuestro/a/os/as, vuestro/a/os/as. Stressed: mío/a, tuyo/a, suyo/a. ¿De quién es...?",
            "vocabRecall": ["Mi / Mis", "Tu / Tus", "Su / Sus", "Nuestro(a)", "Vuestro(a)", "Mío(a)", "Tuyo(a)", "¿De quién es?"]
        },
        "checklist": [
            "Applied 4-way agreement to 'nuestro' and 'vuestro' (gender & number)",
            "Used stressed possessives after SER (es mío, es tuya)",
            "Asked ownership with '¿De quién es / de quiénes son?'",
            "Differentiated unstressed adjectives from stressed pronouns",
            "Completed all 4 possessive exercises",
            "Practiced claiming and asking ownership aloud in Spanish"
        ]
    },
    {
        "day": 45,
        "stage": 5,
        "title": "Reflexive Verbs in Depth: Emotions & Social Life",
        "subtitle": "Sentirse, Acordarse, Preocuparse, Despedirse + Mid-Stage 5 Review",
        "goals": [
            "Expand reflexive verbs beyond physical hygiene into emotions and social interactions",
            "Conjugate key verbs: sentirse (to feel), acordarse de (to remember), preocuparse por (to worry about), despedirse (to say goodbye)",
            "Notice stem changes inside reflexive verbs (sentirse: e -> ie; acordarse: o -> ue; despedirse: e -> i)",
            "Complete the Stage 5 Mid-Point Revision (Days 41 to 45 review)"
        ],
        "bengaliNote": "Reflexive verbs express internal emotional states. In Bangla, we say 'আমার ভালো লাগছে' (I feel good) or 'আমি ওর কথা মনে করছি' (I remember him). In Spanish, these are reflexive: *Me siento bien* (sentirse), *Me acuerdo de él* (acordarse de). Notice how the pronoun *me* reflects the state inside you!",
        "vocabulary": [
            {"word": "Sentirse (e -> ie)", "translation": "To feel (emotionally or physically)", "pos": "reflexive verb", "gender": None, "example": "Hoy me siento muy feliz y motivado.", "exampleTranslation": "Today I feel very happy and motivated."},
            {"word": "¿Cómo te sientes?", "translation": "How do you feel?", "pos": "phrase", "gender": None, "example": "¿Cómo te sientes hoy, amigo?", "exampleTranslation": "How do you feel today, friend?"},
            {"word": "Acordarse de (o -> ue)", "translation": "To remember (always paired with 'de')", "pos": "reflexive verb", "gender": None, "example": "Me acuerdo de mi primer día de clase.", "exampleTranslation": "I remember my first day of class."},
            {"word": "Olvidarse de", "translation": "To forget about", "pos": "reflexive verb", "gender": None, "example": "No te olvides de cerrar la puerta.", "exampleTranslation": "Don't forget to close the door."},
            {"word": "Preocuparse por", "translation": "To worry about", "pos": "reflexive verb", "gender": None, "example": "No te preocupes por nada.", "exampleTranslation": "Don't worry about anything."},
            {"word": "Despedirse de (e -> i)", "translation": "To say goodbye to", "pos": "reflexive verb", "gender": None, "example": "Me despido de mis amigos en el aeropuerto.", "exampleTranslation": "I say goodbye to my friends at the airport."},
            {"word": "Quedarse (en casa / en Madrid)", "translation": "To stay / remain in a place", "pos": "reflexive verb", "gender": None, "example": "Este fin de semana me quedo en Madrid.", "exampleTranslation": "This weekend I stay in Madrid."},
            {"word": "Divertirse (e -> ie)", "translation": "To have fun / To enjoy oneself", "pos": "reflexive verb", "gender": None, "example": "Nos divertimos mucho en clase.", "exampleTranslation": "We have a lot of fun in class."},
            {"word": "Ponerse (+ adjetivo)", "translation": "To become / get (sudden emotional change)", "pos": "reflexive verb", "gender": None, "example": "Me pongo contento cuando hablo español.", "exampleTranslation": "I get happy when I speak Spanish."},
            {"word": "Enamorarse de", "translation": "To fall in love with", "pos": "reflexive verb", "gender": None, "example": "Me he enamorado de España.", "exampleTranslation": "I have fallen in love with Spain."}
        ],
        "sentences": [
            {"spanish": "¿Cómo te sientes hoy? —Me siento con mucha energía.", "english": "How do you feel today? —I feel with a lot of energy."},
            {"spanish": "Siempre me acuerdo de los consejos de mi abuelo.", "english": "I always remember my grandfather's advice."},
            {"spanish": "No te preocupes por el examen, estás muy preparado.", "english": "Don't worry about the exam, you are very prepared."},
            {"spanish": "Nos divertimos muchísimo cuando cocinamos juntos.", "english": "We have so much fun when we cook together."},
            {"spanish": "Antes de viajar, me despido de todos mis profesores.", "english": "Before traveling, I say goodbye to all my teachers."},
            {"spanish": "Los domingos me quedo en casa descansando.", "english": "On Sundays I stay at home resting."}
        ],
        "grammar": {
            "title": "Emotional Reflexives & Preposition Collocations (Acordarse DE, Preocuparse POR)",
            "explanation": "Many reflexive verbs in Spanish must be followed by a specific preposition. Learning the verb together with its preposition is essential:",
            "rules": [
                "Acordarse + DE: Always requires 'de': *Me acuerdo DE ti* (I remember you), *Me acuerdo DE la lección* (I remember the lesson). (Compare: *Recordar* is NOT reflexive and has no 'de': *Recuerdo la lección*).",
                "Preocuparse + POR: Always requires 'por': *Me preocupo POR mi futuro*, *No te preocupes POR eso*.",
                "Despedirse + DE: Always requires 'de': *Me despido DE mis compañeros* (I say goodbye to my classmates).",
                "Stem changes inside Reflexives: 1) Sentirse (e -> ie): *me siento, te sientes, se siente, nos sentimos, os sentís, se sienten*. 2) Acordarse (o -> ue): *me acuerdo, te acuerdas, se acuerda, nos acordamos, os acordáis, se acuerdan*. 3) Despedirse (e -> i): *me despido, te despides, se despide, nos despedimos, os despedís, se despiden*."
            ],
            "structures": [
                "Sentirse: me siento | te sientes | se siente | nos sentimos | os sentís | se sienten",
                "Acordarse: me acuerdo | te acuerdas | se acuerda | nos acordamos | os acordáis | se acuerdan",
                "Preposition formulas: acordarse DE / preocuparse POR / despedirse DE / enamorarse DE"
            ],
            "examples": [
                {"spanish": "Me siento orgulloso de mi progreso.", "english": "I feel proud of my progress."},
                {"spanish": "¿Te acuerdas de nuestra primera clase?", "english": "Do you remember our first class?"},
                {"spanish": "Ellos se despiden con un abrazo.", "english": "They say goodbye with a hug."},
                {"spanish": "Nos quedamos en el parque hasta el anochecer.", "english": "We stay in the park until nightfall."}
            ],
            "commonMistakes": [
                {"wrong": "Me acuerdo la fecha (missing 'de')", "right": "Me acuerdo de la fecha", "explanation": "'Acordarse' strictly requires the preposition 'de'."},
                {"wrong": "Preocuparse para algo", "right": "Preocuparse por algo", "explanation": "Worrying takes 'por' (cause), never 'para'."}
            ],
            "proTip": "Notice the difference: **Dormir** = To sleep (*Duermo ocho horas*). **Dormirse** (reflexive) = To fall asleep (*Me duermo enseguida* = I fall asleep right away)!"
        },
        "conversation": {
            "title": "A Heartfelt Conversation Over Tea",
            "context": "Sakib and his friend Elena share their feelings at the 45-day milestone.",
            "dialogue": [
                {"speaker": "Elena", "role": "Friend", "spanish": "Sakib, te veo muy sonriente. ¿Cómo te sientes hoy?", "english": "Sakib, I see you smiling a lot. How do you feel today?"},
                {"speaker": "Sakib", "role": "Student", "spanish": "Me siento muy feliz y tranquilo. La verdad es que me acuerdo de cuando llegué a Madrid y no entendía nada.", "english": "I feel very happy and peaceful. The truth is that I remember when I arrived in Madrid and understood nothing."},
                {"speaker": "Elena", "role": "Friend", "spanish": "¿Te preocupabas mucho al principio?", "english": "Did you worry a lot at first?"},
                {"speaker": "Sakib", "role": "Student", "spanish": "Sí, me preocupaba por no poder comunicarme. Pero ahora me divierto hablando en las tiendas y con la gente.", "english": "Yes, I worried about not being able to communicate. But now I have fun talking in shops and with people."},
                {"speaker": "Elena", "role": "Friend", "spanish": "¡Es que has trabajado muchísimo! Y te has enamorado de la cultura española, ¿verdad?", "english": "It's just that you've worked so hard! And you've fallen in love with Spanish culture, right?"},
                {"speaker": "Sakib", "role": "Student", "spanish": "¡Totalmente! Me encanta la calidez de la gente. Ya no me quiero despedir nunca de este idioma.", "english": "Totally! I love the warmth of the people. I don't ever want to say goodbye to this language anymore."}
            ],
            "keyPhrases": [
                {"phrase": "Sonriente", "explanation": "'Smiling / cheerful'."},
                {"phrase": "Al principio", "explanation": "'At the beginning / at first'."},
                {"phrase": "Me divierto", "explanation": "'I have fun / I enjoy myself'."}
            ]
        },
        "reading": {
            "title": "Mid-Stage 5 Review Story: Cuarenta y cinco días de superación",
            "passage": "El día cuarenta y cinco representa tres cuartas partes del camino hacia la meta. Sakib mira hacia atrás y siente una emoción profunda. Recuerda con cariño sus primeras dudas sobre los artículos y las terminaciones verbales. Hoy domina el vocabulario profesional de las empresas y oficinas, conoce el sistema educativo y sabe desenvolverse en situaciones médicas y farmacéuticas. Maneja los posesivos con precisión y expresa sus estados emocionales más íntimos utilizando verbos reflexivos como sentirse, acordarse y preocuparse. Mañana dará un paso histórico en su aprendizaje: comenzará a explorar el tiempo pasado para narrar sus vivencias. Con cuarenta y cinco días completados, Sakib sabe que su constancia ha vencido todas las dificultades.",
            "translation": "Day forty-five represents three quarters of the path toward the goal. Sakib looks back and feels a deep emotion. He fondly remembers his early doubts about articles and verb endings. Today he masters professional vocabulary of businesses and offices, understands the educational system, and knows how to manage in medical and pharmaceutical situations. He handles possessives with precision and expresses his most intimate emotional states using reflexive verbs like sentirse, acordarse, and preocuparse. Tomorrow he will take a historic step in his learning: he will begin exploring the past tense to narrate his experiences. With forty-five days completed, Sakib knows that his consistency has conquered all difficulties.",
            "questions": [
                {"question": "¿Qué proporción del desafío de sesenta días está cumplida en el día 45?", "options": ["Un cuarto", "La mitad", "Tres cuartas partes (75%)", "El examen final"], "answer": 2, "explanation": "Three quarters (75%) of the challenge ('tres cuartas partes')."},
                {"question": "¿Qué paso histórico dará Sakib a partir de mañana?", "options": ["Dejar de estudiar", "Comenzar a explorar el tiempo pasado (pretérito) para narrar vivencias", "Volver a empezar desde el día 1", "Aprender solo números"], "answer": 1, "explanation": "Begin exploring the past tense ('explorar el tiempo pasado')."},
                {"question": "¿Qué ha vencido todas las dificultades según el texto?", "options": ["La suerte", "Su constancia", "El dinero", "El tiempo frío"], "answer": 1, "explanation": "His consistency ('su constancia ha vencido...')."}
            ]
        },
        "exercises": [
            {
                "id": "d45-ex1",
                "type": "fill-in",
                "prompt": "Conjugate SENTIRSE (e -> ie) for 'yo': Hoy yo ______ (sentirse) muy contento.",
                "options": ["me siento", "me sento", "se siente", "te sientes"],
                "correct": 0,
                "explanation": "Yo form is 'me siento'."
            },
            {
                "id": "d45-ex2",
                "type": "fill-in",
                "prompt": "Complete with the mandatory preposition: Siempre me acuerdo ______ (of) mis amigos.",
                "options": ["de", "en", "por", "con"],
                "correct": 0,
                "explanation": "'Acordarse' strictly requires 'de': 'acordarse de'."
            },
            {
                "id": "d45-ex3",
                "type": "multiple-choice",
                "prompt": "What does 'No te preocupes por nada' mean?",
                "options": ["Don't study anything", "Don't worry about anything", "Don't speak to anyone", "Don't eat anything"],
                "correct": 1,
                "explanation": "'No te preocupes por nada' means 'Don't worry about anything'."
            },
            {
                "id": "d45-ex4",
                "type": "translation",
                "prompt": "Translate: 'We have a lot of fun in Spanish class.'",
                "options": ["Nos divertimos mucho en la clase de español.", "Nosotros divertimos mucho en la clase de español.", "Nos sentimos mucho en la clase de español.", "Nos quedamos mucho en la clase de español."],
                "correct": 0,
                "explanation": "'Nos divertimos mucho en la clase de español' conjugates divertirse for nosotros."
            }
        ],
        "speakingChallenge": [
            {"prompt": "Say how you feel today using 'Me siento + adjetivo'.", "hint": "Hoy me siento...", "sampleAnswer": "Hoy me siento muy motivado, feliz y orgulloso de mi progreso en español."},
            {"prompt": "Say something you remember fondly using 'Me acuerdo de...'", "hint": "Siempre me acuerdo de...", "sampleAnswer": "Siempre me acuerdo de mi primer viaje a España y de la comida deliciosa."},
            {"prompt": "Tell a friend not to worry about anything.", "hint": "Tranquilo, no te preocupes por...", "sampleAnswer": "Tranquilo, amigo mío, no te preocupes por el examen, vas a aprobar seguro."}
        ],
        "dailyRevision": {
            "quickQuestions": [
                "What preposition must follow 'acordarse' (to remember)? (DE)",
                "What preposition must follow 'preocuparse' (to worry)? (POR)"
            ],
            "grammarRecall": "Reflexive emotions: sentirse (e->ie), acordarse de (o->ue), preocuparse por, despedirse de (e->i), divertirse (e->ie).",
            "vocabRecall": ["Sentirse", "Acordarse de", "Preocuparse por", "Despedirse de", "Quedarse", "Divertirse", "Ponerse contento"]
        },
        "checklist": [
            "Conjugated emotional reflexive verbs (sentirse, acordarse, preocuparse)",
            "Applied mandatory prepositions: acordarse DE, preocuparse POR, despedirse DE",
            "Handled stem changes inside reflexive verbs (me siento, me acuerdo)",
            "Completed the Mid-Stage 5 reading review at the 75% mark",
            "Passed all 4 emotional reflexive exercises",
            "Expressed personal feelings and memories aloud in Spanish"
        ]
    }
]

print(f"Loaded {len(stage5_days)} initial days for Stage 5.")
