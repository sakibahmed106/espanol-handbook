"""
Build Stage 2: Days 11 to 20 (Everyday Spanish)
"""
import json

stage2_days = [
    {
        "day": 11,
        "stage": 2,
        "title": "Family & Relationships",
        "subtitle": "Talking about family members, relatives, and marital status",
        "goals": [
            "Name close and extended family members in Spanish",
            "Introduce your family with possessive adjectives (mi, mis, tu, tus)",
            "Talk about age, marital status, and occupations of family members",
            "Express familial relationships clearly"
        ],
        "bengaliNote": "In Bangla, family relationships are deeply cherished and respected (বাবা, মা, ভাই, বোন, দাদা, চাচা). In Spanish culture, family (*la familia*) is equally central. Notice that Spanish uses the masculine plural to refer to both parents (*los padres*) and both grandparents (*los abuelos*).",
        "vocabulary": [
            {"word": "La familia", "translation": "The family", "pos": "noun", "gender": "feminine", "example": "Mi familia es muy unida.", "exampleTranslation": "My family is very close-knit."},
            {"word": "El padre / La madre", "translation": "The father / The mother (Los padres = the parents)", "pos": "noun", "gender": "masculine / feminine", "example": "Mis padres viven en Bangladés.", "exampleTranslation": "My parents live in Bangladesh."},
            {"word": "El hermano / La hermana", "translation": "The brother / The sister (Los hermanos = siblings)", "pos": "noun", "gender": "masculine / feminine", "example": "Tengo dos hermanos y una hermana.", "exampleTranslation": "I have two brothers and one sister."},
            {"word": "El hijo / La hija", "translation": "The son / The daughter (Los hijos = children/offspring)", "pos": "noun", "gender": "masculine / feminine", "example": "Ellos tienen tres hijos.", "exampleTranslation": "They have three children."},
            {"word": "El abuelo / La abuela", "translation": "The grandfather / The grandmother (Los abuelos = grandparents)", "pos": "noun", "gender": "masculine / feminine", "example": "Mi abuela cocina de maravilla.", "exampleTranslation": "My grandmother cooks wonderfully."},
            {"word": "El tío / La tía", "translation": "The uncle / The aunt", "pos": "noun", "gender": "masculine / feminine", "example": "Mi tío trabaja en un hospital.", "exampleTranslation": "My uncle works in a hospital."},
            {"word": "El primo / La prima", "translation": "The cousin (male / female)", "pos": "noun", "gender": "masculine / feminine", "example": "Mis primos son muy simpáticos.", "exampleTranslation": "My cousins are very nice."},
            {"word": "El esposo / La esposa", "translation": "The husband / The wife (also: el marido / la mujer)", "pos": "noun", "gender": "masculine / feminine", "example": "Su esposo es ingeniero.", "exampleTranslation": "Her husband is an engineer."},
            {"word": "Casado / Soltero", "translation": "Married / Single", "pos": "adjective", "gender": "masculine", "example": "Soy soltero, no estoy casado.", "exampleTranslation": "I am single, I am not married."},
            {"word": "Mayor / Menor", "translation": "Older / Younger", "pos": "adjective", "gender": None, "example": "Tengo un hermano mayor y una hermana menor.", "exampleTranslation": "I have an older brother and a younger sister."}
        ],
        "sentences": [
            {"spanish": "¿Tienes hermanos?", "english": "Do you have siblings?"},
            {"spanish": "Sí, tengo un hermano mayor y una hermana menor.", "english": "Yes, I have an older brother and a younger sister."},
            {"spanish": "Mis padres viven en Daca y están muy bien.", "english": "My parents live in Dhaka and are doing very well."},
            {"spanish": "¿Cómo se llama tu madre?", "english": "What is your mother's name?"},
            {"spanish": "Mi madre se llama Fatima y es profesora.", "english": "My mother's name is Fatima and she is a teacher."},
            {"spanish": "Somos cinco personas en mi familia.", "english": "We are five people in my family."}
        ],
        "grammar": {
            "title": "Basic Possessive Adjectives & Collective Plural Nouns",
            "explanation": "Possessive adjectives (my, your, his/her) in Spanish must match the NUMBER of the item possessed, not the owner!",
            "rules": [
                "My: 'mi' (singular) / 'mis' (plural). E.g. *mi hermano* (my brother) vs. *mis hermanos* (my brothers/siblings).",
                "Your (informal): 'tu' (singular) / 'tus' (plural). E.g. *tu padre* vs. *tus padres*. (Remember: 'tu' possessive has no accent, while 'tú' pronoun does!)",
                "His / Her / Your (formal) / Their: 'su' (singular) / 'sus' (plural). E.g. *su coche* vs. *sus libros*.",
                "Collective Plurals: Spanish uses the masculine plural to refer to mixed-gender groups: *los padres* = father + mother (parents); *los hermanos* = brothers + sisters (siblings); *los hijos* = sons + daughters (children); *los abuelos* = grandparents.",
                "Marital Status uses ESTAR: *Está casado / Está soltero / Está divorciado*."
            ],
            "structures": [
                "Possessive Singular: mi / tu / su + [Singular Noun]",
                "Possessive Plural: mis / tus / sus + [Plural Noun]",
                "Stating Marital Status: Estar + casado(a) / soltero(a)"
            ],
            "examples": [
                {"spanish": "Mi hermana es estudiante.", "english": "My sister is a student."},
                {"spanish": "Mis hermanas son estudiantes.", "english": "My sisters are students."},
                {"spanish": "¿Dónde viven tus abuelos?", "english": "Where do your grandparents live?"},
                {"spanish": "Mi tío está soltero.", "english": "My uncle is single."}
            ],
            "commonMistakes": [
                {"wrong": "Mi padres", "right": "Mis padres", "explanation": "Because 'padres' is plural, 'mi' must become 'mis'."},
                {"wrong": "Soy casado", "right": "Estoy casado", "explanation": "Marital status is considered a state of life, so it strictly takes 'estar'."}
            ],
            "proTip": "In Spain, people often casually use *marido* for husband and *mujer* for wife instead of *esposo/esposa*."
        },
        "conversation": {
            "title": "Showing Photos of Family",
            "context": "Sakib and his friend Elena look at photos on Sakib's phone over coffee.",
            "dialogue": [
                {"speaker": "Elena", "role": "Friend", "spanish": "Sakib, ¿quiénes son las personas de esta foto?", "english": "Sakib, who are the people in this photo?"},
                {"speaker": "Sakib", "role": "Student", "spanish": "Son mis padres y mis dos hermanos. Esta es mi familia.", "english": "They are my parents and my two brothers. This is my family."},
                {"speaker": "Elena", "role": "Friend", "spanish": "¡Qué familia tan bonita! ¿Cuántos años tienen tus hermanos?", "english": "What a beautiful family! How old are your brothers?"},
                {"speaker": "Sakib", "role": "Student", "spanish": "Mi hermano mayor tiene veintiocho años y el menor tiene diecinueve.", "english": "My older brother is twenty-eight and the younger is nineteen."},
                {"speaker": "Elena", "role": "Friend", "spanish": "¿Y ellos también viven en Bangladés?", "english": "And do they also live in Bangladesh?"},
                {"speaker": "Sakib", "role": "Student", "spanish": "Sí, todos viven allí. Hablamos por videollamada los domingos.", "english": "Yes, they all live there. We talk on video call on Sundays."}
            ],
            "keyPhrases": [
                {"phrase": "¿Quiénes son?", "explanation": "'Who are they?' (Plural form of ¿Quién?)."},
                {"phrase": "¡Qué familia tan bonita!", "explanation": "'What such a beautiful family!' (Expressive exclamation)."},
                {"phrase": "Por videollamada", "explanation": "'Via video call'."}
            ]
        },
        "reading": {
            "title": "La familia de Sakib",
            "passage": "La familia de Sakib es muy unida y cariñosa. Sus padres viven en una casa con jardín en Bangladés. Su padre es un hombre trabajador y su madre es profesora en una escuela local. Sakib tiene un hermano mayor que se llama Tariq y está casado. También tiene una hermana menor que se llama Samira y es estudiante universitaria. Aunque Sakib ahora vive lejos, en Madrid, siempre recuerda a su familia con mucho amor y habla con sus padres todas las semanas.",
            "translation": "Sakib's family is very close-knit and loving. His parents live in a house with a garden in Bangladesh. His father is a hardworking man and his mother is a teacher at a local school. Sakib has an older brother named Tariq who is married. He also has a younger sister named Samira who is a university student. Although Sakib now lives far away, in Madrid, he always remembers his family with much love and talks with his parents every week.",
            "questions": [
                {"question": "¿A qué se dedica la madre de Sakib?", "options": ["Es médica", "Es profesora en una escuela local", "Es ingeniera", "Trabaja en un banco"], "answer": 1, "explanation": "His mother is a teacher ('su madre es profesora')."},
                {"question": "¿Cómo se llama el hermano mayor de Sakib?", "options": ["Carlos", "Tariq", "Javier", "Samira"], "answer": 1, "explanation": "His older brother is Tariq ('se llama Tariq')."},
                {"question": "¿Dónde viven los padres de Sakib?", "options": ["En Madrid", "En Bangladés", "En Sevilla", "En Londres"], "answer": 1, "explanation": "They live in Bangladesh ('viven en una casa con jardín en Bangladés')."}
            ]
        },
        "exercises": [
            {
                "id": "d11-ex1",
                "type": "fill-in",
                "prompt": "Choose the correct possessive: ______ (My) hermanos son simpáticos.",
                "options": ["Mis", "Mi", "Tu", "Su"],
                "correct": 0,
                "explanation": "Because 'hermanos' is plural, the possessive is 'Mis'."
            },
            {
                "id": "d11-ex2",
                "type": "multiple-choice",
                "prompt": "What does 'los padres' mean in Spanish?",
                "options": ["Only the fathers", "The parents (father and mother)", "The uncles", "The grandparents"],
                "correct": 1,
                "explanation": "'Los padres' means 'the parents'."
            },
            {
                "id": "d11-ex3",
                "type": "multiple-choice",
                "prompt": "How do you say 'My uncle is married' in Spanish?",
                "options": ["Mi tío es casado", "Mi tío está casado", "Mi tío tiene casado", "Mi tío hay casado"],
                "correct": 1,
                "explanation": "Marital status uses 'estar': 'está casado'."
            },
            {
                "id": "d11-ex4",
                "type": "translation",
                "prompt": "Translate: 'Do you have brothers or sisters?' (informal)",
                "options": ["¿Tienes hermanos?", "¿Eres hermanos?", "¿Estás hermanos?", "¿Dónde hermanos?"],
                "correct": 0,
                "explanation": "'¿Tienes hermanos?' is the natural way to ask about siblings."
            }
        ],
        "speakingChallenge": [
            {"prompt": "Say how many people are in your family in Spanish.", "hint": "En mi familia somos [número] personas...", "sampleAnswer": "En mi familia somos cinco personas: mis padres, mis hermanos y yo."},
            {"prompt": "State your siblings' names and ages.", "hint": "Tengo un hermano que tiene...", "sampleAnswer": "Tengo un hermano mayor que tiene veintiocho años."},
            {"prompt": "State your mother's or father's profession.", "hint": "Mi madre es... / Mi padre es...", "sampleAnswer": "Mi madre es profesora y mi padre es comerciante."}
        ],
        "dailyRevision": {
            "quickQuestions": [
                "What is the difference between 'mi' and 'mis'?",
                "Why do we say 'está casado' instead of 'es casado'?"
            ],
            "grammarRecall": "Possessives: mi/mis, tu/tus, su/sus. Mixed groups: los padres, los hermanos, los hijos.",
            "vocabRecall": ["La familia", "El padre", "La madre", "El hermano", "El abuelo", "Casado", "Soltero"]
        },
        "checklist": [
            "Learned the names of close and extended family members",
            "Matched possessive adjectives (mi vs mis) with plural nouns",
            "Used collective plural nouns (los padres, los abuelos)",
            "Described marital status using 'estar'",
            "Completed all 4 family exercises",
            "Described my own family out loud in Spanish"
        ]
    },
    {
        "day": 12,
        "stage": 2,
        "title": "Food & Everyday Drinks",
        "subtitle": "Essential groceries, Spanish cuisine, and ordering meals",
        "goals": [
            "Name essential everyday food items and beverages in Spanish",
            "Navigate a Spanish market, bakery, and grocery store",
            "Express hunger and thirst using 'Tener hambre' and 'Tener sed'",
            "Understand iconic Spanish culinary staples (tapas, paella, tortilla, jamón)"
        ],
        "bengaliNote": "Food is culture! Just like rice (*arroz*) and fish (*pescado*) are staple foods in Bengal (মাছে ভাতে বাঙালি), bread (*pan*), olive oil (*aceite de oliva*), and potatoes (*patatas*) are staples in Spain. In Spanish, you don't say 'I am hungry'; you say 'I have hunger' (*Tengo hambre*)!",
        "vocabulary": [
            {"word": "La comida / La bebida", "translation": "The food / The drink", "pos": "noun", "gender": "feminine", "example": "La comida española es deliciosa.", "exampleTranslation": "Spanish food is delicious."},
            {"word": "El pan", "translation": "The bread", "pos": "noun", "gender": "masculine", "example": "Compro una barra de pan.", "exampleTranslation": "I buy a loaf of bread."},
            {"word": "El agua", "translation": "The water (feminine noun, takes 'el' in singular)", "pos": "noun", "gender": "feminine", "example": "Un vaso de agua fría, por favor.", "exampleTranslation": "A glass of cold water, please."},
            {"word": "El café / El té", "translation": "The coffee / The tea", "pos": "noun", "gender": "masculine", "example": "Tomo café con leche por la mañana.", "exampleTranslation": "I drink coffee with milk in the morning."},
            {"word": "El arroz", "translation": "The rice", "pos": "noun", "gender": "masculine", "example": "Me gusta comer arroz con verduras.", "exampleTranslation": "I like to eat rice with vegetables."},
            {"word": "La carne / El pescado", "translation": "The meat / The fish", "pos": "noun", "gender": "feminine / masculine", "example": "Hoy prefiero pescado fresco.", "exampleTranslation": "Today I prefer fresh fish."},
            {"word": "La fruta / Las verduras", "translation": "The fruit / The vegetables", "pos": "noun", "gender": "feminine", "example": "Como fruta todos los días.", "exampleTranslation": "I eat fruit every day."},
            {"word": "El queso / Los huevos", "translation": "The cheese / The eggs", "pos": "noun", "gender": "masculine", "example": "Una tortilla de patatas con huevos.", "exampleTranslation": "A potato omelette with eggs."},
            {"word": "Tener hambre / Tener sed", "translation": "To be hungry / To be thirsty (literally: to have hunger/thirst)", "pos": "phrase", "gender": None, "example": "Tengo mucha hambre, ¿vamos a comer?", "exampleTranslation": "I am very hungry, shall we go eat?"},
            {"word": "El desayuno, El almuerzo, La cena", "translation": "Breakfast, Lunch, Dinner", "pos": "noun", "gender": "mixed", "example": "El almuerzo en España es a las dos.", "exampleTranslation": "Lunch in Spain is at two o'clock."}
        ],
        "sentences": [
            {"spanish": "Tengo mucha hambre, ¿dónde podemos comer?", "english": "I am very hungry, where can we eat?"},
            {"spanish": "Tengo sed, quiero un vaso de agua.", "english": "I am thirsty, I want a glass of water."},
            {"spanish": "¿Qué desayunas por las mañanas?", "english": "What do you have for breakfast in the mornings?"},
            {"spanish": "Normalmente desayuno tostadas con aceite de oliva y té.", "english": "Normally I have toast with olive oil and tea for breakfast."},
            {"spanish": "¿Cuánto cuesta el kilo de tomates?", "english": "How much does a kilogram of tomatoes cost?"},
            {"spanish": "La tortilla española lleva patatas y huevos.", "english": "The Spanish omelette contains potatoes and eggs."}
        ],
        "grammar": {
            "title": "Expressing Hunger & Thirst (Tener) + The 'El Agua' Phenomenon",
            "explanation": "In Spanish, physical sensations like hunger, thirst, heat, and cold are expressed using **TENER + Noun**, not 'to be'!",
            "rules": [
                "Hunger: *Tengo hambre* (literally: I have hunger). To say 'very hungry', use *mucha hambre* (because hambre is feminine): *Tengo mucha hambre*.",
                "Thirst: *Tengo sed* (literally: I have thirst). To say 'very thirsty', use *mucha sed* (sed is feminine): *Tengo mucha sed*.",
                "The 'El Agua' Rule: 'Agua' is a feminine noun. However, because it starts with a stressed 'a' sound, Spanish uses the masculine article 'el' (*el agua*) in singular to prevent vowel clash. In plural, it returns to feminine: *las aguas*. Any adjective remains feminine: *el agua fría* (cold water)!",
                "Meals in Spain: *El desayuno* (around 8–9 AM), *El almuerzo / La comida* (the main meal of the day, 2:00–3:30 PM), *La cena* (late dinner, 9:00–10:30 PM)."
            ],
            "structures": [
                "Sensation formula: Tener + hambre / sed / frío / calor",
                "Degree: Tener + mucho(a) + [Sensation] (Tengo mucha hambre)",
                "Ordering grocery: Un kilo de [Alimento], por favor"
            ],
            "examples": [
                {"spanish": "¿Tienes hambre? —Sí, mucha.", "english": "Are you hungry? —Yes, very."},
                {"spanish": "El agua está muy fresca.", "english": "The water is very fresh/cool."},
                {"spanish": "Quiero comprar un kilo de manzanas.", "english": "I want to buy a kilo of apples."},
                {"spanish": "Cenamos a las nueve y media.", "english": "We have dinner at nine thirty."}
            ],
            "commonMistakes": [
                {"wrong": "Soy hambriento / Estoy hambre", "right": "Tengo hambre", "explanation": "Spanish uses 'tener' (to have) for hunger and thirst."},
                {"wrong": "El agua frío", "right": "El agua fría", "explanation": "Even though 'agua' takes 'el' to prevent pronunciation clash, the noun is feminine, so adjectives are feminine."}
            ],
            "proTip": "In Spain, if you order water in a restaurant, the waiter will ask: *¿Del tiempo o fría?* ('Room temperature or cold?') and *¿Con gas o sin gas?* ('Sparkling or still?')."
        },
        "conversation": {
            "title": "At the Traditional Market (El Mercado)",
            "context": "Sakib visits Mercado de San Antón in Madrid to buy fresh groceries.",
            "dialogue": [
                {"speaker": "Frutero", "role": "Fruit vendor", "spanish": "¡Buenos días, joven! ¿Qué le pongo hoy?", "english": "Good morning, young man! What can I get you today?"},
                {"speaker": "Sakib", "role": "Shopper", "spanish": "Buenos días. Quería un kilo de plátanos y medio kilo de tomates.", "english": "Good morning. I would like a kilo of bananas and half a kilo of tomatoes."},
                {"speaker": "Frutero", "role": "Fruit vendor", "spanish": "Muy bien. Los tomates están riquísimos hoy. ¿Alguna cosa más?", "english": "Very well. The tomatoes are delicious today. Anything else?"},
                {"speaker": "Sakib", "role": "Shopper", "spanish": "Sí, ¿tiene naranjas de Valencia?", "english": "Yes, do you have oranges from Valencia?"},
                {"speaker": "Frutero", "role": "Fruit vendor", "spanish": "¡Por supuesto! Las mejores de España. ¿Cuántas quiere?", "english": "Of course! The best in Spain. How many do you want?"},
                {"speaker": "Sakib", "role": "Shopper", "spanish": "Dos kilos, por favor. ¿Cuánto es en total?", "english": "Two kilos, please. How much is it in total?"},
                {"speaker": "Frutero", "role": "Fruit vendor", "spanish": "Son seis euros con cincuenta céntimos.", "english": "That is six euros and fifty cents."},
                {"speaker": "Sakib", "role": "Shopper", "spanish": "Aquí tiene. ¡Muchas gracias!", "english": "Here you go. Thank you very much!"}
            ],
            "keyPhrases": [
                {"phrase": "Quería...", "explanation": "Polite conditional form meaning 'I would like...' (softer than 'quiero')."},
                {"phrase": "¿Alguna cosa más?", "explanation": "Standard shop phrase: 'Anything else?'"},
                {"phrase": "Riquísimo(a)", "explanation": "Superlative of 'rico' meaning 'super delicious'."}
            ]
        },
        "reading": {
            "title": "La gastronomía española y los horarios",
            "passage": "La comida en España es un acto social muy importante. Las familias y los amigos se reúnen para comer juntos y hablar durante horas; esta costumbre se llama «la sobremesa». El plato más conocido internacionalmente es la paella, que tiene arroz, azafrán, verduras y carne o marisco. Otro plato fundamental es la tortilla de patatas. Los españoles comen más tarde que en otros países: el almuerzo es entre las dos y las tres de la tarde, y la cena es a partir de las nueve de la noche.",
            "translation": "Food in Spain is a very important social act. Families and friends gather to eat together and talk for hours; this custom is called 'la sobremesa'. The most internationally known dish is paella, which has rice, saffron, vegetables, and meat or seafood. Another fundamental dish is the potato omelette. Spaniards eat later than in other countries: lunch is between two and three in the afternoon, and dinner is from nine at night onwards.",
            "questions": [
                {"question": "¿Cómo se llama la costumbre de charlar en la mesa después de comer?", "options": ["La siesta", "La sobremesa", "La paella", "La tapa"], "answer": 1, "explanation": "It is called 'la sobremesa'."},
                {"question": "¿Cuál es el ingrediente principal de la paella?", "options": ["El pan", "El arroz", "La pasta", "El queso"], "answer": 1, "explanation": "The main base of paella is rice ('tiene arroz')."},
                {"question": "¿A qué hora suele ser el almuerzo en España?", "options": ["A las doce", "Entre las dos y las tres de la tarde", "A las seis de la tarde", "A las diez de la noche"], "answer": 1, "explanation": "Lunch is between 2:00 and 3:00 PM."}
            ]
        },
        "exercises": [
            {
                "id": "d12-ex1",
                "type": "multiple-choice",
                "prompt": "How do you say 'I am very hungry' in Spanish?",
                "options": ["Estoy muy hambriento", "Tengo mucha hambre", "Soy mucho hambre", "Tengo muy hambre"],
                "correct": 1,
                "explanation": "Spanish uses 'Tener mucha hambre' (hambre is feminine noun)."
            },
            {
                "id": "d12-ex2",
                "type": "fill-in",
                "prompt": "Complete: Un vaso de agua ______ (cold), por favor.",
                "options": ["fría", "frío", "frías", "fríos"],
                "correct": 0,
                "explanation": "'Agua' is grammatically feminine, so the adjective must be 'fría'."
            },
            {
                "id": "d12-ex3",
                "type": "multiple-choice",
                "prompt": "What is 'la sobremesa' in Spanish culture?",
                "options": ["A dessert", "The table cloth", "The conversation after eating at the table", "A bill payment"],
                "correct": 2,
                "explanation": "'La sobremesa' is the beloved cultural practice of relaxing and chatting around the table after finishing a meal."
            },
            {
                "id": "d12-ex4",
                "type": "translation",
                "prompt": "Translate: 'How much does a kilo of apples cost?'",
                "options": ["¿Cuánto cuesta el kilo de manzanas?", "¿Dónde está el kilo de manzanas?", "¿Cuántas manzanas hay?", "¿Quién quiere manzanas?"],
                "correct": 0,
                "explanation": "'¿Cuánto cuesta el kilo de manzanas?' asks for the price per kilogram."
            }
        ],
        "speakingChallenge": [
            {"prompt": "Say that you are very thirsty and want a glass of cold water.", "hint": "Tengo mucha sed y quiero...", "sampleAnswer": "Tengo mucha sed, quiero un vaso de agua fría, por favor."},
            {"prompt": "Describe your typical breakfast in Spanish.", "hint": "Por la mañana desayuno...", "sampleAnswer": "Por las mañanas desayuno pan tostado con huevos y una taza de té."},
            {"prompt": "Order 1 kilo of rice and 2 kilos of oranges in a Spanish market.", "hint": "Quería un kilo de... y dos kilos de...", "sampleAnswer": "Buenos días, quería un kilo de arroz y dos kilos de naranjas, por favor."}
        ],
        "dailyRevision": {
            "quickQuestions": [
                "Why do we say 'el agua' instead of 'la agua', yet 'el agua fría'?",
                "What verb is used for hunger and thirst?"
            ],
            "grammarRecall": "Tener hambre / sed. 'Agua' takes 'el' in singular, but remains feminine for adjectives (agua fría).",
            "vocabRecall": ["La comida", "El pan", "El agua", "El arroz", "Tener hambre", "Tener sed", "El almuerzo"]
        },
        "checklist": [
            "Mastered Spanish names for essential foods and drinks",
            "Expressed hunger and thirst accurately using 'Tener'",
            "Learned the special rule of 'el agua fría'",
            "Practiced buying fruit at the market dialogue",
            "Understood the Spanish meal schedule and 'la sobremesa'",
            "Completed all 4 food exercises"
        ]
    },
    {
        "day": 13,
        "stage": 2,
        "title": "Home, Rooms & Household Objects",
        "subtitle": "Describing your apartment, rooms, furniture, and prepositions of location",
        "goals": [
            "Name the main rooms in a house or apartment (piso)",
            "Identify key pieces of furniture and household objects",
            "Use spatial prepositions (encima de, debajo de, al lado de, delante de, detrás de)",
            "Describe where things are located in your living space"
        ],
        "bengaliNote": "In Spain, most city residents live in a *piso* (apartment/flat) rather than a freestanding *casa*. Notice that prepositions in Spanish use compound phrases with 'de' (যেমন: *al lado de* = beside; *encima de* = on top of), which match nicely with Bangla postpositions (যেমন: টেবিলের ওপরে, দরজার পাশে).",
        "vocabulary": [
            {"word": "La casa / El piso", "translation": "The house / The apartment (flat)", "pos": "noun", "gender": "feminine / masculine", "example": "Vivo en un piso en el centro.", "exampleTranslation": "I live in an apartment in the center."},
            {"word": "La habitación / El dormitorio", "translation": "The room / The bedroom", "pos": "noun", "gender": "feminine / masculine", "example": "Mi habitación tiene una ventana grande.", "exampleTranslation": "My room has a large window."},
            {"word": "El salón / La sala de estar", "translation": "The living room", "pos": "noun", "gender": "masculine / feminine", "example": "En el salón hay un sofá cómodo.", "exampleTranslation": "In the living room there is a comfortable sofa."},
            {"word": "La cocina", "translation": "The kitchen", "pos": "noun", "gender": "feminine", "example": "Cocino todos los días en la cocina.", "exampleTranslation": "I cook every day in the kitchen."},
            {"word": "El baño", "translation": "The bathroom", "pos": "noun", "gender": "masculine", "example": "¿Dónde está el baño, por favor?", "exampleTranslation": "Where is the bathroom, please?"},
            {"word": "La cama", "translation": "The bed", "pos": "noun", "gender": "feminine", "example": "Duermo en una cama grande.", "exampleTranslation": "I sleep in a big bed."},
            {"word": "La silla / El sofá", "translation": "The chair / The sofa", "pos": "noun", "gender": "feminine / masculine", "example": "Hay cuatro sillas en el comedor.", "exampleTranslation": "There are four chairs in the dining room."},
            {"word": "La puerta / La ventana", "translation": "The door / The window", "pos": "noun", "gender": "feminine", "example": "Abre la ventana, por favor.", "exampleTranslation": "Open the window, please."},
            {"word": "Encima de / Debajo de", "translation": "On top of / Underneath", "pos": "prepositional phrase", "gender": None, "example": "Las llaves están encima de la mesa.", "exampleTranslation": "The keys are on top of the table."},
            {"word": "Al lado de / Cerca de", "translation": "Next to, beside / Near to", "pos": "prepositional phrase", "gender": None, "example": "La farmacia está al lado del banco.", "exampleTranslation": "The pharmacy is next to the bank."}
        ],
        "sentences": [
            {"spanish": "Mi piso tiene dos habitaciones, un salón, una cocina y un baño.", "english": "My apartment has two bedrooms, a living room, a kitchen, and a bathroom."},
            {"spanish": "¿Dónde están mis llaves? —Están encima de la mesa.", "english": "Where are my keys? —They are on top of the table."},
            {"spanish": "El gato duerme debajo de la cama.", "english": "The cat sleeps underneath the bed."},
            {"spanish": "La lámpara está al lado del sofá.", "english": "The lamp is next to the sofa."},
            {"spanish": "Mi habitación es pequeña, pero muy luminosa y tranquila.", "english": "My room is small, but very bright and quiet."},
            {"spanish": "Hay una mesa con cuatro sillas en la cocina.", "english": "There is a table with four chairs in the kitchen."}
        ],
        "grammar": {
            "title": "HAY vs. ESTÁ & Prepositions of Spatial Location",
            "explanation": "Two of the most crucial tools for describing spaces are knowing when to use **HAY** (there is / there are) versus **ESTÁ / ESTÁN** (is / are located), and using prepositions of place.",
            "rules": [
                "HAY (Existence): Use 'hay' to state the existence of something unspecific (with un/una/unos/unas, numbers, or indefinite words): *Hay una mesa en la cocina* (There is a table in the kitchen). *Hay tres sillas* (There are three chairs). Note: 'Hay' never changes in plural!",
                "ESTÁ / ESTÁN (Location): Use 'está' (singular) or 'están' (plural) to state the specific location of known items (with definite articles el/la/los/las, possessives, or names): *La mesa está en la cocina* (The table is in the kitchen). *Mis llaves están en la mesa*.",
                "Key Spatial Prepositions: *encima de* (on/above), *debajo de* (under), *al lado de* (next to), *delante de* (in front of), *detrás de* (behind), *entre* (between), *dentro de* (inside), *fuera de* (outside).",
                "Watch the contraction: *al lado de + el banco* -> *al lado del banco*!"
            ],
            "structures": [
                "Existence: Hay + un / una / unos / unas / [Número] + [Objeto]",
                "Location: [Objeto específico] + está / están + [Preposición] + [Lugar]",
                "Preposition formula: encima de / debajo de / al lado de + [Lugar]"
            ],
            "examples": [
                {"spanish": "En mi piso hay tres habitaciones. (Hay: Existence)", "english": "In my apartment there are three rooms."},
                {"spanish": "El ordenador está encima del escritorio. (Estar: Location)", "english": "The computer is on top of the desk."},
                {"spanish": "¿Hay un baño cerca de aquí?", "english": "Is there a bathroom near here?"},
                {"spanish": "El baño está al final del pasillo.", "english": "The bathroom is at the end of the hallway."}
            ],
            "commonMistakes": [
                {"wrong": "Hay el libro en la mesa", "right": "El libro está en la mesa (or: Hay un libro en la mesa)", "explanation": "'Hay' is never used with definite articles (el/la/los/las)."},
                {"wrong": "Al lado de el sofá", "right": "Al lado del sofá", "explanation": "'De + el' must contract to 'del'."}
            ],
            "proTip": "A quick test: If you are introducing something new into the conversation, use **HAY** ('There is a great café nearby'). If the listener already knows what you are talking about, use **ESTAR** ('The café is around the corner')."
        },
        "conversation": {
            "title": "Describing an Apartment to a Friend",
            "context": "Sakib shows his newly rented Madrid apartment to his classmate Carlos.",
            "dialogue": [
                {"speaker": "Carlos", "role": "Friend", "spanish": "¡Vaya, Sakib! ¡Qué piso tan bonito y luminoso!", "english": "Wow, Sakib! What a beautiful and bright apartment!"},
                {"speaker": "Sakib", "role": "Tenant", "spanish": "Gracias, Carlos. Pasa, pasa. Este es el salón.", "english": "Thank you, Carlos. Come in, come in. This is the living room."},
                {"speaker": "Carlos", "role": "Friend", "spanish": "Me encanta el sofá. Y la mesa de madera es preciosa. ¿Cuántas habitaciones tiene?", "english": "I love the sofa. And the wooden table is gorgeous. How many rooms does it have?"},
                {"speaker": "Sakib", "role": "Tenant", "spanish": "Tiene dos habitaciones. Mi dormitorio está a la derecha y la cocina está al lado del baño.", "english": "It has two rooms. My bedroom is to the right and the kitchen is next to the bathroom."},
                {"speaker": "Carlos", "role": "Friend", "spanish": "¿Y el balcón? ¿Hay balcón?", "english": "And the balcony? Is there a balcony?"},
                {"speaker": "Sakib", "role": "Tenant", "spanish": "Sí, mira por la ventana. Desde el balcón se ve una plaza muy bonita.", "english": "Yes, look through the window. From the balcony you can see a very pretty plaza."}
            ],
            "keyPhrases": [
                {"phrase": "¡Vaya!", "explanation": "Conversational interjection expressing pleasant surprise or admiration: 'Wow!'"},
                {"phrase": "Pasa, pasa", "explanation": "'Come in, come in' — warm welcoming phrase when receiving guests."},
                {"phrase": "Me encanta", "explanation": "'I love it' (stronger than me gusta)."}
            ]
        },
        "reading": {
            "title": "La vida en un piso de Madrid",
            "passage": "En las grandes ciudades de España, como Madrid o Barcelona, la mayoría de los jóvenes viven en pisos compartidos. El piso de Sakib está situado en el barrio de Chamberí, un barrio tradicional y seguro. En el piso hay tres habitaciones: una para Sakib, otra para un estudiante italiano y otra para un estudiante español. Comparten la cocina y el salón. En el salón hay una estantería grande llena de libros, un sofá cómodo y una televisión. Es un lugar perfecto para practicar español todos los días con sus compañeros.",
            "translation": "In Spain's big cities, like Madrid or Barcelona, most young people live in shared apartments. Sakib's apartment is located in the Chamberí neighborhood, a traditional and safe area. In the apartment there are three bedrooms: one for Sakib, another for an Italian student, and another for a Spanish student. They share the kitchen and living room. In the living room there is a large bookshelf full of books, a comfortable sofa, and a television. It is a perfect place to practice Spanish every day with his flatmates.",
            "questions": [
                {"question": "¿En qué barrio de Madrid vive Sakib?", "options": ["En Malasaña", "En Chamberí", "En Salamanca", "En Lavapiés"], "answer": 1, "explanation": "In Chamberí ('en el barrio de Chamberí')."},
                {"question": "¿Con quién comparte el piso Sakib?", "options": ["Con su familia", "Con un estudiante italiano y un estudiante español", "Vive solo", "Con su profesor"], "answer": 1, "explanation": "With an Italian student and a Spanish student."},
                {"question": "¿Qué hay en el salón?", "options": ["Una cama grande", "Una estantería con libros, un sofá y una televisión", "Solo una mesa", "Un coche"], "answer": 1, "explanation": "A bookshelf, sofa, and television."}
            ]
        },
        "exercises": [
            {
                "id": "d13-ex1",
                "type": "multiple-choice",
                "prompt": "Choose HAY or ESTÁ: En mi cocina ______ una mesa blanca.",
                "options": ["hay", "está", "están", "es"],
                "correct": 0,
                "explanation": "'Una mesa' (indefinite item) states existence, so use 'hay'."
            },
            {
                "id": "d13-ex2",
                "type": "fill-in",
                "prompt": "Complete: Las llaves están encima ______ (of the) mesa.",
                "options": ["de la", "del", "en la", "a la"],
                "correct": 0,
                "explanation": "'Encima de' + feminine 'la mesa' = 'encima de la mesa'."
            },
            {
                "id": "d13-ex3",
                "type": "fill-in",
                "prompt": "Choose HAY or ESTÁN: Los libros ______ en la estantería.",
                "options": ["están", "hay", "son", "tienen"],
                "correct": 0,
                "explanation": "'Los libros' is a specific known item, so use 'están' for location."
            },
            {
                "id": "d13-ex4",
                "type": "translation",
                "prompt": "Translate: 'The kitchen is next to the living room.'",
                "options": ["La cocina está al lado del salón.", "La cocina hay al lado el salón.", "La cocina es cerca del salón.", "La cocina está encima del salón."],
                "correct": 0,
                "explanation": "'La cocina está al lado del salón' (note de + el = del)."
            }
        ],
        "speakingChallenge": [
            {"prompt": "Describe your room: what furniture is inside it?", "hint": "En mi habitación hay una cama, un...", "sampleAnswer": "En mi habitación hay una cama, una mesa de estudio y un armario grande."},
            {"prompt": "Say where your phone is right now using a preposition.", "hint": "Mi teléfono está encima de...", "sampleAnswer": "Mi teléfono está encima de la mesa, al lado del ordenador."},
            {"prompt": "Tell a guest where the bathroom is.", "hint": "El baño está al final...", "sampleAnswer": "El baño está al fondo a la derecha."}
        ],
        "dailyRevision": {
            "quickQuestions": [
                "What is the difference between 'Hay un libro' and 'El libro está'?",
                "What prepositional phrase means 'next to'?"
            ],
            "grammarRecall": "HAY + un/una/números (existence). ESTAR + el/la/posesivo (location). Encima de, debajo de, al lado de.",
            "vocabRecall": ["El piso", "La habitación", "El salón", "La cocina", "El baño", "Encima de", "Al lado de"]
        },
        "checklist": [
            "Named all the main rooms of a home",
            "Identified household furniture items",
            "Mastered the difference between HAY and ESTAR",
            "Applied spatial prepositions (encima de, debajo de, al lado de)",
            "Completed all 4 home exercises",
            "Described my study space out loud in Spanish"
        ]
    },
    {
        "day": 14,
        "stage": 2,
        "title": "Common Adjectives & Agreement Rules",
        "subtitle": "Mastering gender, number agreement, and colors to describe everything",
        "goals": [
            "Learn essential high-frequency descriptive adjectives and common colors",
            "Apply the golden rule: adjectives must match their noun in both gender AND number",
            "Understand adjectives that don't change for gender (-e and consonant endings)",
            "Place adjectives in their natural Spanish position (after the noun)"
        ],
        "bengaliNote": "In English and Bangla, adjectives never change their form whether describing one thing or ten things (e.g. 'red book' or 'red books'; 'লাল বই'). In Spanish, adjectives are active chameleons! If the noun is feminine plural, the adjective MUST also become feminine plural (*el libro rojo* -> *las casas rojas*).",
        "vocabulary": [
            {"word": "Grande / Pequeño(a)", "translation": "Big / Small", "pos": "adjective", "gender": "neutral / variable", "example": "Madrid es una ciudad grande.", "exampleTranslation": "Madrid is a big city."},
            {"word": "Bueno(a) / Malo(a)", "translation": "Good / Bad", "pos": "adjective", "gender": "variable", "example": "Es una buena idea.", "exampleTranslation": "It is a good idea."},
            {"word": "Bonito(a) / Feo(a)", "translation": "Pretty, beautiful / Ugly", "pos": "adjective", "gender": "variable", "example": "Una casa muy bonita.", "exampleTranslation": "A very pretty house."},
            {"word": "Alto(a) / Bajo(a)", "translation": "Tall, high / Short, low", "pos": "adjective", "gender": "variable", "example": "Mi hermano es alto y delgado.", "exampleTranslation": "My brother is tall and slim."},
            {"word": "Nuevo(a) / Viejo(a)", "translation": "New / Old", "pos": "adjective", "gender": "variable", "example": "Tengo un coche nuevo.", "exampleTranslation": "I have a new car."},
            {"word": "Fácil / Difícil", "translation": "Easy / Difficult", "pos": "adjective", "gender": "neutral", "example": "El español es fácil si practicas.", "exampleTranslation": "Spanish is easy if you practice."},
            {"word": "Rápido(a) / Lento(a)", "translation": "Fast / Slow", "pos": "adjective", "gender": "variable", "example": "El tren de alta velocidad es muy rápido.", "exampleTranslation": "The high-speed train is very fast."},
            {"word": "Blanco(a) / Negro(a)", "translation": "White / Black", "pos": "adjective", "gender": "variable", "example": "Una camisa blanca y pantalones negros.", "exampleTranslation": "A white shirt and black trousers."},
            {"word": "Rojo(a) / Azul / Verde / Amarillo(a)", "translation": "Red / Blue / Green / Yellow", "pos": "adjective", "gender": "mixed", "example": "La bandera española es roja y amarilla.", "exampleTranslation": "The Spanish flag is red and yellow."},
            {"word": "Interesante / Importante", "translation": "Interesting / Important", "pos": "adjective", "gender": "neutral", "example": "Es una lección muy importante.", "exampleTranslation": "It is a very important lesson."}
        ],
        "sentences": [
            {"spanish": "Madrid tiene parques grandes y calles bonitas.", "english": "Madrid has big parks and beautiful streets."},
            {"spanish": "Mi mochila es azul y mis zapatos son negros.", "english": "My backpack is blue and my shoes are black."},
            {"spanish": "Esta lección no es difícil, es muy interesante.", "english": "This lesson is not difficult, it is very interesting."},
            {"spanish": "Carlos tiene dos coches viejos pero rápidos.", "english": "Carlos has two old but fast cars."},
            {"spanish": "La comida española es muy buena.", "english": "Spanish food is very good."},
            {"spanish": "Tengo una pregunta importante para el profesor.", "english": "I have an important question for the teacher."}
        ],
        "grammar": {
            "title": "The Golden Rule of Adjective Agreement & Position",
            "explanation": "In Spanish, an adjective is married to its noun: they share the same gender (masculine/feminine) and the same number (singular/plural)!",
            "rules": [
                "4-Form Adjectives (-o/-a/-os/-as): Adjectives ending in -o have four distinct forms: *rojo, roja, rojos, rojas*. E.g. *el libro rojo, la mesa roja, los libros rojos, las mesas rojas*.",
                "2-Form Adjectives (-e or Consonant): Adjectives ending in -e (*grande, interesante, verde*) or a consonant (*azul, fácil, joven*) do NOT change for gender! They only change for number (+s or +es): *un chico inteligente / una chica inteligente* -> *unos chicos inteligentes / unas chicas inteligentes*.",
                "Adjectives of Nationality: Special rule: nationalities ending in a consonant add -a for feminine: *español -> española*, *inglés -> inglesa*.",
                "Adjective Placement: In 90% of cases, descriptive adjectives follow the noun: *el coche rojo* (never *el rojo coche*).",
                "Bueno & Malo: When placed before a masculine singular noun, *bueno* drops the -o to become *buen*: *un buen amigo*."
            ],
            "structures": [
                "Agreement Formula: Noun [M/F, S/P] + Adjective [Matching M/F, S/P]",
                "Standard Order: Sustantivo + Adjetivo descriptivo (la casa blanca)",
                "Plural formation: -vowel + s (grandes) | -consonant + es (azules, fáciles)"
            ],
            "examples": [
                {"spanish": "El chico alto -> La chica alta", "english": "The tall boy -> The tall girl"},
                {"spanish": "Los chicos altos -> Las chicas altas", "english": "The tall boys -> The tall girls"},
                {"spanish": "Un problema difícil -> Unos problemas difíciles", "english": "A difficult problem -> Difficult problems"},
                {"spanish": "La casa verde -> Las casas verdes", "english": "The green house -> The green houses"}
            ],
            "commonMistakes": [
                {"wrong": "Las chicas alto", "right": "Las chicas altas", "explanation": "The adjective must agree in both gender and plural: 'altas'."},
                {"wrong": "La coche roja", "right": "El coche rojo", "explanation": "'Coche' is masculine, so it takes 'el' and 'rojo'."},
                {"wrong": "El rojo vestido", "right": "El vestido rojo", "explanation": "Descriptive color adjectives must come AFTER the noun."}
            ],
            "proTip": "Remember: Adjectives ending in -e or consonants (*grande, azul, fácil, inteligente*) are gender-neutral! They work equally for men, women, and objects without altering their ending."
        },
        "conversation": {
            "title": "Shopping for a Jacket in Gran Vía",
            "context": "Sakib shops for a winter jacket in a Madrid clothing boutique.",
            "dialogue": [
                {"speaker": "Dependienta", "role": "Shop clerk", "spanish": "¡Hola! Buenas tardes. ¿Le puedo ayudar en algo?", "english": "Hello! Good afternoon. Can I help you with anything?"},
                {"speaker": "Sakib", "role": "Shopper", "spanish": "Sí, busco una chaqueta abrigada para el invierno.", "english": "Yes, I am looking for a warm jacket for winter."},
                {"speaker": "Dependienta", "role": "Shop clerk", "spanish": "Tenemos esta chaqueta negra que es muy elegante, o esta azul.", "english": "We have this black jacket which is very elegant, or this blue one."},
                {"speaker": "Sakib", "role": "Shopper", "spanish": "La azul me gusta mucho. ¿Tiene una talla más grande?", "english": "I like the blue one a lot. Do you have a larger size?"},
                {"speaker": "Dependienta", "role": "Shop clerk", "spanish": "Sí, aquí tiene una talla L. Pruébela.", "english": "Yes, here is a size L. Try it on."},
                {"speaker": "Sakib", "role": "Shopper", "spanish": "Me queda perfecta. Es muy cómoda y no es cara.", "english": "It fits me perfectly. It is very comfortable and not expensive."},
                {"speaker": "Dependienta", "role": "Shop clerk", "spanish": "¡Estupendo! Vamos a la caja.", "english": "Wonderful! Let's go to the cash register."}
            ],
            "keyPhrases": [
                {"phrase": "Busco...", "explanation": "'I am looking for...' (verb buscar)."},
                {"phrase": "Me queda perfecta", "explanation": "'It fits me perfectly'."},
                {"phrase": "Talla", "explanation": "'Clothing size' (for shoe size, use 'número')."}
            ]
        },
        "reading": {
            "title": "Los colores de las ciudades españolas",
            "passage": "Cada ciudad de España tiene sus propios colores característicos. En el sur, en Andalucía, los pueblos son completamente blancos: las casas blancas reflejan el sol brillante del verano y mantienen el interior fresco. En Madrid, los edificios históricos combinan el ladrillo rojo con el granito gris. En el norte de España, en Galicia y Asturias, el paisaje es intensamente verde debido a las lluvias frecuentes. Y por todas partes, el cielo azul mediterráneo ilumina la vida diaria de sus habitantes.",
            "translation": "Each city in Spain has its own characteristic colors. In the south, in Andalusia, the villages are completely white: the white houses reflect the brilliant summer sun and keep the interior cool. In Madrid, historic buildings combine red brick with gray granite. In the north of Spain, in Galicia and Asturias, the landscape is intensely green due to frequent rains. And everywhere, the Mediterranean blue sky illuminates the daily life of its inhabitants.",
            "questions": [
                {"question": "¿De qué color son las casas en los pueblos de Andalucía?", "options": ["Rojas", "Blancas", "Azules", "Amarillas"], "answer": 1, "explanation": "The houses are white ('las casas blancas')."},
                {"question": "¿Por qué el paisaje del norte es verde?", "options": ["Por la pintura", "Por las lluvias frecuentes", "Porque no hay sol", "Por el frío"], "answer": 1, "explanation": "Due to frequent rains ('debido a las lluvias frecuentes')."},
                {"question": "¿Qué materiales combinan los edificios históricos de Madrid?", "options": ["Ladrillo rojo y granito gris", "Madera y plástico", "Oro y plata", "Cristal verde"], "answer": 0, "explanation": "Red brick and gray granite."}
            ]
        },
        "exercises": [
            {
                "id": "d14-ex1",
                "type": "fill-in",
                "prompt": "Make the adjective agree: Una ciudad ______ (bonito).",
                "options": ["bonita", "bonito", "bonitas", "bonitos"],
                "correct": 0,
                "explanation": "'Ciudad' is feminine singular, so the adjective is 'bonita'."
            },
            {
                "id": "d14-ex2",
                "type": "fill-in",
                "prompt": "Make plural: Dos estudiantes ______ (inteligente).",
                "options": ["inteligentes", "inteligentas", "inteligentos", "inteligente"],
                "correct": 0,
                "explanation": "Adjectives ending in -e simply add -s in plural: 'inteligentes'."
            },
            {
                "id": "d14-ex3",
                "type": "multiple-choice",
                "prompt": "Where do descriptive adjectives usually go in Spanish?",
                "options": ["Before the noun", "After the noun", "At the very end of the sentence", "Anywhere randomly"],
                "correct": 1,
                "explanation": "Descriptive adjectives normally follow the noun: 'el libro rojo'."
            },
            {
                "id": "d14-ex4",
                "type": "translation",
                "prompt": "Translate: 'The blue shoes are very comfortable.'",
                "options": ["Los zapatos azules son muy cómodos.", "Los zapatos azul son muy cómodo.", "Los azules zapatos son cómodos.", "Las zapatas azules están cómodas."],
                "correct": 0,
                "explanation": "'Los zapatos azules son muy cómodos' agrees in masculine plural across all words."
            }
        ],
        "speakingChallenge": [
            {"prompt": "Describe your clothes right now (colors and items).", "hint": "Llevo una camisa blanca y...", "sampleAnswer": "Llevo una camiseta azul y unos pantalones negros."},
            {"prompt": "Describe your city in two sentences using adjectives.", "hint": "Mi ciudad es grande, ruidosa y...", "sampleAnswer": "Daca es una ciudad muy grande, vibrante y poblada."},
            {"prompt": "Say that Spanish is interesting and important.", "hint": "El español es un idioma...", "sampleAnswer": "El español es un idioma muy interesante e importante para mi futuro."}
        ],
        "dailyRevision": {
            "quickQuestions": [
                "Do adjectives ending in -e (like 'grande') change for feminine?",
                "How do you make an adjective ending in a consonant (like 'azul') plural?"
            ],
            "grammarRecall": "-o/-a/-os/-as (4 forms) | -e/-es & cons/-es (2 forms). Position: Sustantivo + Adjetivo.",
            "vocabRecall": ["Grande", "Pequeño", "Bonito", "Fácil", "Difícil", "Rojo", "Azul", "Blanco", "Negro"]
        },
        "checklist": [
            "Matched adjective gender and number to nouns",
            "Identified 2-form adjectives (-e and consonants)",
            "Learned core color words in Spanish",
            "Placed descriptive adjectives after nouns naturally",
            "Completed all 4 adjective exercises",
            "Described physical objects aloud with full agreement"
        ]
    },
    {
        "day": 15,
        "stage": 2,
        "title": "Regular Present Tense: -AR Verbs",
        "subtitle": "Conjugating Hablar, Trabajar, Estudiar, Escuchar, Comprar + Mid-Stage 2 Review",
        "goals": [
            "Understand how verb stems and personal endings work in Spanish",
            "Master the complete present tense conjugation of regular -AR verbs",
            "Conjugate high-frequency verbs: hablar, estudiar, trabajar, escuchar, comprar, viajar",
            "Complete the Stage 2 Mid-Point Revision (Days 11 to 15 review)"
        ],
        "bengaliNote": "In Bangla, verb endings change depending on who is speaking (যেমন: আমি বলি, তুমি বলো, সে বলে, আপনি বলেন). Spanish works on the exact same elegant principle! To conjugate an -AR verb, drop the '-ar' and add the matching ending: -o, -as, -a, -amos, -áis, -an.",
        "vocabulary": [
            {"word": "Hablar", "translation": "To speak / To talk", "pos": "verb", "gender": None, "example": "Hablo español con mis amigos.", "exampleTranslation": "I speak Spanish with my friends."},
            {"word": "Estudiar", "translation": "To study", "pos": "verb", "gender": None, "example": "Estudio tres horas al día.", "exampleTranslation": "I study three hours a day."},
            {"word": "Trabajar", "translation": "To work", "pos": "verb", "gender": None, "example": "¿Dónde trabajas tú?", "exampleTranslation": "Where do you work?"},
            {"word": "Escuchar", "translation": "To listen to", "pos": "verb", "gender": None, "example": "Escucho música española en Spotify.", "exampleTranslation": "I listen to Spanish music on Spotify."},
            {"word": "Comprar", "translation": "To buy", "pos": "verb", "gender": None, "example": "Compramos fruta en el mercado.", "exampleTranslation": "We buy fruit at the market."},
            {"word": "Viajar", "translation": "To travel", "pos": "verb", "gender": None, "example": "Me gusta viajar en tren por España.", "exampleTranslation": "I like to travel by train through Spain."},
            {"word": "Buscar", "translation": "To look for / To search", "pos": "verb", "gender": None, "example": "Busco la estación de metro.", "exampleTranslation": "I am looking for the subway station."},
            {"word": "Preguntar", "translation": "To ask (a question)", "pos": "verb", "gender": None, "example": "Pregunto una duda a la profesora.", "exampleTranslation": "I ask the teacher a question."},
            {"word": "Necesitar", "translation": "To need", "pos": "verb", "gender": None, "example": "Necesito practicar más la pronunciación.", "exampleTranslation": "I need to practice pronunciation more."},
            {"word": "Tomar", "translation": "To take / To drink / To consume", "pos": "verb", "gender": None, "example": "Por las mañanas tomo té con limón.", "exampleTranslation": "In the mornings I drink tea with lemon."}
        ],
        "sentences": [
            {"spanish": "Yo hablo bengalí e inglés, y ahora estudio español.", "english": "I speak Bengali and English, and now I study Spanish."},
            {"spanish": "¿Dónde trabajas tú? —Trabajo en una empresa tecnológica.", "english": "Where do you work? —I work at a tech company."},
            {"spanish": "Nosotros estudiamos juntos en la biblioteca.", "english": "We study together in the library."},
            {"spanish": "¿Vosotros viajáis mucho los fines de semana?", "english": "Do you all travel a lot on weekends? (Spain informal plural)"},
            {"spanish": "Ellos escuchan la radio en español todos los días.", "english": "They listen to Spanish radio every day."},
            {"spanish": "Necesito comprar un cuaderno nuevo.", "english": "I need to buy a new notebook."}
        ],
        "grammar": {
            "title": "The Master -AR Conjugation Chart: -o, -as, -a, -amos, -áis, -an",
            "explanation": "Every Spanish verb has two parts: the **stem** (root meaning) and the **ending** (tells you who is doing the action and when). For regular -AR verbs, drop the '-ar' and attach the personal endings!",
            "rules": [
                "Stem Formula: Infinitivo HABLAR minus -AR = Stem 'HABL-'.",
                "Yo: add -o -> hablo (I speak)",
                "Tú: add -as -> hablas (You speak / তুমি বলো)",
                "Él / Ella / Usted: add -a -> habla (He/She speaks, You formal speak / আপনি বলেন)",
                "Nosotros / Nosotras: add -amos -> hablamos (We speak)",
                "Vosotros / Vosotras: add -áis -> habláis (You all speak / তোমরা বলো - Spain only!)",
                "Ellos / Ellas / Ustedes: add -an -> hablan (They speak, You all speak)"
            ],
            "structures": [
                "-AR Present Endings: -o | -as | -a | -amos | -áis | -an",
                "Trabajar: trabajo, trabajas, trabaja, trabajamos, trabajáis, trabajan",
                "Estudiar: estudio, estudias, estudia, estudiamos, estudiáis, estudian",
                "Escuchar: escucho, escuchas, escucha, escuchamos, escucháis, escuchan"
            ],
            "examples": [
                {"spanish": "Hablo español. (Yo)", "english": "I speak Spanish."},
                {"spanish": "¿Hablas inglés? (Tú)", "english": "Do you speak English?"},
                {"spanish": "El profesor habla despacio. (Él)", "english": "The teacher speaks slowly."},
                {"spanish": "Trabajamos mucho esta semana. (Nosotros)", "english": "We work a lot this week."}
            ],
            "commonMistakes": [
                {"wrong": "Yo hablar español", "right": "Yo hablo español", "explanation": "You must conjugate the verb to match the subject; don't leave it in the infinitive (-ar)."},
                {"wrong": "Nosotros estudian", "right": "Nosotros estudiamos", "explanation": "The 'nosotros' ending for -AR verbs is always '-amos'."}
            ],
            "proTip": "Notice that the 'Yo' form for almost EVERY regular verb in Spanish ends in the letter **-O** (*hablo, trabajo, estudio, compro*)! It makes identifying first-person speech immediate."
        },
        "conversation": {
            "title": "Talking About Study and Work Routines",
            "context": "Sakib and his classmate Laura take a study break in the university cafeteria.",
            "dialogue": [
                {"speaker": "Laura", "role": "Classmate", "spanish": "Sakib, ¿tú solo estudias o también trabajas?", "english": "Sakib, do you only study or do you also work?"},
                {"speaker": "Sakib", "role": "Student", "spanish": "Por ahora solo estudio español a tiempo completo. ¿Y tú, Laura?", "english": "For now I only study Spanish full time. And you, Laura?"},
                {"speaker": "Laura", "role": "Classmate", "spanish": "Yo trabajo por las mañanas en una librería y estudio por las tardes.", "english": "I work in the mornings at a bookstore and study in the afternoons."},
                {"speaker": "Sakib", "role": "Student", "spanish": "¡Qué trabajadora eres! ¿Y escuchas música mientras estudias?", "english": "How hardworking you are! And do you listen to music while you study?"},
                {"speaker": "Laura", "role": "Classmate", "spanish": "Sí, siempre escucho música clásica para concentrarme.", "english": "Yes, I always listen to classical music to concentrate."},
                {"speaker": "Sakib", "role": "Student", "spanish": "Yo necesito silencio absoluto cuando estudio gramática.", "english": "I need absolute silence when I study grammar."}
            ],
            "keyPhrases": [
                {"phrase": "A tiempo completo", "explanation": "'Full time' (vs. a tiempo parcial = part time)."},
                {"phrase": "Mientras", "explanation": "'While / Meanwhile'."},
                {"phrase": "Para concentrarme", "explanation": "'In order to concentrate (myself)'."}
            ]
        },
        "reading": {
            "title": "Mid-Stage 2 Review: La vida activa de los estudiantes",
            "passage": "En Madrid, miles de estudiantes internacionales estudian y trabajan todos los días. Sakib y sus amigos pasan muchas horas en la biblioteca central. Por las mañanas hablan español con los profesores, preguntan sus dudas y toman notas en sus cuadernos. A las dos de la tarde compran unos bocadillos en la cafetería y descansan en el jardín. Por la noche, Sakib habla por videollamada con su familia en Bangladés y les cuenta todo lo que aprende. Ya comprende oraciones completas y se siente muy motivado.",
            "translation": "In Madrid, thousands of international students study and work every day. Sakib and his friends spend many hours in the central library. In the mornings they speak Spanish with the teachers, ask their questions, and take notes in their notebooks. At two in the afternoon they buy some sandwiches in the cafeteria and rest in the garden. At night, Sakib speaks on video call with his family in Bangladesh and tells them everything he learns. He already understands complete sentences and feels very motivated.",
            "questions": [
                {"question": "¿Dónde pasan muchas horas Sakib y sus amigos?", "options": ["En el cine", "En la biblioteca central", "En el metro", "En una tienda"], "answer": 1, "explanation": "In the central library ('en la biblioteca central')."},
                {"question": "¿Qué compran a las dos de la tarde?", "options": ["Libros", "Unos bocadillos en la cafetería", "Ropa", "Billetes"], "answer": 1, "explanation": "Some sandwiches ('unos bocadillos en la cafetería')."},
                {"question": "¿Con quién habla Sakib por videollamada por la noche?", "options": ["Con la profesora", "Con su familia en Bangladés", "Con el camarero", "Con el médico"], "answer": 1, "explanation": "With his family in Bangladesh ('con su familia en Bangladés')."}
            ]
        },
        "exercises": [
            {
                "id": "d15-ex1",
                "type": "fill-in",
                "prompt": "Conjugate HABLAR for 'yo': Yo ______ español e inglés.",
                "options": ["hablo", "hablas", "habla", "hablamos"],
                "correct": 0,
                "explanation": "Yo form ends in -o: 'hablo'."
            },
            {
                "id": "d15-ex2",
                "type": "fill-in",
                "prompt": "Conjugate TRABAJAR for 'nosotros': Nosotros ______ en una oficina.",
                "options": ["trabajamos", "trabajan", "trabajáis", "trabajas"],
                "correct": 0,
                "explanation": "Nosotros form for -AR verbs ends in -amos: 'trabajamos'."
            },
            {
                "id": "d15-ex3",
                "type": "multiple-choice",
                "prompt": "What is the 'vosotros' ending for -AR verbs in Spain?",
                "options": ["-áis", "-éis", "-ís", "-an"],
                "correct": 0,
                "explanation": "The vosotros ending for -AR is '-áis' (e.g. habláis, estudiáis)."
            },
            {
                "id": "d15-ex4",
                "type": "translation",
                "prompt": "Translate: 'They listen to music every day.'",
                "options": ["Ellos escuchan música todos los días.", "Ellos escucha música todos los días.", "Ellos escuchamos música cada día.", "Ellos escuchar música siempre."],
                "correct": 0,
                "explanation": "'Ellos escuchan música todos los días' has accurate subject-verb agreement."
            }
        ],
        "speakingChallenge": [
            {"prompt": "Say where you study and what language you practice.", "hint": "Estudio en... y practico...", "sampleAnswer": "Estudio en mi casa y practico español todos los días."},
            {"prompt": "Ask someone what music they listen to.", "hint": "¿Qué música escuchas...", "sampleAnswer": "¿Qué tipo de música escuchas cuando estudias?"},
            {"prompt": "Conjugate the verb TRABAJAR aloud for all 6 persons.", "hint": "Trabajo, trabajas...", "sampleAnswer": "Yo trabajo, tú trabajas, él trabaja, nosotros trabajamos, vosotros trabajáis, ellos trabajan."}
        ],
        "dailyRevision": {
            "quickQuestions": [
                "What are the 6 personal endings for regular -AR verbs?",
                "What letter does the 'Yo' form end in for almost all present tense verbs?"
            ],
            "grammarRecall": "-AR Endings: -o, -as, -a, -amos, -áis, -an.",
            "vocabRecall": ["Hablar", "Estudiar", "Trabajar", "Escuchar", "Comprar", "Viajar", "Necesitar"]
        },
        "checklist": [
            "Conjugated regular -AR verbs in all 6 persons",
            "Identified the verb stem and attached appropriate endings",
            "Mastered the 'vosotros' ending (-áis) used in Spain",
            "Completed the Mid-Stage 2 reading review passage",
            "Passed all 4 verb conjugation exercises",
            "Conjugated a full -AR verb aloud without hesitation"
        ]
    }
]

print(f"Loaded {len(stage2_days)} initial days for Stage 2.")
