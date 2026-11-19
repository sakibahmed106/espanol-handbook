"""
Build Stage 4: Days 36 to 40 + Combine Stage 4 into data/lessons/stage4.js
"""
import json
from build_stage4_part1 import stage4_days

stage4_part2 = [
    {
        "day": 36,
        "stage": 4,
        "title": "Hobbies, Sports & Free Time (JUGAR vs. TOCAR)",
        "subtitle": "Talking about leisure, sports, music, and the crucial distinction between JUGAR and TOCAR",
        "goals": [
            "Name common hobbies, free time pastimes, and popular sports in Spanish",
            "Master the difference: JUGAR (to play sports/games) vs. TOCAR (to play musical instruments)",
            "Use the preposition 'a' with sports: *jugar al fútbol, jugar al tenis*",
            "Express frequency of hobbies (a menudo, de vez en cuando, los fines de semana)"
        ],
        "bengaliNote": "In English, the verb 'play' is used for both sports ('play football') and instruments ('play guitar'). But in Spanish and Bangla, these are separate actions! For sports/games, use **JUGAR AL** (*খেলা করা*); for musical instruments, use **TOCAR** (literally: to touch / *বাজানো*)! Never say 'jugar la guitarra'!",
        "vocabulary": [
            {"word": "El tiempo libre / Los pasatiempos", "translation": "Free time / Hobbies, pastimes", "pos": "noun", "gender": "masculine", "example": "En mi tiempo libre leo novelas.", "exampleTranslation": "In my free time I read novels."},
            {"word": "Jugar (al fútbol, al baloncesto, al tenis)", "translation": "To play (sports/games: u -> ue)", "pos": "verb", "gender": None, "example": "Juego al fútbol con mis amigos.", "exampleTranslation": "I play football with my friends."},
            {"word": "Tocar (la guitarra, el piano, la batería)", "translation": "To play (musical instrument) / To touch", "pos": "verb", "gender": None, "example": "Toco la guitarra española.", "exampleTranslation": "I play the Spanish guitar."},
            {"word": "Hacer deporte / ejercicio", "translation": "To do sports / exercise", "pos": "phrase", "gender": None, "example": "Hago deporte tres veces por semana.", "exampleTranslation": "I do sports three times a week."},
            {"word": "Ver películas / series", "translation": "To watch movies / series", "pos": "phrase", "gender": None, "example": "Veo series en español en Netflix.", "exampleTranslation": "I watch series in Spanish on Netflix."},
            {"word": "Bailar (salsa, flamenco)", "translation": "To dance (salsa, flamenco)", "pos": "verb", "gender": None, "example": "Quiero aprender a bailar salsa.", "exampleTranslation": "I want to learn to dance salsa."},
            {"word": "Cocinar", "translation": "To cook", "pos": "verb", "gender": None, "example": "Cocinar es mi gran pasión.", "exampleTranslation": "Cooking is my great passion."},
            {"word": "Pintar / Dibujar", "translation": "To paint / To draw", "pos": "verb", "gender": None, "example": "Pinto cuadros al óleo.", "exampleTranslation": "I paint oil paintings."},
            {"word": "A menudo / De vez en cuando", "translation": "Often / From time to time", "pos": "adverb", "gender": None, "example": "Juego al tenis a menudo.", "exampleTranslation": "I play tennis often."},
            {"word": "El fin de semana", "translation": "The weekend", "pos": "noun", "gender": "masculine", "example": "El fin de semana salgo al campo.", "exampleTranslation": "On the weekend I go out to the countryside."}
        ],
        "sentences": [
            {"spanish": "En mi tiempo libre me gusta tocar la guitarra y cocinar.", "english": "In my free time I like playing the guitar and cooking."},
            {"spanish": "¿Juegas al fútbol los sábados? —Sí, juego con mis compañeros.", "english": "Do you play football on Saturdays? —Yes, I play with my classmates."},
            {"spanish": "Mi hermana toca el piano desde los siete años.", "english": "My sister plays the piano since seven years old."},
            {"spanish": "De vez en cuando voy al cine a ver películas independientes.", "english": "From time to time I go to the cinema to watch indie movies."},
            {"spanish": "¿Haces algún deporte para mantenerte en forma?", "english": "Do you do any sport to stay in shape?"},
            {"spanish": "Veo series españolas para mejorar mi comprensión auditiva.", "english": "I watch Spanish series to improve my listening comprehension."}
        ],
        "grammar": {
            "title": "The Golden Rule: JUGAR vs. TOCAR & Conjugation of JUGAR",
            "explanation": "One of the quickest ways to sound like a true Spanish speaker is using JUGAR and TOCAR correctly.",
            "rules": [
                "JUGAR (Sports & Games): Always followed by the preposition **a** + article (*al fútbol, al tenis, al ajedrez* = chess, *a las cartas* = cards). Jugar is an irregular stem-changer: u -> ue! **juego, juegas, juega, jugamos, jugáis, juegan**.",
                "TOCAR (Instruments): Followed DIRECTLY by the definite article + instrument: *toco la guitarra, tocas el piano, toca el violín*. No preposition 'a' is used!",
                "VER vs. MIRAR: Use **ver** for watching movies, TV, or series (*ver una película*). Use **mirar** for looking intentionally at something (*mirar una foto*, *mirar por la ventana*).",
                "Frequency Hierarchy: Siempre (always) > A menudo (often) > De vez en cuando (from time to time) > Raras veces (rarely) > Nunca (never)."
            ],
            "structures": [
                "Sports Formula: JUGAR + a + el/la [deporte] -> Jugar al fútbol / tenis",
                "Instruments Formula: TOCAR + el/la [instrumento] -> Tocar la guitarra / el piano",
                "JUGAR Present: juego | juegas | juega | jugamos | jugáis | juegan"
            ],
            "examples": [
                {"spanish": "Juego al baloncesto los domingos.", "english": "I play basketball on Sundays."},
                {"spanish": "Mi amigo toca la batería en un grupo de rock.", "english": "My friend plays the drums in a rock band."},
                {"spanish": "Jugamos al ajedrez por las tardes.", "english": "We play chess in the afternoons. (Nosotros: regular!)"},
                {"spanish": "Vemos una serie muy interesante.", "english": "We are watching a very interesting series."}
            ],
            "commonMistakes": [
                {"wrong": "Juego la guitarra (disastrous error)", "right": "Toco la guitarra", "explanation": "Instruments take 'tocar', never 'jugar'."},
                {"wrong": "Juego fútbol (missing 'al')", "right": "Juego al fútbol", "explanation": "In standard Spain Spanish, sports with jugar require 'a + el' -> 'al'."}
            ],
            "proTip": "In Spain, playing padel tennis (*jugar al pádel*) is enormously popular among people of all ages! If a Spanish colleague invites you: *«¿Te apetece jugar un partido de pádel el sábado?»*, say *«¡Claro que sí!»*."
        },
        "conversation": {
            "title": "Chatting About Weekend Passions",
            "context": "Sakib and his friend Javier share what they do on Saturday afternoons.",
            "dialogue": [
                {"speaker": "Javier", "role": "Friend", "spanish": "Sakib, este sábado jugamos un partido de fútbol sala. ¿Te apetece jugar con nosotros?", "english": "Sakib, this Saturday we're playing a futsal match. Do you fancy playing with us?"},
                {"speaker": "Sakib", "role": "Student", "spanish": "¡Me encantaría! Me gusta mucho el fútbol, aunque hace tiempo que no juego.", "english": "I would love to! I like football a lot, although it's been a while since I played."},
                {"speaker": "Javier", "role": "Friend", "spanish": "No te preocupes, jugamos para divertirnos y hacer un poco de ejercicio.", "english": "Don't worry, we play to have fun and do a little exercise."},
                {"speaker": "Sakib", "role": "Student", "spanish": "¿Y después qué hacéis?", "english": "And afterwards what do you all do?"},
                {"speaker": "Javier", "role": "Friend", "spanish": "Después tomamos unas cañas y a veces mi amigo Pablo toca la guitarra y cantamos canciones.", "english": "Afterwards we have some drinks and sometimes my friend Pablo plays the guitar and we sing songs."},
                {"speaker": "Sakib", "role": "Student", "spanish": "¡Qué planazo! Cuenta conmigo.", "english": "What a fantastic plan! Count on me."}
            ],
            "keyPhrases": [
                {"phrase": "¿Te apetece...?", "explanation": "Extremely common conversational phrase: 'Do you fancy / feel like [doing something]?'"},
                {"phrase": "¡Qué planazo!", "explanation": "Spain slang: 'What an awesome plan!' (-azo adds grand scale)."},
                {"phrase": "Cuenta conmigo", "explanation": "'Count on me / I'm in'."}
            ]
        },
        "reading": {
            "title": "El ocio y el tiempo libre en la cultura española",
            "passage": "El concepto del tiempo libre en España está íntimamente ligado a la vida social y a la comunidad. Para los españoles, el ocio no significa aislarse en una habitación, sino compartir momentos con amigos y familiares. Los fines de semana, los parques se llenan de personas corriendo, montando en bicicleta o jugando al fútbol. En las escuelas de música y centros culturales, miles de jóvenes aprenden a tocar instrumentos tradicionales como la guitarra flamenca o el cajón. Además, la afición por la gastronomía es enorme: cocinar para los seres queridos y disfrutar de una buena comida compartida es, sin duda, uno de los pasatiempos favoritos de la sociedad española.",
            "translation": "The concept of free time in Spain is intimately linked to social life and community. For Spaniards, leisure does not mean isolating oneself in a room, but sharing moments with friends and family. On weekends, parks fill with people running, riding bicycles, or playing football. In music schools and cultural centers, thousands of young people learn to play traditional instruments like the flamenco guitar or the cajón. Furthermore, the passion for gastronomy is enormous: cooking for loved ones and enjoying a good shared meal is, without doubt, one of the favorite pastimes of Spanish society.",
            "questions": [
                {"question": "¿Qué significa el ocio para los españoles?", "options": ["Aislarse en una habitación", "Compartir momentos con amigos y familiares", "Trabajar horas extra", "Dormir todo el día"], "answer": 1, "explanation": "Sharing moments with friends and family ('compartir momentos...')."},
                {"question": "¿Qué instrumentos tradicionales aprenden los jóvenes?", "options": ["Gaita escocesa", "Guitarra flamenca y el cajón", "Trompeta japonesa", "Órgano de iglesia"], "answer": 1, "explanation": "Flamenco guitar and cajón ('la guitarra flamenca o el cajón')."},
                {"question": "¿Cuál es uno de los pasatiempos favoritos de la sociedad española?", "options": ["Comprar coches caros", "Cocinar para los seres queridos y compartir comida", "Mirar el móvil solos", "Correr maratones siempre"], "answer": 1, "explanation": "Cooking for loved ones and sharing meals."}
            ]
        },
        "exercises": [
            {
                "id": "d36-ex1",
                "type": "fill-in",
                "prompt": "Choose JUGAR or TOCAR: Mi hermano ______ (plays) el piano muy bien.",
                "options": ["toca", "juega", "hace", "ve"],
                "correct": 0,
                "explanation": "Musical instruments strictly take 'tocar': 'toca el piano'."
            },
            {
                "id": "d36-ex2",
                "type": "fill-in",
                "prompt": "Complete with the correct preposition: Los domingos juego ______ (to the) fútbol.",
                "options": ["al", "a la", "en el", "el"],
                "correct": 0,
                "explanation": "Sports with jugar take 'a + el' -> 'al fútbol'."
            },
            {
                "id": "d36-ex3",
                "type": "multiple-choice",
                "prompt": "What does '¿Te apetece...?' mean?",
                "options": ["Are you angry?", "Do you fancy / feel like doing something?", "What is your appetite?", "Where are you going?"],
                "correct": 1,
                "explanation": "'¿Te apetece...?' is the colloquial Spain way to invite someone ('Do you fancy...?')."
            },
            {
                "id": "d36-ex4",
                "type": "translation",
                "prompt": "Translate: 'In my free time I play tennis and watch series.'",
                "options": ["En mi tiempo libre juego al tenis y veo series.", "En mi tiempo libre toco el tenis y miro series.", "En mi tiempo libre hago el tenis y tengo series.", "En mi tiempo libre juego tenis y veo serie."],
                "correct": 0,
                "explanation": "'En mi tiempo libre juego al tenis y veo series' uses accurate prepositions and verbs."
            }
        ],
        "speakingChallenge": [
            {"prompt": "Say what hobbies you do in your free time.", "hint": "En mi tiempo libre me gusta... y...", "sampleAnswer": "En mi tiempo libre me gusta leer libros, escuchar música y cocinar platos deliciosos."},
            {"prompt": "Say that you play a sport or musical instrument.", "hint": "Juego al... / Toco el...", "sampleAnswer": "Juego al fútbol de vez en cuando y toco la guitarra acústica."},
            {"prompt": "Invite a friend to play a match or go to the cinema using '¿Te apetece...?'.", "hint": "¿Te apetece ir al cine...", "sampleAnswer": "¿Te apetece ir al cine este sábado a ver una película española?"}
        ],
        "dailyRevision": {
            "quickQuestions": [
                "What verb is used for sports vs. musical instruments?",
                "What preposition is required after JUGAR when naming a sport?"
            ],
            "grammarRecall": "JUGAR al fútbol/tenis (sports). TOCAR la guitarra/piano (instruments). Ver películas vs. mirar fotos.",
            "vocabRecall": ["El tiempo libre", "Jugar al fútbol", "Tocar la guitarra", "Hacer deporte", "Ver películas", "Bailar", "¿Te apetece?"]
        },
        "checklist": [
            "Distinguished JUGAR (sports/games) from TOCAR (musical instruments)",
            "Conjugated the stem-changing verb JUGAR (juego, juegas, juega...)",
            "Applied 'jugar al [deporte]' with proper preposition",
            "Used conversational invitation '¿Te apetece...?'",
            "Completed all 4 hobby exercises",
            "Described personal leisure activities aloud in Spanish"
        ]
    },
    {
        "day": 37,
        "stage": 4,
        "title": "Modal Verbs: QUERER & PODER in Depth",
        "subtitle": "Asking permissions, expressing ability, and ordering politely with Quisiera and Podría",
        "goals": [
            "Deepen mastery of modal auxiliary verbs: QUERER (to want) and PODER (can / to be able to)",
            "Understand how modal verbs combine with infinitive actions (*puedo ir, quiero hablar*)",
            "Learn ultra-polite conditional forms: *quisiera* (I would like) and *¿podría...?* (could you...?)",
            "Express permissions, possibilities, and polite requests across everyday situations"
        ],
        "bengaliNote": "Modal verbs give your Spanish sophistication! In English, you say 'Can you help me?' or 'Could you help me?'. In Spanish, *«¿Puedes ayudarme?»* is friendly, while *«¿Podría ayudarme?»* (could you) and *«Quisiera un café»* (I would like) represent the highest level of European Spanish courtesy — like Bangla 'দয়া করে আপনি কি একটু সাহায্য করতে পারবেন?'.",
        "vocabulary": [
            {"word": "Quisiera (+ infinitivo)", "translation": "I would like (polite conditional form of querer)", "pos": "verb form", "gender": None, "example": "Quisiera reservar una mesa para dos.", "exampleTranslation": "I would like to book a table for two."},
            {"word": "¿Podría (+ infinitivo)?", "translation": "Could you / Could I? (polite conditional of poder)", "pos": "verb form", "gender": None, "example": "¿Podría traerme un vaso de agua?", "exampleTranslation": "Could you bring me a glass of water?"},
            {"word": "Poder (+ infinitivo)", "translation": "To be able to / Can", "pos": "verb", "gender": None, "example": "No puedo asistir a la reunión.", "exampleTranslation": "I cannot attend the meeting."},
            {"word": "Querer (+ infinitivo)", "translation": "To want to do something", "pos": "verb", "gender": None, "example": "Queremos mejorar nuestro acento.", "exampleTranslation": "We want to improve our accent."},
            {"word": "La reserva / Reservar", "translation": "The reservation / To reserve, book", "pos": "noun / verb", "gender": "feminine", "example": "Quisiera hacer una reserva para el viernes.", "exampleTranslation": "I would like to make a reservation for Friday."},
            {"word": "Ayudar / La ayuda", "translation": "To help / The help", "pos": "verb / noun", "gender": "feminine", "example": "¿Me puedes ayudar con este ejercicio?", "exampleTranslation": "Can you help me with this exercise?"},
            {"word": "Permiso / Con permiso", "translation": "Permission / Excuse me (passing through a crowd)", "pos": "noun / phrase", "gender": "masculine", "example": "Con permiso, tengo que pasar.", "exampleTranslation": "Excuse me, I have to pass through."},
            {"word": "Posible / Imposible", "translation": "Possible / Impossible", "pos": "adjective", "gender": "neutral", "example": "Es totalmente posible si estudias.", "exampleTranslation": "It is totally possible if you study."},
            {"word": "Cambiar", "translation": "To change / To exchange", "pos": "verb", "gender": None, "example": "¿Puedo cambiar este billete?", "exampleTranslation": "Can I change this ticket?"},
            {"word": "Probar / Probarse", "translation": "To try / To try on (food or clothes)", "pos": "verb", "gender": None, "example": "¿Puedo probarme esta chaqueta?", "exampleTranslation": "Can I try on this jacket?"}
        ],
        "sentences": [
            {"spanish": "Quisiera pedir un café cortado y una tostada con tomate.", "english": "I would like to order an espresso with a dash of milk and toast with tomato."},
            {"spanish": "¿Podría decirme dónde está la parada de autobús más cercana?", "english": "Could you tell me where the nearest bus stop is? (Ultra-polite)"},
            {"spanish": "¿Puedo entrar? —Sí, claro, adelante.", "english": "Can I come in? —Yes, of course, come in / go ahead."},
            {"spanish": "No podemos salir hoy porque llueve mucho.", "english": "We cannot go out today because it is raining hard."},
            {"spanish": "¿Quieres venir conmigo al Museo Reina Sofía?", "english": "Do you want to come with me to the Reina Sofia Museum?"},
            {"spanish": "¿Podemos pagar por separado, por favor?", "english": "Can we pay separately, please?"}
        ],
        "grammar": {
            "title": "Modal Architecture: Conjugated Verb + Infinitive & Polite Registers",
            "explanation": "When two verbs appear together in Spanish, only the FIRST verb is conjugated. The second verb remains untouched in its pure infinitive form (-ar, -er, -ir)!",
            "rules": [
                "Two-Verb Rule: **[Modal Conjugado] + [Infinitivo]**. E.g. *Quiero hablar* (I want to speak), *Puedo ayudar* (I can help). Never conjugate both verbs (*Quiero hablo* is a terrible error!).",
                "Quisiera (Polite Request): When ordering in restaurants, shops, or hotels, substituting *quiero* (I want) with *quisiera* (I would like) sounds infinitely softer and more elegant.",
                "Podría (Polite Condition): Use *¿Podría usted...?* when addressing strangers, elders, or officials: *¿Podría ayudarme?* (Could you help me?).",
                "Pronoun Placement with Infinitives: Object pronouns can attach directly to the END of the infinitive: *¿Puedes ayudarME?* (Can you help me?) or go before: *¿ME puedes ayudar?*. Both are 100% correct!"
            ],
            "structures": [
                "Desire: Quiero / Quisiera + [Infinitivo] (Quisiera hacer una reserva)",
                "Permission/Ability: ¿Puedo / Podría + [Infinitivo]? (¿Podría pasar?)",
                "Pronoun Attachment: ¿Puedes ayudarme? = ¿Me puedes ayudar?"
            ],
            "examples": [
                {"spanish": "Quisiera ver la carta de postres.", "english": "I would like to see the dessert menu."},
                {"spanish": "¿Podría hablar con el gerente?", "english": "Could I speak with the manager?"},
                {"spanish": "No puedo comer marisco, tengo alergia.", "english": "I cannot eat seafood, I have an allergy."},
                {"spanish": "¿Quieres acompañarme al banco?", "english": "Do you want to accompany me to the bank?"}
            ],
            "commonMistakes": [
                {"wrong": "Quiero hablo español", "right": "Quiero hablar español", "explanation": "The second verb MUST remain in the infinitive."},
                {"wrong": "Puedo voy (double conjugation)", "right": "Puedo ir", "explanation": "Conjugate only the modal verb: 'Puedo ir'."}
            ],
            "proTip": "When navigating a crowded Spanish train or metro car, say **«Con permiso»** (Excuse me / With permission). People will instantly clear a path for you with a smile!"
        },
        "conversation": {
            "title": "Booking a Hotel Room in Sevilla",
            "context": "Sakib calls a boutique hotel in Seville to book a room for his weekend trip.",
            "dialogue": [
                {"speaker": "Recepcionista", "role": "Hotel staff", "spanish": "Hotel Alcázar, buenas tardes. ¿En qué puedo ayudarle?", "english": "Hotel Alcazar, good afternoon. How can I help you?"},
                {"speaker": "Sakib", "role": "Caller", "spanish": "Buenas tardes. Quisiera hacer una reserva para este fin de semana, por favor.", "english": "Good afternoon. I would like to make a reservation for this weekend, please."},
                {"speaker": "Recepcionista", "role": "Hotel staff", "spanish": "Con mucho gusto. ¿Para cuántas noches y cuántas personas sería?", "english": "With pleasure. For how many nights and how many people would it be?"},
                {"speaker": "Sakib", "role": "Caller", "spanish": "Para dos noches: entrada el viernes y salida el domingo. Una habitación individual.", "english": "For two nights: check-in Friday and check-out Sunday. A single room."},
                {"speaker": "Recepcionista", "role": "Hotel staff", "spanish": "Tenemos una habitación luminosa con vistas al patio andaluz. Son sesenta euros por noche con desayuno incluido.", "english": "We have a bright room with views of the Andalusian patio. It is sixty euros per night with breakfast included."},
                {"speaker": "Sakib", "role": "Caller", "spanish": "¿Podría enviarme la confirmación por correo electrónico?", "english": "Could you send me the confirmation by email?"},
                {"speaker": "Recepcionista", "role": "Hotel staff", "spanish": "¡Por supuesto! Dígame su nombre completo y su dirección de correo.", "english": "Of course! Tell me your full name and your email address."}
            ],
            "keyPhrases": [
                {"phrase": "Con mucho gusto", "explanation": "'With great pleasure'."},
                {"phrase": "Entrada y salida", "explanation": "'Check-in and check-out'."},
                {"phrase": "Por correo electrónico", "explanation": "'By email'."}
            ]
        },
        "reading": {
            "title": "La cortesía y la amabilidad en el trato diario en España",
            "passage": "La cultura española se caracteriza por un trato humano cercano y cálido, pero en las situaciones de servicio público y hostelería, la cortesía marca la diferencia. Cuando una persona utiliza fórmulas educadas como «quisiera» en lugar de «quiero», o «¿podría ayudarme?» en lugar de «ayúdame», las puertas se abren de par en par. La palabra «con permiso» se utiliza al pasar entre una multitud en el metro o en un bar abarrotado. Saber modular el lenguaje entre la cercanía informal con los amigos y el respeto educado con personas desconocidas es una habilidad fundamental de la competencia comunicativa. Sakib practica estas formas elegantes todos los días y nota cómo los camareros y empleados le responden con especial amabilidad.",
            "translation": "Spanish culture is characterized by close, warm human interaction, but in situations of public service and hospitality, courtesy makes all the difference. When a person uses polite formulas like 'quisiera' instead of 'quiero', or 'could you help me?' instead of 'help me', doors open wide. The phrase 'con permiso' is used when passing through a crowd on the metro or in a crowded bar. Knowing how to modulate language between informal closeness with friends and polite respect with strangers is a fundamental skill of communicative competence. Sakib practices these elegant forms every day and notices how waiters and employees answer him with special kindness.",
            "questions": [
                {"question": "¿Qué fórmula educada sustituye a 'quiero' en un restaurante?", "options": ["Dame", "Quisiera", "Tengo que", "Voy a"], "answer": 1, "explanation": "'Quisiera' is the polite substitution ('utiliza fórmulas educadas como quisiera')."},
                {"question": "¿Cuándo se utiliza la expresión 'con permiso'?", "options": ["Al pagar la cuenta", "Al pasar entre una multitud en el metro o bar", "Al despedirse por la noche", "Al empezar a comer"], "answer": 1, "explanation": "When passing through a crowd ('al pasar entre una multitud')."},
                {"question": "¿Qué nota Sakib cuando utiliza estas formas educadas?", "options": ["Que no le entienden", "Que le cobran más caro", "Que le responden con especial amabilidad", "Que la gente se enfada"], "answer": 2, "explanation": "People answer him with special kindness ('le responden con especial amabilidad')."}
            ]
        },
        "exercises": [
            {
                "id": "d37-ex1",
                "type": "multiple-choice",
                "prompt": "How do you politely say 'I would like to book a room' in Spanish?",
                "options": ["Quisiera reservar una habitación", "Yo quiero reservo una habitación", "Puedo reservo la habitación", "Tengo que reserva la habitación"],
                "correct": 0,
                "explanation": "'Quisiera reservar una habitación' uses polite 'quisiera' followed by an infinitive."
            },
            {
                "id": "d37-ex2",
                "type": "fill-in",
                "prompt": "When using two verbs together: Yo quiero ______ (hablar) con el profesor.",
                "options": ["hablar", "hablo", "habla", "hablas"],
                "correct": 0,
                "explanation": "The second verb must remain in the infinitive: 'hablar'."
            },
            {
                "id": "d37-ex3",
                "type": "multiple-choice",
                "prompt": "Where can the pronoun 'me' go in '¿Puedes ayudarme?'?",
                "options": ["Only attached to the end of ayudar", "Either attached to the end (ayudarme) OR before puedes (me puedes ayudar)", "Only at the very end of the sentence", "Nowhere"],
                "correct": 1,
                "explanation": "With an infinitive, pronouns can either precede the conjugated verb or attach to the infinitive."
            },
            {
                "id": "d37-ex4",
                "type": "translation",
                "prompt": "Translate: 'Could you bring me a glass of water, please?'",
                "options": ["¿Podría traerme un vaso de agua, por favor?", "¿Puede traigo un vaso de agua por favor?", "¿Quisiera traer un vaso de agua por favor?", "¿Tiene que traerme agua por favor?"],
                "correct": 0,
                "explanation": "'¿Podría traerme un vaso de agua, por favor?' is the most courteous phrasing."
            }
        ],
        "speakingChallenge": [
            {"prompt": "Order a coffee and croissant politely using 'Quisiera...'", "hint": "Buenos días, quisiera...", "sampleAnswer": "Buenos días, quisiera un café con leche y un cruasán, por favor."},
            {"prompt": "Ask someone on the street if they could help you using '¿Podría...?'", "hint": "Disculpe, ¿podría ayudarme...?", "sampleAnswer": "Disculpe, señor, ¿podría ayudarme a encontrar esta dirección?"},
            {"prompt": "Say: 'Excuse me, I need to pass through.'", "hint": "Con permiso, tengo que...", "sampleAnswer": "Con permiso, por favor, tengo que bajar en esta estación."}
        ],
        "dailyRevision": {
            "quickQuestions": [
                "Why must the second verb in a modal sentence remain in the infinitive?",
                "What is the polite conditional equivalent of 'quiero'?"
            ],
            "grammarRecall": "Modal formula: [Modal conjugado] + [Infinitivo]. Polite forms: Quisiera [infinitivo], ¿Podría [infinitivo]?. Con permiso.",
            "vocabRecall": ["Quisiera", "¿Podría?", "Poder", "Querer", "Reservar", "Ayudar", "Con permiso", "Posible"]
        },
        "checklist": [
            "Combined modal verbs with infinitives without double-conjugating",
            "Used 'quisiera' for polite ordering in restaurants and hotels",
            "Used '¿podría...?' for formal courteous inquiries",
            "Attached object pronouns to the end of infinitives (ayudarme)",
            "Completed all 4 modal exercises",
            "Practiced polite hotel booking dialogue out loud"
        ]
    },
    {
        "day": 38,
        "stage": 4,
        "title": "Obligation: TENER QUE vs. HAY QUE",
        "subtitle": "Personal obligation (Tengo que estudiar) vs. General duty (Hay que reciclar)",
        "goals": [
            "Express personal obligation using 'TENER QUE + Infinitive' (I have to...)",
            "Express impersonal, general necessity using 'HAY QUE + Infinitive' (One must / We need to...)",
            "Conjugate TENER QUE across all subjects (*tienes que descansar, tenemos que salir*)",
            "Talk about duties, responsibilities, and healthy life habits"
        ],
        "bengaliNote": "Expressing obligation is essential! In Bangla, we differentiate between personal duty (*আমাকে পড়তে হবে* = *Tengo que estudiar*) and universal rules (*নিয়ম মানতে হয়* = *Hay que respetar las reglas*). In Spanish: **Tener que** has a specific person attached; **Hay que** is impersonal and applies to everyone!",
        "vocabulary": [
            {"word": "Tener que (+ infinitivo)", "translation": "To have to (personal obligation)", "pos": "grammar structure", "gender": None, "example": "Tengo que estudiar para el examen.", "exampleTranslation": "I have to study for the exam."},
            {"word": "Hay que (+ infinitivo)", "translation": "One must / It is necessary to (impersonal duty)", "pos": "grammar structure", "gender": None, "example": "Hay que beber dos litros de agua al día.", "exampleTranslation": "One must drink two liters of water a day."},
            {"word": "El deber / Los deberes", "translation": "Duty / Homework, chores", "pos": "noun", "gender": "masculine", "example": "Hago los deberes de español.", "exampleTranslation": "I do my Spanish homework."},
            {"word": "La regla / La norma", "translation": "The rule / The norm", "pos": "noun", "gender": "feminine", "example": "Hay que respetar las normas de tráfico.", "exampleTranslation": "One must respect traffic regulations."},
            {"word": "La responsabilidad", "translation": "The responsibility", "pos": "noun", "gender": "feminine", "example": "Es mi responsabilidad personal.", "exampleTranslation": "It is my personal responsibility."},
            {"word": "Limpiar / Ordenar", "translation": "To clean / To tidy up", "pos": "verb", "gender": None, "example": "Tengo que limpiar mi habitación hoy.", "exampleTranslation": "I have to clean my room today."},
            {"word": "Puntual / La puntualidad", "translation": "Punctual / Punctuality", "pos": "adjective / noun", "gender": "mixed", "example": "Hay que ser puntual en el trabajo.", "exampleTranslation": "One must be punctual at work."},
            {"word": "Reciclar", "translation": "To recycle", "pos": "verb", "gender": None, "example": "Hay que reciclar el plástico y el vidrio.", "exampleTranslation": "One must recycle plastic and glass."},
            {"word": "Descansar", "translation": "To rest", "pos": "verb", "gender": None, "example": "Tienes que descansar más, estás agotado.", "exampleTranslation": "You have to rest more, you are exhausted."},
            {"word": "Madrugar", "translation": "To get up very early (dedicated Spanish verb!)", "pos": "verb", "gender": None, "example": "Mañana tengo que madrugar.", "exampleTranslation": "Tomorrow I have to get up at the crack of dawn."}
        ],
        "sentences": [
            {"spanish": "Hoy tengo que estudiar tres horas porque mañana hay examen.", "english": "Today I have to study three hours because tomorrow there is an exam."},
            {"spanish": "Para aprender un idioma, hay que practicar todos los días.", "english": "To learn a language, one must practice every day. (General truth)"},
            {"spanish": "Tienes que comer más fruta y verdura para tener energía.", "english": "You have to eat more fruit and vegetables to have energy."},
            {"spanish": "Hay que ser educado y paciente con todo el mundo.", "english": "One must be polite and patient with everyone."},
            {"spanish": "Nosotros tenemos que levantarnos temprano mañana para viajar.", "english": "We have to get up early tomorrow to travel."},
            {"spanish": "¿Qué tenemos que hacer ahora? —Tenemos que esperar el autobús.", "english": "What do we have to do now? —We have to wait for the bus."}
        ],
        "grammar": {
            "title": "Personal vs. Impersonal Obligation: TENER QUE vs. HAY QUE",
            "explanation": "Mastering the two faces of obligation will allow you to give advice, state rules, and manage your daily responsibilities.",
            "rules": [
                "1. TENER QUE + Infinitivo (Specific Person): Conjugate TENER for the person who must do the action: *Yo tengo que ir*, *Tú tienes que estudiar*, *Él tiene que trabajar*, *Nosotros tenemos que pagar*, *Vosotros tenéis que escuchar*, *Ellos tienen que venir*.",
                "2. HAY QUE + Infinitivo (Universal Rule / No Person): 'Hay que' NEVER changes! It has no subject; it states general rules, life advice, or civic duties: *Hay que estudiar* (One must study / Studying is necessary), *Hay que cruzar con luz verde* (One must cross on the green light).",
                "The Linking 'QUE': Never omit 'que'! Both structures strictly require 'que' before the infinitive verb (*Tengo QUE salir*, *Hay QUE reciclar*)."
            ],
            "structures": [
                "Personal Obligation: [tengo/tienes/tiene/tenemos/tenéis/tienen] + QUE + [Infinitivo]",
                "Impersonal Obligation: HAY QUE + [Infinitivo]",
                "Negative Obligation: No hay que... (One must not...) / No tienes que... (You don't have to...)"
            ],
            "examples": [
                {"spanish": "Tengo que hacer la compra. (Specific: I must)", "english": "I have to do the grocery shopping."},
                {"spanish": "Hay que hacer deporte para estar sano. (General rule)", "english": "One must do sports to be healthy."},
                {"spanish": "No tienes que preocuparte.", "english": "You don't have to worry."},
                {"spanish": "Hay que apagar el móvil en el cine.", "english": "One must turn off the phone in the cinema."}
            ],
            "commonMistakes": [
                {"wrong": "Tengo estudiar (missing 'que')", "right": "Tengo que estudiar", "explanation": "The structure is strictly 'Tener + QUE + infinitive'."},
                {"wrong": "Hay de reciclar", "right": "Hay que reciclar", "explanation": "The impersonal obligation formula is 'Hay QUE', not 'de'."}
            ],
            "proTip": "Spain has an exclusive single verb for waking up super early: **MADRUGAR**! There is even a beloved proverb: *«A quien madruga, Dios le ayuda»* (God helps those who wake up early — the Spanish equivalent of 'The early bird catches the worm')!"
        },
        "conversation": {
            "title": "Studying for the Upcoming Exam",
            "context": "Sakib and his classmate Carlos talk in the library study lounge.",
            "dialogue": [
                {"speaker": "Carlos", "role": "Classmate", "spanish": "Sakib, ¿vienes esta noche a tomar algo?", "english": "Sakib, are you coming tonight to have a drink?"},
                {"speaker": "Sakib", "role": "Student", "spanish": "No puedo, Carlos. Esta noche tengo que estudiar gramática y repasar el vocabulario.", "english": "I cannot, Carlos. Tonight I have to study grammar and review the vocabulary."},
                {"speaker": "Carlos", "role": "Classmate", "spanish": "Es verdad, el examen de la etapa cuatro es pronto. ¿Tienes muchos temas pendientes?", "english": "That's true, the stage four exam is soon. Do you have many pending topics?"},
                {"speaker": "Sakib", "role": "Student", "spanish": "No muchos, pero hay que repasar bien las diferencias entre por y para, y los verbos modales.", "english": "Not many, but one must thoroughly review the differences between por and para, and modal verbs."},
                {"speaker": "Carlos", "role": "Classmate", "spanish": "Tienes toda la razón. Si quieres, mañana estudiamos juntos en la biblioteca.", "english": "You are completely right. If you want, tomorrow we study together in the library."},
                {"speaker": "Sakib", "role": "Student", "spanish": "¡Me parece una idea genial! Además, hay que dormir ocho horas para tener la mente despejada.", "english": "Sounds like a great idea to me! Furthermore, one must sleep eight hours to have a clear mind."}
            ],
            "keyPhrases": [
                {"phrase": "Mente despejada", "explanation": "'Clear / refreshed mind'."},
                {"phrase": "Temas pendientes", "explanation": "'Pending topics / unfinished items'."},
                {"phrase": "Repasar bien", "explanation": "'To review thoroughly'."}
            ]
        },
        "reading": {
            "title": "Los deberes cívicos y la convivencia en Madrid",
            "passage": "Vivir en una gran capital como Madrid requiere ciertas responsabilidades compartidas para que la convivencia sea pacífica y agradable. En la comunidad de vecinos, hay que respetar el descanso nocturno a partir de las diez de la noche. En el transporte público, hay que ceder el asiento a las personas mayores, a las mujeres embarazadas y a quienes tienen movilidad reducida. Para cuidar el medio ambiente, los ciudadanos tienen que separar la basura en los contenedores de reciclaje correspondientes: azul para el papel, amarillo para los envases y verde para el vidrio. Sakib aprende estas normas ciudadanas con agrado y dice: «Para ser un buen vecino, hay que pensar en los demás».",
            "translation": "Living in a great capital like Madrid requires certain shared responsibilities so that coexistence is peaceful and pleasant. In the apartment building community, one must respect night rest from ten at night onwards. On public transport, one must yield the seat to elderly people, pregnant women, and those with reduced mobility. To care for the environment, citizens have to separate garbage into the corresponding recycling bins: blue for paper, yellow for packaging, and green for glass. Sakib learns these civic norms with pleasure and says: 'To be a good neighbor, one must think of others.'",
            "questions": [
                {"question": "¿A quién hay que ceder el asiento en el transporte público?", "options": ["A nadie", "A los mayores, embarazadas y personas con movilidad reducida", "Solo a los niños", "A los turistas"], "answer": 1, "explanation": "To the elderly, pregnant women, and mobility reduced."},
                {"question": "¿De qué color es el contenedor para el papel y cartón?", "options": ["Amarillo", "Verde", "Azul", "Rojo"], "answer": 2, "explanation": "Blue for paper ('azul para el papel')."},
                {"question": "¿Qué dice Sakib que hay que hacer para ser un buen vecino?", "options": ["Comprar regalos caros", "Pensar en los demás", "No hablar nunca", "Pagar el doble"], "answer": 1, "explanation": "Think of others ('hay que pensar en los demás')."}
            ]
        },
        "exercises": [
            {
                "id": "d38-ex1",
                "type": "fill-in",
                "prompt": "Choose TENER QUE or HAY QUE: Hoy yo ______ estudiar para el examen.",
                "options": ["tengo que", "hay que", "tiene que", "tienen que"],
                "correct": 0,
                "explanation": "Specific personal obligation for 'yo' takes 'tengo que'."
            },
            {
                "id": "d38-ex2",
                "type": "fill-in",
                "prompt": "Choose TENER QUE or HAY QUE: Para tener buena salud, ______ hacer deporte.",
                "options": ["hay que", "tengo que", "tienes que", "tenemos que"],
                "correct": 0,
                "explanation": "General universal necessity takes impersonal 'hay que'."
            },
            {
                "id": "d38-ex3",
                "type": "multiple-choice",
                "prompt": "What does the Spanish verb 'madrugar' mean?",
                "options": ["To stay up late", "To get up at the crack of dawn (very early)", "To cook breakfast", "To run fast"],
                "correct": 1,
                "explanation": "'Madrugar' specifically means to wake up / get up very early."
            },
            {
                "id": "d38-ex4",
                "type": "translation",
                "prompt": "Translate: 'We have to leave the house at 8:00 AM.'",
                "options": ["Tenemos que salir de casa a las ocho de la mañana.", "Hay que salir de casa a las ocho de la mañana.", "Tienen que salir de casa a las ocho de la mañana.", "Tengo que salir de casa a las ocho de la mañana."],
                "correct": 0,
                "explanation": "'Tenemos que salir de casa a las ocho de la mañana' conjugates for nosotros."
            }
        ],
        "speakingChallenge": [
            {"prompt": "Say 2 things you HAVE to do today using 'Tengo que...'", "hint": "Hoy tengo que [verbo] y tengo que [verbo]...", "sampleAnswer": "Hoy tengo que repasar mi vocabulario de español y tengo que limpiar mi habitación."},
            {"prompt": "State a general rule for learning Spanish using 'Hay que...'", "hint": "Para aprender español, hay que...", "sampleAnswer": "Para aprender español con éxito, hay que practicar todos los días y no tener miedo de hablar."},
            {"prompt": "Tell a tired friend that they have to rest.", "hint": "Tienes que descansar...", "sampleAnswer": "Amigo, estás muy cansado, tienes que descansar y dormir ocho horas."}
        ],
        "dailyRevision": {
            "quickQuestions": [
                "What is the difference between 'Tengo que estudiar' and 'Hay que estudiar'?",
                "What preposition is required between 'tener' and the infinitive verb? (QUE)"
            ],
            "grammarRecall": "Obligation: TENER QUE + infinitivo (personal) vs. HAY QUE + infinitivo (impersonal/general). Madrugar.",
            "vocabRecall": ["Tener que", "Hay que", "Los deberes", "La regla", "La responsabilidad", "Puntual", "Reciclar", "Madrugar"]
        },
        "checklist": [
            "Conjugated TENER QUE across all persons for personal obligation",
            "Used impersonal HAY QUE for universal rules and health advice",
            "Never omitted the linking 'que' before the infinitive",
            "Learned the dedicated Spanish verb 'madrugar'",
            "Completed all 4 obligation exercises",
            "Formulated personal duties and general rules out loud"
        ]
    },
    {
        "day": 39,
        "stage": 4,
        "title": "Essential Prepositions: POR vs. PARA",
        "subtitle": "The definitive guide to Spanish's most infamous preposition pair",
        "goals": [
            "End the confusion between POR and PARA once and for all with clear mental frameworks",
            "Master PARA: Purpose (in order to), Recipient, Destination, Deadline",
            "Master POR: Cause/Reason (because of), Duration, Means/Transport, Exchange/Price, Through",
            "Apply high-frequency idioms: por favor, por ejemplo, por eso, para siempre"
        ],
        "bengaliNote": "Both 'por' and 'para' are translated as 'for' in English, which causes endless headaches for native English speakers! But in Bangla, the difference is crystal clear: **PARA** = 'জন্য / উদ্দেশ্যে' (purpose, recipient, destination: *তোমার জন্য / শিখার উদ্দেশ্যে*); **POR** = 'কারণে / দিয়ে / মাধ্যমে' (motive, cause, through, by means of: *বৃষ্টির কারণে / ট্রেন দিয়ে / বিনিময়ে*). Your Bengali intuition makes this easy!",
        "vocabulary": [
            {"word": "Para", "translation": "For / In order to (purpose, recipient, destination, deadline)", "pos": "preposition", "gender": None, "example": "Este regalo es para ti.", "exampleTranslation": "This gift is for you (recipient -> para)."},
            {"word": "Por", "translation": "For / By / Through / Because of (cause, duration, exchange)", "pos": "preposition", "gender": None, "example": "Gracias por tu ayuda.", "exampleTranslation": "Thank you for your help (cause/gratitude -> por)."},
            {"word": "Para + infinitivo", "translation": "In order to / So as to", "pos": "grammar structure", "gender": None, "example": "Estudio para aprender.", "exampleTranslation": "I study in order to learn (purpose -> para)."},
            {"word": "Por la mañana / tarde / noche", "translation": "In the morning / afternoon / night (time of day)", "pos": "phrase", "gender": None, "example": "Hago deporte por la mañana.", "exampleTranslation": "I do sports in the morning (time of day -> por)."},
            {"word": "Por ejemplo", "translation": "For example", "pos": "phrase", "gender": None, "example": "Hay muchas frutas, por ejemplo manzanas.", "exampleTranslation": "There are many fruits, for example apples."},
            {"word": "Por fin", "translation": "Finally / At last", "pos": "phrase", "gender": None, "example": "¡Por fin es viernes!", "exampleTranslation": "Finally it is Friday!"},
            {"word": "Por supuesto", "translation": "Of course", "pos": "phrase", "gender": None, "example": "—¿Vienes? —¡Por supuesto!", "exampleTranslation": "—Are you coming? —Of course!"},
            {"word": "Pasear por el parque", "translation": "To stroll through/around the park (motion through space)", "pos": "phrase", "gender": None, "example": "Paseo por las calles de Madrid.", "exampleTranslation": "I stroll through the streets of Madrid (through -> por)."},
            {"word": "Para siempre", "translation": "Forever", "pos": "phrase", "gender": None, "example": "Amigos para siempre.", "exampleTranslation": "Friends forever."},
            {"word": "Para mí", "translation": "In my opinion / For me", "pos": "phrase", "gender": None, "example": "Para mí, el español es fascinante.", "exampleTranslation": "In my opinion, Spanish is fascinating."}
        ],
        "sentences": [
            {"spanish": "Estudio español para conseguir un buen trabajo.", "english": "I study Spanish in order to get a good job. (Purpose -> PARA)"},
            {"spanish": "Muchas gracias por tu paciencia y por tu tiempo.", "english": "Thank you very much for your patience and for your time. (Cause/Gratitude -> POR)"},
            {"spanish": "Este billete de tren es para mañana por la tarde.", "english": "This train ticket is for tomorrow (deadline -> PARA) in the afternoon (time of day -> POR)."},
            {"spanish": "Salgo para Barcelona a las ocho en punto.", "english": "I leave for Barcelona at eight sharp. (Destination -> PARA)"},
            {"spanish": "Paseamos por el centro histórico durante dos horas.", "english": "We strolled through the historic center (through -> POR)."},
            {"spanish": "Compré este libro por quince euros.", "english": "I bought this book for fifteen euros. (Exchange/Price -> POR)"}
        ],
        "grammar": {
            "title": "The Master Decision Tree: When to Use PARA vs. POR",
            "explanation": "Think of **PARA** as an ARROW pointing forward to a goal, destination, or recipient. Think of **POR** as the MOTIVE behind you, the PATH you travel through, or an EXCHANGE.",
            "rules": [
                "PARA (The Forward Arrow ->):",
                "1. Purpose / Goal (In order to): *Estudio para aprender*.",
                "2. Recipient: *Este libro es para Sakib*.",
                "3. Destination: *El tren sale para Sevilla*.",
                "4. Deadline: *La tarea es para el lunes*.",
                "5. Opinion: *Para mí, Madrid es la mejor ciudad*.",
                "POR (The Cause, Route & Exchange <->):",
                "1. Cause / Reason (Because of): *Gracias por el regalo*, *Llegué tarde por el tráfico*.",
                "2. Duration of Time: *Estudié por tres horas*.",
                "3. Movement Through / Along / Around: *Camino por el parque*, *Paso por tu casa*.",
                "4. Means / Communication: *Hablamos por teléfono*, *Envío por correo*.",
                "5. Exchange / Money: *Pagué veinte euros por la cena*."
            ],
            "structures": [
                "PARA: Propósito (para + inf), Destinatario (para ti), Destino (para Madrid), Fecha límite (para el viernes)",
                "POR: Causa (por el tráfico), Medio (por teléfono), Lugar (por el parque), Precio (por 10€)"
            ],
            "examples": [
                {"spanish": "Trabajo para ganar dinero. (Purpose: Para)", "english": "I work in order to earn money."},
                {"spanish": "No puedo salir por la lluvia. (Cause: Por)", "english": "I cannot go out because of the rain."},
                {"spanish": "El regalo es para mi madre. (Recipient: Para)", "english": "The gift is for my mother."},
                {"spanish": "Viajo por tren. (Means: Por)", "english": "I travel by train."}
            ],
            "commonMistakes": [
                {"wrong": "Gracias para la ayuda", "right": "Gracias por la ayuda", "explanation": "Gratitude and reasons strictly take 'por'."},
                {"wrong": "Estudio por aprender español", "right": "Estudio para aprender español", "explanation": "'In order to + verb' is always 'para + infinitive'."}
            ],
            "proTip": "The ultimate test sentence: *«Trabajo PARA ganar dinero, pero hoy no puedo trabajar POR la huelga»* (I work IN ORDER TO earn money, but today I cannot work BECAUSE OF the strike)!"
        },
        "conversation": {
            "title": "Sending a Gift Package to Family",
            "context": "Sakib visits the Correos post office to send Spanish souvenirs to his family.",
            "dialogue": [
                {"speaker": "Empleado", "role": "Postal clerk", "spanish": "¡Buenos días! ¿Qué desea enviar?", "english": "Good morning! What would you like to send?"},
                {"speaker": "Sakib", "role": "Customer", "spanish": "Buenos días. Quisiera enviar este paquete para mi familia en Bangladés.", "english": "Good morning. I would like to send this package for my family in Bangladesh."},
                {"speaker": "Empleado", "role": "Postal clerk", "spanish": "Muy bien. ¿Lo quiere enviar por correo aéreo urgente o por correo estándar?", "english": "Very well. Do you want to send it by urgent airmail or by standard post?"},
                {"speaker": "Sakib", "role": "Customer", "spanish": "Por correo aéreo, por favor. Es para el cumpleaños de mi madre y tiene que llegar para el quince de noviembre.", "english": "By airmail, please. It is for my mother's birthday and it has to arrive by the fifteenth of November."},
                {"speaker": "Empleado", "role": "Postal clerk", "spanish": "Llega seguro en diez días. Son veinticuatro euros por el envío.", "english": "It arrives safely in ten days. That is twenty-four euros for the shipping."},
                {"speaker": "Sakib", "role": "Customer", "spanish": "Aquí tiene. Muchas gracias por su amabilidad.", "english": "Here you go. Thank you very much for your kindness."},
                {"speaker": "Empleado", "role": "Postal clerk", "spanish": "A usted. ¡Que tenga buen día!", "english": "To you. Have a good day!"}
            ],
            "keyPhrases": [
                {"phrase": "Por correo aéreo", "explanation": "'By airmail' (means of transport -> por)."},
                {"phrase": "Para el cumpleaños", "explanation": "'For the birthday' (purpose/event -> para)."},
                {"phrase": "Para el quince de...", "explanation": "'By the 15th of...' (deadline -> para)."}
            ]
        },
        "reading": {
            "title": "El valor del esfuerzo: Estudiar para superarse",
            "passage": "Aprender un idioma no es una tarea fácil; requiere tiempo, paciencia y dedicación constante. Sakib se levanta todos los días temprano por la mañana para repasar sus lecciones. No estudia por obligación, sino por pasión y porque desea comunicarse con el mundo. Para Sakib, cada palabra aprendida es un puente hacia nuevas oportunidades profesionales y personales. Cuando pasea por las avenidas de Madrid por la tarde, escucha las conversaciones de la gente y sonríe: comprende los giros idiomáticos, las preguntas y las bromas. Sabe que todo el esfuerzo realizado es para construir un futuro mejor.",
            "translation": "Learning a language is not an easy task; it requires time, patience, and constant dedication. Sakib gets up every day early in the morning to review his lessons. He does not study out of obligation, but out of passion and because he wishes to communicate with the world. For Sakib, each word learned is a bridge towards new professional and personal opportunities. When he strolls through the avenues of Madrid in the afternoon, he listens to people's conversations and smiles: he understands idiomatic turns, questions, and jokes. He knows that all the effort made is in order to build a better future.",
            "questions": [
                {"question": "¿Por qué estudia Sakib español?", "options": ["Solo por obligación de sus padres", "Por pasión y para comunicarse con el mundo", "Porque no tiene nada más que hacer", "Para comprar ropa"], "answer": 1, "explanation": "Out of passion and to communicate with the world ('por pasión y porque desea...')."},
                {"question": "¿Por dónde pasea Sakib por la tarde?", "options": ["Por el aeropuerto", "Por las avenidas de Madrid", "Por una estación vacía", "Por el bosque"], "answer": 1, "explanation": "Through Madrid's avenues ('por las avenidas de Madrid')."},
                {"question": "¿Para qué es todo el esfuerzo que realiza Sakib?", "options": ["Para ganar dinero rápido", "Para construir un futuro mejor", "Para viajar solo un día", "Para olvidar su idioma"], "answer": 1, "explanation": "In order to build a better future ('para construir un futuro mejor')."}
            ]
        },
        "exercises": [
            {
                "id": "d39-ex1",
                "type": "fill-in",
                "prompt": "Choose POR or PARA: Muchas gracias ______ (for) tu ayuda.",
                "options": ["por", "para", "en", "de"],
                "correct": 0,
                "explanation": "Gratitude and causes take 'por': 'gracias por tu ayuda'."
            },
            {
                "id": "d39-ex2",
                "type": "fill-in",
                "prompt": "Choose POR or PARA: Estudio todos los días ______ (in order to) aprender.",
                "options": ["para", "por", "a", "con"],
                "correct": 0,
                "explanation": "'In order to + verb' takes 'para + infinitivo'."
            },
            {
                "id": "d39-ex3",
                "type": "fill-in",
                "prompt": "Choose POR or PARA: Este regalo es ______ (for/recipient) mi madre.",
                "options": ["para", "por", "de", "en"],
                "correct": 0,
                "explanation": "The recipient of a gift takes 'para'."
            },
            {
                "id": "d39-ex4",
                "type": "translation",
                "prompt": "Translate: 'I stroll through the park in the afternoon.'",
                "options": ["Paseo por el parque por la tarde.", "Paseo para el parque para la tarde.", "Paseo en el parque para la tarde.", "Paseo por el parque para la tarde."],
                "correct": 0,
                "explanation": "Movement through space and times of day both take 'por': 'Paseo por el parque por la tarde'."
            }
        ],
        "speakingChallenge": [
            {"prompt": "Say why you study Spanish using 'Estudio para + infinitivo'.", "hint": "Estudio español para...", "sampleAnswer": "Estudio español para viajar por España y hablar con la gente local."},
            {"prompt": "Thank someone for their help using 'Gracias por...'", "hint": "Muchas gracias por...", "sampleAnswer": "Muchas gracias por tu tiempo, por tu paciencia y por tu ayuda."},
            {"prompt": "State: 'In my opinion, Spanish is beautiful and useful.'", "hint": "Para mí, el español...", "sampleAnswer": "Para mí, el español es un idioma hermoso, rico y muy útil."}
        ],
        "dailyRevision": {
            "quickQuestions": [
                "What is the difference between 'Estudio para aprender' and 'Gracias por ayudar'?",
                "Which preposition is used for deadlines (e.g. for Friday)? (PARA)"
            ],
            "grammarRecall": "PARA: Purpose (para + inf), Recipient, Destination, Deadline, Opinion. POR: Cause/Reason, Duration, Movement through, Means, Price.",
            "vocabRecall": ["Para", "Por", "Para mí", "Por ejemplo", "Por fin", "Por supuesto", "Por la mañana", "Para siempre"]
        },
        "checklist": [
            "Mastered the functional differences between POR and PARA",
            "Used PARA for purpose (in order to), recipient, and deadlines",
            "Used POR for cause (because of), gratitude, through, and price",
            "Applied common idioms (por ejemplo, por fin, por supuesto)",
            "Completed all 4 POR vs. PARA exercises",
            "Distinguished the two prepositions in spoken sentences"
        ]
    },
    {
        "day": 40,
        "stage": 4,
        "title": "Natural Everyday Conversations & Small Talk",
        "subtitle": "Filler words, agreement markers, conversational pauses + Stage 4 Milestone Assessment",
        "goals": [
            "Master authentic Spanish conversation fillers: bueno, pues, o sea, a ver, vale, mira",
            "Express active listening reactions: ¡no me digas!, ¡qué bien!, ¡vaya!, ¡claro!",
            "Handle small talk gracefully (weather, weekend, common interests)",
            "Complete the Stage 4 Milestone Assessment (DAYS 31–40 COMPREHENSIVE TEST)"
        ],
        "bengaliNote": "Native speakers don't talk like robot textbooks! In Bangla, we constantly insert natural conversational fillers (যেমন: 'মানে', 'আসলে', 'আচ্ছা', 'ঠিক আছে'). In Spain, you will hear: **bueno** (well), **pues** (well/so), **o sea** (I mean / in other words), and **vale** (okay)! Using these instantly makes you sound like an insider.",
        "vocabulary": [
            {"word": "Bueno / Pues", "translation": "Well... / Well then... (conversational starters)", "pos": "filler word", "gender": None, "example": "Bueno, pues la verdad es que me gusta.", "exampleTranslation": "Well, the truth is that I like it."},
            {"word": "O sea", "translation": "I mean / In other words / That is to say", "pos": "filler phrase", "gender": None, "example": "No tengo dinero, o sea, no puedo ir.", "exampleTranslation": "I have no money, I mean, I cannot go."},
            {"word": "A ver", "translation": "Let's see / Look here", "pos": "filler phrase", "gender": None, "example": "A ver, déjame pensar un momento.", "exampleTranslation": "Let's see, let me think for a moment."},
            {"word": "¡Vale!", "translation": "Okay! / Alright! / Deal! (Spain's #1 word)", "pos": "interjection", "gender": None, "example": "—¿Quedamos a las ocho? —¡Vale, perfecto!", "exampleTranslation": "—Shall we meet at eight? —Okay, perfect!"},
            {"word": "¡No me digas!", "translation": "You don't say! / Really?! / No way!", "pos": "interjection", "gender": None, "example": "—Aprobé el examen. —¡No me digas! ¡Qué alegría!", "exampleTranslation": "—I passed the exam. —You don't say! What joy!"},
            {"word": "Mira / Oye", "translation": "Look / Hey, listen (capturing attention)", "pos": "verb command", "gender": None, "example": "Oye, ¿sabes qué hora es?", "exampleTranslation": "Hey, do you know what time it is?"},
            {"word": "La verdad es que...", "translation": "The truth is that... / Honestly...", "pos": "phrase", "gender": None, "example": "La verdad es que estoy un poco cansado.", "exampleTranslation": "Honestly, I am a little tired."},
            {"word": "¿Qué tal todo?", "translation": "How is everything going? (casual small talk)", "pos": "phrase", "gender": None, "example": "¡Hola, Sakib! ¿Qué tal todo?", "exampleTranslation": "Hello, Sakib! How is everything going?"},
            {"word": "¡Qué pasada! / ¡Qué guay!", "translation": "How cool! / How awesome! (Spain youth slang)", "pos": "interjection", "gender": None, "example": "¡Qué guay tu camiseta nueva!", "exampleTranslation": "How cool is your new T-shirt!"},
            {"word": "En fin", "translation": "Anyway / All in all (wrapping up a conversation)", "pos": "phrase", "gender": None, "example": "En fin, me tengo que ir ya.", "exampleTranslation": "Anyway, I have to go now."}
        ],
        "sentences": [
            {"spanish": "Bueno, la verdad es que hoy hace un día fantástico.", "english": "Well, honestly today is a fantastic day."},
            {"spanish": "¿Quedamos a las siete en Sol? —¡Vale, me parece perfecto!", "english": "Shall we meet at seven in Sol? —Okay, sounds perfect to me!"},
            {"spanish": "—Ayer visité el Palacio Real. —¡Qué pasada! ¿Te gustó?", "english": "—Yesterday I visited the Royal Palace. —How cool! Did you like it?"},
            {"spanish": "O sea, si no estudiamos hoy, mañana va a ser más difícil.", "english": "I mean, if we don't study today, tomorrow will be harder."},
            {"spanish": "Oye, ¿tienes planes para este fin de semana?", "english": "Hey, do you have plans for this weekend?"},
            {"spanish": "En fin, no te quito más tiempo, nos vemos mañana.", "english": "Anyway, I won't take up more of your time, see you tomorrow."}
        ],
        "grammar": {
            "title": "Conversational Fillers (Muletillas) & Spanish Active Listening Reactions",
            "explanation": "In linguistics, filler words are called **muletillas** (little crutches). They buy your brain processing time to formulate thoughts without awkward silence!",
            "rules": [
                "Buying Thinking Time: Instead of saying 'Uhhhh...', Spanish speakers say: *Bueno...*, *Pues...*, *A ver...*, *Es que...*.",
                "Reactions of Surprise & Joy: *¡No me digas!* (You don't say!), *¡Qué bien!* (How great!), *¡Vaya!* (Wow!), *¡Madre mía!* (My goodness!).",
                "Reactions of Sympathy: *¡Qué pena!* (What a pity!), *¡Vaya por Dios!* (Oh dear!), *¡Lo siento mucho!* (I'm so sorry).",
                "Polite Exit Formulas: To wrap up a chat naturally, use: *Bueno, pues me tengo que ir* (Well, I've got to head out) or *En fin, no te entretengo más* (Anyway, I won't hold you up any longer)."
            ],
            "structures": [
                "Filler Starter: Bueno, pues + [pensamiento]",
                "Clarifier: O sea, + [explicación]",
                "Exit Formula: En fin, me tengo que ir + [despedida]"
            ],
            "examples": [
                {"spanish": "A ver qué hacemos este fin de semana.", "english": "Let's see what we do this weekend."},
                {"spanish": "—He perdido las llaves. —¡No me digas! ¿Dónde?", "english": "—I lost the keys. —No way! Where?"},
                {"spanish": "Es que hoy no tengo mucho tiempo. ('Es que' softens excuses)", "english": "It's just that today I don't have much time."},
                {"spanish": "¡Vale, nos vemos el lunes!", "english": "Alright, see you Monday!"}
            ],
            "commonMistakes": [
                {"wrong": "Saying 'Uhhhh' silently or freezing", "right": "Say 'Bueno...', 'A ver...', 'Pues...'", "explanation": "Using Spanish fillers keeps the conversational channel open."},
                {"wrong": "Using 'Okay' exclusively in Spain", "right": "Say '¡Vale!'", "explanation": "'Vale' is universally loved in Spain for agreement."}
            ],
            "proTip": "The magic excuse softener is **«Es que...»** (It's just that...). Whenever you need to politely decline an invitation: *«Me encantaría ir, es que tengo que estudiar»* (I'd love to go, it's just that I have to study). It sounds 100% natural!"
        },
        "conversation": {
            "title": "Casual Coffee Chat with Classmates",
            "context": "Sakib chats casually with Laura and Mateo at a sidewalk terrace.",
            "dialogue": [
                {"speaker": "Mateo", "role": "Friend", "spanish": "¡Hombre, Sakib! ¿Qué tal todo?", "english": "Hey man, Sakib! How is everything?"},
                {"speaker": "Sakib", "role": "Student", "spanish": "¡Hola, Mateo! Pues muy bien, la verdad. Aquí tomando un café al sol.", "english": "Hello, Mateo! Well very good, honestly. Here having a coffee in the sun."},
                {"speaker": "Laura", "role": "Friend", "spanish": "Oye, ¿sabéis que ya llevamos cuarenta días de curso?", "english": "Hey, do you guys know that we've already done forty days of the course?"},
                {"speaker": "Mateo", "role": "Friend", "spanish": "¡No me digas! ¿En serio? ¡Qué pasada! El tiempo vuela.", "english": "No way! Seriously? How cool! Time flies."},
                {"speaker": "Sakib", "role": "Student", "spanish": "A ver, es verdad: hemos aprendido restaurantes, viajes, descripciones y preposiciones. O sea, ya podemos sobrevivir en cualquier ciudad de España.", "english": "Let's see, it's true: we have learned restaurants, travel, descriptions, and prepositions. I mean, we can already survive in any Spanish city."},
                {"speaker": "Laura", "role": "Friend", "spanish": "¿Celebramos el día cuarenta con unas tapas esta noche?", "english": "Shall we celebrate day forty with some tapas tonight?"},
                {"speaker": "Sakib", "role": "Student", "spanish": "¡Vale, perfecto! Quedamos en Sol a las ocho y media, ¿os parece?", "english": "Alright, perfect! We meet in Sol at eight thirty, what do you all think?"},
                {"speaker": "Mateo", "role": "Friend", "spanish": "¡Hecho! Bueno, me voy a clase. ¡Hasta luego!", "english": "Done! Well, I'm heading to class. See you later!"}
            ],
            "keyPhrases": [
                {"phrase": "¡Hombre!", "explanation": "Friendly colloquial greeting: 'Hey man!' (used with both men and women)."},
                {"phrase": "¿En serio?", "explanation": "'Seriously?!'"},
                {"phrase": "El tiempo vuela", "explanation": "'Time flies'."}
            ]
        },
        "reading": {
            "title": "Stage 4 Capstone Story: Cuarenta días — La soltura comunicativa de Sakib",
            "passage": "El día cuarenta marca un hito extraordinario en el aprendizaje de Sakib. Ya no traduce mentalmente desde el bengalí o el inglés; ahora piensa y reacciona de manera espontánea en español. En estos últimos diez días ha conquistado situaciones prácticas esenciales de la vida real: sabe desenvolverse en restaurantes tradicionales pidiendo el menú del día, comprar billetes de tren de alta velocidad en las estaciones, describir el tiempo y la temperatura con precisión, retratar a las personas combinando ser, tener y llevar, y diferenciar por y para con claridad. Pero lo más valioso es su naturalidad: utiliza muletillas como «bueno», «o sea» y «vale» con la cadencia auténtica de un madrileño. Con dos tercios del desafío completados, Sakib entra en la recta final hacia el dominio sólido del nivel A1.",
            "translation": "Day forty marks an extraordinary milestone in Sakib's learning. He no longer mentally translates from Bengali or English; now he thinks and reacts spontaneously in Spanish. In these last ten days he has conquered essential real-world practical situations: he knows how to manage in traditional restaurants ordering the set menu, buy high-speed train tickets at stations, describe weather and temperature with precision, portray people combining ser, tener, and llevar, and differentiate por and para with clarity. But most valuable is his naturalness: he uses fillers like 'bueno', 'o sea', and 'vale' with the authentic cadence of a local of Madrid. With two thirds of the challenge completed, Sakib enters the home stretch toward solid mastery of level A1.",
            "questions": [
                {"question": "¿Qué hito marca el día cuarenta en el aprendizaje de Sakib?", "options": ["Que ha suspendido el curso", "Ya no traduce mentalmente; piensa y reacciona espontáneamente en español", "Solo sabe saludar", "Quiere cambiar de idioma"], "answer": 1, "explanation": "No longer translates mentally; thinks and reacts spontaneously."},
                {"question": "¿Qué parte del desafío de sesenta días está completada hoy?", "options": ["Un tercio", "La mitad", "Dos tercios del desafío", "El cien por cien"], "answer": 2, "explanation": "Two thirds of the challenge ('dos tercios del desafío')."},
                {"question": "¿Qué muletillas utiliza Sakib con naturalidad?", "options": ["Solo palabras en inglés", "Bueno, o sea y vale", "Ninguna palabra", "Solo silencio"], "answer": 1, "explanation": "Bueno, o sea, and vale ('utiliza muletillas como bueno, o sea y vale')."}
            ]
        },
        "exercises": [
            {
                "id": "d40-ex1",
                "type": "multiple-choice",
                "prompt": "Which filler word means 'I mean / in other words' in Spanish?",
                "options": ["O sea", "A ver", "Vale", "Pues"],
                "correct": 0,
                "explanation": "'O sea' means 'I mean / in other words'."
            },
            {
                "id": "d40-ex2",
                "type": "multiple-choice",
                "prompt": "How do Spaniards most naturally express 'Okay! / Agreed!'?",
                "options": ["¡Vale!", "¡Bien!", "¡Seguro!", "¡Sí señor!"],
                "correct": 0,
                "explanation": "'¡Vale!' is the quintessential Spanish agreement word."
            },
            {
                "id": "d40-ex3",
                "type": "fill-in",
                "prompt": "Complete the natural reaction of surprise: —¡Aprobé todo! —¡No me ______ (say)! ¡Felicidades!",
                "options": ["digas", "dices", "diga", "decir"],
                "correct": 0,
                "explanation": "'¡No me digas!' is the classic idiom for 'You don't say / No way!'."
            },
            {
                "id": "d40-ex4",
                "type": "translation",
                "prompt": "Translate: 'Well, honestly I have to go now.'",
                "options": ["Bueno, la verdad es que me tengo que ir ya.", "Pues, la verdad está que voy ahora.", "O sea, la verdad tengo que salir.", "A ver, la verdad es me voy."],
                "correct": 0,
                "explanation": "'Bueno, la verdad es que me tengo que ir ya' strings authentic fillers and exit formulas perfectly."
            }
        ],
        "speakingChallenge": [
            {"prompt": "React with enthusiastic surprise to good news using '¡No me digas!' and '¡Qué bien!'.", "hint": "¡No me digas! ¡Qué alegría!", "sampleAnswer": "¡No me digas! ¿En serio? ¡Qué bien, me alegro muchísimo por ti!"},
            {"prompt": "Politely excuse yourself from a chat using 'Es que...' and 'En fin...'", "hint": "Es que tengo que... en fin...", "sampleAnswer": "Me encantaría quedarme, es que tengo que estudiar para mañana. En fin, nos vemos pronto."},
            {"prompt": "Celebrate reaching Day 40 out loud: two thirds of the journey complete!", "hint": "¡Ya son cuarenta días! Dos tercios...", "sampleAnswer": "¡Ya he completado cuarenta días de mi desafío! Dos tercios del camino hacia A1 están superados."}
        ],
        "dailyRevision": {
            "quickQuestions": [
                "What is a 'muletilla' in Spanish?",
                "What does '¡No me digas!' express?"
            ],
            "grammarRecall": "Fillers: bueno, pues, o sea, a ver, vale. Reactions: ¡No me digas!, ¡Qué bien!, ¡Vaya! Softeners: Es que...",
            "vocabRecall": ["Bueno", "Pues", "O sea", "A ver", "¡Vale!", "¡No me digas!", "La verdad es que", "En fin", "¿Qué tal todo?"]
        },
        "checklist": [
            "Incorporated natural Spanish filler words (bueno, pues, o sea, a ver, vale)",
            "Used active listening reactions (¡no me digas!, ¡qué pasada!)",
            "Used 'Es que...' to soften polite excuses naturally",
            "Completed the Stage 4 Milestone Assessment Reading Passage",
            "Passed all 4 conversation exercises",
            "CELEBRATED COMPLETING STAGE 4 (DAYS 31–40) — TWO THIRDS OF THE 60-DAY CHALLENGE! 🎉🇪🇸"
        ]
    }
]

# Combine both parts
stage4_complete = stage4_days + stage4_part2

with open("d:/ag/espanol-handbook/data/lessons/stage4.js", "w", encoding="utf-8") as f:
    f.write("// Stage 4: Days 31 to 40 (Practical Communication)\n")
    f.write("window.STAGE_4_LESSONS = ")
    json.dump(stage4_complete, f, ensure_ascii=False, indent=2)
    f.write(";\n")

print(f"Successfully generated stage4.js with all {len(stage4_complete)} full days!")
