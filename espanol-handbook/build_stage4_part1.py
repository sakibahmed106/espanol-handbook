"""
Build Stage 4: Days 31 to 35 (Practical Communication)
"""
import json

stage4_days = [
    {
        "day": 31,
        "stage": 4,
        "title": "At the Restaurant & Ordering Food",
        "subtitle": "Navigating the Menú del Día, ordering courses, asking for the bill, and tipping",
        "goals": [
            "Order confidently in a Spanish restaurant from start to finish",
            "Understand Spain's famous 'Menú del día' (primer plato, segundo plato, postre, pan y bebida)",
            "Ask for dietary preferences and ingredients (vegetariano, sin gluten)",
            "Ask for the bill politely: 'La cuenta, por favor' and understand tipping customs in Spain"
        ],
        "bengaliNote": "Dining in Spain is a celebrated cultural ritual! The weekday lunch bargain is the **Menú del día** (usually €10–€15 including 2 courses, dessert, bread, and wine/water!). To ask for the bill, you don't say 'give me the bill'; you simply make eye contact with the waiter and say: *«La cuenta, por favor»* (বিলটা দিন, দয়া করে).",
        "vocabulary": [
            {"word": "El restaurante / El camarero", "translation": "The restaurant / The waiter", "pos": "noun", "gender": "masculine", "example": "El camarero nos trae la carta.", "exampleTranslation": "The waiter brings us the menu."},
            {"word": "La carta / El menú del día", "translation": "The full menu / The daily set menu", "pos": "noun", "gender": "feminine / masculine", "example": "¿Tienen menú del día?", "exampleTranslation": "Do you have a daily set menu?"},
            {"word": "De primer plato / De primero", "translation": "For the first course", "pos": "phrase", "gender": "masculine", "example": "De primero quiero sopa de verduras.", "exampleTranslation": "For the first course I want vegetable soup."},
            {"word": "De segundo plato / De segundo", "translation": "For the second (main) course", "pos": "phrase", "gender": "masculine", "example": "De segundo prefiero merluza a la plancha.", "exampleTranslation": "For main course I prefer grilled hake."},
            {"word": "El postre", "translation": "The dessert", "pos": "noun", "gender": "masculine", "example": "¿Qué hay de postre?", "exampleTranslation": "What is there for dessert?"},
            {"word": "La cuenta, por favor", "translation": "The bill/check, please", "pos": "phrase", "gender": "feminine", "example": "Camarero, ¿nos trae la cuenta, por favor?", "exampleTranslation": "Waiter, can you bring us the bill, please?"},
            {"word": "La propina", "translation": "The tip (gratuity)", "pos": "noun", "gender": "feminine", "example": "Dejamos una pequeña propina en la mesa.", "exampleTranslation": "We leave a small tip on the table."},
            {"word": "¿Qué lleva este plato?", "translation": "What is in this dish? (ingredients)", "pos": "phrase", "gender": None, "example": "¿Qué lleva esta salsa?", "exampleTranslation": "What does this sauce contain?"},
            {"word": "Soy vegetariano(a)", "translation": "I am vegetarian", "pos": "phrase", "gender": "masculine / feminine", "example": "No como carne, soy vegetariano.", "exampleTranslation": "I don't eat meat, I am vegetarian."},
            {"word": "¡Buen provecho! / ¡Que aproveche!", "translation": "Bon appétit! / Enjoy your meal!", "pos": "interjection", "gender": None, "example": "Aquí tienen su comida, ¡que aproveche!", "exampleTranslation": "Here is your food, enjoy your meal!"}
        ],
        "sentences": [
            {"spanish": "Buenas tardes, ¿tienen una mesa para dos personas?", "english": "Good afternoon, do you have a table for two people?"},
            {"spanish": "¿Nos trae la carta o tienen menú del día?", "english": "Could you bring us the menu or do you have a daily set menu?"},
            {"spanish": "De primero, gazpacho andaluz; y de segundo, pollo asado.", "english": "For first course, Andalusian gazpacho; and for second, roast chicken."},
            {"spanish": "¿Está incluido el pan y la bebida en el menú?", "english": "Are bread and drink included in the set menu?"},
            {"spanish": "Todo estaba riquísimo, felicitaciones al cocinero.", "english": "Everything was delicious, compliments to the chef."},
            {"spanish": "La cuenta, por favor. ¿Se puede pagar con tarjeta?", "english": "The bill, please. Can we pay with card?"}
        ],
        "grammar": {
            "title": "Dining Formulas: 'Para mí', 'De primero/segundo' & Tipping Rules in Spain",
            "explanation": "Ordering food in Spain uses smooth, direct, polite formulas rather than stiff English-style phrasing.",
            "rules": [
                "Ordering Formula: Use **Para mí...** (For me...) or **Quería...** (I would like...). Native speakers rarely say *Yo demando* or *Yo ordeno* (ordeno means 'I command'!).",
                "Course Sequencing: *De primero...* (For starters), *De segundo...* (For mains), *De postre...* (For dessert).",
                "Ingredient Inquiries: Ask *¿Lleva carne / gluten / marisco?* (Does it contain meat / gluten / seafood?).",
                "Tipping in Spain (La Propina): Unlike the US, tips are NOT obligatory in Spain. Service is included in the bill. Spaniards typically leave small change (e.g., 1 or 2 euros on a 30-euro bill) only if the service was exceptional."
            ],
            "structures": [
                "Ordering starter: De primero, para mí [plato]",
                "Ordering main: De segundo, voy a tomar [plato]",
                "Requesting bill: ¿Nos trae la cuenta, por favor? / La cuenta cuando pueda"
            ],
            "examples": [
                {"spanish": "Para mí, una ensalada mixta de primero.", "english": "For me, a mixed salad for the first course."},
                {"spanish": "¿Qué tienen de postre hoy?", "english": "What do you have for dessert today?"},
                {"spanish": "¿El agua está incluida en el menú?", "english": "Is water included in the set menu?"},
                {"spanish": "¡Que aproveche!", "english": "Enjoy your meal!"}
            ],
            "commonMistakes": [
                {"wrong": "Yo ordeno la sopa (using English 'order')", "right": "Para mí la sopa / Quiero la sopa", "explanation": "'Ordenar' in Spanish means to put things in tidy order or to issue military commands. Use 'Para mí' or 'Voy a tomar'."},
                {"wrong": "Dame la cuenta (too blunt)", "right": "La cuenta, por favor / ¿Me trae la cuenta?", "explanation": "Add 'por favor' or phrasing with 'trae'."}
            ],
            "proTip": "When you are finished and ready to leave, catch the waiter's eye, raise your hand slightly and say: **«La cuenta cuando pueda, por favor»** (The bill whenever you can, please). It is the hallmark of a polite, seasoned Spanish speaker."
        },
        "conversation": {
            "title": "Enjoying the Menú del Día in Malasaña",
            "context": "Sakib and his classmate Carlos have lunch at a traditional Madrid bistro.",
            "dialogue": [
                {"speaker": "Camarero", "role": "Waiter", "spanish": "¡Buenas tardes! ¿Mesa para dos?", "english": "Good afternoon! Table for two?"},
                {"speaker": "Carlos", "role": "Friend", "spanish": "Sí, por favor. ¿Tienen menú del día?", "english": "Yes, please. Do you have a daily set menu?"},
                {"speaker": "Camarero", "role": "Waiter", "spanish": "Sí, doce euros cincuenta con primero, segundo, pan, bebida y postre. Aquí tienen la pizarra con los platos.", "english": "Yes, twelve fifty with first, second, bread, drink, and dessert. Here is the blackboard with the dishes."},
                {"speaker": "Sakib", "role": "Student", "spanish": "De primero, para mí la ensalada de tomate y queso de cabra. ¿Lleva carne?", "english": "For first course, for me the tomato and goat cheese salad. Does it have meat?"},
                {"speaker": "Camarero", "role": "Waiter", "spanish": "No, nada de carne. Es totalmente vegetariana.", "english": "No, no meat at all. It is totally vegetarian."},
                {"speaker": "Sakib", "role": "Student", "spanish": "Perfecto. Y de segundo, el salmón a la plancha con patatas.", "english": "Perfect. And for main, the grilled salmon with potatoes."},
                {"speaker": "Carlos", "role": "Friend", "spanish": "Para mí, de primero lentejas con chorizo y de segundo ternera asada. Y agua para los dos.", "english": "For me, first course lentils with chorizo, and second roast veal. And water for both."},
                {"speaker": "Camarero", "role": "Waiter", "spanish": "Marchando. ¡Que aproveche, caballeros!", "english": "Coming right up. Enjoy your meal, gentlemen!"}
            ],
            "keyPhrases": [
                {"phrase": "A la plancha", "explanation": "'Grilled on a flat metal hot plate' (very healthy Spanish cooking style)."},
                {"phrase": "Agua para los dos", "explanation": "'Water for both of us'."},
                {"phrase": "Queso de cabra", "explanation": "'Goat cheese'."}
            ]
        },
        "reading": {
            "title": "La historia del Menú del Día español",
            "passage": "El «Menú del Día» es una de las instituciones gastronómicas más queridas de España. Nació en los años sesenta por ley para garantizar que los trabajadores y los primeros turistas pudieran comer una comida completa, nutritiva y asequible fuera de casa. Por un precio fijo que suele rondar entre los diez y los quince euros, el comensal puede elegir entre tres o cuatro primeros platos, tres o cuatro segundos, pan recién horneado, una bebida (agua, refresco o vino de la casa) y un postre casero como flan, arroz con leche o fruta de temporada. Hoy en día, millones de españoles almuerzan con el menú del día de lunes a viernes.",
            "translation": "The 'Menú del Día' is one of the most beloved gastronomic institutions of Spain. It was born in the sixties by law to guarantee that workers and early tourists could eat a complete, nutritious, and affordable meal away from home. For a fixed price that usually hovers between ten and fifteen euros, the diner can choose between three or four starters, three or four mains, freshly baked bread, a beverage (water, soda, or house wine), and a homemade dessert such as flan, rice pudding, or seasonal fruit. Nowadays, millions of Spaniards have lunch with the daily set menu from Monday to Friday.",
            "questions": [
                {"question": "¿Cuándo nació el Menú del Día en España?", "options": ["En la Edad Media", "En los años sesenta", "El año pasado", "En el siglo XIX"], "answer": 1, "explanation": "In the 1960s ('en los años sesenta')."},
                {"question": "¿Qué incluye habitualmente el Menú del Día?", "options": ["Solo café", "Primero, segundo, pan, bebida y postre por precio fijo", "Solo una ensalada pequeña", "Solo un plato"], "answer": 1, "explanation": "First, second, bread, drink, and dessert for a fixed price."},
                {"question": "¿Cuáles son postres caseros tradicionales mencionados?", "options": ["Pizza y hamburguesa", "Flan, arroz con leche o fruta de temporada", "Pastel de chocolate americano", "Tacos"], "answer": 1, "explanation": "Flan, rice pudding, or seasonal fruit."}
            ]
        },
        "exercises": [
            {
                "id": "d31-ex1",
                "type": "multiple-choice",
                "prompt": "How do you naturally order the first course in a Spanish restaurant?",
                "options": ["De primero, para mí el gazpacho", "Yo ordeno primeramente el gazpacho", "Mi primera comida es gazpacho", "Dame primer plato gazpacho"],
                "correct": 0,
                "explanation": "'De primero, para mí...' is the natural polite formula."
            },
            {
                "id": "d31-ex2",
                "type": "fill-in",
                "prompt": "Complete: Camarero, ¿nos trae la ______ (bill), por favor?",
                "options": ["cuenta", "carta", "comida", "propina"],
                "correct": 0,
                "explanation": "'La cuenta' means the restaurant bill."
            },
            {
                "id": "d31-ex3",
                "type": "multiple-choice",
                "prompt": "What does '¡Que aproveche!' mean?",
                "options": ["Hurry up!", "Enjoy your meal / Bon appétit!", "Pay quickly!", "Goodbye forever!"],
                "correct": 1,
                "explanation": "'¡Que aproveche!' means 'Enjoy your meal!'."
            },
            {
                "id": "d31-ex4",
                "type": "translation",
                "prompt": "Translate: 'Does this dish have meat? I am vegetarian.'",
                "options": ["¿Lleva carne este plato? Soy vegetariano.", "¿Tiene carne la comida? Estoy vegetariano.", "¿Dónde está la carne? Tengo vegetariano.", "¿Por qué carne? Hago vegetariano."],
                "correct": 0,
                "explanation": "'¿Lleva carne este plato? Soy vegetariano' has proper verbs (llevar + ser)."
            }
        ],
        "speakingChallenge": [
            {"prompt": "Order a 2-course meal with water in Spanish.", "hint": "De primero quiero... y de segundo...", "sampleAnswer": "De primero quiero sopa de verduras y de segundo merluza a la plancha con una botella de agua."},
            {"prompt": "Ask the waiter if dessert is included in the menu.", "hint": "¿El postre está incluido en...", "sampleAnswer": "Disculpe, ¿el postre está incluido en el menú del día?"},
            {"prompt": "Ask for the bill politely when finishing.", "hint": "La cuenta cuando pueda...", "sampleAnswer": "Camarero, la cuenta cuando pueda, por favor. ¿Se puede pagar con tarjeta?"}
        ],
        "dailyRevision": {
            "quickQuestions": [
                "What does 'De segundo' mean when ordering?",
                "Are tips mandatory in Spanish restaurants?"
            ],
            "grammarRecall": "Ordering: Para mí [plato], De primero/segundo, La cuenta por favor. ¿Lleva [ingrediente]?",
            "vocabRecall": ["El restaurante", "El camarero", "El menú del día", "De primero", "De segundo", "El postre", "La cuenta", "¡Que aproveche!"]
        },
        "checklist": [
            "Ordered first and second courses using 'De primero' and 'De segundo'",
            "Asked about ingredients using '¿Qué lleva este plato?'",
            "Asked for the bill politely with 'La cuenta, por favor'",
            "Understood Spanish tipping customs (la propina)",
            "Completed all 4 restaurant exercises",
            "Simulated a complete restaurant ordering dialogue aloud"
        ]
    },
    {
        "day": 32,
        "stage": 4,
        "title": "Travelling, Airport & Transportation",
        "subtitle": "Navigating airports, train stations, buying return tickets, and announcements",
        "goals": [
            "Master airport and train station vocabulary (aeropuerto, estación, andén, billete, retraso)",
            "Buy a round-trip ticket (*un billete de ida y vuelta*)",
            "Ask about departure and arrival times (*la salida* and *la llegada*)",
            "Understand loudspeaker transit announcements in Spanish"
        ],
        "bengaliNote": "Spain has the second largest high-speed train network (AVE) in the world! Notice the difference between a one-way ticket (*billete de ida*) and a round-trip ticket (*billete de ida y vuelta* = যাওয়া এবং আসার টিকিট). Station platforms are called *andenes*.",
        "vocabulary": [
            {"word": "El aeropuerto / La estación de tren", "translation": "The airport / The train station", "pos": "noun", "gender": "masculine / feminine", "example": "El aeropuerto de Madrid se llama Barajas.", "exampleTranslation": "Madrid's airport is called Barajas."},
            {"word": "El billete de ida / de ida y vuelta", "translation": "One-way ticket / Round-trip (return) ticket", "pos": "noun", "gender": "masculine", "example": "Un billete de ida y vuelta a Barcelona, por favor.", "exampleTranslation": "A round-trip ticket to Barcelona, please."},
            {"word": "La salida / La llegada", "translation": "Departure / Arrival", "pos": "noun", "gender": "feminine", "example": "La puerta de salida número doce.", "exampleTranslation": "Departure gate number twelve."},
            {"word": "El andén / La vía", "translation": "The platform / The track", "pos": "noun", "gender": "masculine / feminine", "example": "El tren sale del andén número cuatro.", "exampleTranslation": "The train leaves from platform number four."},
            {"word": "El vuelo / El avión", "translation": "The flight / The plane", "pos": "noun", "gender": "masculine", "example": "Mi vuelo sale a las diez de la mañana.", "exampleTranslation": "My flight leaves at ten in the morning."},
            {"word": "El tren de alta velocidad (AVE)", "translation": "High-speed train", "pos": "noun", "gender": "masculine", "example": "Viajo en AVE porque es comodísimo.", "exampleTranslation": "I travel by AVE because it is super comfortable."},
            {"word": "El retraso / Con retraso", "translation": "The delay / Delayed", "pos": "noun / phrase", "gender": "masculine", "example": "El vuelo lleva veinte minutos de retraso.", "exampleTranslation": "The flight has a twenty-minute delay."},
            {"word": "El equipaje / La maleta", "translation": "Luggage / Suitcase", "pos": "noun", "gender": "masculine / feminine", "example": "Llevo solo una maleta de mano.", "exampleTranslation": "I carry only one hand suitcase."},
            {"word": "El pasaporte / El DNI", "translation": "Passport / National ID card", "pos": "noun", "gender": "masculine", "example": "Muestre su pasaporte en el control.", "exampleTranslation": "Show your passport at control."},
            {"word": "Embarcar / La puerta de embarque", "translation": "To board / Boarding gate", "pos": "verb / noun", "gender": "feminine", "example": "Empezamos a embarcar en diez minutos.", "exampleTranslation": "We begin to board in ten minutes."}
        ],
        "sentences": [
            {"spanish": "Quería un billete de ida y vuelta para Sevilla en el AVE.", "english": "I would like a round-trip ticket to Seville on the high-speed train."},
            {"spanish": "¿De qué andén sale el tren con destino a Valencia?", "english": "From which platform does the train bound for Valencia depart?"},
            {"spanish": "El vuelo IB-3840 tiene una hora de retraso.", "english": "Flight IB-3840 has a one-hour delay."},
            {"spanish": "¿Dónde se recogen las maletas facturadas?", "english": "Where do you pick up checked baggage?"},
            {"spanish": "Tenga su pasaporte y tarjeta de embarque preparados.", "english": "Have your passport and boarding pass ready."},
            {"spanish": "El tren llega a su destino en dos horas y media.", "english": "The train arrives at its destination in two and a half hours."}
        ],
        "grammar": {
            "title": "Transit Formulas: 'Salir de', 'Llegar a', 'Con destino a' & Time Delays",
            "explanation": "Navigating transit requires precise prepositions of origin (*de*) and destination (*a*).",
            "rules": [
                "Origin & Destination: *Salir DE + [Origen]* (to leave from...) vs. *Llegar A + [Destino]* (to arrive at...). E.g. *El tren sale DE Madrid y llega A Barcelona*.",
                "Target Destination: *Con destino a + [Ciudad]* (bound for [City]): *El tren con destino a Málaga*.",
                "Expressing Delays: Use the verb LLEVAR: *Lleva veinte minutos de retraso* (It has a 20-minute delay) or *Llega con retraso* (It arrives with delay).",
                "Ticket Types: *Billete de ida* (single/one-way) vs. *Billete de ida y vuelta* (round-trip/return)."
            ],
            "structures": [
                "Ticket Purchase: Quería un billete de ida [y vuelta] para [Ciudad]",
                "Platform Query: ¿De qué andén sale el tren para [Ciudad]?",
                "Departure Time: Sale a las [Hora] / Llega a las [Hora]"
            ],
            "examples": [
                {"spanish": "El tren sale del andén tres. (de + el = del)", "english": "The train departs from platform three."},
                {"spanish": "Llegamos a la estación con tiempo de sobra.", "english": "We arrive at the station with plenty of time."},
                {"spanish": "¿Cuánto cuesta el billete de ida y vuelta?", "english": "How much does the round-trip ticket cost?"},
                {"spanish": "Pasajeros con destino a París, acudan a la puerta B22.", "english": "Passengers bound for Paris, proceed to gate B22."}
            ],
            "commonMistakes": [
                {"wrong": "El tren sale en andén dos", "right": "El tren sale del andén dos", "explanation": "Use 'del andén' (from platform)."},
                {"wrong": "Billete de retorno", "right": "Billete de ida y vuelta", "explanation": "In standard Spanish, return ticket is 'billete de ida y vuelta'."}
            ],
            "proTip": "In Spain's train stations (RENFE), look at the big electronic boards for two key headings: **SALIDAS** (Departures) and **LLEGADAS** (Arrivals). Your platform number (*Vía* or *Andén*) usually appears 15–20 minutes before departure."
        },
        "conversation": {
            "title": "Buying an AVE Train Ticket at Atocha",
            "context": "Sakib purchases a high-speed train ticket at Madrid's Atocha station.",
            "dialogue": [
                {"speaker": "Taquillera", "role": "Ticket agent", "spanish": "¡Buenos días! ¿En qué puedo ayudarle?", "english": "Good morning! How can I help you?"},
                {"speaker": "Sakib", "role": "Traveler", "spanish": "Buenos días. Quería un billete de ida y vuelta para Córdoba en el AVE.", "english": "Good morning. I would like a round-trip ticket for Cordoba on the AVE."},
                {"speaker": "Taquillera", "role": "Ticket agent", "spanish": "¿Para qué fecha y a qué hora prefiere salir?", "english": "For what date and at what time do you prefer to leave?"},
                {"speaker": "Sakib", "role": "Traveler", "spanish": "Para este viernes por la mañana, sobre las nueve. Y la vuelta el domingo por la tarde.", "english": "For this Friday morning, around nine. And the return on Sunday afternoon."},
                {"speaker": "Taquillera", "role": "Ticket agent", "spanish": "Tengo uno que sale el viernes a las nueve y cuarto, y vuelve el domingo a las seis y media. Son setenta y cinco euros en total.", "english": "I have one leaving Friday at nine fifteen, and returning Sunday at six thirty. It is seventy-five euros in total."},
                {"speaker": "Sakib", "role": "Traveler", "spanish": "Me parece perfecto. Pago con tarjeta.", "english": "Sounds perfect to me. I'll pay with card."},
                {"speaker": "Taquillera", "role": "Ticket agent", "spanish": "Aquí tiene sus billetes. Recuerde que el control de equipajes cierra dos minutos antes de la salida.", "english": "Here are your tickets. Remember that the baggage check closes two minutes before departure."},
                {"speaker": "Sakib", "role": "Traveler", "spanish": "Muchas gracias por su información. ¡Buen día!", "english": "Thank you very much for your information. Have a good day!"}
            ],
            "keyPhrases": [
                {"phrase": "Sobre las nueve", "explanation": "'Around nine o'clock' (approximate time)."},
                {"phrase": "La vuelta", "explanation": "'The return journey'."},
                {"phrase": "Con tiempo de sobra", "explanation": "'With time to spare'."}
            ]
        },
        "reading": {
            "title": "La joya ferroviaria de España: El tren AVE",
            "passage": "España cuenta con una de las redes de trenes de alta velocidad más modernas y eficientes del planeta: el AVE (Alta Velocidad Española). La palabra «ave» también significa pájaro en español, un símbolo perfecto de rapidez y vuelo rasante. El primer AVE conectó Madrid con Sevilla en el año 1992 para la Exposición Universal. Hoy en día, la red une casi todas las grandes ciudades peninsulares: puedes viajar desde Madrid a Barcelona en solo dos horas y media a trescientos kilómetros por hora, sin las colas ni los retrasos de los aeropuertos. Además, las estaciones históricas como Atocha en Madrid albergan incluso un jardín botánico tropical en su interior.",
            "translation": "Spain boasts one of the most modern and efficient high-speed rail networks on the planet: the AVE (Alta Velocidad Española). The word 'ave' also means bird in Spanish, a perfect symbol of speed and gliding flight. The first AVE connected Madrid with Seville in the year 1992 for the Universal Expo. Nowadays, the network unites almost all large peninsular cities: you can travel from Madrid to Barcelona in only two and a half hours at three hundred kilometers per hour, without the queues or delays of airports. Furthermore, historic stations like Atocha in Madrid even house a tropical botanical garden inside.",
            "questions": [
                {"question": "¿Qué significa la palabra 'ave' además de las siglas del tren?", "options": ["Un tipo de flor", "Pájaro (bird)", "Un pez", "Un volcán"], "answer": 1, "explanation": "'Ave' means bird ('significa pájaro')."},
                {"question": "¿Qué dos ciudades conectó el primer tren AVE en 1992?", "options": ["Madrid y Barcelona", "Madrid y Sevilla", "Valencia y Málaga", "Bilbao y Madrid"], "answer": 1, "explanation": "Madrid and Seville ('conectó Madrid con Sevilla')."},
                {"question": "¿Qué alberga la estación de Atocha en su interior?", "options": ["Una pista de hielo", "Un jardín botánico tropical", "Un zoológico", "Una playa artificial"], "answer": 1, "explanation": "A tropical botanical garden ('un jardín botánico tropical')."}
            ]
        },
        "exercises": [
            {
                "id": "d32-ex1",
                "type": "multiple-choice",
                "prompt": "How do you ask for a round-trip train ticket in Spanish?",
                "options": ["Un billete de ida y vuelta", "Un billete de vuelta solo", "Un billete de salir y entrar", "Un billete doble"],
                "correct": 0,
                "explanation": "'Un billete de ida y vuelta' is the standard term."
            },
            {
                "id": "d32-ex2",
                "type": "fill-in",
                "prompt": "Complete: El tren sale ______ (from the) andén número cinco.",
                "options": ["del", "de el", "al", "en el"],
                "correct": 0,
                "explanation": "'de + el' contracts to 'del': 'del andén'."
            },
            {
                "id": "d32-ex3",
                "type": "multiple-choice",
                "prompt": "What does 'El vuelo lleva una hora de retraso' mean?",
                "options": ["The flight takes one hour", "The flight has a one-hour delay", "The flight leaves in one hour", "The flight is canceled"],
                "correct": 1,
                "explanation": "'Llevar retraso' means to be delayed."
            },
            {
                "id": "d32-ex4",
                "type": "translation",
                "prompt": "Translate: 'From which platform does the train depart?'",
                "options": ["¿De qué andén sale el tren?", "¿Dónde andén está el tren?", "¿Cuándo andén va el tren?", "¿Qué andén tiene el tren?"],
                "correct": 0,
                "explanation": "'¿De qué andén sale el tren?' asks for departure platform."
            }
        ],
        "speakingChallenge": [
            {"prompt": "Ask for a round-trip ticket to Barcelona leaving Friday morning.", "hint": "Quería un billete de ida y vuelta para... saliendo el...", "sampleAnswer": "Buenos días, quería un billete de ida y vuelta para Barcelona saliendo el viernes por la mañana."},
            {"prompt": "Ask station staff which platform the train to Valencia leaves from.", "hint": "¿De qué andén sale el tren para...?", "sampleAnswer": "Disculpe, ¿de qué andén sale el tren con destino a Valencia?"},
            {"prompt": "Say that your flight has a 30-minute delay.", "hint": "Mi vuelo lleva...", "sampleAnswer": "Mi vuelo lleva treinta minutos de retraso, pero no pasa nada."}
        ],
        "dailyRevision": {
            "quickQuestions": [
                "What is the difference between 'billete de ida' and 'billete de ida y vuelta'?",
                "What preposition is used for departure origin? (Salir DE)"
            ],
            "grammarRecall": "Transit: Salir de / llegar a. Billete de ida y vuelta. ¿De qué andén sale? Lleva [tiempo] de retraso.",
            "vocabRecall": ["El aeropuerto", "La estación", "El andén", "El billete", "La salida", "La llegada", "El retraso", "El AVE"]
        },
        "checklist": [
            "Learned airport and train station vocabulary",
            "Bought single and return tickets (billete de ida y vuelta)",
            "Understood 'Salir de' vs. 'Llegar a'",
            "Identified platform (andén) and delay (retraso) terminology",
            "Completed all 4 transit exercises",
            "Practiced buying high-speed train tickets aloud"
        ]
    },
    {
        "day": 33,
        "stage": 4,
        "title": "Weather, Climates & the 4 Seasons",
        "subtitle": "Expanding weather vocabulary: storm, fog, degrees, and regional forecasts",
        "goals": [
            "Deepen weather discussions beyond basics: grados, tormenta, niebla, cielo despejado",
            "Talk about temperatures using 'Estamos a [número] grados'",
            "Describe the four seasons and seasonal activities in detail",
            "Understand a Spanish weather forecast report"
        ],
        "bengaliNote": "Bengal has 6 seasons (ঋতু), while Spain has the classic 4 European seasons (primavera, verano, otoño, invierno). When stating the temperature, Spanish speakers say: *«Estamos a 25 grados»* (literally: We are AT 25 degrees) — using ESTAR + A!",
        "vocabulary": [
            {"word": "El grado (centígrado)", "translation": "The degree (Celsius)", "pos": "noun", "gender": "masculine", "example": "Hoy estamos a veintidós grados.", "exampleTranslation": "Today we are at twenty-two degrees."},
            {"word": "El cielo despejado / nublado", "translation": "Clear sky / Overcast (cloudy) sky", "pos": "phrase", "gender": "masculine", "example": "El cielo está totalmente despejado.", "exampleTranslation": "The sky is totally clear."},
            {"word": "La tormenta", "translation": "The storm", "pos": "noun", "gender": "feminine", "example": "Hay tormenta con rayos y truenos.", "exampleTranslation": "There is a storm with lightning and thunder."},
            {"word": "La niebla", "translation": "The fog / mist", "pos": "noun", "gender": "feminine", "example": "Hay mucha niebla en la carretera.", "exampleTranslation": "There is a lot of fog on the road."},
            {"word": "El paraguas", "translation": "The umbrella (ends in -s in both singular and plural)", "pos": "noun", "gender": "masculine", "example": "Lleva un paraguas porque va a llover.", "exampleTranslation": "Take an umbrella because it is going to rain."},
            {"word": "Las gafas de sol", "translation": "Sunglasses", "pos": "noun", "gender": "feminine plural", "example": "Hace mucho sol, me pongo las gafas de sol.", "exampleTranslation": "It is very sunny, I put on my sunglasses."},
            {"word": "Humedad / Seco", "translation": "Humidity / Dry", "pos": "noun / adjective", "gender": "feminine / masculine", "example": "El clima de Madrid es seco, no hay humedad.", "exampleTranslation": "Madrid's climate is dry, there is no humidity."},
            {"word": "El pronóstico del tiempo", "translation": "The weather forecast", "pos": "noun", "gender": "masculine", "example": "Miro el pronóstico en la aplicación del móvil.", "exampleTranslation": "I check the forecast on the mobile app."},
            {"word": "Subir / Bajar (las temperaturas)", "translation": "To rise / To drop (temperatures)", "pos": "verb", "gender": None, "example": "Mañana bajan las temperaturas.", "exampleTranslation": "Tomorrow temperatures will drop."},
            {"word": "Agradable / Caluroso / Frío", "translation": "Pleasant / Hot / Cold", "pos": "adjective", "gender": "mixed", "example": "Hace una temperatura muy agradable.", "exampleTranslation": "It is a very pleasant temperature."}
        ],
        "sentences": [
            {"spanish": "¿A cuántos grados estamos hoy? —Estamos a dieciocho grados.", "english": "What temperature are we at today? —We are at eighteen degrees."},
            {"spanish": "El cielo está despejado y hace un sol magnífico.", "english": "The sky is clear and it is magnificently sunny."},
            {"spanish": "Coge el paraguas porque el pronóstico dice que va a llover.", "english": "Grab the umbrella because the forecast says it is going to rain."},
            {"spanish": "En verano las temperaturas suben hasta los cuarenta grados en Córdoba.", "english": "In summer temperatures rise up to forty degrees in Cordoba."},
            {"spanish": "Hay mucha niebla esta mañana, conduce con precaución.", "english": "There is a lot of fog this morning, drive with caution."},
            {"spanish": "La primavera es mi estación favorita porque los días son más largos.", "english": "Spring is my favorite season because the days are longer."}
        ],
        "grammar": {
            "title": "Temperature Formulas (Estamos a...) & Weather Verbs",
            "explanation": "Describing degrees and advanced weather conditions uses fixed idiomatic structures in Spanish.",
            "rules": [
                "Asking Temperature: *¿A cuántos grados estamos?* (At how many degrees are we?) or *¿Qué temperatura hace?*.",
                "Stating Temperature: Use **Estamos a + [Número] + grados**: *Estamos a veinticinco grados* (We are at 25 degrees). Below zero: *Bajo cero*: *Estamos a tres grados bajo cero* (-3°C).",
                "HAY with Atmospheric Phenomena: Use **Hay** for fog, storms, and clouds: *Hay niebla* (There is fog), *Hay tormenta* (There is a storm), *Hay nubes* (There are clouds).",
                "ESTAR with Sky Condition: *El cielo está despejado* (clear) / *El cielo está nublado* (cloudy).",
                "The Compound Noun 'Paraguas': *Un paraguas* (one umbrella) -> *Dos paraguas* (two umbrellas). It protects *para* + *aguas* (stops waters)!"
            ],
            "structures": [
                "Temperature: Estamos a [Número] grados (bajo cero)",
                "Sky condition: El cielo está despejado / nublado",
                "Atmospheric event: Hay niebla / tormenta / viento"
            ],
            "examples": [
                {"spanish": "Hoy estamos a treinta grados a la sombra.", "english": "Today we are at thirty degrees in the shade."},
                {"spanish": "Hay niebla en el aeropuerto.", "english": "There is fog at the airport."},
                {"spanish": "El cielo está totalmente azul y despejado.", "english": "The sky is totally blue and clear."},
                {"spanish": "Mañana van a subir las temperaturas.", "english": "Tomorrow temperatures are going to rise."}
            ],
            "commonMistakes": [
                {"wrong": "Hace 20 grados (common, but colloquial)", "right": "Estamos a 20 grados", "explanation": "The most natural, elegant way to state temperature in Spain is 'Estamos a 20 grados'."},
                {"wrong": "Un paragua (dropping the s)", "right": "Un paraguas", "explanation": "'Paraguas' always ends in -s in both singular and plural."}
            ],
            "proTip": "The famous Spanish weather proverb for spring: **«Hasta el cuarenta de mayo no te quites el sayo»** (Until May 40th — June 9th — don't take off your woolen sweater)! It reminds people that sudden cold snaps happen well into late spring in central Spain."
        },
        "conversation": {
            "title": "Discussing the Weekend Weather Forecast",
            "context": "Sakib and his friend Elena plan an outdoor picnic.",
            "dialogue": [
                {"speaker": "Elena", "role": "Friend", "spanish": "Sakib, ¿has mirado el pronóstico del tiempo para el sábado?", "english": "Sakib, have you looked at the weather forecast for Saturday?"},
                {"speaker": "Sakib", "role": "Student", "spanish": "Sí, acabo de mirarlo en la aplicación. Dice que el cielo va a estar despejado.", "english": "Yes, I just looked at it on the app. It says the sky is going to be clear."},
                {"speaker": "Elena", "role": "Friend", "spanish": "¿Y a cuántos grados vamos a estar?", "english": "And at how many degrees are we going to be?"},
                {"speaker": "Sakib", "role": "Student", "spanish": "Las temperaturas suben: vamos a estar a unos veintitrés grados al mediodía. No va a hacer nada de frío.", "english": "Temperatures are rising: we are going to be at around twenty-three degrees at noon. It is not going to be cold at all."},
                {"speaker": "Elena", "role": "Friend", "spanish": "¡Qué tiempo tan estupendo! Entonces podemos hacer el picnic en el Parque del Retiro.", "english": "What great weather! Then we can do the picnic in the Retiro Park."},
                {"speaker": "Sakib", "role": "Student", "spanish": "¡Claro! Yo llevo mis gafas de sol y preparo algo rico para comer.", "english": "Of course! I'll bring my sunglasses and prepare something delicious to eat."}
            ],
            "keyPhrases": [
                {"phrase": "Acabo de mirar", "explanation": "'I just looked' (acabar de + infinitive = to have just done something)."},
                {"phrase": "A la sombra", "explanation": "'In the shade'."},
                {"phrase": "Hacer un picnic", "explanation": "'To have a picnic'."}
            ]
        },
        "reading": {
            "title": "Las cuatro estaciones en la vida española",
            "passage": "El cambio de estación marca profundamente la vida cotidiana en España. La primavera despierta los campos con flores silvestres y terrazas animadas; las temperaturas son suaves y oscilan entre los quince y los veintidós grados. El verano transforma el país: en julio y agosto el sol brilla intensamente y en el interior se alcanzan fácilmente los cuarenta grados, lo que empuja a millones de personas hacia las playas mediterráneas y cantábricas. El otoño viste los parques de tonos dorados y rojizos; las lluvias regresan y las temperaturas bajan gradualmente. Finalmente, el invierno cubre de nieve las cumbres de Sierra Nevada y los Pirineos, llenando las ciudades de luces festivas y castañas asadas humeantes en las esquinas.",
            "translation": "The change of season profoundly marks daily life in Spain. Spring awakens the fields with wild flowers and lively terraces; temperatures are mild and hover between fifteen and twenty-two degrees. Summer transforms the country: in July and August the sun shines intensely and inland forty degrees is easily reached, which pushes millions of people toward the Mediterranean and Cantabrian beaches. Autumn dresses parks in golden and reddish tones; rains return and temperatures drop gradually. Finally, winter covers the peaks of Sierra Nevada and the Pyrenees with snow, filling cities with festive lights and steaming roasted chestnuts on street corners.",
            "questions": [
                {"question": "¿A qué temperaturas se puede llegar en el interior de España en verano?", "options": ["A diez grados", "Fácilmente a los cuarenta grados", "A cero grados", "A quince grados"], "answer": 1, "explanation": "40 degrees ('fácilmente los cuarenta grados')."},
                {"question": "¿Qué comen en las esquinas de las ciudades en invierno?", "options": ["Helado de fresa", "Castañas asadas humeantes", "Gazpacho frío", "Sandías"], "answer": 1, "explanation": "Steaming roasted chestnuts ('castañas asadas humeantes')."},
                {"question": "¿Dónde hay nieve en invierno?", "options": ["En las playas", "En las cumbres de Sierra Nevada y Pirineos", "Solo en el metro", "En los museos"], "answer": 1, "explanation": "Sierra Nevada and Pyrenees mountains."}
            ]
        },
        "exercises": [
            {
                "id": "d33-ex1",
                "type": "fill-in",
                "prompt": "How do you state temperature: Hoy ______ (we are at) 22 grados.",
                "options": ["estamos a", "somos en", "hacemos a", "tenemos en"],
                "correct": 0,
                "explanation": "'Estamos a [número] grados' is the standard Spanish formula."
            },
            {
                "id": "d33-ex2",
                "type": "multiple-choice",
                "prompt": "Which word is used for 'There is fog'?",
                "options": ["Hace niebla / Hay niebla", "Es niebla", "Está niebla", "Tiene niebla"],
                "correct": 0,
                "explanation": "'Hay niebla' (or hace niebla) is used for fog."
            },
            {
                "id": "d33-ex3",
                "type": "multiple-choice",
                "prompt": "What does 'El cielo está despejado' mean?",
                "options": ["The sky is raining", "The sky is clear (cloudless)", "The sky is stormy", "It is night"],
                "correct": 1,
                "explanation": "'Despejado' means clear / unclouded."
            },
            {
                "id": "d33-ex4",
                "type": "translation",
                "prompt": "Translate: 'Tomorrow temperatures are going to drop.'",
                "options": ["Mañana van a bajar las temperaturas.", "Mañana van a subir las temperaturas.", "Mañana hacen frío temperaturas.", "Mañana están bajas temperaturas."],
                "correct": 0,
                "explanation": "'Bajar' means to drop / descend: 'van a bajar las temperaturas'."
            }
        ],
        "speakingChallenge": [
            {"prompt": "Say what temperature it is today using 'Estamos a...'", "hint": "Hoy estamos a... grados.", "sampleAnswer": "Hoy estamos a veintiún grados con cielo despejado."},
            {"prompt": "Say what your favorite season is and why.", "hint": "Mi estación favorita es... porque...", "sampleAnswer": "Mi estación favorita es la primavera porque no hace ni frío ni calor y los días son largos."},
            {"prompt": "Tell someone to take an umbrella because it's going to rain.", "hint": "Coge el paraguas porque...", "sampleAnswer": "Coge el paraguas porque el cielo está nublado y va a llover."}
        ],
        "dailyRevision": {
            "quickQuestions": [
                "How do you say 'We are at 20 degrees'?",
                "Why does 'paraguas' end in -s even for one umbrella?"
            ],
            "grammarRecall": "Temperature: Estamos a [X] grados. Sky: El cielo está despejado/nublado. Atmosphere: Hay niebla/tormenta. Subir vs. bajar.",
            "vocabRecall": ["El grado", "El cielo despejado", "La tormenta", "La niebla", "El paraguas", "El pronóstico", "Subir", "Bajar"]
        },
        "checklist": [
            "Expressed temperatures using 'Estamos a [X] grados'",
            "Learned weather terms: tormenta, niebla, despejado, nublado",
            "Understood 'subir' and 'bajar' for temperature trends",
            "Described the 4 Spanish seasons in depth",
            "Completed all 4 weather exercises",
            "Practiced giving a short weather forecast out loud"
        ]
    },
    {
        "day": 34,
        "stage": 4,
        "title": "Describing People: Appearance & Personality",
        "subtitle": "Physical traits (hair, eyes, height) vs. Personality (SER vs. TENER vs. LLEVAR)",
        "goals": [
            "Describe physical appearance: hair (pelo), eyes (ojos), height, build",
            "Describe personality and character traits (simpático, trabajador, tímido, generoso)",
            "Master the three-verb descriptive system: SER (essence/traits) vs. TENER (features) vs. LLEVAR (accessories/hair/beard)",
            "Combine descriptions into cohesive character profiles"
        ],
        "bengaliNote": "Describing people in Spanish is an art! Just like in Bangla, you use three distinct verbs: 1) **SER** for overall traits (*তিনি লম্বা ও দয়ালু* = *Es alto y amable*); 2) **TENER** for features (*তার কালো চোখ আছে* = *Tiene los ojos negros*); 3) **LLEVAR** for what someone wears or bears (*তার দাড়ি আছে / চশমা পরে* = *Lleva barba / Lleva gafas*)!",
        "vocabulary": [
            {"word": "El pelo (moreno, rubio, castaño, liso, rizado)", "translation": "Hair (dark, blond, brown, straight, curly)", "pos": "noun", "gender": "masculine", "example": "Tiene el pelo castaño y rizado.", "exampleTranslation": "He/she has curly brown hair."},
            {"word": "Los ojos (marrones, azules, verdes, negros)", "translation": "Eyes (brown, blue, green, black)", "pos": "noun", "gender": "masculine plural", "example": "Tiene los ojos marrones y grandes.", "exampleTranslation": "He/she has big brown eyes."},
            {"word": "Alto(a) / Bajo(a) / Delgado(a) / Fuerte", "translation": "Tall / Short / Slim / Strong (build)", "pos": "adjective", "gender": "variable", "example": "Es un chico alto y delgado.", "exampleTranslation": "He is a tall, slim boy."},
            {"word": "La barba / El bigote", "translation": "The beard / The mustache", "pos": "noun", "gender": "masculine", "example": "Lleva barba recortada.", "exampleTranslation": "He wears a trimmed beard."},
            {"word": "Las gafas (llevar gafas)", "translation": "Glasses (to wear glasses)", "pos": "noun", "gender": "feminine plural", "example": "Lleva gafas de lectura.", "exampleTranslation": "He/she wears reading glasses."},
            {"word": "Simpático(a) / Antipático(a)", "translation": "Friendly, nice / Unfriendly, unpleasant", "pos": "adjective", "gender": "variable", "example": "La profesora es simpatiquísima.", "exampleTranslation": "The teacher is extremely friendly."},
            {"word": "Trabajador(a) / Vago(a)", "translation": "Hardworking / Lazy", "pos": "adjective", "gender": "variable", "example": "Sakib es un estudiante muy trabajador.", "exampleTranslation": "Sakib is a very hardworking student."},
            {"word": "Tímido(a) / Extrovertido(a)", "translation": "Shy / Outgoing, extroverted", "pos": "adjective", "gender": "variable", "example": "Al principio es tímido, pero luego es muy sociable.", "exampleTranslation": "At first he is shy, but then he is very sociable."},
            {"word": "Generoso(a) / Tacaño(a)", "translation": "Generous / Stingy, cheap", "pos": "adjective", "gender": "variable", "example": "Mis amigos son muy generosos.", "exampleTranslation": "My friends are very generous."},
            {"word": "Inteligente / Divertido(a)", "translation": "Intelligent / Fun, entertaining", "pos": "adjective", "gender": "mixed", "example": "Es una persona divertida e inteligente.", "exampleTranslation": "He/she is a fun and intelligent person."}
        ],
        "sentences": [
            {"spanish": "Sakib es de estatura media, tiene el pelo negro y los ojos oscuros.", "english": "Sakib is of medium height, has black hair and dark eyes."},
            {"spanish": "Mi mejor amigo es muy alto, simpático y divertido.", "english": "My best friend is very tall, friendly, and fun."},
            {"spanish": "Ella lleva gafas y tiene el pelo rubio y rizado.", "english": "She wears glasses and has curly blond hair."},
            {"spanish": "El profesor lleva barba y es un hombre muy sabio.", "english": "The teacher wears a beard and is a very wise man."},
            {"spanish": "¿Cómo es físicamente tu hermano? —Es alto y moreno.", "english": "What does your brother look like physically? —He is tall and dark-haired."},
            {"spanish": "Es una persona muy trabajadora, honesta y generosa.", "english": "She/he is a very hardworking, honest, and generous person."}
        ],
        "grammar": {
            "title": "The 3-Verb Descriptive Engine: SER, TENER & LLEVAR",
            "explanation": "Never mix up these three verbs when painting a portrait of a person in Spanish:",
            "rules": [
                "1. SER is for Permanent Traits & Personality: Use *ser* for height, general build, and character traits: *Es alto, es delgado, es simpático, es tímido, es generoso*.",
                "2. TENER is for Physical Features (Eyes, Hair, Age): Use *tener* with definite articles for hair and eyes: *Tiene el pelo negro* (NOT *Tiene pelo negro*), *Tiene los ojos verdes* (NOT *Tiene ojos verdes*), *Tiene 25 años*.",
                "3. LLEVAR is for Accessories & Facial Hair: Use *llevar* (literally: to carry/wear) for things that can be removed or changed: *Lleva gafas* (wears glasses), *Lleva barba* (wears a beard), *Lleva bigote* (wears a mustache), *Lleva una camisa roja*.",
                "Adjective of personality agreement: Remember that adjectives ending in -dor add -a for feminine: *trabajador -> trabajadora*!"
            ],
            "structures": [
                "SER + Adjetivo de carácter / estatura: Es alto / simpático / generoso",
                "TENER + el pelo [color/forma] + los ojos [color]: Tiene el pelo castaño y los ojos marrones",
                "LLEVAR + accesorios / barba / ropa: Lleva gafas / barba / sombrero"
            ],
            "examples": [
                {"spanish": "Carlos es moreno. (Ser: physical trait)", "english": "Carlos is dark-haired."},
                {"spanish": "Carlos tiene los ojos azules. (Tener: feature)", "english": "Carlos has blue eyes."},
                {"spanish": "Carlos lleva barba. (Llevar: beard)", "english": "Carlos has a beard."},
                {"spanish": "Elena es muy trabajadora. (Ser: personality)", "english": "Elena is very hardworking."}
            ],
            "commonMistakes": [
                {"wrong": "Es ojos marrones", "right": "Tiene los ojos marrones", "explanation": "Features are possessed with 'tener'."},
                {"wrong": "Tiene barba (acceptable, but native preference is:)", "right": "Lleva barba", "explanation": "In Spain, 'llevar barba' is the authentic native idiom."}
            ],
            "proTip": "Notice the difference: *Moreno* means dark-haired or tan skin. *Rubio* means blond. *Pelirrojo* means red-haired. *Calvo* means bald (*Es calvo*)!"
        },
        "conversation": {
            "title": "Meeting at the Train Station",
            "context": "Sakib describes his visiting friend Tariq to Alberto so they can spot him at the station.",
            "dialogue": [
                {"speaker": "Alberto", "role": "Friend", "spanish": "Hay muchísima gente en Atocha. ¿Cómo es tu hermano Tariq físicamente?", "english": "There are so many people at Atocha. What does your brother Tariq look like physically?"},
                {"speaker": "Sakib", "role": "Student", "spanish": "Es bastante alto, más alto que yo. Tiene el pelo negro y corto, y los ojos muy oscuros.", "english": "He is quite tall, taller than me. He has short black hair and very dark eyes."},
                {"speaker": "Alberto", "role": "Friend", "spanish": "¿Lleva barba o gafas?", "english": "Does he wear a beard or glasses?"},
                {"speaker": "Sakib", "role": "Student", "spanish": "Lleva una barba corta y bien recortada, pero no lleva gafas. Ah, y me ha dicho que lleva una chaqueta verde oscura.", "english": "He has a short, neatly trimmed beard, but doesn't wear glasses. Ah, and he told me he's wearing a dark green jacket."},
                {"speaker": "Alberto", "role": "Friend", "spanish": "¿Es aquel chico que sonríe junto a la cafetería?", "english": "Is it that guy smiling next to the cafeteria?"},
                {"speaker": "Sakib", "role": "Student", "spanish": "¡Sí, es él! ¡Tariq! ¡Aquí estamos!", "english": "Yes, that's him! Tariq! Here we are!"}
            ],
            "keyPhrases": [
                {"phrase": "Estatura media", "explanation": "'Medium height'."},
                {"phrase": "Aquel chico", "explanation": "'That guy over there'."},
                {"phrase": "Bien recortada", "explanation": "'Well trimmed'."}
            ]
        },
        "reading": {
            "title": "Un retrato de mis amigos en Madrid",
            "passage": "En estos meses en Madrid, Sakib ha formado un grupo de amigos muy diverso. Su compañero de piso, Alberto, es madrileño, alto, con el pelo rizado y castaño. Es un chico extrovertido, divertido y siempre cuenta chistes que hacen reír a todos. Su compañera de clase, Laura, es de Valencia: es delgada, tiene los ojos verdes brillantes y lleva gafas modernas de pasta roja. Laura es muy trabajadora, ordenada y generosa; siempre comparte sus apuntes de gramática con Sakib cuando hay dudas complejas. Aunque todos tienen apariencias y personalidades distintas, la amistad y el deseo de aprender los une como una familia.",
            "translation": "During these months in Madrid, Sakib has formed a very diverse group of friends. His flatmate, Alberto, is from Madrid, tall, with curly brown hair. He is an outgoing, fun guy and always tells jokes that make everyone laugh. His classmate, Laura, is from Valencia: she is slim, has bright green eyes, and wears modern red plastic-frame glasses. Laura is very hardworking, organized, and generous; she always shares her grammar notes with Sakib when there are complex questions. Although all have distinct appearances and personalities, friendship and the desire to learn unites them like a family.",
            "questions": [
                {"question": "¿Cómo es el pelo de Alberto?", "options": ["Rubio y liso", "Rizado y castaño", "Pelirrojo", "Es calvo"], "answer": 1, "explanation": "Curly brown ('rizado y castaño')."},
                {"question": "¿De qué color son los ojos de Laura?", "options": ["Marrones", "Azules", "Verdes brillantes", "Negros"], "answer": 2, "explanation": "Bright green ('ojos verdes brillantes')."},
                {"question": "¿Qué lleva Laura en la cara?", "options": ["Una barba", "Un sombrero", "Gafas modernas de pasta roja", "Un antifaz"], "answer": 2, "explanation": "Modern red glasses ('gafas modernas de pasta roja')."}
            ]
        },
        "exercises": [
            {
                "id": "d34-ex1",
                "type": "fill-in",
                "prompt": "Choose SER, TENER, or LLEVAR: Carlos ______ (has) los ojos verdes.",
                "options": ["tiene", "es", "lleva", "está"],
                "correct": 0,
                "explanation": "Eyes are described with 'tener': 'tiene los ojos verdes'."
            },
            {
                "id": "d34-ex2",
                "type": "fill-in",
                "prompt": "Choose SER, TENER, or LLEVAR: Mi profesor ______ (wears) barba y gafas.",
                "options": ["lleva", "es", "tiene", "está"],
                "correct": 0,
                "explanation": "Beards and glasses use 'llevar': 'lleva barba y gafas'."
            },
            {
                "id": "d34-ex3",
                "type": "fill-in",
                "prompt": "Make the adjective agree: María es una estudiante muy ______ (trabajador).",
                "options": ["trabajadora", "trabajador", "trabajadoras", "trabajadores"],
                "correct": 0,
                "explanation": "Adjectives ending in -dor add -a for feminine: 'trabajadora'."
            },
            {
                "id": "d34-ex4",
                "type": "translation",
                "prompt": "Translate: 'He is tall, friendly, and wears glasses.'",
                "options": ["Es alto, simpático y lleva gafas.", "Tiene alto, simpático y es gafas.", "Lleva alto, simpático y tiene gafas.", "Está alto, simpático y hace gafas."],
                "correct": 0,
                "explanation": "'Es alto, simpático y lleva gafas' accurately coordinates SER and LLEVAR."
            }
        ],
        "speakingChallenge": [
            {"prompt": "Describe your own physical appearance in Spanish (hair, eyes, build).", "hint": "Soy... tengo el pelo... y los ojos...", "sampleAnswer": "Soy de estatura media, tengo el pelo negro y corto, y los ojos marrones oscuros."},
            {"prompt": "Describe your best friend's personality using 3 adjectives.", "hint": "Mi mejor amigo es...", "sampleAnswer": "Mi mejor amigo es muy simpático, honesto y trabajador."},
            {"prompt": "Say that someone wears a beard and glasses.", "hint": "Él lleva barba y...", "sampleAnswer": "Mi tío lleva barba recortada y lleva gafas de sol."}
        ],
        "dailyRevision": {
            "quickQuestions": [
                "What verb is used for height and personality? (SER)",
                "What verb is used for beard and glasses in Spain? (LLEVAR)"
            ],
            "grammarRecall": "SER: alto, bajo, simpático. TENER: el pelo [tipo], los ojos [color]. LLEVAR: barba, bigote, gafas.",
            "vocabRecall": ["El pelo", "Los ojos", "La barba", "Las gafas", "Simpático", "Trabajador", "Tímido", "Generoso"]
        },
        "checklist": [
            "Separated descriptive tasks across SER, TENER, and LLEVAR",
            "Described hair and eye colors with definite articles",
            "Used 'llevar' for beards, mustaches, and glasses",
            "Formed feminine forms for -dor adjectives (trabajadora)",
            "Completed all 4 description exercises",
            "Delivered a complete portrait description out loud"
        ]
    },
    {
        "day": 35,
        "stage": 4,
        "title": "Describing Places & Cities",
        "subtitle": "City adjectives, cultural landmarks, and HAY vs. ESTÁ in urban settings + Mid-Stage 4 Review",
        "goals": [
            "Describe neighborhoods, towns, and cities with descriptive adjectives",
            "Use place adjectives: antiguo, moderno, tranquilo, ruidoso, turístico, acogedor",
            "Master HAY (existence of places) vs. ESTÁ (location of landmarks) with 100% precision",
            "Complete the Stage 4 Mid-Point Revision (Days 31 to 35 review)"
        ],
        "bengaliNote": "Describing a city like Madrid, Barcelona, or Dhaka requires contrasting historical charm with modern vibrance. In Spanish, remember the master rule: **Hay** = 'আছে' (there exists an unspecific thing: *Hay un museo*); **Está** = 'অবস্থিত' (a specific known landmark is located: *El museo está aquí*).",
        "vocabulary": [
            {"word": "Antiguo(a) / Histórico(a)", "translation": "Ancient, antique / Historic", "pos": "adjective", "gender": "variable", "example": "Toledo tiene un casco antiguo precioso.", "exampleTranslation": "Toledo has a gorgeous historic old town."},
            {"word": "Moderno(a)", "translation": "Modern", "pos": "adjective", "gender": "variable", "example": "La estación de tren es muy moderna.", "exampleTranslation": "The train station is very modern."},
            {"word": "Tranquilo(a) / Ruidoso(a)", "translation": "Quiet, peaceful / Noisy", "pos": "adjective", "gender": "variable", "example": "Mi barrio es tranquilo, no hay ruido.", "exampleTranslation": "My neighborhood is quiet, there is no noise."},
            {"word": "Turístico(a)", "translation": "Touristy / Tourist-friendly", "pos": "adjective", "gender": "variable", "example": "Plaza Mayor es una zona muy turística.", "exampleTranslation": "Plaza Mayor is a very touristy area."},
            {"word": "Acogedor(a)", "translation": "Cozy / Welcoming / Warm", "pos": "adjective", "gender": "variable", "example": "Es una ciudad muy acogedora.", "exampleTranslation": "It is a very welcoming city."},
            {"word": "El monumento / El edificio", "translation": "The monument / The building", "pos": "noun", "gender": "masculine", "example": "Hay muchos monumentos históricos.", "exampleTranslation": "There are many historic monuments."},
            {"word": "El barrio", "translation": "The neighborhood / district", "pos": "noun", "gender": "masculine", "example": "Vivo en un barrio tradicional.", "exampleTranslation": "I live in a traditional neighborhood."},
            {"word": "El puente / La fuente", "translation": "The bridge / The fountain", "pos": "noun", "gender": "masculine / feminine", "example": "La fuente de Cibeles es famosa.", "exampleTranslation": "The Cibeles fountain is famous."},
            {"word": "El ambiente", "translation": "The atmosphere / vibe", "pos": "noun", "gender": "masculine", "example": "Hay un ambiente animado en las calles.", "exampleTranslation": "There is a lively vibe in the streets."},
            {"word": "Estar situado(a) en...", "translation": "To be situated / located in...", "pos": "phrase", "gender": "variable", "example": "Madrid está situada en el centro de España.", "exampleTranslation": "Madrid is situated in the center of Spain."}
        ],
        "sentences": [
            {"spanish": "Madrid es una ciudad grande, cosmopolita y muy acogedora.", "english": "Madrid is a big, cosmopolitan, and very welcoming city."},
            {"spanish": "En mi barrio hay muchas tiendas pequeñas y un parque tranquilo.", "english": "In my neighborhood there are many small shops and a quiet park."},
            {"spanish": "El Palacio Real está situado cerca del río Manzanares.", "english": "The Royal Palace is situated near the Manzanares river."},
            {"spanish": "¿Hay alguna farmacia de guardia por aquí?", "english": "Is there any 24-hour pharmacy around here?"},
            {"spanish": "Las calles del centro son estrechas, peatonales y llenas de vida.", "english": "The streets of the center are narrow, pedestrian, and full of life."},
            {"spanish": "Me encanta el ambiente nocturno de las plazas españolas.", "english": "I love the evening atmosphere of Spanish squares."}
        ],
        "grammar": {
            "title": "Urban Master Guide: HAY vs. ESTÁ & Estar Situado",
            "explanation": "In city navigation, confusing HAY and ESTÁ is the most common beginner error. Lock this distinction into your mind forever:",
            "rules": [
                "HAY (Existence / Discovery): Use 'Hay' with indefinite articles (*un, una, unos, unas*), numbers, or quantity words (*muchos, pocos, ningún*). E.g. *En esta calle HAY un banco* (On this street there is a bank). *HAY tres cafeterías*.",
                "ESTÁ / ESTÁN (Specific Landmark Location): Use 'Está' with names of landmarks, definite articles (*el, la, los, las*), or possessives. E.g. *El Museo del Prado ESTÁ en el Paseo del Prado* (NOT *Hay el Museo del Prado*!).",
                "Estar Situado(a): To formally state geographic placement, use *está situado(a) en...*: *Toledo está situada sobre una colina*.",
                "Descriptive Word Order: Remember, place adjectives follow the noun: *un barrio tranquilo*, *una ciudad moderna*."
            ],
            "structures": [
                "Existence: En [Lugar] HAY + un/una/unos/unas/muchos + [Sitios]",
                "Location: [Nombre o el/la + Sitio] + ESTÁ + en / al lado de / cerca de",
                "Character: [Ciudad / Barrio] ES + [Adjetivo: grande, bonito, ruidoso]"
            ],
            "examples": [
                {"spanish": "En Madrid hay muchos parques. (Hay: quantity/existence)", "english": "In Madrid there are many parks."},
                {"spanish": "El parque del Retiro está en el centro. (Estar: specific location)", "english": "Retiro park is in the center."},
                {"spanish": "Salamanca es una ciudad universitaria muy antigua.", "english": "Salamanca is a very ancient university city."},
                {"spanish": "Mi piso está situado en una calle peatonal.", "english": "My apartment is situated on a pedestrian street."}
            ],
            "commonMistakes": [
                {"wrong": "¿Dónde hay el banco? (fatal error)", "right": "¿Dónde está el banco? (or: ¿Hay un banco por aquí?)", "explanation": "Never use 'hay' with 'el/la'."},
                {"wrong": "El museo hay en la plaza", "right": "El museo está en la plaza", "explanation": "Specific known landmarks use 'estar'."}
            ],
            "proTip": "If you ask a stranger on the street: Ask **«¿Hay una farmacia por aquí cerca?»** (Is there A pharmacy nearby?) if you just need any medicine. But ask **«¿Dónde está la farmacia más cercana?»** (Where is THE nearest pharmacy?) if asking for location!"
        },
        "conversation": {
            "title": "Showing a Visiting Friend Around Madrid",
            "context": "Sakib gives his visiting friend a tour of the historic neighborhood of Los Austrias.",
            "dialogue": [
                {"speaker": "Sakib", "role": "Guide / Student", "spanish": "Bienvenido al Madrid de los Austrias. Esta es la parte más antigua e histórica de la ciudad.", "english": "Welcome to Hapsburg Madrid. This is the oldest and most historic part of the city."},
                {"speaker": "Amigo", "role": "Visitor", "spanish": "¡Qué maravilla de edificios! Las fachadas son preciosas. ¿Qué hay en esa plaza?", "english": "What wonderful buildings! The facades are gorgeous. What is in that plaza?"},
                {"speaker": "Sakib", "role": "Guide / Student", "spanish": "Esa es la Plaza de la Villa. Hay tres edificios medievales del siglo quince. Y justo detrás está la calle Mayor.", "english": "That is the Plaza de la Villa. There are three 15th-century medieval buildings. And right behind is Mayor street."},
                {"speaker": "Amigo", "role": "Visitor", "spanish": "¿Y el Palacio Real está muy lejos de aquí?", "english": "And is the Royal Palace very far from here?"},
                {"speaker": "Sakib", "role": "Guide / Student", "spanish": "No, está a solo cinco minutos a pie. Bajamos por esta calle tranquila y llegamos enseguida.", "english": "No, it is only five minutes on foot. We go down this quiet street and arrive right away."},
                {"speaker": "Amigo", "role": "Visitor", "spanish": "Me encanta el ambiente de esta zona. No es ruidosa y la gente es muy amable.", "english": "I love the vibe of this area. It's not noisy and the people are very kind."}
            ],
            "keyPhrases": [
                {"phrase": "Fachadas", "explanation": "'Building facades / fronts'."},
                {"phrase": "Casco antiguo", "explanation": "'Historic old quarter / historic town center'."},
                {"phrase": "Calle peatonal", "explanation": "'Pedestrian-only street'."}
            ]
        },
        "reading": {
            "title": "Mid-Stage 4 Review Story: El encanto de las ciudades españolas",
            "passage": "A los treinta y cinco días de comenzar su aprendizaje, Sakib realiza un viaje de fin de semana a Segovia con sus compañeros. Segovia es una ciudad histórica situada al norte de Madrid, declarada Patrimonio de la Humanidad. Al llegar, los estudiantes quedan impresionados ante el majestuoso Acueducto romano, que tiene más de dos mil años de antigüedad. Sakib camina por las calles empedradas y entra en un restaurante tradicional donde piden el menú del día con cochinillo asado. Sakib habla con el camarero en español con total fluidez: pide agua sin gas, pregunta por los ingredientes de los platos y pide la cuenta al terminar. Luego visitan el Alcázar, un castillo de cuento de hadas que está situado sobre una roca entre dos ríos. Sakib piensa: «Mi español ya no es un sueño, es una realidad viva».",
            "translation": "Thirty-five days after beginning his learning, Sakib takes a weekend trip to Segovia with his classmates. Segovia is a historic city situated north of Madrid, declared a World Heritage Site. Upon arriving, the students are impressed before the majestic Roman Aqueduct, which is over two thousand years old. Sakib walks through cobblestone streets and enters a traditional restaurant where they order the daily set menu with roast suckling pig. Sakib speaks with the waiter in Spanish with total fluency: orders still water, asks about dish ingredients, and asks for the bill upon finishing. Then they visit the Alcazar, a fairytale castle situated on a rock between two rivers. Sakib thinks: 'My Spanish is no longer a dream, it is a living reality.'",
            "questions": [
                {"question": "¿A qué ciudad viaja Sakib en el día 35?", "options": ["A Barcelona", "A Segovia", "A Valencia", "A Sevilla"], "answer": 1, "explanation": "To Segovia ('un viaje de fin de semana a Segovia')."},
                {"question": "¿Cuántos años de antigüedad tiene el Acueducto romano de Segovia?", "options": ["Cien años", "Quinientos años", "Más de dos mil años", "Cincuenta años"], "answer": 2, "explanation": "Over two thousand years old ('más de dos mil años')."},
                {"question": "¿Qué piensa Sakib al final del día?", "options": ["Que tiene ganas de volver a casa", "Que su español ya no es un sueño, es una realidad viva", "Que el examen va a ser difícil", "Que tiene frío"], "answer": 1, "explanation": "That his Spanish is no longer a dream, it is a living reality."}
            ]
        },
        "exercises": [
            {
                "id": "d35-ex1",
                "type": "fill-in",
                "prompt": "Choose HAY or ESTÁ: En mi barrio ______ (there is) un parque precioso.",
                "options": ["hay", "está", "están", "es"],
                "correct": 0,
                "explanation": "'Un parque' (indefinite) states existence, so use 'hay'."
            },
            {
                "id": "d35-ex2",
                "type": "fill-in",
                "prompt": "Choose HAY or ESTÁ: La catedral ______ (is located) en la plaza mayor.",
                "options": ["está", "hay", "es", "tiene"],
                "correct": 0,
                "explanation": "'La catedral' (specific landmark) takes 'está'."
            },
            {
                "id": "d35-ex3",
                "type": "multiple-choice",
                "prompt": "What does 'acogedor(a)' mean when describing a town or room?",
                "options": ["Noisy and polluted", "Cozy, welcoming, and warm", "Expensive", "Industrial"],
                "correct": 1,
                "explanation": "'Acogedor' means cozy, warm, and hospitable."
            },
            {
                "id": "d35-ex4",
                "type": "translation",
                "prompt": "Translate: 'It is a quiet neighborhood and the streets are clean.'",
                "options": ["Es un barrio tranquilo y las calles están limpias.", "Está un barrio tranquilo y las calles son limpias.", "Hay un barrio tranquilo y calles limpias.", "Tiene un barrio tranquilo y es limpio."],
                "correct": 0,
                "explanation": "'Es un barrio tranquilo y las calles están limpias' accurately pairs SER and ESTAR."
            }
        ],
        "speakingChallenge": [
            {"prompt": "Describe your hometown: is it big, historic, noisy, or modern?", "hint": "Mi ciudad natal es... y tiene...", "sampleAnswer": "Mi ciudad natal es muy grande, vibrante, ruidosa y llena de historia."},
            {"prompt": "Say where a famous landmark in your city is located using 'está situado en'.", "hint": "El monumento está situado en...", "sampleAnswer": "El monumento nacional está situado en el centro de la ciudad."},
            {"prompt": "Say that there are many restaurants and a quiet park in your neighborhood.", "hint": "En mi barrio hay muchos... y un...", "sampleAnswer": "En mi barrio hay muchos restaurantes deliciosos y un parque muy tranquilo para pasear."}
        ],
        "dailyRevision": {
            "quickQuestions": [
                "What is the difference between '¿Dónde hay un banco?' and '¿Dónde está el banco?'?",
                "What adjective means 'welcoming / cozy' in Spanish?"
            ],
            "grammarRecall": "HAY + un/una/muchos (existence). ESTAR + el/la/nombre (location). Adjectives: histórico, moderno, tranquilo, ruidoso, acogedor.",
            "vocabRecall": ["Antiguo", "Moderno", "Tranquilo", "Ruidoso", "Turístico", "Acogedor", "El barrio", "El monumento"]
        },
        "checklist": [
            "Described cities and neighborhoods using rich adjectives",
            "Mastered the critical distinction between HAY and ESTÁ",
            "Used 'estar situado en' for geographic location",
            "Completed the Mid-Stage 4 reading review story in Segovia",
            "Passed all 4 urban description exercises",
            "Described my own hometown fluently out loud"
        ]
    }
]

print(f"Loaded {len(stage4_days)} initial days for Stage 4.")
