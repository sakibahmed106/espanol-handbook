"""
Build Stage 3: Days 26 to 30 + Combine Stage 3 into data/lessons/stage3.js
"""
import json
from build_stage3_part1 import stage3_days

stage3_part2 = [
    {
        "day": 26,
        "stage": 3,
        "title": "Stem-Changing Verbs: O -> UE & E -> I",
        "subtitle": "Conjugating Poder, Dormir, Volver, Pedir, Servir",
        "goals": [
            "Master the O -> UE stem change (poder, dormir, volver, encontrar)",
            "Master the E -> I stem change (pedir, servir, repetir)",
            "Use modal verb PODER (can / to be able to) + infinitive for polite requests",
            "Remember that Nosotros and Vosotros remain regular outside the boot"
        ],
        "bengaliNote": "Just like E became IE yesterday, here the vowel 'O' splits into 'UE' (*dormir* -> *duermo* = আমি ঘুমাই). And for E -> I, the vowel shifts directly (*pedir* -> *pido* = আমি চাই/অর্ডার করি). The modal verb *poder* (*¿puedo...?* = 'আমি কি পারি...?') is the most useful politeness key in all of Spain!",
        "vocabulary": [
            {"word": "Poder (o -> ue)", "translation": "To be able to / Can", "pos": "verb", "gender": None, "example": "¿Puedo hacer una pregunta?", "exampleTranslation": "Can I ask a question?"},
            {"word": "Dormir (o -> ue)", "translation": "To sleep", "pos": "verb", "gender": None, "example": "Duermo ocho horas cada noche.", "exampleTranslation": "I sleep eight hours every night."},
            {"word": "Volver (o -> ue)", "translation": "To return / To come back", "pos": "verb", "gender": None, "example": "Vuelvo a casa a las seis.", "exampleTranslation": "I return home at six."},
            {"word": "Encontrar (o -> ue)", "translation": "To find / To meet", "pos": "verb", "gender": None, "example": "No encuentro mis llaves.", "exampleTranslation": "I cannot find my keys."},
            {"word": "Pedir (e -> i)", "translation": "To ask for / To order (food/drink)", "pos": "verb", "gender": None, "example": "Pido una paella de verduras.", "exampleTranslation": "I order a vegetable paella."},
            {"word": "Servir (e -> i)", "translation": "To serve / To be useful (no sirve = it doesn't work)", "pos": "verb", "gender": None, "example": "El camarero sirve la comida.", "exampleTranslation": "The waiter serves the food."},
            {"word": "Repetir (e -> i)", "translation": "To repeat", "pos": "verb", "gender": None, "example": "¿Puede repetir, por favor?", "exampleTranslation": "Can you repeat, please?"},
            {"word": "Recordar (o -> ue)", "translation": "To remember", "pos": "verb", "gender": None, "example": "No recuerdo su nombre.", "exampleTranslation": "I don't remember his name."},
            {"word": "Costar (o -> ue)", "translation": "To cost", "pos": "verb", "gender": None, "example": "¿Cuánto cuesta?", "exampleTranslation": "How much does it cost?"},
            {"word": "¿Se puede?", "translation": "May I? / Is it permitted?", "pos": "phrase", "gender": None, "example": "¿Se puede pasar?", "exampleTranslation": "May I come in?"}
        ],
        "sentences": [
            {"spanish": "¿Puedes hablar más despacio, por favor?", "english": "Can you speak more slowly, please?"},
            {"spanish": "No puedo ir hoy porque tengo mucho que estudiar.", "english": "I cannot go today because I have a lot to study."},
            {"spanish": "Los fines de semana duermo hasta tarde.", "english": "On weekends I sleep until late."},
            {"spanish": "Siempre pedimos la cuenta después de comer.", "english": "We always ask for the bill after eating. (Nosotros: pedimos!)"},
            {"spanish": "¿A qué hora vuelven ustedes a Madrid?", "english": "At what time do you all return to Madrid?"},
            {"spanish": "¿Me puede servir un vaso de agua?", "english": "Can you serve me a glass of water? (formal)"}
        ],
        "grammar": {
            "title": "The Master O -> UE & E -> I Boot Verb Charts",
            "explanation": "Stem changes occur in the same 4 boot persons: yo, tú, él/ella/usted, and ellos/ellas/ustedes. Nosotros and vosotros stay regular!",
            "rules": [
                "O -> UE Pattern: PODER: puedo, puedes, puede, **podemos**, **podéis**, pueden. DORMIR: duermo, duermes, duerme, **dormimos**, **dormís**, duermen.",
                "E -> I Pattern: PEDIR: pido, pides, pide, **pedimos**, **pedís**, piden. SERVIR: sirvo, sirves, sirve, **servimos**, **servís**, sirven.",
                "Modal PODER + Infinitive: To make polite requests or express ability, conjugate PODER and leave the main action verb in the infinitive: *¿Puedo pasar?* (Can I come in?), *¿Puedes ayudarme?* (Can you help me?).",
                "Nosotros & Vosotros Exception: Remember, they NEVER change stems: *podemos*, *dormimos*, *pedimos*."
            ],
            "structures": [
                "PODER: puedo | puedes | puede | podemos | podéis | pueden",
                "PEDIR: pido | pides | pide | pedimos | pedís | piden",
                "Polite Request: ¿Puedo + [Infinitivo]? / ¿Puedes + [Infinitivo]?"
            ],
            "examples": [
                {"spanish": "¿Puedes repetir la frase?", "english": "Can you repeat the phrase?"},
                {"spanish": "El bebé duerme tranquilamente.", "english": "The baby sleeps peacefully."},
                {"spanish": "Nosotros podemos ayudar.", "english": "We can help. (No stem change!)"},
                {"spanish": "Pido un café solo.", "english": "I order a black coffee."}
            ],
            "commonMistakes": [
                {"wrong": "Nosotros puedemos", "right": "Nosotros podemos", "explanation": "Nosotros never changes stem in present tense."},
                {"wrong": "Puedo hablar con tú", "right": "Puedo hablar contigo", "explanation": "'With you' is the special word 'contigo'."}
            ],
            "proTip": "The single most useful phrase when you don't catch something a Spaniard says: **«¿Puedes repetir más despacio, por favor?»** (Can you repeat more slowly, please?). Memorize it like a reflex!"
        },
        "conversation": {
            "title": "Ordering at a Restaurant with PODER and PEDIR",
            "context": "Sakib and his friend Javier order dinner at a traditional tavern.",
            "dialogue": [
                {"speaker": "Camarero", "role": "Waiter", "spanish": "Buenas noches. ¿Tienen reserva?", "english": "Good evening. Do you have a reservation?"},
                {"speaker": "Javier", "role": "Friend", "spanish": "No, no tenemos reserva. ¿Podemos sentarnos en esa mesa junto a la ventana?", "english": "No, we don't have a reservation. Can we sit at that table next to the window?"},
                {"speaker": "Camarero", "role": "Waiter", "spanish": "Sí, por supuesto, está libre. ¿Qué van a pedir para beber?", "english": "Yes, of course, it's free. What are you going to order to drink?"},
                {"speaker": "Sakib", "role": "Student", "spanish": "Para mí, ¿puede servirme un agua mineral con gas, por favor?", "english": "For me, can you serve me a sparkling mineral water, please?"},
                {"speaker": "Camarero", "role": "Waiter", "spanish": "Claro que sí. Y de comer, ¿saben ya lo que quieren?", "english": "Of course. And to eat, do you already know what you want?"},
                {"speaker": "Javier", "role": "Friend", "spanish": "Pedimos una ración de tortilla y otra de calamares para compartir.", "english": "We order a portion of omelette and another of squid to share."},
                {"speaker": "Camarero", "role": "Waiter", "spanish": "¡Marchando! Enseguida se lo traigo.", "english": "Coming right up! Right away I bring it to you."}
            ],
            "keyPhrases": [
                {"phrase": "Para compartir", "explanation": "'To share' (essential Spanish dining habit with tapas)."},
                {"phrase": "¡Marchando!", "explanation": "Spain waiter slang: 'Coming right up!'"},
                {"phrase": "¿Puede servirme...?", "explanation": "'Can you serve me...?' (polite request)."}
            ]
        },
        "reading": {
            "title": "El descanso y el sueño en España",
            "passage": "El descanso adecuado es fundamental para la salud mental y física. En España existe la famosa leyenda de la siesta. Aunque muchos extranjeros piensan que todos los españoles duermen la siesta todos los días, la realidad moderna es diferente: debido a los horarios de trabajo en las grandes oficinas, solo un dieciséis por ciento de los adultos puede dormir una siesta corta entre semana. Sin embargo, los fines de semana, muchas familias disfrutan de un pequeño descanso después del almuerzo de quince a veinte minutos. Los médicos confirman que esta pequeña pausa renueva la energía para el resto del día.",
            "translation": "Proper rest is fundamental for mental and physical health. In Spain exists the famous legend of the siesta. Although many foreigners think that all Spaniards sleep the siesta every day, modern reality is different: due to work schedules in big offices, only sixteen percent of adults can sleep a short siesta on weekdays. However, on weekends, many families enjoy a small rest after lunch of fifteen to twenty minutes. Doctors confirm that this short pause renews energy for the rest of the day.",
            "questions": [
                {"question": "¿Qué porcentaje de adultos duerme la siesta entre semana?", "options": ["El cien por cien", "El cincuenta por ciento", "Solo un dieciséis por ciento", "Nadie"], "answer": 2, "explanation": "Only 16 percent ('solo un dieciséis por ciento')."},
                {"question": "¿Cuándo disfruta más gente de la siesta?", "options": ["Los lunes por la mañana", "Los fines de semana después del almuerzo", "A medianoche", "En el metro"], "answer": 1, "explanation": "On weekends after lunch ('los fines de semana...')."},
                {"question": "¿Cuánto tiempo recomiendan los médicos para una siesta?", "options": ["Tres horas", "De quince a veinte minutos", "Toda la tarde", "Diez segundos"], "answer": 1, "explanation": "15 to 20 minutes ('de quince a veinte minutos')."}
            ]
        },
        "exercises": [
            {
                "id": "d26-ex1",
                "type": "fill-in",
                "prompt": "Conjugate PODER for 'tú': ¿______ (poder) hablar más despacio?",
                "options": ["Puedes", "Puedo", "Puede", "Podemos"],
                "correct": 0,
                "explanation": "Tú form changes O -> UE: 'Puedes'."
            },
            {
                "id": "d26-ex2",
                "type": "fill-in",
                "prompt": "Conjugate DORMIR for 'yo': Yo ______ (dormir) ocho horas.",
                "options": ["duermo", "dormo", "duermes", "dormimos"],
                "correct": 0,
                "explanation": "Yo form changes O -> UE: 'duermo'."
            },
            {
                "id": "d26-ex3",
                "type": "fill-in",
                "prompt": "Conjugate PEDIR for 'él': Carlos ______ (pedir) una paella.",
                "options": ["pide", "pede", "pido", "pedimos"],
                "correct": 0,
                "explanation": "Él form changes E -> I: 'pide'."
            },
            {
                "id": "d26-ex4",
                "type": "translation",
                "prompt": "Translate: 'Can I ask a question?'",
                "options": ["¿Puedo hacer una pregunta?", "¿Tengo hacer una pregunta?", "¿Quiero una pregunta?", "¿Dónde hacer una pregunta?"],
                "correct": 0,
                "explanation": "'¿Puedo hacer una pregunta?' is the proper polite inquiry."
            }
        ],
        "speakingChallenge": [
            {"prompt": "Ask someone politely to speak slower.", "hint": "¿Puedes hablar más...", "sampleAnswer": "¿Puedes hablar más despacio, por favor? Aún estoy aprendiendo."},
            {"prompt": "Say how many hours you sleep each night.", "hint": "Normalmente duermo...", "sampleAnswer": "Normalmente duermo siete u ocho horas cada noche."},
            {"prompt": "Order a bottle of water in a restaurant using 'Pido' or '¿Me puede servir?'.", "hint": "¿Me puede servir una botella de...", "sampleAnswer": "Por favor, ¿me puede servir una botella de agua sin gas?"}
        ],
        "dailyRevision": {
            "quickQuestions": [
                "What vowel changes happen in 'poder' and 'pedir'?",
                "Why don't 'nosotros' change stems in 'podemos' or 'pedimos'?"
            ],
            "grammarRecall": "O -> UE (poder, dormir, volver). E -> I (pedir, servir). Nosotros/Vosotros remain regular.",
            "vocabRecall": ["Poder", "Puedo", "Dormir", "Volver", "Pedir", "Servir", "Repetir", "¿Se puede?"]
        },
        "checklist": [
            "Conjugated O -> UE verbs (poder, dormir, volver)",
            "Conjugated E -> I verbs (pedir, servir)",
            "Used PODER + infinitive for polite requests",
            "Maintained regular stems for nosotros and vosotros",
            "Completed all 4 stem-changing exercises",
            "Practiced making polite requests out loud"
        ]
    },
    {
        "day": 27,
        "stage": 3,
        "title": "Question Formation & Word Order Mastery",
        "subtitle": "Mastering inversion, pitch intonation, and tag questions",
        "goals": [
            "Master the 3 distinct ways to ask questions in Spanish",
            "Use intonation questions (statement with rising pitch: ¿Tú vives aquí?)",
            "Use inverted word order questions (Verb + Subject: ¿Vives tú aquí?)",
            "Use tag questions (¿verdad?, ¿no?) to confirm information"
        ],
        "bengaliNote": "Spanish question formation is wonderfully flexible! In English, you are forced to add auxiliary verbs ('Do you speak? Does he work?'). In Spanish and Bangla, you can simply change your vocal pitch or flip the verb and subject (যেমন: 'তুমি কি চা খাবে?' or 'চা খাবে তুমি?').",
        "vocabulary": [
            {"word": "Preguntar / La pregunta", "translation": "To ask / The question", "pos": "verb / noun", "gender": "feminine", "example": "Quiero hacer una pregunta.", "exampleTranslation": "I want to ask a question."},
            {"word": "Dudar / La duda", "translation": "To doubt / The doubt (question/hesitation)", "pos": "verb / noun", "gender": "feminine", "example": "¿Tienes alguna duda?", "exampleTranslation": "Do you have any question/doubt?"},
            {"word": "¿Es verdad? / ¿Verdad?", "translation": "Is it true? / Right? (tag question)", "pos": "phrase", "gender": None, "example": "Eres de Bangladés, ¿verdad?", "exampleTranslation": "You are from Bangladesh, right?"},
            {"word": "¿No es así?", "translation": "Isn't it so?", "pos": "phrase", "gender": None, "example": "Madrid es muy bonita, ¿no es así?", "exampleTranslation": "Madrid is very beautiful, isn't it so?"},
            {"word": "Acaso", "translation": "Perhaps / By chance (rhetorical question marker)", "pos": "adverb", "gender": None, "example": "¿Acaso no lo sabes?", "exampleTranslation": "Don't you know it by chance?"},
            {"word": "Saber", "translation": "To know (facts, information, languages)", "pos": "verb", "gender": None, "example": "¿Sabes dónde está el banco?", "exampleTranslation": "Do you know where the bank is?"},
            {"word": "Conocer", "translation": "To know / To be acquainted with (people, cities)", "pos": "verb", "gender": None, "example": "¿Conoces Barcelona?", "exampleTranslation": "Do you know (have you been to) Barcelona?"},
            {"word": "Claro / Claro que sí", "translation": "Clear / Of course, clearly yes", "pos": "adverb / phrase", "gender": None, "example": "—¿Vienes? —¡Claro que sí!", "exampleTranslation": "—Are you coming? —Of course yes!"},
            {"word": "Depende", "translation": "It depends", "pos": "verb / phrase", "gender": None, "example": "Depende del tiempo que haga.", "exampleTranslation": "It depends on what the weather is like."},
            {"word": "Seguro(a)", "translation": "Sure / Certain", "pos": "adjective", "gender": "variable", "example": "¿Estás seguro?", "exampleTranslation": "Are you sure?"}
        ],
        "sentences": [
            {"spanish": "¿Hablas español con tus compañeros de clase?", "english": "Do you speak Spanish with your classmates?"},
            {"spanish": "¿Trabaja tu hermano en un hospital?", "english": "Does your brother work in a hospital? (Inverted order: Verb + Subject)"},
            {"spanish": "Tú vives cerca del Retiro, ¿verdad?", "english": "You live near the Retiro, right? (Tag question)"},
            {"spanish": "¿Sabes a qué hora cierra la biblioteca?", "english": "Do you know what time the library closes?"},
            {"spanish": "¿Conoces algún buen restaurante por aquí?", "english": "Do you know any good restaurant around here?"},
            {"spanish": "¿Estás seguro de la respuesta?", "english": "Are you sure about the answer?"}
        ],
        "grammar": {
            "title": "The Three Methods of Question Formation & SABER vs. CONOCER",
            "explanation": "Spanish questions do NOT require auxiliary verbs like English 'do / does / did'. You can form questions in three natural ways:",
            "rules": [
                "Method 1: Intonation (Pitch rise). The sentence structure is identical to a statement; only your voice rises at the end: *Tú hablas español.* (You speak Spanish) -> *¿Tú hablas español?* (Do you speak Spanish?).",
                "Method 2: Inversion (Verb before Subject). Place the verb first and the subject after: *¿Trabaja Carlos aquí?* (Does Carlos work here?), *¿Comprendes tú la lección?*.",
                "Method 3: Confirmation Tags. Add *¿verdad?* or *¿no?* to the end of any affirmative statement: *Vives en Madrid, ¿verdad?*",
                "SABER vs. CONOCER: 1) **Saber** = knowing facts, data, or how to do something (*Sé hablar bengalí*, *¿Sabes la hora?*). 2) **Conocer** = knowing people, places, or being familiar with art/cities (*Conozco a Carlos*, *¿Conoces Madrid?*)."
            ],
            "structures": [
                "Intonation: ¿ [Sujeto] + [Verbo] + [Complemento] ?",
                "Inversion: ¿ [Verbo] + [Sujeto] + [Complemento] ?",
                "Tag Question: [Oración afirmativa], ¿verdad? / ¿no?",
                "Saber: sé, sabes, sabe, sabemos, sabéis, saben",
                "Conocer: conozco, conoces, conoce, conocemos, conocéis, conocen"
            ],
            "examples": [
                {"spanish": "¿Vive María en Barcelona? (Inversion)", "english": "Does Maria live in Barcelona?"},
                {"spanish": "¿Tú sabes cocinar comida española? (Saber)", "english": "Do you know how to cook Spanish food?"},
                {"spanish": "¿Conoces al profesor Gómez? (Conocer + 'a' personal)", "english": "Do you know Professor Gomez?"},
                {"spanish": "Mañana no hay clase, ¿no?", "english": "Tomorrow there is no class, right?"}
            ],
            "commonMistakes": [
                {"wrong": "¿Haces tú hablar español? (literal translation of 'do you speak')", "right": "¿Hablas español?", "explanation": "Spanish never uses 'hacer' as a dummy question auxiliary like English 'do'."},
                {"wrong": "Conozco la hora", "right": "Sé la hora", "explanation": "Facts and information take 'saber', not 'conocer'."}
            ],
            "proTip": "The Personal 'A': When the direct object of a verb is a specific person, Spanish inserts the preposition **'a'**! *Conozco A Carlos* (I know Carlos), *Veo A María* (I see Maria). Bengali learners love this because Bangla also marks definite personal objects (যেমন: 'আমি কার্লোস**কে** চিনি')!"
        },
        "conversation": {
            "title": "Getting to Know Classmates",
            "context": "Sakib and his new classmate Marta ask each other questions during a class mixer.",
            "dialogue": [
                {"speaker": "Marta", "role": "Classmate", "spanish": "Sakib, ¿conoces bien Madrid o todavía no?", "english": "Sakib, do you know Madrid well or not yet?"},
                {"speaker": "Sakib", "role": "Student", "spanish": "Conozco el centro y algunos barrios, pero todavía no conozco todo. ¿Y tú, eres de aquí?", "english": "I know the center and some neighborhoods, but not everything yet. And you, are you from here?"},
                {"speaker": "Marta", "role": "Classmate", "spanish": "Sí, soy madrileña de toda la vida. ¿Sabes cocinar platos de tu país?", "english": "Yes, I am a local from Madrid all my life. Do you know how to cook dishes from your country?"},
                {"speaker": "Sakib", "role": "Student", "spanish": "¡Claro que sí! Sé cocinar curry bengalí, arroz biryani y verduras especiadas.", "english": "Of course yes! I know how to cook Bengali curry, biryani rice, and spiced vegetables."},
                {"speaker": "Marta", "role": "Classmate", "spanish": "¡Qué delicia! Tú vives en Chamberí, ¿verdad?", "english": "What a delight! You live in Chamberí, right?"},
                {"speaker": "Sakib", "role": "Student", "spanish": "Sí, vivo allí. ¿Por qué no vienes un día a cenar con otros compañeros?", "english": "Yes, I live there. Why don't you come one day to dinner with other classmates?"},
                {"speaker": "Marta", "role": "Classmate", "spanish": "¡Me encantaría! Muchas gracias por la invitación.", "english": "I would love to! Thank you very much for the invitation."}
            ],
            "keyPhrases": [
                {"phrase": "De toda la vida", "explanation": "'All my/one's life' (native local)."},
                {"phrase": "Todavía no", "explanation": "'Not yet'."},
                {"phrase": "¡Me encantaría!", "explanation": "'I would love to!'" }
            ]
        },
        "reading": {
            "title": "La curiosidad de aprender un idioma",
            "passage": "Hacer preguntas es la herramienta más poderosa para aprender una lengua extranjera. Cuando un estudiante no tiene miedo de preguntar, su aprendizaje se acelera enormemente. En la clase de español, los estudiantes hacen preguntas constantes: «¿Qué significa esta palabra?», «¿Cómo se pronuncia?», «¿Es verdad que en España la gente cena muy tarde?». Los profesores responden con paciencia y entusiasmo. Sakib sabe que cada pregunta abre una nueva ventana hacia la cultura española. Ahora formula preguntas con entonación perfecta y utiliza etiquetas de confirmación como un nativo.",
            "translation": "Asking questions is the most powerful tool for learning a foreign language. When a student is not afraid of asking, their learning accelerates enormously. In Spanish class, students ask constant questions: 'What does this word mean?', 'How is it pronounced?', 'Is it true that in Spain people have dinner very late?'. The teachers answer with patience and enthusiasm. Sakib knows that every question opens a new window onto Spanish culture. Now he formulates questions with perfect intonation and uses confirmation tags like a native.",
            "questions": [
                {"question": "¿Cuál es la herramienta más poderosa para aprender un idioma?", "options": ["Dormir mucho", "Hacer preguntas sin miedo", "No hablar nunca", "Comprar ropa cara"], "answer": 1, "explanation": "Asking questions without fear ('hacer preguntas...')."},
                {"question": "¿Qué preguntan los estudiantes sobre la cena en España?", "options": ["Si cenan a las cuatro", "Si es verdad que cenan muy tarde", "Si no cenan nunca", "Si cenan fruta solo"], "answer": 1, "explanation": "If it is true that they have dinner very late."},
                {"question": "¿Cómo formula las preguntas Sakib ahora?", "options": ["Con miedo", "Con entonación perfecta y etiquetas de confirmación", "Solo en inglés", "Por escrito únicamente"], "answer": 1, "explanation": "With perfect intonation and confirmation tags."}
            ]
        },
        "exercises": [
            {
                "id": "d27-ex1",
                "type": "multiple-choice",
                "prompt": "Does Spanish require auxiliary verbs like 'do' or 'does' to form questions?",
                "options": ["Yes, always", "Never", "Only on weekends", "Only in written essays"],
                "correct": 1,
                "explanation": "Spanish never uses dummy auxiliary verbs like 'do/does'."
            },
            {
                "id": "d27-ex2",
                "type": "fill-in",
                "prompt": "Choose Saber or Conocer: Yo no ______ (know) a esa persona.",
                "options": ["conozco", "sé", "sabe", "conoce"],
                "correct": 0,
                "explanation": "Knowing a person takes 'conocer' + personal 'a': 'conozco a esa persona'."
            },
            {
                "id": "d27-ex3",
                "type": "fill-in",
                "prompt": "Complete the tag question: Tú eres estudiante, ¿______?",
                "options": ["verdad", "cierto no", "es verdad no", "seguro"],
                "correct": 0,
                "explanation": "'¿verdad?' is the standard tag question meaning 'right?'."
            },
            {
                "id": "d27-ex4",
                "type": "translation",
                "prompt": "Translate: 'Do you know what time it is?'",
                "options": ["¿Sabes qué hora es?", "¿Conoces qué hora es?", "¿Haces saber la hora?", "¿Tienes hora verdad?"],
                "correct": 0,
                "explanation": "Facts and information take 'saber': '¿Sabes qué hora es?'."
            }
        ],
        "speakingChallenge": [
            {"prompt": "Form an inverted question: ask if Carlos lives in Madrid.", "hint": "¿Vive Carlos en...", "sampleAnswer": "¿Vive Carlos en el centro de Madrid?"},
            {"prompt": "Use a tag question: confirm that someone speaks English.", "hint": "Tú hablas inglés, ¿verdad?", "sampleAnswer": "Tú hablas inglés perfectamente, ¿verdad?"},
            {"prompt": "Say that you know Madrid and know how to speak Bengali.", "hint": "Conozco Madrid y sé hablar...", "sampleAnswer": "Conozco Madrid muy bien y sé hablar bengalí, inglés y español."}
        ],
        "dailyRevision": {
            "quickQuestions": [
                "What are the 3 ways to ask a question in Spanish?",
                "What is the difference between 'saber' and 'conocer'?"
            ],
            "grammarRecall": "Questions: Intonation (¿Tú hablas?), Inversion (¿Hablas tú?), Tags (¿verdad?, ¿no?). Saber = facts/skills; Conocer = people/places.",
            "vocabRecall": ["La pregunta", "La duda", "¿Verdad?", "¿No es así?", "Saber", "Conocer", "Claro que sí", "Seguro"]
        },
        "checklist": [
            "Formed questions via pitch intonation without auxiliary verbs",
            "Applied word order inversion (Verb + Subject)",
            "Used tag questions (¿verdad? / ¿no?) naturally",
            "Distinguished SABER (facts/skills) from CONOCER (people/places)",
            "Applied the personal 'a' with known persons (conozco a Carlos)",
            "Completed all 4 question formation exercises"
        ]
    },
    {
        "day": 28,
        "stage": 3,
        "title": "Negation & Negative Words",
        "subtitle": "No, Nunca, Nada, Nadie, Tampoco, Ninguno and the Spanish Double Negative",
        "goals": [
            "Master Spanish negative words: no, nunca (never), nada (nothing), nadie (nobody), tampoco (neither), ningún/ninguna (none)",
            "Understand that Spanish PROUDLY uses double (and triple!) negatives — unlike English",
            "Form natural negative sentences: *No tengo nada*, *No viene nadie*, *Yo tampoco*",
            "Shorten 'ninguno' to 'ningún' before masculine singular nouns"
        ],
        "bengaliNote": "In English grammar class, teachers scold you: 'Never use double negatives!'. But in Spanish (and just like in Bangla: 'আমি কাউকেই কিছু বলি না' = I don't tell nothing to nobody), double negatives are not just allowed — they are MANDATORY! *No sé nada* = I don't know nothing (I know nothing). It feels wonderfully natural to a Bengali speaker!",
        "vocabulary": [
            {"word": "No", "translation": "No / Not", "pos": "adverb", "gender": None, "example": "No hablo alemán.", "exampleTranslation": "I do not speak German."},
            {"word": "Nunca / Jamás", "translation": "Never", "pos": "adverb", "gender": None, "example": "Nunca llego tarde a clase.", "exampleTranslation": "I never arrive late to class."},
            {"word": "Nada", "translation": "Nothing / Not anything", "pos": "pronoun", "gender": None, "example": "No pasa nada.", "exampleTranslation": "Nothing is wrong / It's nothing (No problem)."},
            {"word": "Nadie", "translation": "Nobody / No one", "pos": "pronoun", "gender": None, "example": "No hay nadie en la sala.", "exampleTranslation": "There is nobody in the room."},
            {"word": "Tampoco", "translation": "Neither / Not either (opposite of también)", "pos": "adverb", "gender": None, "example": "—No me gusta el frío. —A mí tampoco.", "exampleTranslation": "—I don't like the cold. —Me neither."},
            {"word": "Ninguno / Ninguna (Ningún)", "translation": "None / Not any", "pos": "adjective / pronoun", "gender": "variable", "example": "No tengo ningún problema.", "exampleTranslation": "I have no problem at all."},
            {"word": "Ni... ni...", "translation": "Neither... nor...", "pos": "conjunction", "gender": None, "example": "No tengo ni tiempo ni dinero.", "exampleTranslation": "I have neither time nor money."},
            {"word": "Todavía no / Aún no", "translation": "Not yet", "pos": "phrase", "gender": None, "example": "Todavía no estoy listo.", "exampleTranslation": "I am not ready yet."},
            {"word": "Ya no", "translation": "No longer / Not anymore", "pos": "phrase", "gender": None, "example": "Ya no vivo allí.", "exampleTranslation": "I no longer live there."},
            {"word": "De ninguna manera", "translation": "By no means / No way", "pos": "phrase", "gender": None, "example": "De ninguna manera es culpa tuya.", "exampleTranslation": "In no way is it your fault."}
        ],
        "sentences": [
            {"spanish": "No sé nada sobre este tema.", "english": "I don't know anything about this topic. (Double negative)"},
            {"spanish": "Hoy no viene nadie a la fiesta.", "english": "Today nobody is coming to the party."},
            {"spanish": "Yo no fumo y mi compañero tampoco fuma.", "english": "I don't smoke and my roommate doesn't smoke either."},
            {"spanish": "No tengo ningún billete para el concierto.", "english": "I have no ticket for the concert. (ninguno -> ningún)"},
            {"spanish": "Nunca viajo en avión si puedo ir en tren.", "english": "I never travel by plane if I can go by train."},
            {"spanish": "No pasa nada, tranquilo.", "english": "Don't worry, nothing's wrong (it's totally fine)."}
        ],
        "grammar": {
            "title": "The Spanish Double Negative Rule & The Negative Word Pairs",
            "explanation": "In Spanish, if a negative word (*nada, nadie, nunca, tampoco, ninguno*) comes AFTER the verb, the verb MUST also be preceded by 'NO'!",
            "rules": [
                "The Golden Double Negative Rule: If the negative word is after the verb: **NO + Verb + [Negative Word]**. E.g. *No sé NADA* (I know nothing), *No veo a NADIE* (I see nobody), *No voy NUNCA* (I never go).",
                "Single Negative Rule (Word before verb): If the negative word is placed BEFORE the verb, you do NOT use 'no': *Nadie vino* (Nobody came), *Nunca voy allí* (Never do I go there). Both styles mean the exact same thing!",
                "Ninguno drops the -o: Directly before a masculine singular noun, *ninguno* drops the -o and gains an accent: *ningún libro*, *ningún problema* (NOT *ninguno libro*). For feminine: *ninguna persona*.",
                "Affirmative vs. Negative Pairs: algo (something) <-> nada (nothing); alguien (someone) <-> nadie (nobody); siempre (always) <-> nunca (never); también (also) <-> tampoco (neither); algún (some) <-> ningún (none)."
            ],
            "structures": [
                "Double Negative: NO + [Verbo] + nada / nadie / nunca / tampoco / ningún",
                "Fronted Negative: Nunca / Nadie / Nada + [Verbo] (no 'no' needed)",
                "Shortening: ningún + [sustantivo masculino singular]"
            ],
            "examples": [
                {"spanish": "No hay nadie aquí. = Nadie hay aquí.", "english": "There is nobody here."},
                {"spanish": "No tengo nada en los bolsillos.", "english": "I have nothing in my pockets."},
                {"spanish": "No hay ningún error.", "english": "There is not a single error."},
                {"spanish": "—No hablo francés. —Yo tampoco.", "english": "—I don't speak French. —Me neither."}
            ],
            "commonMistakes": [
                {"wrong": "Sé nada (missing 'no')", "right": "No sé nada", "explanation": "If 'nada' follows the verb, 'no' MUST precede the verb."},
                {"wrong": "Yo también no", "right": "Yo tampoco", "explanation": "'También no' does not exist in Spanish; use 'tampoco' (neither)."}
            ],
            "proTip": "The most comforting Spanish phrase in existence: **«¡No pasa nada!»** (Literally: Nothing happens! It means: No worries, don't worry about it, it's all good!). You will hear it 10 times a day in Spain."
        },
        "conversation": {
            "title": "A Quiet Sunday Morning",
            "context": "Sakib and Alberto wake up on a sleepy Sunday in their apartment.",
            "dialogue": [
                {"speaker": "Alberto", "role": "Roommate", "spanish": "¿Hay alguien en la cocina?", "english": "Is there someone in the kitchen?"},
                {"speaker": "Sakib", "role": "Student", "spanish": "No, no hay nadie. Estoy yo solo preparando té.", "english": "No, there is nobody. It's just me preparing tea."},
                {"speaker": "Alberto", "role": "Roommate", "spanish": "¿Queda algo de leche en la nevera?", "english": "Is there any milk left in the fridge?"},
                {"speaker": "Sakib", "role": "Student", "spanish": "No, no queda nada de leche ni pan.", "english": "No, there is nothing left of milk nor bread."},
                {"speaker": "Alberto", "role": "Roommate", "spanish": "¡Vaya! Y los domingos no abre ninguna tienda cerca.", "english": "Wow! And on Sundays not a single shop opens nearby."},
                {"speaker": "Sakib", "role": "Student", "spanish": "No pasa nada. Hay una cafetería abierta en la esquina. Podemos desayunar allí.", "english": "No problem! There is a café open on the corner. We can have breakfast there."},
                {"speaker": "Alberto", "role": "Roommate", "spanish": "¡Perfecto! Yo tampoco tengo ganas de cocinar hoy.", "english": "Perfect! I don't feel like cooking today either."}
            ],
            "keyPhrases": [
                {"phrase": "¿Hay alguien?", "explanation": "'Is there anybody / someone?'"},
                {"phrase": "No queda nada", "explanation": "'There is nothing left'."},
                {"phrase": "Yo tampoco", "explanation": "'Me neither'."}
            ]
        },
        "reading": {
            "title": "La tranquilidad de un domingo en Madrid",
            "passage": "Los domingos por la mañana, Madrid parece una ciudad diferente. No hay casi nadie en las calles antes de las diez. No se escucha ningún ruido de tráfico ni bocinas. Muchas tiendas tradicionales no abren, pero las panaderías y las cafeterías siempre tienen sus puertas abiertas. Sakib camina tranquilamente por su barrio. No tiene prisa, no tiene tareas pendientes y no piensa en nada estresante. Respira el aire fresco de la mañana y disfruta del silencio. En una sociedad que siempre corre, aprender a no hacer nada es un arte maravilloso.",
            "translation": "On Sunday mornings, Madrid seems like a different city. There is almost nobody in the streets before ten. Not a single sound of traffic or horns is heard. Many traditional shops do not open, but bakeries and cafés always have their doors open. Sakib walks peacefully through his neighborhood. He is in no hurry, has no pending tasks, and thinks about nothing stressful. He breathes the fresh morning air and enjoys the silence. In a society that always rushes, learning to do nothing is a wonderful art.",
            "questions": [
                {"question": "¿Cómo son las calles de Madrid los domingos antes de las diez?", "options": ["Llenas de tráfico ruidoso", "No hay casi nadie y no se escucha ningún ruido", "Cerradas con muros", "Llenas de coches de policía"], "answer": 1, "explanation": "Almost nobody and no noise ('no hay casi nadie...')."},
                {"question": "¿Qué lugares siempre tienen sus puertas abiertas?", "options": ["Los bancos", "Las panaderías y cafeterías", "Los ministerios", "Las fábricas"], "answer": 1, "explanation": "Bakeries and cafés ('las panaderías y cafeterías')."},
                {"question": "¿En qué piensa Sakib mientras camina?", "options": ["En sus exámenes difíciles", "En nada estresante", "En comprar un coche", "En volver a su país"], "answer": 1, "explanation": "In nothing stressful ('no piensa en nada estresante')."}
            ]
        },
        "exercises": [
            {
                "id": "d28-ex1",
                "type": "fill-in",
                "prompt": "Complete with double negative: Yo no sé ______ (nothing) sobre eso.",
                "options": ["nada", "nadie", "nunca", "ninguno"],
                "correct": 0,
                "explanation": "'No sé nada' is the correct double negative structure."
            },
            {
                "id": "d28-ex2",
                "type": "multiple-choice",
                "prompt": "How do you respond to 'No me gusta el frío' to mean 'Me neither'?",
                "options": ["A mí también", "A mí tampoco", "Yo también no", "No a mí"],
                "correct": 1,
                "explanation": "'A mí tampoco' means 'Me neither'."
            },
            {
                "id": "d28-ex3",
                "type": "fill-in",
                "prompt": "Shorten 'ninguno' before masculine noun: No tengo ______ (ninguno) problema.",
                "options": ["ningún", "ninguno", "ninguna", "ningunos"],
                "correct": 0,
                "explanation": "'Ninguno' drops the -o before masculine singular nouns: 'ningún problema'."
            },
            {
                "id": "d28-ex4",
                "type": "translation",
                "prompt": "Translate: 'No problem / It's totally fine!'",
                "options": ["¡No pasa nada!", "¡No tiene nada!", "¡No es nada problema!", "¡Nunca pasa nada!"],
                "correct": 0,
                "explanation": "'¡No pasa nada!' is the universal Spanish reassurance."
            }
        ],
        "speakingChallenge": [
            {"prompt": "Say that you don't know anything about a subject using a double negative.", "hint": "No sé nada de...", "sampleAnswer": "Lo siento, no sé nada sobre ese asunto."},
            {"prompt": "Say 'Me neither' when someone says they don't like rain.", "hint": "A mí tampoco me gusta...", "sampleAnswer": "A mí tampoco me gusta la lluvia cuando tengo que salir."},
            {"prompt": "Reassure someone who apologized to you with '¡No pasa nada!'.", "hint": "Tranquilo, no pasa nada.", "sampleAnswer": "Tranquilo, amigo, no te preocupes, ¡no pasa nada!"}
        ],
        "dailyRevision": {
            "quickQuestions": [
                "How does the Spanish double negative work?",
                "What is the negative equivalent of 'también'?"
            ],
            "grammarRecall": "NO + Verb + nada/nadie/nunca/tampoco/ningún. Ninguno -> ningún before masculine singular nouns.",
            "vocabRecall": ["No", "Nunca", "Nada", "Nadie", "Tampoco", "Ningún", "No pasa nada", "Todavía no"]
        },
        "checklist": [
            "Constructed authentic Spanish double negatives (no sé nada)",
            "Learned fronted negatives (nadie vino, nunca voy)",
            "Used 'tampoco' instead of 'también no'",
            "Shortened ninguno to ningún before masculine nouns",
            "Completed all 4 negation exercises",
            "Said '¡No pasa nada!' out loud with natural Spanish rhythm"
        ]
    },
    {
        "day": 29,
        "stage": 3,
        "title": "The Verb GUSTAR: Likes & Dislikes",
        "subtitle": "Mastering Me Gusta vs. Me Gustan, Te Gusta, and Indirect Object Pronouns",
        "goals": [
            "Understand that GUSTAR literally means 'To be pleasing to someone'",
            "Use 'Me gusta' with singular nouns and infinitive verbs",
            "Use 'Me gustan' with plural nouns",
            "Master all indirect object pronouns: me, te, le, nos, os, les gusta(n)"
        ],
        "bengaliNote": "GUSTAR works EXACTLY like Bangla! In English, you say 'I like the book' (I do the action). But in Bangla, you say: 'বইটা আমার ভালো লাগে' (The book is pleasing to me!). In Spanish, it is identical: *El libro me gusta* (The book pleases me)! Because the thing liked is the true subject, the verb ONLY has two forms: **gusta** (for one thing or actions) and **gustan** (for multiple things)!",
        "vocabulary": [
            {"word": "Gustar", "translation": "To be pleasing to / To like", "pos": "verb", "gender": None, "example": "Me gusta el español.", "exampleTranslation": "I like Spanish (Spanish is pleasing to me)."},
            {"word": "Me gusta / Me gustan", "translation": "I like (singular item / plural items)", "pos": "phrase", "gender": None, "example": "Me gusta la paella / Me gustan las tapas.", "exampleTranslation": "I like paella / I like tapas."},
            {"word": "¿Te gusta? / ¿Te gustan?", "translation": "Do you like? (singular / plural)", "pos": "phrase", "gender": None, "example": "¿Te gusta vivir en Madrid?", "exampleTranslation": "Do you like living in Madrid?"},
            {"word": "Le gusta / Le gustan", "translation": "He/She/You formal likes", "pos": "phrase", "gender": None, "example": "A María le gusta leer libros.", "exampleTranslation": "Maria likes to read books."},
            {"word": "Nos gusta / Nos gustan", "translation": "We like", "pos": "phrase", "gender": None, "example": "Nos gusta viajar juntos.", "exampleTranslation": "We like to travel together."},
            {"word": "Encantar (me encanta / me encantan)", "translation": "To love / To enchant (stronger than gustar)", "pos": "verb", "gender": None, "example": "¡Me encanta la música española!", "exampleTranslation": "I love Spanish music!"},
            {"word": "No me gusta nada", "translation": "I don't like it at all", "pos": "phrase", "gender": None, "example": "No me gusta nada el frío.", "exampleTranslation": "I don't like the cold at all."},
            {"word": "A mí también / A mí tampoco", "translation": "Me too / Me neither (with gustar)", "pos": "phrase", "gender": None, "example": "—Me gusta el fútbol. —A mí también.", "exampleTranslation": "—I like football. —Me too."},
            {"word": "La música / El cine / El deporte", "translation": "Music / Cinema / Sports", "pos": "noun", "gender": "mixed", "example": "Me gusta mucho el cine español.", "exampleTranslation": "I like Spanish cinema a lot."},
            {"word": "Pasar tiempo con amigos", "translation": "To spend time with friends", "pos": "phrase", "gender": None, "example": "Me gusta pasar tiempo con mis amigos.", "exampleTranslation": "I like to spend time with my friends."}
        ],
        "sentences": [
            {"spanish": "Me gusta mucho aprender idiomas nuevos.", "english": "I like learning new languages very much. (Infinitive verb -> gusta)"},
            {"spanish": "Me gustan las ciudades históricas de España.", "english": "I like the historic cities of Spain. (Plural noun -> gustan)"},
            {"spanish": "¿Te gusta la comida picante? —Sí, me encanta.", "english": "Do you like spicy food? —Yes, I love it."},
            {"spanish": "A mis compañeros les gustan las tapas de Madrid.", "english": "My classmates like the tapas of Madrid."},
            {"spanish": "No me gusta nada levantarme temprano los domingos.", "english": "I don't like getting up early on Sundays at all."},
            {"spanish": "A nosotros nos gusta pasear por el parque del Retiro.", "english": "We like to stroll through Retiro park."}
        ],
        "grammar": {
            "title": "The Master Anatomy of GUSTAR: Me, Te, Le, Nos, Os, Les",
            "explanation": "Never say 'Yo gusto'! GUSTAR conjugates to match WHAT is liked, not the person who likes it.",
            "rules": [
                "Two Forms Only: 1) **gusta**: used before a singular noun (*el café*) OR any infinitive verb (*viajar, comer*). 2) **gustan**: used before plural nouns (*los libros, las playas*).",
                "Indirect Object Pronouns (Who is pleased?): me (to me) | te (to you) | le (to him/her/you formal) | nos (to us) | os (to you all) | les (to them/you all).",
                "Optional Emphasis with 'A': To emphasize or clarify who likes something, add 'a + person' at the start: *A mí me gusta* (As for me, I like), *A Carlos le gusta* (Carlos likes), *A nosotros nos gusta*.",
                "Expressing Degree: *Me encanta* (I love it!) > *Me gusta mucho* (I like a lot) > *Me gusta* (I like) > *No me gusta* (I don't like) > *No me gusta nada* (I don't like it at all!)."
            ],
            "structures": [
                "Singular Noun: [me/te/le/nos/os/les] + GUSTA + el/la [sustantivo singular]",
                "Plural Noun: [me/te/le/nos/os/les] + GUSTAN + los/las [sustantivos plurales]",
                "Action/Verb: [me/te/le/nos/os/les] + GUSTA + [Verbo en infinitivo]"
            ],
            "examples": [
                {"spanish": "Me gusta el libro. (Singular)", "english": "I like the book."},
                {"spanish": "Me gustan los libros. (Plural)", "english": "I like the books."},
                {"spanish": "Me gusta leer y escribir. (Infinitives take singular 'gusta'!)", "english": "I like reading and writing."},
                {"spanish": "A ella le encantan las flores.", "english": "She loves flowers."}
            ],
            "commonMistakes": [
                {"wrong": "Yo gusto el café", "right": "Me gusta el café", "explanation": "'Yo gusto' means 'I am pleasing/attractive to others'. Say 'Me gusta'."},
                {"wrong": "Me gusta los coches", "right": "Me gustan los coches", "explanation": "'Los coches' is plural, so the verb must be plural 'gustan'."}
            ],
            "proTip": "Even if you list ten action verbs, GUSTAR stays singular **gusta**: *Me gusta cantar, bailar, viajar y reír*! Actions are always singular in Spanish."
        },
        "conversation": {
            "title": "Talking About Hobbies and Passions",
            "context": "Sakib and his friend Sophie discuss what they enjoy doing outside class.",
            "dialogue": [
                {"speaker": "Sophie", "role": "Friend", "spanish": "Sakib, ¿qué te gusta hacer en tu tiempo libre?", "english": "Sakib, what do you like to do in your free time?"},
                {"speaker": "Sakib", "role": "Student", "spanish": "Me gusta mucho leer novelas históricas y escuchar música. Y los fines de semana me encanta cocinar para mis amigos.", "english": "I like reading historical novels and listening to music a lot. And on weekends I love cooking for my friends."},
                {"speaker": "Sophie", "role": "Friend", "spanish": "¿Te gusta el fútbol español?", "english": "Do you like Spanish football?"},
                {"speaker": "Sakib", "role": "Student", "spanish": "¡Sí, me encanta! Me gustan los partidos del Real Madrid. ¿Y a ti?", "english": "Yes, I love it! I like Real Madrid's matches. And you?"},
                {"speaker": "Sophie", "role": "Friend", "spanish": "A mí no me gusta mucho el fútbol, prefiero el cine y el teatro.", "english": "As for me, I don't like football much, I prefer cinema and theater."},
                {"speaker": "Sakib", "role": "Student", "spanish": "El cine español es buenísimo. Me gustan mucho las películas de Almodóvar.", "english": "Spanish cinema is wonderful. I like Almodovar's movies a lot."}
            ],
            "keyPhrases": [
                {"phrase": "¿Y a ti?", "explanation": "'And as for you?' (rebounding a gustar question)."},
                {"phrase": "Tiempo libre", "explanation": "'Free time / spare time'."},
                {"phrase": "Películas", "explanation": "'Movies / films'."}
            ]
        },
        "reading": {
            "title": "Las pasiones y aficiones de los españoles",
            "passage": "A los españoles les apasiona disfrutar de la vida al aire libre. Les encanta sentarse en las terrazas soleadas a tomar algo con amigos, charlar durante horas y compartir unas raciones de comida sabrosa. El fútbol es el deporte rey: a millones de personas les gustan los partidos de la liga española y los debaten apasionadamente. También les gusta mucho la cultura: España es uno de los países con más museos, festivales de música y fiestas tradicionales del mundo. A Sakib le fascina esta alegría de vivir y cada día se siente más integrado en el estilo de vida español.",
            "translation": "Spaniards are passionate about enjoying life outdoors. They love sitting on sunny terraces having a drink with friends, chatting for hours, and sharing portions of tasty food. Football is the king of sports: millions of people like the matches of the Spanish league and debate them passionately. They also like culture a lot: Spain is one of the countries with the most museums, music festivals, and traditional festivals in the world. Sakib is fascinated by this joy of living and every day feels more integrated into the Spanish lifestyle.",
            "questions": [
                {"question": "¿Dónde les encanta sentarse a los españoles con amigos?", "options": ["En sótanos oscuros", "En las terrazas soleadas", "En los coches", "En las estaciones de tren"], "answer": 1, "explanation": "On sunny terraces ('en las terrazas soleadas')."},
                {"question": "¿Cuál es el deporte rey en España?", "options": ["El cricket", "El fútbol", "El baloncesto", "El tenis"], "answer": 1, "explanation": "Football ('el fútbol es el deporte rey')."},
                {"question": "¿Qué le fascina a Sakib?", "options": ["El frío", "Esta alegría de vivir", "El precio del metro", "Los deberes difíciles"], "answer": 1, "explanation": "This joy of living ('esta alegría de vivir')."}
            ]
        },
        "exercises": [
            {
                "id": "d29-ex1",
                "type": "fill-in",
                "prompt": "Choose gusta or gustan: Me ______ los museos de Madrid.",
                "options": ["gustan", "gusta", "gusto", "gustar"],
                "correct": 0,
                "explanation": "'Los museos' is plural, so use 'gustan'."
            },
            {
                "id": "d29-ex2",
                "type": "fill-in",
                "prompt": "Choose gusta or gustan: Me ______ leer libros y viajar.",
                "options": ["gusta", "gustan", "gusto", "gustamos"],
                "correct": 0,
                "explanation": "Infinitive actions always take singular 'gusta'."
            },
            {
                "id": "d29-ex3",
                "type": "multiple-choice",
                "prompt": "How do you say 'We like Spanish' using indirect pronouns?",
                "options": ["Nos gusta el español", "Nosotros gustamos el español", "Nos gustan el español", "Se gusta el español"],
                "correct": 0,
                "explanation": "'Nos gusta el español' is the correct indirect object pronoun structure."
            },
            {
                "id": "d29-ex4",
                "type": "translation",
                "prompt": "Translate: 'I love Spanish food!'",
                "options": ["¡Me encanta la comida española!", "¡Yo amo la comida española!", "¡Me gusto la comida española!", "¡Me encantan la comida española!"],
                "correct": 0,
                "explanation": "'¡Me encanta la comida española!' (singular item -> me encanta)."
            }
        ],
        "speakingChallenge": [
            {"prompt": "Say 2 things you like and 1 thing you do NOT like in Spanish.", "hint": "Me gusta... pero no me gusta...", "sampleAnswer": "Me gusta la comida española y me gusta viajar, pero no me gusta el frío intenso."},
            {"prompt": "Say that you love listening to music using 'Me encanta'.", "hint": "Me encanta escuchar...", "sampleAnswer": "Me encanta escuchar música clásica y aprender canciones en español."},
            {"prompt": "Ask someone if they like living in their city.", "hint": "¿Te gusta vivir en...", "sampleAnswer": "¿Te gusta vivir en tu ciudad o prefieres otra?"}
        ],
        "dailyRevision": {
            "quickQuestions": [
                "Why does GUSTAR only have two main forms (gusta and gustan)?",
                "What form does GUSTAR take when followed by two verbs (e.g. bailar y cantar)?"
            ],
            "grammarRecall": "GUSTAR: me, te, le, nos, os, les + gusta (singular noun / verbs) or gustan (plural nouns). Encantar = to love.",
            "vocabRecall": ["Gustar", "Me gusta", "Me gustan", "¿Te gusta?", "Encantar", "No me gusta nada", "A mí también", "A mí tampoco"]
        },
        "checklist": [
            "Understood the true grammatical nature of GUSTAR (to be pleasing to)",
            "Applied 'me gusta' for singular nouns and infinitive actions",
            "Applied 'me gustan' for plural nouns",
            "Mastered indirect object pronouns (me, te, le, nos, os, les)",
            "Completed all 4 GUSTAR exercises",
            "Expressed personal passions out loud in Spanish"
        ]
    },
    {
        "day": 30,
        "stage": 3,
        "title": "Sentence Connectors & Conjunctions",
        "subtitle": "Y/E, O/U, Pero, Porque, Además, Entonces, Por eso + Stage 3 Milestone Assessment",
        "goals": [
            "Connect simple ideas into smooth, fluent, professional sentences",
            "Master coordinate conjunctions: y (and), o (or), pero (but), porque (because)",
            "Learn phonetic substitution rules: 'Y' becomes 'E' before 'i/hi'; 'O' becomes 'U' before 'o/ho'",
            "Use transition connectors: además (furthermore), entonces (then), por eso (therefore)",
            "Complete the Stage 3 Milestone Assessment (HALF-WAY POINT: 30 DAYS COMPLETED!)"
        ],
        "bengaliNote": "Connectors are the glue of human thought! In Bangla, we connect thoughts with এবং, অথবা, কিন্তু, কারণ, তাই. In Spanish, you will use *y, o, pero, porque, por eso*. Notice the brilliant phonetic rule: just as Bangla avoids harsh vowel clashes, Spanish changes 'y' to 'e' before an 'i' sound (*español e inglés*, NOT *español y inglés*)!",
        "vocabulary": [
            {"word": "Y / E", "translation": "And (y becomes 'e' before i- or hi- sounds)", "pos": "conjunction", "gender": None, "example": "Hablo español e inglés.", "exampleTranslation": "I speak Spanish and English (e replaces y before inglés)."},
            {"word": "O / U", "translation": "Or (o becomes 'u' before o- or ho- sounds)", "pos": "conjunction", "gender": None, "example": "Siete u ocho personas.", "exampleTranslation": "Seven or eight people (u replaces o before ocho)."},
            {"word": "Pero", "translation": "But", "pos": "conjunction", "gender": None, "example": "Estudio mucho, pero no estoy cansado.", "exampleTranslation": "I study a lot, but I am not tired."},
            {"word": "Porque", "translation": "Because", "pos": "conjunction", "gender": None, "example": "Estudio porque quiero superarme.", "exampleTranslation": "I study because I want to improve myself."},
            {"word": "Además", "translation": "Furthermore / In addition / Besides", "pos": "adverb", "gender": None, "example": "Es barato y, además, es de buena calidad.", "exampleTranslation": "It is cheap and, furthermore, it is of good quality."},
            {"word": "Entonces", "translation": "Then / In that case / So", "pos": "adverb", "gender": None, "example": "Si tienes hambre, entonces vamos a comer.", "exampleTranslation": "If you are hungry, then let's go eat."},
            {"word": "Por eso / Por lo tanto", "translation": "Therefore / That's why", "pos": "phrase", "gender": None, "example": "Me gusta la cultura, por eso vivo en España.", "exampleTranslation": "I like the culture, that's why I live in Spain."},
            {"word": "Aunque", "translation": "Although / Even though", "pos": "conjunction", "gender": None, "example": "Salgo a caminar aunque hace un poco de frío.", "exampleTranslation": "I go out to walk although it is a little cold."},
            {"word": "Sin embargo", "translation": "However / Nevertheless", "pos": "phrase", "gender": None, "example": "Es difícil; sin embargo, no me rindo.", "exampleTranslation": "It is difficult; however, I do not give up."},
            {"word": "Por un lado... por otro lado...", "translation": "On one hand... on the other hand...", "pos": "phrase", "gender": None, "example": "Por un lado me gusta viajar, por otro lado extraño mi casa.", "exampleTranslation": "On one hand I like traveling, on the other hand I miss home."}
        ],
        "sentences": [
            {"spanish": "Estudio español e historia de España.", "english": "I study Spanish and history of Spain. (e replaces y before historia)"},
            {"spanish": "¿Prefieres té u horchata?", "english": "Do you prefer tea or horchata? (u replaces o before horchata)"},
            {"spanish": "Quiero viajar a Sevilla, pero este mes no tengo dinero.", "english": "I want to travel to Seville, but this month I don't have money."},
            {"spanish": "Me encanta Madrid porque la gente es muy acogedora.", "english": "I love Madrid because the people are very welcoming."},
            {"spanish": "Hoy no hay clase; por eso voy a estudiar en la biblioteca.", "english": "Today there is no class; that is why I am going to study in the library."},
            {"spanish": "El piso es luminoso y, además, está muy bien comunicado.", "english": "The flat is bright and, in addition, is very well connected."}
        ],
        "grammar": {
            "title": "The Euphonic Substitution Rules: Y -> E and O -> U + Transition Connectors",
            "explanation": "Spanish hates harsh vowel repetitions (cacophony). To keep speech singing smoothly, Spanish alters 'y' and 'o' before identical sounds.",
            "rules": [
                "Y becomes E: Whenever the following word starts with the sound /i/ (written with letter **I** or **HI**), 'y' becomes **E**: *padres e hijos* (NOT *padres y hijos*), *español e inglés* (NOT *español y inglés*). Exception: If the 'i' forms a diphthong like /ya/ (*cobre y hierro*), keep 'y'.",
                "O becomes U: Whenever the following word starts with the sound /o/ (written with letter **O** or **HO**), 'o' becomes **U**: *siete u ocho* (NOT *siete o ocho*), *mujer u hombre* (NOT *mujer o hombre*).",
                "Cause vs. Effect: 1) **Porque** introduces the CAUSE: *Como porque tengo hambre.* 2) **Por eso** introduces the RESULT/EFFECT: *Tengo hambre, por eso como.*",
                "Punctuation with Connectors: Connectors like *sin embargo, además*, and *por eso* are normally followed by a comma when placed at the start of a clause."
            ],
            "structures": [
                "Euphonic Y -> E: [Palabra] + E + [Palabra con i- o hi-]",
                "Euphonic O -> U: [Palabra] + U + [Palabra con o- o ho-]",
                "Cause -> Effect: [Situación], por eso + [Resultado]",
                "Contrast: [Idea 1], pero / sin embargo + [Idea 2]"
            ],
            "examples": [
                {"spanish": "Geografía e historia.", "english": "Geography and history."},
                {"spanish": "Uno u otro.", "english": "One or the other."},
                {"spanish": "Estoy cansado, por eso me acuesto temprano.", "english": "I am tired, that's why I go to bed early."},
                {"spanish": "Es caro, además no me gusta el color.", "english": "It is expensive, furthermore I don't like the color."}
            ],
            "commonMistakes": [
                {"wrong": "Español y inglés", "right": "Español e inglés", "explanation": "'Y' must become 'e' before words starting with the sound /i/."},
                {"wrong": "Siete o ocho", "right": "Siete u ocho", "explanation": "'O' must become 'u' before words starting with /o/."}
            ],
            "proTip": "Using connectors like *además, entonces, por eso*, and *sin embargo* is the secret weapon that elevates your speech instantly from broken beginner sentences to polished, flowing A1+ Spanish!"
        },
        "conversation": {
            "title": "Reflecting on the 30-Day Milestone",
            "context": "Sakib and his teacher Carmen have a milestone progress review.",
            "dialogue": [
                {"speaker": "Profª Carmen", "role": "Teacher", "spanish": "¡Felicidades, Sakib! ¡Hoy cumples treinta días de desafío!", "english": "Congratulations, Sakib! Today you reach thirty days of the challenge!"},
                {"speaker": "Sakib", "role": "Student", "spanish": "¡Muchas gracias, Carmen! Parece mentira lo rápido que pasa el tiempo.", "english": "Thank you very much, Carmen! It seems unbelievable how fast time passes."},
                {"speaker": "Profª Carmen", "role": "Teacher", "spanish": "¿Cómo te sientes con tu español ahora?", "english": "How do you feel with your Spanish now?"},
                {"speaker": "Sakib", "role": "Student", "spanish": "Me siento muy seguro. Al principio me costaba entender, pero ahora comprendo las conversaciones cotidianas. Además, ya sé conectar oraciones y expresar mis gustos.", "english": "I feel very confident. At first it was hard to understand, but now I understand daily conversations. Furthermore, I already know how to connect sentences and express my likes."},
                {"speaker": "Profª Carmen", "role": "Teacher", "spanish": "Tienes un vocabulario de más de trescientas palabras y tu gramática es sólida. ¿Estás listo para la segunda mitad?", "english": "You have a vocabulary of over three hundred words and your grammar is solid. Are you ready for the second half?"},
                {"speaker": "Sakib", "role": "Student", "spanish": "¡Por supuesto que sí! Pienso seguir con la misma energía hasta el día sesenta.", "english": "Of course yes! I plan to continue with the same energy until day sixty."}
            ],
            "keyPhrases": [
                {"phrase": "¡Felicidades!", "explanation": "'Congratulations!'"},
                {"phrase": "Parece mentira", "explanation": "Common idiom meaning 'It seems hard to believe / unbelievable'."},
                {"phrase": "Me costaba...", "explanation": "'It was difficult/hard for me to...'"}
            ]
        },
        "reading": {
            "title": "Stage 3 Capstone: El ecuador del viaje — Treinta días cumplidos",
            "passage": "Llegar al día treinta significa alcanzar el ecuador del desafío de sesenta días. La transformación lingüística de Sakib es asombrosa. Hace solo un mes, las palabras en español eran sonidos misteriosos. Hoy, Sakib puede describir su rutina matutina con verbos reflexivos, dar y comprender direcciones por las calles de Madrid, comprar en tiendas y regatear educadamente. Conoce los verbos con cambio de raíz y domina las estructuras de gustar. Además, conecta sus pensamientos con fluidez utilizando conectores naturales. Su cuaderno personal tiene cientos de palabras útiles y ejemplos vivos. Con la mitad del camino recorrido, la meta de A1 brilla con total claridad.",
            "translation": "Reaching day thirty means reaching the halfway point (equator) of the sixty-day challenge. Sakib's linguistic transformation is astonishing. Just one month ago, Spanish words were mysterious sounds. Today, Sakib can describe his morning routine with reflexive verbs, give and understand directions in the streets of Madrid, shop in stores and transact politely. He knows stem-changing verbs and masters the structures of gustar. Furthermore, he connects his thoughts fluently using natural connectors. His personal notebook has hundreds of useful words and living examples. With half the journey traveled, the goal of A1 shines with total clarity.",
            "questions": [
                {"question": "¿Qué representa el día treinta en el desafío?", "options": ["El final del curso", "El ecuador (la mitad) del viaje de sesenta días", "Solo el principio", "El examen final"], "answer": 1, "explanation": "The halfway mark / equator ('el ecuador del desafío')."},
                {"question": "¿Qué puede hacer Sakib hoy con su español?", "options": ["Solo decir hola", "Describir su rutina, dar direcciones, comprar, usar gustar y conectar oraciones", "Traducir libros antiguos", "Trabajar como embajador"], "answer": 1, "explanation": "Describe routine, directions, shop, use gustar, connect sentences."},
                {"question": "¿Cómo brilla la meta de A1 ahora?", "options": ["Con miedo", "Con total claridad", "Muy lejana e imposible", "Oscura"], "answer": 1, "explanation": "With total clarity ('brilla con total claridad')."}
            ]
        },
        "exercises": [
            {
                "id": "d30-ex1",
                "type": "fill-in",
                "prompt": "Apply euphonic rule: Hablo español ______ (and) inglés.",
                "options": ["e", "y", "u", "o"],
                "correct": 0,
                "explanation": "'Y' becomes 'e' before words starting with /i/ sound: 'español e inglés'."
            },
            {
                "id": "d30-ex2",
                "type": "fill-in",
                "prompt": "Apply euphonic rule: Hay siete ______ (or) ocho personas.",
                "options": ["u", "o", "e", "y"],
                "correct": 0,
                "explanation": "'O' becomes 'u' before words starting with /o/ sound: 'siete u ocho'."
            },
            {
                "id": "d30-ex3",
                "type": "multiple-choice",
                "prompt": "What does 'por eso' express in a sentence?",
                "options": ["The cause", "The effect / result (therefore / that's why)", "A question", "A greeting"],
                "correct": 1,
                "explanation": "'Por eso' expresses the effect/result ('therefore / that's why')."
            },
            {
                "id": "d30-ex4",
                "type": "translation",
                "prompt": "Translate: 'I am tired, that's why I am going to sleep.'",
                "options": ["Estoy cansado, por eso voy a dormir.", "Estoy cansado, porque voy a dormir.", "Soy cansado, por eso voy a dormir.", "Tengo cansado, por eso duermo."],
                "correct": 0,
                "explanation": "'Estoy cansado, por eso voy a dormir' links condition and consequence perfectly."
            }
        ],
        "speakingChallenge": [
            {"prompt": "Say that you speak Bengali and English using the 'e' euphonic rule.", "hint": "Hablo bengalí e inglés...", "sampleAnswer": "Hablo bengalí e inglés, y ahora aprendo español."},
            {"prompt": "Connect two ideas using 'pero' and 'por eso'.", "hint": "Tengo mucho trabajo, pero... por eso...", "sampleAnswer": "Tengo mucho que estudiar, pero me encanta el idioma; por eso practico todos los días."},
            {"prompt": "Celebrate reaching Day 30 out loud in Spanish!", "hint": "¡Hoy cumplo treinta días...", "sampleAnswer": "¡Hoy cumplo treinta días de mi desafío de español! ¡Estoy a mitad de camino y voy a lograr mi meta!"}
        ],
        "dailyRevision": {
            "quickQuestions": [
                "When does 'y' change to 'e'? (Before words starting with i- or hi-)",
                "When does 'o' change to 'u'? (Before words starting with o- or ho-)"
            ],
            "grammarRecall": "Connectors: y/e, o/u, pero, porque, además, entonces, por eso, sin embargo. Y -> E before i/hi; O -> U before o/ho.",
            "vocabRecall": ["Y / E", "O / U", "Pero", "Porque", "Además", "Entonces", "Por eso", "Sin embargo", "Aunque"]
        },
        "checklist": [
            "Mastered the euphonic substitution rules: Y -> E and O -> U",
            "Connected clauses with pero, porque, además, and por eso",
            "Distinguished cause (porque) from consequence (por eso)",
            "Completed the Stage 3 Milestone Reading Passage",
            "Finished all 4 sentence connector exercises",
            "CELEBRATED THE 30-DAY HALFWAY MARK OF THE 60-DAY CHALLENGE! 🎉🇪🇸"
        ]
    }
]

# Combine both parts
stage3_complete = stage3_days + stage3_part2

with open("d:/ag/espanol-handbook/data/lessons/stage3.js", "w", encoding="utf-8") as f:
    f.write("// Stage 3: Days 21 to 30 (Building Better Sentences)\n")
    f.write("window.STAGE_3_LESSONS = ")
    json.dump(stage3_complete, f, ensure_ascii=False, indent=2)
    f.write(";\n")

print(f"Successfully generated stage3.js with all {len(stage3_complete)} full days!")
