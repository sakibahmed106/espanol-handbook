"""
Build Stage 1: Days 6 to 10 + Combine Stage 1 into data/lessons/stage1.js
"""
import json
from build_stage1_part1 import stage1_days

stage1_part2 = [
    {
        "day": 6,
        "stage": 1,
        "title": "Alphabet, Phonetics & Special Characters",
        "subtitle": "Mastering tricky Spanish sounds, trilled 'rr', and punctuation",
        "goals": [
            "Review tricky Spanish letter combinations: C/Z, G/J, LL, Ñ, and RR",
            "Master the difference between tapped 'r' (*pero*) and trilled 'rr' (*perro*)",
            "Understand why Spanish uses inverted question marks (¿ ?) and exclamations (¡ !)",
            "Spell your name and address using Spanish letter names"
        ],
        "bengaliNote": "Spanish 'r' in *caro* (expensive) is a single tap, exactly like Bangla 'র'. But *carro* (car) or *perro* (dog) requires a trill where your tongue vibrates. Practice by repeating: 'Erre con erre guitarra, erre con erre barril'!",
        "vocabulary": [
            {"word": "La letra", "translation": "The letter (of the alphabet)", "pos": "noun", "gender": "feminine", "example": "La letra 'ñ' es típica de España.", "exampleTranslation": "The letter 'ñ' is typical of Spain."},
            {"word": "La palabra", "translation": "The word", "pos": "noun", "gender": "feminine", "example": "¿Cómo se pronuncia esta palabra?", "exampleTranslation": "How is this word pronounced?"},
            {"word": "El acento / La tilde", "translation": "The accent mark", "pos": "noun", "gender": "masculine / feminine", "example": "La palabra 'café' lleva tilde.", "exampleTranslation": "The word 'café' carries an accent mark."},
            {"word": "Deletrear", "translation": "To spell", "pos": "verb", "gender": None, "example": "¿Puedes deletrear tu nombre, por favor?", "exampleTranslation": "Can you spell your name, please?"},
            {"word": "El sonido", "translation": "The sound", "pos": "noun", "gender": "masculine", "example": "El sonido de la 'jota' es fuerte.", "exampleTranslation": "The sound of the 'jota' is strong."},
            {"word": "La frase", "translation": "The phrase / sentence", "pos": "noun", "gender": "feminine", "example": "Repite esta frase conmigo.", "exampleTranslation": "Repeat this phrase with me."},
            {"word": "El idioma / La lengua", "translation": "The language", "pos": "noun", "gender": "masculine / feminine", "example": "El español es un idioma hermoso.", "exampleTranslation": "Spanish is a beautiful language."},
            {"word": "¿Cómo se escribe?", "translation": "How do you write/spell it?", "pos": "phrase", "gender": None, "example": "¿Cómo se escribe tu apellido?", "exampleTranslation": "How is your last name spelled?"},
            {"word": "¿Cómo se pronuncia?", "translation": "How is it pronounced?", "pos": "phrase", "gender": None, "example": "¿Cómo se pronuncia 'cerveza'?", "exampleTranslation": "How is 'cerveza' pronounced?"},
            {"word": "Más despacio", "translation": "More slowly", "pos": "phrase", "gender": None, "example": "Más despacio, por favor, no entiendo.", "exampleTranslation": "More slowly, please, I don't understand."}
        ],
        "sentences": [
            {"spanish": "¿Cómo se escribe tu nombre?", "english": "How is your name written/spelled?"},
            {"spanish": "Se escribe ese - a - ka - i - be: S-A-K-I-B.", "english": "It is spelled S-A-K-I-B."},
            {"spanish": "¿Puede hablar más despacio, por favor?", "english": "Can you speak more slowly, please?"},
            {"spanish": "¿Qué significa esta palabra?", "english": "What does this word mean?"},
            {"spanish": "El español se lee tal como se escribe.", "english": "Spanish is read just as it is written."},
            {"spanish": "¡Qué sonido tan interesante!", "english": "What an interesting sound!"}
        ],
        "grammar": {
            "title": "Castilian Pronunciation Mechanics: C, Z, G, J & RR",
            "explanation": "Spanish is 98% phonetically consistent. Once you learn how each consonant behaves before specific vowels, you can read any Spanish book out loud with 100% accuracy!",
            "rules": [
                "C Sound Rules: 'C' before E or I makes the Castilian voiceless 'th' sound (cena, cinco). Before A, O, U, it makes a hard 'K' sound (casa, coche, cuna).",
                "Z Sound Rule: 'Z' in Spain ALWAYS makes the 'th' sound, regardless of the vowel (zapato, zumo, corazón).",
                "G Sound Rules: 'G' before E or I makes a strong throaty 'H/Kh' sound (gente, girasol). Before A, O, U, it makes a hard 'G' as in 'go' (gato, gota, gusto).",
                "Single R vs. Double RR: A single 'r' in the middle of a word (*caro*) is a soft tap. A double 'rr' (*carro*) or an 'r' at the VERY BEGINNING of a word (*rojo*, *radio*) is ALWAYS strongly trilled!"
            ],
            "structures": [
                "Asking spelling: ¿Cómo se escribe [Palabra]?",
                "Spelling out: Se escribe con [Letra] (Se escribe con 'be' / Se escribe con tilde)",
                "Asking meaning: ¿Qué significa [Palabra]?"
            ],
            "examples": [
                {"spanish": "Se escribe con zeta.", "english": "It is written with a Z."},
                {"spanish": "La palabra 'lección' lleva dos ces y tilde.", "english": "The word 'lección' carries two C's and an accent mark."},
                {"spanish": "El perro corre rápido.", "english": "The dog runs fast. (Note the trilled RR in both words!)"},
                {"spanish": "Gracias por la información.", "english": "Thank you for the information."}
            ],
            "commonMistakes": [
                {"wrong": "Pronouncing 'Z' like English buzzing 'Zebra'", "right": "In Spain, pronounce 'Z' like 'th' in 'thin'", "explanation": "Spanish has no buzzing English 'Z' sound. 'Zapato' is pronounced 'thah-pah-toh'."},
                {"wrong": "Forgetting the upside down '¿' at the start of a question", "right": "Always write ¿ at the start and ? at the end", "explanation": "Inverted marks are mandatory in formal Spanish writing."}
            ],
            "proTip": "The classic Spanish tongue-twister for the trilled 'rr': 'Erre con erre cigarro, erre con erre barril, rápido corren los carros del ferrocarril!'"
        },
        "conversation": {
            "title": "Spelling at the Reception Desk",
            "context": "Sakib checks into a hotel in Salamanca.",
            "dialogue": [
                {"speaker": "Recepcionista", "role": "Hotel staff", "spanish": "Buenas tardes, señor. ¿Tiene una reserva?", "english": "Good afternoon, sir. Do you have a reservation?"},
                {"speaker": "Sakib", "role": "Guest", "spanish": "Sí, buenas tardes. Tengo una reserva.", "english": "Yes, good afternoon. I have a reservation."},
                {"speaker": "Recepcionista", "role": "Hotel staff", "spanish": "¿Cuál es su nombre y apellido, por favor?", "english": "What is your name and last name, please?"},
                {"speaker": "Sakib", "role": "Guest", "spanish": "Me llamo Sakib Ahmed.", "english": "My name is Sakib Ahmed."},
                {"speaker": "Recepcionista", "role": "Hotel staff", "spanish": "¿Puede deletrear su apellido, por favor?", "english": "Can you spell your last name, please?"},
                {"speaker": "Sakib", "role": "Guest", "spanish": "Sí, por supuesto: A - Hache - Eme - E - De. Ahmed.", "english": "Yes, of course: A - H - M - E - D. Ahmed."},
                {"speaker": "Recepcionista", "role": "Hotel staff", "spanish": "¡Perfecto, señor Ahmed! Habitación número catorce.", "english": "Perfect, Mr. Ahmed! Room number fourteen."}
            ],
            "keyPhrases": [
                {"phrase": "Por supuesto", "explanation": "Natural, polite expression for 'Of course' or 'Certainly'."},
                {"phrase": "Nombre y apellido", "explanation": "'First name and surname'. In Spain, people traditionally have two surnames (father's and mother's)."},
                {"phrase": "¿Puede deletrear...?", "explanation": "'Can you spell...?' (formal request)."}
            ]
        },
        "reading": {
            "title": "El misterio de la letra Ñ",
            "passage": "La letra Ñ es el símbolo más famoso del idioma español. Nació en la Edad Media en los monasterios de España. Los monjes copistas escribían muchos libros a mano. Para ahorrar espacio y pergamino, escribían una pequeña 'n' encima de otra 'n' (nn -> ñ). Así nació la virgulilla, el sombrerito de la eñe. Hoy, la letra ñ existe en miles de palabras importantes como España, año, niño, pequeño y señor.",
            "translation": "The letter Ñ is the most famous symbol of the Spanish language. It was born in the Middle Ages in the monasteries of Spain. The monk copyists wrote many books by hand. To save space and parchment, they wrote a small 'n' on top of another 'n' (nn -> ñ). Thus was born the tilde, the little hat of the eñe. Today, the letter ñ exists in thousands of important words like Spain, year, child, small, and sir.",
            "questions": [
                {"question": "¿Dónde nació la letra Ñ?", "options": ["En Roma", "En los monasterios de España", "En América", "En una escuela moderna"], "answer": 1, "explanation": "It was born in the monasteries of Spain ('en los monasterios de España')."},
                {"question": "¿Por qué los monjes inventaron la virgulilla?", "options": ["Para pintar colores", "Para ahorrar espacio y pergamino", "Porque no tenían tinta", "Por diversión"], "answer": 1, "explanation": "To save space and parchment ('Para ahorrar espacio y pergamino')."},
                {"question": "¿Cuál de estas palabras lleva la letra Ñ?", "options": ["Casa", "Niño", "Libro", "Mesa"], "answer": 1, "explanation": "'Niño' contains the unique letter ñ."}
            ]
        },
        "exercises": [
            {
                "id": "d6-ex1",
                "type": "multiple-choice",
                "prompt": "How is 'C' pronounced before 'E' and 'I' in Spain?",
                "options": ["Like 'K' in kite", "Like 'th' in think", "Like 'CH' in chair", "It is silent"],
                "correct": 1,
                "explanation": "In Spain, C before E and I is pronounced like 'th'."
            },
            {
                "id": "d6-ex2",
                "type": "multiple-choice",
                "prompt": "When is the letter 'R' strongly trilled in Spanish?",
                "options": ["Only when written as 'rr'", "When written as 'rr' AND at the very start of a word", "Never", "Only at the end of a word"],
                "correct": 1,
                "explanation": "Both 'rr' and an initial 'r' (like 'rojo') are strongly trilled."
            },
            {
                "id": "d6-ex3",
                "type": "fill-in",
                "prompt": "Complete: ¿Cómo se ______ tu apellido? (How is it written/spelled?)",
                "options": ["escribe", "habla", "llama", "vive"],
                "correct": 0,
                "explanation": "'¿Cómo se escribe?' asks how something is spelled/written."
            },
            {
                "id": "d6-ex4",
                "type": "translation",
                "prompt": "Translate: 'Can you speak more slowly, please?'",
                "options": ["¿Puede hablar más despacio, por favor?", "¿Cómo te llamas por favor?", "¿Dónde vives por favor?", "¿Cuánto cuesta por favor?"],
                "correct": 0,
                "explanation": "'¿Puede hablar más despacio, por favor?' is the essential survival phrase."
            }
        ],
        "speakingChallenge": [
            {"prompt": "Spell out your first name letter by letter using Spanish letter names.", "hint": "S (ese) - A (a) - K (ka)...", "sampleAnswer": "Ese - A - Ka - I - Be: Sakib."},
            {"prompt": "Ask a local in Madrid how to pronounce a word.", "hint": "¿Cómo se pronuncia...", "sampleAnswer": "Disculpe, ¿cómo se pronuncia esta palabra?"},
            {"prompt": "Practice the trilled 'rr': say 'perro', 'ferrocarril', and 'arroz'.", "hint": "Vibrate the tip of your tongue against your upper ridge.", "sampleAnswer": "Perro, ferrocarril, arroz."}
        ],
        "dailyRevision": {
            "quickQuestions": [
                "What is the wavy symbol on top of the 'ñ' called in Spanish? (La virgulilla)",
                "How do you pronounce 'Z' in Madrid?"
            ],
            "grammarRecall": "Initial 'R' and 'RR' are trilled. 'C' before E/I and 'Z' sound like 'th'. 'H' is always silent.",
            "vocabRecall": ["La letra", "La palabra", "Deletrear", "¿Cómo se escribe?", "Más despacio"]
        },
        "checklist": [
            "Pronounced the Spanish alphabet letter names",
            "Mastered the Castilian 'th' sound for Z and CE/CI",
            "Practiced the trilled 'rr' with authentic vibration",
            "Spelled my name out loud in Spanish",
            "Completed all 4 phonetics exercises",
            "Read the historical story of the letter Ñ"
        ]
    },
    {
        "day": 7,
        "stage": 1,
        "title": "Gender of Nouns & Plural Rules",
        "subtitle": "Understanding masculine vs. feminine nouns and forming plurals",
        "goals": [
            "Understand that every Spanish noun has a grammatical gender (masculine or feminine)",
            "Identify the standard patterns: -o for masculine, -a for feminine",
            "Learn the high-frequency tricky exceptions (el problema, el día, el mapa, la mano, la foto)",
            "Apply the universal rules for forming plural nouns (-s vs. -es)"
        ],
        "bengaliNote": "Bangla does not have grammatical gender for objects (a table is just a table). But in Spanish, every single object in the universe is either male (*el libro*, *el sol*) or female (*la mesa*, *la luna*). Think of gender as a permanent sticker on every noun!",
        "vocabulary": [
            {"word": "El sustantivo", "translation": "The noun", "pos": "noun", "gender": "masculine", "example": "Los sustantivos tienen género.", "exampleTranslation": "Nouns have gender."},
            {"word": "Masculino / Femenino", "translation": "Masculine / Feminine", "pos": "adjective", "gender": "masculine / feminine", "example": "'El libro' es masculino y 'la mesa' es femenina.", "exampleTranslation": "'El libro' is masculine and 'la mesa' is feminine."},
            {"word": "El libro / Los libros", "translation": "The book / The books", "pos": "noun", "gender": "masculine", "example": "Leo un libro interesante.", "exampleTranslation": "I read an interesting book."},
            {"word": "La mesa / Las mesas", "translation": "The table / The tables", "pos": "noun", "gender": "feminine", "example": "Hay cuatro sillas alrededor de la mesa.", "exampleTranslation": "There are four chairs around the table."},
            {"word": "El día / Los días", "translation": "The day / The days (exception: ends in -a but is masculine!)", "pos": "noun", "gender": "masculine", "example": "Buenos días.", "exampleTranslation": "Good morning."},
            {"word": "El problema / Los problemas", "translation": "The problem / The problems (Greek origin exception: masculine!)", "pos": "noun", "gender": "masculine", "example": "No hay ningún problema.", "exampleTranslation": "There is no problem at all."},
            {"word": "El mapa / Los mapas", "translation": "The map / The maps (exception: ends in -a but masculine!)", "pos": "noun", "gender": "masculine", "example": "Miro el mapa de la ciudad.", "exampleTranslation": "I look at the map of the city."},
            {"word": "La mano / Las manos", "translation": "The hand / The hands (exception: ends in -o but feminine!)", "pos": "noun", "gender": "feminine", "example": "Levanta la mano.", "exampleTranslation": "Raise your hand."},
            {"word": "La foto / Las fotos", "translation": "The photo / The photos (short for 'la fotografía')", "pos": "noun", "gender": "feminine", "example": "Una foto muy bonita.", "exampleTranslation": "A very pretty photo."},
            {"word": "La ciudad / Las ciudades", "translation": "The city / The cities (-dad is always feminine)", "pos": "noun", "gender": "feminine", "example": "Madrid es una ciudad hermosa.", "exampleTranslation": "Madrid is a beautiful city."}
        ],
        "sentences": [
            {"spanish": "No hay ningún problema, todo está bien.", "english": "There is no problem, everything is fine."},
            {"spanish": "Tengo dos libros en mi mochila.", "english": "I have two books in my backpack."},
            {"spanish": "Lavarse las manos es importante.", "english": "Washing hands is important."},
            {"spanish": "¿Tienes el mapa de Madrid?", "english": "Do you have the map of Madrid?"},
            {"spanish": "Hoy es un día maravilloso.", "english": "Today is a wonderful day."},
            {"spanish": "Las ciudades españolas son muy históricas.", "english": "Spanish cities are very historic."}
        ],
        "grammar": {
            "title": "Noun Gender Rules, Clues & Plural Formation",
            "explanation": "To master Spanish nouns, you must never learn a word in isolation. Always learn the noun together with its article (*el libro*, *la mesa*)!",
            "rules": [
                "Typically Masculine: Nouns ending in -o (*el chico*, *el vaso*), -or (*el profesor*, *el amor*), and Greek words ending in -ma (*el problema*, *el sistema*, *el idioma*, *el tema*).",
                "Typically Feminine: Nouns ending in -a (*la chica*, *la casa*), -ción/-sión (*la lección*, *la conversación*), -dad/-tad (*la ciudad*, *la libertad*), and -ez (*la vejez*).",
                "The 5 Famous Exceptions: *El día* (day), *El mapa* (map), *El problema* (problem) are masculine! *La mano* (hand) and *La foto* (photo - short for fotografía) are feminine!",
                "Plural Rule 1: If a noun ends in a vowel, simply add -s: *libro -> libros*, *mesa -> mesas*.",
                "Plural Rule 2: If a noun ends in a consonant, add -es: *ciudad -> ciudades*, *profesor -> profesores*.",
                "Plural Rule 3: If a noun ends in -z, change -z to -ces: *lápiz -> lápices*, *vez -> veces*."
            ],
            "structures": [
                "Vowel ending: [Noun] + s (casa -> casas)",
                "Consonant ending: [Noun] + es (hotel -> hoteles)",
                "Z ending: -z -> -ces (luz -> luces)"
            ],
            "examples": [
                {"spanish": "El chico -> Los chicos", "english": "The boy -> The boys"},
                {"spanish": "La lección -> Las lecciones", "english": "The lesson -> The lessons"},
                {"spanish": "Un problema difícil.", "english": "A difficult problem. (Problem is masculine!)"},
                {"spanish": "Tengo las manos frías.", "english": "I have cold hands. (Mano is feminine!)"}
            ],
            "commonMistakes": [
                {"wrong": "La problema", "right": "El problema", "explanation": "Words of Greek origin ending in -ma (*problema, sistema, idioma, programa*) are masculine."},
                {"wrong": "El mano", "right": "La mano", "explanation": "'Mano' is an ancient exception: it is feminine."},
                {"wrong": "La día", "right": "El día", "explanation": "'Día' is masculine (that's why we say *buenos días*, not *buenas días*)!"}
            ],
            "proTip": "Remember the acronym **L-O-N-E-R-S** for masculine noun endings, and **D-IÓN-Z-A** for feminine noun endings!"
        },
        "conversation": {
            "title": "Asking for Help at the Tourist Office",
            "context": "Sakib visits the tourist office in Plaza Mayor, Madrid.",
            "dialogue": [
                {"speaker": "Sakib", "role": "Visitor", "spanish": "¡Hola! Buenos días. ¿Tienen un mapa de la ciudad?", "english": "Hello! Good morning. Do you have a map of the city?"},
                {"speaker": "Informadora", "role": "Office guide", "spanish": "¡Buenos días! Sí, aquí tiene el mapa y dos guías turísticas.", "english": "Good morning! Yes, here is the map and two tourist guides."},
                {"speaker": "Sakib", "role": "Visitor", "spanish": "Muchas gracias. Tengo una pregunta sobre los museos.", "english": "Thank you very much. I have a question about the museums."},
                {"speaker": "Informadora", "role": "Office guide", "spanish": "Dígame, ¿cuál es el problema o la duda?", "english": "Tell me, what is the problem or question?"},
                {"speaker": "Sakib", "role": "Visitor", "spanish": "No hay ningún problema, solo quiero saber los horarios.", "english": "There is no problem, I only want to know the schedules."},
                {"speaker": "Informadora", "role": "Office guide", "spanish": "Los museos abren todos los días a las diez de la mañana.", "english": "Museums open every day at ten in the morning."}
            ],
            "keyPhrases": [
                {"phrase": "Dígame", "explanation": "'Tell me' (formal command) used by receptionists or when answering the phone in Spain."},
                {"phrase": "No hay ningún problema", "explanation": "'There is no problem at all' — a common reassuring phrase."},
                {"phrase": "Todos los días", "explanation": "'Every day'."}
            ]
        },
        "reading": {
            "title": "Las cosas en mi habitación",
            "passage": "En mi habitación en Madrid tengo muchas cosas útiles. Encima de la mesa hay tres libros de español, dos lápices y un cuaderno azul. También tengo una foto de mi familia en Bangladés. En la pared hay un mapa grande de España para planear mis viajes los fines de semana. Por la mañana entra mucha luz por la ventana. Es un espacio tranquilo para estudiar.",
            "translation": "In my room in Madrid I have many useful things. On the table there are three Spanish books, two pencils, and a blue notebook. I also have a photo of my family in Bangladesh. On the wall there is a big map of Spain to plan my trips on weekends. In the morning a lot of light enters through the window. It is a quiet space to study.",
            "questions": [
                {"question": "¿Cuántos libros de español hay en la mesa?", "options": ["Uno", "Dos", "Tres", "Cuatro"], "answer": 2, "explanation": "There are three books ('tres libros de español')."},
                {"question": "¿Qué hay en la pared?", "options": ["Un reloj", "Un mapa grande de España", "Una televisión", "Una guitarra"], "answer": 1, "explanation": "There is a large map of Spain ('un mapa grande de España')."},
                {"question": "¿De qué es la foto que tiene Sakib?", "options": ["De Madrid", "De su familia en Bangladés", "De su escuela", "De su perro"], "answer": 1, "explanation": "It is of his family in Bangladesh ('una foto de mi familia en Bangladés')."}
            ]
        },
        "exercises": [
            {
                "id": "d7-ex1",
                "type": "multiple-choice",
                "prompt": "Which of the following is correct for 'the problem'?",
                "options": ["La problema", "El problema", "Los problema", "Las problema"],
                "correct": 1,
                "explanation": "'Problema' is a Greek-origin noun and is masculine: 'El problema'."
            },
            {
                "id": "d7-ex2",
                "type": "fill-in",
                "prompt": "Form the plural of 'ciudad': Una ciudad -> Dos ______.",
                "options": ["ciudads", "ciudades", "ciudadis", "ciudados"],
                "correct": 1,
                "explanation": "Nouns ending in a consonant add -es: 'ciudades'."
            },
            {
                "id": "d7-ex3",
                "type": "multiple-choice",
                "prompt": "What is the gender of 'la mano' (the hand)?",
                "options": ["Masculine", "Feminine", "Neutral", "Both"],
                "correct": 1,
                "explanation": "'Mano' is an exception ending in -o that is grammatically feminine ('la mano')."
            },
            {
                "id": "d7-ex4",
                "type": "translation",
                "prompt": "Translate: 'No problem, thank you.'",
                "options": ["No hay problema, gracias.", "No tiene problema, hola.", "La problema no está.", "Mucho problema, por favor."],
                "correct": 0,
                "explanation": "'No hay problema, gracias' is the accurate translation."
            }
        ],
        "speakingChallenge": [
            {"prompt": "Look around your room and name 2 masculine and 2 feminine objects in Spanish.", "hint": "El libro, el teléfono / la mesa, la ventana.", "sampleAnswer": "El libro, el vaso, la mesa y la silla."},
            {"prompt": "Say: 'I have a map and three books.'", "hint": "Tengo un mapa y tres libros.", "sampleAnswer": "Tengo un mapa y tres libros en mi habitación."},
            {"prompt": "Reassure someone politely that there is no problem.", "hint": "No hay ningún problema...", "sampleAnswer": "Tranquilo, no hay ningún problema."}
        ],
        "dailyRevision": {
            "quickQuestions": [
                "Why is 'el día' masculine even though it ends with -a?",
                "How do you make a word ending in -z plural (e.g. lápiz)?"
            ],
            "grammarRecall": "-o = masculine | -a = feminine | Greek -ma = masculine | -dad/-ción = feminine | Plural: +s (vowel) or +es (consonant).",
            "vocabRecall": ["El problema", "El mapa", "El día", "La mano", "La foto", "La ciudad"]
        },
        "checklist": [
            "Mastered -o (masculine) vs -a (feminine) patterns",
            "Memorized the 5 key exceptions (problema, mapa, día, mano, foto)",
            "Applied plural rules (+s vs +es vs -ces)",
            "Understood the LONERS and D-IÓN-Z-A acronyms",
            "Completed all 4 noun exercises",
            "Practiced identifying noun genders in my surroundings"
        ]
    },
    {
        "day": 8,
        "stage": 1,
        "title": "Articles: Definite & Indefinite",
        "subtitle": "Mastering El, La, Los, Las, Un, Una, Unos, Unas + Contractions Al & Del",
        "goals": [
            "Master all four definite articles ('the'): el, la, los, las",
            "Master all four indefinite articles ('a / an / some'): un, una, unos, unas",
            "Learn the two mandatory contractions in Spanish: a + el = al, de + el = del",
            "Know when to omit articles in Spanish (professions with 'ser')"
        ],
        "bengaliNote": "Bangla has definite markers (যেমন: বইটা, বইগুলো). In Spanish, articles are separate words that must agree in both gender AND number with the noun. Notice that 'a + el' merges into 'al' and 'de + el' merges into 'del' — just like contractions in spoken Bangla!",
        "vocabulary": [
            {"word": "El / Los", "translation": "The (masculine singular / plural)", "pos": "article", "gender": "masculine", "example": "El tren y los trenes.", "exampleTranslation": "The train and the trains."},
            {"word": "La / Las", "translation": "The (feminine singular / plural)", "pos": "article", "gender": "feminine", "example": "La casa y las casas.", "exampleTranslation": "The house and the houses."},
            {"word": "Un / Unos", "translation": "A / Some (masculine singular / plural)", "pos": "article", "gender": "masculine", "example": "Un café y unos cruasanes.", "exampleTranslation": "A coffee and some croissants."},
            {"word": "Una / Unas", "translation": "A / Some (feminine singular / plural)", "pos": "article", "gender": "feminine", "example": "Una manzana y unas tapas.", "exampleTranslation": "An apple and some tapas."},
            {"word": "Al (a + el)", "translation": "To the (mandatory contraction)", "pos": "contraction", "gender": "masculine", "example": "Voy al supermercado.", "exampleTranslation": "I go to the supermarket."},
            {"word": "Del (de + el)", "translation": "Of the / From the (mandatory contraction)", "pos": "contraction", "gender": "masculine", "example": "El libro del profesor.", "exampleTranslation": "The teacher's book (the book of the teacher)."},
            {"word": "El chico / La chica", "translation": "The boy / The girl", "pos": "noun", "gender": "masculine / feminine", "example": "Los chicos juegan en el parque.", "exampleTranslation": "The boys play in the park."},
            {"word": "El profesor / La profesora", "translation": "The teacher / professor", "pos": "noun", "gender": "masculine / feminine", "example": "Soy profesor de idiomas.", "exampleTranslation": "I am a language teacher (no article with profession!)."},
            {"word": "El parque", "translation": "The park", "pos": "noun", "gender": "masculine", "example": "Paseo por el parque del Retiro.", "exampleTranslation": "I stroll through the Retiro park."},
            {"word": "La tienda", "translation": "The store / shop", "pos": "noun", "gender": "feminine", "example": "Voy a la tienda de ropa.", "exampleTranslation": "I go to the clothing store."}
        ],
        "sentences": [
            {"spanish": "Voy al banco a sacar dinero.", "english": "I go to the bank to take out money."},
            {"spanish": "Este es el coche del doctor López.", "english": "This is Doctor Lopez's car."},
            {"spanish": "Quiero comprar unos libros de gramática.", "english": "I want to buy some grammar books."},
            {"spanish": "Hay unas chicas en la cafetería.", "english": "There are some girls in the cafeteria."},
            {"spanish": "Soy estudiante de arquitectura.", "english": "I am an architecture student. (Note: no 'un'!)"},
            {"spanish": "Vamos al parque por la tarde.", "english": "We go to the park in the afternoon."}
        ],
        "grammar": {
            "title": "The Four Corners of Articles & The Two Contractions",
            "explanation": "Articles in Spanish are precision instruments. They specify whether you mean something specific ('the') or general ('a/some'), and they must mirror the noun's gender and count.",
            "rules": [
                "Definite Articles ('the'): el (masc sing), la (fem sing), los (masc plur), las (fem plur).",
                "Indefinite Articles ('a/some'): un (masc sing), una (fem sing), unos (masc plur), unas (fem plur).",
                "The Only 2 Spanish Contractions: In Spanish, 'a + el' MUST become 'al' (*Voy al cine*). 'de + el' MUST become 'del' (*La puerta del hotel*). Note: 'a la' and 'de la' do NOT contract (*Voy a la playa*).",
                "Omission with Professions: When stating what you do with 'ser', do NOT use an article: 'Soy ingeniero' (not 'Soy un ingeniero'), UNLESS qualified by an adjective: 'Soy un ingeniero excelente'."
            ],
            "structures": [
                "Definite: el / la / los / las + [Noun]",
                "Indefinite: un / una / unos / unas + [Noun]",
                "a + el = al (Voy al parque)",
                "de + el = del (La casa del señor Gómez)"
            ],
            "examples": [
                {"spanish": "El chico y la chica van al cine.", "english": "The boy and the girl go to the cinema."},
                {"spanish": "Compro unos tomates y unas manzanas.", "english": "I buy some tomatoes and some apples."},
                {"spanish": "Es el bolígrafo del estudiante.", "english": "It is the student's pen."},
                {"spanish": "Soy profesor. (Not: Soy un profesor)", "english": "I am a teacher."}
            ],
            "commonMistakes": [
                {"wrong": "Voy a el parque", "right": "Voy al parque", "explanation": "'A + el' must contract to 'al'."},
                {"wrong": "El libro de el estudiante", "right": "El libro del estudiante", "explanation": "'De + el' must contract to 'del'."},
                {"wrong": "Soy un médico", "right": "Soy médico", "explanation": "Do not use 'un' or 'una' when stating your profession with 'ser'."}
            ],
            "proTip": "If a feminine singular noun starts with a stressed 'a' or 'ha' sound (like *agua* or *hacha*), Spanish uses 'el' in the singular to prevent awkward vowel bumping (*el agua*, not *la agua*). But in plural, it returns to feminine: *las aguas*!"
        },
        "conversation": {
            "title": "Ordering Tapas in Madrid",
            "context": "Sakib and his friend David order tapas at a traditional tavern.",
            "dialogue": [
                {"speaker": "Camarero", "role": "Waiter", "spanish": "¡Hola! Buenas tardes. ¿Qué les pongo?", "english": "Hello! Good afternoon. What can I get you all?"},
                {"speaker": "David", "role": "Friend", "spanish": "Para mí, una caña y una ración de patatas bravas, por favor.", "english": "For me, a small draft beer and a portion of spicy potatoes, please."},
                {"speaker": "Sakib", "role": "Student", "spanish": "Para mí, un zumo de naranja y unos calamares, por favor.", "english": "For me, an orange juice and some squid rings, please."},
                {"speaker": "Camarero", "role": "Waiter", "spanish": "Muy bien. ¿El zumo con hielo?", "english": "Very well. The juice with ice?"},
                {"speaker": "Sakib", "role": "Student", "spanish": "Sí, con un poco de hielo, gracias.", "english": "Yes, with a little ice, thank you."},
                {"speaker": "Camarero", "role": "Waiter", "spanish": "Enseguida se lo traigo.", "english": "Right away I bring it to you."}
            ],
            "keyPhrases": [
                {"phrase": "¿Qué les pongo?", "explanation": "Classic Spain bar phrase used by waiters: 'What can I serve you?'"},
                {"phrase": "Para mí...", "explanation": "The standard way to order food or drinks: 'For me, [item]...'"},
                {"phrase": "Enseguida", "explanation": "'Right away' / 'Immediately'."}
            ]
        },
        "reading": {
            "title": "Un paseo por el Parque del Retiro",
            "passage": "El Parque del Retiro es el corazón verde de Madrid. Los fines de semana, muchas personas van al parque a pasear, leer o hacer deporte. Hay un estanque grande con barcas donde los niños y las familias reman alegremente. Al lado del estanque está el Palacio de Cristal, un edificio hermoso hecho de cristal y metal. En los jardines hay unas flores preciosas y árboles centenarios. Es el lugar favorito de los madrileños.",
            "translation": "The Retiro Park is the green heart of Madrid. On weekends, many people go to the park to stroll, read, or do sports. There is a large pond with rowboats where children and families row happily. Next to the pond is the Crystal Palace, a beautiful building made of glass and metal. In the gardens there are some gorgeous flowers and centennial trees. It is the favorite place of the locals of Madrid.",
            "questions": [
                {"question": "¿A dónde van muchas personas los fines de semana?", "options": ["Al cine", "Al Parque del Retiro", "A la estación", "Al banco"], "answer": 1, "explanation": "They go to the Retiro Park ('van al parque')."},
                {"question": "¿Qué edificio está al lado del estanque?", "options": ["El Palacio Real", "El Palacio de Cristal", "La biblioteca", "El hotel"], "answer": 1, "explanation": "The Crystal Palace ('el Palacio de Cristal')."},
                {"question": "¿De qué está hecho el Palacio de Cristal?", "options": ["De madera y piedra", "De cristal y metal", "De ladrillo", "De plástico"], "answer": 1, "explanation": "Made of glass and metal ('hecho de cristal y metal')."}
            ]
        },
        "exercises": [
            {
                "id": "d8-ex1",
                "type": "fill-in",
                "prompt": "Complete with the correct contraction: Voy ______ (a + el) supermercado.",
                "options": ["al", "a el", "del", "de el"],
                "correct": 0,
                "explanation": "'a + el' contracts to 'al'."
            },
            {
                "id": "d8-ex2",
                "type": "multiple-choice",
                "prompt": "How do you say 'I am an engineer' correctly in natural Spanish?",
                "options": ["Soy un ingeniero", "Soy ingeniero", "Estoy ingeniero", "Tengo ingeniero"],
                "correct": 1,
                "explanation": "Spanish drops the article with professions: 'Soy ingeniero'."
            },
            {
                "id": "d8-ex3",
                "type": "fill-in",
                "prompt": "Complete: El libro ______ (de + el) profesor está en la mesa.",
                "options": ["del", "de el", "al", "en el"],
                "correct": 0,
                "explanation": "'de + el' contracts to 'del'."
            },
            {
                "id": "d8-ex4",
                "type": "translation",
                "prompt": "Translate: 'For me, an orange juice, please.'",
                "options": ["Para mí, un zumo de naranja, por favor.", "Yo quiero zumo naranja gracias.", "Para me, el zumo naranja.", "Un zumo naranja de nada."],
                "correct": 0,
                "explanation": "'Para mí, un zumo de naranja, por favor' is the exact natural sentence."
            }
        ],
        "speakingChallenge": [
            {"prompt": "Order a coffee with milk and a croissant in a Spanish café.", "hint": "Para mí, un café con leche y...", "sampleAnswer": "Para mí, un café con leche y un cruasán, por favor."},
            {"prompt": "Say that you are going to the park today.", "hint": "Hoy voy al parque...", "sampleAnswer": "Hoy voy al parque a caminar."},
            {"prompt": "State your profession or that you are a student without using 'un'.", "hint": "Soy estudiante / Soy...", "sampleAnswer": "Soy estudiante de español."}
        ],
        "dailyRevision": {
            "quickQuestions": [
                "What are the only two mandatory contractions in Spanish? (al and del)",
                "Why don't we say 'Soy un estudiante' in Spanish?"
            ],
            "grammarRecall": "el/la/los/las (the) | un/una/unos/unas (a/some) | a + el = al | de + el = del.",
            "vocabRecall": ["Al", "Del", "El chico", "La chica", "El profesor", "El parque", "La tienda"]
        },
        "checklist": [
            "Mastered the 4 definite articles (el, la, los, las)",
            "Mastered the 4 indefinite articles (un, una, unos, unas)",
            "Applied the mandatory contractions 'al' and 'del'",
            "Learned to drop articles with professions",
            "Completed all 4 article exercises",
            "Practiced ordering tapas aloud in Spanish"
        ]
    },
    {
        "day": 9,
        "stage": 1,
        "title": "Basic Sentence Structure & Word Order",
        "subtitle": "Subject-Verb-Object, negative sentences with 'NO', and question structures",
        "goals": [
            "Understand standard Spanish word order: Subject + Verb + Object",
            "Create negative sentences easily by placing 'no' directly before the conjugated verb",
            "Form questions using intonation, inverted word order, and question tags (*¿verdad?*)",
            "Notice how adjectives naturally follow nouns (*el coche rojo*)"
        ],
        "bengaliNote": "In Bangla, verbs naturally come at the end of the sentence (যেমন: 'আমি ভাত খাই' - Subject + Object + Verb). But in Spanish, just like in English, verbs come in the middle: Subject + Verb + Object (যেমন: *Yo como arroz*). And negation is wonderfully simple: just put 'NO' in front of the verb!",
        "vocabulary": [
            {"word": "Sí / No", "translation": "Yes / No (or 'not')", "pos": "adverb", "gender": None, "example": "Sí, hablo español. / No, no hablo francés.", "exampleTranslation": "Yes, I speak Spanish. / No, I do not speak French."},
            {"word": "Siempre / Nunca", "translation": "Always / Never", "pos": "adverb", "gender": None, "example": "Siempre estudio por la mañana.", "exampleTranslation": "I always study in the morning."},
            {"word": "También / Tampoco", "translation": "Also, too / Neither, not either", "pos": "adverb", "gender": None, "example": "Yo también estudio español.", "exampleTranslation": "I also study Spanish."},
            {"word": "Comer", "translation": "To eat", "pos": "verb", "gender": None, "example": "Como arroz con verduras.", "exampleTranslation": "I eat rice with vegetables."},
            {"word": "Vivir", "translation": "To live", "pos": "verb", "gender": None, "example": "Vivo en un apartamento céntrico.", "exampleTranslation": "I live in a central apartment."},
            {"word": "Comprar", "translation": "To buy", "pos": "verb", "gender": None, "example": "Compro pan todos los días.", "exampleTranslation": "I buy bread every day."},
            {"word": "La casa", "translation": "The house / home", "pos": "noun", "gender": "feminine", "example": "Estoy en casa.", "exampleTranslation": "I am at home."},
            {"word": "El amigo / La amiga", "translation": "The friend", "pos": "noun", "gender": "masculine / feminine", "example": "Mi amigo vive en Madrid.", "exampleTranslation": "My friend lives in Madrid."},
            {"word": "¿Verdad? / ¿No?", "translation": "Right? / Isn't it? (tag questions)", "pos": "phrase", "gender": None, "example": "Tú eres de Bangladés, ¿verdad?", "exampleTranslation": "You are from Bangladesh, right?"},
            {"word": "Pero", "translation": "But", "pos": "conjunction", "gender": None, "example": "Estudio mucho, pero es fácil.", "exampleTranslation": "I study a lot, but it is easy."}
        ],
        "sentences": [
            {"spanish": "Carlos no come carne los viernes.", "english": "Carlos does not eat meat on Fridays."},
            {"spanish": "Yo no hablo alemán, pero hablo inglés.", "english": "I do not speak German, but I speak English."},
            {"spanish": "¿Tú vives en Madrid? —Sí, vivo en el centro.", "english": "Do you live in Madrid? —Yes, I live in the center."},
            {"spanish": "Ella nunca llega tarde a clase.", "english": "She never arrives late to class."},
            {"spanish": "Nosotros también queremos aprender español.", "english": "We also want to learn Spanish."},
            {"spanish": "Esta lección no es difícil, ¿verdad?", "english": "This lesson is not difficult, right?"}
        ],
        "grammar": {
            "title": "Sentence Architecture: Affirmation, Negation & Questions",
            "explanation": "Constructing sentences in Spanish is remarkably flexible, but mastering the core 3 formulas will allow you to express almost any thought with clarity.",
            "rules": [
                "Affirmative Formula: [Subject] + [Verb] + [Object/Complement]. E.g. *Sakib aprende español en Madrid.* Remember: the subject can be omitted! (*Aprende español en Madrid.*)",
                "Negative Formula: [Subject] + NO + [Verb] + [Object]. The word 'no' MUST go directly before the conjugated verb! E.g. *Sakib NO habla alemán.*",
                "Double 'No' in Answers: When answering 'No' to a question, use 'No' twice: the first is the interjection, the second negates the verb. E.g. *—¿Hablas ruso? —No, no hablo ruso.*",
                "Forming Questions: 1) Simply raise your voice pitch at the end: *¿Tú vives aquí?* 2) Invert Verb and Subject: *¿Vives tú aquí?* 3) Add tag question: *Tú vives aquí, ¿verdad?*",
                "Adjective Placement: Adjectives usually come AFTER the noun: *un libro interesante*, *una casa blanca*."
            ],
            "structures": [
                "Statement: Sujeto + Verbo + Objeto (Yo compro pan)",
                "Negative: Sujeto + NO + Verbo + Objeto (Yo NO compro pan)",
                "Question Inversion: ¿Verbo + Sujeto + Objeto? (¿Comprende usted la pregunta?)",
                "Question Tag: [Frase afirmativa], ¿verdad? / ¿no?"
            ],
            "examples": [
                {"spanish": "Sakib vive en Madrid.", "english": "Sakib lives in Madrid."},
                {"spanish": "Sakib no vive en Barcelona.", "english": "Sakib does not live in Barcelona."},
                {"spanish": "¿Vive Sakib en Madrid?", "english": "Does Sakib live in Madrid?"},
                {"spanish": "Sakib vive en Madrid, ¿verdad?", "english": "Sakib lives in Madrid, right?"}
            ],
            "commonMistakes": [
                {"wrong": "Yo hablo no español", "right": "Yo no hablo español", "explanation": "'No' must be placed directly BEFORE the conjugated verb."},
                {"wrong": "El rojo coche", "right": "El coche rojo", "explanation": "In Spanish, descriptive adjectives follow the noun."}
            ],
            "proTip": "In Spanish, you don't need auxiliary verbs like 'do' or 'does' in English! To say 'Do you speak Spanish?', you don't say 'Do you'; you just ask '¿Hablas español?' with rising intonation!"
        },
        "conversation": {
            "title": "Chatting Between Classes",
            "context": "Mateo and Sakib compare their daily routines outside the library.",
            "dialogue": [
                {"speaker": "Mateo", "role": "Friend", "spanish": "Sakib, ¿tú comes en la universidad o en casa?", "english": "Sakib, do you eat at university or at home?"},
                {"speaker": "Sakib", "role": "Student", "spanish": "Normalmente no como en la universidad, como en casa.", "english": "Normally I do not eat at university, I eat at home."},
                {"speaker": "Mateo", "role": "Friend", "spanish": "¿Y cocinas tú todos los días?", "english": "And do you cook every day?"},
                {"speaker": "Sakib", "role": "Student", "spanish": "Sí, me gusta cocinar comida bengalí. Es muy rica.", "english": "Yes, I like to cook Bengali food. It is very delicious."},
                {"speaker": "Mateo", "role": "Friend", "spanish": "¡Qué interesante! Yo no sé cocinar nada, siempre compro comida preparada.", "english": "How interesting! I don't know how to cook anything, I always buy prepared food."},
                {"speaker": "Sakib", "role": "Student", "spanish": "Un día cocino para ti, ¿vale?", "english": "One day I'll cook for you, okay?"},
                {"speaker": "Mateo", "role": "Friend", "spanish": "¡Hecho! Muchas gracias, amigo.", "english": "Done / Deal! Thank you very much, friend."}
            ],
            "keyPhrases": [
                {"phrase": "¿Vale?", "explanation": "Spain's most famous filler word meaning 'Okay?' or 'Agreed?'"},
                {"phrase": "¡Hecho!", "explanation": "'Done!' / 'Deal!' indicating enthusiastic agreement."},
                {"phrase": "Normalmente", "explanation": "'Normally' / 'Usually'."}
            ]
        },
        "reading": {
            "title": "La rutina sencilla de Sakib",
            "passage": "Sakib vive en un piso luminoso cerca del centro de Madrid. No tiene coche porque en Madrid el metro funciona muy bien. Por las mañanas estudia español en la academia y por las tardes hace sus ejercicios. No bebe café, pero bebe mucho té caliente. Los fines de semana pasea por la ciudad con sus amigos. Sakib está muy contento con su progreso: comprende las frases básicas y no tiene miedo de hablar.",
            "translation": "Sakib lives in a bright apartment near the center of Madrid. He does not have a car because in Madrid the subway works very well. In the mornings he studies Spanish at the academy and in the afternoons he does his exercises. He does not drink coffee, but he drinks a lot of hot tea. On weekends he strolls through the city with his friends. Sakib is very happy with his progress: he understands basic sentences and is not afraid to speak.",
            "questions": [
                {"question": "¿Por qué Sakib no tiene coche?", "options": ["Porque es caro", "Porque el metro funciona muy bien", "Porque no sabe conducir", "Porque no le gustan los coches"], "answer": 1, "explanation": "Because the subway works very well ('el metro funciona muy bien')."},
                {"question": "¿Qué bebe Sakib?", "options": ["Café frío", "Mucho té caliente", "Solo agua", "Refrescos"], "answer": 1, "explanation": "He drinks hot tea ('bebe mucho té caliente')."},
                {"question": "¿De qué no tiene miedo Sakib?", "options": ["De los exámenes", "De hablar", "De perderse", "De la profesora"], "answer": 1, "explanation": "He is not afraid to speak ('no tiene miedo de hablar')."}
            ]
        },
        "exercises": [
            {
                "id": "d9-ex1",
                "type": "multiple-choice",
                "prompt": "Where does 'no' go to make a Spanish sentence negative?",
                "options": ["At the very end of the sentence", "Directly before the conjugated verb", "Directly after the conjugated verb", "Before the object"],
                "correct": 1,
                "explanation": "'No' is placed directly before the conjugated verb: 'Yo no hablo'."
            },
            {
                "id": "d9-ex2",
                "type": "fill-in",
                "prompt": "Turn into negative: Yo como carne. -> Yo ______ como carne.",
                "options": ["no", "nunca no", "no nada", "tampoco no"],
                "correct": 0,
                "explanation": "Simply add 'no' before the verb: 'Yo no como carne'."
            },
            {
                "id": "d9-ex3",
                "type": "multiple-choice",
                "prompt": "How do you say 'You live in Madrid, right?'",
                "options": ["¿Tú vives en Madrid, verdad?", "¿Vives tú en Madrid no?", "¿Dónde vives en Madrid verdad?", "¿Por qué vives en Madrid verdad?"],
                "correct": 0,
                "explanation": "'¿Tú vives en Madrid, verdad?' uses the natural tag question '¿verdad?'."
            },
            {
                "id": "d9-ex4",
                "type": "translation",
                "prompt": "Translate: 'I do not speak German, but I speak English.'",
                "options": ["No hablo alemán, pero hablo inglés.", "Hablo no alemán, y hablo inglés.", "Yo alemán no, pero inglés sí.", "No hablar alemán, pero hablar inglés."],
                "correct": 0,
                "explanation": "'No hablo alemán, pero hablo inglés' is grammatically perfect."
            }
        ],
        "speakingChallenge": [
            {"prompt": "Say two things you do NOT do in Spanish using 'no'.", "hint": "No fumo, no bebo alcohol...", "sampleAnswer": "No fumo y no como carne roja."},
            {"prompt": "Ask someone if they live here using a tag question.", "hint": "Tú vives aquí, ¿verdad?", "sampleAnswer": "¿Tú vives en este barrio, verdad?"},
            {"prompt": "Say that you also study Spanish.", "hint": "Yo también estudio...", "sampleAnswer": "Yo también estudio español todos los días."}
        ],
        "dailyRevision": {
            "quickQuestions": [
                "Does Spanish need auxiliary words like 'do/does' to ask questions?",
                "Where do descriptive adjectives usually go in relation to nouns?"
            ],
            "grammarRecall": "Affirmative: S + V + O | Negative: S + NO + V + O | Questions: Inversion or rising pitch.",
            "vocabRecall": ["Sí", "No", "Siempre", "Nunca", "También", "Tampoco", "¿Verdad?", "Pero"]
        },
        "checklist": [
            "Constructed standard Subject-Verb-Object sentences",
            "Formed clean negative sentences with 'no'",
            "Learned that Spanish does not need auxiliary 'do/does'",
            "Used tag questions (¿verdad? / ¿no?)",
            "Placed descriptive adjectives after nouns",
            "Passed all 4 sentence structure exercises"
        ]
    },
    {
        "day": 10,
        "stage": 1,
        "title": "Introduction to SER vs. ESTAR",
        "subtitle": "Essence vs. State: The two Spanish verbs for 'To Be' + Stage 1 Milestone Assessment",
        "goals": [
            "Conjugate both SER and ESTAR fully in the present tense",
            "Understand the fundamental difference: SER = permanent essence/identity; ESTAR = temporary state/location",
            "Learn the DOCTOR (Ser) and PLACE (Estar) memory frameworks",
            "Complete the Stage 1 Milestone Assessment (Days 1–10 comprehensive test)"
        ],
        "bengaliNote": "English has only one verb 'to be' (am/is/are), which confuses native English speakers. But in Spanish, identity (*আমি সাকিব / I am Sakib* = SER) is completely different from location or mood (*আমি ভালো আছি / I am in Madrid / I am happy* = ESTAR). Think: SER defines WHAT you are; ESTAR describes HOW or WHERE you are!",
        "vocabulary": [
            {"word": "Ser", "translation": "To be (permanent essence, identity, origin, profession)", "pos": "verb", "gender": None, "example": "Yo soy estudiante.", "exampleTranslation": "I am a student."},
            {"word": "Estar", "translation": "To be (temporary state, condition, emotion, location)", "pos": "verb", "gender": None, "example": "Estoy muy contento hoy.", "exampleTranslation": "I am very happy today."},
            {"word": "Soy, Eres, Es", "translation": "I am, you are, he/she/it is (Ser)", "pos": "verb form", "gender": None, "example": "Ella es de España.", "exampleTranslation": "She is from Spain."},
            {"word": "Somos, Sois, Son", "translation": "We are, you all are, they are (Ser)", "pos": "verb form", "gender": None, "example": "Nosotros somos amigos.", "exampleTranslation": "We are friends."},
            {"word": "Estoy, Estás, Está", "translation": "I am, you are, he/she/it is (Estar)", "pos": "verb form", "gender": None, "example": "¿Dónde estás?", "exampleTranslation": "Where are you?"},
            {"word": "Estamos, Estáis, Están", "translation": "We are, you all are, they are (Estar)", "pos": "verb form", "gender": None, "example": "Estamos en clase.", "exampleTranslation": "We are in class."},
            {"word": "Cansado / Cansada", "translation": "Tired (condition -> Estar)", "pos": "adjective", "gender": "masculine / feminine", "example": "Estoy un poco cansado.", "exampleTranslation": "I am a little tired."},
            {"word": "Listo / Lista", "translation": "Ready (with Estar) / Clever (with Ser)", "pos": "adjective", "gender": "masculine / feminine", "example": "Estoy listo para empezar.", "exampleTranslation": "I am ready to start."},
            {"word": "Ocupado / Ocupada", "translation": "Busy (condition -> Estar)", "pos": "adjective", "gender": "masculine / feminine", "example": "El profesor está ocupado ahora.", "exampleTranslation": "The professor is busy right now."},
            {"word": "Feliz / Contento", "translation": "Happy / Glad (emotion -> Estar/Ser)", "pos": "adjective", "gender": None, "example": "Estoy muy contento con mi progreso.", "exampleTranslation": "I am very happy with my progress."}
        ],
        "sentences": [
            {"spanish": "Yo soy Sakib y soy de Bangladés.", "english": "I am Sakib and I am from Bangladesh. (Identity & Origin -> SER)"},
            {"spanish": "Ahora estoy en Madrid y estoy muy contento.", "english": "Now I am in Madrid and I am very happy. (Location & Mood -> ESTAR)"},
            {"spanish": "¿Dónde estás? —Estoy en la biblioteca.", "english": "Where are you? —I am in the library. (Location -> ESTAR)"},
            {"spanish": "Mi hermana es médica y es muy inteligente.", "english": "My sister is a doctor and is very intelligent. (Profession & Characteristic -> SER)"},
            {"spanish": "Hoy estoy un poco cansado de estudiar.", "english": "Today I am a little tired of studying. (Temporary physical state -> ESTAR)"},
            {"spanish": "El café está caliente.", "english": "The coffee is hot. (Current condition -> ESTAR)"}
        ],
        "grammar": {
            "title": "The Master Guide to SER vs. ESTAR",
            "explanation": "Mastering the divide between SER and ESTAR is the single most celebrated milestone of A1 Spanish! Use the proven **D.O.C.T.O.R.** and **P.L.A.C.E.** acronyms.",
            "rules": [
                "SER is for D.O.C.T.O.R.: Description (alto, bajo), Occupation (profesor, estudiante), Characteristic (simpático, inteligente), Time/Date (son las tres, hoy es lunes), Origin (soy de Bangladés), Relationship (es mi hermano).",
                "ESTAR is for P.L.A.C.E.: Position (sentado, de pie), Location (en Madrid, en casa), Action (progressive: estoy hablando), Condition (cansado, enfermo, roto), Emotion (triste, contento, feliz).",
                "Conjugation of SER: yo soy, tú eres, él/ella/usted es, nosotros somos, vosotros sois, ellos/ellas/ustedes son.",
                "Conjugation of ESTAR: yo estoy, tú estás, él/ella/usted está, nosotros estamos, vosotros estáis, ellos/ellas/ustedes están.",
                "Notice the accent marks on ESTAR: estás, está, estáis, están! Without the accent, 'esta' means 'this' (esta mesa)!"
            ],
            "structures": [
                "SER Conjugation: soy | eres | es | somos | sois | son",
                "ESTAR Conjugation: estoy | estás | está | estamos | estáis | están",
                "SER: What something IS by nature (Identity, Origin, Profession)",
                "ESTAR: How or where something IS right now (State, Location, Feeling)"
            ],
            "examples": [
                {"spanish": "Soy estudiante. (Ser: Profession)", "english": "I am a student."},
                {"spanish": "Estoy en la cafetería. (Estar: Location)", "english": "I am in the cafeteria."},
                {"spanish": "Carlos es moreno. (Ser: Physical trait)", "english": "Carlos is dark-haired."},
                {"spanish": "Carlos está enfermo hoy. (Estar: Temporary condition)", "english": "Carlos is sick today."}
            ],
            "commonMistakes": [
                {"wrong": "Soy en Madrid", "right": "Estoy en Madrid", "explanation": "Geographic location ALWAYS takes 'estar', never 'ser'."},
                {"wrong": "Estoy profesor", "right": "Soy profesor", "explanation": "Professions define one's social identity, so they strictly take 'ser'."},
                {"wrong": "Hoy es cansado", "right": "Hoy estoy cansado", "explanation": "Tiredness is a temporary physical state, so it takes 'estar'."}
            ],
            "proTip": "Watch out for meaning changers! *Ser listo* = To be smart/clever. *Estar listo* = To be ready! *Ser aburrido* = To be boring. *Estar aburrido* = To be bored!"
        },
        "conversation": {
            "title": "Catching Up After Class",
            "context": "Sakib meets Lucía on the university steps.",
            "dialogue": [
                {"speaker": "Lucía", "role": "Classmate", "spanish": "¡Hola, Sakib! ¿Cómo estás hoy?", "english": "Hello, Sakib! How are you today?"},
                {"speaker": "Sakib", "role": "Student", "spanish": "¡Hola, Lucía! Estoy muy bien, pero un poco cansado. ¿Y tú?", "english": "Hello, Lucia! I am very well, but a little tired. And you?"},
                {"speaker": "Lucía", "role": "Classmate", "spanish": "Yo estoy bien también. Oye, ¿dónde está Carlos?", "english": "I am well too. Hey, where is Carlos?"},
                {"speaker": "Sakib", "role": "Student", "spanish": "Carlos está en la biblioteca. Es un chico muy estudioso.", "english": "Carlos is in the library. He is a very studious boy."},
                {"speaker": "Lucía", "role": "Classmate", "spanish": "Es verdad. ¿Estás listo para el café de la tarde?", "english": "That's true. Are you ready for afternoon coffee?"},
                {"speaker": "Sakib", "role": "Student", "spanish": "¡Sí, estoy listísimo! Vamos.", "english": "Yes, I am completely ready! Let's go."}
            ],
            "keyPhrases": [
                {"phrase": "¿Cómo estás?", "explanation": "Asking how someone is feeling right now (Estar)."},
                {"phrase": "Es un chico muy estudioso", "explanation": "Describing character/personality (Ser)."},
                {"phrase": "¿Estás listo?", "explanation": "'Are you ready?' (Estar listo)."}
            ]
        },
        "reading": {
            "title": "Stage 1 Capstone Story: La nueva vida de Sakib",
            "passage": "Sakib tiene veinticuatro años y es de Bangladés. Ahora vive en Madrid. Su piso es pequeño pero muy luminoso. En su mesa de estudio hay tres libros de español, un mapa de la ciudad y una foto de su familia. Hoy es diez de octubre. Son las diez de la mañana y Sakib está en la cocina preparando té. Está muy contento porque comprende las lecciones básicas de español: los saludos, los números, los artículos y la diferencia entre ser y estar. Sabe que el camino es largo, pero su motivación es enorme. ¡Ha completado los primeros diez días del desafío!",
            "translation": "Sakib is twenty-four years old and is from Bangladesh. Now he lives in Madrid. His apartment is small but very bright. On his study table there are three Spanish books, a city map, and a photo of his family. Today is October tenth. It is ten in the morning and Sakib is in the kitchen preparing tea. He is very happy because he understands the basic lessons of Spanish: greetings, numbers, articles, and the difference between ser and estar. He knows the journey is long, but his motivation is enormous. He has completed the first ten days of the challenge!",
            "questions": [
                {"question": "¿Dónde está Sakib a las diez de la mañana?", "options": ["En el metro", "En la cocina preparando té", "En el parque", "En el banco"], "answer": 1, "explanation": "He is in the kitchen preparing tea ('está en la cocina preparando té')."},
                {"question": "¿Por qué está contento Sakib?", "options": ["Porque tiene un coche nuevo", "Porque comprende las lecciones básicas de español", "Porque es viernes", "Porque no hay clase"], "answer": 1, "explanation": "Because he understands the basic Spanish lessons."},
                {"question": "¿Cuántos días del desafío ha completado Sakib hoy?", "options": ["Cinco días", "Diez días", "Veinte días", "Treinta días"], "answer": 1, "explanation": "He has completed the first ten days ('los primeros diez días')!"}
            ]
        },
        "exercises": [
            {
                "id": "d10-ex1",
                "type": "fill-in",
                "prompt": "Choose Ser or Estar: Yo ______ de Bangladés. (Origin)",
                "options": ["soy", "estoy", "es", "está"],
                "correct": 0,
                "explanation": "Origin takes 'ser': 'Yo soy de Bangladés'."
            },
            {
                "id": "d10-ex2",
                "type": "fill-in",
                "prompt": "Choose Ser or Estar: Ahora nosotros ______ en Madrid. (Location)",
                "options": ["somos", "estamos", "están", "son"],
                "correct": 1,
                "explanation": "Location takes 'estar': 'Nosotros estamos en Madrid'."
            },
            {
                "id": "d10-ex3",
                "type": "multiple-choice",
                "prompt": "What does 'Carlos está listo' mean?",
                "options": ["Carlos is smart/clever", "Carlos is ready", "Carlos is boring", "Carlos is bored"],
                "correct": 1,
                "explanation": "'Estar listo' means 'to be ready'. ('Ser listo' means to be clever)."
            },
            {
                "id": "d10-ex4",
                "type": "translation",
                "prompt": "Translate: 'The teacher is busy today.'",
                "options": ["El profesor está ocupado hoy.", "El profesor es ocupado hoy.", "El profesor tiene ocupado hoy.", "El profesor va ocupado hoy."],
                "correct": 0,
                "explanation": "Temporary condition takes 'estar': 'El profesor está ocupado hoy'."
            }
        ],
        "speakingChallenge": [
            {"prompt": "Describe your identity and profession using SER.", "hint": "Yo soy...", "sampleAnswer": "Yo soy Sakib y soy estudiante de idiomas."},
            {"prompt": "Describe your current location and how you feel using ESTAR.", "hint": "Estoy en... y estoy...", "sampleAnswer": "Estoy en mi habitación y estoy muy contento y motivado."},
            {"prompt": "Explain the difference between 'Ser listo' and 'Estar listo' in your own words.", "hint": "Clever vs ready.", "sampleAnswer": "'Ser listo' significa ser inteligente; 'estar listo' significa estar preparado."}
        ],
        "dailyRevision": {
            "quickQuestions": [
                "What does the acronym DOCTOR stand for? (Description, Occupation, Characteristic, Time, Origin, Relationship)",
                "What does the acronym PLACE stand for? (Position, Location, Action, Condition, Emotion)"
            ],
            "grammarRecall": "SER: soy, eres, es, somos, sois, son | ESTAR: estoy, estás, está, estamos, estáis, están.",
            "vocabRecall": ["Ser", "Estar", "Soy", "Estoy", "Cansado", "Listo", "Ocupado", "Feliz"]
        },
        "checklist": [
            "Conjugated SER in all 6 present tense forms",
            "Conjugated ESTAR in all 6 present tense forms",
            "Mastered DOCTOR for Ser and PLACE for Estar",
            "Understood the meaning difference of 'listo' with Ser vs Estar",
            "Completed the Stage 1 Milestone Reading Passage",
            "CELEBRATED COMPLETING STAGE 1 (DAYS 1–10) OF THE 60-DAY CHALLENGE! 🎉"
        ]
    }
]

# Combine both parts
stage1_complete = stage1_days + stage1_part2

with open("d:/ag/espanol-handbook/data/lessons/stage1.js", "w", encoding="utf-8") as f:
    f.write("// Stage 1: Days 1 to 10 (Foundations of Spanish)\n")
    f.write("window.STAGE_1_LESSONS = ")
    json.dump(stage1_complete, f, ensure_ascii=False, indent=2)
    f.write(";\n")

print(f"Successfully generated stage1.js with all {len(stage1_complete)} full days!")
