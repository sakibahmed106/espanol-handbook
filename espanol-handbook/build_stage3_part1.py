"""
Build Stage 3: Days 21 to 25
"""
import json

stage3_days = [
    {
        "day": 21,
        "stage": 3,
        "title": "Daily Routines & Reflexive Verbs",
        "subtitle": "Talking about your day from waking up to going to sleep",
        "goals": [
            "Describe your typical day using daily routine verbs",
            "Understand the concept of Reflexive Verbs (actions you do to yourself)",
            "Master reflexive pronouns: me, te, se, nos, os, se",
            "Conjugate daily verbs: levantarse, ducharse, vestirse, acostarse"
        ],
        "bengaliNote": "In Bangla, we say 'আমি ঘুম থেকে উঠি' or 'আমি গোসল করি'. In Spanish, actions you perform on your own body require a **reflexive pronoun** (*me, te, se, nos, os, se*). For example: *levantar* = to lift; *levantarse* = to lift oneself (to get up)! *Me levanto* = I get myself up.",
        "vocabulary": [
            {"word": "Levantarse", "translation": "To get up (out of bed)", "pos": "reflexive verb", "gender": None, "example": "Me levanto a las siete de la mañana.", "exampleTranslation": "I get up at seven in the morning."},
            {"word": "Despertarse", "translation": "To wake up (e -> ie)", "pos": "reflexive verb", "gender": None, "example": "Me despierto temprano todos los días.", "exampleTranslation": "I wake up early every day."},
            {"word": "Ducharse", "translation": "To take a shower", "pos": "reflexive verb", "gender": None, "example": "Me ducho con agua caliente.", "exampleTranslation": "I shower with warm water."},
            {"word": "Lavarse (los dientes / las manos)", "translation": "To wash oneself (teeth / hands)", "pos": "reflexive verb", "gender": None, "example": "Me lavo los dientes después de comer.", "exampleTranslation": "I brush my teeth after eating."},
            {"word": "Vestirse", "translation": "To get dressed (e -> i)", "pos": "reflexive verb", "gender": None, "example": "Me visto rápidamente.", "exampleTranslation": "I get dressed quickly."},
            {"word": "Desayunar", "translation": "To have breakfast", "pos": "verb", "gender": None, "example": "Desayuno café con tostadas.", "exampleTranslation": "I have breakfast of coffee with toast."},
            {"word": "Salir de casa", "translation": "To leave the house", "pos": "phrase", "gender": None, "example": "Salgo de casa a las ocho y media.", "exampleTranslation": "I leave the house at eight thirty."},
            {"word": "Volver a casa", "translation": "To return home (o -> ue)", "pos": "phrase", "gender": None, "example": "Vuelvo a casa a las seis de la tarde.", "exampleTranslation": "I return home at six in the evening."},
            {"word": "Cenar", "translation": "To have dinner", "pos": "verb", "gender": None, "example": "Ceno con mis compañeros a las nueve.", "exampleTranslation": "I have dinner with my roommates at nine."},
            {"word": "Acostarse", "translation": "To go to bed (o -> ue)", "pos": "reflexive verb", "gender": None, "example": "Me acuesto a las once de la noche.", "exampleTranslation": "I go to bed at eleven at night."}
        ],
        "sentences": [
            {"spanish": "Todos los días me despierto a las siete y me levanto enseguida.", "english": "Every day I wake up at seven and get up right away."},
            {"spanish": "Primero me ducho y luego me visto.", "english": "First I shower and then I get dressed."},
            {"spanish": "¿A qué hora te acuestas normalmente?", "english": "What time do you normally go to bed?"},
            {"spanish": "Salgo de casa a las ocho para ir a clase.", "english": "I leave home at eight to go to class."},
            {"spanish": "Por la noche ceno ligero y leo un rato.", "english": "At night I eat a light dinner and read for a while."},
            {"spanish": "Los domingos me levanto más tarde.", "english": "On Sundays I get up later."}
        ],
        "grammar": {
            "title": "Reflexive Verbs & The Reflexive Pronoun System",
            "explanation": "A verb is reflexive when the subject does the action to or for themselves. You can spot an infinitive reflexive verb because it ends in '-se' (levantar -> levantarse).",
            "rules": [
                "Reflexive Pronouns: Yo -> me | Tú -> te | Él/Ella/Usted -> se | Nosotros -> nos | Vosotros -> os | Ellos/Ellas/Ustedes -> se.",
                "Position: The reflexive pronoun goes DIRECTLY BEFORE the conjugated verb: *Yo me levanto*, *Tú te levantas*, *Él se levanta*.",
                "Conjugating LEVANTARSE: me levanto, te levantas, se levanta, nos levantamos, os levantáis, se levantan.",
                "Body parts with reflexive verbs: In Spanish, use definite articles (*el, la, los, las*), NEVER possessives: *Me lavo las manos* (I wash my hands — NOT *Me lavo mis manos*!)."
            ],
            "structures": [
                "Reflexive Formula: [Pronombre reflexivo: me/te/se/nos/os/se] + [Verbo conjugado]",
                "Levantarse: me levanto | te levantas | se levanta | nos levantamos | os levantáis | se levantan",
                "Sequence markers: Primero (first) -> Luego / Después (then/later) -> Finalmente (finally)"
            ],
            "examples": [
                {"spanish": "Me ducho todas las mañanas.", "english": "I shower every morning."},
                {"spanish": "¿A qué hora te despiertas?", "english": "What time do you wake up?"},
                {"spanish": "Carlos se acuesta muy tarde.", "english": "Carlos goes to bed very late."},
                {"spanish": "Nos levantamos a las ocho.", "english": "We get up at eight."}
            ],
            "commonMistakes": [
                {"wrong": "Me lavo mis dientes", "right": "Me lavo los dientes", "explanation": "Spanish uses the definite article with body parts because 'me' already shows whose teeth they are."},
                {"wrong": "Levanto a las siete (meaning I get up)", "right": "Me levanto a las siete", "explanation": "Without 'me', 'levanto' means I lift something else!"}
            ],
            "proTip": "Remember the sequence formula to narrate any day: **Primero** (First) -> **Luego / Después** (Then / Afterward) -> **Por último / Finalmente** (Finally)!"
        },
        "conversation": {
            "title": "Comparing Daily Morning Routines",
            "context": "Sakib and his friend David chat about their busy morning routines.",
            "dialogue": [
                {"speaker": "David", "role": "Friend", "spanish": "Sakib, ¿a qué hora te levantas entre semana?", "english": "Sakib, what time do you get up on weekdays?"},
                {"speaker": "Sakib", "role": "Student", "spanish": "Me despierto a las siete, pero me levanto a las siete y cuarto.", "english": "I wake up at seven, but I get up at seven fifteen."},
                {"speaker": "David", "role": "Friend", "spanish": "¿Y qué haces primero?", "english": "And what do you do first?"},
                {"speaker": "Sakib", "role": "Student", "spanish": "Primero me ducho con agua templada y me lavo los dientes. Luego desayuno un té y salgo de casa a las ocho.", "english": "First I shower with lukewarm water and brush my teeth. Then I have tea for breakfast and leave home at eight."},
                {"speaker": "David", "role": "Friend", "spanish": "¡Qué organizado eres! Yo siempre tengo prisa y salgo corriendo.", "english": "How organized you are! I am always in a hurry and leave running."},
                {"speaker": "Sakib", "role": "Student", "spanish": "El secreto es acostarse temprano la noche anterior.", "english": "The secret is going to bed early the night before."}
            ],
            "keyPhrases": [
                {"phrase": "Entre semana", "explanation": "'On weekdays' (Monday to Friday)."},
                {"phrase": "Agua templada", "explanation": "'Lukewarm / mild water'."},
                {"phrase": "Salir corriendo", "explanation": "'To leave in a rush / running'."}
            ]
        },
        "reading": {
            "title": "Un día en la vida de Sakib",
            "passage": "La rutina de Sakib en Madrid es activa y productiva. De lunes a viernes, su alarma suena a las siete en punto. Se levanta sin pereza, se ducha y se viste con ropa cómoda. En la cocina prepara un té negro aromático con tostadas de pan con aceite de oliva. A las ocho y media toma el metro en la estación de Iglesia para ir a la academia. Sus clases empiezan a las nueve. Por la tarde vuelve a casa, estudia gramática, cocina comida sana y a las once se acuesta feliz.",
            "translation": "Sakib's routine in Madrid is active and productive. From Monday to Friday, his alarm rings at seven on the dot. He gets up without laziness, showers, and dresses in comfortable clothes. In the kitchen he prepares aromatic black tea with toast and olive oil. At eight thirty he takes the metro at Iglesia station to go to the academy. His classes start at nine. In the afternoon he returns home, studies grammar, cooks healthy food, and at eleven goes to bed happy.",
            "questions": [
                {"question": "¿A qué hora suena la alarma de Sakib entre semana?", "options": ["A las seis", "A las siete en punto", "A las ocho", "A las nueve"], "answer": 1, "explanation": "At seven on the dot ('a las siete en punto')."},
                {"question": "¿En qué estación toma el metro Sakib?", "options": ["Sol", "Atocha", "Iglesia", "Moncloa"], "answer": 2, "explanation": "Iglesia station ('en la estación de Iglesia')."},
                {"question": "¿A qué hora se acuesta Sakib por la noche?", "options": ["A las diez", "A las once", "A la una de la madrugada", "A las ocho"], "answer": 1, "explanation": "At eleven ('a las once se acuesta')."}
            ]
        },
        "exercises": [
            {
                "id": "d21-ex1",
                "type": "fill-in",
                "prompt": "Choose the correct reflexive pronoun: Yo ______ levanto a las siete.",
                "options": ["me", "te", "se", "nos"],
                "correct": 0,
                "explanation": "Yo takes the reflexive pronoun 'me'."
            },
            {
                "id": "d21-ex2",
                "type": "fill-in",
                "prompt": "Complete: Me lavo ______ (my hands) antes de comer.",
                "options": ["las manos", "mis manos", "las manos mías", "los manos"],
                "correct": 0,
                "explanation": "Spanish uses definite articles with body parts in reflexive sentences: 'las manos'."
            },
            {
                "id": "d21-ex3",
                "type": "multiple-choice",
                "prompt": "What does 'acostarse' mean?",
                "options": ["To wake up", "To get dressed", "To go to bed", "To have breakfast"],
                "correct": 2,
                "explanation": "'Acostarse' means to go to bed / lay down."
            },
            {
                "id": "d21-ex4",
                "type": "translation",
                "prompt": "Translate: 'First I shower, then I get dressed.'",
                "options": ["Primero me ducho, luego me visto.", "Primero ducho, luego visto.", "Antes me ducho, después me visto.", "Primero te duchas, luego te vistes."],
                "correct": 0,
                "explanation": "'Primero me ducho, luego me visto' is accurate with reflexive pronouns."
            }
        ],
        "speakingChallenge": [
            {"prompt": "Say what time you wake up and get up in the morning.", "hint": "Me despierto a las... y me levanto a las...", "sampleAnswer": "Me despierto a las siete y me levanto a las siete y media."},
            {"prompt": "Narrate your morning sequence using 'primero' and 'luego'.", "hint": "Primero me ducho, luego...", "sampleAnswer": "Primero me ducho y luego desayuno un café con leche."},
            {"prompt": "Say what time you go to bed on weeknights.", "hint": "Normalmente me acuesto a las...", "sampleAnswer": "Normalmente me acuesto a las once de la noche."}
        ],
        "dailyRevision": {
            "quickQuestions": [
                "What are the 6 reflexive pronouns in Spanish? (me, te, se, nos, os, se)",
                "Why do we say 'me lavo las manos' instead of 'me lavo mis manos'?"
            ],
            "grammarRecall": "Reflexive verbs: Pronoun before verb (me levanto, te levantas, se levanta, nos levantamos, os levantáis, se levantan).",
            "vocabRecall": ["Levantarse", "Despertarse", "Ducharse", "Lavarse", "Vestirse", "Acostarse", "Primero", "Luego"]
        },
        "checklist": [
            "Conjugated reflexive verbs with me, te, se, nos, os, se",
            "Used definite articles with body parts (las manos, los dientes)",
            "Narrated a morning routine chronologically",
            "Read aloud the story of Sakib's day in Madrid",
            "Completed all 4 routine exercises",
            "Described personal routine out loud in Spanish"
        ]
    },
    {
        "day": 22,
        "stage": 3,
        "title": "Time, Schedules & Telling Time",
        "subtitle": "Mastering ¿Qué hora es?, Es la una, Son las dos, and daily schedules",
        "goals": [
            "Ask and tell the time accurately in Spanish (¿Qué hora es?)",
            "Use 'Es la una' (singular for 1:00) vs. 'Son las...' (plural for all other hours)",
            "Express minutes using 'y cuarto' (:15), 'y media' (:30), and 'menos cuarto' (:45)",
            "Distinguish between stating the current time (*Son las tres*) and stating when an event occurs (*A las tres*)"
        ],
        "bengaliNote": "In Bangla, we say 'কয়টা বাজে?' and answer 'এখন তিনটা বাজে' (It is 3 o'clock) or 'তিনটায় দেখা করব' (We'll meet AT 3). In Spanish, notice the vital difference between stating the time (**Son las tres**) and stating an appointment time (**A las tres**). Never forget the 'A' for appointment times!",
        "vocabulary": [
            {"word": "¿Qué hora es?", "translation": "What time is it?", "pos": "phrase", "gender": None, "example": "¿Tiene hora, por favor? ¿Qué hora es?", "exampleTranslation": "Do you have the time, please? What time is it?"},
            {"word": "Es la una", "translation": "It is one o'clock (singular)", "pos": "phrase", "gender": None, "example": "Es la una en punto.", "exampleTranslation": "It is one o'clock sharp."},
            {"word": "Son las dos / tres / cuatro...", "translation": "It is two / three / four o'clock (plural)", "pos": "phrase", "gender": None, "example": "Son las cuatro de la tarde.", "exampleTranslation": "It is four in the afternoon."},
            {"word": "Y cuarto", "translation": "Quarter past (:15)", "pos": "phrase", "gender": None, "example": "Son las diez y cuarto.", "exampleTranslation": "It is ten fifteen (quarter past ten)."},
            {"word": "Y media", "translation": "Half past (:30)", "pos": "phrase", "gender": None, "example": "Son las ocho y media.", "exampleTranslation": "It is eight thirty (half past eight)."},
            {"word": "Menos cuarto", "translation": "Quarter to (:45)", "pos": "phrase", "gender": None, "example": "Son las doce menos cuarto.", "exampleTranslation": "It is a quarter to twelve (11:45)."},
            {"word": "En punto", "translation": "On the dot / Sharp", "pos": "phrase", "gender": None, "example": "La clase empieza a las nueve en punto.", "exampleTranslation": "Class starts at nine o'clock sharp."},
            {"word": "El mediodía / La medianoche", "translation": "Noon / Midnight", "pos": "noun", "gender": "masculine / feminine", "example": "Es mediodía, hora de comer.", "exampleTranslation": "It is noon, lunchtime."},
            {"word": "¿A qué hora...?", "translation": "At what time...?", "pos": "phrase", "gender": None, "example": "¿A qué hora abre la farmacia?", "exampleTranslation": "At what time does the pharmacy open?"},
            {"word": "De la mañana / de la tarde / de la noche", "translation": "In the morning / afternoon / night (with specific time)", "pos": "phrase", "gender": None, "example": "A las tres de la tarde.", "exampleTranslation": "At three in the afternoon."}
        ],
        "sentences": [
            {"spanish": "¿Qué hora es, por favor? —Son las tres y media.", "english": "What time is it, please? —It is three thirty."},
            {"spanish": "¿A qué hora empieza la película? —A las ocho y cuarto.", "english": "At what time does the movie start? —At eight fifteen."},
            {"spanish": "Es la una menos diez.", "english": "It is ten to one (12:50)."},
            {"spanish": "Tengo una reunión a las diez en punto de la mañana.", "english": "I have a meeting at ten o'clock sharp in the morning."},
            {"spanish": "El tren sale a las seis y veinticinco.", "english": "The train leaves at six twenty-five."},
            {"spanish": "En España se come alrededor de las dos y media de la tarde.", "english": "In Spain people eat around two thirty in the afternoon."}
        ],
        "grammar": {
            "title": "The Master Clock: 'Es la' vs. 'Son las' & 'A las'",
            "explanation": "Telling time in Spanish uses the verb SER because time represents an abstract identity/state.",
            "rules": [
                "Singular vs. Plural: For 1:00 to 1:59 (and noon/midnight), use singular **Es la una** (because 'hora' is singular feminine). For all other hours (2 to 12), use plural **Son las dos, Son las tres**, etc.",
                "Minutes Past (:01 to :30): Use **y**: *Son las cuatro y diez* (4:10), *Son las cuatro y cuarto* (4:15), *Son las cuatro y media* (4:30).",
                "Minutes To (:31 to :59): In Spain, use **menos** with the UPCOMING hour: *Son las cinco menos veinte* (4:40 - 20 to 5), *Son las cinco menos cuarto* (4:45 - quarter to 5).",
                "Current Time vs. Event Time: 1) What time IS it? -> *Son las cinco* (It is 5). 2) AT what time is the event? -> *A las cinco* (AT 5)."
            ],
            "structures": [
                "Current Time (1:00): Es la una + [minutos]",
                "Current Time (2:00-12:00): Son las [Hora] + y/menos + [minutos]",
                "Event Schedule: A la una / A las [Hora] + [minutos]"
            ],
            "examples": [
                {"spanish": "Es la una y cuarto.", "english": "It is 1:15."},
                {"spanish": "Son las siete menos cuarto.", "english": "It is 6:45 (quarter to 7)."},
                {"spanish": "¿A qué hora quedamos? —A las nueve.", "english": "At what time do we meet? —At 9:00."},
                {"spanish": "Son las once de la noche.", "english": "It is 11:00 PM."}
            ],
            "commonMistakes": [
                {"wrong": "Son la una", "right": "Es la una", "explanation": "1:00 is singular, so it must be 'Es la una'."},
                {"wrong": "La clase empieza las nueve (missing 'a')", "right": "La clase empieza a las nueve", "explanation": "To say 'AT [time]', you must include the preposition 'a'."}
            ],
            "proTip": "In Spain, the 24-hour digital clock (14:30, 20:00) is standard for train tickets, movie schedules, and official appointments. But in daily spoken conversation, people use the 12-hour clock with *de la mañana, de la tarde*, and *de la noche*!"
        },
        "conversation": {
            "title": "Arranging to Meet for Tapas",
            "context": "Sakib and his classmate Carlos check their watches after class.",
            "dialogue": [
                {"speaker": "Carlos", "role": "Friend", "spanish": "Sakib, ¿qué hora tienes? Mi móvil no tiene batería.", "english": "Sakib, what time do you have? My phone has no battery."},
                {"speaker": "Sakib", "role": "Student", "spanish": "Son las dos menos diez.", "english": "It is ten to two (1:50)."},
                {"speaker": "Carlos", "role": "Friend", "spanish": "¡Vaya, qué tarde! ¿A qué hora tienes tu próxima clase?", "english": "Wow, how late! At what time is your next class?"},
                {"speaker": "Sakib", "role": "Student", "spanish": "A las cuatro y media de la tarde. Tengo dos horas y media libres.", "english": "At four thirty in the afternoon. I have two and a half hours free."},
                {"speaker": "Carlos", "role": "Friend", "spanish": "¡Perfecto! ¿Vamos a comer una tapa al bar de enfrente?", "english": "Perfect! Shall we go eat a tapa at the bar opposite?"},
                {"speaker": "Sakib", "role": "Student", "spanish": "¡Sí, genial! A las dos en punto estamos allí.", "english": "Yes, great! At two o'clock sharp we'll be there."}
            ],
            "keyPhrases": [
                {"phrase": "¿Qué hora tienes?", "explanation": "Informal natural way to ask 'What time do you have?'"},
                {"phrase": "El bar de enfrente", "explanation": "'The bar opposite / across the street'."},
                {"phrase": "Horas libres", "explanation": "'Free hours / spare time'."}
            ]
        },
        "reading": {
            "title": "Los horarios y el ritmo de vida en España",
            "passage": "El ritmo horario de España es único en Europa. Debido a su posición geográfica y a sus costumbres culturales, las jornadas diarias se organizan más tarde que en otros países. Las tiendas abren a las diez de la mañana. La comida o almuerzo es entre las dos y las tres de la tarde. Muchas tiendas pequeñas cierran de dos a cinco para el descanso de mediodía. Por la tarde, la gente vuelve a trabajar hasta las ocho. Y la cena nunca es antes de las nueve o las diez de la noche. Al principio, a los extranjeros les sorprende este horario, pero pronto se acostumbran a disfrutar de las tardes largas.",
            "translation": "Spain's daily timetable is unique in Europe. Due to its geographical position and cultural customs, daily routines are organized later than in other countries. Shops open at ten in the morning. Lunch is between two and three in the afternoon. Many small shops close from two to five for the midday break. In the afternoon, people return to work until eight. And dinner is never before nine or ten at night. At first, foreigners are surprised by this schedule, but soon they get used to enjoying the long evenings.",
            "questions": [
                {"question": "¿A qué hora abren habitualmente las tiendas en España?", "options": ["A las siete", "A las ocho", "A las diez de la mañana", "A las doce"], "answer": 2, "explanation": "At 10:00 AM ('a las diez de la mañana')."},
                {"question": "¿A qué hora suele ser la cena en España?", "options": ["A las seis de la tarde", "A las siete", "Nunca antes de las nueve o diez de la noche", "A medianoche siempre"], "answer": 2, "explanation": "Never before 9 or 10 at night."},
                {"question": "¿Por qué cierran algunas tiendas pequeñas entre las dos y las cinco?", "options": ["Porque no hay luz", "Para el descanso de mediodía", "Porque tienen frío", "Por el tráfico"], "answer": 1, "explanation": "For the midday break ('para el descanso de mediodía')."}
            ]
        },
        "exercises": [
            {
                "id": "d22-ex1",
                "type": "multiple-choice",
                "prompt": "How do you say 'It is 1:00 PM' in Spanish?",
                "options": ["Son la una", "Es la una", "Está la una", "Tiene la una"],
                "correct": 1,
                "explanation": "1:00 is singular: 'Es la una'."
            },
            {
                "id": "d22-ex2",
                "type": "fill-in",
                "prompt": "Complete: La película empieza ______ (at) ocho y media.",
                "options": ["a las", "a la", "en las", "por las"],
                "correct": 0,
                "explanation": "'At [time]' is 'a las' (plural for 8:30)."
            },
            {
                "id": "d22-ex3",
                "type": "multiple-choice",
                "prompt": "What does 'Son las seis menos cuarto' mean?",
                "options": ["It is 6:15", "It is 5:45 (quarter to 6)", "It is 6:45", "It is 6:30"],
                "correct": 1,
                "explanation": "'Menos cuarto' means quarter to the upcoming hour (6:00 - 15 = 5:45)."
            },
            {
                "id": "d22-ex4",
                "type": "translation",
                "prompt": "Translate: 'It is 3:30 in the afternoon.'",
                "options": ["Son las tres y media de la tarde.", "Es las tres y media de la tarde.", "Son las tres y cuarto de la tarde.", "A las tres y media de la tarde."],
                "correct": 0,
                "explanation": "'Son las tres y media de la tarde' is the complete accurate expression."
            }
        ],
        "speakingChallenge": [
            {"prompt": "Look at your watch and say the exact current time in Spanish.", "hint": "Son las... / Es la...", "sampleAnswer": "Son las cuatro y veinte de la tarde."},
            {"prompt": "Say what time your Spanish study session starts.", "hint": "Mi sesión de estudio empieza a las...", "sampleAnswer": "Mi sesión de estudio empieza a las siete en punto de la tarde."},
            {"prompt": "Ask someone politely for the time on the street.", "hint": "Disculpe, ¿tiene hora?", "sampleAnswer": "Disculpe, señor, ¿qué hora tiene, por favor?"}
        ],
        "dailyRevision": {
            "quickQuestions": [
                "Why is 1:00 'Es la una' while 2:00 is 'Son las dos'?",
                "What is the Spanish expression for 'quarter to'?"
            ],
            "grammarRecall": "Time: Es la una (1:00) vs. Son las [2-12]. Minutes: y cuarto (:15), y media (:30), menos cuarto (:45). At [time] = A las [hora].",
            "vocabRecall": ["¿Qué hora es?", "Es la una", "Son las dos", "Y cuarto", "Y media", "Menos cuarto", "En punto", "¿A qué hora?"]
        },
        "checklist": [
            "Told time using 'Es la una' for 1:00 and 'Son las...' for 2:00–12:00",
            "Used 'y cuarto', 'y media', and 'menos cuarto' for fractions",
            "Distinguished between 'Son las cinco' (current) and 'A las cinco' (schedule)",
            "Understood Spanish cultural timetable (lunch at 2:30, dinner at 9:30)",
            "Completed all 4 time exercises",
            "Practiced asking and stating the time out loud"
        ]
    },
    {
        "day": 23,
        "stage": 3,
        "title": "Places in Town & Giving Directions",
        "subtitle": "Navigating city streets, asking directions, and locating landmarks",
        "goals": [
            "Name essential urban places (banco, farmacia, supermercado, museo, estación)",
            "Ask for directions politely using '¿Dónde está...?' and '¿Cómo puedo ir a...?'",
            "Give and understand direction commands (todo recto, a la derecha, a la izquierda, girar, cruzar)",
            "Locate landmarks using reference points (cerca, lejos, enfrente de, al lado de)"
        ],
        "bengaliNote": "Finding your way in a Spanish city is exciting! Notice how Spanish gives directions: *todo recto* (সোজা), *a la derecha* (ডানদিকে), *a la izquierda* (বামদিকে). Spaniards are famously friendly and will often walk half a block with you to show you the way!",
        "vocabulary": [
            {"word": "La calle / La avenida", "translation": "The street / The avenue", "pos": "noun", "gender": "feminine", "example": "¿Dónde está la calle Mayor?", "exampleTranslation": "Where is Mayor street?"},
            {"word": "La plaza", "translation": "The square / plaza", "pos": "noun", "gender": "feminine", "example": "Nos vemos en la Plaza del Sol.", "exampleTranslation": "We'll see each other in Sol Square."},
            {"word": "El banco / El cajero automático", "translation": "The bank / The ATM", "pos": "noun", "gender": "masculine", "example": "Necesito sacar dinero del cajero.", "exampleTranslation": "I need to withdraw money from the ATM."},
            {"word": "La farmacia", "translation": "The pharmacy / Chemist", "pos": "noun", "gender": "feminine", "example": "La farmacia tiene una cruz verde brillante.", "exampleTranslation": "The pharmacy has a bright green cross."},
            {"word": "El supermercado", "translation": "The supermarket", "pos": "noun", "gender": "masculine", "example": "Hago la compra en el supermercado.", "exampleTranslation": "I shop in the supermarket."},
            {"word": "La estación (de metro / de tren)", "translation": "The station (metro / train)", "pos": "noun", "gender": "feminine", "example": "¿Dónde está la estación de Atocha?", "exampleTranslation": "Where is Atocha station?"},
            {"word": "Todo recto", "translation": "Straight ahead", "pos": "phrase", "gender": None, "example": "Sigue todo recto dos calles.", "exampleTranslation": "Continue straight ahead two streets."},
            {"word": "A la derecha / A la izquierda", "translation": "To the right / To the left", "pos": "phrase", "gender": None, "example": "Gira a la derecha en la esquina.", "exampleTranslation": "Turn right at the corner."},
            {"word": "Girar / Cruzar", "translation": "To turn / To cross", "pos": "verb", "gender": None, "example": "Cruza la calle por el paso de peatones.", "exampleTranslation": "Cross the street at the pedestrian crossing."},
            {"word": "Cerca / Lejos", "translation": "Near / Far", "pos": "adverb", "gender": None, "example": "El museo está muy cerca, a cinco minutos.", "exampleTranslation": "The museum is very close, five minutes away."}
        ],
        "sentences": [
            {"spanish": "Disculpe, ¿dónde está la farmacia más cercana?", "english": "Excuse me, where is the nearest pharmacy?"},
            {"spanish": "Siga todo recto y gire a la derecha en la segunda calle.", "english": "Continue straight ahead and turn right at the second street. (formal)"},
            {"spanish": "¿Está lejos el Museo del Prado? —No, está muy cerca, a diez minutos a pie.", "english": "Is the Prado Museum far? —No, it is very close, ten minutes on foot."},
            {"spanish": "El banco está enfrente de la estación de metro.", "english": "The bank is opposite the metro station."},
            {"spanish": "Cruza la plaza y allí está la oficina de correos.", "english": "Cross the plaza and there is the post office."},
            {"spanish": "¿Cómo puedo ir a la Puerta del Sol?", "english": "How can I get to Puerta del Sol?"}
        ],
        "grammar": {
            "title": "Direction Imperatives & Spatial Prepositions (Cerca de / Lejos de)",
            "explanation": "Giving directions in Spanish relies on standard navigational formulas and key motion verbs (*seguir, girar, cruzar*).",
            "rules": [
                "Polite Request Opener: Always start with *Disculpe* (formal) or *Perdona* (informal) followed by *¿dónde está...?* or *¿hay una [farmacia] por aquí cerca?*.",
                "Basic Direction Commands: *Sigue todo recto* (Go straight ahead - informal) / *Siga todo recto* (formal). *Gira a la derecha / a la izquierda* (Turn right / left). *Cruza la calle / plaza* (Cross the street / square).",
                "Distance Expressions: *Cerca de* (near) / *Lejos de* (far from). Remember the contraction: *cerca de + el metro* -> *cerca del metro*!",
                "Relative Position: *Enfrente de* (in front of / opposite), *al lado de* (next to), *en la esquina* (at the corner)."
            ],
            "structures": [
                "Asking: Disculpe, ¿dónde está [Lugar]? / ¿Cómo voy a [Lugar]?",
                "Direction: Sigue todo recto + gira a la derecha/izquierda + en [Lugar]",
                "Distance: Está a [Número] minutos a pie / en metro"
            ],
            "examples": [
                {"spanish": "¿Hay un banco por aquí?", "english": "Is there a bank around here?"},
                {"spanish": "Está en la esquina, al lado de la farmacia.", "english": "It is on the corner, next to the pharmacy."},
                {"spanish": "El hotel está lejos del aeropuerto.", "english": "The hotel is far from the airport."},
                {"spanish": "Gira en la primera calle a la izquierda.", "english": "Turn at the first street on the left."}
            ],
            "commonMistakes": [
                {"wrong": "Todo derecho (meaning straight ahead in Spain)", "right": "Todo recto", "explanation": "In Spain, 'straight ahead' is 'todo recto'. ('Derecho' is heard in Latin America, but in Spain 'derecho' can be confused with 'derecha' = right)."},
                {"wrong": "Cerca de el parque", "right": "Cerca del parque", "explanation": "Contract 'de + el' to 'del'."}
            ],
            "proTip": "In Spain, pharmacies are marked by a flashing bright **green or red cross** (*cruz verde*). Even at 2 AM, there is always a designated 24-hour on-duty pharmacy (*farmacia de guardia*) in every neighborhood!"
        },
        "conversation": {
            "title": "Lost Near Plaza Mayor",
            "context": "Sakib asks a friendly local pedestrian for directions to the San Miguel Market.",
            "dialogue": [
                {"speaker": "Sakib", "role": "Traveler", "spanish": "Perdona, buenas tardes. ¿Me puedes ayudar?", "english": "Excuse me, good afternoon. Can you help me?"},
                {"speaker": "Madrileño", "role": "Local resident", "spanish": "¡Hola! Sí, claro, dime. ¿Qué buscas?", "english": "Hello! Yes, of course, tell me. What are you looking for?"},
                {"speaker": "Sakib", "role": "Traveler", "spanish": "¿Dónde está el Mercado de San Miguel? Creo que estoy un poco perdido.", "english": "Where is the San Miguel Market? I think I am a little lost."},
                {"speaker": "Madrileño", "role": "Local resident", "spanish": "No te preocupes, está facilísimo. Sigue todo recto por esta calle hasta la plaza.", "english": "Don't worry, it is super easy. Continue straight ahead along this street until the plaza."},
                {"speaker": "Sakib", "role": "Traveler", "spanish": "¿Y luego?", "english": "And then?"},
                {"speaker": "Madrileño", "role": "Local resident", "spanish": "Cruzas la plaza y giras a la derecha. Vas a ver un edificio grande de cristal y hierro. ¡Ese es!", "english": "You cross the plaza and turn right. You are going to see a large building of glass and iron. That's it!"},
                {"speaker": "Sakib", "role": "Traveler", "spanish": "¡Muchísimas gracias por tu amabilidad!", "english": "Thank you so very much for your kindness!"},
                {"speaker": "Madrileño", "role": "Local resident", "spanish": "¡De nada, hombre! ¡Que disfrutes de las tapas!", "english": "You're welcome, man! Enjoy the tapas!"}
            ],
            "keyPhrases": [
                {"phrase": "No te preocupes", "explanation": "'Don't worry' (very common comforting expression)."},
                {"phrase": "Estoy perdido(a)", "explanation": "'I am lost'."},
                {"phrase": "¡De nada, hombre!", "explanation": "Colloquial friendly Spain expression: 'You're welcome, man/mate!'"}
            ]
        },
        "reading": {
            "title": "Pasear y orientarse por el centro de Madrid",
            "passage": "El centro histórico de Madrid es un lugar magnífico para pasear a pie. Su trazado medieval combina plazas amplias con calles estrechas y llenas de historia. La Puerta del Sol es el kilómetro cero de todas las carreteras de España. Desde Sol, si caminas todo recto por la calle Mayor, llegas en pocos minutos a la majestuosa Plaza Mayor. Al lado de la plaza está el Mercado de San Miguel, un paraíso gastronómico de tapas deliciosas. Si continúas bajando por la calle Mayor, aparece el impresionante Palacio Real y la Catedral de la Almudena. En Madrid, perderse es la mejor manera de descubrir rincones mágicos.",
            "translation": "The historic center of Madrid is a magnificent place to stroll on foot. Its medieval layout combines wide squares with narrow streets full of history. Puerta del Sol is kilometer zero of all the roads of Spain. From Sol, if you walk straight ahead along Mayor street, you arrive in a few minutes at the majestic Plaza Mayor. Next to the plaza is the San Miguel Market, a gastronomic paradise of delicious tapas. If you continue down Mayor street, appears the impressive Royal Palace and the Almudena Cathedral. In Madrid, getting lost is the best way to discover magical corners.",
            "questions": [
                {"question": "¿Qué monumento representa el kilómetro cero de las carreteras de España?", "options": ["La Plaza Mayor", "La Puerta del Sol", "El Palacio Real", "La estación de Atocha"], "answer": 1, "explanation": "Puerta del Sol ('es el kilómetro cero')."},
                {"question": "¿Qué mercado gastronómico está al lado de la Plaza Mayor?", "options": ["El Mercado de San Antón", "El Mercado de San Miguel", "El Mercado de la Paz", "El Mercado de Chamberí"], "answer": 1, "explanation": "Mercado de San Miguel ('al lado de la plaza está...')."},
                {"question": "¿Qué dos monumentos aparecen al final de la calle Mayor?", "options": ["El estadio y el parque", "El Palacio Real y la Catedral de la Almudena", "Dos museos modernos", "La estación de tren"], "answer": 1, "explanation": "Royal Palace and Almudena Cathedral."}
            ]
        },
        "exercises": [
            {
                "id": "d23-ex1",
                "type": "multiple-choice",
                "prompt": "How do you say 'Straight ahead' in Spain?",
                "options": ["A la derecha", "Todo recto", "A la izquierda", "En la esquina"],
                "correct": 1,
                "explanation": "'Todo recto' is the Spain Spanish term for straight ahead."
            },
            {
                "id": "d23-ex2",
                "type": "fill-in",
                "prompt": "Complete: El banco está al lado ______ (of the) metro.",
                "options": ["del", "de el", "al", "en el"],
                "correct": 0,
                "explanation": "'de + el' contracts to 'del': 'al lado del metro'."
            },
            {
                "id": "d23-ex3",
                "type": "multiple-choice",
                "prompt": "How do you politely ask 'Where is the nearest pharmacy?'",
                "options": ["¿Dónde está la farmacia más cercana?", "¿Quién es la farmacia?", "¿Cómo cuesta la farmacia?", "¿Cuándo es la farmacia?"],
                "correct": 0,
                "explanation": "'¿Dónde está la farmacia más cercana?' asks for location politely."
            },
            {
                "id": "d23-ex4",
                "type": "translation",
                "prompt": "Translate: 'Turn left at the second street.'",
                "options": ["Gira a la izquierda en la segunda calle.", "Gira a la derecha en la segunda calle.", "Sigue todo recto en la calle.", "Cruza la calle a la izquierda."],
                "correct": 0,
                "explanation": "'Gira a la izquierda en la segunda calle' is the precise instruction."
            }
        ],
        "speakingChallenge": [
            {"prompt": "Ask someone politely where the train station is.", "hint": "Disculpe, ¿dónde está la estación...", "sampleAnswer": "Disculpe, señor, ¿dónde está la estación de tren más cercana?"},
            {"prompt": "Give simple directions: 'Go straight ahead and turn right.'", "hint": "Sigue todo recto y gira...", "sampleAnswer": "Sigue todo recto por esta calle y gira a la derecha."},
            {"prompt": "Say that you are lost and need help.", "hint": "Estoy un poco perdido...", "sampleAnswer": "Perdona, estoy un poco perdido, ¿me puedes ayudar?"}
        ],
        "dailyRevision": {
            "quickQuestions": [
                "What is the difference between 'a la derecha' and 'todo recto'?",
                "What prepositional phrase means 'opposite / across from'?"
            ],
            "grammarRecall": "Directions: Sigue todo recto, gira a la derecha/izquierda, cruza la calle. Enfrente de, al lado de, cerca de, lejos de.",
            "vocabRecall": ["La calle", "La plaza", "El banco", "La farmacia", "Todo recto", "A la derecha", "A la izquierda", "Cerca"]
        },
        "checklist": [
            "Named core urban places (calle, plaza, banco, farmacia)",
            "Understood direction commands (todo recto, gira a la derecha/izquierda)",
            "Applied spatial prepositions (enfrente de, al lado del)",
            "Read aloud the Madrid walking tour passage",
            "Passed all 4 navigation exercises",
            "Practiced asking for and giving directions out loud"
        ]
    },
    {
        "day": 24,
        "stage": 3,
        "title": "Shopping, Stores & Money",
        "subtitle": "Navigating shops, paying in cash or card, asking prices, and bargain basics",
        "goals": [
            "Master shopping vocabulary: tienda, pagar, tarjeta, efectivo, euro, céntimos",
            "Ask prices fluently using '¿Cuánto cuesta?' (singular) vs. '¿Cuánto cuestan?' (plural)",
            "Ask about payment methods (*¿Se puede pagar con tarjeta?*)",
            "Describe goods with price adjectives: caro (expensive) vs. barato (cheap)"
        ],
        "bengaliNote": "In Spain, currency is the Euro (€) divided into 100 *céntimos*. Paying with card (*con tarjeta*) or contactless phone (*contactless*) is accepted everywhere, even for a 1-euro coffee! Notice the plural rule: *¿Cuánto cuesta el libro?* (singular) vs. *¿Cuánto cuestan los zapatos?* (plural) — just like Bangla 'এটার দাম কত?' vs 'এগুলোর দাম কত?'.",
        "vocabulary": [
            {"word": "La tienda", "translation": "The shop / store", "pos": "noun", "gender": "feminine", "example": "La tienda abre a las diez.", "exampleTranslation": "The shop opens at ten."},
            {"word": "Comprar / Vender", "translation": "To buy / To sell", "pos": "verb", "gender": None, "example": "Quiero comprar una camisa nueva.", "exampleTranslation": "I want to buy a new shirt."},
            {"word": "Pagar", "translation": "To pay", "pos": "verb", "gender": None, "example": "¿Dónde se paga?", "exampleTranslation": "Where do you pay?"},
            {"word": "En efectivo / Con tarjeta", "translation": "In cash / With card", "pos": "phrase", "gender": None, "example": "¿Puedo pagar con tarjeta?", "exampleTranslation": "Can I pay with card?"},
            {"word": "El euro / El céntimo", "translation": "The euro / The cent", "pos": "noun", "gender": "masculine", "example": "Son dos euros con cincuenta céntimos.", "exampleTranslation": "It is two euros and fifty cents."},
            {"word": "¿Cuánto cuesta? / ¿Cuánto es?", "translation": "How much does it cost? / How much is it?", "pos": "phrase", "gender": None, "example": "¿Cuánto cuesta esta chaqueta?", "exampleTranslation": "How much does this jacket cost?"},
            {"word": "¿Cuánto cuestan?", "translation": "How much do they cost? (plural)", "pos": "phrase", "gender": None, "example": "¿Cuánto cuestan estos pantalones?", "exampleTranslation": "How much do these trousers cost?"},
            {"word": "Caro(a) / Barato(a)", "translation": "Expensive / Cheap", "pos": "adjective", "gender": "variable", "example": "Este restaurante no es caro, es muy barato.", "exampleTranslation": "This restaurant is not expensive, it is very cheap."},
            {"word": "La oferta / Las rebajas", "translation": "The offer, deal / The sales (discounts)", "pos": "noun", "gender": "feminine", "example": "En enero hay grandes rebajas en Madrid.", "exampleTranslation": "In January there are big sales in Madrid."},
            {"word": "El recibo / El tique", "translation": "The receipt", "pos": "noun", "gender": "masculine", "example": "Aquí tiene su recibo.", "exampleTranslation": "Here is your receipt."}
        ],
        "sentences": [
            {"spanish": "¿Cuánto cuesta esta camiseta roja?", "english": "How much does this red T-shirt cost?"},
            {"spanish": "¿Cuánto cuestan esos zapatos de cuero?", "english": "How much do those leather shoes cost?"},
            {"spanish": "¿Se puede pagar con tarjeta de crédito?", "english": "Can one pay with a credit card?"},
            {"spanish": "Sí, aceptamos tarjeta y también efectivo.", "english": "Yes, we accept card and also cash."},
            {"spanish": "Es demasiado caro para mí, ¿tienen algo más barato?", "english": "It is too expensive for me, do you have something cheaper?"},
            {"spanish": "Me lo llevo, muchas gracias.", "english": "I'll take it, thank you very much."}
        ],
        "grammar": {
            "title": "Cost Agreement: '¿Cuánto cuesta?' vs. '¿Cuánto cuestan?' & Purchasing Verbs",
            "explanation": "The verb COSTAR (to cost) is a stem-changing verb (o -> ue). Because things cost money, it is almost exclusively used in the 3rd person singular (*cuesta*) or 3rd person plural (*cuestan*).",
            "rules": [
                "Singular Item: ¿Cuánto cuesta + [Singular item]? -> *¿Cuánto cuesta este libro?* -> *Cuesta quince euros*.",
                "Plural Items: ¿Cuánto cuestan + [Plural items]? -> *¿Cuánto cuestan estos zapatos?* -> *Cuestan cincuenta euros*.",
                "Asking the Total: Simply ask: *¿Cuánto es en total?* (How much is it in total?)",
                "Payment Questions: *¿Puedo pagar con tarjeta?* (Can I pay with card?) / *¿Aceptan efectivo?* (Do you accept cash?).",
                "Taking an item: To tell the clerk you will buy an item, say: *Me lo llevo* (masculine item: I'll take it) or *Me la llevo* (feminine item)."
            ],
            "structures": [
                "Singular query: ¿Cuánto cuesta [el/la + objeto]? -> Cuesta [precio].",
                "Plural query: ¿Cuánto cuestan [los/las + objetos]? -> Cuestan [precio].",
                "Payment: Pagar en efectivo (cash) vs. Pagar con tarjeta (card)"
            ],
            "examples": [
                {"spanish": "¿Cuánto cuesta el café? —Cuesta un euro con sesenta.", "english": "How much does the coffee cost? —It costs 1.60€."},
                {"spanish": "¿Cuánto cuestan las manzanas? —Cuestan dos euros el kilo.", "english": "How much do the apples cost? —They cost 2€ a kilo."},
                {"spanish": "¿Tiene cambio de veinte euros?", "english": "Do you have change for twenty euros?"},
                {"spanish": "Me llevo esta camisa azul.", "english": "I'll take this blue shirt."}
            ],
            "commonMistakes": [
                {"wrong": "¿Cuánto cuesta los pantalones?", "right": "¿Cuánto cuestan los pantalones?", "explanation": "'Pantalones' is plural, so the verb must be plural: 'cuestan'."},
                {"wrong": "Pagar en tarjeta", "right": "Pagar con tarjeta", "explanation": "Use 'con tarjeta' (with card) and 'en efectivo' (in cash)."}
            ],
            "proTip": "In Spain, the big semi-annual sales periods are called **Las Rebajas**! They happen twice a year: Winter Rebajas (starting January 7 after Kings' Day) and Summer Rebajas (starting July 1), with discounts up to 70%!"
        },
        "conversation": {
            "title": "Buying Shoes in a Madrid Store",
            "context": "Sakib finds a nice pair of walking shoes in a shoe shop on Calle Fuencarral.",
            "dialogue": [
                {"speaker": "Dependiente", "role": "Shop clerk", "spanish": "¡Hola! Buenas tardes. ¿Busca algo en particular?", "english": "Hello! Good afternoon. Looking for anything in particular?"},
                {"speaker": "Sakib", "role": "Shopper", "spanish": "Sí, me gustan mucho estos zapatos marrones. ¿Cuánto cuestan?", "english": "Yes, I like these brown shoes a lot. How much do they cost?"},
                {"speaker": "Dependiente", "role": "Shop clerk", "spanish": "Están de oferta. Antes costaban setenta euros y ahora cuestan cuarenta y cinco.", "english": "They are on sale. Before they cost seventy euros and now they cost forty-five."},
                {"speaker": "Sakib", "role": "Shopper", "spanish": "¡Qué buen precio! ¿Tiene el número cuarenta y dos?", "english": "What a good price! Do you have size forty-two?"},
                {"speaker": "Dependiente", "role": "Shop clerk", "spanish": "Voy a mirar en el almacén... Sí, aquí tiene. Pruébeselos.", "english": "I'll look in the stockroom... Yes, here you go. Try them on."},
                {"speaker": "Sakib", "role": "Shopper", "spanish": "Son comodísimos. Me los llevo. ¿Puedo pagar con tarjeta?", "english": "They are super comfortable. I'll take them. Can I pay with card?"},
                {"speaker": "Dependiente", "role": "Shop clerk", "spanish": "Por supuesto. Acerque la tarjeta al datáfono. Muchas gracias y que los disfrute.", "english": "Of course. Tap the card on the terminal. Thank you very much and enjoy them."},
                {"speaker": "Sakib", "role": "Student", "spanish": "¡Muchas gracias! Adiós.", "english": "Thank you very much! Goodbye."}
            ],
            "keyPhrases": [
                {"phrase": "Estar de oferta", "explanation": "'To be on special offer / sale'."},
                {"phrase": "El número (de calzado)", "explanation": "Shoe size (distinct from 'la talla' for clothes)."},
                {"phrase": "El datáfono", "explanation": "The electronic POS card payment terminal in Spain."}
            ]
        },
        "reading": {
            "title": "Las compras y las rebajas en España",
            "passage": "A los españoles les gusta ir de compras y pasear por las zonas comerciales de las ciudades. En Madrid, calles peatonales como Preciados, Fuencarral y la emblemática Gran Vía están siempre llenas de gente mirando escaparates. En España, las rebajas son un acontecimiento social. Durante las rebajas de enero y julio, las tiendas ofrecen descuentos de hasta el setenta por ciento. Los compradores comparan precios, buscan gangas y renuevan su armario. Hoy en día, casi todos los comercios aceptan pagos con tarjeta o con el teléfono móvil mediante tecnología sin contacto.",
            "translation": "Spaniards enjoy going shopping and strolling through city shopping areas. In Madrid, pedestrian streets like Preciados, Fuencarral, and the iconic Gran Vía are always full of people window-shopping. In Spain, the sales are a social event. During the January and July sales, shops offer discounts of up to seventy percent. Shoppers compare prices, look for bargains, and renew their wardrobe. Nowadays, almost all businesses accept payments by card or mobile phone through contactless technology.",
            "questions": [
                {"question": "¿En qué meses son las grandes rebajas en España?", "options": ["En marzo y octubre", "En enero y julio", "Solo en diciembre", "En agosto"], "answer": 1, "explanation": "In January and July ('las rebajas de enero y julio')."},
                {"question": "¿Qué significa 'mirar escaparates'?", "options": ["Comprar comida", "Window-shopping (looking at shop windows)", "Pagar con efectivo", "Trabajar en la tienda"], "answer": 1, "explanation": "Window-shopping."},
                {"question": "¿Cómo paga casi todo el mundo hoy en día?", "options": ["Con cheques antiguos", "Con tarjeta o móvil sin contacto", "Solo con monedas de oro", "Cambiando comida"], "answer": 1, "explanation": "By card or mobile phone ('con tarjeta o con el teléfono móvil')."}
            ]
        },
        "exercises": [
            {
                "id": "d24-ex1",
                "type": "fill-in",
                "prompt": "Choose cuesta or cuestan: ¿Cuánto ______ estos dos libros?",
                "options": ["cuestan", "cuesta", "cuesto", "costar"],
                "correct": 0,
                "explanation": "Plural items take 'cuestan': '¿Cuánto cuestan estos dos libros?'."
            },
            {
                "id": "d24-ex2",
                "type": "multiple-choice",
                "prompt": "How do you say 'Can I pay with card?' in Spanish?",
                "options": ["¿Puedo pagar con tarjeta?", "¿Tengo pagar en tarjeta?", "¿Puedo comprar la tarjeta?", "¿Dónde tarjeta de pagar?"],
                "correct": 0,
                "explanation": "'¿Puedo pagar con tarjeta?' is the standard polite request."
            },
            {
                "id": "d24-ex3",
                "type": "multiple-choice",
                "prompt": "What does 'Me lo llevo' mean when shopping?",
                "options": ["I'm returning it", "I'll take it (I'm buying it)", "It is too expensive", "I don't like it"],
                "correct": 1,
                "explanation": "'Me lo llevo' means 'I'll take it / I'll buy it'."
            },
            {
                "id": "d24-ex4",
                "type": "translation",
                "prompt": "Translate: 'It is very cheap and I like it.'",
                "options": ["Es muy barato y me gusta.", "Es muy caro y me gusta.", "Está muy barato y me gusta.", "Tiene muy barato y me gusta."],
                "correct": 0,
                "explanation": "'Es muy barato y me gusta' uses 'ser' for price quality and 'gustar' for preference."
            }
        ],
        "speakingChallenge": [
            {"prompt": "Ask a store clerk how much a jacket costs.", "hint": "Disculpe, ¿cuánto cuesta esta...", "sampleAnswer": "Disculpe, ¿cuánto cuesta esta chaqueta azul?"},
            {"prompt": "Ask if you can pay with card or cash.", "hint": "¿Puedo pagar con... o en...?", "sampleAnswer": "¿Se puede pagar con tarjeta o prefieren efectivo?"},
            {"prompt": "Say: 'I like it a lot, I'll take it.'", "hint": "Me gusta mucho, me lo...", "sampleAnswer": "Me gusta mucho, es muy cómodo. Me lo llevo."}
        ],
        "dailyRevision": {
            "quickQuestions": [
                "What is the difference between '¿Cuánto cuesta?' and '¿Cuánto cuestan?'?",
                "How do you say 'cash' and 'card' in Spanish?"
            ],
            "grammarRecall": "Singular: ¿Cuánto cuesta el [objeto]? | Plural: ¿Cuánto cuestan los [objetos]? Pagar en efectivo / con tarjeta. Caro vs. barato.",
            "vocabRecall": ["La tienda", "Comprar", "Pagar", "En efectivo", "Con tarjeta", "¿Cuánto cuesta?", "Caro", "Barato", "Las rebajas"]
        },
        "checklist": [
            "Used ¿Cuánto cuesta? (singular) vs. ¿Cuánto cuestan? (plural)",
            "Asked about payment methods (con tarjeta vs. en efectivo)",
            "Learned shoe size (número) vs clothing size (talla)",
            "Used 'Me lo llevo' to confirm a purchase",
            "Completed all 4 shopping exercises",
            "Roleplayed a store purchase out loud"
        ]
    },
    {
        "day": 25,
        "stage": 3,
        "title": "Stem-Changing Verbs: E -> IE",
        "subtitle": "Conjugating Querer, Entender, Empezar, Preferir + Mid-Stage 3 Review",
        "goals": [
            "Understand the concept of Stem-Changing (Boot) Verbs in the Spanish present tense",
            "Master the E -> IE change: the vowel 'e' in the stem splits into 'ie' under stress",
            "Conjugate core verbs: querer (to want/love), entender (to understand), empezar (to begin), preferir (to prefer)",
            "Notice that Nosotros and Vosotros NEVER change stem (the boot rule!) + Mid-Stage 3 Review"
        ],
        "bengaliNote": "Spanish stem-changing verbs are called 'Boot Verbs' (Verbos bota). When the stress lands on the stem vowel 'e', it splits into two vowels: 'ie'! E.g. *querer* -> *quiero, quieres, quiere, quieren*. But outside the boot (for nosotros and vosotros: *queremos, queréis*), it stays regular. Think of it as a musical diphthongization under accent stress!",
        "vocabulary": [
            {"word": "Querer (e -> ie)", "translation": "To want / To love", "pos": "verb", "gender": None, "example": "Quiero aprender español.", "exampleTranslation": "I want to learn Spanish."},
            {"word": "Entender (e -> ie)", "translation": "To understand", "pos": "verb", "gender": None, "example": "¿Entiendes la pregunta?", "exampleTranslation": "Do you understand the question?"},
            {"word": "Empezar (e -> ie) / Comenzar", "translation": "To start / To begin", "pos": "verb", "gender": None, "example": "La clase empieza a las nueve.", "exampleTranslation": "Class starts at nine."},
            {"word": "Preferir (e -> ie)", "translation": "To prefer", "pos": "verb", "gender": None, "example": "Prefiero té en vez de café.", "exampleTranslation": "I prefer tea instead of coffee."},
            {"word": "Pensar (e -> ie)", "translation": "To think / To intend", "pos": "verb", "gender": None, "example": "¿Qué piensas de Madrid?", "exampleTranslation": "What do you think of Madrid?"},
            {"word": "Cerrar (e -> ie)", "translation": "To close", "pos": "verb", "gender": None, "example": "La tienda cierra a las ocho.", "exampleTranslation": "The shop closes at eight."},
            {"word": "Perder (e -> ie)", "translation": "To lose / To miss (a train/bus)", "pos": "verb", "gender": None, "example": "No quiero perder el tren.", "exampleTranslation": "I don't want to miss the train."},
            {"word": "Sentir (e -> ie)", "translation": "To feel / To regret (Lo siento = I'm sorry)", "pos": "verb", "gender": None, "example": "Lo siento mucho.", "exampleTranslation": "I am very sorry."},
            {"word": "Querer + infinitivo", "translation": "To want to do something", "pos": "grammar structure", "gender": None, "example": "Quiero viajar por Andalucía.", "exampleTranslation": "I want to travel through Andalusia."},
            {"word": "Pensar + infinitivo", "translation": "To plan / intend to do something", "pos": "grammar structure", "gender": None, "example": "Pienso estudiar medicina.", "exampleTranslation": "I plan to study medicine."}
        ],
        "sentences": [
            {"spanish": "Quiero hablar español con fluidez.", "english": "I want to speak Spanish fluently."},
            {"spanish": "¿Entiendes cuando los españoles hablan rápido?", "english": "Do you understand when Spanish speakers talk fast?"},
            {"spanish": "La película empieza a las siete y media.", "english": "The movie starts at seven thirty."},
            {"spanish": "Nosotros preferimos comer comida casera.", "english": "We prefer to eat homemade food. (Notice regular stem: preferimos!)"},
            {"spanish": "¿Qué quieres hacer esta tarde?", "english": "What do you want to do this afternoon?"},
            {"spanish": "Pienso visitar Barcelona el mes que viene.", "english": "I plan to visit Barcelona next month."}
        ],
        "grammar": {
            "title": "The 'Boot Verb' Rule: E -> IE Stem-Changers",
            "explanation": "In Spanish, some verbs experience a vowel fracture when the stem syllable receives spoken stress. The letter 'E' becomes 'IE'.",
            "rules": [
                "The Boot Shape: The stem change happens in 4 forms: Yo, Tú, Él/Ella/Usted, and Ellos/Ellas/Ustedes. Draw a line around these 4 forms on paper and it looks like a boot!",
                "Outside the Boot: **Nosotros** and **Vosotros** are OUTSIDE the boot because the spoken stress lands on the ending (-émos, -éis), NOT on the stem! They NEVER change: *queremos, queréis*.",
                "QUERER Conjugation: quiero | quieres | quiere | **queremos** | **queréis** | quieren.",
                "ENTENDER Conjugation: entiendo | entiendes | entiende | **entendemos** | **entendéis** | entienden.",
                "EMPEZAR Conjugation: empiezo | empiezas | empieza | **empezamos** | **empezáis** | empiezan."
            ],
            "structures": [
                "QUERER: quiero, quieres, quiere, queremos, queréis, quieren",
                "PREFERIR: prefiero, prefieres, prefiere, preferimos, preferís, prefieren",
                "Desire: Querer + [Verbo en infinitivo] (Quiero comer paella)",
                "Intention: Pensar + [Verbo en infinitivo] (Pienso viajar mañana)"
            ],
            "examples": [
                {"spanish": "Yo quiero un café con leche.", "english": "I want a coffee with milk."},
                {"spanish": "¿Entendéis vosotros la lección? (Vosotros: no stem change!)", "english": "Do you all understand the lesson?"},
                {"spanish": "Ellos prefieren viajar en tren.", "english": "They prefer to travel by train."},
                {"spanish": "¿A qué hora cierran las tiendas?", "english": "At what time do the shops close?"}
            ],
            "commonMistakes": [
                {"wrong": "Nosotros quieremos", "right": "Nosotros queremos", "explanation": "Nosotros never changes stem! It stays 'queremos'."},
                {"wrong": "Vosotros entendéis (stem changing error: entiendéis)", "right": "Vosotros entendéis", "explanation": "Vosotros never changes stem."}
            ],
            "proTip": "When using two verbs together where the first is conjugated, the second MUST remain in the infinitive: *Quiero APRENDER* (I want to learn), *Prefiero BEBER* (I prefer to drink)!"
        },
        "conversation": {
            "title": "Choosing Where to Have Dinner",
            "context": "Sakib and his friend Elena decide where to eat on Friday night.",
            "dialogue": [
                {"speaker": "Elena", "role": "Friend", "spanish": "Sakib, ¿qué quieres hacer para cenar hoy?", "english": "Sakib, what do you want to do for dinner today?"},
                {"speaker": "Sakib", "role": "Student", "spanish": "Tengo mucha hambre. ¿Prefieres comida española o comida asiática?", "english": "I am very hungry. Do you prefer Spanish food or Asian food?"},
                {"speaker": "Elena", "role": "Friend", "spanish": "Hoy prefiero tapas españolas. Conozco un bar buenísimo en La Latina.", "english": "Today I prefer Spanish tapas. I know a really good bar in La Latina."},
                {"speaker": "Sakib", "role": "Student", "spanish": "¡Perfecto! ¿A qué hora empieza a llenarse?", "english": "Perfect! At what time does it start to fill up?"},
                {"speaker": "Elena", "role": "Friend", "spanish": "Empieza a llenarse a las nueve. Si vamos a las ocho y media, encontramos mesa seguro.", "english": "It starts filling up at nine. If we go at eight thirty, we'll find a table for sure."},
                {"speaker": "Sakib", "role": "Student", "spanish": "Entiendo. Entonces nos vemos allí a las ocho y media.", "english": "I understand. Then we'll see each other there at eight thirty."}
            ],
            "keyPhrases": [
                {"phrase": "Buenísimo(a)", "explanation": "'Extremely good / wonderful'."},
                {"phrase": "Empezar a (+ infinitivo)", "explanation": "'To start / begin to [do something]'."},
                {"phrase": "Seguro", "explanation": "'For sure / safely'."}
            ]
        },
        "reading": {
            "title": "Mid-Stage 3 Review Story: Nuevos deseos y planes de Sakib",
            "passage": "Sakib lleva veinticinco días estudiando español. Ya no se siente como un extraño en Madrid. Cuando entra en una panadería, dice: «Buenos días, quiero una barra de pan, por favor». Cuando viaja en metro, entiende perfectamente los anuncios de las estaciones. Por las mañanas se levanta a las siete, se ducha y desayuna con tranquilidad. Por las tardes prefiere estudiar en el parque cuando hace sol. Piensa viajar a Granada el mes que viene para ver la Alhambra. Su profesora le dice: «Sakib, tu progreso es fantástico. Entiendes las estructuras complejas y hablas con mucha naturalidad».",
            "translation": "Sakib has been studying Spanish for twenty-five days. He no longer feels like a stranger in Madrid. When he enters a bakery, he says: 'Good morning, I want a loaf of bread, please.' When he travels by subway, he perfectly understands the station announcements. In the mornings he gets up at seven, showers, and has breakfast peacefully. In the afternoons he prefers to study in the park when it is sunny. He plans to travel to Granada next month to see the Alhambra. His teacher tells him: 'Sakib, your progress is fantastic. You understand complex structures and speak very naturally.'",
            "questions": [
                {"question": "¿Cómo se siente Sakib ahora en Madrid?", "options": ["Como un extraño", "Ya no se siente como un extraño", "Tiene miedo", "Quiere volver a casa"], "answer": 1, "explanation": "He no longer feels like a stranger ('ya no se siente como un extraño')."},
                {"question": "¿A qué ciudad piensa viajar Sakib el mes que viene?", "options": ["A Sevilla", "A Barcelona", "A Granada para ver la Alhambra", "A Valencia"], "answer": 2, "explanation": "To Granada to see the Alhambra ('piensa viajar a Granada')."},
                {"question": "¿Qué le dice su profesora?", "options": ["Que tiene que estudiar más", "Que su progreso es fantástico", "Que el examen es difícil", "Que no entiende nada"], "answer": 1, "explanation": "That his progress is fantastic ('tu progreso es fantástico')."}
            ]
        },
        "exercises": [
            {
                "id": "d25-ex1",
                "type": "fill-in",
                "prompt": "Conjugate QUERER for 'yo': Yo ______ (querer) aprender más vocabulario.",
                "options": ["quiero", "quero", "quiere", "queremos"],
                "correct": 0,
                "explanation": "Yo form changes E -> IE: 'quiero'."
            },
            {
                "id": "d25-ex2",
                "type": "fill-in",
                "prompt": "Conjugate ENTENDER for 'nosotros': Nosotros ______ (entender) la regla.",
                "options": ["entendemos", "entiendemos", "entienden", "entendéis"],
                "correct": 0,
                "explanation": "Nosotros does NOT change stem: 'entendemos'."
            },
            {
                "id": "d25-ex3",
                "type": "multiple-choice",
                "prompt": "Which forms of stem-changing verbs NEVER change their stem in the present tense?",
                "options": ["Yo and Tú", "Él and Ellos", "Nosotros and Vosotros", "Tú and Nosotros"],
                "correct": 2,
                "explanation": "Nosotros and Vosotros are outside the boot and never change their stem."
            },
            {
                "id": "d25-ex4",
                "type": "translation",
                "prompt": "Translate: 'The class starts at 9:00 AM.'",
                "options": ["La clase empieza a las nueve de la mañana.", "La clase empieza en nueve de la mañana.", "La clase empeza a las nueve.", "La clase quiero a las nueve."],
                "correct": 0,
                "explanation": "'La clase empieza a las nueve de la mañana' (empezar changes e -> ie)."
            }
        ],
        "speakingChallenge": [
            {"prompt": "Say two things you WANT to do this weekend using 'Quiero + infinitivo'.", "hint": "Este fin de semana quiero...", "sampleAnswer": "Este fin de semana quiero descansar y quiero visitar un museo."},
            {"prompt": "Say what you PREFER: coffee or tea?", "hint": "Prefiero... en vez de...", "sampleAnswer": "Prefiero té caliente con limón en vez de café."},
            {"prompt": "Conjugate QUERER aloud for all 6 persons.", "hint": "Quiero, quieres, quiere, queremos, queréis, quieren.", "sampleAnswer": "Quiero, quieres, quiere, queremos, queréis, quieren."}
        ],
        "dailyRevision": {
            "quickQuestions": [
                "What is a 'boot verb' in Spanish?",
                "Why don't 'nosotros' and 'vosotros' change their stem in verbs like querer?"
            ],
            "grammarRecall": "E -> IE Stem Changers: quiero, quieres, quiere, queremos, queréis, quieren. Infinitivo following: Quiero viajar.",
            "vocabRecall": ["Querer", "Entender", "Empezar", "Preferir", "Pensar", "Cerrar", "Perder", "Sentir"]
        },
        "checklist": [
            "Understood the concept of Boot Verbs (e -> ie)",
            "Conjugated querer, entender, empezar, preferir",
            "Preserved the regular stem for nosotros and vosotros",
            "Used 'Querer + infinitivo' and 'Pensar + infinitivo'",
            "Completed the Mid-Stage 3 review reading passage",
            "Completed all 4 stem-changing exercises"
        ]
    }
]

print(f"Loaded {len(stage3_days)} initial days for Stage 3.")
