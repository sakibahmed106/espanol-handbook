"""
Build Stage 2: Days 16 to 20 + Combine Stage 2 into data/lessons/stage2.js
"""
import json
from build_stage2_part1 import stage2_days

stage2_part2 = [
    {
        "day": 16,
        "stage": 2,
        "title": "Regular Present Tense: -ER & -IR Verbs",
        "subtitle": "Conjugating Comer, Beber, Aprender, Vivir, Escribir, Abrir",
        "goals": [
            "Conjugate regular -ER verbs (comer, beber, aprender, comprender)",
            "Conjugate regular -IR verbs (vivir, escribir, abrir, subir)",
            "Compare -ER vs. -IR endings: notice they are identical EXCEPT for nosotros (-emos vs. -imos) and vosotros (-éis vs. -ís)",
            "Construct multi-clause sentences combining -AR, -ER, and -IR verbs"
        ],
        "bengaliNote": "-ER and -IR verbs are fraternal twins! Their endings are identical in 4 out of 6 persons (-o, -es, -e, -en). Only 'nosotros' (-emos vs. -imos) and 'vosotros' (-éis vs. -ís) reveal their true identity. In Bangla, think of them as two closely related verb families.",
        "vocabulary": [
            {"word": "Comer", "translation": "To eat", "pos": "verb", "gender": None, "example": "Como una manzana por la mañana.", "exampleTranslation": "I eat an apple in the morning."},
            {"word": "Beber", "translation": "To drink", "pos": "verb", "gender": None, "example": "¿Qué bebes con la comida?", "exampleTranslation": "What do you drink with the meal?"},
            {"word": "Aprender", "translation": "To learn", "pos": "verb", "gender": None, "example": "Aprendemos vocabulario nuevo cada día.", "exampleTranslation": "We learn new vocabulary every day."},
            {"word": "Comprender", "translation": "To understand / comprehend", "pos": "verb", "gender": None, "example": "Comprendo las reglas de gramática.", "exampleTranslation": "I understand the grammar rules."},
            {"word": "Vivir", "translation": "To live", "pos": "verb", "gender": None, "example": "¿Dónde vives tú?", "exampleTranslation": "Where do you live?"},
            {"word": "Escribir", "translation": "To write", "pos": "verb", "gender": None, "example": "Escribo notas en mi cuaderno.", "exampleTranslation": "I write notes in my notebook."},
            {"word": "Abrir", "translation": "To open", "pos": "verb", "gender": None, "example": "El supermercado abre a las nueve.", "exampleTranslation": "The supermarket opens at nine."},
            {"word": "Subir", "translation": "To go up / To climb / To upload", "pos": "verb", "gender": None, "example": "Subo por las escaleras.", "exampleTranslation": "I go up by the stairs."},
            {"word": "Leer", "translation": "To read", "pos": "verb", "gender": None, "example": "Leo un artículo interesante.", "exampleTranslation": "I read an interesting article."},
            {"word": "Decidir", "translation": "To decide", "pos": "verb", "gender": None, "example": "Decido estudiar más tiempo.", "exampleTranslation": "I decide to study more time."}
        ],
        "sentences": [
            {"spanish": "Vivo en Madrid y aprendo español todos los días.", "english": "I live in Madrid and I learn Spanish every day."},
            {"spanish": "¿Qué comes al mediodía? —Normalmente como arroz con pollo.", "english": "What do you eat at noon? —Normally I eat rice with chicken."},
            {"spanish": "Nosotros vivimos en un piso compartido cerca del centro.", "english": "We live in a shared flat near the center."},
            {"spanish": "Los profesores escriben ejemplos en la pizarra.", "english": "The teachers write examples on the board."},
            {"spanish": "Ella no bebe café, solo bebe agua y té.", "english": "She does not drink coffee, she only drinks water and tea."},
            {"spanish": "¿Comprendéis la explicación de la profesora?", "english": "Do you all understand the teacher's explanation? (Spain informal plural)"}
        ],
        "grammar": {
            "title": "The Master -ER and -IR Conjugation Charts",
            "explanation": "Look at how closely -ER and -IR verbs parallel each other:",
            "rules": [
                "-ER Endings: -o, -es, -e, -emos, -éis, -en (COMER: como, comes, come, comemos, coméis, comen).",
                "-IR Endings: -o, -es, -e, -imos, -ís, -en (VIVIR: vivo, vives, vive, vivimos, vivís, viven).",
                "The Twin Comparison: Notice that yo (-o), tú (-es), él/ella/usted (-e), and ellos/ustedes (-en) are IDENTICAL for both -ER and -IR!",
                "The Only Two Differences: 1) Nosotros: -emos for -ER (*comemos*) vs. -imos for -IR (*vivimos*). 2) Vosotros: -éis for -ER (*coméis*) vs. -ís for -IR (*vivís*)."
            ],
            "structures": [
                "-ER Chart: como | comes | come | comemos | coméis | comen",
                "-IR Chart: vivo | vives | vive | vivimos | vivís | viven",
                "Twin rule: Only Nosotros & Vosotros differ between -ER and -IR!"
            ],
            "examples": [
                {"spanish": "Yo como paella los domingos.", "english": "I eat paella on Sundays."},
                {"spanish": "Tú vives muy cerca de aquí.", "english": "You live very close to here."},
                {"spanish": "Nosotros aprendemos muchas palabras.", "english": "We learn many words."},
                {"spanish": "Ellos escriben mensajes en el móvil.", "english": "They write messages on the mobile phone."}
            ],
            "commonMistakes": [
                {"wrong": "Nosotros vivamos (present tense)", "right": "Nosotros vivimos", "explanation": "Regular -IR verbs take '-imos' in the present tense."},
                {"wrong": "Yo coma (in present indicative)", "right": "Yo como", "explanation": "First person singular present is always '-o' for indicative regular verbs."}
            ],
            "proTip": "Now that you know -AR, -ER, and -IR, you can conjugate literally thousands of regular Spanish verbs! All Spanish verbs without exception belong to one of these three families."
        },
        "conversation": {
            "title": "Discussing Daily Habits and Diet",
            "context": "Sakib and his friend Mateo compare what they eat and where they live.",
            "dialogue": [
                {"speaker": "Mateo", "role": "Friend", "spanish": "Sakib, ¿dónde vives exactamente en Madrid?", "english": "Sakib, where exactly do you live in Madrid?"},
                {"speaker": "Sakib", "role": "Student", "spanish": "Vivo en Chamberí, en la calle Santa Engracia. ¿Y tú?", "english": "I live in Chamberí, on Santa Engracia street. And you?"},
                {"speaker": "Mateo", "role": "Friend", "spanish": "Yo vivo en Moncloa. Oye, ¿qué comes normalmente en casa?", "english": "I live in Moncloa. Hey, what do you normally eat at home?"},
                {"speaker": "Sakib", "role": "Student", "spanish": "Casi siempre como arroz, lentejas y verduras. A veces como pescado.", "english": "Almost always I eat rice, lentils, and vegetables. Sometimes I eat fish."},
                {"speaker": "Mateo", "role": "Friend", "spanish": "¿Y qué bebes?", "english": "And what do you drink?"},
                {"speaker": "Sakib", "role": "Student", "spanish": "Bebo mucha agua y té negro. No bebo refrescos con azúcar.", "english": "I drink a lot of water and black tea. I don't drink sugary soft drinks."},
                {"speaker": "Mateo", "role": "Friend", "spanish": "¡Qué sano! Yo debería aprender de ti.", "english": "How healthy! I should learn from you."}
            ],
            "keyPhrases": [
                {"phrase": "Casi siempre", "explanation": "'Almost always'."},
                {"phrase": "A veces", "explanation": "'Sometimes'."},
                {"phrase": "¡Qué sano!", "explanation": "'How healthy!'"}
            ]
        },
        "reading": {
            "title": "Hábitos saludables de un estudiante",
            "passage": "Llevar una vida saludable es esencial para rendir bien en los estudios. Sakib vive según una rutina equilibrada. Todos los días se despierta temprano, bebe un vaso grande de agua y toma un desayuno nutritivo. En la escuela de idiomas aprende vocabulario y lee textos interesantes en español. Escribe oraciones nuevas en su diario personal. Al mediodía come con sus compañeros en el parque cuando hace sol. No come comida rápida porque prefiere cocinar comida fresca en su cocina.",
            "translation": "Leading a healthy life is essential to perform well in studies. Sakib lives according to a balanced routine. Every day he wakes up early, drinks a big glass of water, and has a nutritious breakfast. At the language school he learns vocabulary and reads interesting texts in Spanish. He writes new sentences in his personal diary. At noon he eats with his classmates in the park when it is sunny. He does not eat fast food because he prefers to cook fresh food in his kitchen.",
            "questions": [
                {"question": "¿Qué bebe Sakib al despertarse?", "options": ["Café solo", "Un vaso grande de agua", "Zumo de piña", "Leche fría"], "answer": 1, "explanation": "A big glass of water ('un vaso grande de agua')."},
                {"question": "¿Dónde escribe Sakib sus oraciones nuevas?", "options": ["En la pared", "En su diario personal", "En el móvil", "En una servilleta"], "answer": 1, "explanation": "In his personal diary ('en su diario personal')."},
                {"question": "¿Por qué Sakib no come comida rápida?", "options": ["Porque es cara", "Porque prefiere cocinar comida fresca", "Porque está cerrada", "Porque no tiene tiempo"], "answer": 1, "explanation": "Because he prefers to cook fresh food ('prefiere cocinar comida fresca')."}
            ]
        },
        "exercises": [
            {
                "id": "d16-ex1",
                "type": "fill-in",
                "prompt": "Conjugate COMER for 'tú': ¿Qué ______ tú al mediodía?",
                "options": ["comes", "como", "come", "comemos"],
                "correct": 0,
                "explanation": "Tú form for -ER verbs ends in -es: 'comes'."
            },
            {
                "id": "d16-ex2",
                "type": "fill-in",
                "prompt": "Conjugate VIVIR for 'nosotros': Nosotros ______ en Madrid.",
                "options": ["vivimos", "vivemos", "viven", "vivís"],
                "correct": 0,
                "explanation": "Nosotros form for -IR verbs ends in -imos: 'vivimos'."
            },
            {
                "id": "d16-ex3",
                "type": "multiple-choice",
                "prompt": "Which ending is identical for both -ER and -IR verbs in the 'yo' form?",
                "options": ["-o", "-es", "-e", "-en"],
                "correct": 0,
                "explanation": "Both -ER and -IR (and -AR) verbs take '-o' in the 'yo' form."
            },
            {
                "id": "d16-ex4",
                "type": "translation",
                "prompt": "Translate: 'We learn Spanish and they write letters.'",
                "options": ["Aprendemos español y ellos escriben cartas.", "Aprenden español y nosotros escribimos cartas.", "Aprende español y escribe cartas.", "Aprendéis español y ellos escriben cartas."],
                "correct": 0,
                "explanation": "'Aprendemos español y ellos escriben cartas' accurately conjugates both verbs."
            }
        ],
        "speakingChallenge": [
            {"prompt": "Say what you normally eat and drink for lunch in Spanish.", "hint": "Normalmente como... y bebo...", "sampleAnswer": "Normalmente como arroz con pollo y bebo agua mineral."},
            {"prompt": "State where you live and what you are learning.", "hint": "Vivo en... y aprendo...", "sampleAnswer": "Vivo en Madrid y aprendo español cada día."},
            {"prompt": "Conjugate COMER and VIVIR for 'nosotros' out loud.", "hint": "Comemos, vivimos.", "sampleAnswer": "Nosotros comemos y nosotros vivimos."}
        ],
        "dailyRevision": {
            "quickQuestions": [
                "What are the only two persons where -ER and -IR verb endings differ? (nosotros and vosotros)",
                "What is the 'ellos' ending for both -ER and -IR verbs? (-en)"
            ],
            "grammarRecall": "-ER: -o, -es, -e, -emos, -éis, -en | -IR: -o, -es, -e, -imos, -ís, -en.",
            "vocabRecall": ["Comer", "Beber", "Aprender", "Vivir", "Escribir", "Abrir", "Leer"]
        },
        "checklist": [
            "Conjugated regular -ER verbs across all persons",
            "Conjugated regular -IR verbs across all persons",
            "Identified the difference in nosotros (-emos vs -imos)",
            "Mastered the vosotros forms (-éis vs -ís)",
            "Completed all 4 verb exercises",
            "Practiced expressing dietary habits out loud"
        ]
    },
    {
        "day": 17,
        "stage": 2,
        "title": "The Irregular Verb TENER & Idioms",
        "subtitle": "Conjugating TENER and expressing hunger, thirst, cold, heat, fear, and age",
        "goals": [
            "Conjugate the highly irregular verb TENER in all 6 present tense forms",
            "Understand that TENER is both an 'yo-go' verb (*tengo*) and an 'e->ie' stem changer (*tienes, tiene*)",
            "Master Spanish idiomatic expressions using TENER (tener frío, calor, prisa, miedo, sueño)",
            "Express desire using 'Tener ganas de + infinitive'"
        ],
        "bengaliNote": "In English, you say 'I am cold' or 'I am afraid'. But in Spanish (and very similarly to Bangla: 'আমার শীত লাগছে / আমার ভয় করছে'), you don't say you *are* the condition — you say you *have* it (*Tengo frío*, *Tengo miedo*).",
        "vocabulary": [
            {"word": "Tener", "translation": "To have / To possess", "pos": "verb", "gender": None, "example": "Tengo una idea excelente.", "exampleTranslation": "I have an excellent idea."},
            {"word": "Tengo, Tienes, Tiene", "translation": "I have, you have, he/she has", "pos": "verb form", "gender": None, "example": "¿Tienes un bolígrafo?", "exampleTranslation": "Do you have a pen?"},
            {"word": "Tenemos, Tenéis, Tienen", "translation": "We have, you all have, they have", "pos": "verb form", "gender": None, "example": "Tenemos clase a las diez.", "exampleTranslation": "We have class at ten."},
            {"word": "Tener frío / calor", "translation": "To be cold / To be warm/hot", "pos": "phrase", "gender": None, "example": "Cierra la ventana, tengo frío.", "exampleTranslation": "Close the window, I am cold."},
            {"word": "Tener prisa", "translation": "To be in a hurry", "pos": "phrase", "gender": None, "example": "No puedo hablar ahora, tengo prisa.", "exampleTranslation": "I cannot talk right now, I am in a hurry."},
            {"word": "Tener miedo", "translation": "To be afraid / scared", "pos": "phrase", "gender": None, "example": "No tengas miedo de cometer errores.", "exampleTranslation": "Don't be afraid to make mistakes."},
            {"word": "Tener sueño", "translation": "To be sleepy", "pos": "phrase", "gender": None, "example": "Son las doce de la noche y tengo sueño.", "exampleTranslation": "It is midnight and I am sleepy."},
            {"word": "Tener razón", "translation": "To be right (correct)", "pos": "phrase", "gender": None, "example": "Sí, tienes toda la razón.", "exampleTranslation": "Yes, you are completely right."},
            {"word": "Tener suerte", "translation": "To be lucky", "pos": "phrase", "gender": None, "example": "¡Qué suerte tienes!", "exampleTranslation": "What luck you have! (How lucky you are!)"},
            {"word": "Tener ganas de (+ inf)", "translation": "To feel like / To fancy doing something", "pos": "phrase", "gender": None, "example": "Tengo ganas de comer una paella.", "exampleTranslation": "I feel like eating a paella."}
        ],
        "sentences": [
            {"spanish": "Tengo veinticuatro años y tengo muchas metas.", "english": "I am twenty-four years old and I have many goals."},
            {"spanish": "¿Tienes frío? —Sí, un poco, voy a poner la calefacción.", "english": "Are you cold? —Yes, a little, I'm going to turn on the heating."},
            {"spanish": "Lo siento, no puedo parar, tengo mucha prisa.", "english": "I'm sorry, I cannot stop, I am in a big hurry."},
            {"spanish": "Tenemos muchas ganas de conocer Barcelona.", "english": "We really feel like visiting/knowing Barcelona."},
            {"spanish": "Tienes razón, esta palabra es difícil de pronunciar.", "english": "You are right, this word is difficult to pronounce."},
            {"spanish": "¿Cuántos años tienen tus padres?", "english": "How old are your parents?"}
        ],
        "grammar": {
            "title": "Conjugating TENER & The Master 'Tener Idioms'",
            "explanation": "The verb TENER is one of the top 5 most important verbs in the Spanish language. It is irregular in two interesting ways:",
            "rules": [
                "Yo-Go Verb: The 'Yo' form adds a 'g': *Yo TENGO*.",
                "Stem Changing (E -> IE): In tú, él/ella/usted, and ellos/ustedes, the 'e' splits into 'ie': *tú tienes, él tiene, ellos tienen*.",
                "Nosotros and Vosotros stay regular: *nosotros tenemos, vosotros tenéis*.",
                "TENER Conjugation: tengo | tienes | tiene | tenemos | tenéis | tienen.",
                "Tener Expressions (Never use 'to be'): Tener años (age), Tener hambre (hunger), Tener sed (thirst), Tener frío (cold), Tener calor (heat), Tener prisa (hurry), Tener miedo (fear), Tener sueño (sleepiness), Tener razón (to be right), Tener ganas de + inf (to feel like doing something)."
            ],
            "structures": [
                "Full Conjugation: tengo, tienes, tiene, tenemos, tenéis, tienen",
                "Tener Idiom Formula: Tener + [Sustantivo de sensación]",
                "Desire Formula: Tener ganas de + [Verbo en infinitivo]"
            ],
            "examples": [
                {"spanish": "Tengo frío. (Never: 'Soy frío')", "english": "I am cold."},
                {"spanish": "Ella tiene mucho sueño.", "english": "She is very sleepy."},
                {"spanish": "¿Tenéis prisa, chicos?", "english": "Are you all in a hurry, guys?"},
                {"spanish": "Tengo ganas de tomar un café caliente.", "english": "I feel like having a hot coffee."}
            ],
            "commonMistakes": [
                {"wrong": "Estoy frío / Soy frío", "right": "Tengo frío", "explanation": "'Estoy frío' means your body temperature feels physically like an ice cube to the touch. To express feeling cold, say 'Tengo frío'."},
                {"wrong": "Tú eres razón", "right": "Tienes razón", "explanation": "In Spanish, you don't 'be' reason; you 'have' reason: 'Tienes razón'."}
            ],
            "proTip": "To intensify any 'Tener' idiom, use **mucho** or **mucha** (matching the gender of the noun): *Tengo MUCHA hambre* (fem), *Tengo MUCHO frío* (masc), *Tengo MUCHA prisa* (fem)!"
        },
        "conversation": {
            "title": "A Chilly Afternoon in Madrid",
            "context": "Sakib and his friend Javier walk through the city on a brisk November afternoon.",
            "dialogue": [
                {"speaker": "Javier", "role": "Friend", "spanish": "¡Uf! Hace mucho viento hoy. ¿Tienes frío, Sakib?", "english": "Oof! It is very windy today. Are you cold, Sakib?"},
                {"speaker": "Sakib", "role": "Student", "spanish": "¡Sí, tengo muchísimo frío! En mi país nunca hace este frío.", "english": "Yes, I am extremely cold! In my country it is never this cold."},
                {"speaker": "Javier", "role": "Friend", "spanish": "¿Tienes ganas de entrar en una cafetería a tomar chocolate con churros?", "english": "Do you feel like going into a café to have hot chocolate with churros?"},
                {"speaker": "Sakib", "role": "Student", "spanish": "¡Qué gran idea! Tengo mucha hambre y también tengo ganas de algo caliente.", "english": "What a great idea! I am very hungry and also feel like something hot."},
                {"speaker": "Javier", "role": "Friend", "spanish": "Además, no tenemos prisa, podemos charlar tranquilamente.", "english": "Besides, we are not in a hurry, we can chat peacefully."},
                {"speaker": "Sakib", "role": "Student", "spanish": "Tienes toda la razón. ¡Vamos adentro!", "english": "You are completely right. Let's go inside!"}
            ],
            "keyPhrases": [
                {"phrase": "Chocolate con churros", "explanation": "Spain's beloved winter treat: thick dipping hot chocolate with fried dough pastries."},
                {"phrase": "Tienes toda la razón", "explanation": "'You are completely right' (strong emphatic agreement)."},
                {"phrase": "Tranquilamente", "explanation": "'Calmly / Peacefully'."}
            ]
        },
        "reading": {
            "title": "El invierno en Madrid y las costumbres",
            "passage": "El invierno en Madrid es seco y frío. Durante los meses de diciembre y enero, la gente tiene frío y lleva abrigos gruesos, bufandas y guantes. Cuando los madrileños tienen tiempo libre y no tienen prisa, les encanta entrar en las cafeterías tradicionales para calentarse. Piden una taza humeante de chocolate espeso con churros crujientes. Es una tradición centenaria. Sakib prueba este manjar por primera vez y dice: «¡Javier, tienes razón! Este chocolate quita todo el frío».",
            "translation": "Winter in Madrid is dry and cold. During the months of December and January, people are cold and wear thick coats, scarves, and gloves. When locals of Madrid have free time and are not in a hurry, they love going into traditional cafés to warm up. They order a steaming cup of thick chocolate with crispy churros. It is a centuries-old tradition. Sakib tries this delicacy for the first time and says: 'Javier, you are right! This chocolate takes away all the cold.'",
            "questions": [
                {"question": "¿Cómo es el invierno en Madrid?", "options": ["Húmedo y lluvioso", "Seco y frío", "Cálido y soleado", "Tropical"], "answer": 1, "explanation": "Dry and cold ('seco y frío')."},
                {"question": "¿Qué piden los madrileños en las cafeterías en invierno?", "options": ["Helado de vainilla", "Chocolate espeso con churros", "Agua fría con hielo", "Zumo de tomate"], "answer": 1, "explanation": "Thick chocolate with churros ('chocolate espeso con churros')."},
                {"question": "¿Qué dice Sakib sobre el chocolate?", "options": ["Que no le gusta", "Que es muy caro", "Que quita todo el frío", "Que es amargo"], "answer": 2, "explanation": "It takes away all the cold ('quita todo el frío')."}
            ]
        },
        "exercises": [
            {
                "id": "d17-ex1",
                "type": "fill-in",
                "prompt": "Conjugate TENER for 'yo': Yo ______ veinticuatro años.",
                "options": ["tengo", "tienes", "tiene", "tenemos"],
                "correct": 0,
                "explanation": "Yo form is 'tengo'."
            },
            {
                "id": "d17-ex2",
                "type": "multiple-choice",
                "prompt": "How do you say 'You are right' in Spanish?",
                "options": ["Estás razón", "Eres razón", "Tienes razón", "Haces razón"],
                "correct": 2,
                "explanation": "Spanish uses 'Tener razón'."
            },
            {
                "id": "d17-ex3",
                "type": "fill-in",
                "prompt": "Complete: Tengo ganas ______ tomar un café. (to feel like)",
                "options": ["de", "a", "en", "por"],
                "correct": 0,
                "explanation": "The idiom is 'tener ganas DE + infinitive'."
            },
            {
                "id": "d17-ex4",
                "type": "translation",
                "prompt": "Translate: 'I am in a hurry and I am cold.'",
                "options": ["Tengo prisa y tengo frío.", "Soy prisa y estoy frío.", "Estoy prisa y soy frío.", "Hago prisa y tengo frío."],
                "correct": 0,
                "explanation": "'Tengo prisa y tengo frío' uses the proper idiomatic expressions."
            }
        ],
        "speakingChallenge": [
            {"prompt": "Say that you are very sleepy today.", "hint": "Tengo mucho sueño...", "sampleAnswer": "Hoy tengo mucho sueño porque he estudiado hasta tarde."},
            {"prompt": "Express that you feel like eating Spanish food.", "hint": "Tengo ganas de comer...", "sampleAnswer": "Tengo muchas ganas de comer paella este fin de semana."},
            {"prompt": "Tell a friend: 'Don't worry, you are right.'", "hint": "Tranquilo, tienes razón.", "sampleAnswer": "Tranquilo, amigo, tú tienes toda la razón."}
        ],
        "dailyRevision": {
            "quickQuestions": [
                "What kind of verb is TENER? (Yo-go + stem-changing E -> IE)",
                "How do you say 'I am sleepy' in Spanish?"
            ],
            "grammarRecall": "TENER: tengo, tienes, tiene, tenemos, tenéis, tienen. Idioms: tener hambre, sed, frío, calor, prisa, miedo, sueño, razón.",
            "vocabRecall": ["Tener", "Tengo", "Tener frío", "Tener calor", "Tener prisa", "Tener miedo", "Tener sueño", "Tener razón"]
        },
        "checklist": [
            "Conjugated TENER in all 6 present tense forms",
            "Understood the 'yo-go' and 'e->ie' stem changes",
            "Mastered the 8 essential TENER idiomatic expressions",
            "Learned 'Tener ganas de + infinitive' for expressing desires",
            "Completed all 4 TENER exercises",
            "Used 'Tengo frío' and 'Tengo prisa' in spoken sentences"
        ]
    },
    {
        "day": 18,
        "stage": 2,
        "title": "The Verb HACER & Weather Basics",
        "subtitle": "Conjugating HACER, weather expressions, and daily activities",
        "goals": [
            "Conjugate the irregular verb HACER (to do / to make) in the present tense",
            "Learn how Spanish uses 'HACE + noun' to express weather (hace calor, hace frío, hace sol)",
            "Talk about what you do in your free time using HACER",
            "Describe the weather across different seasons in Spain"
        ],
        "bengaliNote": "In English, you say 'It is hot' or 'It is sunny'. But in Spanish, the atmosphere *makes* weather! Spanish uses the third-person of HACER (*Hace sol* = It makes sun; *Hace calor* = It makes heat). In Bangla, we say 'আজ খুব গরম' — Spanish expresses this directly as *Hoy hace mucho calor*!",
        "vocabulary": [
            {"word": "Hacer", "translation": "To do / To make", "pos": "verb", "gender": None, "example": "¿Qué haces hoy?", "exampleTranslation": "What are you doing today?"},
            {"word": "Hago, Haces, Hace", "translation": "I do, you do, he/she does", "pos": "verb form", "gender": None, "example": "Hago mis deberes por la tarde.", "exampleTranslation": "I do my homework in the afternoon."},
            {"word": "Hacemos, Hacéis, Hacen", "translation": "We do, you all do, they do", "pos": "verb form", "gender": None, "example": "Hacemos deporte los sábados.", "exampleTranslation": "We do sports on Saturdays."},
            {"word": "Hace buen tiempo / mal tiempo", "translation": "The weather is good / bad", "pos": "phrase", "gender": None, "example": "Hoy hace muy buen tiempo.", "exampleTranslation": "Today the weather is very good."},
            {"word": "Hace sol / Hace viento", "translation": "It is sunny / It is windy", "pos": "phrase", "gender": None, "example": "Hace mucho sol, necesitas gafas.", "exampleTranslation": "It is very sunny, you need sunglasses."},
            {"word": "Hace calor / Hace frío", "translation": "It is hot / It is cold (weather)", "pos": "phrase", "gender": None, "example": "En Sevilla en verano hace mucho calor.", "exampleTranslation": "In Seville in summer it is very hot."},
            {"word": "Llover (llueve)", "translation": "To rain (it rains)", "pos": "verb", "gender": None, "example": "Hoy llueve mucho en Galicia.", "exampleTranslation": "Today it rains a lot in Galicia."},
            {"word": "Nevar (nieva)", "translation": "To snow (it snows)", "pos": "verb", "gender": None, "example": "Nieva en las montañas.", "exampleTranslation": "It snows in the mountains."},
            {"word": "El tiempo", "translation": "The weather / The time", "pos": "noun", "gender": "masculine", "example": "¿Qué tiempo hace hoy?", "exampleTranslation": "What is the weather like today?"},
            {"word": "Hacer la maleta", "translation": "To pack the suitcase", "pos": "phrase", "gender": None, "example": "Hago la maleta para el viaje.", "exampleTranslation": "I pack the suitcase for the trip."}
        ],
        "sentences": [
            {"spanish": "¿Qué tiempo hace hoy en Madrid?", "english": "What is the weather like today in Madrid?"},
            {"spanish": "Hoy hace sol y hace una temperatura muy agradable.", "english": "Today it is sunny and there is a very pleasant temperature."},
            {"spanish": "¿Qué haces los fines de semana? —Hago deporte y leo.", "english": "What do you do on weekends? —I do sports and read."},
            {"spanish": "En invierno hace bastante frío y a veces nieva.", "english": "In winter it is quite cold and sometimes it snows."},
            {"spanish": "Cuando llueve me gusta quedarme en casa leyendo.", "english": "When it rains I like staying at home reading."},
            {"spanish": "Nosotros hacemos la compra los sábados por la mañana.", "english": "We do the grocery shopping on Saturday mornings."}
        ],
        "grammar": {
            "title": "Conjugating HACER & The Weather Formula",
            "explanation": "HACER is an irregular 'yo-go' verb (*yo hago*), but its remaining forms follow regular -er patterns (*haces, hace, hacemos, hacéis, hacen*).",
            "rules": [
                "HACER Conjugation: hago | haces | hace | hacemos | hacéis | hacen.",
                "Asking about weather: ¿Qué tiempo hace? (Literally: What weather does it make?)",
                "HACE + Weather Noun: *Hace sol* (It's sunny), *Hace calor* (It's hot), *Hace frío* (It's cold), *Hace viento* (It's windy), *Hace buen tiempo* (Good weather), *Hace mal tiempo* (Bad weather).",
                "Intensity: Use 'mucho' because sol, calor, frío, viento are nouns: *Hace MUCHO calor* (NOT *Hace muy calor*!).",
                "Direct Weather Verbs: *Llueve* (It rains - from llover), *Nieva* (It snows - from nevar). These do not use 'hace'."
            ],
            "structures": [
                "HACER Present: hago, haces, hace, hacemos, hacéis, hacen",
                "Weather Query: ¿Qué tiempo hace hoy en [Ciudad]?",
                "Weather Statement: Hace + mucho/bastante + [sol / frío / calor / viento]"
            ],
            "examples": [
                {"spanish": "Hago mis ejercicios de español.", "english": "I do my Spanish exercises."},
                {"spanish": "Hace mucho viento en la costa.", "english": "It is very windy on the coast."},
                {"spanish": "Hoy no hace calor, hace fresco.", "english": "Today it is not hot, it is cool."},
                {"spanish": "Llueve a cántaros. (Idiom)", "english": "It is raining cats and dogs (raining pitchers)."}
            ],
            "commonMistakes": [
                {"wrong": "Hace muy calor", "right": "Hace mucho calor", "explanation": "'Calor' is a noun, so it must be modified by the adjective 'mucho', not the adverb 'muy'."},
                {"wrong": "Es calor hoy", "right": "Hace calor hoy", "explanation": "Weather uses 'hacer', never 'ser'."}
            ],
            "proTip": "Remember the critical difference: *HACE calor* = The weather outside is hot! *TENGO calor* = I personally feel hot! *ESTÁ caliente* = The coffee or soup is hot to the touch!"
        },
        "conversation": {
            "title": "Checking the Weather Forecast",
            "context": "Sakib and his roommate Alberto check the weather before planning a hike.",
            "dialogue": [
                {"speaker": "Sakib", "role": "Student", "spanish": "Alberto, ¿qué tiempo hace hoy fuera?", "english": "Alberto, what is the weather like outside today?"},
                {"speaker": "Alberto", "role": "Roommate", "spanish": "Mira por la ventana: hace un sol espléndido y el cielo está totalmente azul.", "english": "Look through the window: it is splendidly sunny and the sky is totally blue."},
                {"speaker": "Sakib", "role": "Student", "spanish": "¿Y hace frío?", "english": "And is it cold?"},
                {"speaker": "Alberto", "role": "Roommate", "spanish": "No, hace una temperatura primaveral, unos veinte grados.", "english": "No, it's a spring-like temperature, around twenty degrees."},
                {"speaker": "Sakib", "role": "Student", "spanish": "¡Qué maravilla! ¿Qué hacemos hoy entonces?", "english": "What a wonder! What are we doing today then?"},
                {"speaker": "Alberto", "role": "Roommate", "spanish": "Podemos ir a la Sierra de Guadarrama a caminar y hacer fotos.", "english": "We can go to the Guadarrama Mountains to hike and take photos."},
                {"speaker": "Sakib", "role": "Student", "spanish": "¡Me parece genial! Preparo mi mochila enseguida.", "english": "Sounds great to me! I'll pack my backpack right away."}
            ],
            "keyPhrases": [
                {"phrase": "¿Qué tiempo hace fuera?", "explanation": "'What is the weather like outside?'"},
                {"phrase": "Hacer fotos", "explanation": "'To take photos' (Spanish uses 'hacer fotos' or 'sacar fotos')."},
                {"phrase": "Me parece genial", "explanation": "'That sounds great / brilliant to me'."}
            ]
        },
        "reading": {
            "title": "Los diferentes climas de la Península Ibérica",
            "passage": "España es un país con una gran diversidad climática. En el norte, en la zona cantábrica y atlántica, el clima es oceánico: llueve con frecuencia durante todo el año y los veranos son suaves y frescos. En el centro, en la meseta donde está Madrid, el clima es continental: en invierno hace mucho frío y en verano hace un calor seco e intenso. Por otro lado, en la costa este y en las islas Baleares reina el clima mediterráneo, con inviernos templados y veranos soleados. ¡En España siempre puedes encontrar el clima que más te guste!",
            "translation": "Spain is a country with great climatic diversity. In the north, in the Cantabrian and Atlantic zone, the climate is oceanic: it rains frequently throughout the whole year and summers are mild and cool. In the center, on the plateau where Madrid is located, the climate is continental: in winter it is very cold and in summer it is dry and intense heat. On the other hand, on the eastern coast and the Balearic Islands reigns the Mediterranean climate, with mild winters and sunny summers. In Spain you can always find the climate you like most!",
            "questions": [
                {"question": "¿Cómo es el clima en el norte de España?", "options": ["Muy seco y desértico", "Llueve con frecuencia y los veranos son suaves", "Siempre nieva", "Hace 40 grados todo el año"], "answer": 1, "explanation": "It rains frequently and summers are mild ('llueve con frecuencia...')."},
                {"question": "¿Cómo es el verano en el centro de España (Madrid)?", "options": ["Frío", "Lluvioso", "Un calor seco e intenso", "Nevado"], "answer": 2, "explanation": "Dry and intense heat ('un calor seco e intenso')."},
                {"question": "¿Qué tipo de clima hay en la costa este y Baleares?", "options": ["Clima mediterráneo", "Clima polar", "Clima tropical húmedo", "Clima montañoso"], "answer": 0, "explanation": "Mediterranean climate ('el clima mediterráneo')."}
            ]
        },
        "exercises": [
            {
                "id": "d18-ex1",
                "type": "fill-in",
                "prompt": "Conjugate HACER for 'yo': Yo ______ deporte por las mañanas.",
                "options": ["hago", "haces", "hace", "hacemos"],
                "correct": 0,
                "explanation": "Yo form of hacer is 'hago'."
            },
            {
                "id": "d18-ex2",
                "type": "multiple-choice",
                "prompt": "How do you say 'It is very hot today' (weather)?",
                "options": ["Hoy es muy calor", "Hoy está mucho calor", "Hoy hace mucho calor", "Hoy tiene mucho calor"],
                "correct": 2,
                "explanation": "Weather uses 'Hace mucho calor'."
            },
            {
                "id": "d18-ex3",
                "type": "multiple-choice",
                "prompt": "What does 'Hace sol' mean?",
                "options": ["The sun is far", "It is sunny", "I feel hot", "It is raining"],
                "correct": 1,
                "explanation": "'Hace sol' means 'It is sunny'."
            },
            {
                "id": "d18-ex4",
                "type": "translation",
                "prompt": "Translate: 'What are you doing this weekend?' (informal)",
                "options": ["¿Qué haces este fin de semana?", "¿Dónde estás este fin de semana?", "¿Cómo vas este fin de semana?", "¿Quién hace este fin de semana?"],
                "correct": 0,
                "explanation": "'¿Qué haces este fin de semana?' is the natural translation."
            }
        ],
        "speakingChallenge": [
            {"prompt": "Look out your window and describe today's weather in Spanish.", "hint": "Hoy hace... / Hoy está...", "sampleAnswer": "Hoy hace sol y hace un poco de viento."},
            {"prompt": "Say what you do on Saturday mornings.", "hint": "Los sábados por la mañana hago...", "sampleAnswer": "Los sábados por la mañana hago la compra y limpio mi habitación."},
            {"prompt": "State: 'When it rains, I study at home.'", "hint": "Cuando llueve, estudio en...", "sampleAnswer": "Cuando llueve, me quedo en casa y estudio español."}
        ],
        "dailyRevision": {
            "quickQuestions": [
                "Why do we say 'Hace mucho calor' instead of 'Hace muy calor'?",
                "What is the difference between 'Hace calor' and 'Tengo calor'?"
            ],
            "grammarRecall": "HACER: hago, haces, hace, hacemos, hacéis, hacen. Weather: Hace sol/frío/calor/viento. Llueve / Nieva.",
            "vocabRecall": ["Hacer", "Hago", "Hace sol", "Hace calor", "Hace frío", "Llueve", "Nieva", "El tiempo"]
        },
        "checklist": [
            "Conjugated the verb HACER with the irregular 'yo hago'",
            "Learned the weather formula 'Hace + weather noun'",
            "Used direct weather verbs (llueve, nieva)",
            "Distinguished between 'Hace calor' and 'Tengo calor'",
            "Completed all 4 HACER exercises",
            "Described local weather aloud in Spanish"
        ]
    },
    {
        "day": 19,
        "stage": 2,
        "title": "The Irregular Verb IR & The Near Future",
        "subtitle": "Conjugating IR, expressing movement, and using 'IR + A + Infinitive'",
        "goals": [
            "Conjugate the completely irregular verb IR (to go): voy, vas, va, vamos, vais, van",
            "Express movement towards destinations using 'Ir + a + [Lugar]'",
            "Master the mandatory contraction: ir + a + el = **ir al** (*Voy al cine*)",
            "Unlock the Near Future tense: **IR + A + Infinitive** (*Voy a estudiar* = I am going to study)"
        ],
        "bengaliNote": "This is one of the greatest linguistic shortcuts in the Spanish language! Just like in English ('I am going to study') and Bangla ('আমি পড়াশোনা করতে যাচ্ছি'), Spanish allows you to talk about the future using **IR + A + Infinitive**. You don't need complicated future verb conjugations yet; this simple formula covers 95% of future plans!",
        "vocabulary": [
            {"word": "Ir", "translation": "To go", "pos": "verb", "gender": None, "example": "¿Adónde vas?", "exampleTranslation": "Where are you going?"},
            {"word": "Voy, Vas, Va", "translation": "I go, you go, he/she goes", "pos": "verb form", "gender": None, "example": "Voy a la universidad.", "exampleTranslation": "I go to the university."},
            {"word": "Vamos, Vais, Van", "translation": "We go, you all go, they go", "pos": "verb form", "gender": None, "example": "¡Vamos!", "exampleTranslation": "Let's go!"},
            {"word": "Ir a (+ lugar)", "translation": "To go to (a place)", "pos": "phrase", "gender": None, "example": "Voy al supermercado a comprar pan.", "exampleTranslation": "I go to the supermarket to buy bread."},
            {"word": "Ir a (+ infinitivo)", "translation": "To be going to (near future formula)", "pos": "grammar structure", "gender": None, "example": "Mañana voy a estudiar cuatro horas.", "exampleTranslation": "Tomorrow I am going to study four hours."},
            {"word": "¿Adónde vas?", "translation": "Where are you going? (asking direction/destination)", "pos": "phrase", "gender": None, "example": "Hola Carlos, ¿adónde vas tan rápido?", "exampleTranslation": "Hello Carlos, where are you going so fast?"},
            {"word": "A pie / En metro / En autobús", "translation": "On foot / By metro / By bus", "pos": "phrase", "gender": None, "example": "Voy a la escuela en metro.", "exampleTranslation": "I go to school by subway."},
            {"word": "El fin de semana que viene / Próximo", "translation": "Next weekend", "pos": "phrase", "gender": "masculine", "example": "El fin de semana próximo voy a viajar a Toledo.", "exampleTranslation": "Next weekend I am going to travel to Toledo."},
            {"word": "Esta tarde / Esta noche", "translation": "This afternoon / Tonight", "pos": "phrase", "gender": "feminine", "example": "Esta noche voy a descansar.", "exampleTranslation": "Tonight I am going to rest."},
            {"word": "Pronto", "translation": "Soon", "pos": "adverb", "gender": None, "example": "Nos vemos muy pronto.", "exampleTranslation": "See you very soon."}
        ],
        "sentences": [
            {"spanish": "Voy al supermercado, ¿necesitas algo?", "english": "I am going to the supermarket, do you need anything?"},
            {"spanish": "Mañana voy a levantarme temprano para repasar.", "english": "Tomorrow I am going to wake up early to review."},
            {"spanish": "¿Qué vas a hacer este fin de semana?", "english": "What are you going to do this weekend?"},
            {"spanish": "Nosotros vamos a cenar en un restaurante tradicional.", "english": "We are going to have dinner at a traditional restaurant."},
            {"spanish": "¿Cómo vas al trabajo? —Voy a pie porque vivo cerca.", "english": "How do you go to work? —I go on foot because I live nearby."},
            {"spanish": "Ellos van a viajar a Barcelona en tren de alta velocidad.", "english": "They are going to travel to Barcelona by high-speed train."}
        ],
        "grammar": {
            "title": "Conjugating IR & The Near Future Formula (IR + A + Infinitive)",
            "explanation": "The verb IR is completely irregular — it looks nothing like its infinitive! But once memorized, it becomes your most versatile superpower.",
            "rules": [
                "IR Conjugation: voy, vas, va, vamos, vais, van.",
                "Mandatory Contraction with Places: When going to a masculine place (*el parque*, *el cine*, *el supermercado*), 'a + el' MUST become 'al': *Voy AL parque* (never *Voy a el parque*!). For feminine: *Voy a la playa*.",
                "The Near Future Formula: [Conjugated IR] + A + [Infinitive Verb]. E.g. *Voy a comer* (I am going to eat), *Vas a aprender* (You are going to learn), *Vamos a viajar* (We are going to travel).",
                "Crucial Detail: Never forget the linking preposition **'A'**! It connects the conjugated form of IR to the infinitive action."
            ],
            "structures": [
                "IR Conjugation: voy | vas | va | vamos | vais | van",
                "Destination: Ir + a la / al + [Lugar]",
                "Near Future: [voy/vas/va/vamos/vais/van] + A + [Infinitivo]"
            ],
            "examples": [
                {"spanish": "Voy a estudiar español.", "english": "I am going to study Spanish."},
                {"spanish": "¿Vas a venir a la fiesta?", "english": "Are you going to come to the party?"},
                {"spanish": "Vamos a comprar comida.", "english": "We are going to buy food."},
                {"spanish": "Van a vivir en España un año.", "english": "They are going to live in Spain for a year."}
            ],
            "commonMistakes": [
                {"wrong": "Voy estudiar (missing 'a')", "right": "Voy a estudiar", "explanation": "The structure strictly requires the connecting preposition 'a'."},
                {"wrong": "Voy a el cine", "right": "Voy al cine", "explanation": "'A + el' must contract to 'al'."}
            ],
            "proTip": "With 'IR + A + Infinitive', you don't need to know future tense verb conjugations. Master this single formula today, and you can speak about all your plans for tomorrow, next week, or next year!"
        },
        "conversation": {
            "title": "Weekend Travel Plans to Toledo",
            "context": "Sakib and his friend Lucía make plans in the academy courtyard.",
            "dialogue": [
                {"speaker": "Lucía", "role": "Friend", "spanish": "Sakib, ¿qué vas a hacer este sábado?", "english": "Sakib, what are you going to do this Saturday?"},
                {"speaker": "Sakib", "role": "Student", "spanish": "Voy a hacer una excursión de un día a Toledo. ¿La conoces?", "english": "I am going to do a day trip to Toledo. Do you know it?"},
                {"speaker": "Lucía", "role": "Friend", "spanish": "¡Sí! Toledo es una ciudad medieval fascinante. ¿Cómo vas a ir?", "english": "Yes! Toledo is a fascinating medieval city. How are you going to go?"},
                {"speaker": "Sakib", "role": "Student", "spanish": "Voy a ir en tren de alta velocidad desde la estación de Atocha. Tarda solo treinta minutos.", "english": "I am going to go by high-speed train from Atocha station. It takes only thirty minutes."},
                {"speaker": "Lucía", "role": "Friend", "spanish": "¡Qué bien! Vas a ver la catedral gótica, el Alcázar y los puentes antiguos.", "english": "How wonderful! You are going to see the Gothic cathedral, the Alcazar, and ancient bridges."},
                {"speaker": "Sakib", "role": "Student", "spanish": "Sí, y voy a sacar muchísimas fotos.", "english": "Yes, and I am going to take tons of photos."}
            ],
            "keyPhrases": [
                {"phrase": "Hacer una excursión", "explanation": "'To go on a day trip / excursion'."},
                {"phrase": "¿Cómo vas a ir?", "explanation": "'How are you going to go?' (asking for method of transport)."},
                {"phrase": "Tarda solo...", "explanation": "'It takes only [amount of time]'."}
            ]
        },
        "reading": {
            "title": "La excursión a Toledo",
            "passage": "El sábado por la mañana, Sakib se levanta a las siete. Va a la cocina, prepara un té y come unas tostadas. Luego va a pie hasta la estación de Atocha. Allí compra su billete para Toledo. El tren es moderno, limpio y muy rápido. En solo media hora llega a la histórica ciudad de las tres culturas. Sakib camina por sus estrechas calles empedradas, visita la gran catedral y prueba el famoso mazapán de Toledo. Por la tarde regresa a Madrid en tren, cansado pero muy feliz.",
            "translation": "On Saturday morning, Sakib wakes up at seven. He goes to the kitchen, prepares tea, and eats some toast. Then he goes on foot to Atocha station. There he buys his ticket for Toledo. The train is modern, clean, and very fast. In only half an hour he arrives at the historic city of the three cultures. Sakib walks through its narrow cobblestone streets, visits the great cathedral, and tries the famous marzipan of Toledo. In the afternoon he returns to Madrid by train, tired but very happy.",
            "questions": [
                {"question": "¿A qué hora se levanta Sakib el sábado?", "options": ["A las nueve", "A las siete", "A las diez", "A las cinco"], "answer": 1, "explanation": "At seven ('a las siete')."},
                {"question": "¿Cómo va Sakib hasta la estación de Atocha?", "options": ["En taxi", "A pie", "En bicicleta", "En coche"], "answer": 1, "explanation": "On foot ('va a pie')."},
                {"question": "¿Qué dulce famoso prueba Sakib en Toledo?", "options": ["Chocolate con churros", "El famoso mazapán de Toledo", "Helado de fresa", "Tarta de queso"], "answer": 1, "explanation": "Marzipan ('el famoso mazapán de Toledo')."}
            ]
        },
        "exercises": [
            {
                "id": "d19-ex1",
                "type": "fill-in",
                "prompt": "Conjugate IR for 'yo': Mañana yo ______ a estudiar gramática.",
                "options": ["voy", "vas", "va", "vamos"],
                "correct": 0,
                "explanation": "Yo form of IR is 'voy': 'voy a estudiar'."
            },
            {
                "id": "d19-ex2",
                "type": "fill-in",
                "prompt": "Complete with the correct contraction: Voy ______ (a + el) parque.",
                "options": ["al", "a el", "del", "de el"],
                "correct": 0,
                "explanation": "'a + el' must contract to 'al'."
            },
            {
                "id": "d19-ex3",
                "type": "multiple-choice",
                "prompt": "What preposition is required between IR and the infinitive verb?",
                "options": ["de", "a", "en", "por"],
                "correct": 1,
                "explanation": "The formula is strictly 'IR + A + Infinitive'."
            },
            {
                "id": "d19-ex4",
                "type": "translation",
                "prompt": "Translate: 'What are you going to do tonight?' (informal)",
                "options": ["¿Qué vas a hacer esta noche?", "¿Dónde vas a ir esta noche?", "¿Cómo vas a hacer esta noche?", "¿Quién va a hacer esta noche?"],
                "correct": 0,
                "explanation": "'¿Qué vas a hacer esta noche?' asks for tonight's plans."
            }
        ],
        "speakingChallenge": [
            {"prompt": "Say two things you are going to do tomorrow using 'Voy a...'", "hint": "Mañana voy a [verbo] y voy a [verbo]...", "sampleAnswer": "Mañana voy a estudiar español y voy a cocinar arroz con pollo."},
            {"prompt": "Ask someone what they are going to do this weekend.", "hint": "¿Qué vas a hacer este...", "sampleAnswer": "¿Qué vas a hacer este fin de semana, amigo?"},
            {"prompt": "Conjugate the verb IR aloud for all 6 persons.", "hint": "Voy, vas, va, vamos, vais, van.", "sampleAnswer": "Yo voy, tú vas, él va, nosotros vamos, vosotros vais, ellos van."}
        ],
        "dailyRevision": {
            "quickQuestions": [
                "What is the near future formula in Spanish? (IR + A + Infinitive)",
                "What contraction occurs when using IR with a masculine noun? (a + el = al)"
            ],
            "grammarRecall": "IR: voy, vas, va, vamos, vais, van. Near Future: Ir + a + infinitive. Ir al cine, ir a la playa.",
            "vocabRecall": ["Ir", "Voy", "Vas", "Vamos", "Ir al", "A pie", "Esta tarde", "Esta noche", "Pronto"]
        },
        "checklist": [
            "Conjugated the irregular verb IR in all 6 forms",
            "Mastered the Near Future formula (IR + A + Infinitive)",
            "Applied the mandatory contraction 'al' (a + el)",
            "Expressed methods of transport (a pie, en metro, en tren)",
            "Completed all 4 IR exercises",
            "Stated my plans for tomorrow out loud in Spanish"
        ]
    },
    {
        "day": 20,
        "stage": 2,
        "title": "Asking & Answering Questions",
        "subtitle": "The 8 Question Words (Interrogatives) + Stage 2 Milestone Assessment",
        "goals": [
            "Master the 8 essential question words: ¿Qué?, ¿Quién?, ¿Dónde?, ¿Adónde?, ¿Cuándo?, ¿Por qué?, ¿Cómo?, ¿Cuánto?",
            "Notice that all Spanish question words carry a mandatory accent mark (tilde)",
            "Distinguish between '¿Por qué?' (Why?) and 'Porque' (Because)",
            "Complete the Stage 2 Milestone Assessment (Days 11–20 comprehensive test)"
        ],
        "bengaliNote": "In Bangla, we have the 'K-words' (কে, কী, কোথায়, কখন, কেন, কীভাবে, কত). In Spanish, these are the question words! Notice that when asking 'Why?' it is written as two separate words with an accent (*¿Por qué?* = কেন?), but when answering 'Because', it is a single word without an accent (*Porque* = কারণ)!",
        "vocabulary": [
            {"word": "¿Qué?", "translation": "What? / Which?", "pos": "interrogative", "gender": None, "example": "¿Qué estudias?", "exampleTranslation": "What do you study?"},
            {"word": "¿Quién? / ¿Quiénes?", "translation": "Who? (singular / plural)", "pos": "interrogative", "gender": None, "example": "¿Quién es tu profesor?", "exampleTranslation": "Who is your teacher?"},
            {"word": "¿Dónde? / ¿Adónde?", "translation": "Where? (location) / Where to? (destination)", "pos": "interrogative", "gender": None, "example": "¿Dónde vives? / ¿Adónde vas?", "exampleTranslation": "Where do you live? / Where are you going?"},
            {"word": "¿Cuándo?", "translation": "When?", "pos": "interrogative", "gender": None, "example": "¿Cuándo empieza la clase?", "exampleTranslation": "When does the class start?"},
            {"word": "¿Por qué? / Porque", "translation": "Why? / Because", "pos": "phrase / conjunction", "gender": None, "example": "¿Por qué estudias español? —Porque me gusta mucho.", "exampleTranslation": "Why do you study Spanish? —Because I like it a lot."},
            {"word": "¿Cómo?", "translation": "How? / What? (in greetings/names)", "pos": "interrogative", "gender": None, "example": "¿Cómo se dice esto en español?", "exampleTranslation": "How is this said in Spanish?"},
            {"word": "¿Cuánto(a)? / ¿Cuántos(as)?", "translation": "How much? / How many?", "pos": "interrogative", "gender": "variable", "example": "¿Cuántos años tienes?", "exampleTranslation": "How many years do you have? (How old are you?)"},
            {"word": "¿Cuál? / ¿Cuáles?", "translation": "Which one? / What? (choice/selection)", "pos": "interrogative", "gender": None, "example": "¿Cuál es tu número de teléfono?", "exampleTranslation": "What is your telephone number?"},
            {"word": "La pregunta / La respuesta", "translation": "The question / The answer", "pos": "noun", "gender": "feminine", "example": "Tengo una pregunta.", "exampleTranslation": "I have a question."},
            {"word": "Responder / Contestar", "translation": "To answer / To reply", "pos": "verb", "gender": None, "example": "Respondo a las preguntas del examen.", "exampleTranslation": "I answer the exam questions."}
        ],
        "sentences": [
            {"spanish": "¿Por qué estudias español? —Porque quiero viajar y trabajar.", "english": "Why do you study Spanish? —Because I want to travel and work."},
            {"spanish": "¿Dónde está la estación de metro más cercana?", "english": "Where is the nearest metro station?"},
            {"spanish": "¿Cuánto cuesta un billete de autobús?", "english": "How much does a bus ticket cost?"},
            {"spanish": "¿Quiénes son tus compañeros de piso?", "english": "Who are your flatmates?"},
            {"spanish": "¿Cuándo termina el curso?", "english": "When does the course end?"},
            {"spanish": "¿Cómo se pronuncia esta palabra?", "english": "How is this word pronounced?"}
        ],
        "grammar": {
            "title": "The Master Interrogative Guide & The 4-Way 'Porqué' Rule",
            "explanation": "Question words are the compass of conversation. Without them, you cannot ask for help, buy tickets, or make friends.",
            "rules": [
                "Mandatory Written Accents: All interrogative words carry a written tilde when used in questions (direct or indirect): *qué, quién, dónde, cuándo, cómo, cuánto, cuál, por qué*.",
                "¿Por qué? vs. Porque: 1) *¿Por qué?* (two words, accented 'e') = Why? (question). 2) *Porque* (one word, no accent) = Because (answer / reason).",
                "¿Dónde? vs. ¿Adónde?: Use *¿Dónde?* for static location (*¿Dónde estás?* = Where are you?). Use *¿Adónde?* (a + dónde) with verbs of motion like IR (*¿Adónde vas?* = Where to are you going?).",
                "¿Cuánto? Agreement: 'Cuánto' behaves like an adjective and agrees with the noun: *¿Cuánto dinero?* (masc sing), *¿Cuánta agua?* (fem sing), *¿Cuántos libros?* (masc plur), *¿Cuántas personas?* (fem plur)."
            ],
            "structures": [
                "Question Architecture: ¿ [Interrogativo] + [Verbo] + [Sujeto / Complemento] ?",
                "Why & Because: ¿Por qué + [pregunta]? -> Porque + [respuesta]",
                "Motion: ¿Adónde + vas / va / van?"
            ],
            "examples": [
                {"spanish": "¿Qué hora es?", "english": "What time is it?"},
                {"spanish": "¿Quién es ella?", "english": "Who is she?"},
                {"spanish": "¿Adónde vais vosotros?", "english": "Where are you all going?"},
                {"spanish": "¿Cuántas hermanas tienes?", "english": "How many sisters do you have?"}
            ],
            "commonMistakes": [
                {"wrong": "Por qué me gusta (as an answer)", "right": "Porque me gusta", "explanation": "'Porque' (single word, no accent) is used for answers ('because')."},
                {"wrong": "Donde vas (in a question)", "right": "¿Adónde vas?", "explanation": "Movement towards a destination takes 'Adónde' with accent mark and question marks."}
            ],
            "proTip": "¿Qué vs. ¿Cuál?: Use **¿Qué?** to ask for a definition or explanation (*¿Qué es la paella?*). Use **¿Cuál?** when choosing from possibilities (*¿Cuál es tu color favorito?*, *¿Cuál es tu nombre?*)."
        },
        "conversation": {
            "title": "An Interview at the Language Academy",
            "context": "Professor Carmen interviews Sakib to assess his progress at the end of Stage 2.",
            "dialogue": [
                {"speaker": "Profª Carmen", "role": "Teacher", "spanish": "¡Hola, Sakib! ¿Cómo estás hoy?", "english": "Hello, Sakib! How are you today?"},
                {"speaker": "Sakib", "role": "Student", "spanish": "¡Hola, profesora! Estoy muy bien, gracias. ¿Y usted?", "english": "Hello, professor! I am very well, thank you. And you?"},
                {"speaker": "Profª Carmen", "role": "Teacher", "spanish": "Muy bien. A ver, ¿dónde vives y con quién vives?", "english": "Very well. Let's see, where do you live and who do you live with?"},
                {"speaker": "Sakib", "role": "Student", "spanish": "Vivo en Chamberí con dos compañeros estudiantes.", "english": "I live in Chamberí with two student flatmates."},
                {"speaker": "Profª Carmen", "role": "Teacher", "spanish": "¿Y qué haces por las tardes después de clase?", "english": "And what do you do in the afternoons after class?"},
                {"speaker": "Sakib", "role": "Student", "spanish": "Hago mis deberes, leo textos sencillos y voy al parque a caminar.", "english": "I do my homework, read simple texts, and go to the park to walk."},
                {"speaker": "Profª Carmen", "role": "Teacher", "spanish": "¿Por qué estudias español?", "english": "Why do you study Spanish?"},
                {"speaker": "Sakib", "role": "Student", "spanish": "Porque me encanta la cultura y quiero comunicarme con fluidez en España.", "english": "Because I love the culture and want to communicate fluently in Spain."},
                {"speaker": "Profª Carmen", "role": "Teacher", "spanish": "¡Excelente, Sakib! Tu progreso en estos veinte días es impresionante.", "english": "Excellent, Sakib! Your progress in these twenty days is impressive."}
            ],
            "keyPhrases": [
                {"phrase": "A ver", "explanation": "'Let's see...' (conversational transition phrase)."},
                {"phrase": "Con quién vives", "explanation": "'Who you live with'."},
                {"phrase": "Con fluidez", "explanation": "'With fluency / fluently'."}
            ]
        },
        "reading": {
            "title": "Stage 2 Capstone Story: Veinte días de progreso",
            "passage": "Han pasado veinte días desde que Sakib comenzó su desafío de español. Al principio, solo sabía decir «¡Hola!» y contar hasta diez. Ahora, su vida en Madrid está llena de español. Sabe describir su familia, pedir comida deliciosa en el mercado, hablar sobre su piso y el tiempo que hace. Conoce los verbos regulares (-ar, -er, -ir) y verbos clave como ser, estar, tener, hacer e ir. Sabe hacer preguntas esenciales y formular planes con el futuro próximo. Hoy celebra su día 20 con una tortilla española y una taza de té caliente. ¡Un tercio del camino hacia A1 está completado con éxito!",
            "translation": "Twenty days have passed since Sakib began his Spanish challenge. At first, he only knew how to say 'Hello!' and count to ten. Now, his life in Madrid is full of Spanish. He knows how to describe his family, order delicious food at the market, talk about his flat and the weather. He knows regular verbs (-ar, -er, -ir) and key verbs like ser, estar, tener, hacer, and ir. He knows how to ask essential questions and formulate plans with the near future. Today he celebrates his Day 20 with a Spanish omelette and a hot cup of tea. One third of the path to A1 is successfully completed!",
            "questions": [
                {"question": "¿Cuánto tiempo ha completado Sakib hoy?", "options": ["Diez días", "Quince días", "Veinte días (un tercio del desafío)", "Cuarenta días"], "answer": 2, "explanation": "Twenty days, one third of the challenge ('Veinte días... Un tercio del camino')."},
                {"question": "¿Con qué celebra Sakib su día 20?", "options": ["Con paella", "Con una tortilla española y una taza de té", "Con café frío", "Con una pizza"], "answer": 1, "explanation": "With a Spanish omelette and a cup of hot tea."},
                {"question": "¿Qué sabe hacer Sakib ahora?", "options": ["Solo decir hola", "Describir su familia, pedir comida, usar verbos y hacer preguntas", "Hablar como un nativo C2", "Escribir novelas"], "answer": 1, "explanation": "Describe family, order food, conjugate verbs, ask questions."}
            ]
        },
        "exercises": [
            {
                "id": "d20-ex1",
                "type": "fill-in",
                "prompt": "Choose the correct word: ¿______ (Where to) vas este fin de semana?",
                "options": ["Adónde", "Dónde", "Cuándo", "Quién"],
                "correct": 0,
                "explanation": "'Adónde' is used with verbs of movement (ir)."
            },
            {
                "id": "d20-ex2",
                "type": "fill-in",
                "prompt": "Choose ¿Por qué? or Porque: —¿Por qué estudias español? —______ me gusta.",
                "options": ["Porque", "¿Por qué?", "Por que", "Porqué"],
                "correct": 0,
                "explanation": "'Porque' (single word, no accent) is used for answering 'because'."
            },
            {
                "id": "d20-ex3",
                "type": "multiple-choice",
                "prompt": "Do Spanish question words carry accent marks?",
                "options": ["Always in questions", "Never", "Only if plural", "Only at the end of a sentence"],
                "correct": 0,
                "explanation": "All Spanish question words carry a mandatory accent mark."
            },
            {
                "id": "d20-ex4",
                "type": "translation",
                "prompt": "Translate: 'How many sisters do you have?'",
                "options": ["¿Cuántas hermanas tienes?", "¿Cuántos hermanas tienes?", "¿Qué hermanas tienes?", "¿Cuál hermanas tienes?"],
                "correct": 0,
                "explanation": "'Hermanas' is feminine plural, so use '¿Cuántas hermanas tienes?'."
            }
        ],
        "speakingChallenge": [
            {"prompt": "Answer the question in a complete sentence: ¿Por qué estudias español?", "hint": "Estudio español porque...", "sampleAnswer": "Estudio español porque me gusta el idioma y quiero viajar por España."},
            {"prompt": "Ask someone where the nearest metro station is.", "hint": "¿Dónde está la estación...", "sampleAnswer": "Disculpe, ¿dónde está la estación de metro más cercana?"},
            {"prompt": "Ask a shopkeeper how much two books cost.", "hint": "¿Cuánto cuestan dos...", "sampleAnswer": "Por favor, ¿cuánto cuestan estos dos libros?"}
        ],
        "dailyRevision": {
            "quickQuestions": [
                "What is the difference between '¿Por qué?' and 'Porque'?",
                "What is the difference between '¿Dónde?' and '¿Adónde?'?"
            ],
            "grammarRecall": "Interrogatives: qué, quién, dónde, cuándo, cómo, cuánto, cuál, por qué. All carry written accents in questions.",
            "vocabRecall": ["¿Qué?", "¿Quién?", "¿Dónde?", "¿Adónde?", "¿Cuándo?", "¿Por qué?", "Porque", "¿Cómo?", "¿Cuánto?"]
        },
        "checklist": [
            "Memorized the 8 essential Spanish question words with written accents",
            "Understood ¿Por qué? (Why?) vs. Porque (Because)",
            "Distinguished static ¿Dónde? from directional ¿Adónde?",
            "Matched ¿Cuánto/a/os/as? with noun gender and number",
            "Completed the Stage 2 Milestone Assessment Reading Passage",
            "CELEBRATED COMPLETING STAGE 2 (DAYS 11–20) — ONE THIRD OF THE CHALLENGE! 🇪🇸🎉"
        ]
    }
]

# Combine both parts
stage2_complete = stage2_days + stage2_part2

with open("d:/ag/espanol-handbook/data/lessons/stage2.js", "w", encoding="utf-8") as f:
    f.write("// Stage 2: Days 11 to 20 (Everyday Spanish)\n")
    f.write("window.STAGE_2_LESSONS = ")
    json.dump(stage2_complete, f, ensure_ascii=False, indent=2)
    f.write(";\n")

print(f"Successfully generated stage2.js with all {len(stage2_complete)} full days!")
