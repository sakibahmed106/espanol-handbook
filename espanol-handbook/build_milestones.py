"""
Milestones Builder for ESPAÑOL 60-Day Handbook
Generates data/milestones.js with 6 milestone assessments with 100% English titles and badges
"""
import json

milestones_data = [
    {
        "stage": 1,
        "day": 10,
        "title": "Milestone 1: Foundations of Spanish",
        "subtitle": "Celebrating the First 10 Days — Alphabet, Articles, Pronouns, Numbers & Ser vs Estar",
        "description": "Congratulations on completing Stage 1! You have mastered the foundational building blocks of Spanish: phonetics, 100 essential words, subject pronouns, gender agreement, and the critical distinction between Ser and Estar.",
        "badge": "🇪🇸🥉 Foundational Bronze",
        "keyMetrics": {
            "daysCompleted": 10,
            "vocabularyTarget": 100,
            "grammarPillars": ["Pronouns & Articles", "Gender & Number", "Ser vs Estar", "Basic Sentence Structure"],
            "conversationalAbility": "Greetings, introducing oneself, asking names, counting 0-30, and basic questions."
        },
        "selfAssessmentQuestions": [
            {"id": "m1-q1", "question": "Can you introduce yourself in Spanish stating your name, nationality, and profession?", "type": "yes-no"},
            {"id": "m1-q2", "question": "Do you clearly distinguish when to use 'ser' (identity/origin) and 'estar' (location/condition)?", "type": "yes-no"},
            {"id": "m1-q3", "question": "Can you comfortably count from 0 to 30 and say today's date in Spanish?", "type": "yes-no"},
            {"id": "m1-q4", "question": "Do you correctly apply gender agreement (el libro / la mesa) and plural formations?", "type": "yes-no"}
        ],
        "quiz": [
            {
                "id": "m1-test-1",
                "question": "Which is the correct sentence for 'I am from Spain and I am in Madrid'?",
                "options": [
                    "Soy de España y estoy en Madrid.",
                    "Estoy de España y soy en Madrid.",
                    "Soy de España y soy en Madrid.",
                    "Estoy de España y estoy en Madrid."
                ],
                "correct": 0,
                "explanation": "Permanent origin takes 'ser' (Soy de España) and geographic location takes 'estar' (estoy en Madrid)."
            },
            {
                "id": "m1-test-2",
                "question": "Which are the plural indefinite articles ('some')?",
                "options": ["Un, una", "Unos, unas", "Los, las", "El, la"],
                "correct": 1,
                "explanation": "'Unos' (masculine plural) and 'unas' (feminine plural) are the indefinite articles."
            },
            {
                "id": "m1-test-3",
                "question": "How do you spell the number 16 in Spanish?",
                "options": ["Diez y seis", "Dieciséis", "Dieziseis", "Seisdiez"],
                "correct": 1,
                "explanation": "Numbers 16 to 19 are written as a single word with an accent mark: 'dieciséis'."
            },
            {
                "id": "m1-test-4",
                "question": "Which pronoun corresponds to 'you all' (informal plural in Spain)?",
                "options": ["Ustedes", "Ellos", "Vosotros / Vosotras", "Nosotros"],
                "correct": 2,
                "explanation": "In Spain, 'vosotros / vosotras' is used for the informal plural."
            }
        ],
        "teacherFeedback": "Sakib, completing the first ten days demonstrates admirable discipline. Your phonetic and structural base is solid. You are now ready to step into Everyday Spanish in Stage 2!"
    },
    {
        "stage": 2,
        "day": 20,
        "title": "Milestone 2: Everyday Spanish",
        "subtitle": "Celebrating Day 20 — Family, Home, Food & Core Regular/Irregular Verbs",
        "description": "Stage 2 conquered! You have unlocked everyday living Spanish: family descriptions, ordering food, describing your home, and conjugating present regular verbs along with the heavyweights TENER, HACER, and IR.",
        "badge": "🥈 Communicative Silver",
        "keyMetrics": {
            "daysCompleted": 20,
            "vocabularyTarget": 200,
            "grammarPillars": ["Regular Verbs -AR/-ER/-IR", "Tener (Possession, Age, Idioms)", "Hacer & Weather", "Ir a + Infinitive (Near Future)"],
            "conversationalAbility": "Talking about family members, describing houses, expressing hunger/thirst/age, and formulating near future plans."
        },
        "selfAssessmentQuestions": [
            {"id": "m2-q1", "question": "Can you describe your family and their professions in 5 sentences in Spanish?", "type": "yes-no"},
            {"id": "m2-q2", "question": "Do you conjugate verbs like hablar, comer, and vivir correctly in the present tense?", "type": "yes-no"},
            {"id": "m2-q3", "question": "Do you use 'tener' for age (Tengo 24 años) instead of ser or estar?", "type": "yes-no"},
            {"id": "m2-q4", "question": "Do you know how to form the immediate near future with 'ir a + infinitive' (Voy a estudiar)?", "type": "yes-no"}
        ],
        "quiz": [
            {
                "id": "m2-test-1",
                "question": "How do you conjugate 'vivir' for 'nosotros'?",
                "options": ["Vivimos", "Vivéis", "Viven", "Vivo"],
                "correct": 0,
                "explanation": "-IR verbs take -imos in the 1st person plural: 'nosotros vivimos'."
            },
            {
                "id": "m2-test-2",
                "question": "How do you say 'I am going to cook dinner tonight'?",
                "options": [
                    "Voy a cocinar la cena esta noche.",
                    "Voy cocinando la cena esta noche.",
                    "Cocino a voy la cena esta noche.",
                    "Tengo a cocinar la cena esta noche."
                ],
                "correct": 0,
                "explanation": "Near future periphrasis formula: IR (present) + A + Infinitive ('Voy a cocinar')."
            },
            {
                "id": "m2-test-3",
                "question": "What is the correct form for 'He is 25 years old and he is hungry'?",
                "options": [
                    "Él tiene 25 años y tiene hambre.",
                    "Él es 25 años y está hambre.",
                    "Él está 25 años y tiene hambre.",
                    "Él tiene 25 años y es hambre."
                ],
                "correct": 0,
                "explanation": "Both age and physiological sensations require the verb 'tener'."
            },
            {
                "id": "m2-test-4",
                "question": "What is the weather according to: 'Hace sol y hace mucho calor'?",
                "options": ["It's raining", "It's sunny and very hot", "It's snowing", "It's foggy"],
                "correct": 1,
                "explanation": "In Spanish, atmospheric weather uses the verb 'hacer' ('hace sol, hace calor')."
            }
        ],
        "teacherFeedback": "Fantastic progress! You broke through the 200-word milestone and verbs are second nature. Your ability to speak about real daily life has doubled."
    },
    {
        "stage": 3,
        "day": 30,
        "title": "Milestone 3: The Halfway Mark",
        "subtitle": "Celebrating 30 Days — Reflexive Routines, Telling Time, Stem-Changers & Gustar",
        "description": "YOU ARE HALFWAY THROUGH THE CHALLENGE! 30 days of consistent Spanish. You now possess reflexives for daily routines, tell time flawlessly, understand stem-changing verbs (e->ie, o->ue, e->i), and wield the psychology of 'GUSTAR'.",
        "badge": "🥇 Midpoint Gold",
        "keyMetrics": {
            "daysCompleted": 30,
            "vocabularyTarget": 300,
            "grammarPillars": ["Reflexive Verbs (levantarse, ducharse)", "Time & Schedules", "Stem-Changers (querer, poder, pedir)", "Structure of Gustar"],
            "conversationalAbility": "Describing full daily schedules from dawn to dusk, shopping and prices, expressing passions and dislikes."
        },
        "selfAssessmentQuestions": [
            {"id": "m3-q1", "question": "Can you narrate your morning routine using at least 4 reflexive verbs?", "type": "yes-no"},
            {"id": "m3-q2", "question": "Can you tell time accurately (son las tres y media, es la una menos cuarto)?", "type": "yes-no"},
            {"id": "m3-q3", "question": "Do you master the e->ie (quiero) and o->ue (puedo, duermo) stem changes?", "type": "yes-no"},
            {"id": "m3-q4", "question": "Do you agree 'gustar' with the object: 'me gusta el café' vs 'me gustan los museos'?", "type": "yes-no"}
        ],
        "quiz": [
            {
                "id": "m3-test-1",
                "question": "What is the correct 'yo' form for 'despertarse' (e->ie)?",
                "options": ["Me despierto", "Yo desperto", "Me desperto", "Yo desierto"],
                "correct": 0,
                "explanation": "Requires reflexive pronoun 'me' and root diphthong: 'me despierto'."
            },
            {
                "id": "m3-test-2",
                "question": "How do you say 'Quarter to eight' in Spain?",
                "options": [
                    "Las ocho menos cuarto.",
                    "Las siete y cuarenta y cinco solamente.",
                    "Cuarto para las ocho.",
                    "Las ocho y cuarto."
                ],
                "correct": 0,
                "explanation": "In Spain the standard phrase is 'Las ocho menos cuarto'."
            },
            {
                "id": "m3-test-3",
                "question": "Which is the correct option for 'We like Spanish cities'?",
                "options": [
                    "Nos gustan las ciudades españolas.",
                    "Nos gusta las ciudades españolas.",
                    "A nosotros gustamos las ciudades.",
                    "Nosotros gustan las ciudades."
                ],
                "correct": 0,
                "explanation": "Because the grammatical subject 'las ciudades' is plural, the verb must be 'gustan'."
            },
            {
                "id": "m3-test-4",
                "question": "What is the conjugation of 'poder' (o->ue) for 'tú'?",
                "options": ["Puedes", "Podes", "Puedas", "Pude"],
                "correct": 0,
                "explanation": "The vowel mutation o->ue yields 'tú puedes'."
            }
        ],
        "teacherFeedback": "Thirty days of dedication! You crossed the equator of the challenge. You are constructing sentences with true autonomy."
    },
    {
        "stage": 4,
        "day": 40,
        "title": "Milestone 4: Practical Immersion & Urban Spanish",
        "subtitle": "Celebrating Day 40 — Restaurants, AVE Trains, Describing People & Por vs Para",
        "description": "Stage 4 mastered! You have stepped out into the streets of Spain: ordering Menú del Día in restaurants, navigating train stations, describing physical features and personalities, and solving the historic enigma of Por vs Para.",
        "badge": "🎖️ Urban Communicator",
        "keyMetrics": {
            "daysCompleted": 40,
            "vocabularyTarget": 400,
            "grammarPillars": ["Ser vs Tener vs Llevar in Descriptions", "Modals: Poder, Querer, Deber", "Obligation: Tener que vs Hay que", "Fundamental Contrast: Por vs Para"],
            "conversationalAbility": "Ordering multi-course meals with wine and dessert, buying rail tickets, describing people and towns with rich nuance."
        },
        "selfAssessmentQuestions": [
            {"id": "m4-q1", "question": "Can you order a full Spanish Menú del Día (primer plato, segundo, postre y cuenta)?", "type": "yes-no"},
            {"id": "m4-q2", "question": "Do you know how to describe someone combining 'es alto', 'tiene ojos marrones', and 'lleva gafas'?", "type": "yes-no"},
            {"id": "m4-q3", "question": "Do you distinguish when to use 'por' (cause/price/medium) and 'para' (destination/purpose)?", "type": "yes-no"},
            {"id": "m4-q4", "question": "Can you express personal obligation (tengo que estudiar) and general obligation (hay que reciclar)?", "type": "yes-no"}
        ],
        "quiz": [
            {
                "id": "m4-test-1",
                "question": "In a Spanish restaurant, what do you ask for at the end to pay?",
                "options": ["La cuenta, por favor.", "El billete, por favor.", "La carta, por favor.", "El recibo, por favor."],
                "correct": 0,
                "explanation": "'La cuenta, por favor' is the polite, universal phrase in Spain."
            },
            {
                "id": "m4-test-2",
                "question": "Complete: 'Este tren sale _____ Sevilla y el billete es _____ mi madre.'",
                "options": ["para / para", "por / por", "para / por", "por / para"],
                "correct": 0,
                "explanation": "Both indicate destination or recipient: 'para Sevilla' (destination) and 'para mi madre' (recipient)."
            },
            {
                "id": "m4-test-3",
                "question": "Which verb describes wearing clothes and accessories today?",
                "options": ["Llevar (lleva una chaqueta)", "Ser (es una chaqueta)", "Tener (tiene una chaqueta puesta)", "Estar (está una chaqueta)"],
                "correct": 0,
                "explanation": "For clothes and accessories, Spanish uses the verb 'llevar'."
            },
            {
                "id": "m4-test-4",
                "question": "What is the difference between 'Tengo que estudiar' and 'Hay que estudiar'?",
                "options": [
                    "'Tengo que' is personal (I have to); 'Hay que' is a general rule (one must).",
                    "They are identical in meaning and usage.",
                    "'Hay que' is only used for food.",
                    "'Tengo que' is past and 'Hay que' is future."
                ],
                "correct": 0,
                "explanation": "'Tener que + inf' is personal obligation; 'Hay que + inf' is general impersonal obligation."
            }
        ],
        "teacherFeedback": "Sakib, you could now travel alone through Madrid or Seville without relying on a digital translator. Your real-world conversational skills are impressive!"
    },
    {
        "stage": 5,
        "day": 50,
        "title": "Milestone 5: The Gate to the Past Tense",
        "subtitle": "Celebrating Day 50 — Professions, Health & The Preterite Past",
        "description": "Stage 5 achieved! You have crossed the greatest milestone in Spanish grammar: THE PAST TENSE! You can now recount yesterday's events, talk about your travels, express health issues with 'doler', and write cohesive paragraphs.",
        "badge": "⭐ Past Tense Master",
        "keyMetrics": {
            "daysCompleted": 50,
            "vocabularyTarget": 500,
            "grammarPillars": ["Preterite Past Regular (-AR, -ER, -IR)", "Key Irregular Preterites (Fui, Estuve, Tuve)", "The Verb Doler & Physical Symptoms", "Building Cohesive Paragraphs"],
            "conversationalAbility": "Recounting weekend trips, talking about past professional experiences, explaining ailments at the pharmacy."
        },
        "selfAssessmentQuestions": [
            {"id": "m5-q1", "question": "Can you conjugate 'hablé, hablaste, habló, hablamos, hablasteis, hablaron' from memory?", "type": "yes-no"},
            {"id": "m5-q2", "question": "Do you know that 'yo fui' serves as the preterite for BOTH the verb SER and the verb IR?", "type": "yes-no"},
            {"id": "m5-q3", "question": "Can you explain a health symptom using 'me duele la garganta' or 'tengo fiebre'?", "type": "yes-no"},
            {"id": "m5-q4", "question": "Can you write a 60-word paragraph narrating what you did last weekend?", "type": "yes-no"}
        ],
        "quiz": [
            {
                "id": "m5-test-1",
                "question": "What is the preterite form for 'Yesterday I (comer) paella and my friend (beber) wine'?",
                "options": [
                    "Ayer yo comí paella y mi amigo bebió vino.",
                    "Ayer yo comió paella y mi amigo comí vino.",
                    "Ayer yo comaba paella y mi amigo bebaba vino.",
                    "Ayer yo como paella y mi amigo bebe vino."
                ],
                "correct": 0,
                "explanation": "In -ER: 1st person 'comí' and 3rd person 'bebió' (with mandatory accent marks)."
            },
            {
                "id": "m5-test-2",
                "question": "In the sentence 'Ayer fui a Granada y la Alhambra fue maravillosa', what do the two 'fui/fue' mean?",
                "options": [
                    "The first is IR (went); the second is SER (was).",
                    "Both are the verb IR.",
                    "Both are the verb SER.",
                    "The first is SER; the second is ESTAR."
                ],
                "correct": 0,
                "explanation": "SER and IR share identical forms in the preterite; destination 'a Granada' indicates IR (went)."
            },
            {
                "id": "m5-test-3",
                "question": "How do you say 'My legs hurt' in Spanish?",
                "options": ["Me duelen las piernas.", "Me duele las piernas.", "Tengo dolor las piernas.", "Mis piernas duelen."],
                "correct": 0,
                "explanation": "'Doler' functions like 'gustar': plural subject 'las piernas' requires 'duelen'."
            },
            {
                "id": "m5-test-4",
                "question": "What is the 1st person preterite of 'estar'?",
                "options": ["Yo estuve", "Yo estube", "Yo estaba", "Yo fui estado"],
                "correct": 0,
                "explanation": "The preterite of estar has an irregular stem: 'yo estuve, tú estuviste, él estuvo'."
            }
        ],
        "teacherFeedback": "Fifty days completed! The preterite past tense is the golden key that transforms a static present-tense student into an authentic storyteller. Only ten days left to glory!"
    },
    {
        "stage": 6,
        "day": 60,
        "title": "Milestone 6: A1 Consolidation & Capstone",
        "subtitle": "Celebrating 60 Days — Full Mastery of CEFR A1 Level & Official Exam Readiness",
        "description": "VICTORY! You have completed the entire 60-Day Spanish Learning Challenge. From 0 words to 600 words, from silence to fluent conversational sentences, all 8 grammatical pillars, reading, writing, and cultural immersion.",
        "badge": "🏆 Grand A1 Golden Crown",
        "keyMetrics": {
            "daysCompleted": 60,
            "vocabularyTarget": 600,
            "grammarPillars": ["The 8 Grammatical Pillars of CEFR A1", "Idioms & Colloquial Modismos", "Opinion, Agreement & Debate", "Past-Present-Future Integration"],
            "conversationalAbility": "Autonomous A1 communication in social, emergency, travel, professional, and everyday cultural contexts across Spain."
        },
        "selfAssessmentQuestions": [
            {"id": "m6-q1", "question": "Do you feel capable of holding a 10-minute conversation with a native speaker in Madrid?", "type": "yes-no"},
            {"id": "m6-q2", "question": "Can you read a 3-page authentic Spanish cultural text and answer comprehension questions?", "type": "yes-no"},
            {"id": "m6-q3", "question": "Do you comfortably wield the 600 essential vocabulary words in the index?", "type": "yes-no"},
            {"id": "m6-q4", "question": "Are you ready to take the Final A1 Examination and claim your official certificate?", "type": "yes-no"}
        ],
        "quiz": [
            {
                "id": "m6-test-1",
                "question": "What does the Spanish idiom 'ser pan comido' mean?",
                "options": ["To be extremely easy (a piece of cake)", "To be very hungry", "To buy expensive bread", "To be a glutton"],
                "correct": 0,
                "explanation": "'Ser pan comido' is the Castilian idiom for something super easy (a piece of cake)."
            },
            {
                "id": "m6-test-2",
                "question": "How do people politely answer the phone in Spain?",
                "options": ["¿Dígame?", "¿Quién habla?", "¡Hola tú!", "¿Qué quieres?"],
                "correct": 0,
                "explanation": "'¿Dígame?' or '¿Sí, dígame?' is standard Spain telephone etiquette."
            },
            {
                "id": "m6-test-3",
                "question": "What is the false friend meaning of 'embarazada'?",
                "options": [
                    "It means 'pregnant', never 'embarrassed' (embarrassed is 'avergonzado').",
                    "It means 'tired'.",
                    "It means 'stomach ache'.",
                    "It means 'angry'."
                ],
                "correct": 0,
                "explanation": "'Embarazada' = pregnant; 'avergonzado/a' = embarrassed."
            },
            {
                "id": "m6-test-4",
                "question": "Which statement accurately describes your level upon completing this 60-day handbook?",
                "options": [
                    "I possess a solid CEFR A1 foundation to communicate with autonomy in daily situations.",
                    "I speak without knowing any grammar rules.",
                    "I only know 50 isolated words.",
                    "I cannot understand anything without Google Translate."
                ],
                "correct": 0,
                "explanation": "Upon completing all 60 days, you have consolidated CEFR A1 mastery with 600 words and 8 grammatical pillars."
            }
        ],
        "teacherFeedback": "Sakib, your name is engraved with gold letters in this handbook. You proved that with daily dedication, passion, and a structured system, language barriers vanish. Get ready to take your Final Exam and claim your Official Certificate!"
    }
]

with open("d:/ag/espanol-handbook/data/milestones.js", "w", encoding="utf-8") as f:
    f.write("// Milestones: 6 Stage Assessments & Progress Checkpoints\n")
    f.write("window.HANDBOOK_MILESTONES = ")
    json.dump(milestones_data, f, ensure_ascii=False, indent=2)
    f.write(";\n")

print(f"Generated data/milestones.js with {len(milestones_data)} milestones with 100% English titles.")
