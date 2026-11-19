"""
Build Stage 6: Days 56 to 59
"""
import json

stage6_part2 = [
    {
        "day": 56,
        "stage": 6,
        "title": "Comprehensive Reading: A Journey Through Spain",
        "subtitle": "A Grand Tour of Madrid, Barcelona, Sevilla, Granada, and Santiago de Compostela",
        "goals": [
            "Read an authentic, multi-city cultural travel text spanning northern and southern Spain",
            "Synthesize descriptive adjectives, historical facts, and preterite past narrations",
            "Understand Spain's regional diversity: Castile, Catalonia, Andalusia, Galicia",
            "Answer advanced CEFR A1 reading comprehension questions"
        ],
        "bengaliNote": "Spain is a tapestry of distinct cultures, landscapes, and languages! From Madrid's grand avenues to Barcelona's modernist Gaudi architecture, Seville's flamenco courtyards, Granada's Moorish Alhambra, and Santiago's misty pilgrim paths. Reading this text will prove how far your reading comprehension has soared!",
        "vocabulary": [
            {"word": "El viaje por España", "translation": "The journey through Spain", "pos": "noun", "gender": "masculine", "example": "Mi viaje por España fue inolvidable.", "exampleTranslation": "My journey through Spain was unforgettable."},
            {"word": "El patrimonio de la humanidad", "translation": "World Heritage (UNESCO)", "pos": "noun", "gender": "masculine", "example": "La Alhambra es patrimonio de la humanidad.", "exampleTranslation": "The Alhambra is World Heritage."},
            {"word": "El peregrino / El Camino de Santiago", "translation": "The pilgrim / The Way of Saint James", "pos": "noun", "gender": "masculine", "example": "Miles de peregrinos caminan a Santiago.", "exampleTranslation": "Thousands of pilgrims walk to Santiago."},
            {"word": "El monumento árabe / La mezquita / La catedral", "translation": "Arab monument / Mosque / Cathedral", "pos": "noun", "gender": "mixed", "example": "Los arcos árabes son impresionantes.", "exampleTranslation": "The Arab arches are impressive."},
            {"word": "La arquitectura modernista", "translation": "Modernist architecture (Gaudí in Barcelona)", "pos": "noun", "gender": "feminine", "example": "La Sagrada Familia es arquitectura modernista.", "exampleTranslation": "The Sagrada Familia is modernist architecture."},
            {"word": "La costa / El mar / La playa", "translation": "The coast / The sea / The beach", "pos": "noun", "gender": "mixed", "example": "El mar Mediterráneo es cálido y azul.", "exampleTranslation": "The Mediterranean sea is warm and blue."},
            {"word": "El paisaje verde / La montaña", "translation": "Green landscape / The mountain", "pos": "noun", "gender": "masculine / feminine", "example": "Galicia tiene un paisaje verde y frondoso.", "exampleTranslation": "Galicia has a lush green landscape."},
            {"word": "La diversidad cultural", "translation": "Cultural diversity", "pos": "noun", "gender": "feminine", "example": "España destaca por su gran diversidad cultural.", "exampleTranslation": "Spain stands out for its great cultural diversity."},
            {"word": "Inolvidable / Impresionante", "translation": "Unforgettable / Impressive", "pos": "adjective", "gender": "neutral", "example": "Una experiencia totalmente inolvidable.", "exampleTranslation": "A totally unforgettable experience."},
            {"word": "Enamorarse de un país", "translation": "To fall in love with a country", "pos": "phrase", "gender": None, "example": "Me he enamorado de este hermoso país.", "exampleTranslation": "I have fallen in love with this beautiful country."}
        ],
        "sentences": [
            {"spanish": "España es un país fascinante con paisajes, gastronomía e historias únicas.", "english": "Spain is a fascinating country with unique landscapes, gastronomy, and histories."},
            {"spanish": "En Barcelona visité la impresionante basílica de la Sagrada Familia de Antoni Gaudí.", "english": "In Barcelona I visited Antoni Gaudi's impressive basilica of the Sagrada Familia."},
            {"spanish": "Sevilla me enamoró con el aroma de sus naranjos y la pasión del flamenco.", "english": "Seville made me fall in love with the scent of its orange trees and the passion of flamenco."},
            {"spanish": "En Granada contemplé la Alhambra roja bajo las cumbres nevadas de Sierra Nevada.", "english": "In Granada I gazed at the red Alhambra beneath the snowy peaks of Sierra Nevada."},
            {"spanish": "El norte de Galicia es verde y húmedo, y los peregrinos llegan emocionados a Santiago.", "english": "Northern Galicia is green and humid, and pilgrims arrive deeply moved in Santiago."},
            {"spanish": "Viajar por España me permitió practicar español en cada rincón y con todo tipo de personas.", "english": "Traveling through Spain allowed me to practice Spanish in every corner and with all kinds of people."}
        ],
        "grammar": {
            "title": "Comprehensive Text Synthesis: Descriptive Flow & Regional Collocations",
            "explanation": "At Day 56, you possess the full structural grammar engine to read long editorial texts without relying on dictionaries.",
            "rules": [
                "Layer 1: Structural Scaffolding: Time markers (*En primer lugar, a continuación, finalmente*) guide the reader through geographic transitions.",
                "Layer 2: Descriptive Adjectives: Post-nominal descriptive adjectives bring monuments to life (*paisaje verde, catedral gótica, arcos árabes*).",
                "Layer 3: Preterite Verbs: Actions of travel, arrival, and discovery drive the narrative (*viajé, descubrí, contemplé, sentí*).",
                "Layer 4: Prepositional Accuracy: Note *enamorarse DE* (fall in love with), *viajar POR* (travel through), and *llegar A* (arrive at)."
            ],
            "structures": [
                "Geographic Passage: De [Ciudad Norte] a [Ciudad Sur], pasando por [Región]",
                "Emotional Impact: [Lugar] me impresionó por su [cualidad]",
                "Synthesis: Fue una experiencia que combinó [historia] y [cultura]"
            ],
            "examples": [
                {"spanish": "Viajé por toda Andalucía en tren.", "english": "I traveled through all of Andalusia by train."},
                {"spanish": "La mezquita de Córdoba me impresionó profundamente.", "english": "The mosque of Cordoba impressed me deeply."},
                {"spanish": "Caminé junto a los peregrinos en Galicia.", "english": "I walked alongside the pilgrims in Galicia."},
                {"spanish": "El viaje combinó arte, historia y buena comida.", "english": "The trip combined art, history, and good food."}
            ],
            "commonMistakes": [
                {"wrong": "Viajar para España (when meaning through)", "right": "Viajar por España", "explanation": "Travel through or around an area takes 'por'."},
                {"wrong": "Enamorarse con España", "right": "Enamorarse de España", "explanation": "The idiom is strictly 'enamorarse de'."}
            ],
            "proTip": "Notice how many Spanish place names carry geographic history: **Guadalquivir** comes from Arabic *al-wādī al-kabīr* (the great river); **Alhambra** comes from *al-ḥamrāʾ* (the red fortress). Spain's history is written right into its vowels and consonants!"
        },
        "conversation": {
            "title": "Planning the Dream Journey Across Spain",
            "context": "Sakib and his teacher Carmen discuss the five iconic regions of Spain on a wall map.",
            "dialogue": [
                {"speaker": "Profª Carmen", "role": "Teacher", "spanish": "Sakib, si tuvieras que elegir una ruta para mostrar España a tu familia, ¿por dónde empezarías?", "english": "Sakib, if you had to choose a route to show Spain to your family, where would you start?"},
                {"speaker": "Sakib", "role": "Student", "spanish": "Empezaría sin duda en Madrid, el corazón del país. Les enseñaría el Museo del Prado y el Palacio Real, y pasearíamos por el Parque del Retiro.", "english": "I would start without a doubt in Madrid, the heart of the country. I'd show them the Prado Museum and Royal Palace, and we'd stroll through Retiro Park."},
                {"speaker": "Profª Carmen", "role": "Teacher", "spanish": "¡Perfecto comienzo! ¿Y después hacia dónde iríais?", "english": "Perfect start! And afterward where would you go?"},
                {"speaker": "Sakib", "role": "Student", "spanish": "Tomaríamos el AVE hacia el sur, hacia Andalucía: Sevilla y Granada. Quiero que vean los jardines de la Alhambra y escuchen flamenco en directo en las cuevas del Sacromonte.", "english": "We'd take the AVE south, toward Andalusia: Seville and Granada. I want them to see the gardens of the Alhambra and hear live flamenco in the caves of Sacromonte."},
                {"speaker": "Profª Carmen", "role": "Teacher", "spanish": "¿Y el norte verde? ¿Les gustaría Galicia o Barcelona?", "english": "And the green north? Would they like Galicia or Barcelona?"},
                {"speaker": "Sakib", "role": "Student", "spanish": "¡Por supuesto! Terminaríamos en Barcelona para ver la Sagrada Familia y el mar Mediterráneo. En resumen: una ruta de contrastes inolvidables.", "english": "Of course! We'd finish in Barcelona to see the Sagrada Familia and the Mediterranean sea. In summary: an unforgettable route of contrasts."},
                {"speaker": "Profª Carmen", "role": "Teacher", "spanish": "¡Qué maravilla de itinerario! Hablas de España con la pasión y el conocimiento de un auténtico embajador cultural.", "english": "What a wonderful itinerary! You speak of Spain with the passion and knowledge of an authentic cultural ambassador."}
            ],
            "keyPhrases": [
                {"phrase": "Flamenco en directo", "explanation": "'Live flamenco' (live music/performance)."},
                {"phrase": "Ruta de contrastes", "explanation": "'Route of contrasts'."},
                {"phrase": "Embajador cultural", "explanation": "'Cultural ambassador'."}
            ]
        },
        "reading": {
            "title": "Gran lectura panorámica: Un viaje por la España de las tres culturas",
            "passage": "España es mucho más que un país europeo: es una encrucijada milenaria donde confluyeron las culturas romana, judía, musulmana y cristiana, dejando un legado artístico y arquitectónico único en el mundo.\n\nEl viaje comienza en **Madrid**, la vibrante capital situada en la meseta central. Madrid es una ciudad de cielo azul infinito, donde los museos de fama mundial como el Prado, el Reina Sofía y el Thyssen conviven con la vida callejera de terrazas animadas en barrios castizos como La Latina y Chamberí.\n\nHacia el este, a orillas del mar Mediterráneo, se alza **Barcelona**, la joya modernista de Cataluña. En sus bulevares señoriales como el Paseo de Gracia brillan las obras maestras del genial arquitecto Antoni Gaudí: la Casa Batlló, la Casa Milà y la colosal basílica de la Sagrada Familia, cuyas torres parecen esculpidas por la propia naturaleza marina.\n\nViajando hacia el sur en el tren de alta velocidad, el paisaje cambia: aparecen extensos mares de olivos plateados que conducen a **Andalucía**. En **Sevilla**, el aroma a azahar inunda el barrio de Santa Cruz, mientras el Real Alcázar y la Giralda recuerdan el pasado esplendoroso del Siglo de Oro. Más al este, en **Granada**, a los pies de las cumbres nevadas de Sierra Nevada, se levanta la **Alhambra**, la ciudadela palatina árabe más bella que existe, donde el agua de sus fuentes susurra poemas centenarios.\n\nFinalmente, el viaje culmina en el extremo noroeste, en **Galicia**, la tierra verde de la lluvia, los bosques brumosos y las rías salvajes. En **Santiago de Compostela**, miles de peregrinos de todos los continentes abrazan con emoción al Apóstol en la majestuosa catedral de piedra de la Plaza del Obradoiro tras recorrer a pie cientos de kilómetros por el milenario Camino de Santiago.\n\nPara Sakib, comprender este texto de principio a fin sin tropiezos demuestra que su 60-Day Challenge no fue solo un curso de gramática, sino una auténtica inmersión en el alma de un país.",
            "translation": "Spain is much more than a European country: it is a millennial crossroads where Roman, Jewish, Muslim, and Christian cultures converged, leaving a unique artistic and architectural legacy in the world.\n\nThe journey begins in **Madrid**, the vibrant capital situated on the central plateau. Madrid is a city of infinite blue sky, where world-famous museums like the Prado, Reina Sofia, and Thyssen coexist with the street life of lively terraces in traditional neighborhoods like La Latina and Chamberi.\n\nToward the east, on the shores of the Mediterranean Sea, rises **Barcelona**, the modernist jewel of Catalonia. On its stately boulevards like Paseo de Gracia shine the masterworks of the genius architect Antoni Gaudi: Casa Batllo, Casa Mila, and the colossal basilica of the Sagrada Familia, whose towers seem sculpted by marine nature itself.\n\nTraveling south on the high-speed train, the landscape changes: extensive seas of silver olive trees appear, leading to **Andalusia**. In **Seville**, the scent of orange blossoms floods the Santa Cruz quarter, while the Real Alcazar and the Giralda recall the splendid past of the Golden Age. Further east, in **Granada**, at the feet of the snowy peaks of Sierra Nevada, stands the **Alhambra**, the most beautiful Arab palatine citadel in existence, where the water of its fountains whispers centuries-old poems.\n\nFinally, the journey culminates in the extreme northwest, in **Galicia**, the green land of rain, misty forests, and wild estuaries. In **Santiago de Compostela**, thousands of pilgrims from all continents embrace the Apostle with emotion in the majestic stone cathedral of the Plaza del Obradoiro after walking on foot hundreds of kilometers along the millennial Way of Saint James.\n\nFor Sakib, understanding this text from beginning to end without stumbling demonstrates that his 60-Day Challenge was not just a grammar course, but an authentic immersion into the soul of a country.",
            "questions": [
                {"question": "¿Qué cuatro culturas históricas confluyeron en España según el texto?", "options": ["China, japonesa, rusa e india", "Romana, judía, musulmana y cristiana", "Vikinga y azteca", "Egipcia y griega únicamente"], "answer": 1, "explanation": "Roman, Jewish, Muslim, and Christian ('confluyeron las culturas romana, judía, musulmana y cristiana')."},
                {"question": "¿Quién fue el genial arquitecto modernista de la Sagrada Familia en Barcelona?", "options": ["Pablo Picasso", "Antoni Gaudí", "Salvador Dalí", "Diego Velázquez"], "answer": 1, "explanation": "Antoni Gaudí ('el genial arquitecto Antoni Gaudí')."},
                {"question": "¿Dónde culmina el famoso Camino de Santiago?", "options": ["En Madrid", "En la catedral de Santiago de Compostela en Galicia", "En Sevilla", "En Toledo"], "answer": 1, "explanation": "Santiago de Compostela in Galicia ('en Santiago de Compostela...')."},
                {"question": "¿Qué demuestra a Sakib entender este texto de principio a fin?", "options": ["Que necesita un traductor urgente", "Que su 60-Day Challenge fue una auténtica inmersión en el alma de un país", "Que solo sabe inglés", "Que el español es aburrido"], "answer": 1, "explanation": "An authentic immersion into the soul of a country."}
            ]
        },
        "exercises": [
            {
                "id": "d56-ex1",
                "type": "multiple-choice",
                "prompt": "Where is the famous Alhambra located in Spain?",
                "options": ["En Madrid", "En Barcelona", "En Granada (Andalucía)", "En Santiago de Compostela"],
                "correct": 2,
                "explanation": "The Alhambra is located in Granada at the foot of Sierra Nevada."
            },
            {
                "id": "d56-ex2",
                "type": "fill-in",
                "prompt": "Complete with the correct preposition: Me he enamorado ______ (of/with) la cultura española.",
                "options": ["de", "con", "en", "por"],
                "correct": 0,
                "explanation": "'Enamorarse' strictly requires the preposition 'de': 'enamorarse de'."
            },
            {
                "id": "d56-ex3",
                "type": "multiple-choice",
                "prompt": "What landscape is characteristic of Galicia in the northwest?",
                "options": ["Desierto seco", "Verde, húmedo y con bosques brumosos", "Solo playas de arena blanca", "Rascacielos industriales"],
                "correct": 1,
                "explanation": "Galicia is famous for green, lush, rainy landscapes."
            },
            {
                "id": "d56-ex4",
                "type": "translation",
                "prompt": "Translate: 'Traveling through Spain was an unforgettable experience.'",
                "options": ["Viajar por España fue una experiencia inolvidable.", "Viajar para España fue una experiencia inolvidable.", "Viajar en España estuvo una experiencia inolvidable.", "Viajar por España era una experiencia olvidable."],
                "correct": 0,
                "explanation": "'Viajar por España fue una experiencia inolvidable' uses 'por' for motion and 'fue' for evaluation."
            }
        ],
        "speakingChallenge": [
            {"prompt": "Say which Spanish city you would like to visit most and why.", "hint": "Quisiera visitar... porque me fascina...", "sampleAnswer": "Quisiera visitar Granada porque me fascinan los palacios árabes de la Alhambra y la vista de Sierra Nevada."},
            {"prompt": "Describe the contrast between Madrid and Barcelona in one sentence.", "hint": "Madrid es... mientras que Barcelona...", "sampleAnswer": "Madrid es la capital histórica en el centro, mientras que Barcelona tiene mar Mediterráneo y arquitectura modernista."},
            {"prompt": "State: 'Spanish culture is rich, diverse, and welcoming.'", "hint": "La cultura española es...", "sampleAnswer": "La cultura española es sumamente rica, diversa, acogedora y llena de historia viva."}
        ],
        "dailyRevision": {
            "quickQuestions": [
                "What preposition follows 'enamorarse'? (DE)",
                "What preposition is used when traveling through a country? (POR)"
            ],
            "grammarRecall": "Reading synthesis: Advanced descriptive vocabulary, regional heritage, preterite narrative cohesion. Enamorarse de, viajar por.",
            "vocabRecall": ["El patrimonio de la humanidad", "El peregrino", "La arquitectura modernista", "Inolvidable", "Impresionante", "La diversidad cultural", "Enamorarse de"]
        },
        "checklist": [
            "Read and understood a comprehensive 5-region cultural Spanish text",
            "Synthesized descriptive adjectives with historical narration",
            "Explored the cultural heritage of Madrid, Barcelona, Sevilla, Granada, and Santiago",
            "Answered all 4 advanced A1 reading comprehension questions",
            "Completed all 4 regional reading exercises",
            "Articulated personal travel dreams aloud in Spanish"
        ]
    },
    {
        "day": 57,
        "stage": 6,
        "title": "Conversational Fluency & Real-World Roleplays",
        "subtitle": "Interactive roleplays: 1) Hotel Check-in, 2) Market Shopping, 3) Street Directions, 4) Doctor's Office",
        "goals": [
            "Simulate 4 complete real-world immersion dialogues with speed and confidence",
            "Roleplay 1: Hotel Check-in (confirming reservation, room keys, breakfast hours, wifi password)",
            "Roleplay 2: Traditional Market (asking prices, weights, requesting fresh recommendations)",
            "Roleplay 3: Street Directions (asking lost, landmark reference points, thanking warmly)",
            "Roleplay 4: Clinic / Doctor's Office (explaining symptoms, receiving prescriptions, dosage instructions)"
        ],
        "bengaliNote": "Real fluency is not memorizing rules; it is the ability to walk into a hotel, pharmacy, train station, or market in Spain and conduct business naturally without freezing! Today's 4 roleplays test your real-world conversational reflexes across all four essential life scenarios.",
        "vocabulary": [
            {"word": "El juego de rol / La simulación", "translation": "Roleplay / Simulation", "pos": "noun", "gender": "masculine / feminine", "example": "Hacemos una simulación de conversación real.", "exampleTranslation": "We do a simulation of a real conversation."},
            {"word": "La estancia / El huésped", "translation": "The stay / The guest", "pos": "noun", "gender": "feminine / masculine", "example": "¡Que tenga una feliz estancia!", "exampleTranslation": "Have a happy stay!"},
            {"word": "La llave / La tarjeta de la habitación", "translation": "The key / Room key card", "pos": "noun", "gender": "feminine", "example": "Aquí tiene la tarjeta de su habitación.", "exampleTranslation": "Here is your room key card."},
            {"word": "La contraseña del wifi", "translation": "Wifi password", "pos": "noun", "gender": "feminine", "example": "¿Cuál es la contraseña del wifi?", "exampleTranslation": "What is the wifi password?"},
            {"word": "Medio kilo / Un cuarto de kilo", "translation": "Half a kilo (500g) / Quarter kilo (250g)", "pos": "phrase", "gender": "masculine", "example": "Póngame medio kilo de queso manchego.", "exampleTranslation": "Give me half a kilo of Manchego cheese."},
            {"word": "A mano derecha / A mano izquierda", "translation": "On the right hand side / On the left hand side", "pos": "phrase", "gender": None, "example": "El banco está a mano derecha.", "exampleTranslation": "The bank is on the right hand side."},
            {"word": "El síntoma / La receta médica", "translation": "Symptom / Medical prescription", "pos": "noun", "gender": "masculine / feminine", "example": "El médico escribe una receta.", "exampleTranslation": "The doctor writes a prescription."},
            {"word": "La dosis / Cada ocho horas", "translation": "Dose / Every eight hours", "pos": "noun / phrase", "gender": "feminine", "example": "Tome esta pastilla cada ocho horas.", "exampleTranslation": "Take this pill every eight hours."},
            {"word": "Cobrar / El cobro", "translation": "To charge / The payment collection", "pos": "verb / noun", "gender": "masculine", "example": "¿Me cobra, por favor?", "exampleTranslation": "Can you charge me, please? (ready to pay)"},
            {"word": "Despedida cordial", "translation": "Warm goodbye / Cordial farewell", "pos": "phrase", "gender": "feminine", "example": "Nos despedimos con una sonrisa cordial.", "exampleTranslation": "We say goodbye with a cordial smile."}
        ],
        "sentences": [
            {"spanish": "Buenas tardes, tengo una reserva a nombre de Sakib Ahmed.", "english": "Good afternoon, I have a reservation under the name of Sakib Ahmed. (Hotel)"},
            {"spanish": "¿A qué hora se sirve el desayuno y cuál es la clave del wifi?", "english": "At what time is breakfast served and what is the wifi code? (Hotel)"},
            {"spanish": "Póngame un kilo de naranjas y trescientos gramos de jamón, por favor.", "english": "Give me a kilo of oranges and 300 grams of ham, please. (Market)"},
            {"spanish": "Disculpe, ¿el Museo del Prado queda a mano derecha o izquierda?", "english": "Excuse me, is the Prado Museum on the right or left hand side? (Directions)"},
            {"spanish": "Doctor, me duele la garganta desde hace dos días y tengo dolor de cabeza.", "english": "Doctor, my throat has hurt for two days and I have a headache. (Clinic)"},
            {"spanish": "Tómese este medicamento con agua después de cada comida.", "english": "Take this medication with water after each meal. (Clinic)"}
        ],
        "grammar": {
            "title": "The 4 Immersion Roleplay Scripts & Polite Customer Formulas",
            "explanation": "Mastering these four foundational customer scripts prepares you for 90% of all public interactions in Spain:",
            "rules": [
                "Script 1 (Hotel Check-In): *Tengo una reserva a nombre de...* -> *Rellene esta ficha...* -> *Habitación [número] en la tercera planta...* -> *¿A qué hora es el desayuno?*.",
                "Script 2 (Market / Deli): *Póngame...* (Give me / serve me - standard polite Spain market formula!) -> *¿Algo más?* -> *¿Cuánto es todo?*.",
                "Script 3 (Street Direction): *Perdone, ¿para ir a...?* -> *Siga todo recto hasta...* -> *A mano derecha* -> *Muchas gracias por su tiempo*.",
                "Script 4 (Doctor / Health Clinic): *Me encuentro mal...* -> *Me duele...* -> *¿Desde cuándo?* -> *Desde hace dos días* -> *Tome esto cada ocho horas*."
            ],
            "structures": [
                "Ordering at market: Póngame + [cantidad] + de + [alimento]",
                "Name of booking: A nombre de [Nombre y Apellido]",
                "Duration of symptom: Desde hace + [tiempo] (desde hace tres días)"
            ],
            "examples": [
                {"spanish": "Póngame medio kilo de fresas.", "english": "Give me half a kilo of strawberries."},
                {"spanish": "La reserva está a nombre de Ahmed.", "english": "The reservation is under the name of Ahmed."},
                {"spanish": "Me duele el estómago desde hace dos días.", "english": "My stomach hurts for two days."},
                {"spanish": "La farmacia está a mano izquierda.", "english": "The pharmacy is on the left-hand side."}
            ],
            "commonMistakes": [
                {"wrong": "Dame medio kilo (too blunt/rude)", "right": "Póngame medio kilo, por favor", "explanation": "'Póngame' is the universal polite market request in Spain."},
                {"wrong": "La reserva es en mi nombre", "right": "La reserva está a nombre de Sakib", "explanation": "The proper idiom is 'a nombre de'."}
            ],
            "proTip": "In Spain, market vendors warmly call customers *«joven»* (young man/woman), *«caballero»* (gentleman), or *«guapo/guapa»* (handsome/pretty). Don't be surprised; it's affectionate cultural friendliness!"
        },
        "conversation": {
            "title": "Interactive Multi-Roleplay Simulation",
            "context": "Sakib practices four real-world micro-dialogues back to back.",
            "dialogue": [
                {"speaker": "Hotelero", "role": "Hotel clerk", "spanish": "¡Buenas tardes! Bienvenido al Hotel Cervantes.", "english": "Good afternoon! Welcome to the Cervantes Hotel."},
                {"speaker": "Sakib", "role": "Guest", "spanish": "Buenas tardes. Tengo una reserva para dos noches a nombre de Sakib Ahmed.", "english": "Good afternoon. I have a reservation for two nights under the name of Sakib Ahmed."},
                {"speaker": "Hotelero", "role": "Hotel clerk", "spanish": "Aquí está, señor Ahmed. Habitación 304. El desayuno es de siete a diez y media en la planta baja. Aquí tiene su llave.", "english": "Here it is, Mr. Ahmed. Room 304. Breakfast is from seven to ten thirty on the ground floor. Here is your key."},
                {"speaker": "Sakib", "role": "Shopper (Market)", "spanish": "Ahora en el mercado: ¡Hola! Póngame medio kilo de tomates y un cuarto de kilo de queso manchego curado, por favor.", "english": "Now at the market: Hello! Give me half a kilo of tomatoes and a quarter kilo of cured Manchego cheese, please."},
                {"speaker": "Tendero", "role": "Market clerk", "spanish": "Aquí tiene, joven. El queso está espectacular. Son seis euros con veinte.", "english": "Here you go, young man. The cheese is spectacular. That is six euros and twenty."},
                {"speaker": "Sakib", "role": "Patient (Clinic)", "spanish": "Y en la clínica: Doctor, me encuentro mal desde hace dos días. Me duele mucho la cabeza y tengo tos seca.", "english": "And at the clinic: Doctor, I have felt unwell for two days. My head hurts a lot and I have a dry cough."},
                {"speaker": "Médico", "role": "Doctor", "spanish": "Tranquilo, Sakib. Es solo un resfriado común. Beba agua tibia, descanse y tómese este jarabe cada ocho horas.", "english": "Don't worry, Sakib. It is just a common cold. Drink warm water, rest, and take this syrup every eight hours."},
                {"speaker": "Sakib", "role": "Citizen", "spanish": "¡Muchas gracias, doctor! ¡Qué bien se siente poder comunicarse con tanta seguridad!", "english": "Thank you very much, doctor! How good it feels to be able to communicate with such confidence!"}
            ],
            "keyPhrases": [
                {"phrase": "Planta baja", "explanation": "'Ground floor' (street level)."},
                {"phrase": "Queso manchego curado", "explanation": "Spain's iconic aged sheep cheese from La Mancha."},
                {"phrase": "Desde hace dos días", "explanation": "'For two days' (time duration into the present)."}
            ]
        },
        "reading": {
            "title": "La autonomía lingüística: El verdadero objetivo del nivel A1",
            "passage": "El Marco Común Europeo de Referencia para las Lenguas (MCER) define el nivel A1 no por la cantidad de reglas teóricas memorizadas en silencio, sino por la capacidad práctica de interactuar en situaciones cotidianas de supervivencia e interés inmediato. Un hablante A1 competente no necesita un traductor en el teléfono móvil para registrarse en un hotel, comprar fruta fresca en un mercado de barrio, pedir indicaciones a un policía en la calle o describir sus síntomas básicos a un médico. Esta independencia comunicativa es lo que los pedagogos denominan «autonomía lingüística». Sakib ha alcanzado este estado con creces. Ya no teme equivocarse porque sabe que la lengua es un puente vivo de conexión humana. A través de la simulación de situaciones reales, su mente ha automatizado las respuestas y su pronunciación fluye con naturalidad y cortesía.",
            "translation": "The Common European Framework of Reference for Languages (CEFR) defines level A1 not by the amount of theoretical rules memorized in silence, but by the practical ability to interact in everyday situations of survival and immediate interest. A competent A1 speaker does not need a translator on their mobile phone to register in a hotel, buy fresh fruit at a neighborhood market, ask a police officer for directions on the street, or describe their basic symptoms to a doctor. This communicative independence is what pedagogues call 'linguistic autonomy'. Sakib has reached this state with flying colors. He no longer fears making mistakes because he knows that language is a living bridge of human connection. Through the simulation of real situations, his mind has automated the answers and his pronunciation flows with naturalness and courtesy.",
            "questions": [
                {"question": "¿Cómo define el MCER el nivel A1?", "options": ["Por memorizar libros antiguos", "Por la capacidad práctica de interactuar en situaciones cotidianas de supervivencia e interés inmediato", "Por escribir poesía barroca", "Por no hablar nunca"], "answer": 1, "explanation": "Practical ability to interact in everyday survival situations."},
                {"question": "¿Qué significa el concepto de 'autonomía lingüística'?", "options": ["No necesitar a nadie nunca", "Poder desenvolverse en la vida diaria sin depender de un traductor", "Hablar solo con robots", "Vivir solo"], "answer": 1, "explanation": "Managing daily life without depending on a translator ('sin depender de un traductor')."},
                {"question": "¿Por qué Sakib ya no teme cometer errores?", "options": ["Porque ya sabe que la lengua es un puente vivo de conexión humana", "Porque no le importa nada", "Porque no habla con nadie", "Porque siempre está en silencio"], "answer": 0, "explanation": "Because language is a living bridge of human connection."}
            ]
        },
        "exercises": [
            {
                "id": "d57-ex1",
                "type": "fill-in",
                "prompt": "How do you politely order cheese at a Spanish market?: ______ (Give me) medio kilo de queso.",
                "options": ["Póngame", "Dame", "Pones", "Quiero me"],
                "correct": 0,
                "explanation": "'Póngame' is the polite market formula."
            },
            {
                "id": "d57-ex2",
                "type": "multiple-choice",
                "prompt": "How do you state a hotel booking name in Spanish?",
                "options": ["Tengo una reserva a nombre de...", "Mi reserva es con nombre...", "Tengo reserva en mi nombre...", "Hago reserva para mi nombre..."],
                "correct": 0,
                "explanation": "'Tengo una reserva a nombre de [nombre]' is the standard phrase."
            },
            {
                "id": "d57-ex3",
                "type": "fill-in",
                "prompt": "Complete duration of symptoms: Me duele la cabeza ______ (for) dos días.",
                "options": ["desde hace", "por hace", "para hace", "en hace"],
                "correct": 0,
                "explanation": "'Desde hace + tiempo' expresses duration into the present."
            },
            {
                "id": "d57-ex4",
                "type": "translation",
                "prompt": "Translate: 'What time is breakfast served?'",
                "options": ["¿A qué hora se sirve el desayuno?", "¿Cuándo desayuno está?", "¿Dónde se come desayuno?", "¿Qué hora desayuno es?"],
                "correct": 0,
                "explanation": "'¿A qué hora se sirve el desayuno?' is the natural hotel inquiry."
            }
        ],
        "speakingChallenge": [
            {"prompt": "Check in to a hotel in Spanish: state your name, reservation, and ask for wifi.", "hint": "Buenas tardes, tengo una reserva a nombre de...", "sampleAnswer": "Buenas tardes, tengo una reserva para dos noches a nombre de Sakib Ahmed. ¿Cuál es la contraseña del wifi, por favor?"},
            {"prompt": "Order fruit and cheese at a Spanish market using 'Póngame...'", "hint": "Buenos días, póngame un kilo de... y medio kilo de...", "sampleAnswer": "Buenos días, póngame un kilo de manzanas y medio kilo de queso semicurado, por favor."},
            {"prompt": "Describe a symptom to a doctor using 'Desde hace...'", "hint": "Doctor, me duele... desde hace...", "sampleAnswer": "Doctor, me duele mucho la garganta y tengo tos seca desde hace dos días."}
        ],
        "dailyRevision": {
            "quickQuestions": [
                "What is the polite phrase to order goods at a market counter? (Póngame...)",
                "How do you say 'under the name of' for reservations? (a nombre de)"
            ],
            "grammarRecall": "Real-world formulas: A nombre de, Póngame [cantidad], A mano derecha/izquierda, Desde hace [tiempo], Tómese cada ocho horas.",
            "vocabRecall": ["La estancia", "La llave", "La contraseña del wifi", "Póngame", "A mano derecha", "La receta médica", "Desde hace"]
        },
        "checklist": [
            "Completed Hotel Check-in roleplay simulation smoothly",
            "Completed Market Grocery shopping roleplay using 'Póngame'",
            "Completed Street Directions roleplay with directional markers",
            "Completed Doctor's Office clinic roleplay with symptom duration",
            "Passed all 4 real-world fluency exercises",
            "Achieved true conversational linguistic autonomy"
        ]
    },
    {
        "day": 58,
        "stage": 6,
        "title": "A1 Writing Workshop: Personal Bio & Diary",
        "subtitle": "Writing your complete personal biography, daily reflections, and dreams in Spanish",
        "goals": [
            "Write a multi-paragraph personal biography in Spanish from scratch",
            "Synthesize identity, origins, family, daily routine, past journey, and future dreams",
            "Follow professional editorial essay architecture (introducción, desarrollo, vivencias, metas)",
            "Produce an authentic Spanish writing portfolio piece for Sakib Ahmed"
        ],
        "bengaliNote": "Writing is thinking made visible! Today is your dedicated creative writing workshop. You will assemble every single thread of grammar, vocabulary, and emotion you have studied over the last 58 days into an authentic, inspiring personal bio and diary in Spanish.",
        "vocabulary": [
            {"word": "La biografía / La autobiografía", "translation": "The biography / The autobiography", "pos": "noun", "gender": "feminine", "example": "Escribo mi autobiografía en español.", "exampleTranslation": "I write my autobiography in Spanish."},
            {"word": "El diario personal", "translation": "Personal diary / journal", "pos": "noun", "gender": "masculine", "example": "Escribo en mi diario todas las noches.", "exampleTranslation": "I write in my diary every night."},
            {"word": "Los orígenes / Mis raíces", "translation": "Origins / My roots", "pos": "noun", "gender": "masculine / feminine plural", "example": "Estoy muy orgulloso de mis raíces bengalíes.", "exampleTranslation": "I am very proud of my Bengali roots."},
            {"word": "La infancia / El pasado", "translation": "Childhood / The past", "pos": "noun", "gender": "feminine / masculine", "example": "Tuve una infancia feliz rodeado de mi familia.", "exampleTranslation": "I had a happy childhood surrounded by my family."},
            {"word": "La superación personal", "translation": "Personal growth / Self-improvement", "pos": "noun", "gender": "feminine", "example": "Este reto ha sido un viaje de superación personal.", "exampleTranslation": "This challenge has been a journey of self-improvement."},
            {"word": "El sueño / Mis aspiraciones", "translation": "The dream / My aspirations", "pos": "noun", "gender": "masculine / feminine plural", "example": "Mi sueño es viajar por toda Hispanoamérica.", "exampleTranslation": "My dream is to travel through all of Spanish America."},
            {"word": "Lograr / Alcanzar una meta", "translation": "To achieve / To reach a goal", "pos": "verb", "gender": None, "example": "He logrado mi objetivo de A1.", "exampleTranslation": "I have achieved my A1 objective."},
            {"word": "La transformación", "translation": "The transformation", "pos": "noun", "gender": "feminine", "example": "He vivido una transformación maravillosa.", "exampleTranslation": "I have lived a wonderful transformation."},
            {"word": "Estar agradecido(a)", "translation": "To be grateful / thankful", "pos": "phrase", "gender": "variable", "example": "Estoy muy agradecido por esta oportunidad.", "exampleTranslation": "I am very grateful for this opportunity."},
            {"word": "El futuro / Mirar hacia adelante", "translation": "The future / To look forward", "pos": "noun / phrase", "gender": "masculine", "example": "Miro hacia el futuro con optimismo.", "exampleTranslation": "I look toward the future with optimism."}
        ],
        "sentences": [
            {"spanish": "Me llamo Sakib Ahmed, nací en Bangladés y actualmente vivo en Madrid.", "english": "My name is Sakib Ahmed, I was born in Bangladesh and currently live in Madrid."},
            {"spanish": "En mi familia somos cinco personas muy unidas y cariñosas.", "english": "In my family we are five very close-knit and loving people."},
            {"spanish": "Todos los días me despierto temprano, estudio con constancia y practico con la gente local.", "english": "Every day I wake up early, study with consistency, and practice with local people."},
            {"spanish": "El mes pasado viajé a Toledo y Segovia, donde viví experiencias inolvidables.", "english": "Last month I traveled to Toledo and Segovia, where I lived unforgettable experiences."},
            {"spanish": "Aprender español ha sido el viaje de superación personal más enriquecedor de mi vida.", "english": "Learning Spanish has been the most enriching self-improvement journey of my life."},
            {"spanish": "Miro hacia el futuro con entusiasmo porque sé que el idioma me abrirá infinitas puertas.", "english": "I look toward the future with enthusiasm because I know the language will open infinite doors for me."}
        ],
        "grammar": {
            "title": "The Master Autobiographical Architecture (The 4 Pillar Essay)",
            "explanation": "A complete personal bio weaves four distinct temporal and thematic zones:",
            "rules": [
                "Pillar 1: Identity & Origins (Present + Preterite): *Me llamo Sakib Ahmed, nací en Bangladés en 1999 y soy estudiante/profesional...*",
                "Pillar 2: Family & Routine (Present + Reflexives): *Mi familia vive en... Todos los días me levanto a las siete, estudio gramática y...*",
                "Pillar 3: The Journey & Milestones (Preterite Past): *Cuando llegué a España hace dos meses, no hablaba nada; sin embargo, viajé a Segovia, hablé con gente en los mercados y aprendí...*",
                "Pillar 4: Passions & Future Aspirations (Gustar + Near Future): *Me apasiona la cultura española. En el futuro voy a continuar hacia el nivel A2 y viajar por toda Andalucía...*"
            ],
            "structures": [
                "Bio Scaffold: 1. Identidad y origen -> 2. Familia y rutina -> 3. Vivencias pasadas -> 4. Sueños futuros"
            ],
            "examples": [
                {"spanish": "Soy un apasionado de los idiomas y la tecnología.", "english": "I am passionate about languages and technology."},
                {"spanish": "Mi meta más inmediata es certificar mi nivel A1 y seguir creciendo.", "english": "My most immediate goal is to certify my A1 level and keep growing."}
            ],
            "commonMistakes": [
                {"wrong": "Writing in only one tense (only present)", "right": "Demonstrate range by combining Present, Preterite, and Near Future", "explanation": "Mixing tenses cleanly is the ultimate proof of A1 competence."}
            ],
            "proTip": "Use your own name with pride! In Spain, introducing yourself with full name, origin, and genuine passions creates immediate warmth and respect."
        },
        "conversation": {
            "title": "Peer Reviewing the Autobiographical Essay",
            "context": "Sakib and his classmate Laura read each other's written autobiographies in workshop.",
            "dialogue": [
                {"speaker": "Laura", "role": "Peer reviewer", "spanish": "Sakib, acabo de leer tu autobiografía en español. ¡Me he emocionado muchísimo!", "english": "Sakib, I just read your autobiography in Spanish. I was so deeply moved!"},
                {"speaker": "Sakib", "role": "Author", "spanish": "¿De verdad, Laura? ¿Qué te ha parecido la estructura?", "english": "Really, Laura? What did you think of the structure?"},
                {"speaker": "Laura", "role": "Peer reviewer", "spanish": "Es perfecta. Comienzas con tus raíces en Bangladés, describes tu rutina madrileña y cuentas tu viaje a Toledo con detalles preciosos. Y el párrafo final sobre tus sueños de futuro es muy inspirador.", "english": "It is perfect. You start with your roots in Bangladesh, describe your Madrid routine, and recount your trip to Toledo with precious details. And the final paragraph about your future dreams is very inspiring."},
                {"speaker": "Sakib", "role": "Author", "spanish": "Muchas gracias, Laura. He intentado utilizar todo lo que hemos aprendido: verbos reflexivos, conectores, el pretérito y las expresiones idiomáticas.", "english": "Thank you very much, Laura. I tried to use everything we have learned: reflexive verbs, connectors, the preterite, and idiomatic expressions."},
                {"speaker": "Laura", "role": "Peer reviewer", "spanish": "Se nota el esfuerzo y el cariño. Tienes una voz propia en español, Sakib.", "english": "The effort and care show. You have your own voice in Spanish, Sakib."}
            ],
            "keyPhrases": [
                {"phrase": "Me he emocionado", "explanation": "'I was deeply moved / touched'."},
                {"phrase": "Tener una voz propia", "explanation": "'To have one's own voice (authentic expression)'."},
                {"phrase": "Se nota el esfuerzo", "explanation": "'The effort really shows'."}
            ]
        },
        "reading": {
            "title": "Autobiografía modelo: La historia de Sakib Ahmed",
            "passage": "«Mi nombre es Sakib Ahmed. Nací en Bangladés, una tierra verde y cálida de ríos majestuosos y gente hospitalaria. En mi familia somos cinco personas muy unidas: mis queridos padres, mis dos hermanos y yo. Mi padre es un comerciante honesto y mi madre es una profesora dedicada; ellos me enseñaron desde pequeño el inmenso valor de la educación y el esfuerzo constante.\n\nActualmente vivo en Madrid, una de las ciudades más hermosas, seguras y vibrantes de Europa. Mi rutina diaria es activa y disciplinada: me despierto a las siete de la mañana, preparo un té caliente y salgo hacia la academia de idiomas. En la escuela estudio gramática, tomo apuntes rigurosos y converso con compañeros de todo el mundo. Por las tardes me gusta pasear por el Parque del Retiro, hacer deporte al aire libre y cocinar comida sana en mi piso.\n\nDurante estos meses en España he vivido experiencias que guardo en mi corazón para siempre. El mes pasado viajé en tren de alta velocidad a Toledo y Segovia: caminé por calles medievales, contemplé monumentos milenarios y conversé en español en restaurantes y mercados con total soltura. Al principio tenía miedo de cometer errores; sin embargo, pronto comprendí que los errores son los mejores maestros del camino.\n\nHoy, tras casi sesenta días de estudio apasionado, miro hacia el futuro con una confianza renovada. Aprender español no solo me ha permitido dominar un vocabulario de más de seiscientas palabras y comprender la gramática básica; me ha transformado como persona. Mi sueño es seguir perfeccionando mi fluidez hacia el nivel A2 y recorrer los pueblos blancos de Andalucía y las costas de Hispanoamérica. El español ya es parte inseparable de mi identidad».",
            "translation": "'My name is Sakib Ahmed. I was born in Bangladesh, a green, warm land of majestic rivers and hospitable people. In my family we are five very close-knit people: my dear parents, my two brothers, and me. My father is an honest merchant and my mother is a dedicated teacher; they taught me from a young age the immense value of education and constant effort.\n\nCurrently I live in Madrid, one of the most beautiful, safe, and vibrant cities in Europe. My daily routine is active and disciplined: I wake up at seven in the morning, prepare hot tea, and leave for the language academy. At school I study grammar, take rigorous notes, and chat with classmates from all over the world. In the afternoons I like strolling through Retiro Park, doing sports outdoors, and cooking healthy food in my flat.\n\nDuring these months in Spain I have lived experiences that I keep in my heart forever. Last month I traveled by high-speed train to Toledo and Segovia: I walked through medieval streets, gazed at millennial monuments, and conversed in Spanish in restaurants and markets with total fluency. At first I was afraid of making mistakes; however, I soon understood that mistakes are the best teachers on the path.\n\nToday, after nearly sixty days of passionate study, I look toward the future with renewed confidence. Learning Spanish has not only allowed me to master a vocabulary of over six hundred words and understand basic grammar; it has transformed me as a person. My dream is to keep perfecting my fluency toward level A2 and travel through the white villages of Andalusia and the coasts of Spanish America. Spanish is now an inseparable part of my identity.'",
            "questions": [
                {"question": "¿Dónde nació Sakib y cómo describe su tierra natal?", "options": ["En Francia", "En Bangladés, una tierra verde y cálida de ríos majestuosos y gente hospitalaria", "En un desierto polar", "En una isla solitaria"], "answer": 1, "explanation": "In Bangladesh, a green warm land of rivers and hospitable people."},
                {"question": "¿Qué le enseñaron sus padres desde pequeño?", "options": ["A comprar coches caros", "El inmenso valor de la educación y el esfuerzo constante", "A no estudiar nunca", "A viajar solo"], "answer": 1, "explanation": "The immense value of education and constant effort."},
                {"question": "¿Qué comprendió Sakib sobre los errores?", "options": ["Que hay que dejar de hablar", "Que los errores son los mejores maestros del camino", "Que no se debe estudiar más", "Que es mejor hablar inglés"], "answer": 1, "explanation": "Mistakes are the best teachers on the path."},
                {"question": "¿Cuál es el sueño de futuro de Sakib?", "options": ["Olvidar el español", "Perfeccionar su fluidez hacia A2 y recorrer Andalucía e Hispanoamérica", "Vivir en un sótano", "Comprar una fábrica"], "answer": 1, "explanation": "Perfect fluency toward A2 and travel through Andalusia and Spanish America."}
            ]
        },
        "exercises": [
            {
                "id": "d58-ex1",
                "type": "fill-in",
                "prompt": "Complete with past of birth: Yo ______ (was born) en Bangladés.",
                "options": ["nací", "nació", "naciste", "nacemos"],
                "correct": 0,
                "explanation": "Yo form of nacer in preterite is 'nací'."
            },
            {
                "id": "d58-ex2",
                "type": "multiple-choice",
                "prompt": "Which connector expresses 'however / nevertheless' in a formal essay?",
                "options": ["Sin embargo", "También", "O sea", "Vale"],
                "correct": 0,
                "explanation": "'Sin embargo' expresses formal contrast in writing."
            },
            {
                "id": "d58-ex3",
                "type": "fill-in",
                "prompt": "Complete: El español ya es parte inseparable ______ (of) mi identidad.",
                "options": ["de", "por", "para", "en"],
                "correct": 0,
                "explanation": "'Parte inseparable de' takes the preposition 'de'."
            },
            {
                "id": "d58-ex4",
                "type": "translation",
                "prompt": "Translate: 'Learning Spanish has transformed my life.'",
                "options": ["Aprender español ha transformado mi vida.", "Aprender español tiene transformar mi vida.", "Aprender español está transformando mi vida.", "Aprender español fue transformar mi vida."],
                "correct": 0,
                "explanation": "'Aprender español ha transformado mi vida' expresses a lasting life milestone."
            }
        ],
        "speakingChallenge": [
            {"prompt": "Deliver your 1-minute personal elevator pitch in Spanish (name, origin, current city, profession/studies).", "hint": "Hola, me llamo Sakib Ahmed, soy de... vivo en... y estudio...", "sampleAnswer": "Hola a todos, me llamo Sakib Ahmed. Nací en Bangladés y ahora vivo en Madrid. Soy desarrollador de software y estudiante apasionado de español."},
            {"prompt": "Say what your parents taught you with pride.", "hint": "Mis padres me enseñaron...", "sampleAnswer": "Mis padres me enseñaron el valor del trabajo honesto, la educación constante y la generosidad con los demás."},
            {"prompt": "Express your vision for the future in Spanish.", "hint": "En el futuro voy a...", "sampleAnswer": "En el futuro voy a continuar aprendiendo español hacia el nivel A2 y voy a viajar por toda España e Hispanoamérica."}
        ],
        "dailyRevision": {
            "quickQuestions": [
                "What are the 4 pillars of a personal autobiographical essay?",
                "How do you express 'I was born' in Spanish? (Nací)"
            ],
            "grammarRecall": "Writing synthesis: Combining present, preterite, near future, connectors, and emotional reflections into a cohesive autobiographical essay.",
            "vocabRecall": ["La biografía", "El diario personal", "Los orígenes", "La superación personal", "El sueño", "Lograr una meta", "La transformación", "Agradecido"]
        },
        "checklist": [
            "Wrote a complete 4-pillar autobiographical essay in Spanish",
            "Synthesized present routines, preterite journeys, and future aspirations",
            "Applied connectors (sin embargo, además, por lo tanto) with editorial elegance",
            "Answered 4 reading comprehension questions on the model biography",
            "Completed all 4 creative writing exercises",
            "Delivered personal elevator pitch aloud with confidence"
        ]
    },
    {
        "day": 59,
        "stage": 6,
        "title": "Complete A1 Grammar & Vocabulary Grand Revision",
        "subtitle": "The Master Review: 600 Words, Core Conjugations, Traps, and Key Patterns",
        "goals": [
            "Conduct the Grand Revision across all 600 vocabulary words and core grammar pillars",
            "Review the 3 present regular conjugations (-AR, -ER, -IR) and the Preterite Simple Past",
            "Review the Essential 5 Irregulars: Ser, Estar, Tener, Hacer, Ir",
            "Test yourself across all question types to prepare for tomorrow's Final A1 Examination"
        ],
        "bengaliNote": "Tomorrow is Day 60: the Grand Milestone and Final A1 Examination! Today is your Grand Dress Rehearsal. We will review every pillar: Ser vs. Estar, Gustar, Reflexives, Por vs. Para, Preterite, and Vocabulary. Take a deep breath: your mind is ready, your foundation is solid, and you are prepared for victory!",
        "vocabulary": [
            {"word": "El repaso general / La revisión", "translation": "General review / Revision", "pos": "noun", "gender": "masculine / feminine", "example": "Hacemos un repaso general de todo el curso.", "exampleTranslation": "We do a general review of the entire course."},
            {"word": "El pilar / La base sólida", "translation": "The pillar / The solid foundation", "pos": "noun", "gender": "masculine / feminine", "example": "Tienes una base sólida de A1.", "exampleTranslation": "You have a solid A1 foundation."},
            {"word": "La conjugación verbal", "translation": "Verb conjugation", "pos": "noun", "gender": "feminine", "example": "Dominas todas las conjugaciones de A1.", "exampleTranslation": "You master all A1 conjugations."},
            {"word": "El vocabulario clave", "translation": "Key vocabulary", "pos": "noun", "gender": "masculine", "example": "Conoces más de seiscientas palabras útiles.", "exampleTranslation": "You know over 600 useful words."},
            {"word": "La comprensión auditiva", "translation": "Listening comprehension", "pos": "noun", "gender": "feminine", "example": "Tu comprensión auditiva es fantástica.", "exampleTranslation": "Your listening comprehension is fantastic."},
            {"word": "La expresión oral y escrita", "translation": "Oral and written expression", "pos": "noun", "gender": "feminine", "example": "Practicamos la expresión oral.", "exampleTranslation": "We practice oral expression."},
            {"word": "La preparación / Estar preparado(a)", "translation": "Preparation / To be prepared", "pos": "noun / phrase", "gender": "feminine / variable", "example": "Estás totalmente preparado para el examen.", "exampleTranslation": "You are totally prepared for the exam."},
            {"word": "La seguridad / La confianza", "translation": "Certainty, safety / Confidence", "pos": "noun", "gender": "feminine", "example": "Hablas con seguridad y confianza.", "exampleTranslation": "You speak with certainty and confidence."},
            {"word": "La culminación", "translation": "The culmination / crowning achievement", "pos": "noun", "gender": "feminine", "example": "Mañana es la culminación del desafío.", "exampleTranslation": "Tomorrow is the culmination of the challenge."},
            {"word": "¡Ánimo! / ¡A por todas!", "translation": "Cheer up! / Go for it all! (encouragement)", "pos": "interjection", "gender": None, "example": "¡Ánimo, Sakib, lo vas a hacer genial!", "exampleTranslation": "Cheer up, Sakib, you're going to do great!"}
        ],
        "sentences": [
            {"spanish": "Hemos repasado los artículos, los pronombres y la diferencia entre ser y estar.", "english": "We have reviewed articles, pronouns, and the difference between ser and estar."},
            {"spanish": "Dominas los verbos regulares en presente y en pretérito indefinido.", "english": "You master regular verbs in present and simple past preterite."},
            {"spanish": "Sabes usar los verbos con cambio de raíz como querer, poder, pedir y jugar.", "english": "You know how to use stem-changing verbs like querer, poder, pedir, and jugar."},
            {"spanish": "Diferencias perfectamente por y para según la causa, el propósito o el destino.", "english": "You differentiate por and para perfectly according to cause, purpose, or destination."},
            {"spanish": "Tu vocabulario abarca la familia, la comida, los viajes, la salud y el trabajo.", "english": "Your vocabulary covers family, food, travel, health, and work."},
            {"spanish": "Mañana es el gran día: el examen final de consolidación del nivel A1.", "english": "Tomorrow is the big day: the final consolidation exam of level A1."}
        ],
        "grammar": {
            "title": "The Grand A1 Grammar Synthesis: The 8 Golden Pillars",
            "explanation": "Here is the master summary of the 8 fundamental grammatical systems of CEFR Level A1:",
            "rules": [
                "Pillar 1: Nouns & Articles: el/la/los/las vs un/una/unos/unas. Exceptions: *el problema, el día, el mapa, la mano*. Contractions: *al* (a+el), *del* (de+el).",
                "Pillar 2: SER vs. ESTAR: SER (DOCTOR: Description, Occupation, Characteristic, Time, Origin, Relationship). ESTAR (PLACE: Position, Location, Action, Condition, Emotion).",
                "Pillar 3: Present Tense Regulars: -AR (-o, -as, -a, -amos, -áis, -an). -ER (-o, -es, -e, -emos, -éis, -en). -IR (-o, -es, -e, -imos, -ís, -en).",
                "Pillar 4: The Core Irregulars: Ser (soy, eres, es...), Estar (estoy, estás...), Tener (tengo, tienes...), Hacer (hago, haces...), Ir (voy, vas, va...).",
                "Pillar 5: Stem-Changers (Boot Verbs): E->IE (querer, entender); O->UE (poder, dormir); E->I (pedir, servir); U->UE (jugar). Nosotros/vosotros stay regular!",
                "Pillar 6: GUSTAR & DOLER: me, te, le, nos, os, les + GUSTA/DUELE (singular/verbs) or GUSTAN/DUELEN (plural nouns).",
                "Pillar 7: POR vs. PARA: PARA = forward arrow (purpose, recipient, destination, deadline). POR = motive, through, duration, exchange.",
                "Pillar 8: The Preterite Past: -AR (-é, -aste, -ó, -amos, -asteis, -aron). -ER/-IR (-í, -iste, -ió, -imos, -isteis, -ieron). Ir/Ser = fui, fuiste, fue... Estar = estuve, estuviste, estuvo..."
            ],
            "structures": [
                "The 8 Golden Pillars of A1: Nouns/Articles | Ser vs Estar | Present Regulars | Core Irregulars | Stem-Changers | Gustar/Doler | Por vs Para | Preterite Past"
            ],
            "examples": [
                {"spanish": "Soy de Bangladés y estoy en Madrid. (Ser vs Estar)", "english": "I am from Bangladesh and I am in Madrid."},
                {"spanish": "Me gusta la paella y me gustan las tapas. (Gustar)", "english": "I like paella and I like tapas."},
                {"spanish": "Estudio para superarme y viajo por placer. (Por vs Para)", "english": "I study in order to improve myself and I travel for pleasure."},
                {"spanish": "Ayer hablé, comí y fui al cine. (Preterite past)", "english": "Yesterday I spoke, ate, and went to the cinema."}
            ],
            "commonMistakes": [
                {"wrong": "Cramming in panic the night before an exam", "right": "Rest well, trust your 59 days of daily consistency", "explanation": "Consistency beats cramming every single time."}
            ],
            "proTip": "Look back at Day 1: you didn't even know that the 'H' in *¡Hola!* was silent. Today, you possess the complete theoretical and practical linguistic architecture of the Spanish language at A1. Be proud of yourself!"
        },
        "conversation": {
            "title": "The Final Pre-Exam Strategy Session",
            "context": "Sakib and Professor Carmen do a rapid-fire quiz check the day before the final exam.",
            "dialogue": [
                {"speaker": "Profª Carmen", "role": "Teacher", "spanish": "Sakib, hagamos una ronda rápida de preguntas relámpago. ¿Preparado?", "english": "Sakib, let's do a quick round of lightning questions. Ready?"},
                {"speaker": "Sakib", "role": "Student", "spanish": "¡Listísimo, profesora! Dispare.", "english": "Totally ready, teacher! Fire away."},
                {"speaker": "Profª Carmen", "role": "Teacher", "spanish": "Primera: ¿'El problema' o 'la problema'?", "english": "First: 'El problema' or 'la problema'?"},
                {"speaker": "Sakib", "role": "Student", "spanish": "¡El problema, siempre masculino por su origen griego!", "english": "El problema, always masculine due to its Greek origin!"},
                {"speaker": "Profª Carmen", "role": "Teacher", "spanish": "Segunda: ¿'Soy en el banco' o 'estoy en el banco'?", "english": "Second: 'Soy en el banco' or 'estoy en el banco'?"},
                {"speaker": "Sakib", "role": "Student", "spanish": "¡Estoy en el banco! La ubicación geográfica siempre lleva estar.", "english": "Estoy en el banco! Geographic location always takes estar."},
                {"speaker": "Profª Carmen", "role": "Teacher", "spanish": "Tercera: ¿Pretérito de 'yo fui a Toledo': es el verbo ser o el verbo ir?", "english": "Third: Preterite of 'yo fui a Toledo': is it the verb ser or the verb ir?"},
                {"speaker": "Sakib", "role": "Student", "spanish": "Es el verbo IR, porque indica movimiento hacia un destino con la preposición 'a'.", "english": "It is the verb IR, because it indicates movement toward a destination with preposition 'a'."},
                {"speaker": "Profª Carmen", "role": "Teacher", "spanish": "¡Excelente! Tres de tres. Tu mente está afilada como una navaja. Descansa bien esta noche, duerme tus ocho horas y mañana celebraremos tu graduación de A1.", "english": "Excellent! Three out of three. Your mind is sharp as a razor. Rest well tonight, sleep your eight hours, and tomorrow we will celebrate your A1 graduation."},
                {"speaker": "Sakib", "role": "Student", "spanish": "¡Muchas gracias, Carmen! Mañana voy a por todas.", "english": "Thank you very much, Carmen! Tomorrow I'm going for it all."}
            ],
            "keyPhrases": [
                {"phrase": "Preguntas relámpago", "explanation": "'Lightning / rapid-fire questions'."},
                {"phrase": "¡Dispare!", "explanation": "Colloquial idiom: 'Fire away! / Shoot!' (ready for questions)."},
                {"phrase": "¡Voy a por todas!", "explanation": "Classic Spain rallying cry: 'I'm going all out / going for gold!'"}
            ]
        },
        "reading": {
            "title": "La víspera de la culminación: Reflexión de un estudiante perseverante",
            "passage": "La víspera de un examen importante no es un momento para la angustia, sino para la serenidad. Cincuenta y nueve días de estudio ininterrumpido representan un testimonio incuestionable de disciplina, voluntad y pasión. Sakib cierra su libro de gramática sobre la mesa de su habitación en Madrid. Mira las notas acumuladas: las listas de vocabulario organizadas por temas, los esquemas de verbos con cambio de raíz, los diálogos de restaurantes y mercados, y las redacciones personales escritas con su propio puño y letra. Recuerda el primer día, cuando las palabras parecían un rompecabezas indescifrable. Hoy, esas mismas palabras fluyen de sus labios con soltura, emoción y belleza. Sabe que el examen de mañana no es un obstáculo que temer, sino una celebración festiva de todo lo que ha logrado. Con la mente en paz y el corazón agradecido, Sakib se prepara para coronar su sueño.",
            "translation": "The eve of an important exam is not a moment for anguish, but for serenity. Fifty-nine days of uninterrupted study represent an unquestionable testimony of discipline, will, and passion. Sakib closes his grammar book on his room's table in Madrid. He looks at the accumulated notes: vocabulary lists organized by topic, diagrams of stem-changing verbs, dialogues of restaurants and markets, and personal essays written in his own handwriting. He remembers the first day, when the words seemed like an indecipherable puzzle. Today, those same words flow from his lips with fluency, emotion, and beauty. He knows that tomorrow's exam is not an obstacle to fear, but a festive celebration of everything he has achieved. With mind at peace and heart grateful, Sakib prepares to crown his dream.",
            "questions": [
                {"question": "¿Qué representa la víspera del examen para Sakib?", "options": ["Un momento de terror y pánico", "Un momento de serenidad y celebración de su disciplina", "Ganas de rendirse", "Olvido total"], "answer": 1, "explanation": "A moment of serenity and celebration ('un momento para la serenidad')."},
                {"question": "¿Cómo parecían las palabras en español el primer día?", "options": ["Pan comido", "Un rompecabezas indescifrable", "Muy fáciles", "Aburridas"], "answer": 1, "explanation": "An indecipherable puzzle ('un rompecabezas indescifrable')."},
                {"question": "¿Qué es el examen de mañana según el texto?", "options": ["Un castigo", "Una celebración festiva de todo lo que ha logrado", "Una pérdida de tiempo", "Algo sin importancia"], "answer": 1, "explanation": "A festive celebration of everything achieved ('una celebración festiva...')."}
            ]
        },
        "exercises": [
            {
                "id": "d59-ex1",
                "type": "multiple-choice",
                "prompt": "Which of the following is correct for 'The problem is difficult'?",
                "options": ["El problema es difícil", "La problema es difícil", "El problema está difícil", "La problema está difícil"],
                "correct": 0,
                "explanation": "'Problema' is masculine: 'El problema es difícil'."
            },
            {
                "id": "d59-ex2",
                "type": "fill-in",
                "prompt": "Choose POR or PARA: Estudio todos los días ______ (in order to) aprobar con éxito.",
                "options": ["para", "por", "de", "con"],
                "correct": 0,
                "explanation": "'In order to' is strictly 'para + infinitive'."
            },
            {
                "id": "d59-ex3",
                "type": "fill-in",
                "prompt": "Choose Ser or Estar: Carlos ______ (is) en la biblioteca estudiando.",
                "options": ["está", "es", "tiene", "hace"],
                "correct": 0,
                "explanation": "Location takes ESTAR: 'está en la biblioteca'."
            },
            {
                "id": "d59-ex4",
                "type": "translation",
                "prompt": "Translate: 'Yesterday I traveled to Toledo and ate paella.'",
                "options": ["Ayer viajé a Toledo y comí paella.", "Ayer viajo a Toledo y como paella.", "Ayer viajó a Toledo y comió paella.", "Ayer viajar a Toledo y comer paella."],
                "correct": 0,
                "explanation": "'Ayer viajé a Toledo y comí paella' coordinates 1st person preterite for -AR and -ER."
            }
        ],
        "speakingChallenge": [
            {"prompt": "Conjugate SER, ESTAR, TENER, HACER, and IR in the 'yo' present form.", "hint": "Soy, estoy, tengo, hago, voy.", "sampleAnswer": "Yo soy, yo estoy, yo tengo, yo hago y yo voy."},
            {"prompt": "Conjugate the preterite of IR/SER for all 6 persons.", "hint": "Fui, fuiste, fue, fuimos, fuisteis, fueron.", "sampleAnswer": "Fui, fuiste, fue, fuimos, fuisteis, fueron."},
            {"prompt": "Say: 'Tomorrow I am going all out to conquer the Final A1 Examination!'", "hint": "¡Mañana voy a por todas...!", "sampleAnswer": "¡Mañana voy a por todas en el Examen Final de A1! ¡Estoy totalmente preparado y seguro!"}
        ],
        "dailyRevision": {
            "quickQuestions": [
                "Name the 8 Golden Pillars of A1 Spanish grammar.",
                "What is the Spain rallying cry for 'going all out'? (¡A por todas!)"
            ],
            "grammarRecall": "The complete A1 Grammar Architecture: Nouns/Articles, Ser vs Estar, Present Regulars, Core Irregulars, Stem Changers, Gustar/Doler, Por vs Para, Preterite Past.",
            "vocabRecall": ["El repaso general", "El pilar", "La base sólida", "La preparación", "La confianza", "¡Ánimo!", "¡A por todas!"]
        },
        "checklist": [
            "Conducted the Grand Revision across all 8 grammatical pillars",
            "Synthesized the 600-word vocabulary reservoir",
            "Reviewed the Core 5 irregulars in both present and preterite",
            "Answered all 4 Grand Revision pre-exam questions",
            "Passed all 4 grammar check exercises",
            "CONFIRMED READINESS FOR TOMORROW'S FINAL A1 EXAMINATION! 🎉"
        ]
    }
]

if __name__ == "__main__":
    print(f"Loaded {len(stage6_part2)} days for Stage 6 (Days 56-59).")
