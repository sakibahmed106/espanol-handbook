"""
Stage 6: Days 51-55 Builder
"""
import json

stage6_days_51_55 = [
    {
        "day": 51,
        "stage": 6,
        "title": "Essential Idioms & Colloquial Expressions in Spain",
        "subtitle": "Speaking Like a True Native: Spanish Modismos and Coloquialismos",
        "goals": [
            "Master 10 essential Spain Spanish idioms used daily in casual conversation",
            "Understand the figurative meaning vs literal translation of modismos",
            "Use colloquial phrases naturally in social situations without sounding stiff",
            "Recognize Spain-specific idioms like 'estar como una cabra' and 'ser pan comido'"
        ],
        "bengaliNote": "বাংলায় যেমন আমরা বলি 'ডালভাত' (খুব সহজ) বা 'মাথা খারাপ' (উন্মাদ), স্প্যানিশেও হুবহু একই রকম রূপক প্রবাদ বা 'modismos' রয়েছে! যেমন 'ser pan comido' (literally: chewed bread) মানে বাংলা 'ডালভাত' বা English 'a piece of cake'। এগুলো মুখস্থ করলে আপনার স্প্যানিশ শুনতেই একদম নেটিভদের মতো লাগবে!",
        "vocabulary": [
            {"word": "Ser pan comido", "translation": "To be a piece of cake / extremely easy", "pos": "idiom", "gender": None, "example": "El examen de A1 va a ser pan comido para ti.", "exampleTranslation": "The A1 exam is going to be a piece of cake for you."},
            {"word": "Estar como una cabra", "translation": "To be completely crazy / wacky", "pos": "idiom", "gender": None, "example": "Mi tío siempre cuenta chistes raros, está como una cabra.", "exampleTranslation": "My uncle always tells weird jokes, he is completely crazy."},
            {"word": "Costar un ojo de la cara", "translation": "To cost an arm and a leg / very expensive", "pos": "idiom", "gender": None, "example": "Ese coche deportivo cuesta un ojo de la cara.", "exampleTranslation": "That sports car costs an arm and a leg."},
            {"word": "Tomar el pelo (a alguien)", "translation": "To pull someone's leg / tease someone", "pos": "idiom", "gender": None, "example": "¿Dices que viste a Messi en el metro? ¡Me estás tomando el pelo!", "exampleTranslation": "You say you saw Messi on the subway? You are pulling my leg!"},
            {"word": "Meter la pata", "translation": "To put one's foot in one's mouth / mess up", "pos": "idiom", "gender": None, "example": "Hablé de la fiesta sorpresa y metí la pata.", "exampleTranslation": "I spoke about the surprise party and put my foot in my mouth."},
            {"word": "Tirar la casa por la ventana", "translation": "To spare no expense / throw a lavish party", "pos": "idiom", "gender": None, "example": "Para su boda van a tirar la casa por la ventana.", "exampleTranslation": "For their wedding they are going to spare no expense."},
            {"word": "Estar en las nubes", "translation": "To be daydreaming / head in the clouds", "pos": "idiom", "gender": None, "example": "Sakib no escucha la pregunta porque está en las nubes.", "exampleTranslation": "Sakib doesn't hear the question because he is daydreaming."},
            {"word": "Ponerse las pilas", "translation": "To get one's act together / get moving / energize", "pos": "idiom", "gender": None, "example": "Quedan diez días de curso, hay que ponerse las pilas.", "exampleTranslation": "There are ten days of the course left, we must get our act together."},
            {"word": "Estar hasta las narices", "translation": "To be fed up to one's back teeth", "pos": "idiom", "gender": None, "example": "Estoy hasta las narices de este tráfico horrible.", "exampleTranslation": "I am fed up to my back teeth with this horrible traffic."},
            {"word": "Ser uña y carne", "translation": "To be two peas in a pod / inseparable friends", "pos": "idiom", "gender": None, "example": "Elena y Lucía son uña y carne desde la infancia.", "exampleTranslation": "Elena and Lucía are inseparable friends since childhood."}
        ],
        "sentences": [
            {"spanish": "No te preocupes por la prueba de gramática, es pan comido.", "english": "Don't worry about the grammar test, it's a piece of cake."},
            {"spanish": "¿Me estás tomando el pelo o me estás diciendo la verdad?", "english": "Are you pulling my leg or are you telling me the truth?"},
            {"spanish": "Ese piso en el centro de Madrid cuesta un ojo de la cara.", "english": "That apartment in downtown Madrid costs an arm and a leg."},
            {"spanish": "Lo siento mucho, hablé sin pensar y metí la pata hasta el fondo.", "english": "I'm very sorry, I spoke without thinking and totally messed up."},
            {"spanish": "¡Vamos, chicos, hay que ponerse las pilas para terminar a tiempo!", "english": "Come on, guys, we need to get our act together to finish on time!"},
            {"spanish": "Mi hermano y yo somos uña y carne; siempre viajamos juntos.", "english": "My brother and I are inseparable; we always travel together."}
        ],
        "grammar": {
            "title": "Spanish Idioms (Modismos): Structure, Agreement, and Pragmatic Usage",
            "explanation": "Idioms are fixed phrases where the collective meaning differs from individual literal words. In Spanish, idioms revolve around verbs (ser, estar, tener, meter, tomar, costar) and body parts (ojo, cara, pelo, narices, pata).",
            "rules": [
                "Verb Conjugation Rule: The verb inside the idiom conjugates to match the subject (*yo metí la pata, tú metiste la pata*), while the noun portion remains fixed (*la pata* never changes to plural).",
                "Ser vs Estar Distinction: *Ser pan comido* (inherent ease), *Estar como una cabra* (temporary state or behavioral quirk), *Estar en las nubes* (state of mind).",
                "Indirect Object with 'Tomar el pelo': Requires indirect object pronoun for the person being teased (*me tomas el pelo*, *le tomo el pelo*).",
                "Tone and Register: While colloquial, these idioms are universally accepted across Spain in everyday workplace chats, family dinners, and social gatherings."
            ],
            "structures": [
                "Conjugated Verb + Fixed Idiomatic Nominal Phrase: [Sujeto] + [Verbo conjugado] + [frase hecha]",
                "Encouragement Formula: '¡Hay que' / 'Tienes que' + [Infinitivo idiomático]"
            ],
            "examples": [
                {"spanish": "Ayer metí la pata en la oficina con el jefe.", "english": "Yesterday I put my foot in my mouth at the office with the boss.", "breakdown": "metí (preterite 1st person) + la pata (fixed noun phrase)"},
                {"spanish": "El billete de avión a Tokio cuesta un ojo de la cara.", "english": "The plane ticket to Tokyo costs an eye from the face (an arm and a leg).", "breakdown": "cuesta (present 3rd person) + un ojo de la cara"},
                {"spanish": "¿Por qué estás en las nubes hoy?", "english": "Why are you in the clouds today (daydreaming)?", "breakdown": "estás (estar present 2nd person) + en las nubes"},
                {"spanish": "¡Ponte las pilas si quieres aprobar!", "english": "Put your batteries on (get your act together) if you want to pass!", "breakdown": "Ponte (imperative reflexive) + las pilas"}
            ],
            "commonMistakes": [
                {"incorrect": "El examen está pan comido.", "correct": "El examen es pan comido.", "why": "Inherent simplicity takes 'ser', never 'estar'."},
                {"incorrect": "Ellos metieron las patas.", "correct": "Ellos metieron la pata.", "why": "The noun 'la pata' in this idiom remains strictly singular."}
            ],
            "proTip": "When using idioms in Spain, Spaniards will be delighted and often exclaim '¡Hablas español por los codos!' (You talk Spanish up to your elbows / like a true native)!"
        },
        "conversation": {
            "context": "Sakib and his Spanish friend Carlos are studying in a cafe in Madrid before the final review.",
            "dialogue": [
                {"speaker": "Carlos", "role": "Friend", "spanish": "¡Hola, Sakib! ¿Cómo llevas el repaso para la semana final?", "english": "Hi, Sakib! How is the review going for the final week?"},
                {"speaker": "Sakib", "role": "Student", "spanish": "Al principio pensé que el pretérito era difícil, pero ahora veo que es pan comido.", "english": "At first I thought the preterite was difficult, but now I see that it's a piece of cake."},
                {"speaker": "Carlos", "role": "Friend", "spanish": "¡Olé! Te veo con mucha seguridad. Pero no te quedes en las nubes, todavía hay que repasar vocabulario.", "english": "Bravo! I see you with great confidence. But don't daydream, we still need to review vocabulary."},
                {"speaker": "Sakib", "role": "Student", "spanish": "Tienes razón, Carlos. Hay que ponerse las pilas hasta el último minuto.", "english": "You're right, Carlos. We must get our act together until the last minute."},
                {"speaker": "Carlos", "role": "Friend", "spanish": "¿Y qué planes tienes para después del examen del Día 60?", "english": "And what plans do you have for after the Day 60 exam?"},
                {"speaker": "Sakib", "role": "Student", "spanish": "¡Voy a tirar la casa por la ventana y cenar una paella enorme en la Plaza Mayor!", "english": "I'm going to spare no expense and have a huge paella dinner in Plaza Mayor!"},
                {"speaker": "Carlos", "role": "Friend", "spanish": "¡Ja, ja! Pero cuidado, que cenar en la Plaza Mayor cuesta un ojo de la cara.", "english": "Ha, ha! But be careful, dining in Plaza Mayor costs an arm and a leg."},
                {"speaker": "Sakib", "role": "Student", "spanish": "¿En serio o me estás tomando el pelo?", "english": "Really or are you pulling my leg?"},
                {"speaker": "Carlos", "role": "Friend", "spanish": "Medio en serio. ¡Pero te lo mereces después de sesenta días de esfuerzo!", "english": "Half serious. But you deserve it after sixty days of effort!"}
            ],
            "keyPhrases": [
                {"phrase": "Es pan comido", "explanation": "'It's a piece of cake / super easy'."},
                {"phrase": "Tirar la casa por la ventana", "explanation": "'To celebrate lavishly / spare no expense'."},
                {"phrase": "Ponerse las pilas", "explanation": "'To step up / get energized / get one's act together'."}
            ]
        },
        "reading": {
            "title": "El encanto de las expresiones españolas",
            "passage": "Aprender una lengua extranjera no consiste únicamente en memorizar listas de palabras y reglas de conjugación gramatical. La verdadera magia del idioma surge cuando el estudiante descubre los modismos populares. En España, las personas recurren a menudo a metáforas curiosas relacionadas con animales, partes del cuerpo y comida para colorear sus conversaciones diarias. Si alguien dice que una tarea es 'pan comido', expresa que resulta sumamente accesible. Si alguien afirma que un billete de tren 'cuesta un ojo de la cara', todos comprenden inmediatamente que el precio es desorbitado. Estas frases no deben traducirse literalmente palabra por palabra, sino interpretarse con su sentido cultural. Cuando un extranjero utiliza con soltura expresiones como 'ponerse las pilas' o 'no me tomes el pelo', los nativos reconocen un dominio comunicativo genuino y cercano.",
            "translation": "Learning a foreign language is not solely about memorizing word lists and grammatical conjugation rules. The true magic of the language emerges when the student discovers popular idioms. In Spain, people frequently turn to curious metaphors related to animals, body parts, and food to color their daily conversations. If someone says that a task is 'pan comido', they express that it is extremely accessible. If someone asserts that a train ticket 'cuesta un ojo de la cara', everyone immediately understands that the price is exorbitant. These phrases must not be translated literally word by word, but interpreted with their cultural sense. When a foreigner uses expressions like 'ponerse las pilas' or 'no me tomes el pelo' with fluency, native speakers recognize genuine and approachable communicative mastery.",
            "questions": [
                {"question": "¿Cuándo surge la verdadera magia de un idioma según el texto?", "options": ["Solo al memorizar el alfabeto", "Cuando se descubren los modismos populares", "Al leer el diccionario de la A a la Z", "Al comprar ropa en Madrid"], "answer": 1, "explanation": "The text states: 'La verdadera magia del idioma surge cuando el estudiante descubre los modismos populares'."},
                {"question": "¿Por qué no se deben traducir los modismos palabra por palabra?", "options": ["Porque están prohibidos", "Porque su significado cultural es figurativo", "Porque no tienen verbos", "Porque son demasiado antiguos"], "answer": 1, "explanation": "They are figurative metaphors that carry cultural meaning rather than word-for-word literalism."},
                {"question": "¿Qué experimentan los nativos cuando un estudiante usa estas frases?", "options": ["Enfado", "Reconocen un dominio comunicativo genuino y cercano", "Confusión total", "Ignoran al estudiante"], "answer": 1, "explanation": "Native speakers appreciate genuine communicative mastery ('dominio comunicativo genuino y cercano')."}
            ]
        },
        "exercises": [
            {
                "id": "d51-ex1",
                "type": "matching",
                "question": "Relaciona cada modismo con su significado exacto:",
                "options": [
                    "Ser pan comido -> Ser extremadamente fácil",
                    "Costar un ojo de la cara -> Ser carísimo",
                    "Ponerse las pilas -> Poner energía y diligencia",
                    "Meter la pata -> Cometer una indiscreción o equivocación"
                ],
                "correct": 0,
                "explanation": "Cada modismo español corresponde exactamente a un concepto figurativo cotidiano."
            },
            {
                "id": "d51-ex2",
                "type": "multiple-choice",
                "question": "¿Cuál es la frase correcta para decir que alguien te está bromeando o engañando con humor?",
                "options": ["Me estás tomando el pelo", "Me estás comiendo el pan", "Me estás poniendo las pilas", "Me estás costando la cara"],
                "correct": 0,
                "explanation": "'Tomar el pelo a alguien' significa bromear o 'pull someone's leg'."
            },
            {
                "id": "d51-ex3",
                "type": "sentence-ordering",
                "question": "Ordena las palabras para formar una frase idiomática perfecta:",
                "options": ["El", "examen", "final", "es", "pan", "comido"],
                "correct": [0, 1, 2, 3, 4, 5],
                "explanation": "'El examen final es pan comido' significa 'The final exam is a piece of cake'."
            },
            {
                "id": "d51-ex4",
                "type": "fill-in-the-blank",
                "question": "Completa: 'Tenemos que terminar el proyecto hoy, así que ¡hay que ponerse las _____!'",
                "options": ["pilas", "manos", "patas", "caras"],
                "correct": 0,
                "explanation": "'Ponerse las pilas' es la expresión castiza para espabilarse o ponerse a trabajar con energía."
            }
        ],
        "speakingChallenge": {
            "title": "Reto Oral: Modismos en Acción",
            "instructions": "Responde en voz alta utilizando al menos un modismo español aprendido hoy.",
            "prompts": [
                {
                    "question": "¿Qué opinas del nivel A1 de español después de cincuenta días de estudio? ¿Es pan comido o difícil?",
                    "hint": "Usa: 'Para mí, el español no es pan comido, pero con esfuerzo...'",
                    "sampleAnswer": "Para mí, el español no siempre es pan comido, pero cuando me pongo las pilas, todo resulta mucho más fácil y divertido."
                },
                {
                    "question": "¿Qué cosas en tu ciudad cuestan un ojo de la cara?",
                    "hint": "Usa: 'En mi ciudad, comprar un piso / coche cuesta un ojo de la cara...'",
                    "sampleAnswer": "En mi ciudad, alquilar un apartamento en el centro cuesta un ojo de la cara, es demasiado caro."
                },
                {
                    "question": "¿Has metido la pata alguna vez hablando en español o en otro idioma?",
                    "hint": "Usa: 'Sí, una vez metí la pata cuando dije...'",
                    "sampleAnswer": "Sí, una vez metí la pata cuando dije 'estoy constipado' pensando que significaba otra cosa, ¡pero nos reímos mucho!"
                }
            ]
        },
        "dailyRevision": {
            "quickQuestions": [
                {"q": "¿Qué significa 'tomar el pelo'?", "a": "Burlar o bromear amistosamente con alguien (pull someone's leg)."},
                {"q": "¿Qué verbo acompaña a 'pan comido'?", "a": "El verbo 'ser' (es pan comido)."},
                {"q": "¿Qué significa 'estar como una cabra'?", "a": "Estar loco o actuar de forma muy extravagante."}
            ],
            "vocabRecall": [
                {"en": "To spare no expense", "es": "Tirar la casa por la ventana"},
                {"en": "To get one's act together", "es": "Ponerse las pilas"},
                {"en": "To cost an arm and a leg", "es": "Costar un ojo de la cara"}
            ],
            "grammarRecall": "Recuerda que en los modismos el verbo se conjuga con la persona, pero el sustantivo se mantiene inmutable: 'Metí la pata', 'Metiste la pata'."
        },
        "checklist": [
            "Aprendí 10 modismos y expresiones coloquiales españolas",
            "Entendí la diferencia entre sentido literal y figurativo",
            "Practiqué la conjugación correcta en modismos verbales",
            "Comprendí el diálogo de Sakib y Carlos en la cafetería",
            "Respondí el reto oral con pronunciación fluida",
            "Completé los ejercicios de modismos con éxito"
        ]
    },
    {
        "day": 52,
        "stage": 6,
        "title": "Expressing Opinions, Agreement, and Friendly Debate",
        "subtitle": "How to Agree, Disagree, Debate, and Share Your Worldview in Spanish",
        "goals": [
            "Express personal viewpoints with clarity using 'Creo que', 'En mi opinión', 'Me parece'",
            "Express complete agreement, partial agreement, and polite disagreement",
            "Structure logical arguments using transition connectors ('Por un lado', 'Por otro lado', 'Sin embargo')",
            "Participate in beginner-level discussion on everyday topics (travel, technology, culture)"
        ],
        "bengaliNote": "মত প্রকাশ করা যেকোনো ভাষার প্রাণ! বাংলায় আমরা যেমন বলি 'আমার মতে' বা 'আমি একমত', স্প্যানিশে 'En mi opinión' ও 'Estoy de acuerdo' হলো সর্বপ্রধান টুল। A1 লেভেলে কোনো তর্ক বা মতামত প্রকাশ করার সময় 'Creo que...' (আমার মনে হয় যে) ব্যবহার করে বাক্য শুরু করবেন।",
        "vocabulary": [
            {"word": "En mi opinión / A mi parecer", "translation": "In my opinion / To my mind", "pos": "phrase", "gender": None, "example": "En mi opinión, viajar en tren es mucho más cómodo.", "exampleTranslation": "In my opinion, traveling by train is much more comfortable."},
            {"word": "Creo que... / Pienso que...", "translation": "I believe that... / I think that...", "pos": "phrase", "gender": None, "example": "Creo que aprender español abre muchas puertas.", "exampleTranslation": "I believe that learning Spanish opens many doors."},
            {"word": "Me parece que...", "translation": "It seems to me that...", "pos": "phrase", "gender": None, "example": "Me parece que esta ciudad es muy segura.", "exampleTranslation": "It seems to me that this city is very safe."},
            {"word": "Estar de acuerdo (con)", "translation": "To agree (with)", "pos": "phrase", "gender": None, "example": "Estoy totalmente de acuerdo contigo.", "exampleTranslation": "I totally agree with you."},
            {"word": "No estar de acuerdo / Discrepar", "translation": "To disagree", "pos": "phrase", "gender": None, "example": "No estoy de acuerdo con esa afirmación.", "exampleTranslation": "I don't agree with that statement."},
            {"word": "Tener razón", "translation": "To be right (lit: to have reason)", "pos": "phrase", "gender": None, "example": "Tienes toda la razón, cometí un error.", "exampleTranslation": "You are completely right, I made a mistake."},
            {"word": "Por un lado... por otro lado...", "translation": "On the one hand... on the other hand...", "pos": "connector", "gender": None, "example": "Por un lado me gusta la ciudad, por otro lado prefiero el campo.", "exampleTranslation": "On the one hand I like the city, on the other hand I prefer the countryside."},
            {"word": "Sin embargo / No obstante", "translation": "However / Nevertheless", "pos": "connector", "gender": None, "example": "El examen es largo; sin embargo, no es difícil.", "exampleTranslation": "The exam is long; however, it is not difficult."},
            {"word": "Desde mi punto de vista", "translation": "From my point of view", "pos": "phrase", "gender": None, "example": "Desde mi punto de vista, la práctica diaria es fundamental.", "exampleTranslation": "From my point of view, daily practice is fundamental."},
            {"word": "Depende de...", "translation": "It depends on...", "pos": "phrase", "gender": None, "example": "Todo depende del tiempo libre que tengas.", "exampleTranslation": "Everything depends on the free time you have."}
        ],
        "sentences": [
            {"spanish": "Creo que el español es uno de los idiomas más bonitos del mundo.", "english": "I think that Spanish is one of the most beautiful languages in the world."},
            {"spanish": "En mi opinión, es mejor estudiar treinta minutos cada día que cuatro horas el domingo.", "english": "In my opinion, it is better to study 30 minutes every day than 4 hours on Sunday."},
            {"spanish": "Estoy totalmente de acuerdo con tu planteamiento.", "english": "I totally agree with your approach."},
            {"spanish": "No estoy de acuerdo, me parece que esa solución es muy costosa.", "english": "I don't agree, it seems to me that that solution is very expensive."},
            {"spanish": "Tienes razón en lo que dices, pero hay que considerar otros factores.", "english": "You are right in what you say, but other factors must be considered."},
            {"spanish": "¿Qué opinas tú sobre vivir en el extranjero?", "english": "What is your opinion on living abroad?"}
        ],
        "grammar": {
            "title": "Expressing Opinions & Indicative Complementation in A1",
            "explanation": "In Spanish, stating an opinion uses opinion introducers followed by a complete subordinate clause with indicative present verbs (*Creo que el español es fácil*).",
            "rules": [
                "Positive Opinion takes Indicative: When stating an affirmative opinion (*Creo que, Pienso que, Opino que*), use normal indicative verbs (*es, tiene, podemos*).",
                "Tener Razón Formula: In Spanish you don't 'be right' (never *soy correcto*); you 'have reason' (*Tienes razón* = You are right, *Él tiene razón* = He is right).",
                "Polite Disagreement Formula: Start with acknowledging before dissenting (*Entiendo tu idea, pero...* or *Por un lado es verdad, sin embargo...*).",
                "Depender + DE: The preposition following 'depende' is always *de* (*Depende del precio*, *Depende de la situación*)."
            ],
            "structures": [
                "Opinion Header + que + Cláusula: [Creo / Pienso / Me parece] + que + [Sujeto + Verbo]",
                "Acuerdo / Desacuerdo: Estoy + [totalmente / en parte] + de acuerdo + con [persona/idea]"
            ],
            "examples": [
                {"spanish": "Pienso que Madrid tiene una vida cultural inmejorable.", "english": "I think that Madrid has an unbeatable cultural life.", "breakdown": "Pienso (verb 1st person) + que + Madrid tiene (subject + verb)"},
                {"spanish": "Tienes razón: la práctica constante es la clave del éxito.", "english": "You are right: constant practice is the key to success.", "breakdown": "Tienes razón (you have reason / you are right)"},
                {"spanish": "A mi parecer, esta opción es más económica.", "english": "To my mind, this option is more economical.", "breakdown": "A mi parecer (adverbial modifier) + oración principal"},
                {"spanish": "No estoy de acuerdo contigo en ese punto.", "english": "I do not agree with you on that point.", "breakdown": "No estoy + de acuerdo + contigo (with you)"}
            ],
            "commonMistakes": [
                {"incorrect": "Yo soy correcto en este tema.", "correct": "Tengo razón en este tema.", "why": "'To be right' is expressed with 'tener razón', never 'ser correcto'."},
                {"incorrect": "Depende en el clima.", "correct": "Depende del clima.", "why": "'Depender' requires 'de' (de + el = del), never 'en'."}
            ],
            "proTip": "Use 'Desde mi punto de vista' when giving a personal reflection during presentations or speaking exams. Examiners love this professional connector!"
        },
        "conversation": {
            "context": "Sakib and his classmate Laura participate in an A1 conversation exchange about city vs rural life.",
            "dialogue": [
                {"speaker": "Laura", "role": "Classmate", "spanish": "Sakib, ¿qué opinas tú: es mejor vivir en una gran metrópoli como Madrid o en un pueblo tranquilo?", "english": "Sakib, what is your opinion: is it better to live in a big metropolis like Madrid or in a quiet town?"},
                {"speaker": "Sakib", "role": "Student", "spanish": "En mi opinión, depende mucho del momento de la vida de cada persona.", "english": "In my opinion, it depends a lot on the moment of each person's life."},
                {"speaker": "Laura", "role": "Classmate", "spanish": "¿A qué te refieres exactamente?", "english": "What do you mean exactly?"},
                {"speaker": "Sakib", "role": "Student", "spanish": "Por un lado, la gran ciudad ofrece museos, cines y transporte público excelente. Por otro lado, la vida en el campo ofrece paz y aire puro.", "english": "On the one hand, the big city offers museums, cinemas, and excellent public transport. On the other hand, countryside life offers peace and pure air."},
                {"speaker": "Laura", "role": "Classmate", "spanish": "Tienes toda la razón. Sin embargo, yo creo que para los jóvenes la ciudad es más estimulante.", "english": "You are completely right. However, I believe that for young people the city is more stimulating."},
                {"speaker": "Sakib", "role": "Student", "spanish": "Estoy totalmente de acuerdo contigo. Además, en la ciudad es mucho más fácil conocer personas de diferentes culturas.", "english": "I totally agree with you. Moreover, in the city it is much easier to meet people from different cultures."},
                {"speaker": "Laura", "role": "Classmate", "spanish": "¡Exacto! Me parece fantástico cómo expresas tus opiniones en español, Sakib.", "english": "Exactly! It seems fantastic to me how you express your opinions in Spanish, Sakib."},
                {"speaker": "Sakib", "role": "Student", "spanish": "¡Muchas gracias, Laura! Practicar la conversación es lo que más me ayuda.", "english": "Thank you very much, Laura! Practicing conversation is what helps me the most."}
            ],
            "keyPhrases": [
                {"phrase": "En mi opinión...", "explanation": "'In my opinion...' (natural discussion starter)."},
                {"phrase": "Tienes toda la razón", "explanation": "'You are completely right' (strong validation)."},
                {"phrase": "Por un lado... por otro lado...", "explanation": "'On the one hand... on the other hand...' (balanced rhetoric)."}
            ]
        },
        "reading": {
            "title": "El arte de debatir con respeto y claridad",
            "passage": "El diálogo enriquecedor es el fundamento de cualquier sociedad democrática y plural. En el aprendizaje de una segunda lengua, ser capaz de formular una opinión personal representa un salto cualitativo trascendental: el estudiante ya no se limita a describir objetos o pedir comida en un restaurante, sino que comparte sus pensamientos íntimos y su visión del mundo. Para argumentar con eficacia en español, conviene utilizar fórmulas de cortesía y conectores discursivos claros. Comenzar con 'A mi parecer' o 'Considero que' indica madurez reflexiva. Por el contrario, discrepar no significa entrar en conflicto; expresiones como 'Entiendo tu perspectiva, sin embargo...' permiten manifestar desacuerdos con elegancia y elegancia diplomática. La meta de una conversación nunca debe ser imponer una verdad absoluta, sino construir puentes de entendimiento mutuo.",
            "translation": "Enriching dialogue is the foundation of any democratic and plural society. In the learning of a second language, being able to formulate a personal opinion represents a momentous qualitative leap: the student is no longer limited to describing objects or ordering food in a restaurant, but shares their intimate thoughts and worldview. To argue effectively in Spanish, it is advisable to use courtesy formulas and clear discourse connectors. Starting with 'A mi parecer' or 'Considero que' indicates reflective maturity. Conversely, disagreeing does not mean entering into conflict; expressions like 'Entiendo tu perspectiva, sin embargo...' allow stating disagreements with elegance and diplomatic grace. The goal of a conversation must never be to impose an absolute truth, but to build bridges of mutual understanding.",
            "questions": [
                {"question": "¿Qué representa poder formular opiniones en un nuevo idioma?", "options": ["Un salto cualitativo trascendental", "Una pérdida de tiempo", "Algo exclusivo para niños", "Un ejercicio de traducción aburrido"], "answer": 0, "explanation": "It represents a momentous qualitative leap ('un salto cualitativo trascendental')."},
                {"question": "¿Qué permite manifestar expresiones como 'Entiendo tu perspectiva, sin embargo'?", "options": ["Enfado y agresividad", "Desacuerdos con elegancia diplomática", "Olvido del idioma", "Terminar la conversación de golpe"], "answer": 1, "explanation": "It allows stating polite disagreements with diplomatic grace."},
                {"question": "¿Cuál es la meta de una buena conversación según el texto?", "options": ["Gritar más fuerte", "Imponer una verdad absoluta", "Construir puentes de entendimiento mutuo", "Vencer al compañero"], "answer": 2, "explanation": "The text states: 'construir puentes de entendimiento mutuo'."}
            ]
        },
        "exercises": [
            {
                "id": "d52-ex1",
                "type": "matching",
                "question": "Empareja cada expresión de opinión con su función comunicativa:",
                "options": [
                    "Estoy totalmente de acuerdo -> Expresar conformidad total",
                    "A mi parecer... -> Introducir punto de vista personal",
                    "Tienes razón -> Dar la razón al interlocutor",
                    "Por otro lado... -> Contrastar un argumento previo"
                ],
                "correct": 0,
                "explanation": "Estas frases estructuran cualquier debate o intercambio de ideas."
            },
            {
                "id": "d52-ex2",
                "type": "multiple-choice",
                "question": "¿Cómo se dice en español 'You are right'?",
                "options": ["Tienes razón", "Eres correcto", "Estás derecho", "Tienes correcto"],
                "correct": 0,
                "explanation": "En español se usa el modismo 'tener razón'."
            },
            {
                "id": "d52-ex3",
                "type": "sentence-ordering",
                "question": "Ordena la frase de opinión:",
                "options": ["En", "mi", "opinión", "el", "español", "es", "muy", "útil"],
                "correct": [0, 1, 2, 3, 4, 5, 6, 7],
                "explanation": "'En mi opinión el español es muy útil' expresa una opinión personal clara."
            },
            {
                "id": "d52-ex4",
                "type": "fill-in-the-blank",
                "question": "Completa: 'El precio de las entradas depende _____ día de la semana.'",
                "options": ["del", "en el", "por el", "con el"],
                "correct": 0,
                "explanation": "'Depender' siempre rige la preposición 'de' (de + el = del)."
            }
        ],
        "speakingChallenge": {
            "title": "Reto Oral: Tu Opinión Importa",
            "instructions": "Grábate o responde en voz alta justificando tus respuestas con al menos un conector.",
            "prompts": [
                {
                    "question": "¿Qué opinas: es mejor estudiar por la mañana temprano o por la noche?",
                    "hint": "Usa: 'En mi opinión, prefiero estudiar por la mañana / noche porque...'",
                    "sampleAnswer": "En mi opinión, es mucho mejor estudiar por la mañana temprano porque la mente está despejada y descansada."
                },
                {
                    "question": "¿Crees que viajar es la mejor manera de aprender una cultura?",
                    "hint": "Usa: 'Sí, creo que viajar es fundamental, sin embargo...'",
                    "sampleAnswer": "Sí, creo que viajar es la mejor manera porque te permite hablar con nativos y vivir la cultura en primera persona."
                },
                {
                    "question": "¿Estás de acuerdo con que la tecnología ayuda a aprender idiomas más rápido?",
                    "hint": "Usa: 'Estoy totalmente de acuerdo contigo porque...'",
                    "sampleAnswer": "Estoy totalmente de acuerdo, porque las aplicaciones y los cursos digitales nos permiten practicar todos los días en cualquier lugar."
                }
            ]
        },
        "dailyRevision": {
            "quickQuestions": [
                {"q": "¿Cómo se dice 'I agree with you'?", "a": "Estoy de acuerdo contigo."},
                {"q": "¿Cuál es la preposición que sigue a 'depende'?", "a": "La preposición 'de' (depende de)."},
                {"q": "¿Por qué es incorrecto decir 'yo soy correcto' para indicar que tienes razón?", "a": "Porque en español se dice 'tengo razón'."}
            ],
            "vocabRecall": [
                {"en": "In my opinion", "es": "En mi opinión / A mi parecer"},
                {"en": "On the one hand... on the other hand", "es": "Por un lado... por otro lado"},
                {"en": "However / Nevertheless", "es": "Sin embargo / No obstante"}
            ],
            "grammarRecall": "Recuerda que 'Creo que' afirmativo se acompaña del modo indicativo en A1: 'Creo que Madrid es preciosa'."
        },
        "checklist": [
            "Aprendí a introducir opiniones con 'Creo que' y 'En mi opinión'",
            "Practiqué el acuerdo total y el desacuerdo educado",
            "Dominé la expresión 'tener razón' frente al error literal",
            "Utilicé conectores como 'por un lado' y 'sin embargo'",
            "Completé el reto oral expresando mis preferencias",
            "Revisé los ejercicios interactivos de la lección"
        ]
    },
    {
        "day": 53,
        "stage": 6,
        "title": "Practical Phone Calls & Email Etiquette in Spain",
        "subtitle": "¿Dígame? Formal & Informal Telephony, Texting, and Writing Professional Emails",
        "goals": [
            "Answer the phone naturally using Spain standard protocol ('¿Dígame?', '¿De parte de quién?')",
            "Leave clear voice messages, ask for transfers, and take phone notes",
            "Write formal and informal emails with standard Spanish opening greetings and closings",
            "Master abbreviations common in Spanish correspondence (D., Dña., Att., etc.)"
        ],
        "bengaliNote": "স্পেনে ফোন ধরার ধরন কিন্তু অন্য অনেক দেশের চেয়ে আলাদা! স্প্যানিশরা ফোনে 'হ্যালো' বলে না; তারা বলে '¿Dígame?' (আমাকে বলুন) বা '¿Sí, dígame?'. আবার ইমেইলের ক্ষেত্রে ফরমাল হলে 'Estimado/a Señor/a' এবং ইনফরমাল হলে '¡Hola, amigo!'। আজকের লেসনে আপনি স্পেনের প্রফেশনাল যোগাযোগ শৈলী পুরোপুরি আয়ত্ত করবেন!",
        "vocabulary": [
            {"word": "¿Dígame? / ¿Sí, dígame?", "translation": "Hello? / Tell me (standard Spain phone answer)", "pos": "phrase", "gender": None, "example": "¿Dígame? Buenos días, habla Sakib.", "exampleTranslation": "Hello? Good morning, Sakib speaking."},
            {"word": "¿De parte de quién?", "translation": "Who is calling? (lit: on behalf of whom?)", "pos": "phrase", "gender": None, "example": "¿De parte de quién, por favor?", "exampleTranslation": "Who is calling, please?"},
            {"word": "Poner con / Pasar con (alguien)", "translation": "To put through to / transfer to (someone)", "pos": "verb", "gender": None, "example": "¿Me pone con el departamento de reservas?", "exampleTranslation": "Could you put me through to the reservations department?"},
            {"word": "Dejar un recado / mensaje", "translation": "To leave a message", "pos": "phrase", "gender": None, "example": "¿Desea dejar un recado?", "exampleTranslation": "Would you like to leave a message?"},
            {"word": "Se corta / No hay cobertura", "translation": "It is breaking up / There is no reception", "pos": "phrase", "gender": None, "example": "Perdona, se corta la llamada; no tengo cobertura.", "exampleTranslation": "Sorry, the call is breaking up; I have no reception."},
            {"word": "Estimado/a señor/a", "translation": "Dear Sir/Madam (formal email greeting)", "pos": "phrase", "gender": None, "example": "Estimada señora Gómez: le escribo para confirmar la cita.", "exampleTranslation": "Dear Ms. Gómez: I am writing to you to confirm the appointment."},
            {"word": "Un cordial saludo / Atentamente", "translation": "Kind regards / Sincerely (formal closing)", "pos": "phrase", "gender": None, "example": "Atentamente, Sakib Ahmed.", "exampleTranslation": "Sincerely, Sakib Ahmed."},
            {"word": "Un abrazo / Saludos", "translation": "A hug / Warm regards (informal closing)", "pos": "phrase", "gender": None, "example": "Un abrazo muy fuerte y nos vemos pronto.", "exampleTranslation": "A big hug and see you soon."},
            {"word": "El archivo adjunto", "translation": "The attached file", "pos": "noun", "gender": "masculine", "example": "Le adjunto mi currículum en el archivo adjunto.", "exampleTranslation": "I attach my CV for you in the attached file."},
            {"word": "Quedo a su disposición", "translation": "I remain at your disposal (formal formula)", "pos": "phrase", "gender": None, "example": "Quedo a su entera disposición para cualquier duda.", "exampleTranslation": "I remain at your complete disposal for any question."}
        ],
        "sentences": [
            {"spanish": "¿Dígame? Hola, buenos días, ¿podría hablar con el director, por favor?", "english": "Hello? Hi, good morning, could I speak with the director, please?"},
            {"spanish": "Un momento, por favor, ahora mismo le paso con su secretaria.", "english": "One moment, please, right now I'll transfer you to his secretary."},
            {"spanish": "En este momento la línea está ocupada; ¿desea dejar un recado?", "english": "At this moment the line is busy; would you like to leave a message?"},
            {"spanish": "Te escucho un poco entrecortado, creo que entro en un túnel sin cobertura.", "english": "I hear you a bit broken up, I think I'm entering a tunnel without reception."},
            {"spanish": "Estimado profesor: Le escribo para solicitar una tutoría el próximo jueves.", "english": "Dear professor: I am writing to you to request a tutorial next Thursday."},
            {"spanish": "Muchas gracias por su pronta respuesta. Un cordial saludo, Sakib.", "english": "Thank you very much for your prompt reply. Warm regards, Sakib."}
        ],
        "grammar": {
            "title": "Telephony Protocols & Epistolary Registers in Spanish",
            "explanation": "Spanish communication strictly differentiates between formal registry (Usted) for institutions, hotels, and professional contacts, and informal registry (Tú) for friends.",
            "rules": [
                "Phone Answering in Spain: Always answer with '¿Dígame?' or '¿Sí?' Never say 'Hola' alone when picking up a phone.",
                "Introducing Yourself on the Phone: Say 'Habla Sakib' (Sakib speaking) or 'Soy Sakib' (I am Sakib). In formal business say 'Le llama Sakib Ahmed'.",
                "Formal Email Structure: Salutation (Estimado/a + cargo/apellido:) -> Body -> Formal close (Atentamente / Un cordial saludo,) -> Signature.",
                "Punctuation Note: Spanish email salutations use a colon (:), not a comma (*Estimada Sra. López:* instead of *Dear Ms. Lopez,*)."
            ],
            "structures": [
                "Formal Phone Request: ¿Podría hablar con [Nombre/Cargo]?",
                "Email Body Starter: Le escribo / Me pongo en contacto con usted para + [Infinitivo]"
            ],
            "examples": [
                {"spanish": "¿Podría decirme quién llama, por favor?", "english": "Could you tell me who is calling, please?", "breakdown": "Podría (conditional polite) + decirme (infinitive + clitic me)"},
                {"spanish": "Le paso la llamada enseguida.", "english": "I'll transfer the call to you right away.", "breakdown": "Le (indirect object formal Usted) + paso (present)"},
                {"spanish": "Adjunto el justificante médico solicitado.", "english": "I attach the requested medical certificate.", "breakdown": "Adjunto (verb 1st person) + objeto directo"},
                {"spanish": "Quedo a la espera de sus noticias.", "english": "I remain waiting for your news.", "breakdown": "Quedo a la espera (epistolary formula)"}
            ],
            "commonMistakes": [
                {"incorrect": "Estimado señor Gómez, (con coma en español)", "correct": "Estimado señor Gómez: (con dos puntos)", "why": "In Spanish epistolary grammar, greetings are followed by a colon (:), not a comma."},
                {"incorrect": "¿Quién es? (al contestar el teléfono bruscamente)", "correct": "¿De parte de quién? o ¿Quién llama, por favor?", "why": "'¿Quién es?' sounds blunt and impolite on the telephone."}
            ],
            "proTip": "When writing an email to a university or business in Spain, ending with 'Un cordial saludo' strikes the absolute sweet spot: professional, respectful, and warm without being stiff!"
        },
        "conversation": {
            "context": "Sakib calls the student secretary at the Universidad de Salamanca to inquire about an A1 certificate exam date.",
            "dialogue": [
                {"speaker": "Secretaria", "role": "Receptionist", "spanish": "¿Sí, dígame? Secretaría de Cursos Internacionales.", "english": "Yes, hello? International Courses Secretariat."},
                {"speaker": "Sakib", "role": "Student", "spanish": "Buenos días. Habla Sakib Ahmed. Quisiera información sobre la convocatoria del examen de fin de curso.", "english": "Good morning. Sakib Ahmed speaking. I would like information regarding the end-of-course exam session."},
                {"speaker": "Secretaria", "role": "Receptionist", "spanish": "Buenos días, señor Ahmed. Un segundo, por favor, le pongo con el coordinador de exámenes.", "english": "Good morning, Mr. Ahmed. One second, please, I'll put you through to the exam coordinator."},
                {"speaker": "Secretaria", "role": "Receptionist", "spanish": "Vaya, parece que la línea comunica. ¿Desea dejar su número para que le devolvamos la llamada?", "english": "Oh dear, it seems the line is busy. Would you like to leave your number so we can return your call?"},
                {"speaker": "Sakib", "role": "Student", "spanish": "Sí, perfecto. ¿O puedo enviarles un correo electrónico con mis datos?", "english": "Yes, perfect. Or could I send you an email with my details?"},
                {"speaker": "Secretaria", "role": "Receptionist", "spanish": "Por supuesto. Escriba a examenes@universidad.es indicando su nombre completo y número de pasaporte.", "english": "Of course. Write to examenes@universidad.es indicating your full name and passport number."},
                {"speaker": "Sakib", "role": "Student", "spanish": "Estupendo. Redacto el correo ahora mismo. Muchísimas gracias por su amabilidad.", "english": "Great. I'll draft the email right away. Thank you very much for your kindness."},
                {"speaker": "Secretaria", "role": "Receptionist", "spanish": "De nada, señor Ahmed. Un placer. ¡Hasta luego!", "english": "You're welcome, Mr. Ahmed. A pleasure. Goodbye!"}
            ],
            "keyPhrases": [
                {"phrase": "Habla [Nombre]", "explanation": "'[Name] speaking' (natural phone identification)."},
                {"phrase": "Le pongo con...", "explanation": "'I'll put you through to...' (transferring phone calls)."},
                {"phrase": "La línea comunica", "explanation": "'The line is busy' (Spain telephony term)."}
            ]
        },
        "reading": {
            "title": "Modelos epistolares: Del teléfono al correo electrónico",
            "passage": "La comunicación formal en el mundo hispanohablante mantiene normas de cortesía muy apreciadas. En el ámbito telefónico, la fórmula estándar en España para descolgar el auricular es el tradicional '¿Dígame?'. Esta expresión, concisa pero hospitalaria, invita al interlocutor a exponer el motivo de su llamada. Cuando redactamos un correo electrónico profesional, la estructura debe ser impecable. Comenzamos identificando con respeto al destinatario: 'Estimado señor Rodríguez:' o 'Estimada señora Martín:'. En el cuerpo del mensaje, exponemos con brevedad y claridad el objetivo de la comunicación: 'El motivo de este correo es solicitar información sobre...'. Al concluir, evitamos despedidas cortantes y preferimos fórmulas consagradas como 'Quedo a su disposición para cualquier aclaración adicional' y 'Atentamente'. Dominar estos códigos proyecta una imagen de competencia, seriedad y alta estima.",
            "translation": "Formal communication in the Spanish-speaking world maintains highly appreciated norms of courtesy. In the telephone sphere, the standard formula in Spain when picking up the handset is the traditional '¿Dígame?'. This expression, concise yet welcoming, invites the caller to state the purpose of their call. When we draft a professional email, the structure must be impeccable. We begin by identifying the recipient with respect: 'Estimado señor Rodríguez:' or 'Estimada señora Martín:'. In the body of the message, we state with brevity and clarity the objective of the communication: 'The purpose of this email is to request information regarding...'. In concluding, we avoid abrupt farewells and prefer established formulas such as 'I remain at your disposal for any further clarification' and 'Sincerely'. Mastering these codes projects an image of competence, seriousness, and high esteem.",
            "questions": [
                {"question": "¿Cuál es la fórmula estándar para responder al teléfono en España?", "options": ["¿Quién vive?", "¿Dígame?", "¡Oiga!", "¿Qué quieres?"], "answer": 1, "explanation": "'¿Dígame?' o '¿Sí, dígame?' es el estándar telefónico indiscutible en España."},
                {"question": "¿Qué signo de puntuación se pone tras el saludo en un correo en español?", "options": ["Una coma (,)", "Dos puntos (:)", "Un punto y coma (;)", "Un signo de interrogación"], "answer": 1, "explanation": "In Spanish formal letters/emails, greetings take a colon (dos puntos :)."},
                {"question": "¿Qué proyecta dominar estos códigos epistolares?", "options": ["Competencia, seriedad y alta estima", "Falta de originalidad", "Pérdida de tiempo", "Confusión"], "answer": 0, "explanation": "It projects competence, seriousness, and esteem ('competencia, seriedad y alta estima')."}
            ]
        },
        "exercises": [
            {
                "id": "d53-ex1",
                "type": "matching",
                "question": "Empareja cada fórmula epistolar con su categoría correspondiente:",
                "options": [
                    "Estimada directora: -> Saludo formal de correo",
                    "¿De parte de quién? -> Pregunta de protocolo telefónico",
                    "Un cordial saludo -> Despedida formal por escrito",
                    "Un abrazo fuerte -> Despedida informal entre amigos"
                ],
                "correct": 0,
                "explanation": "Cada registro tiene sus fórmulas prototípicas en el mundo hispano."
            },
            {
                "id": "d53-ex2",
                "type": "multiple-choice",
                "question": "¿Cómo se indica en España que una llamada telefónica no puede completarse porque la otra persona está hablando?",
                "options": ["La línea comunica / La línea está ocupada", "El teléfono está dormido", "No hay voz", "El cable está roto"],
                "correct": 0,
                "explanation": "'La línea comunica' o 'está ocupada' son las expresiones naturales."
            },
            {
                "id": "d53-ex3",
                "type": "sentence-ordering",
                "question": "Ordena el inicio de un correo formal:",
                "options": ["Estimado", "señor", "García:", "Le", "escribo", "para", "solicitar", "información"],
                "correct": [0, 1, 2, 3, 4, 5, 6, 7],
                "explanation": "'Estimado señor García: Le escribo para solicitar información' es la estructura formal por excelencia."
            },
            {
                "id": "d53-ex4",
                "type": "fill-in-the-blank",
                "question": "Completa la frase de cortesía: 'Quedo a su _____ para cualquier consulta.'",
                "options": ["disposición", "reunión", "llamada", "mensaje"],
                "correct": 0,
                "explanation": "'Quedo a su disposición' es la fórmula canónica de cortesía profesional."
            }
        ],
        "speakingChallenge": {
            "title": "Reto Oral: Simulacro Telefónico",
            "instructions": "Imagina que llamas a un hotel en Barcelona para confirmar tu reserva. Habla en voz alta.",
            "prompts": [
                {
                    "question": "¿Cómo respondes cuando el recepcionista dice: '¿Dígame, Hotel Cataluña?'",
                    "hint": "Identifícate con educación: 'Buenos días, habla... y llamo para...'",
                    "sampleAnswer": "Buenos días, habla Sakib Ahmed. Llamo para confirmar los detalles de mi reserva de habitación para la próxima semana."
                },
                {
                    "question": "¿Qué dices si no escuchas bien porque la señal es débil?",
                    "hint": "Usa: 'Disculpe, se corta la llamada...'",
                    "sampleAnswer": "Disculpe, se corta la llamada y no le escucho bien; creo que no hay buena cobertura en este momento."
                },
                {
                    "question": "¿Cómo te despides formalmente por teléfono agradeciendo la ayuda recibida?",
                    "hint": "Usa: 'Muchas gracias por su atención, que tenga un buen día...'",
                    "sampleAnswer": "Muchísimas gracias por su atención y amabilidad. Que tenga un buen día. ¡Hasta pronto!"
                }
            ]
        },
        "dailyRevision": {
            "quickQuestions": [
                {"q": "¿Qué palabra se usa en España para contestar al descolgar el teléfono?", "a": "Se dice '¿Dígame?' o '¿Sí, dígame?'."},
                {"q": "¿Qué fórmula formal concluye un correo profesional?", "a": "'Un cordial saludo' o 'Atentamente'."},
                {"q": "¿Qué significa 'dejar un recado'?", "a": "Dejar un mensaje telefónico para una persona ausente."}
            ],
            "vocabRecall": [
                {"en": "Who is calling? (phone)", "es": "¿De parte de quién?"},
                {"en": "Attached file", "es": "El archivo adjunto"},
                {"en": "I remain at your disposal", "es": "Quedo a su disposición"}
            ],
            "grammarRecall": "Recuerda usar siempre dos puntos tras el encabezamiento en las cartas y correos en español: 'Estimada profesora:'."
        },
        "checklist": [
            "Aprendí a contestar el teléfono como en España ('¿Dígame?')",
            "Practiqué la solicitud de transferencias ('poner con')",
            "Dominé la estructura de un correo formal con dos puntos (:)",
            "Conocí fórmulas de despedida formales e informales",
            "Realicé el simulacro de llamada telefónica con soltura",
            "Resolví los ejercicios interactivos de telefonía y correo"
        ]
    },
    {
        "day": 54,
        "stage": 6,
        "title": "Handling Emergencies, Lost Items, and Healthcare in Spain",
        "subtitle": "Urgent Situaciones: Calling 112, Pharmacy On Duty, Police Reports & Medical Care",
        "goals": [
            "Call emergency services in Spain using the universal number 112 with composure",
            "Report lost or stolen items at the police station (comisaría de policía / denuncia)",
            "Explain sudden health symptoms at a clinic (urgencias) or duty pharmacy (farmacia de guardia)",
            "Understand essential emergency signage and legal vocabulary across Spain"
        ],
        "bengaliNote": "বিপদ বলে কয়ে আসে না! ইউরোপে বা স্পেনে যেকোনো জরুরি অবস্থায় (অ্যাম্বুলেন্স, পুলিশ, ফায়ার সার্ভিস) একটাই সার্বজনীন নম্বর: ১১২ (ciento doce)। পাসপোর্ট হারিয়ে গেলে পুলিশের কাছে গিয়ে বলতে হয় 'Quiero poner una denuncia' (আমি একটি জিডি/রিপোর্ট করতে চাই)। এই লেসনটি আপনাকে যেকোনো জরুরি মুহূর্তে শান্ত ও প্রস্তুত রাখবে!",
        "vocabulary": [
            {"word": "El número de emergencias 112", "translation": "The emergency number 112 (free in Europe)", "pos": "noun", "gender": "masculine", "example": "En caso de accidente, llame de inmediato al 112.", "exampleTranslation": "In case of accident, call 112 immediately."},
            {"word": "La comisaría de policía", "translation": "The police station", "pos": "noun", "gender": "feminine", "example": "¿Dónde está la comisaría más cercana?", "exampleTranslation": "Where is the nearest police station?"},
            {"word": "Poner una denuncia", "translation": "To file a police report", "pos": "phrase", "gender": None, "example": "He perdido mi cartera y tengo que poner una denuncia.", "exampleTranslation": "I have lost my wallet and I have to file a police report."},
            {"word": "La farmacia de guardia", "translation": "The 24/7 on-duty pharmacy", "pos": "noun", "gender": "feminine", "example": "Es medianoche; busquemos una farmacia de guardia.", "exampleTranslation": "It's midnight; let's find an on-duty pharmacy."},
            {"word": "El servicio de urgencias", "translation": "Emergency medical room / ER", "pos": "noun", "gender": "masculine", "example": "Fuimos al hospital a urgencias por la fiebre alta.", "exampleTranslation": "We went to the hospital emergency room for high fever."},
            {"word": "La tarjeta sanitaria / El seguro de viaje", "translation": "Health card / Travel insurance", "pos": "noun", "gender": "masculine", "example": "Aquí tiene mi pasaporte y mi póliza de seguro de viaje.", "exampleTranslation": "Here you have my passport and my travel insurance policy."},
            {"word": "Robar / El robo / El carterista", "translation": "To steal / The theft / Pickpocket", "pos": "noun", "gender": "mixed", "example": "Cuidado con los carteristas en las zonas turísticas.", "exampleTranslation": "Watch out for pickpockets in tourist areas."},
            {"word": "Perder / La pérdida del pasaporte", "translation": "To lose / Loss of passport", "pos": "noun", "gender": "feminine", "example": "Necesito un justificante por pérdida de pasaporte.", "exampleTranslation": "I need a certificate for loss of passport."},
            {"word": "Estar mareado/a / Desmayarse", "translation": "To feel dizzy / To faint", "pos": "verb", "gender": None, "example": "Siéntate aquí si estás mareado.", "exampleTranslation": "Sit down here if you feel dizzy."},
            {"word": "¡Ayuda! / ¡Socorro! / ¡Fuego!", "translation": "Help! / SOS! / Fire! (emergency shouts)", "pos": "exclamation", "gender": None, "example": "¡Socorro! ¡Alguien ha sufrido una caída!", "exampleTranslation": "Help! Someone has suffered a fall!"}
        ],
        "sentences": [
            {"spanish": "¡Socorro! ¡Por favor, llamen a una ambulancia rápidamente!", "english": "Help! Please, call an ambulance quickly!"},
            {"spanish": "Buenos días, agente, necesito poner una denuncia porque me han robado la mochila en el metro.", "english": "Good morning, officer, I need to file a report because my backpack was stolen in the subway."},
            {"spanish": "Dentro de la mochila tenía mi pasaporte original, las tarjetas de crédito y las llaves.", "english": "Inside the backpack I had my original passport, credit cards, and keys."},
            {"spanish": "¿Dónde se encuentra la farmacia de guardia más próxima a esta calle?", "english": "Where is the nearest on-duty pharmacy to this street located?"},
            {"spanish": "Tengo un dolor muy agudo en el pecho y me siento mareado; necesito ver a un médico.", "english": "I have very sharp pain in my chest and feel dizzy; I need to see a doctor."},
            {"spanish": "Mantenga la calma, señor Ahmed; los paramédicos ya están en camino.", "english": "Keep calm, Mr. Ahmed; the paramedics are already on their way."}
        ],
        "grammar": {
            "title": "Emergency Imperatives, Passive Formulations & Obligation Modals",
            "explanation": "During emergencies, language must be concise, direct, and unambiguous. We use impersonal passive structures (*se ha perdido, me han robado*) and urgent obligation modals (*tener que + infinitivo, hay que*).",
            "rules": [
                "112 Universal Dialing: Spain uses 112 for all emergencies (police, medical, fire). Operators usually speak Spanish, English, and French.",
                "Reporting Thefts: Use the 3rd person plural impersonal: *Me han robado la cartera* (They stole my wallet = Someone stole my wallet).",
                "Denuncia Documentation: Police require precise details: date, exact time (*hacia las tres de la tarde*), location (*en la estación de Atocha*), and description of items.",
                "Expressing Bodily Sensations: Use *tener* for physical ailments (*tengo mareos, tengo fiebre, tengo náuseas*) and *doler* for pain (*me duele el pecho*)."
            ],
            "structures": [
                "Emergency Directive: ¡Llamen al 112! / ¡Ayúdenme, por favor!",
                "Police Report Formula: Vengo a poner una denuncia por [robo / pérdida] de [objeto]"
            ],
            "examples": [
                {"spanish": "Me han sustraído el teléfono móvil del bolsillo.", "english": "They took the mobile phone from my pocket.", "breakdown": "Me (indirect object) + han sustraído (perfect 3rd plural) + el teléfono"},
                {"spanish": "Necesitamos un médico de guardia urgentemente.", "english": "We need an on-duty doctor urgently.", "breakdown": "Necesitamos (verb) + médico de guardia (phrase) + urgentemente"},
                {"spanish": "¿Tiene usted seguro médico internacional?", "english": "Do you have international health insurance?", "breakdown": "Tiene usted (formal question) + sustantivo"},
                {"spanish": "Firme aquí abajo para formalizar la denuncia.", "english": "Sign down here to formalize the police report.", "breakdown": "Firme (formal imperative) + aquí abajo"}
            ],
            "commonMistakes": [
                {"incorrect": "Quiero hacer una denuncia policía.", "correct": "Quiero poner una denuncia en la comisaría.", "why": "In Spanish the standard legal idiom is 'poner una denuncia'."},
                {"incorrect": "Llama al 911 en España.", "correct": "Llama al 112 en España.", "why": "911 is North American; Europe and Spain use 112 exclusively."}
            ],
            "proTip": "Always keep a photocopy or digital cloud photo of your passport and visa on your phone. In case of loss, having the passport number readily available at the police station speeds up the 'denuncia' process dramatically!"
        },
        "conversation": {
            "context": "Sakib arrives at the National Police station (Comisaría de Policía Nacional) in Madrid to report a lost document folder.",
            "dialogue": [
                {"speaker": "Agente", "role": "Police Officer", "spanish": "Buenas tardes. ¿En qué puedo ayudarle?", "english": "Good afternoon. How can I help you?"},
                {"speaker": "Sakib", "role": "Student", "spanish": "Buenas tardes, agente. Quisiera poner una denuncia por pérdida de documentos.", "english": "Good afternoon, officer. I would like to file a report for loss of documents."},
                {"speaker": "Agente", "role": "Police Officer", "spanish": "De acuerdo. Tome asiento. ¿Qué ha ocurrido exactamente?", "english": "All right. Take a seat. What has occurred exactly?"},
                {"speaker": "Sakib", "role": "Student", "spanish": "Esta mañana, hacia las once, olvidé una carpeta azul en un banco del Parque del Retiro.", "english": "This morning, around eleven, I forgot a blue folder on a bench in El Retiro Park."},
                {"speaker": "Agente", "role": "Police Officer", "spanish": "¿Qué contenía la carpeta?", "english": "What did the folder contain?"},
                {"speaker": "Sakib", "role": "Student", "spanish": "Contenía mi carné de estudiante, fotocopias de mi pasaporte y mis apuntes de español.", "english": "It contained my student card, photocopies of my passport, and my Spanish notes."},
                {"speaker": "Agente", "role": "Police Officer", "spanish": "Afortunadamente no llevaba dinero en efectivo ni tarjetas bancarias. Aquí tiene la copia sellada de la denuncia para su embajada.", "english": "Fortunately you weren't carrying cash or bank cards. Here is the stamped copy of the report for your embassy."},
                {"speaker": "Sakib", "role": "Student", "spanish": "Muchísimas gracias por su ayuda y rapidez, agente.", "english": "Thank you very much for your help and promptness, officer."}
            ],
            "keyPhrases": [
                {"phrase": "Poner una denuncia", "explanation": "'To file a police report' (essential legal step)."},
                {"phrase": "Tome asiento", "explanation": "'Take a seat' (polite administrative directive)."},
                {"phrase": "Copia sellada", "explanation": "'Stamped copy / official stamped certificate'."}
            ]
        },
        "reading": {
            "title": "Seguridad y sanidad en España: Guía práctica para el viajero",
            "passage": "España es considerada internacionalmente como uno de los países más seguros y con mejor sistema de salud pública del continente europeo. Sin embargo, en ciudades cosmopolitas con alta afluencia turística como Madrid o Barcelona, conviene tomar precauciones básicas para evitar hurtos menores por parte de carteristas. En caso de sufrir un incidente, el ciudadano o visitante dispone del número telefónico 112, un servicio gratuito disponible las 24 horas que coordina ambulancias, bomberos y policía. Si necesita adquirir medicamentos fuera del horario comercial ordinario, cada barrio dispone de una 'farmacia de guardia', identificable por una cruz verde iluminada. Los hospitales cuentan con departamentos de urgencias equipados con tecnología de vanguardia donde cualquier persona en situación crítica recibe atención médica inmediata. Saber comunicarse con serenidad en estos escenarios proporciona una tranquilidad inestimable.",
            "translation": "Spain is internationally considered one of the safest countries with the finest public healthcare systems on the European continent. However, in cosmopolitan cities with heavy tourist influx like Madrid or Barcelona, it is advisable to take basic precautions to avoid petty theft by pickpockets. In case of experiencing an incident, the citizen or visitor has the telephone number 112, a free 24-hour service that coordinates ambulances, firefighters, and police. If you need to purchase medicines outside regular business hours, every neighborhood has an 'on-duty pharmacy', identifiable by an illuminated green cross. Hospitals feature emergency departments equipped with state-of-the-art technology where any person in critical condition receives immediate medical care. Knowing how to communicate with composure in these scenarios provides invaluable peace of mind.",
            "questions": [
                {"question": "¿Cuál es el número de teléfono gratuito para emergencias en España?", "options": ["999", "112", "911", "091"], "answer": 1, "explanation": "El 112 es el número centralizado de emergencias europeo."},
                {"question": "¿Cómo se reconoce una farmacia de guardia en España?", "options": ["Por una bandera roja", "Por una cruz verde iluminada", "Por un cartel amarillo", "Por un timbre azul"], "answer": 1, "explanation": "Farmacias en España se identifican por la tradicional cruz verde iluminada."},
                {"question": "¿Qué servicio coordina el 112?", "options": ["Solo taxis", "Ambulancias, bomberos y policía", "Reservas de hoteles", "Vuelos de avión"], "answer": 1, "explanation": "Coordina todos los servicios esenciales de emergencia simultáneamente."}
            ]
        },
        "exercises": [
            {
                "id": "d54-ex1",
                "type": "matching",
                "question": "Relaciona cada situación con el servicio o lugar adecuado:",
                "options": [
                    "Me han sustraído la cartera -> Comisaría de policía",
                    "Tengo fiebre alta a las tres de la madrugada -> Farmacia de guardia / Urgencias",
                    "Incendio o accidente en carretera -> Llamar al 112",
                    "Pérdida de pasaporte en el extranjero -> Consulado o Embajada"
                ],
                "correct": 0,
                "explanation": "Conocer el canal adecuado resuelve emergencias con eficacia."
            },
            {
                "id": "d54-ex2",
                "type": "multiple-choice",
                "question": "¿Cómo se dice en español 'I need to file a police report'?",
                "options": ["Necesito poner una denuncia", "Necesito fabricar una policía", "Necesito ordenar un papel", "Necesito denunciar el banco"],
                "correct": 0,
                "explanation": "La expresión correcta y formal es 'poner una denuncia'."
            },
            {
                "id": "d54-ex3",
                "type": "sentence-ordering",
                "question": "Ordena las palabras de la petición de socorro:",
                "options": ["¡Por", "favor,", "llamen", "a", "una", "ambulancia", "inmediatamente!"],
                "correct": [0, 1, 2, 3, 4, 5, 6],
                "explanation": "Llamada de urgencia directa y comprensible."
            },
            {
                "id": "d54-ex4",
                "type": "fill-in-the-blank",
                "question": "Completa: 'He ido al hospital y me han atendido en el servicio de _____.'",
                "options": ["urgencias", "recados", "denuncias", "fiestas"],
                "correct": 0,
                "explanation": "'Servicio de urgencias' es el área de emergencias hospitalarias."
            }
        ],
        "speakingChallenge": {
            "title": "Reto Oral: Situación de Emergencia Simulada",
            "instructions": "Responde con serenidad a las siguientes preguntas en voz alta.",
            "prompts": [
                {
                    "question": "Llamas al 112 y el operador dice: '112 emergencias, ¿dónde se encuentra usted?'",
                    "hint": "Di tu ubicación clara: 'Estoy en la calle... número...'",
                    "sampleAnswer": "Hola, estoy en la calle Gran Vía, número 25, en Madrid. Una persona se ha desmayado y necesita atención médica urgente."
                },
                {
                    "question": "¿Cómo describes en la farmacia que te duele la cabeza y el estómago?",
                    "hint": "Usa: 'Me duele... y tengo náuseas / fiebre...'",
                    "sampleAnswer": "Buenos días, tengo un dolor de cabeza muy fuerte y me duele el estómago. ¿Tiene algún medicamento suave o analgésico?"
                },
                {
                    "question": "¿Qué dices si pierdes tu tarjeta de crédito?",
                    "hint": "Usa: 'He perdido mi tarjeta de crédito y necesito bloquearla...'",
                    "sampleAnswer": "Hola, llamo a mi banco porque he perdido mi tarjeta de crédito y necesito bloquearla inmediatamente para evitar cargos indebidos."
                }
            ]
        },
        "dailyRevision": {
            "quickQuestions": [
                {"q": "¿Qué número llamas para una emergencia en España?", "a": "Al 112 (ciento doce)."},
                {"q": "¿Qué significa 'farmacia de guardia'?", "a": "Farmacia abierta fuera del horario comercial habitual, inclusive 24 horas."},
                {"q": "¿Cómo se dice 'to file a report'?", "a": "Poner una denuncia."}
            ],
            "vocabRecall": [
                {"en": "Police station", "es": "La comisaría de policía"},
                {"en": "Emergency room", "es": "El servicio de urgencias"},
                {"en": "Travel insurance", "es": "El seguro de viaje"}
            ],
            "grammarRecall": "Recuerda usar 'me han robado' (tercera persona plural impersonal) cuando no conoces la identidad del ladrón."
        },
        "checklist": [
            "Conozco el número de emergencia 112 y cómo funciona",
            "Aprendí a formular una denuncia en la comisaría",
            "Identifico la farmacia de guardia y el servicio de urgencias",
            "Practiqué la descripción de síntomas agudos",
            "Realicé el reto oral de simulación de emergencias",
            "Completé todos los ejercicios interactivos del Día 54"
        ]
    },
    {
        "day": 55,
        "stage": 6,
        "title": "Top 20 A1 Mistakes & Traps + Mid-Stage 6 Diagnostic Review",
        "subtitle": "The Ultimate Clean-Up: False Friends, Gender Traps, Ser/Estar, and Preposition Pitfalls",
        "goals": [
            "Identify and permanently eliminate the 20 most frequent errors made by A1 Spanish learners",
            "Master difficult false friends (embarazada, constipado, éxito, asistir, carpeta)",
            "Conquer deceptive gender exceptions (el problema, el tema, el día, la mano, la foto)",
            "Complete the rigorous Mid-Stage 6 Diagnostic Assessment with 100% accuracy"
        ],
        "bengaliNote": "আজকের দিনটি আপনার স্প্যানিশের সবচেয়ে বড় ফিল্টারিং বা পরিশোধন দিন! A1 লেভেলের শিক্ষার্থীরা সবচেয়ে বেশি যে ২০টি ভুল করে, সেগুলোকে আজ আমরা চিরতরে বিদায় জানাব। যেমন: 'embarazada' মানে কিন্তু 'pregnant' (গর্ভবতী), 'embarrassed' বা লজ্জিত নয়! লজ্জিত হলো 'avergonzado'। এই সূক্ষ্ম পার্থক্যগুলো জানলে কেউ আপনাকে কখনো কাঁচা স্পিকার ভাবতে পারবে না!",
        "vocabulary": [
            {"word": "Embarazada (falso amigo)", "translation": "Pregnant (NOT embarrassed; embarrassed is 'avergonzado')", "pos": "adjective", "gender": "feminine", "example": "Mi hermana está embarazada de cinco meses.", "exampleTranslation": "My sister is five months pregnant."},
            {"word": "Constipado/a (falso amigo)", "translation": "Having a cold (NOT constipated; constipated is 'estreñido')", "pos": "adjective", "gender": "masculine / feminine", "example": "Tengo tos porque estoy constipado.", "exampleTranslation": "I have a cough because I have a cold."},
            {"word": "El éxito (falso amigo)", "translation": "Success (NOT exit; exit is 'la salida')", "pos": "noun", "gender": "masculine", "example": "La obra de teatro tuvo un éxito extraordinario.", "exampleTranslation": "The theatrical play had extraordinary success."},
            {"word": "Asistir (a) (falso amigo)", "translation": "To attend (NOT to assist/help; to assist is 'ayudar')", "pos": "verb", "gender": None, "example": "Mañana voy a asistir a la conferencia de literatura.", "exampleTranslation": "Tomorrow I am going to attend the literature lecture."},
            {"word": "La carpeta (falso amigo)", "translation": "Folder / binder (NOT carpet; carpet is 'la alfombra')", "pos": "noun", "gender": "feminine", "example": "Guardo mis ejercicios en una carpeta roja.", "exampleTranslation": "I keep my exercises in a red folder."},
            {"word": "El problema / El tema / El idioma", "translation": "The problem / The topic / The language (Greek -ma masculine)", "pos": "noun", "gender": "masculine", "example": "El problema tiene una solución sencilla.", "exampleTranslation": "The problem has a simple solution."},
            {"word": "La mano / La foto / La moto", "translation": "The hand / The photo / The motorbike (Feminine nouns ending in -o)", "pos": "noun", "gender": "feminine", "example": "Tengo las manos frías por el viento.", "exampleTranslation": "My hands are cold because of the wind."},
            {"word": "El agua fría / Las aguas frías", "translation": "Cold water (Feminine noun taking 'el' in singular to prevent hiatus)", "pos": "noun", "gender": "feminine", "example": "Bebo el agua fría todos los días.", "exampleTranslation": "I drink cold water every day."},
            {"word": "Gustar singular vs plural", "translation": "Me gusta el libro / Me gustan los libros", "pos": "grammar trap", "gender": None, "example": "Me gustan mucho los museos de Madrid.", "exampleTranslation": "I like the museums of Madrid very much."},
            {"word": "Por fin vs Para siempre", "translation": "At last vs Forever (Preposition contrast)", "pos": "phrase", "gender": None, "example": "¡Por fin terminé el repaso de gramática!", "exampleTranslation": "At last I finished the grammar review!"}
        ],
        "sentences": [
            {"spanish": "Estoy avergonzado por mi despiste; no estoy 'embarazado'.", "english": "I am embarrassed because of my blunder; I am not 'pregnant'."},
            {"spanish": "Si estás constipado, toma un té caliente con miel y limón.", "english": "If you have a cold, drink hot tea with honey and lemon."},
            {"spanish": "Para salir de la estación, busque el cartel verde de 'Salida', no 'Éxito'.", "english": "To exit the station, look for the green sign for 'Salida', not 'Éxito'."},
            {"spanish": "El problema del tráfico en las grandes ciudades es muy grave.", "english": "The traffic problem in big cities is very serious."},
            {"spanish": "A Sakib le gusta mucho la cultura española y le gustan los monumentos históricos.", "english": "Sakib likes Spanish culture very much and likes historic monuments."},
            {"spanish": "Compré este regalo para mi amigo por diez euros en el mercado.", "english": "I bought this gift for my friend for ten euros at the market."}
        ],
        "grammar": {
            "title": "The Master Compendium of 20 A1 Spanish Traps",
            "explanation": "Mastering a language requires not only learning what is right, but being consciously aware of cognitive interference from English and native tongue habits.",
            "rules": [
                "Trap 1: The 'Embarazada' False Friend: *Embarazada* = pregnant. *Avergonzado/a* = embarrassed.",
                "Trap 2: The Greek -MA Words: Nouns ending in *-ma* of Greek origin (*el problema, el tema, el sistema, el idioma, el programa, el planeta*) are MASCULINE.",
                "Trap 3: Truncated Nouns: *La foto* (fotografía) and *la moto* (motocicleta) are FEMININE despite ending in -o.",
                "Trap 4: Hand Gender: *La mano* is feminine (*las manos limpias*).",
                "Trap 5: Tonic A Nouns: Nouns starting with stressed 'a' like *el agua, el águila* take *el* in singular to avoid harsh sound, but remain grammatically feminine (*el agua clara*, *las aguas claras*).",
                "Trap 6: Ser vs Estar Location: Location is ALWAYS *estar* (*Madrid está en España*, never *Madrid es en España*).",
                "Trap 7: Age & Physiological States: Age is held with *tener* (*Tengo 25 años*, never *Soy 25*). Hunger, thirst, cold take *tener* (*Tengo frío*, never *Estoy frío*).",
                "Trap 8: Gustar Plural Agreement: The verb agrees with the thing liked: *Me gusta el café* (singular) vs *Me gustan las manzanas* (plural).",
                "Trap 9: Personal 'A': When the direct object is a specific person or pet, insert 'a': *Veo a María*, *Visito a mis abuelos*.",
                "Trap 10: Por vs Para Price & Recipient: *Pagué 5€ POR el café* (exchange) vs *El regalo es PARA ti* (recipient)."
            ],
            "structures": [
                "Greek Noun Agreement: El [sustantivo -ma] + [adjetivo masculino singular]",
                "Gustar Rule: [Pronombre OI] + gusta (singular) / gustan (plural) + [Sujeto pospuesto]"
            ],
            "examples": [
                {"spanish": "El nuevo sistema informático es eficiente.", "english": "The new computer system is efficient.", "breakdown": "El (masc) + sistema (Greek masc) + eficiente"},
                {"spanish": "Me duelen las dos manos.", "english": "Both my hands hurt.", "breakdown": "Duelen (plural) + las dos manos (fem plural subject)"},
                {"spanish": "El agua mineral está muy fría.", "english": "The mineral water is very cold.", "breakdown": "El agua (singular feminine) + fría (feminine adjective agreement)"},
                {"spanish": "Ayer vi a Carlos en la biblioteca.", "english": "Yesterday I saw Carlos in the library.", "breakdown": "vi (preterite) + a (personal 'a') + Carlos"}
            ],
            "commonMistakes": [
                {"incorrect": "La problema es difícil.", "correct": "El problema es difícil.", "why": "'Problema' is masculine because of its Greek root."},
                {"incorrect": "Estoy 30 años de edad.", "correct": "Tengo 30 años de edad.", "why": "Age is possessed with 'tener' in Spanish, never 'ser' or 'estar'."}
            ],
            "proTip": "Memorize the acronym 'THE MAP' for common Greek masculine words ending in -ma or -pa: Tema, Horóscopa, Esquema, Mapa, Agua, Problema! You will never misgender them again!"
        },
        "conversation": {
            "context": "Professor Carmen conducts a rapid-fire diagnostic drill with Sakib to clean up any remaining subtle errors.",
            "dialogue": [
                {"speaker": "Profª Carmen", "role": "Teacher", "spanish": "Sakib, hoy es el día del gran filtro de errores. Te haré preguntas trampa. ¿Preparado?", "english": "Sakib, today is the day of the great error filter. I'll ask you trick questions. Ready?"},
                {"speaker": "Sakib", "role": "Student", "spanish": "¡Totalmente preparado, profesora! He repasado todos los puntos críticos.", "english": "Totally ready, teacher! I have reviewed all the critical points."},
                {"speaker": "Profª Carmen", "role": "Teacher", "spanish": "Primera trampa: Si alguien te dice que está 'constipado', ¿le das un vaso de agua o le deseas que se mejore del resfriado?", "english": "First trap: If someone tells you they are 'constipado', do you give them a glass of water or wish they recover from their cold?"},
                {"speaker": "Sakib", "role": "Student", "spanish": "Le deseo que se recupere del resfriado, porque 'constipado' significa tener gripe o mocos, no es un problema estomacal.", "english": "I wish they recover from their cold, because 'constipado' means having the flu or a runny nose, it's not a stomach problem."},
                {"speaker": "Profª Carmen", "role": "Teacher", "spanish": "¡Muy bien! Segunda trampa: ¿Cómo describes un problema complicado?", "english": "Very good! Second trap: How do you describe a complicated problem?"},
                {"speaker": "Sakib", "role": "Student", "spanish": "Digo 'el problema complicado', usando el artículo masculino 'el' y el adjetivo terminado en 'o'.", "english": "I say 'el problema complicado', using the masculine article 'el' and the adjective ending in 'o'."},
                {"speaker": "Profª Carmen", "role": "Teacher", "spanish": "¡Impecable! Tercera: ¿'Me gusta los idiomas' o 'Me gustan los idiomas'?", "english": "Impeccable! Third: 'Me gusta los idiomas' or 'Me gustan los idiomas'?"},
                {"speaker": "Sakib", "role": "Student", "spanish": "¡'Me gustan los idiomas', con 'n', porque el sujeto 'los idiomas' es plural!", "english": "'Me gustan los idiomas', with 'n', because the subject 'los idiomas' is plural!"},
                {"speaker": "Profª Carmen", "role": "Teacher", "spanish": "¡Extraordinario, Sakib! Tus reflejos lingüísticos son dignos de un estudiante sobresaliente. Has superado el filtro con matrícula de honor.", "english": "Extraordinary, Sakib! Your linguistic reflexes are worthy of an outstanding student. You have passed the filter with top honors."}
            ],
            "keyPhrases": [
                {"phrase": "Preguntas trampa", "explanation": "'Trick questions / traps' designed to test precision."},
                {"phrase": "Matrícula de honor", "explanation": "The highest Spanish academic grade (Straight A+ with Honors)."},
                {"phrase": "Reflejos lingüísticos", "explanation": "'Linguistic reflexes / instantaneous correct reactions'."}
            ]
        },
        "reading": {
            "title": "La metamorfosis del error: De tropiezo a maestría",
            "passage": "El error no es un síntoma de fracaso; es el motor imprescindible del aprendizaje humano. Ningún políglota en la historia ha alcanzado la fluidez sin haber confundido géneros, pronunciado sonidos con acento extranjero o caído en la trampa de un falso amigo léxico. La diferencia entre el estudiante que se estanca y el que alcanza el dominio estriba en la actitud reflexiva: el estudiante consciente acoge la corrección con curiosidad científica. Al comprender el motivo exacto por el cual se dice 'el problema' en lugar de 'la problema', el cerebro no solo memoriza una regla aislada, sino que asimila la historia etimológica grecolatina que da forma a la lengua de Cervantes. Llegar al Día 55 y contemplar la lista de las veinte trampas clásicas ya no genera incertidumbre, sino una inmensa satisfacción intelectual: aquellas palabras que al principio producían dudas ahora se reconocen al instante como viejas conocidas bajo total control.",
            "translation": "Error is not a symptom of failure; it is the indispensable engine of human learning. No polyglot in history has achieved fluency without having confused genders, pronounced sounds with a foreign accent, or fallen into the trap of a lexical false friend. The difference between the student who stagnates and the one who achieves mastery lies in reflective attitude: the conscious student welcomes correction with scientific curiosity. Upon understanding the exact reason why one says 'el problema' instead of 'la problema', the brain not only memorizes an isolated rule, but assimilates the Greco-Latin etymological history that shapes the language of Cervantes. Arriving at Day 55 and beholding the list of the twenty classic traps no longer generates uncertainty, but immense intellectual satisfaction: those words that at first caused doubt are now instantly recognized as old acquaintances under total control.",
            "questions": [
                {"question": "¿Qué es el error según el texto?", "options": ["Un síntoma de fracaso", "El motor imprescindible del aprendizaje", "Algo vergonzoso", "Una pérdida de tiempo"], "answer": 1, "explanation": "The text calls it 'el motor imprescindible del aprendizaje humano'."},
                {"question": "¿Por qué las palabras que terminan en -ma como 'el problema' son masculinas?", "options": ["Por una regla de 2020", "Por su origen etimológico grecolatino", "Porque son cortas", "Por pura casualidad"], "answer": 1, "explanation": "They are Greek loanwords that retained neuter/masculine gender in Spanish."},
                {"question": "¿Cómo se reconocen las trampas clásicas al llegar al Día 55?", "options": ["Con miedo", "Como viejas conocidas bajo total control", "Con desesperación", "Se olvidan por completo"], "answer": 1, "explanation": "'Se reconocen al instante como viejas conocidas bajo total control'."}
            ]
        },
        "exercises": [
            {
                "id": "d55-ex1",
                "type": "matching",
                "question": "Corrige cada falso amigo con su traducción y sentido real:",
                "options": [
                    "Embarazada -> Pregnant (no avergonzada)",
                    "Constipado -> Resfriado con mocos (no estreñido)",
                    "Éxito -> Triunfo o logro (no salida)",
                    "Asistir -> Ir o presenciar un acto (no ayudar)"
                ],
                "correct": 0,
                "explanation": "Los falsos amigos léxicos son trampas clásicas inglés-español resueltas."
            },
            {
                "id": "d55-ex2",
                "type": "multiple-choice",
                "question": "¿Cuál de las siguientes frases es 100% correcta gramaticalmente?",
                "options": [
                    "Me gustan mucho los idiomas antiguos.",
                    "Me gusta mucho los idiomas antiguos.",
                    "Yo gusto los idiomas antiguos.",
                    "A mí gusta los idiomas antiguos."
                ],
                "correct": 0,
                "explanation": "'Gustan' debe concordar en plural con el sujeto 'los idiomas antiguos'."
            },
            {
                "id": "d55-ex3",
                "type": "sentence-ordering",
                "question": "Ordena las palabras para formar una frase libre de errores de género:",
                "options": ["El", "tema", "del", "examen", "es", "muy", "interesante"],
                "correct": [0, 1, 2, 3, 4, 5, 6],
                "explanation": "'El tema' es masculino; por tanto, 'interesante' y el artículo concuerdan perfectamente."
            },
            {
                "id": "d55-ex4",
                "type": "fill-in-the-blank",
                "question": "Completa con el artículo y adjetivo correcto: 'Bebí _____ agua _____ después de correr.'",
                "options": ["el / fría", "la / fría", "el / frío", "la / frío"],
                "correct": 0,
                "explanation": "'Agua' lleva artículo 'el' en singular por la 'a' tónica, pero mantiene concordancia femenina: 'fría'."
            }
        ],
        "speakingChallenge": {
            "title": "Reto Oral: El Test Anti-Trampas",
            "instructions": "Corrige mentalmente y di en voz alta la forma correcta de estas frases comunes.",
            "prompts": [
                {
                    "question": "Si alguien dice en inglés 'I am 24 years old', ¿cómo lo dices en español sin usar el verbo ser o estar?",
                    "hint": "Usa el verbo 'tener'...",
                    "sampleAnswer": "Tengo veinticuatro años de edad. En español la edad se tiene, nunca se 'es'."
                },
                {
                    "question": "Traduce correctamente: 'I like Spanish movies.' (Cuidado con el plural)",
                    "hint": "Usa: 'Me gustan...'",
                    "sampleAnswer": "Me gustan las películas españolas. Uso 'gustan' porque 'las películas' es un sustantivo plural."
                },
                {
                    "question": "¿Cómo explicas en español que estás avergonzado sin decir la palabra 'embarazado'?",
                    "hint": "Usa: 'Estoy avergonzado por...'",
                    "sampleAnswer": "Estoy muy avergonzado por mi error; sé perfectamente que 'embarazado' significa estar esperando un bebé."
                }
            ]
        },
        "dailyRevision": {
            "quickQuestions": [
                {"q": "¿Por qué decimos 'el agua' pero 'las aguas'?", "a": "Lleva 'el' en singular para evitar el choque de vocales tónicas (el agua), pero es un sustantivo femenino (las aguas frías)."},
                {"q": "¿Qué significa 'asistir a una clase'?", "a": "Significa acudir o estar presente en la clase (attend), no ayudar."},
                {"q": "¿Qué artículo lleva 'mano' y 'problema'?", "a": "'La mano' (femenino) y 'el problema' (masculino)."}
            ],
            "vocabRecall": [
                {"en": "Embarrassed (correct Spanish)", "es": "Avergonzado / Avergonzada"},
                {"en": "Success", "es": "El éxito"},
                {"en": "Exit (the way out)", "es": "La salida"}
            ],
            "grammarRecall": "Recuerda: Ser para identidad, origen y profesiones; Estar para ubicaciones geográficas y estados temporales de ánimo o salud."
        },
        "checklist": [
            "Eliminé los 20 errores y trampas más comunes de A1",
            "Dominé los falsos amigos (embarazada, constipado, éxito, asistir)",
            "Interioricé las excepciones de género (el problema, el tema, la mano, el agua fría)",
            "Consolidé la concordancia plural del verbo gustar",
            "Superé la prueba oral diagnóstica sin titubeos",
            "Completé con éxito todos los ejercicios del Día 55"
        ]
    }
]

if __name__ == "__main__":
    print(f"Loaded {len(stage6_days_51_55)} days for Stage 6 (Days 51-55).")
