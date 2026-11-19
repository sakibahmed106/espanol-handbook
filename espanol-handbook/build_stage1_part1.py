"""
Build Stage 1: Days 1 to 10 (Foundations of Spanish)
"""
import json

stage1_days = [
    {
        "day": 1,
        "stage": 1,
        "title": "Greetings, Goodbyes & Courtesy",
        "subtitle": "First steps into Spanish conversations",
        "goals": [
            "Learn essential Spanish greetings for morning, afternoon, and evening",
            "Express formal and informal goodbyes naturally",
            "Master essential politeness phrases (please, thank you, you're welcome)",
            "Pronounce greetings with authentic Castilian rhythm and silent 'h'"
        ],
        "bengaliNote": "In Spanish, 'h' in '¡Hola!' is 100% silent (pronounced 'ola'). Like Bangla 'নমস্কার' or 'সালাম', greetings change depending on the time of day, and politeness is deeply valued in Spain.",
        "vocabulary": [
            {"word": "¡Hola!", "translation": "Hello / Hi", "pos": "interjection", "gender": None, "example": "¡Hola! ¿Cómo estás?", "exampleTranslation": "Hello! How are you?"},
            {"word": "Buenos días", "translation": "Good morning", "pos": "phrase", "gender": "masculine plural", "example": "Buenos días, señor López.", "exampleTranslation": "Good morning, Mr. Lopez."},
            {"word": "Buenas tardes", "translation": "Good afternoon", "pos": "phrase", "gender": "feminine plural", "example": "Buenas tardes a todos.", "exampleTranslation": "Good afternoon to everyone."},
            {"word": "Buenas noches", "translation": "Good evening / Good night", "pos": "phrase", "gender": "feminine plural", "example": "Buenas noches, hasta mañana.", "exampleTranslation": "Good night, see you tomorrow."},
            {"word": "Por favor", "translation": "Please", "pos": "phrase", "gender": None, "example": "Un café, por favor.", "exampleTranslation": "A coffee, please."},
            {"word": "Gracias", "translation": "Thank you", "pos": "interjection", "gender": None, "example": "Muchas gracias por tu ayuda.", "exampleTranslation": "Thank you very much for your help."},
            {"word": "De nada", "translation": "You're welcome", "pos": "phrase", "gender": None, "example": "—Gracias. —De nada.", "exampleTranslation": "—Thank you. —You're welcome."},
            {"word": "Adiós", "translation": "Goodbye", "pos": "interjection", "gender": None, "example": "Adiós, buen viaje.", "exampleTranslation": "Goodbye, have a good trip."},
            {"word": "Hasta luego", "translation": "See you later", "pos": "phrase", "gender": None, "example": "Hasta luego, amigo.", "exampleTranslation": "See you later, my friend."},
            {"word": "Hasta pronto", "translation": "See you soon", "pos": "phrase", "gender": None, "example": "Nos vemos, hasta pronto.", "exampleTranslation": "See each other, see you soon."}
        ],
        "sentences": [
            {"spanish": "¡Hola! Buenos días, ¿qué tal?", "english": "Hello! Good morning, how are things?"},
            {"spanish": "Muchas gracias por todo.", "english": "Thank you very much for everything."},
            {"spanish": "De nada, es un placer.", "english": "You're welcome, it is a pleasure."},
            {"spanish": "Hasta mañana, que descanses.", "english": "See you tomorrow, rest well."},
            {"spanish": "Perdón, ¿dónde está el baño?", "english": "Excuse me, where is the bathroom?"},
            {"spanish": "Disculpe, una pregunta por favor.", "english": "Pardon me, a question please."}
        ],
        "grammar": {
            "title": "Time-based Greetings & Politeness Formulas",
            "explanation": "Spanish greetings are plural! Notice *Buenos días* (masculine plural, *el día* is masculine) versus *Buenas tardes* and *Buenas noches* (feminine plural, *la tarde* and *la noche* are feminine). In Spanish culture, entering any shop, elevator, or café requires a warm greeting.",
            "rules": [
                "Morning greeting: 'Buenos días' is used from sunrise until lunchtime (typically 2:00 PM in Spain).",
                "Afternoon greeting: 'Buenas tardes' is used from around 2:00 PM until nightfall (approx. 8:30 PM).",
                "Night greeting: 'Buenas noches' serves as both 'Good evening' (arrival) and 'Good night' (departure).",
                "Punctuation rule: Every Spanish exclamation begins with inverted ¡ and ends with !."
            ],
            "structures": [
                "Greeting + Time Formula: ¡Hola! + Buenos días / Buenas tardes",
                "Polite Request: [Item / Request] + por favor",
                "Gratitude Response: Gracias / Muchas gracias -> De nada"
            ],
            "examples": [
                {"spanish": "¡Hola! Buenas tardes.", "english": "Hello! Good afternoon."},
                {"spanish": "Un vaso de agua, por favor.", "english": "A glass of water, please."},
                {"spanish": "Muchas gracias, señor.", "english": "Thank you very much, sir."},
                {"spanish": "Hasta luego, nos vemos.", "english": "See you later, we'll see each other."}
            ],
            "commonMistakes": [
                {"wrong": "Buen día (in Spain)", "right": "Buenos días", "explanation": "While 'Buen día' is heard in Latin America, Spain standard usage is strictly plural 'Buenos días'."},
                {"wrong": "Buenos tardes", "right": "Buenas tardes", "explanation": "'Tarde' is feminine, so the adjective must be feminine: 'buenas'."},
                {"wrong": "Pronouncing the 'H' in Hola", "right": "Say 'OH-lah'", "explanation": "The letter 'H' is always silent in Spanish."}
            ],
            "proTip": "In Spain, if you want a quick, casual, all-day greeting for friends or cashiers, simply say '¡Buenas!' (Good day / Hi!)."
        },
        "conversation": {
            "title": "Meeting at a Madrid Café",
            "context": "Mateo meets his neighbor Elena in a local café on Gran Vía, Madrid.",
            "dialogue": [
                {"speaker": "Mateo", "role": "Local student", "spanish": "¡Hola, Elena! Buenos días.", "english": "Hello, Elena! Good morning."},
                {"speaker": "Elena", "role": "Architect", "spanish": "¡Buenos días, Mateo! ¿Qué tal estás?", "english": "Good morning, Mateo! How are you doing?"},
                {"speaker": "Mateo", "role": "Local student", "spanish": "Muy bien, gracias. ¿Y tú?", "english": "Very well, thank you. And you?"},
                {"speaker": "Elena", "role": "Architect", "spanish": "Bien también. Bueno, me voy. ¡Hasta luego!", "english": "Good too. Well, I'm heading out. See you later!"},
                {"speaker": "Mateo", "role": "Local student", "spanish": "¡Hasta pronto, Elena! Que tengas buen día.", "english": "See you soon, Elena! Have a good day."}
            ],
            "keyPhrases": [
                {"phrase": "¿Qué tal estás?", "explanation": "A very friendly, standard way to ask 'How are you?' combining ¿Qué tal? (How's it going?) with estás (are you)."},
                {"phrase": "Muy bien, gracias", "explanation": "The golden polite response to any inquiry about your state of being."},
                {"phrase": "¿Y tú?", "explanation": "'And you?' — the quickest way to bounce a question back to an informal peer."}
            ]
        },
        "reading": {
            "title": "La cortesía en España (Courtesy in Spain)",
            "passage": "En España, la cortesía es muy importante en la vida diaria. Cuando una persona entra en una tienda o en una cafetería, siempre dice: «¡Hola! Buenos días» o «Buenas tardes». Cuando pide algo, siempre añade «por favor». Y cuando recibe su comida o su compra, dice «muchas gracias». Para despedirse, la gente suele decir «hasta luego» o «adiós». Estas palabras sencillas abren todas las puertas.",
            "translation": "In Spain, courtesy is very important in daily life. When a person enters a shop or a cafeteria, they always say: 'Hello! Good morning' or 'Good afternoon'. When they ask for something, they always add 'please'. And when they receive their food or purchase, they say 'thank you very much'. To say goodbye, people usually say 'see you later' or 'goodbye'. These simple words open all doors.",
            "questions": [
                {"question": "¿Qué dice una persona al entrar en una tienda por la mañana?", "options": ["Adiós", "Buenos días", "Buenas noches", "De nada"], "answer": 1, "explanation": "Morning greeting upon entering is 'Buenos días'."},
                {"question": "¿Qué palabra se usa siempre al pedir algo?", "options": ["Gracias", "Por favor", "Hola", "Hasta pronto"], "answer": 1, "explanation": "'Por favor' means 'please' and accompanies every polite request."},
                {"question": "¿Cuál es una forma común de despedirse?", "options": ["Por favor", "Hasta luego", "Buenas tardes", "Perdón"], "answer": 1, "explanation": "'Hasta luego' is the standard goodbye expression."}
            ]
        },
        "exercises": [
            {
                "id": "d1-ex1",
                "type": "multiple-choice",
                "prompt": "How do you say 'Good afternoon' in Spanish?",
                "options": ["Buenos días", "Buenas tardes", "Buenas noches", "Hasta luego"],
                "correct": 1,
                "explanation": "'Buenas tardes' is feminine plural for good afternoon."
            },
            {
                "id": "d1-ex2",
                "type": "fill-in",
                "prompt": "Complete the polite response: —Muchas gracias. —De ______.",
                "options": ["nada", "favor", "pronto", "hola"],
                "correct": 0,
                "explanation": "'De nada' means 'You are welcome'."
            },
            {
                "id": "d1-ex3",
                "type": "multiple-choice",
                "prompt": "Which letter is completely silent in '¡Hola!'?",
                "options": ["L", "O", "H", "A"],
                "correct": 2,
                "explanation": "The letter 'H' is always completely silent in Spanish."
            },
            {
                "id": "d1-ex4",
                "type": "translation",
                "prompt": "Translate to Spanish: 'A coffee, please.'",
                "options": ["Un café, por favor.", "Un café, gracias.", "El café, de nada.", "Buenas noches café."],
                "correct": 0,
                "explanation": "'Un café, por favor' is the standard polite coffee order."
            }
        ],
        "speakingChallenge": [
            {"prompt": "Greet a shopkeeper at 10:00 AM and ask for water politely.", "hint": "Use 'Buenos días' and 'por favor'.", "sampleAnswer": "¡Buenos días! Un agua, por favor."},
            {"prompt": "Someone says 'Muchas gracias' to you. Respond naturally.", "hint": "Use 'You're welcome'.", "sampleAnswer": "De nada. / Es un placer."},
            {"prompt": "Say goodbye to a friend whom you will see later today.", "hint": "Use 'See you later'.", "sampleAnswer": "¡Hasta luego! Nos vemos."}
        ],
        "dailyRevision": {
            "quickQuestions": [
                "What is the difference between 'Buenos días' and 'Buenas tardes'?",
                "Why does Spanish use inverted exclamation marks (¡)?"
            ],
            "grammarRecall": "All Spanish time-greetings are in the plural form (*días*, *tardes*, *noches*).",
            "vocabRecall": ["¡Hola!", "Por favor", "Gracias", "De nada", "Adiós"]
        },
        "checklist": [
            "Mastered time greetings (días, tardes, noches)",
            "Pronounced '¡Hola!' with silent 'h'",
            "Used 'por favor' and 'de nada' in requests",
            "Read aloud the café dialogue with Elena and Mateo",
            "Completed all 4 interactive exercises",
            "Practiced the 3 speaking prompts out loud"
        ]
    },
    {
        "day": 2,
        "stage": 1,
        "title": "Introductions & Personal Information",
        "subtitle": "Introducing yourself, your name, origin, and age",
        "goals": [
            "Introduce your name using 'Me llamo...' and 'Mi nombre es...'",
            "State your nationality and origin with 'Soy de...'",
            "State your age correctly using the verb 'Tener' (not 'to be')",
            "Ask another person their name and origin politely"
        ],
        "bengaliNote": "In Spanish, you don't say 'I am 25 years old'. You say 'I have 25 years' (*Tengo 25 años*). Notice the letter 'ñ' in *años* — without the tilde, *ano* means something completely different!",
        "vocabulary": [
            {"word": "Me llamo", "translation": "My name is (literally: I call myself)", "pos": "phrase", "gender": None, "example": "Me llamo Sakib.", "exampleTranslation": "My name is Sakib."},
            {"word": "¿Cómo te llamas?", "translation": "What is your name? (informal)", "pos": "phrase", "gender": None, "example": "¿Cómo te llamas tú?", "exampleTranslation": "What is your name?"},
            {"word": "Mucho gusto", "translation": "Nice to meet you (literally: much pleasure)", "pos": "phrase", "gender": None, "example": "—Soy María. —Mucho gusto.", "exampleTranslation": "—I'm Maria. —Nice to meet you."},
            {"word": "Encantado / Encantada", "translation": "Delighted / Pleased to meet you", "pos": "adjective", "gender": "masculine / feminine", "example": "Encantado de conocerte.", "exampleTranslation": "Pleased to meet you."},
            {"word": "Soy de...", "translation": "I am from...", "pos": "phrase", "gender": None, "example": "Soy de Bangladés.", "exampleTranslation": "I am from Bangladesh."},
            {"word": "¿De dónde eres?", "translation": "Where are you from? (informal)", "pos": "phrase", "gender": None, "example": "Hola, ¿de dónde eres?", "exampleTranslation": "Hello, where are you from?"},
            {"word": "Tengo ... años", "translation": "I am ... years old (literally: I have ... years)", "pos": "phrase", "gender": None, "example": "Tengo veinticinco años.", "exampleTranslation": "I am twenty-five years old."},
            {"word": "El estudiante / La estudiante", "translation": "The student", "pos": "noun", "gender": "masculine / feminine", "example": "Soy estudiante de español.", "exampleTranslation": "I am a Spanish student."},
            {"word": "Vivo en...", "translation": "I live in...", "pos": "verb phrase", "gender": None, "example": "Vivo en Madrid.", "exampleTranslation": "I live in Madrid."},
            {"word": "¿Y usted?", "translation": "And you? (formal)", "pos": "phrase", "gender": None, "example": "Yo soy de España, ¿y usted?", "exampleTranslation": "I am from Spain, and you (formal)?"}
        ],
        "sentences": [
            {"spanish": "Me llamo Sakib y soy de Bangladés.", "english": "My name is Sakib and I am from Bangladesh."},
            {"spanish": "Mucho gusto en conocerte.", "english": "Pleased to meet you."},
            {"spanish": "Tengo veinticuatro años y soy estudiante.", "english": "I am twenty-four years old and I am a student."},
            {"spanish": "Vivo en una ciudad muy bonita.", "english": "I live in a very beautiful city."},
            {"spanish": "¿Cómo se llama usted, señor?", "english": "What is your name, sir? (formal)"},
            {"spanish": "Es un placer conocerte.", "english": "It is a pleasure to meet you."}
        ],
        "grammar": {
            "title": "Introducing Identity: Llamarse, Ser & Tener",
            "explanation": "To introduce yourself in Spanish, you use three distinct verbs depending on whether you are stating your name, your origin, or your age.",
            "rules": [
                "Name: Use 'Me llamo + [Name]' (reflexive verb llamarse: I call myself).",
                "Origin / Nationality: Use 'Soy de + [Country / City]' (verb ser: to be).",
                "Age: ALWAYS use 'Tengo + [Number] + años' (verb tener: to have). NEVER say 'Soy ... años'!",
                "Encantado vs. Encantada: If you are male, say 'Encantado'. If female, say 'Encantada'."
            ],
            "structures": [
                "Name formula: Me llamo [Name] / Mi nombre es [Name]",
                "Origin formula: Soy de [Country / City]",
                "Age formula: Tengo [Number] años"
            ],
            "examples": [
                {"spanish": "Me llamo Carlos.", "english": "My name is Carlos."},
                {"spanish": "Soy de España.", "english": "I am from Spain."},
                {"spanish": "Tengo treinta años.", "english": "I am thirty years old."},
                {"spanish": "Encantado de conocerte.", "english": "Delighted to meet you."}
            ],
            "commonMistakes": [
                {"wrong": "Soy 20 años", "right": "Tengo 20 años", "explanation": "In Spanish, age is possessed using 'tener' (to have), not 'ser' (to be)."},
                {"wrong": "Me llamo es Sakib", "right": "Me llamo Sakib (or: Mi nombre es Sakib)", "explanation": "'Me llamo' already means 'I call myself', so adding 'es' (is) creates a double verb error."}
            ],
            "proTip": "Sakib, when a native Spaniard meets you, a firm handshake with 'Mucho gusto' or 'Encantado' is standard."
        },
        "conversation": {
            "title": "First Day at Language Class",
            "context": "Sakib meets Lucía in their Spanish language academy in Madrid.",
            "dialogue": [
                {"speaker": "Lucía", "role": "Teacher / Classmate", "spanish": "¡Hola! Buenos días. ¿Cómo te llamas?", "english": "Hello! Good morning. What is your name?"},
                {"speaker": "Sakib", "role": "Student", "spanish": "¡Hola! Me llamo Sakib. ¿Y tú?", "english": "Hello! My name is Sakib. And you?"},
                {"speaker": "Lucía", "role": "Teacher / Classmate", "spanish": "Me llamo Lucía. Mucho gusto, Sakib.", "english": "My name is Lucia. Nice to meet you, Sakib."},
                {"speaker": "Sakib", "role": "Student", "spanish": "Encantado, Lucía. ¿De dónde eres?", "english": "Pleased to meet you, Lucia. Where are you from?"},
                {"speaker": "Lucía", "role": "Teacher / Classmate", "spanish": "Soy de Sevilla, en el sur de España. ¿Y tú?", "english": "I am from Seville, in the south of Spain. And you?"},
                {"speaker": "Sakib", "role": "Student", "spanish": "Soy de Bangladés. Ahora vivo en Madrid para aprender español.", "english": "I am from Bangladesh. Now I live in Madrid to learn Spanish."},
                {"speaker": "Lucía", "role": "Teacher / Classmate", "spanish": "¡Qué bien! ¡Bienvenido a España!", "english": "How wonderful! Welcome to Spain!"}
            ],
            "keyPhrases": [
                {"phrase": "Mucho gusto", "explanation": "Universal polite expression for 'Nice to meet you'."},
                {"phrase": "Encantado", "explanation": "Short for 'I am enchanted/delighted to meet you'."},
                {"phrase": "¡Qué bien!", "explanation": "Extremely common conversational phrase meaning 'How great!' or 'That's awesome!'"}
            ]
        },
        "reading": {
            "title": "Un nuevo estudiante en Madrid",
            "passage": "Sakib es un estudiante entusiasta. Es de Bangladés y tiene veinticuatro años. Ahora vive en Madrid. Todos los días va a la escuela de idiomas por la mañana. En la clase saluda a sus compañeros: «¡Buenos días! Me llamo Sakib y tengo muchas ganas de aprender español». Sus profesores son amables y la ciudad de Madrid es hermosa y vibrante.",
            "translation": "Sakib is an enthusiastic student. He is from Bangladesh and is twenty-four years old. Now he lives in Madrid. Every day he goes to the language school in the morning. In class he greets his classmates: 'Good morning! My name is Sakib and I am very eager to learn Spanish.' His teachers are kind and the city of Madrid is beautiful and vibrant.",
            "questions": [
                {"question": "¿De dónde es Sakib?", "options": ["De España", "De Bangladés", "De México", "De Italia"], "answer": 1, "explanation": "Sakib is from Bangladesh ('Soy de Bangladés')."},
                {"question": "¿Dónde vive Sakib ahora?", "options": ["En Barcelona", "En Sevilla", "En Madrid", "En Valencia"], "answer": 2, "explanation": "He lives in Madrid ('Ahora vive en Madrid')."},
                {"question": "¿Qué dice Sakib en clase?", "options": ["Adiós a todos", "Me llamo Sakib", "Tengo frío", "No me gusta el café"], "answer": 1, "explanation": "He introduces himself: 'Me llamo Sakib'."}
            ]
        },
        "exercises": [
            {
                "id": "d2-ex1",
                "type": "fill-in",
                "prompt": "Complete with the correct verb: Yo ______ Sakib. (My name is Sakib)",
                "options": ["me llamo", "soy de", "tengo", "vivo"],
                "correct": 0,
                "explanation": "'Me llamo Sakib' is the correct expression for introducing your name."
            },
            {
                "id": "d2-ex2",
                "type": "multiple-choice",
                "prompt": "How do you state your age correctly in Spanish?",
                "options": ["Soy 25 años", "Estoy 25 años", "Tengo 25 años", "Hago 25 años"],
                "correct": 2,
                "explanation": "Spanish uses the verb 'tener' (to have): 'Tengo 25 años'."
            },
            {
                "id": "d2-ex3",
                "type": "multiple-choice",
                "prompt": "If a male speaker says 'Pleased to meet you', he should say:",
                "options": ["Encantada", "Encantado", "Encanto", "Encantador"],
                "correct": 1,
                "explanation": "Adjectives agree with the speaker's gender: male speakers say 'Encantado'."
            },
            {
                "id": "d2-ex4",
                "type": "translation",
                "prompt": "Translate: 'Where are you from?' (informal)",
                "options": ["¿Cómo te llamas?", "¿De dónde eres?", "¿Dónde vives?", "¿Cuántos años tienes?"],
                "correct": 1,
                "explanation": "'¿De dónde eres?' means 'Where are you from?'."
            }
        ],
        "speakingChallenge": [
            {"prompt": "Say your full name in Spanish.", "hint": "Use 'Me llamo...'", "sampleAnswer": "Me llamo Sakib Ahmed."},
            {"prompt": "State your country of origin.", "hint": "Use 'Soy de...'", "sampleAnswer": "Soy de Bangladés."},
            {"prompt": "Say your age and current city.", "hint": "Use 'Tengo ... años' and 'Vivo en...'", "sampleAnswer": "Tengo veinticuatro años y vivo en Madrid."}
        ],
        "dailyRevision": {
            "quickQuestions": [
                "Why can't you say 'Soy 25 años' in Spanish?",
                "What is the difference between 'Encantado' and 'Encantada'?"
            ],
            "grammarRecall": "Name = Me llamo | Origin = Soy de | Age = Tengo ... años.",
            "vocabRecall": ["Me llamo", "¿Cómo te llamas?", "Mucho gusto", "Soy de...", "Tengo ... años"]
        },
        "checklist": [
            "Introduced my name using 'Me llamo'",
            "Stated my origin using 'Soy de'",
            "Stated my age with 'Tengo ... años'",
            "Distinguished between Encantado (male) and Encantada (female)",
            "Solved all 4 practice exercises correctly",
            "Completed the 3 speaking prompts out loud"
        ]
    },
    {
        "day": 3,
        "stage": 1,
        "title": "Numbers 0–30 & Counting",
        "subtitle": "Mastering numbers, counting objects, and phone numbers",
        "goals": [
            "Count flawlessly from 0 to 30 in Spanish",
            "Understand the spelling patterns of numbers 16–29 (dieciséis, veintiuno...)",
            "Ask for and give prices, quantities, and phone numbers",
            "Distinguish between 'uno', 'un', and 'una' when counting objects"
        ],
        "bengaliNote": "Just like counting in Bangla (এক, দুই, তিন...), Spanish numbers from 0 to 15 have distinct unique words (*cero, uno, dos, tres...*), while 16 to 29 blend into single words (*dieciséis, veintiuno*).",
        "vocabulary": [
            {"word": "Cero, Uno, Dos, Tres", "translation": "0, 1, 2, 3", "pos": "number", "gender": None, "example": "Tengo tres libros.", "exampleTranslation": "I have three books."},
            {"word": "Cuatro, Cinco, Seis", "translation": "4, 5, 6", "pos": "number", "gender": None, "example": "Son las cuatro de la tarde.", "exampleTranslation": "It is four in the afternoon."},
            {"word": "Siete, Ocho, Nueve, Diez", "translation": "7, 8, 9, 10", "pos": "number", "gender": None, "example": "Diez euros, por favor.", "exampleTranslation": "Ten euros, please."},
            {"word": "Once, Doce, Trece, Catorce, Quince", "translation": "11, 12, 13, 14, 15", "pos": "number", "gender": None, "example": "Hay quince estudiantes en clase.", "exampleTranslation": "There are fifteen students in class."},
            {"word": "Dieciséis a Diecinueve", "translation": "16 to 19 (10 + number)", "pos": "number", "gender": None, "example": "Tengo dieciocho años.", "exampleTranslation": "I am eighteen years old."},
            {"word": "Veinte", "translation": "20", "pos": "number", "gender": None, "example": "Cuesta veinte euros.", "exampleTranslation": "It costs twenty euros."},
            {"word": "Veintiuno a Veintinueve", "translation": "21 to 29 (veinti + number)", "pos": "number", "gender": None, "example": "El número veinticinco.", "exampleTranslation": "The number twenty-five."},
            {"word": "Treinta", "translation": "30", "pos": "number", "gender": None, "example": "Son treinta días.", "exampleTranslation": "It is thirty days."},
            {"word": "¿Cuánto cuesta?", "translation": "How much does it cost?", "pos": "phrase", "gender": None, "example": "¿Cuánto cuesta este café?", "exampleTranslation": "How much does this coffee cost?"},
            {"word": "El número de teléfono", "translation": "The telephone number", "pos": "noun", "gender": "masculine", "example": "¿Cuál es tu número de teléfono?", "exampleTranslation": "What is your telephone number?"}
        ],
        "sentences": [
            {"spanish": "¿Cuánto cuesta el billete de metro?", "english": "How much does the subway ticket cost?"},
            {"spanish": "Cuesta dos euros con cincuenta céntimos.", "english": "It costs two euros and fifty cents."},
            {"spanish": "¿Cuál es tu número de teléfono?", "english": "What is your telephone number?"},
            {"spanish": "Mi número es el seis, cuatro, dos, ocho...", "english": "My number is six, four, two, eight..."},
            {"spanish": "Tengo veintidós años.", "english": "I am twenty-two years old."},
            {"spanish": "Hay tres personas en la mesa.", "english": "There are three people at the table."}
        ],
        "grammar": {
            "title": "Number Patterns 0–30 & 'Uno' vs. 'Un' / 'Una'",
            "explanation": "Spanish numbers follow very specific orthographic rules that make them easy to master once you understand the pattern.",
            "rules": [
                "Numbers 0–15 are unique single words: cero, uno, dos, tres, cuatro, cinco, seis, siete, ocho, nueve, diez, once, doce, trece, catorce, quince.",
                "Numbers 16–19 merge 'diez y [number]' into one word: dieciséis, diecisiete, dieciocho, diecinueve.",
                "Numbers 21–29 merge 'veinte y [number]' into 'veinti-' as a single word: veintiuno, veintidós, veintitrés, veinticuatro, veinticinco, veintiséis, veintisiete, veintiocho, veintinueve.",
                "Uno drops the -o before a masculine noun: 'un libro' (not 'uno libro'). Before a feminine noun, it becomes 'una': 'una mesa'."
            ],
            "structures": [
                "Counting: uno, dos, tres...",
                "Before Masculine Noun: un + [Noun] (un café, un euro)",
                "Before Feminine Noun: una + [Noun] (una cerveza, una manzana)"
            ],
            "examples": [
                {"spanish": "Tengo un hermano y una hermana.", "english": "I have one brother and one sister."},
                {"spanish": "La habitación veintiuno.", "english": "Room twenty-one."},
                {"spanish": "Quince euros con cincuenta.", "english": "Fifteen euros and fifty."},
                {"spanish": "¿Cuántos años tienes? —Tengo veintiséis.", "english": "How old are you? —I am twenty-six."}
            ],
            "commonMistakes": [
                {"wrong": "Veinte y uno", "right": "Veintiuno", "explanation": "Numbers 21–29 are written as a single combined word with 'veinti-', never separated with 'y'."},
                {"wrong": "Uno euro", "right": "Un euro", "explanation": "'Uno' shortens to 'un' directly before any masculine noun."}
            ],
            "proTip": "In Spain, phone numbers are 9 digits long, usually starting with 6 or 7 for mobiles, and 9 for landlines. Spaniards usually dictate them in pairs (e.g. 642 - 18 - 25 - 30)."
        },
        "conversation": {
            "title": "Buying Metro Tickets in Madrid",
            "context": "Sakib is at the Sol metro ticket office in Madrid.",
            "dialogue": [
                {"speaker": "Sakib", "role": "Traveler", "spanish": "¡Hola! Buenos días.", "english": "Hello! Good morning."},
                {"speaker": "Taquillero", "role": "Metro clerk", "spanish": "Buenos días. ¿Qué desea?", "english": "Good morning. What would you like?"},
                {"speaker": "Sakib", "role": "Traveler", "spanish": "Dos billetes sencillos para el metro, por favor.", "english": "Two single tickets for the metro, please."},
                {"speaker": "Taquillero", "role": "Metro clerk", "spanish": "Muy bien. Son tres euros.", "english": "Very well. That is three euros."},
                {"speaker": "Sakib", "role": "Traveler", "spanish": "Aquí tiene cinco euros.", "english": "Here is five euros."},
                {"speaker": "Taquillero", "role": "Metro clerk", "spanish": "Muchas gracias. Su cambio: dos euros. ¡Buen viaje!", "english": "Thank you very much. Your change: two euros. Have a good trip!"},
                {"speaker": "Sakib", "role": "Traveler", "spanish": "¡Muchas gracias! Hasta luego.", "english": "Thank you very much! See you later."}
            ],
            "keyPhrases": [
                {"phrase": "¿Qué desea?", "explanation": "Polite formula used by clerks meaning 'What would you desire / like?'"},
                {"phrase": "Aquí tiene", "explanation": "'Here you have' / 'Here you go' when handing money or an item to someone."},
                {"phrase": "Su cambio", "explanation": "'Your change' (money returned)."}
            ]
        },
        "reading": {
            "title": "La clase de español",
            "passage": "En la clase de español de Sakib hay quince estudiantes: siete chicos y ocho chicas. La profesora se llama Carmen y tiene treinta años. En el aula hay veinte mesas y veintiuna sillas. La clase dura dos horas, desde las diez hasta las doce de la mañana. Los estudiantes practican los números del cero al treinta todos los días.",
            "translation": "In Sakib's Spanish class there are fifteen students: seven boys and eight girls. The teacher is called Carmen and is thirty years old. In the classroom there are twenty tables and twenty-one chairs. The class lasts two hours, from ten until twelve in the morning. The students practice the numbers from zero to thirty every day.",
            "questions": [
                {"question": "¿Cuántos estudiantes hay en la clase?", "options": ["Diez", "Quince", "Veinte", "Treinta"], "answer": 1, "explanation": "There are fifteen students ('hay quince estudiantes')."},
                {"question": "¿Cuántos años tiene la profesora Carmen?", "options": ["Veinticinco", "Veinte", "Treinta", "Dieciocho"], "answer": 2, "explanation": "Carmen has 30 years ('tiene treinta años')."},
                {"question": "¿Cuántas horas dura la clase?", "options": ["Una hora", "Dos horas", "Tres horas", "Cuatro horas"], "answer": 1, "explanation": "The class lasts two hours ('dura dos horas')."}
            ]
        },
        "exercises": [
            {
                "id": "d3-ex1",
                "type": "multiple-choice",
                "prompt": "What is the correct Spanish spelling for 23?",
                "options": ["Veinte y tres", "Veintitrés", "Venti tres", "Treinta y dos"],
                "correct": 1,
                "explanation": "21-29 are spelled as a single word: 'veintitrés' (with an accent mark on the e)."
            },
            {
                "id": "d3-ex2",
                "type": "fill-in",
                "prompt": "Complete: Tengo ______ café, por favor. (one)",
                "options": ["un", "uno", "una", "unos"],
                "correct": 0,
                "explanation": "'Uno' drops the -o before a masculine noun: 'un café'."
            },
            {
                "id": "d3-ex3",
                "type": "multiple-choice",
                "prompt": "How do you say 15 in Spanish?",
                "options": ["Diez y cinco", "Quince", "Catorce", "Once"],
                "correct": 1,
                "explanation": "15 is 'quince'."
            },
            {
                "id": "d3-ex4",
                "type": "translation",
                "prompt": "Translate: 'How much does it cost?'",
                "options": ["¿Cómo te llamas?", "¿Cuánto cuesta?", "¿Dónde está?", "¿Qué tal estás?"],
                "correct": 1,
                "explanation": "'¿Cuánto cuesta?' asks for price."
            }
        ],
        "speakingChallenge": [
            {"prompt": "Count aloud from 10 to 20 in Spanish.", "hint": "Diez, once, doce...", "sampleAnswer": "Diez, once, doce, trece, catorce, quince, dieciséis, diecisiete, dieciocho, diecinueve, veinte."},
            {"prompt": "Say your phone number digit by digit in Spanish.", "hint": "Mi número es...", "sampleAnswer": "Mi número es cero, uno, siete, ocho..."},
            {"prompt": "Ask a cashier how much a bottle of water costs.", "hint": "¿Cuánto cuesta...", "sampleAnswer": "Por favor, ¿cuánto cuesta el agua?"}
        ],
        "dailyRevision": {
            "quickQuestions": [
                "What happens to 'uno' when placed in front of a masculine noun?",
                "How are numbers between 21 and 29 spelled?"
            ],
            "grammarRecall": "16-19 = dieciséis... | 21-29 = veintiuno... | un libro, una mesa.",
            "vocabRecall": ["Cero", "Diez", "Quince", "Veinte", "Treinta", "¿Cuánto cuesta?"]
        },
        "checklist": [
            "Counted from 0 to 30 smoothly",
            "Understood the spelling rule for 16-19 and 21-29",
            "Applied 'un' vs 'una' correctly to masculine and feminine nouns",
            "Read aloud the Metro station conversation",
            "Passed all 4 number exercises",
            "Dictated phone numbers aloud in Spanish"
        ]
    },
    {
        "day": 4,
        "stage": 1,
        "title": "Days, Months, Seasons & Dates",
        "subtitle": "Talking about time, planning your week, and stating dates",
        "goals": [
            "Name the 7 days of the week and notice they are not capitalized in Spanish",
            "Name the 12 months of the year and 4 seasons",
            "Form complete dates using the pattern: 'el [number] de [month]'",
            "Use temporal words: hoy, ayer, mañana, fin de semana"
        ],
        "bengaliNote": "In Spanish, the days of the week always take the masculine article 'el' or 'los' to express 'on Monday' (*el lunes*) or 'on Mondays' (*los lunes*). Never say 'en lunes'!",
        "vocabulary": [
            {"word": "Lunes, Martes, Miércoles", "translation": "Monday, Tuesday, Wednesday", "pos": "noun", "gender": "masculine", "example": "El lunes tengo clase de español.", "exampleTranslation": "On Monday I have Spanish class."},
            {"word": "Jueves, Viernes", "translation": "Thursday, Friday", "pos": "noun", "gender": "masculine", "example": "El viernes salgo con mis amigos.", "exampleTranslation": "On Friday I go out with my friends."},
            {"word": "Sábado, Domingo", "translation": "Saturday, Sunday", "pos": "noun", "gender": "masculine", "example": "El sábado descanso en casa.", "exampleTranslation": "On Saturday I rest at home."},
            {"word": "El fin de semana", "translation": "The weekend", "pos": "noun", "gender": "masculine", "example": "¡Buen fin de semana!", "exampleTranslation": "Have a good weekend!"},
            {"word": "Hoy, Ayer, Mañana", "translation": "Today, Yesterday, Tomorrow", "pos": "adverb", "gender": None, "example": "Hoy es lunes y mañana es martes.", "exampleTranslation": "Today is Monday and tomorrow is Tuesday."},
            {"word": "Enero, Febrero, Marzo, Abril", "translation": "January, February, March, April", "pos": "noun", "gender": "masculine", "example": "Mi cumpleaños es en marzo.", "exampleTranslation": "My birthday is in March."},
            {"word": "Mayo, Junio, Julio, Agosto", "translation": "May, June, July, August", "pos": "noun", "gender": "masculine", "example": "En agosto hace mucho calor.", "exampleTranslation": "In August it is very hot."},
            {"word": "Septiembre, Octubre, Noviembre, Diciembre", "translation": "September, October, November, December", "pos": "noun", "gender": "masculine", "example": "Diciembre es el último mes del año.", "exampleTranslation": "December is the last month of the year."},
            {"word": "La primavera, El verano, El otoño, El invierno", "translation": "Spring, Summer, Autumn, Winter", "pos": "noun", "gender": "mixed", "example": "Me gusta la primavera.", "exampleTranslation": "I like spring."},
            {"word": "¿Qué día es hoy?", "translation": "What day is today?", "pos": "phrase", "gender": None, "example": "¿Qué día es hoy? —Hoy es miércoles.", "exampleTranslation": "What day is today? —Today is Wednesday."}
        ],
        "sentences": [
            {"spanish": "Hoy es lunes, doce de octubre.", "english": "Today is Monday, October twelfth."},
            {"spanish": "¿Cuándo es tu cumpleaños?", "english": "When is your birthday?"},
            {"spanish": "Mi cumpleaños es el quince de mayo.", "english": "My birthday is on May fifteenth."},
            {"spanish": "Los sábados no trabajo, descanso.", "english": "On Saturdays I do not work, I rest."},
            {"spanish": "¿Qué planes tienes para el fin de semana?", "english": "What plans do you have for the weekend?"},
            {"spanish": "Hasta el lunes, que tengas buen fin de semana.", "english": "See you Monday, have a great weekend."}
        ],
        "grammar": {
            "title": "Date Patterns & Days of the Week Rules",
            "explanation": "Expressing dates and days in Spanish follows strict grammatical conventions that differ from English.",
            "rules": [
                "Lowercase rule: Unlike English, days of the week and months are NOT capitalized in Spanish unless starting a sentence (e.g. lunes, enero).",
                "Saying 'On [Day]': Use 'el' for singular and 'los' for plural. NEVER say 'en lunes'!",
                "Plural days: Days ending in -s (lunes to viernes) do not change spelling in plural; only the article changes: 'el lunes' (on Monday) vs. 'los lunes' (on Mondays). Sábado and domingo add -s: 'los sábados', 'los domingos'.",
                "Date formula: 'Hoy es + [Day of week] + el + [Number] + de + [Month] + de + [Year]'"
            ],
            "structures": [
                "Asking the day: ¿Qué día es hoy? -> Hoy es [Día].",
                "Stating a date: Es el [Día] de [Mes] (Es el 5 de mayo).",
                "First day of the month: In Spain, use the cardinal number 'el uno de...' (el primero is also understood, but el uno is standard)."
            ],
            "examples": [
                {"spanish": "Hoy es miércoles.", "english": "Today is Wednesday."},
                {"spanish": "La fiesta es el sábado.", "english": "The party is on Saturday."},
                {"spanish": "Los domingos como con mi familia.", "english": "On Sundays I eat with my family."},
                {"spanish": "Nací el veintiocho de noviembre.", "english": "I was born on the twenty-eighth of November."}
            ],
            "commonMistakes": [
                {"wrong": "En lunes voy a clase", "right": "El lunes voy a clase", "explanation": "Spanish uses the article 'el' to mean 'on [day of the week]', never 'en'."},
                {"wrong": "Los Lunes (Capital L)", "right": "Los lunes", "explanation": "Days of the week are never capitalized in Spanish."}
            ],
            "proTip": "The Spanish calendar starts on Monday (*lunes*), not Sunday (*domingo*)! Keep this in mind when reading Spanish planners and calendars."
        },
        "conversation": {
            "title": "Planning the Weekend",
            "context": "Sakib and his friend Javier talk after class on Friday afternoon.",
            "dialogue": [
                {"speaker": "Javier", "role": "Friend", "spanish": "¡Por fin es viernes, Sakib! ¿Qué día es hoy?", "english": "Finally it's Friday, Sakib! What day is today?"},
                {"speaker": "Sakib", "role": "Student", "spanish": "Hoy es viernes, veinte de octubre.", "english": "Today is Friday, the twentieth of October."},
                {"speaker": "Javier", "role": "Friend", "spanish": "¿Tienes planes para el fin de semana?", "english": "Do you have plans for the weekend?"},
                {"speaker": "Sakib", "role": "Student", "spanish": "El sábado voy al Museo del Prado y el domingo estudio.", "english": "On Saturday I go to the Prado Museum and on Sunday I study."},
                {"speaker": "Javier", "role": "Friend", "spanish": "¡Qué buen plan! Nos vemos el lunes en clase.", "english": "What a great plan! See you Monday in class."},
                {"speaker": "Sakib", "role": "Student", "spanish": "¡Perfecto! ¡Buen fin de semana, Javier!", "english": "Perfect! Have a great weekend, Javier!"}
            ],
            "keyPhrases": [
                {"phrase": "¡Por fin es viernes!", "explanation": "The Spanish equivalent of 'TGIF / Finally it's Friday!'"},
                {"phrase": "¡Qué buen plan!", "explanation": "A natural reaction meaning 'What a great plan!'"},
                {"phrase": "Nos vemos el lunes", "explanation": "'We'll see each other on Monday'."}
            ]
        },
        "reading": {
            "title": "Las cuatro estaciones en España",
            "passage": "España tiene cuatro estaciones bien marcadas. La primavera empieza en marzo y termina en junio; es una época con flores y temperaturas agradables. El verano comienza a finales de junio y dura hasta septiembre; en ciudades como Madrid y Sevilla hace mucho calor. El otoño llega en septiembre y trae hojas doradas. Finalmente, el invierno empieza en diciembre y hace frío, especialmente en las montañas del norte.",
            "translation": "Spain has four well-marked seasons. Spring begins in March and ends in June; it is a time with flowers and pleasant temperatures. Summer begins at the end of June and lasts until September; in cities like Madrid and Seville it is very hot. Autumn arrives in September and brings golden leaves. Finally, winter begins in December and is cold, especially in the northern mountains.",
            "questions": [
                {"question": "¿Cuándo empieza la primavera en España?", "options": ["En diciembre", "En marzo", "En agosto", "En octubre"], "answer": 1, "explanation": "Spring begins in March ('empieza en marzo')."},
                {"question": "¿Cómo es el verano en Madrid y Sevilla?", "options": ["Hace mucho frío", "Hace mucho calor", "Nieva siempre", "No hay sol"], "answer": 1, "explanation": "In summer it is very hot ('hace mucho calor')."},
                {"question": "¿En qué mes empieza el invierno?", "options": ["En mayo", "En septiembre", "En diciembre", "En julio"], "answer": 2, "explanation": "Winter starts in December ('empieza en diciembre')."}
            ]
        },
        "exercises": [
            {
                "id": "d4-ex1",
                "type": "multiple-choice",
                "prompt": "How do you say 'On Mondays I study Spanish'?",
                "options": ["En lunes estudio español", "Los lunes estudio español", "El lunes estudio español", "Por lunes estudio español"],
                "correct": 1,
                "explanation": "To mean habitual 'On Mondays', use plural 'Los lunes'."
            },
            {
                "id": "d4-ex2",
                "type": "fill-in",
                "prompt": "Complete: Hoy es viernes y mañana es ______.",
                "options": ["sábado", "domingo", "jueves", "lunes"],
                "correct": 0,
                "explanation": "The day after Friday is Saturday (sábado)."
            },
            {
                "id": "d4-ex3",
                "type": "multiple-choice",
                "prompt": "Are days of the week capitalized in Spanish?",
                "options": ["Always", "Never (unless starting a sentence)", "Only on weekends", "Only in official documents"],
                "correct": 1,
                "explanation": "Days and months are written in lowercase in Spanish."
            },
            {
                "id": "d4-ex4",
                "type": "translation",
                "prompt": "Translate: 'My birthday is on May 10th.'",
                "options": ["Mi cumpleaños es el diez de mayo.", "Mi cumpleaños está en diez mayo.", "Mi cumpleaños es en mayo diez.", "Tengo cumpleaños diez de mayo."],
                "correct": 0,
                "explanation": "Date format is 'el [number] de [month]': 'el diez de mayo'."
            }
        ],
        "speakingChallenge": [
            {"prompt": "Say today's day of the week in Spanish.", "hint": "Hoy es...", "sampleAnswer": "Hoy es miércoles."},
            {"prompt": "State your birthday in a complete Spanish sentence.", "hint": "Mi cumpleaños es el [número] de [mes].", "sampleAnswer": "Mi cumpleaños es el quince de agosto."},
            {"prompt": "Wish someone a great weekend.", "hint": "¡Buen fin de semana!", "sampleAnswer": "¡Que tengas un buen fin de semana!"}
        ],
        "dailyRevision": {
            "quickQuestions": [
                "What preposition is used before days of the week? (Trick question!)",
                "Name all 7 days of the week in order from Monday."
            ],
            "grammarRecall": "Days and months are lowercase. Use 'el' for singular day and 'los' for habitual plural days.",
            "vocabRecall": ["Lunes", "Viernes", "Fin de semana", "Hoy", "Mañana", "Cumpleaños"]
        },
        "checklist": [
            "Recited all 7 days from lunes to domingo",
            "Named all 12 months in Spanish",
            "Understood never to use 'en' before days of the week",
            "Formed full Spanish dates with 'el ... de ...'",
            "Completed all 4 practice exercises",
            "Practiced saying your birthday aloud in Spanish"
        ]
    },
    {
        "day": 5,
        "stage": 1,
        "title": "Subject Pronouns & The Bengali Connection",
        "subtitle": "Mastering Yo, Tú, Él, Ella, Usted, Nosotros, Vosotros, Ellos, Ustedes + Mid-Stage 1 Review",
        "goals": [
            "Master all Spanish subject pronouns and their exact grammatical persons",
            "Understand the formal vs. informal distinction (Tú vs. Usted = তুমি vs. আপনি)",
            "Learn when subject pronouns can be omitted (dropped) in Spanish",
            "Complete the Stage 1 Mid-Point Revision (Days 1 to 5 review)"
        ],
        "bengaliNote": "The Spanish pronoun system is a carbon copy of Bangla! Tú = তুমি (informal singular), Usted = আপনি (formal singular), Vosotros = তোমরা (informal plural in Spain), Ustedes = আপনারা (formal plural). English speakers get confused here, but for you it is 100% natural!",
        "vocabulary": [
            {"word": "Yo", "translation": "I", "pos": "pronoun", "gender": None, "example": "Yo soy Sakib.", "exampleTranslation": "I am Sakib."},
            {"word": "Tú", "translation": "You (informal singular / তুমি)", "pos": "pronoun", "gender": None, "example": "¿Tú hablas español?", "exampleTranslation": "Do you speak Spanish?"},
            {"word": "Él / Ella", "translation": "He / She", "pos": "pronoun", "gender": "masculine / feminine", "example": "Él es profesor y ella es médica.", "exampleTranslation": "He is a teacher and she is a doctor."},
            {"word": "Usted", "translation": "You (formal singular / আপনি)", "pos": "pronoun", "gender": None, "example": "¿Cómo está usted?", "exampleTranslation": "How are you? (formal)"},
            {"word": "Nosotros / Nosotras", "translation": "We (masculine / feminine)", "pos": "pronoun", "gender": "plural", "example": "Nosotros somos estudiantes.", "exampleTranslation": "We are students."},
            {"word": "Vosotros / Vosotras", "translation": "You all (informal plural in Spain / তোমরা)", "pos": "pronoun", "gender": "plural", "example": "¿Vosotros sois de Madrid?", "exampleTranslation": "Are you all from Madrid?"},
            {"word": "Ellos / Ellas", "translation": "They (masculine / feminine)", "pos": "pronoun", "gender": "plural", "example": "Ellos viven aquí.", "exampleTranslation": "They live here."},
            {"word": "Ustedes", "translation": "You all (formal in Spain / আপনারা)", "pos": "pronoun", "gender": "plural", "example": "¿Ustedes tienen alguna pregunta?", "exampleTranslation": "Do you all have any question?"},
            {"word": "Hablar", "translation": "To speak", "pos": "verb", "gender": None, "example": "Hablo un poco de español.", "exampleTranslation": "I speak a little bit of Spanish."},
            {"word": "Comprender / Entender", "translation": "To understand", "pos": "verb", "gender": None, "example": "No entiendo, ¿puede repetir?", "exampleTranslation": "I don't understand, can you repeat?"}
        ],
        "sentences": [
            {"spanish": "Yo hablo bengalí, inglés y un poco de español.", "english": "I speak Bengali, English, and a little bit of Spanish."},
            {"spanish": "¿Tú comprendes la lección?", "english": "Do you understand the lesson?"},
            {"spanish": "Usted es muy amable, muchas gracias.", "english": "You are very kind, thank you very much. (formal)"},
            {"spanish": "Nosotros somos compañeros de clase.", "english": "We are classmates."},
            {"spanish": "¿Vosotros sois de España?", "english": "Are you all from Spain? (informal plural)"},
            {"spanish": "No entiendo muy bien, ¿puede hablar más despacio?", "english": "I don't understand very well, can you speak slower? (formal)"}
        ],
        "grammar": {
            "title": "The Complete Subject Pronoun Grid & Omission Rule",
            "explanation": "In Spanish, the verb ending changes for each person. Because the ending reveals who is doing the action, native speakers usually DROP subject pronouns unless they need emphasis or contrast!",
            "rules": [
                "Pronoun Drop: 'Hablo español' already means 'I speak Spanish'. You only say 'Yo hablo español' to emphasize that *I* (as opposed to someone else) speak Spanish.",
                "Tú vs. Tu: 'Tú' with an accent mark is the pronoun 'you'. 'Tu' without an accent is the possessive 'your' (tu libro).",
                "Él vs. El: 'Él' with an accent mark is 'he'. 'El' without an accent is the article 'the' (el libro).",
                "Mixed Gender Plurals: If a group has 99 women and 1 man, Spanish uses the masculine plural: 'nosotros' or 'ellos'."
            ],
            "structures": [
                "Subject Pronoun Grid:",
                "1st Person: Yo (I) | Nosotros/Nosotras (We)",
                "2nd Person Informal: Tú (You / তুমি) | Vosotros/Vosotras (You all / তোমরা - Spain only!)",
                "2nd Person Formal: Usted (You / আপনি) | Ustedes (You all / আপনারা)",
                "3rd Person: Él / Ella (He/She) | Ellos / Ellas (They)"
            ],
            "examples": [
                {"spanish": "Yo soy Sakib. (Soy Sakib)", "english": "I am Sakib."},
                {"spanish": "Ella es médica.", "english": "She is a doctor."},
                {"spanish": "¿Cómo se llama usted?", "english": "What is your name? (formal)"},
                {"spanish": "Vosotros tenéis clase hoy.", "english": "You all have class today."}
            ],
            "commonMistakes": [
                {"wrong": "Overusing 'Yo' in every sentence (Yo hablo, yo como, yo vivo)", "right": "Hablo, como, vivo", "explanation": "Native speakers drop 'yo' to sound natural."},
                {"wrong": "Using 'tú' with an elderly stranger or bank teller", "right": "Use 'usted'", "explanation": "Respectful formal distance is polite in administrative or professional interactions."}
            ],
            "proTip": "In Spain, 'vosotros' is used in every casual daily situation (with friends, colleagues, in a shop). In Latin America, 'vosotros' is replaced by 'ustedes'."
        },
        "conversation": {
            "title": "Meeting a Professor at University",
            "context": "Sakib speaks with Professor Martínez in the hallway.",
            "dialogue": [
                {"speaker": "Sakib", "role": "Student", "spanish": "Disculpe, ¿usted es el profesor Martínez?", "english": "Excuse me, are you Professor Martinez?"},
                {"speaker": "Prof. Martínez", "role": "Professor", "spanish": "Sí, soy yo. Buenos días. ¿Cómo se llama usted?", "english": "Yes, that is me. Good morning. What is your name?"},
                {"speaker": "Sakib", "role": "Student", "spanish": "Me llamo Sakib. Soy nuevo estudiante de español.", "english": "My name is Sakib. I am a new Spanish student."},
                {"speaker": "Prof. Martínez", "role": "Professor", "spanish": "¡Bienvenido, Sakib! ¿De dónde es usted?", "english": "Welcome, Sakib! Where are you from?"},
                {"speaker": "Sakib", "role": "Student", "spanish": "Soy de Bangladés. Hablo bengalí e inglés, y ahora estudio español.", "english": "I am from Bangladesh. I speak Bengali and English, and now I study Spanish."},
                {"speaker": "Prof. Martínez", "role": "Professor", "spanish": "Excelente. Si usted tiene alguna duda, aquí estoy.", "english": "Excellent. If you have any doubt/question, here I am."},
                {"speaker": "Sakib", "role": "Student", "spanish": "Muchas gracias por su tiempo, profesor. Hasta luego.", "english": "Thank you very much for your time, professor. See you later."}
            ],
            "keyPhrases": [
                {"phrase": "¿Usted es...?", "explanation": "Polite inquiry: 'Are you...?'"},
                {"phrase": "Disculpe", "explanation": "'Excuse me' used to capture someone's attention politely."},
                {"phrase": "Aquí estoy", "explanation": "Friendly idiom meaning 'I'm right here (to help)'."}
            ]
        },
        "reading": {
            "title": "Mid-Stage 1 Review Story: Un día en la academia",
            "passage": "Hoy es lunes, dos de octubre. Son las nueve de la mañana en Madrid. En la academia de español hay quince estudiantes. Sakib entra y dice: «¡Buenos días! ¿Qué tal?». Todos son amables. Sakib habla con Carlos, un chico de Italia, y con Sophie, una chica de Francia. Ellos tienen veinte años. Sakib dice: «Yo tengo veinticuatro años y soy de Bangladés». La profesora entra a las nueve y cuarto: «¡Hola a todos! Bienvenidos al curso».",
            "translation": "Today is Monday, October second. It is nine in the morning in Madrid. In the Spanish academy there are fifteen students. Sakib enters and says: 'Good morning! How are things?'. Everyone is kind. Sakib talks with Carlos, a boy from Italy, and with Sophie, a girl from France. They are twenty years old. Sakib says: 'I am twenty-four years old and I am from Bangladesh.' The teacher enters at nine fifteen: 'Hello everyone! Welcome to the course.'",
            "questions": [
                {"question": "¿Qué día y hora es al inicio de la historia?", "options": ["Viernes a las diez", "Lunes a las nueve", "Sábado por la tarde", "Domingo a las doce"], "answer": 1, "explanation": "It is Monday at 9:00 AM ('Hoy es lunes... Son las nueve')."},
                {"question": "¿De qué países son Carlos y Sophie?", "options": ["España y México", "Italia y Francia", "Alemania e Inglaterra", "Bangladés y China"], "answer": 1, "explanation": "Carlos is from Italy and Sophie is from France."},
                {"question": "¿Cuántos años tienen Carlos y Sophie?", "options": ["Quince", "Veinte", "Veinticuatro", "Treinta"], "answer": 1, "explanation": "They have 20 years ('Ellos tienen veinte años')."}
            ]
        },
        "exercises": [
            {
                "id": "d5-ex1",
                "type": "multiple-choice",
                "prompt": "Which pronoun corresponds to formal singular 'you' (like Bangla 'আপনি')?",
                "options": ["Tú", "Vosotros", "Usted", "Ellos"],
                "correct": 2,
                "explanation": "'Usted' is the formal singular 'you'."
            },
            {
                "id": "d5-ex2",
                "type": "multiple-choice",
                "prompt": "Which pronoun is used in Spain to address a group of friends (informal 'you all')?",
                "options": ["Ustedes", "Vosotros", "Ellos", "Nosotros"],
                "correct": 1,
                "explanation": "'Vosotros' is Spain's informal plural you."
            },
            {
                "id": "d5-ex3",
                "type": "fill-in",
                "prompt": "Fill in the accent mark: ______ (He) es mi profesor.",
                "options": ["Él", "El", "Ella", "Tu"],
                "correct": 0,
                "explanation": "'Él' (with accent) means 'he'. Without accent, 'el' means 'the'."
            },
            {
                "id": "d5-ex4",
                "type": "translation",
                "prompt": "Translate: 'We are students.'",
                "options": ["Nosotros somos estudiantes.", "Ellos son estudiantes.", "Yo soy estudiante.", "Vosotros sois estudiantes."],
                "correct": 0,
                "explanation": "'Nosotros somos estudiantes' means 'We are students'."
            }
        ],
        "speakingChallenge": [
            {"prompt": "Address an elderly person politely and ask their name.", "hint": "¿Cómo se llama usted?", "sampleAnswer": "Disculpe, ¿cómo se llama usted, señor?"},
            {"prompt": "Say what languages you speak.", "hint": "Hablo bengalí, inglés y...", "sampleAnswer": "Hablo bengalí, inglés y un poco de español."},
            {"prompt": "State: 'We are in Madrid.'", "hint": "Nosotros estamos en...", "sampleAnswer": "Nosotros estamos en Madrid."}
        ],
        "dailyRevision": {
            "quickQuestions": [
                "What is the difference between 'Tú' and 'Usted'?",
                "Why don't Spanish speakers need to say 'Yo' before every conjugated verb?"
            ],
            "grammarRecall": "Yo, Tú, Él/Ella/Usted, Nosotros, Vosotros, Ellos/Ellas/Ustedes.",
            "vocabRecall": ["Yo", "Tú", "Usted", "Nosotros", "Vosotros", "Hablar", "Entender"]
        },
        "checklist": [
            "Memorized the complete subject pronoun grid",
            "Understood the Tú (তুমি) vs. Usted (আপনি) distinction",
            "Learned why subject pronouns are usually dropped",
            "Completed the Mid-Stage 1 review reading passage",
            "Passed all 4 pronoun exercises",
            "Completed the 3 speaking prompts out loud"
        ]
    }
]

print(f"Loaded {len(stage1_days)} initial days for Stage 1.")
