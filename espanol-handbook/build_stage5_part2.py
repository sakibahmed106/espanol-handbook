"""
Build Stage 5: Days 46 to 50 + Combine Stage 5 into data/lessons/stage5.js
"""
import json
from build_stage5_part1 import stage5_days

stage5_part2 = [
    {
        "day": 46,
        "stage": 5,
        "title": "Introduction to the Preterite: Regular -AR Verbs",
        "subtitle": "Talking about completed past actions: hablé, hablaste, habló, hablamos, hablasteis, hablaron",
        "goals": [
            "Understand the Pretérito Indefinido (Simple Past) for completed actions in the past",
            "Master the personal endings for regular -AR verbs: -é, -aste, -ó, -amos, -asteis, -aron",
            "Notice the mandatory accent marks on the 1st person (-é) and 3rd person (-ó)",
            "Learn essential past time markers: ayer (yesterday), anoche (last night), la semana pasada"
        ],
        "bengaliNote": "Congratulations on reaching the past tense! In Bangla, past actions change the verb ending (যেমন: আমি বলেছিলাম, তুমি বলেছিলে, সে বলেছিল). In Spanish, to say what you did yesterday, drop the '-ar' and add: -é, -aste, -ó, -amos, -asteis, -aron. Notice that *habló* (he spoke - with accent) is completely different from *hablo* (I speak - no accent)!",
        "vocabulary": [
            {"word": "El pretérito (indefinido)", "translation": "The preterite (simple past tense)", "pos": "noun", "gender": "masculine", "example": "El pretérito describe acciones terminadas.", "exampleTranslation": "The preterite describes completed actions."},
            {"word": "Ayer", "translation": "Yesterday", "pos": "adverb", "gender": None, "example": "Ayer hablé con mi madre por teléfono.", "exampleTranslation": "Yesterday I spoke with my mother on the phone."},
            {"word": "Anoche", "translation": "Last night", "pos": "adverb", "gender": None, "example": "Anoche cené con unos amigos.", "exampleTranslation": "Last night I had dinner with some friends."},
            {"word": "La semana pasada / El mes pasado / El año pasado", "translation": "Last week / Last month / Last year", "pos": "phrase", "gender": "mixed", "example": "El año pasado viajé a España.", "exampleTranslation": "Last year I traveled to Spain."},
            {"word": "Hace dos días / Hace una semana", "translation": "Two days ago / A week ago", "pos": "phrase", "gender": None, "example": "Llegué a Madrid hace tres meses.", "exampleTranslation": "I arrived in Madrid three months ago."},
            {"word": "Comprar (compré, compró)", "translation": "To buy (past: I bought, he bought)", "pos": "verb", "gender": None, "example": "Ayer compré una chaqueta de abrigo.", "exampleTranslation": "Yesterday I bought a warm jacket."},
            {"word": "Trabajar (trabajé, trabajó)", "translation": "To work (past)", "pos": "verb", "gender": None, "example": "Trabajé ocho horas el lunes.", "exampleTranslation": "I worked eight hours on Monday."},
            {"word": "Estudiar (estudié, estudió)", "translation": "To study (past)", "pos": "verb", "gender": None, "example": "Estudié gramática toda la tarde.", "exampleTranslation": "I studied grammar all afternoon."},
            {"word": "Viajar (viajé, viajó)", "translation": "To travel (past)", "pos": "verb", "gender": None, "example": "El fin de semana pasado viajé a Toledo.", "exampleTranslation": "Last weekend I traveled to Toledo."},
            {"word": "Terminar (terminé, terminó)", "translation": "To finish / To end (past)", "pos": "verb", "gender": None, "example": "Terminé mis deberes a las diez.", "exampleTranslation": "I finished my homework at ten."}
        ],
        "sentences": [
            {"spanish": "Ayer hablé con mi familia en Bangladés por videollamada.", "english": "Yesterday I spoke with my family in Bangladesh on video call."},
            {"spanish": "¿Qué compraste en el mercado el sábado?", "english": "What did you buy at the market on Saturday?"},
            {"spanish": "Carlos trabajó hasta muy tarde anoche.", "english": "Carlos worked until very late last night."},
            {"spanish": "Nosotros estudiamos juntos para el examen la semana pasada.", "english": "We studied together for the exam last week."},
            {"spanish": "¿Viajasteis vosotros en tren o en autobús?", "english": "Did you all travel by train or by bus? (Spain informal plural)"},
            {"spanish": "Ellos visitaron el Museo del Prado hace dos días.", "english": "They visited the Prado Museum two days ago."}
        ],
        "grammar": {
            "title": "The Master Regular -AR Preterite Chart: -é, -aste, -ó, -amos, -asteis, -aron",
            "explanation": "The Pretérito Indefinido is used for actions that began and finished at a specific point in the past.",
            "rules": [
                "Endings for -AR Verbs: Yo -> **-é** | Tú -> **-aste** | Él/Ella/Usted -> **-ó** | Nosotros -> **-amos** | Vosotros -> **-asteis** | Ellos/Ellas/Ustedes -> **-aron**.",
                "Mandatory Written Accents: Note the critical accent marks on **-é** (yo hablé) and **-ó** (él habló). If you omit the accent on *hablo*, it means 'I speak' in the present!",
                "The Nosotros Coincidence: Notice that the 'nosotros' form for -AR verbs is IDENTICAL in both present and preterite: *hablamos* (we speak / we spoke), *estudiamos* (we study / we studied). Context tells you the time: *Hoy hablamos* (present) vs. *Ayer hablamos* (past)!",
                "Time Anchor Words: The preterite is almost always triggered by past time anchors: *ayer, anoche, el lunes pasado, hace tres días, en 2020*."
            ],
            "structures": [
                "HABLAR Pretérito: hablé | hablaste | habló | hablamos | hablasteis | hablaron",
                "TRABAJAR Pretérito: trabajé | trabajaste | trabajó | trabajamos | trabajasteis | trabajaron",
                "Past Time Anchors: Ayer (yesterday), Anoche (last night), El [mes/año] pasado, Hace [X] días"
            ],
            "examples": [
                {"spanish": "Ayer cené una tortilla española.", "english": "Yesterday I had a Spanish omelette for dinner."},
                {"spanish": "¿A qué hora terminaste los deberes?", "english": "What time did you finish the homework?"},
                {"spanish": "La profesora explicó la lección con claridad.", "english": "The teacher explained the lesson with clarity."},
                {"spanish": "Mis amigos bailaron salsa toda la noche.", "english": "My friends danced salsa all night."}
            ],
            "commonMistakes": [
                {"wrong": "Ayer hablo con Carlos (missing accent on past)", "right": "Ayer hablé con Carlos (or: Carlos habló)", "explanation": "Without the accent, 'hablo' is 1st person present. Past is 'hablé' (I) or 'habló' (he)."},
                {"wrong": "Nosotros hablemos (invented past)", "right": "Nosotros hablamos", "explanation": "The preterite of -AR for nosotros is '-amos'."}
            ],
            "proTip": "Pronunciation tip: Put a heavy vocal punch on the final accented vowels: hab-**LÉ**, ha-**BLÓ**! That sharp acoustic punch signals to any Spanish speaker that the action is done and dusted in the past."
        },
        "conversation": {
            "title": "Recapping the Weekend at Class",
            "context": "Sakib and his classmate Carlos catch up on Monday morning about their weekend.",
            "dialogue": [
                {"speaker": "Carlos", "role": "Classmate", "spanish": "¡Hola, Sakib! ¡Buenos días! ¿Qué tal el fin de semana?", "english": "Hello, Sakib! Good morning! How was the weekend?"},
                {"speaker": "Sakib", "role": "Student", "spanish": "¡Hola, Carlos! Muy bien, fue genial. El sábado viajé a Toledo en el AVE.", "english": "Hello, Carlos! Very good, it was great. On Saturday I traveled to Toledo on the AVE."},
                {"speaker": "Carlos", "role": "Classmate", "spanish": "¡Qué pasada! ¿Y qué visitaste allí?", "english": "How cool! And what did you visit there?"},
                {"speaker": "Sakib", "role": "Student", "spanish": "Caminé por todo el casco antiguo, visité la catedral gótica y compré mazapán tradicional para mis compañeros de piso.", "english": "I walked through the entire old town, visited the Gothic cathedral, and bought traditional marzipan for my flatmates."},
                {"speaker": "Carlos", "role": "Classmate", "spanish": "¿Y cenaste allí o regresaste a Madrid?", "english": "And did you have dinner there or return to Madrid?"},
                {"speaker": "Sakib", "role": "Student", "spanish": "Regresé a Madrid por la tarde y anoche cené en casa tranquilamente. ¿Y tú, qué hiciste?", "english": "I returned to Madrid in the afternoon and last night had dinner at home peacefully. And you, what did you do?"},
                {"speaker": "Carlos", "role": "Classmate", "spanish": "Yo descansé el sábado y el domingo jugué al fútbol con mis primos.", "english": "I rested on Saturday and on Sunday played football with my cousins."}
            ],
            "keyPhrases": [
                {"phrase": "¿Qué tal el fin de semana?", "explanation": "Standard Monday greeting: 'How was the weekend?'"},
                {"phrase": "Caminé por...", "explanation": "'I walked through...' (preterite of caminar)."},
                {"phrase": "Regresé a...", "explanation": "'I returned to...' (preterite of regresar)."}
            ]
        },
        "reading": {
            "title": "Mi primer viaje en tren por España",
            "passage": "El sábado pasado viví una de las experiencias más bonitas desde mi llegada a España. Me levanté temprano, preparé mi mochila y caminé hasta la estación de Atocha. Allí compré un billete de tren y viajé a Toledo. Durante el trayecto miré por la ventana los campos castellanos dorados por el sol de otoño. En Toledo paseé durante horas por sus callejones empedrados y saqué más de cincuenta fotografías. Al mediodía almorcé en una taberna tradicional: probé una sopa castellana caliente y descansé en una terraza. Por la tarde regresé a Madrid en el tren de las seis. Fue un día inolvidable que nunca voy a olvidar.",
            "translation": "Last Saturday I lived one of the most beautiful experiences since my arrival in Spain. I got up early, prepared my backpack, and walked to Atocha station. There I bought a train ticket and traveled to Toledo. During the journey I looked through the window at the Castilian fields golden with the autumn sun. In Toledo I strolled for hours through its cobblestone alleys and took more than fifty photographs. At noon I had lunch in a traditional tavern: I tried a warm Castilian soup and rested on a terrace. In the afternoon I returned to Madrid on the six o'clock train. It was an unforgettable day that I am never going to forget.",
            "questions": [
                {"question": "¿A dónde viajó Sakib el sábado pasado?", "options": ["A Barcelona", "A Toledo", "A Sevilla", "A Valencia"], "answer": 1, "explanation": "To Toledo ('viajé a Toledo')."},
                {"question": "¿Cuántas fotos sacó Sakib en Toledo?", "options": ["Dos", "Más de cincuenta fotografías", "Ninguna", "Mil"], "answer": 1, "explanation": "More than 50 photos ('más de cincuenta fotografías')."},
                {"question": "¿Qué probó al mediodía en la taberna tradicional?", "options": ["Una hamburguesa", "Una sopa castellana caliente", "Pizza fría", "Helado"], "answer": 1, "explanation": "Warm Castilian soup ('una sopa castellana caliente')."}
            ]
        },
        "exercises": [
            {
                "id": "d46-ex1",
                "type": "fill-in",
                "prompt": "Conjugate HABLAR in preterite for 'yo': Ayer yo ______ (hablar) con mi madre.",
                "options": ["hablé", "habló", "hablo", "hablaste"],
                "correct": 0,
                "explanation": "Yo form of regular -AR in the preterite is '-é': 'hablé'."
            },
            {
                "id": "d46-ex2",
                "type": "fill-in",
                "prompt": "Conjugate COMPRAR in preterite for 'él': Carlos ______ (comprar) un billete.",
                "options": ["compró", "compré", "compro", "compraste"],
                "correct": 0,
                "explanation": "Él/Ella form of regular -AR in preterite is '-ó': 'compró'."
            },
            {
                "id": "d46-ex3",
                "type": "multiple-choice",
                "prompt": "Which time word means 'last night'?",
                "options": ["Ayer", "Anoche", "Mañana", "Anteayer"],
                "correct": 1,
                "explanation": "'Anoche' means 'last night'."
            },
            {
                "id": "d46-ex4",
                "type": "translation",
                "prompt": "Translate: 'Last weekend I worked eight hours.'",
                "options": ["El fin de semana pasado trabajé ocho horas.", "El fin de semana pasado trabajo ocho horas.", "El fin de semana pasado trabajó ocho horas.", "El fin de semana pasado trabajar ocho horas."],
                "correct": 0,
                "explanation": "'El fin de semana pasado trabajé ocho horas' conjugates for 1st person past."
            }
        ],
        "speakingChallenge": [
            {"prompt": "Say what you did yesterday using an -AR preterite verb (trabajé, estudié, hablé).", "hint": "Ayer estudié español y...", "sampleAnswer": "Ayer estudié español durante dos horas y hablé con mi familia por teléfono."},
            {"prompt": "Say that you bought something last week.", "hint": "La semana pasada compré...", "sampleAnswer": "La semana pasada compré un libro de gramática en la librería del centro."},
            {"prompt": "Conjugate HABLAR in the preterite for all 6 persons out loud.", "hint": "Hablé, hablaste, habló, hablamos, hablasteis, hablaron.", "sampleAnswer": "Yo hablé, tú hablaste, él habló, nosotros hablamos, vosotros hablasteis, ellos hablaron."}
        ],
        "dailyRevision": {
            "quickQuestions": [
                "What are the 6 personal endings for -AR verbs in the preterite?",
                "Which persons carry a written accent mark in the -AR preterite? (Yo -é, Él/Ella -ó)"
            ],
            "grammarRecall": "-AR Preterite: -é, -aste, -ó, -amos, -asteis, -aron. Time anchors: ayer, anoche, el año pasado, hace dos días.",
            "vocabRecall": ["Ayer", "Anoche", "La semana pasada", "Hace dos días", "Hablé", "Compré", "Trabajé", "Viajé"]
        },
        "checklist": [
            "Conjugated regular -AR verbs in the preterite past tense",
            "Accented the 1st person (-é) and 3rd person (-ó) correctly",
            "Identified past time markers (ayer, anoche, la semana pasada)",
            "Recognized the shared 'nosotros' form (-amos) with the present",
            "Completed all 4 -AR preterite exercises",
            "Narrated a completed past action aloud in Spanish"
        ]
    },
    {
        "day": 47,
        "stage": 5,
        "title": "Preterite: Regular -ER & -IR Verbs",
        "subtitle": "Conjugating Comer, Beber, Vivir, Escribir: -í, -iste, -ió, -imos, -isteis, -ieron",
        "goals": [
            "Conjugate regular -ER verbs in the preterite (comí, comiste, comió, comimos, comisteis, comieron)",
            "Conjugate regular -IR verbs in the preterite (viví, viviste, vivió, vivimos, vivisteis, vivieron)",
            "Notice the fantastic news: -ER and -IR have 100% IDENTICAL endings in the preterite!",
            "Combine -AR, -ER, and -IR verbs into fluent past-tense stories"
        ],
        "bengaliNote": "Here is one of the greatest gifts in Spanish grammar: while -ER and -IR had slightly different endings in the present tense, in the preterite past tense, their endings are **100% identical across all six persons**! Drop the '-er' or '-ir' and add: -í, -iste, -ió, -imos, -isteis, -ieron. You only have to memorize ONE single set of endings for both verb families!",
        "vocabulary": [
            {"word": "Comer (comí, comió)", "translation": "To eat (past: I ate, he ate)", "pos": "verb", "gender": None, "example": "Ayer comí paella con mis amigos.", "exampleTranslation": "Yesterday I ate paella with my friends."},
            {"word": "Beber (bebí, bebió)", "translation": "To drink (past)", "pos": "verb", "gender": None, "example": "Bebí mucha agua después de correr.", "exampleTranslation": "I drank a lot of water after running."},
            {"word": "Vivir (viví, vivió)", "translation": "To live (past)", "pos": "verb", "gender": None, "example": "Viví en Daca durante muchos años.", "exampleTranslation": "I lived in Dhaka for many years."},
            {"word": "Escribir (escribí, escribió)", "translation": "To write (past)", "pos": "verb", "gender": None, "example": "Escribí un correo al profesor.", "exampleTranslation": "I wrote an email to the teacher."},
            {"word": "Aprender (aprendí, aprendió)", "translation": "To learn (past)", "pos": "verb", "gender": None, "example": "Ayer aprendí diez verbos nuevos.", "exampleTranslation": "Yesterday I learned ten new verbs."},
            {"word": "Comprender (comprendí, comprendió)", "translation": "To understand (past)", "pos": "verb", "gender": None, "example": "Comprendí toda la lección de gramática.", "exampleTranslation": "I understood the entire grammar lesson."},
            {"word": "Abrir (abrí, abrió)", "translation": "To open (past)", "pos": "verb", "gender": None, "example": "Abrí la ventana para ventilar.", "exampleTranslation": "I opened the window to air out."},
            {"word": "Salir (salí, salió)", "translation": "To go out / leave (past)", "pos": "verb", "gender": None, "example": "Salí de casa a las ocho.", "exampleTranslation": "I left home at eight."},
            {"word": "Decidir (decidí, decidió)", "translation": "To decide (past)", "pos": "verb", "gender": None, "example": "Decidí estudiar español en Madrid.", "exampleTranslation": "I decided to study Spanish in Madrid."},
            {"word": "Nacer (nací, nació)", "translation": "To be born (past: I was born)", "pos": "verb", "gender": None, "example": "Nací en Bangladés en 1999.", "exampleTranslation": "I was born in Bangladesh in 1999."}
        ],
        "sentences": [
            {"spanish": "Ayer comí en un restaurante tradicional y bebí zumo de naranja.", "english": "Yesterday I ate at a traditional restaurant and drank orange juice."},
            {"spanish": "Nací en Bangladés y viví allí hasta los veintitrés años.", "english": "I was born in Bangladesh and lived there until twenty-three years old."},
            {"spanish": "¿Qué escribiste en tu diario de viaje anoche?", "english": "What did you write in your travel diary last night?"},
            {"spanish": "Nosotros aprendimos muchísimas palabras la semana pasada.", "english": "We learned so many words last week."},
            {"spanish": "El museo abrió sus puertas a las diez en punto.", "english": "The museum opened its doors at ten o'clock sharp."},
            {"spanish": "¿Salisteis vosotros el sábado por la noche?", "english": "Did you all go out on Saturday night? (Spain informal plural)"}
        ],
        "grammar": {
            "title": "The Unified -ER / -IR Preterite Chart: -í, -iste, -ió, -imos, -isteis, -ieron",
            "explanation": "Remember: -ER and -IR verbs share the EXACT SAME endings in the preterite simple past!",
            "rules": [
                "The Shared -ER / -IR Preterite Endings: Yo -> **-í** | Tú -> **-iste** | Él/Ella/Usted -> **-ió** | Nosotros -> **-imos** | Vosotros -> **-isteis** | Ellos/Ellas/Ustedes -> **-ieron**.",
                "Mandatory Written Accents: Note the tildes on the 1st person singular (**-í**) and 3rd person singular (**-ió**): *comí, comió*, *viví, vivió*.",
                "Stating Birth: In Spanish, 'I was born' is expressed with the single preterite verb **Nací** (from nacer): *Nací en Bangladés* (NOT *Fui nacido*!).",
                "The -IR Nosotros Coincidence: For -IR verbs, the 'nosotros' form (*vivimos*, *escribimos*) is identical in both present and preterite, just like -AR (*hablamos*)!"
            ],
            "structures": [
                "COMER: comí | comiste | comió | comimos | comisteis | comieron",
                "VIVIR: viví | viviste | vivió | vivimos | vivisteis | vivieron",
                "Birth formula: Nací en [Año / Lugar] (Nací en 1998 en Daca)"
            ],
            "examples": [
                {"spanish": "Comí una ensalada deliciosa.", "english": "I ate a delicious salad."},
                {"spanish": "Ella vivió en Barcelona dos años.", "english": "She lived in Barcelona for two years."},
                {"spanish": "¿Comprendiste la explicación del profesor?", "english": "Did you understand the teacher's explanation?"},
                {"spanish": "Ellos salieron muy temprano por la mañana.", "english": "They went out very early in the morning."}
            ],
            "commonMistakes": [
                {"wrong": "Yo fui nacido en 2000", "right": "Nací en 2000", "explanation": "Spanish uses the preterite of nacer: 'Nací'."},
                {"wrong": "Él comió sin tilde (comio)", "right": "Él comió", "explanation": "The 3rd person singular preterite strictly requires the accent on the -ó."}
            ],
            "proTip": "Contrast -AR vs. -ER/-IR: -AR uses the letter 'A' heavily (*hablaste, hablaron*). -ER and -IR use the vowel combination 'I' and 'IO' heavily (*comiste, comieron, comió*)!"
        },
        "conversation": {
            "title": "Talking About Personal Backgrounds",
            "context": "Sakib and his friend Sophie discuss where they grew up and their past studies.",
            "dialogue": [
                {"speaker": "Sophie", "role": "Friend", "spanish": "Sakib, ¿dónde naciste exactamente?", "english": "Sakib, where exactly were you born?"},
                {"speaker": "Sakib", "role": "Student", "spanish": "Nací en Bangladés y viví en la capital con mi familia. ¿Y tú, Sophie?", "english": "I was born in Bangladesh and lived in the capital with my family. And you, Sophie?"},
                {"speaker": "Sophie", "role": "Friend", "spanish": "Yo nací en Lyon, en Francia, pero el año pasado viví en Italia durante seis meses.", "english": "I was born in Lyon, France, but last year I lived in Italy for six months."},
                {"speaker": "Sakib", "role": "Student", "spanish": "¡Qué viajera! ¿Y aprendiste italiano allí?", "english": "What a traveler! And did you learn Italian there?"},
                {"speaker": "Sophie", "role": "Friend", "spanish": "Sí, aprendí bastante porque comí todos los días con gente local y salí mucho con amigos italianos.", "english": "Yes, I learned quite a bit because I ate every day with local people and went out a lot with Italian friends."},
                {"speaker": "Sakib", "role": "Student", "spanish": "Es la mejor manera. Yo decidí venir a Madrid por la misma razón: para vivir el idioma en la calle.", "english": "It is the best way. I decided to come to Madrid for the same reason: to live the language in the street."}
            ],
            "keyPhrases": [
                {"phrase": "¿Dónde naciste?", "explanation": "'Where were you born?'"},
                {"phrase": "Aprendí bastante", "explanation": "'I learned quite a bit'."},
                {"phrase": "Decidí venir", "explanation": "'I decided to come'."}
            ]
        },
        "reading": {
            "title": "La historia personal de Sakib",
            "passage": "Sakib nació en Bangladés en una familia amorosa y trabajadora. Creció rodeado de libros, música tradicional y conversaciones animadas. En su país estudió con dedicación y aprendió inglés con fluidez. Sin embargo, siempre sintió una gran atracción por la lengua española y la rica historia de España. El año pasado tomó una decisión valiente: organizó sus documentos, solicitó su visado y se mudó a Madrid. Cuando llegó a España, apenas conocía unas pocas palabras; pero gracias a su constancia diaria, comprendió la gramática, escribió oraciones complejas y salió a conversar con la gente en mercados y cafeterías. Hoy mira hacia atrás y sonríe: cada esfuerzo valió la pena.",
            "translation": "Sakib was born in Bangladesh in a loving and hardworking family. He grew up surrounded by books, traditional music, and lively conversations. In his country he studied with dedication and learned English fluently. However, he always felt a great attraction to the Spanish language and the rich history of Spain. Last year he made a brave decision: he organized his documents, applied for his visa, and moved to Madrid. When he arrived in Spain, he barely knew a few words; but thanks to his daily consistency, he understood grammar, wrote complex sentences, and went out to chat with people in markets and cafés. Today he looks back and smiles: every effort was worth it.",
            "questions": [
                {"question": "¿Dónde nació y creció Sakib?", "options": ["En Francia", "En Bangladés", "En Madrid", "En Italia"], "answer": 1, "explanation": "In Bangladesh ('nació en Bangladés')."},
                {"question": "¿Qué decisión tomó Sakib el año pasado?", "options": ["Comprar una casa grande", "Mudarse a Madrid para estudiar español", "Dejar de estudiar", "Cambiar de profesión"], "answer": 1, "explanation": "Moved to Madrid to study Spanish ('se mudó a Madrid')."},
                {"question": "¿Qué hacía Sakib al llegar a España?", "options": ["Apenas conocía unas pocas palabras", "Hablaba como un nativo C2", "No salía nunca de su habitación", "No quería hablar con nadie"], "answer": 0, "explanation": "He barely knew a few words ('apenas conocía unas pocas palabras')."}
            ]
        },
        "exercises": [
            {
                "id": "d47-ex1",
                "type": "fill-in",
                "prompt": "Conjugate COMER in preterite for 'yo': Anoche yo ______ (comer) paella.",
                "options": ["comí", "comió", "como", "comiste"],
                "correct": 0,
                "explanation": "Yo form of regular -ER in preterite is '-í': 'comí'."
            },
            {
                "id": "d47-ex2",
                "type": "fill-in",
                "prompt": "How do you say 'I was born in 2000' in Spanish?",
                "options": ["Nací en 2000", "Fui nacido en 2000", "Estuve nacido en 2000", "Nació en 2000"],
                "correct": 0,
                "explanation": "'Nací en 2000' is the single authentic past verb for birth."
            },
            {
                "id": "d47-ex3",
                "type": "multiple-choice",
                "prompt": "Are the preterite endings for -ER and -IR verbs different or identical?",
                "options": ["Completely different", "100% identical in all 6 persons", "Only identical in yo", "Only identical in nosotros"],
                "correct": 1,
                "explanation": "-ER and -IR share identical preterite endings across all 6 persons (-í, -iste, -ió, -imos, -isteis, -ieron)."
            },
            {
                "id": "d47-ex4",
                "type": "translation",
                "prompt": "Translate: 'Yesterday we learned many new words.'",
                "options": ["Ayer aprendimos muchas palabras nuevas.", "Ayer aprendieron muchas palabras nuevas.", "Ayer aprendemos muchas palabras nuevas.", "Ayer aprendí muchas palabras nuevas."],
                "correct": 0,
                "explanation": "'Ayer aprendimos muchas palabras nuevas' conjugates for nosotros in the preterite."
            }
        ],
        "speakingChallenge": [
            {"prompt": "Say what year and country you were born in.", "hint": "Nací en [año] en [país]...", "sampleAnswer": "Nací en Bangladés y crecí en una ciudad maravillosa."},
            {"prompt": "Say what you ate and drank yesterday evening.", "hint": "Anoche comí... y bebí...", "sampleAnswer": "Anoche comí arroz con pollo y bebí agua mineral fría."},
            {"prompt": "Conjugate COMER and VIVIR in the preterite for 'yo' and 'él'.", "hint": "Comí / comió; viví / vivió.", "sampleAnswer": "Yo comí y él comió; yo viví y él vivió."}
        ],
        "dailyRevision": {
            "quickQuestions": [
                "What are the 6 personal endings for -ER and -IR verbs in the preterite?",
                "How do you say 'I was born' in Spanish? (Nací)"
            ],
            "grammarRecall": "-ER / -IR Preterite: -í, -iste, -ió, -imos, -isteis, -ieron. Both families share the exact same endings. Nací.",
            "vocabRecall": ["Comí", "Bebí", "Viví", "Escribí", "Aprendí", "Nací", "Decidí", "Salí"]
        },
        "checklist": [
            "Conjugated regular -ER verbs in the preterite past tense",
            "Conjugated regular -IR verbs in the preterite past tense",
            "Recognized that -ER and -IR endings are 100% identical in the preterite",
            "Stated birthplace and birth year with 'Nací en...'",
            "Completed all 4 -ER/-IR preterite exercises",
            "Narrated personal background milestones aloud in Spanish"
        ]
    },
    {
        "day": 48,
        "stage": 5,
        "title": "Essential Irregular Preterite: FUI & ESTUVE",
        "subtitle": "Mastering the past of IR/SER (fui, fuiste, fue...) and ESTAR (estuve, estuviste, estuvo...)",
        "goals": [
            "Learn the mind-blowing Spanish linguistic fact: IR (to go) and SER (to be) share the EXACT SAME preterite conjugation!",
            "Conjugate FUI: fui, fuiste, fue, fuimos, fuisteis, fueron",
            "Conjugate ESTUVE: estuve, estuviste, estuvo, estuvimos, estuvisteis, estuvieron",
            "Distinguish between 'Fue' (it was) and 'Estuvo' (it was located / condition was)"
        ],
        "bengaliNote": "Here is one of the most fascinating features of the Spanish language: the verb **IR** (to go) and the verb **SER** (to be) merge into the EXACT SAME identical twins in the preterite! *Yo fui a Madrid* = I went to Madrid (IR). *La fiesta fue genial* = The party was great (SER). Context instantly makes the meaning obvious!",
        "vocabulary": [
            {"word": "Fui, Fuiste, Fue", "translation": "I went / I was; you went / you were; he went / he was", "pos": "irregular verb form", "gender": None, "example": "Ayer fui al centro de Madrid.", "exampleTranslation": "Yesterday I went to the center of Madrid (IR)."},
            {"word": "Fuimos, Fuisteis, Fueron", "translation": "We went / were; you all went / were; they went / were", "pos": "irregular verb form", "gender": None, "example": "Fuimos al cine juntos.", "exampleTranslation": "We went to the cinema together."},
            {"word": "Estuve, Estuviste, Estuvo", "translation": "I was (state/location); you were; he/she was", "pos": "irregular verb form", "gender": None, "example": "Ayer estuve en casa todo el día.", "exampleTranslation": "Yesterday I was at home all day (ESTAR)."},
            {"word": "Estuvimos, Estuvisteis, Estuvieron", "translation": "We were; you all were; they were (ESTAR)", "pos": "irregular verb form", "gender": None, "example": "Estuvimos muy cansados después del viaje.", "exampleTranslation": "We were very tired after the trip."},
            {"word": "Fue increíble / genial / maravilloso", "translation": "It was incredible / great / wonderful", "pos": "phrase", "gender": None, "example": "El concierto fue increíble.", "exampleTranslation": "The concert was incredible (SER: evaluation of event)."},
            {"word": "El fin de semana pasado", "translation": "Last weekend", "pos": "phrase", "gender": "masculine", "example": "El fin de semana pasado estuve en Sevilla.", "exampleTranslation": "Last weekend I was in Seville."},
            {"word": "Todo el día / Toda la noche", "translation": "All day / All night", "pos": "phrase", "gender": "mixed", "example": "Estuve estudiando todo el día.", "exampleTranslation": "I was studying all day."},
            {"word": "¿Cómo fue?", "translation": "How was it? / How did it go?", "pos": "phrase", "gender": None, "example": "¿Cómo fue tu examen de español?", "exampleTranslation": "How was your Spanish exam?"},
            {"word": "¿Dónde estuviste?", "translation": "Where were you?", "pos": "phrase", "gender": None, "example": "¿Dónde estuviste ayer por la tarde?", "exampleTranslation": "Where were you yesterday afternoon?"},
            {"word": "Un viaje inolvidable", "translation": "An unforgettable trip", "pos": "phrase", "gender": "masculine", "example": "Fue un viaje inolvidable para mí.", "exampleTranslation": "It was an unforgettable trip for me."}
        ],
        "sentences": [
            {"spanish": "El sábado fui al Museo del Prado con unos amigos.", "english": "On Saturday I went to the Prado Museum with some friends. (IR)"},
            {"spanish": "La película fue muy interesante y emocionante.", "english": "The movie was very interesting and emotional. (SER)"},
            {"spanish": "Ayer estuve en la biblioteca desde las diez hasta las dos.", "english": "Yesterday I was in the library from ten until two. (ESTAR: location)"},
            {"spanish": "¿Dónde estuviste anoche? Te llamé por teléfono.", "english": "Where were you last night? I called you on the phone. (ESTAR)"},
            {"spanish": "El examen de gramática fue bastante fácil.", "english": "The grammar exam was quite easy. (SER)"},
            {"spanish": "Estuvimos muy contentos con los resultados de la prueba.", "english": "We were very happy with the test results. (ESTAR: emotion)"}
        ],
        "grammar": {
            "title": "The IR/SER Twin Miracle (FUI) & The ESTAR Preterite (ESTUVE)",
            "explanation": "These are the two most frequently used irregular verbs in the entire Spanish past tense. Memorize them completely:",
            "rules": [
                "1. IR and SER Preterite Conjugation (The Twin Verb): **fui | fuiste | fue | fuimos | fuisteis | fueron**.",
                "How to tell IR from SER? Look at what follows: 1) If followed by 'a' + place, it is **IR** (*Fui a Madrid* = I went to Madrid). 2) If followed by an adjective or describing an event, it is **SER** (*La fiesta fue genial* = The party was great).",
                "2. ESTAR Preterite Conjugation: **estuve | estuviste | estuvo | estuvimos | estuvisteis | estuvieron**.",
                "No Accents on Irregular Preterites! Notice that neither *fui*, *fue*, *estuve*, nor *estuvo* have written accents! Irregular preterite stems are naturally stressed on the penult.",
                "FUE vs. ESTUVO: Use **FUE** to evaluate an event or experience (*La clase fue divertida*). Use **ESTUVO** for location (*Estuve en el parque*) or temporary conditions (*La comida estuvo rica*)."
            ],
            "structures": [
                "IR / SER Pretérito: fui | fuiste | fue | fuimos | fuisteis | fueron",
                "ESTAR Pretérito: estuve | estuviste | estuvo | estuvimos | estuvisteis | estuvieron",
                "Evaluation of event: [Evento] + fue + genial / difícil / divertido"
            ],
            "examples": [
                {"spanish": "Fui a la playa. (IR: Destination)", "english": "I went to the beach."},
                {"spanish": "El viaje fue maravilloso. (SER: Trait of event)", "english": "The trip was wonderful."},
                {"spanish": "Estuve enfermo dos días. (ESTAR: Condition)", "english": "I was sick for two days."},
                {"spanish": "¿Fuisteis vosotros a la fiesta?", "english": "Did you all go to the party?"}
            ],
            "commonMistakes": [
                {"wrong": "Yo fue a Madrid", "right": "Yo fui a Madrid", "explanation": "Yo form is 'fui'. 'Fue' is 3rd person (él/ella/usted)."},
                {"wrong": "Estuvé con tilde", "right": "Estuve (sin tilde)", "explanation": "Irregular preterite forms like 'estuve' and 'estuvo' do NOT carry accent marks."}
            ],
            "proTip": "To ask a friend how any past event, trip, date, or exam went, use the magic formula: **«¿Cómo fue?»** (How was it?). And the standard happy reply: **«¡Fue genial!»** (It was great!)."
        },
        "conversation": {
            "title": "How Did the Weekend Go?",
            "context": "Sakib and his friend Lucía talk about their respective weekends over a morning tea.",
            "dialogue": [
                {"speaker": "Lucía", "role": "Friend", "spanish": "¡Hola, Sakib! No te vi el sábado. ¿Dónde estuviste?", "english": "Hello, Sakib! I didn't see you Saturday. Where were you?"},
                {"speaker": "Sakib", "role": "Student", "spanish": "¡Hola, Lucía! El sábado fui a Segovia de excursión con unos compañeros.", "english": "Hello, Lucia! On Saturday I went to Segovia on a day trip with some classmates."},
                {"speaker": "Lucía", "role": "Friend", "spanish": "¡Qué bien! ¿Y cómo fue el viaje?", "english": "How nice! And how was the trip?"},
                {"speaker": "Sakib", "role": "Student", "spanish": "¡Fue increíble! El acueducto romano es impresionante y el Alcázar fue como un sueño. Estuvimos caminando todo el día.", "english": "It was incredible! The Roman aqueduct is impressive and the Alcazar was like a dream. We were walking all day."},
                {"speaker": "Lucía", "role": "Friend", "spanish": "¿Y el domingo qué hiciste?", "english": "And on Sunday what did you do?"},
                {"speaker": "Sakib", "role": "Student", "spanish": "El domingo estuve descansando en casa porque estaba agotado. ¿Y tú, fuiste a ver a tu familia?", "english": "On Sunday I was resting at home because I was exhausted. And you, did you go see your family?"},
                {"speaker": "Lucía", "role": "Friend", "spanish": "Sí, fui a casa de mis padres y comimos una paella riquísima.", "english": "Yes, I went to my parents' house and we ate a delicious paella."}
            ],
            "keyPhrases": [
                {"phrase": "¿Cómo fue el viaje?", "explanation": "'How was the trip?'"},
                {"phrase": "Fue increíble", "explanation": "'It was incredible'."},
                {"phrase": "Estuve descansando", "explanation": "'I was resting'."}
            ]
        },
        "reading": {
            "title": "Un fin de semana inolvidable",
            "passage": "El fin de semana pasado fue muy especial para Sakib. El viernes por la tarde terminó todas sus tareas pendientes para tener el sábado completamente libre. El sábado por la mañana fue a la estación con sus amigos y tomaron el tren hacia Segovia. El tiempo fue perfecto: el cielo estuvo despejado y no hizo nada de frío. Estuvieron en Segovia más de ocho horas explorando monumentos, tomando fotografías y disfrutando de la gastronomía local. La comida en el restaurante tradicional fue espectacular. Por la noche regresaron a Madrid. Sakib estuvo muy cansado físicamente, pero mentalmente lleno de inspiración y felicidad. Fue, sin duda, una de las mejores decisiones de su estancia en España.",
            "translation": "Last weekend was very special for Sakib. On Friday afternoon he finished all his pending tasks to have Saturday completely free. On Saturday morning he went to the station with his friends and they took the train to Segovia. The weather was perfect: the sky was clear and it was not cold at all. They were in Segovia for more than eight hours exploring monuments, taking photographs, and enjoying local gastronomy. The meal in the traditional restaurant was spectacular. At night they returned to Madrid. Sakib was very tired physically, but mentally full of inspiration and happiness. It was, without doubt, one of the best decisions of his stay in Spain.",
            "questions": [
                {"question": "¿A dónde fue Sakib el sábado por la mañana?", "options": ["Al aeropuerto", "A la estación con sus amigos para ir a Segovia", "A la biblioteca solo", "Al hospital"], "answer": 1, "explanation": "To the station to go to Segovia ('fue a la estación...')."},
                {"question": "¿Cómo estuvo el cielo durante la excursión?", "options": ["Lleno de nieve", "Despejado y sin frío", "Lloviendo todo el día", "Oscuro"], "answer": 1, "explanation": "Clear and not cold ('estuvo despejado y no hizo nada de frío')."},
                {"question": "¿Cómo fue la comida en el restaurante tradicional?", "options": ["Fue mala", "Fue espectacular", "No comieron nada", "Fue fría"], "answer": 1, "explanation": "It was spectacular ('fue espectacular')."}
            ]
        },
        "exercises": [
            {
                "id": "d48-ex1",
                "type": "fill-in",
                "prompt": "Conjugate IR/SER in preterite for 'yo': Ayer yo ______ (went) al supermercado.",
                "options": ["fui", "fue", "fuiste", "fuimos"],
                "correct": 0,
                "explanation": "Yo form of IR in preterite is 'fui'."
            },
            {
                "id": "d48-ex2",
                "type": "fill-in",
                "prompt": "Conjugate ESTAR in preterite for 'yo': Anoche yo ______ (was) en casa.",
                "options": ["estuve", "estuvo", "estuviste", "estuvimos"],
                "correct": 0,
                "explanation": "Yo form of ESTAR in preterite is 'estuve'."
            },
            {
                "id": "d48-ex3",
                "type": "multiple-choice",
                "prompt": "Which two Spanish verbs share the exact same preterite conjugation (fui, fuiste, fue...)?",
                "options": ["Tener and Hacer", "IR and SER", "Estar and Haber", "Comer and Vivir"],
                "correct": 1,
                "explanation": "IR and SER share the exact identical preterite conjugation."
            },
            {
                "id": "d48-ex4",
                "type": "translation",
                "prompt": "Translate: 'How was the exam? —It was very easy.'",
                "options": ["¿Cómo fue el examen? —Fue muy fácil.", "¿Cómo estuvo el examen? —Estuvo muy fácil.", "¿Dónde fue el examen? —Fue fácil.", "¿Cuándo fue el examen? —Fue fácil."],
                "correct": 0,
                "explanation": "'¿Cómo fue el examen? —Fue muy fácil' uses SER (fue) to evaluate an event."
            }
        ],
        "speakingChallenge": [
            {"prompt": "Say where you went yesterday using 'Fui a...'", "hint": "Ayer fui a...", "sampleAnswer": "Ayer fui al supermercado y luego fui al parque a caminar un rato."},
            {"prompt": "Say where you were last night using 'Estuve en...'", "hint": "Anoche estuve en...", "sampleAnswer": "Anoche estuve en mi casa descansando y leyendo en español."},
            {"prompt": "Evaluate a past experience: say 'It was great / It was wonderful.'", "hint": "Fue genial / Fue maravilloso.", "sampleAnswer": "El fin de semana pasado fue maravilloso e inolvidable."}
        ],
        "dailyRevision": {
            "quickQuestions": [
                "What two verbs conjugate as 'fui, fuiste, fue, fuimos, fuisteis, fueron'?",
                "Do irregular preterite forms like 'fui' or 'estuve' take accent marks? (No!)"
            ],
            "grammarRecall": "IR/SER: fui, fuiste, fue, fuimos, fuisteis, fueron. ESTAR: estuve, estuviste, estuvo, estuvimos, estuvisteis, estuvieron. ¿Cómo fue? ¡Fue genial!",
            "vocabRecall": ["Fui", "Fue", "Fuimos", "Estuve", "Estuvo", "Estuvimos", "¿Cómo fue?", "Fue genial"]
        },
        "checklist": [
            "Conjugated the twin verb IR/SER in the preterite (fui, fuiste, fue...)",
            "Conjugated ESTAR in the preterite (estuve, estuviste, estuvo...)",
            "Distinguished IR (movement) from SER (evaluation) in context",
            "Used '¿Cómo fue?' and '¡Fue genial!' in conversation",
            "Completed all 4 irregular preterite exercises",
            "Narrated past locations and experiences aloud in Spanish"
        ]
    },
    {
        "day": 49,
        "stage": 5,
        "title": "Short Stories & Narrative Past Reading",
        "subtitle": "Reading and constructing narratives: 'Un fin de semana inolvidable en Sevilla'",
        "goals": [
            "Read and comprehend a full-length beginner narrative passage in the past tense",
            "Understand narrative sequencing words: *primero, luego, después, más tarde, al final*",
            "Combine past actions (preterite) with descriptions (ser/estar)",
            "Identify key story elements: characters, plot, setting, climax, resolution"
        ],
        "bengaliNote": "Storytelling is the pinnacle of language learning! In Bangla literature and adda (আড্ডা), we weave past actions with vivid descriptions. Today, you will experience a complete, authentic Spanish short story, seeing how all the verbs you've mastered come together like instruments in an orchestra.",
        "vocabulary": [
            {"word": "El cuento / La historia", "translation": "The short story / The history, story", "pos": "noun", "gender": "masculine / feminine", "example": "Leo una historia emocionante.", "exampleTranslation": "I read an exciting story."},
            {"word": "El viaje inolvidable", "translation": "The unforgettable trip", "pos": "phrase", "gender": "masculine", "example": "Sevilla fue un viaje inolvidable.", "exampleTranslation": "Seville was an unforgettable trip."},
            {"word": "Llegar a (llegué, llegó)", "translation": "To arrive at (past)", "pos": "verb", "gender": None, "example": "Llegamos a Sevilla al mediodía.", "exampleTranslation": "We arrived in Seville at noon."},
            {"word": "Descubrir (descubrí, descubrió)", "translation": "To discover (past)", "pos": "verb", "gender": None, "example": "Descubrí rincones mágicos en la ciudad.", "exampleTranslation": "I discovered magical corners in the city."},
            {"word": "Disfrutar de (disfruté, disfrutó)", "translation": "To enjoy (past)", "pos": "verb", "gender": None, "example": "Disfruté de la música flamenca.", "exampleTranslation": "I enjoyed the flamenco music."},
            {"word": "Perderse (me perdí, se perdió)", "translation": "To get lost (past)", "pos": "reflexive verb", "gender": None, "example": "Me perdí por las calles del barrio de Santa Cruz.", "exampleTranslation": "I got lost in the streets of Santa Cruz quarter."},
            {"word": "Al principio / Al final", "translation": "At the beginning / In the end, at last", "pos": "phrase", "gender": None, "example": "Al final todo salió perfecto.", "exampleTranslation": "In the end everything turned out perfect."},
            {"word": "De repente", "translation": "Suddenly", "pos": "phrase", "gender": None, "example": "De repente empezó a sonar una guitarra.", "exampleTranslation": "Suddenly a guitar began to play."},
            {"word": "El recuerdo / Recordar", "translation": "The memory, souvenir / To remember", "pos": "noun / verb", "gender": "masculine", "example": "Tengo recuerdos preciosos de ese viaje.", "exampleTranslation": "I have precious memories of that trip."},
            {"word": "Recomendar (recomiendo, recomendé)", "translation": "To recommend", "pos": "verb", "gender": None, "example": "Recomiendo visitar Andalucía.", "exampleTranslation": "I recommend visiting Andalusia."}
        ],
        "sentences": [
            {"spanish": "El mes pasado viajé a Sevilla en tren de alta velocidad.", "english": "Last month I traveled to Seville by high-speed train."},
            {"spanish": "Cuando llegué a la estación de Santa Justa, hacía un sol radiante.", "english": "When I arrived at Santa Justa station, the sun was radiant."},
            {"spanish": "Primero visité la Plaza de España y me quedé sin palabras ante su belleza.", "english": "First I visited the Plaza de España and was left speechless before its beauty."},
            {"spanish": "Luego me perdí por el laberinto del barrio de Santa Cruz.", "english": "Then I got lost through the labyrinth of the Santa Cruz quarter."},
            {"spanish": "De repente, escuché a un guitarrista tocando flamenco en una plazoleta.", "english": "Suddenly, I heard a guitarist playing flamenco in a small square."},
            {"spanish": "Fue una experiencia mágica que guardo en mi corazón para siempre.", "english": "It was a magical experience that I keep in my heart forever."}
        ],
        "grammar": {
            "title": "Narrative Chronology & Past Connectors",
            "explanation": "To tell a story that captivates listeners in Spanish, organize your narrative with clear chronological anchors.",
            "rules": [
                "Beginning the Story: *El mes pasado...*, *Hace unas semanas...*, *Todo empezó cuando...* (Everything began when...).",
                "Chronological Flow: **Primero** (First) -> **Luego / Después** (Then / Afterward) -> **Más tarde** (Later on) -> **De repente** (Suddenly - introduces surprise/turning point!).",
                "Concluding the Narrative: **Al final** (In the end) -> **Finalmente** (Finally) -> **Fue una experiencia que...** (It was an experience that...).",
                "Spelling Shift in Preterite Yo: Verbs ending in -GAR change 'g' to 'gu' in the 'yo' preterite to preserve the hard 'g' sound: *llegar -> llegué* (NOT *llegé*); *jugar -> jugué*!"
            ],
            "structures": [
                "Narrative Blueprint:",
                "1. Opening: El [día/mes] pasado viajé a [Lugar]",
                "2. Sequence: Primero [verbo preterito] -> Luego [verbo] -> De repente [evento]",
                "3. Conclusion: Al final [resultado] + Fue una experiencia [adjetivo]"
            ],
            "examples": [
                {"spanish": "Llegué a Sevilla a las diez. (Llegar -> llegué)", "english": "I arrived in Seville at ten."},
                {"spanish": "Jugué un partido ayer. (Jugar -> jugué)", "english": "I played a match yesterday."},
                {"spanish": "De repente empezó a llover.", "english": "Suddenly it started to rain."},
                {"spanish": "Al final encontramos el hotel.", "english": "In the end we found the hotel."}
            ],
            "commonMistakes": [
                {"wrong": "Llegé a Sevilla (misspelled)", "right": "Llegué a Sevilla", "explanation": "Verbs in -gar require 'gu' before 'e' to preserve the hard 'g' sound."},
                {"wrong": "A el final", "right": "Al final", "explanation": "Contract 'a + el' to 'al'."}
            ],
            "proTip": "The word **«De repente»** is the golden storytelling switch. Use it right before the most exciting moment in your story: *«Estaba caminando tranquilamente y, de repente... ¡escuché música flamenca!»*."
        },
        "conversation": {
            "title": "Storytelling at Class: Sharing Weekend Adventures",
            "context": "Sakib presents his short trip narrative to his Spanish class.",
            "dialogue": [
                {"speaker": "Profesora", "role": "Teacher", "spanish": "Sakib, cuéntanos tu viaje a Sevilla. ¿Cómo fue la experiencia?", "english": "Sakib, tell us about your trip to Seville. How was the experience?"},
                {"speaker": "Sakib", "role": "Student", "spanish": "¡Fue inolvidable, profesora! Salí de Madrid el viernes por la tarde en el AVE y llegué a Sevilla en dos horas y media.", "english": "It was unforgettable, teacher! I left Madrid on Friday afternoon on the AVE and arrived in Seville in two and a half hours."},
                {"speaker": "Profesora", "role": "Teacher", "spanish": "¿Y qué hiciste el sábado?", "english": "And what did you do on Saturday?"},
                {"speaker": "Sakib", "role": "Student", "spanish": "Primero visité el Real Alcázar y la Giralda. Luego caminé hasta la Plaza de España. Y de repente, en un rincón del parque, vi un espectáculo de flamenco al aire libre. ¡La bailaora transmitía tanta emoción!", "english": "First I visited the Real Alcazar and the Giralda. Then I walked to the Plaza de España. And suddenly, in a corner of the park, I saw an open-air flamenco show. The dancer transmitted so much emotion!"},
                {"speaker": "Profesora", "role": "Teacher", "spanish": "¡Qué maravilla! ¿Y qué comiste?", "english": "How wonderful! And what did you eat?"},
                {"speaker": "Sakib", "role": "Student", "spanish": "Cené gazpacho andaluz y pescado frito en Triana, al lado del río Guadalquivir. Al final regresé el domingo con el corazón lleno de alegría.", "english": "I had Andalusian gazpacho and fried fish in Triana for dinner, next to the Guadalquivir river. In the end I returned on Sunday with my heart full of joy."},
                {"speaker": "Profesora", "role": "Teacher", "spanish": "¡Excelente relato, Sakib! Has narrado la historia con una fluidez y un orden cronológico perfectos.", "english": "Excellent narrative, Sakib! You narrated the story with perfect fluency and chronological order."}
            ],
            "keyPhrases": [
                {"phrase": "Cuéntanos...", "explanation": "'Tell us...' (verb contar)."},
                {"phrase": "Al aire libre", "explanation": "'In the open air / outdoors'."},
                {"phrase": "Con el corazón lleno de alegría", "explanation": "'With my heart full of joy' (expressive narrative phrase)."}
            ]
        },
        "reading": {
            "title": "Historia completa: Un fin de semana inolvidable en Sevilla",
            "passage": "El mes pasado viví una aventura que jamás olvidaré. Decidí viajar a Sevilla, la luminosa capital de Andalucía. Tomé el tren de alta velocidad en la estación de Atocha un viernes por la tarde. El viaje fue suave y veloz. Al llegar a la estación de Santa Justa, sentí el calor suave del sur y el aroma a azahar de los naranjos que adornan las calles.\n\nEl sábado me levanté temprano. Primero desayuné un café con leche y una tostada con aceite y tomate en una terraza de la Alameda. Luego caminé hacia el Real Alcázar: sus jardines verdes, sus fuentes cantarinas y sus arcos árabes me transportaron a un cuento de Las mil y una noches. Después subí a lo alto de la Giralda, la antigua torre campanario de la catedral, desde donde contemplé una panorámica impresionante de tejados blancos y patios floridos.\n\nPor la tarde crucé el histórico puente de Isabel II hacia el barrio marinero de Triana. Me perdí voluntariamente por sus callejuelas estrechas. De repente, al doblar una esquina, escuché el rasgueo apasionado de una guitarra española y el zapateado rítmico del flamenco. Me detuve fascinado junto a decenas de transeúntes. Al final del día, cené unas tapas de pescaíto frito junto al río Guadalquivir mientras la luna llena iluminaba la Torre del Oro. Aquel viaje a Sevilla me demostró que el español ya no era solo una materia de estudio en mi cuaderno, sino la llave que me abrió las puertas a momentos mágicos e inolvidables.",
            "translation": "Last month I lived an adventure that I will never forget. I decided to travel to Seville, the luminous capital of Andalusia. I took the high-speed train at Atocha station on a Friday afternoon. The journey was smooth and swift. Upon arriving at Santa Justa station, I felt the mild warmth of the south and the orange blossom scent of the orange trees that adorn the streets.\n\nOn Saturday I woke up early. First I had a coffee with milk and toast with oil and tomato on a terrace in the Alameda. Then I walked toward the Real Alcazar: its green gardens, singing fountains, and Arabic arches transported me to a tale of One Thousand and One Nights. Afterward I climbed to the top of the Giralda, the cathedral's ancient bell tower, from where I gazed at an impressive panorama of white roofs and flowery courtyards.\n\nIn the afternoon I crossed the historic Isabel II bridge toward the maritime quarter of Triana. I voluntarily got lost in its narrow alleys. Suddenly, upon turning a corner, I heard the passionate strumming of a Spanish guitar and the rhythmic footwork of flamenco. I stopped, fascinated, alongside dozens of passersby. At the end of the day, I had fried fish tapas for dinner next to the Guadalquivir river while the full moon illuminated the Gold Tower. That trip to Seville proved to me that Spanish was no longer just a study subject in my notebook, but the key that unlocked the doors to magical and unforgettable moments.",
            "questions": [
                {"question": "¿A qué olían las calles de Sevilla al llegar Sakib?", "options": ["A gasolina", "A aroma a azahar de los naranjos", "A humo", "A comida rápida"], "answer": 1, "explanation": "Orange blossom scent ('aroma a azahar de los naranjos')."},
                {"question": "¿A qué famosa torre campanario subió Sakib?", "options": ["A la Torre de Pisa", "A la Giralda", "A la Torre Eiffel", "Al Big Ben"], "answer": 1, "explanation": "La Giralda ('subí a lo alto de la Giralda')."},
                {"question": "¿Qué escuchó Sakib de repente al doblar una esquina en Triana?", "options": ["Una ambulancia", "Una guitarra española y el zapateado del flamenco", "Un perro ladrando", "Gritos de tráfico"], "answer": 1, "explanation": "Spanish guitar and flamenco footwork ('el rasgueo apasionado de una guitarra...')."},
                {"question": "¿Qué demostró este viaje a Sakib sobre su español?", "options": ["Que debía renunciar", "Que ya no era solo una materia de estudio, sino una llave a momentos mágicos", "Que el examen era muy fácil", "Que prefiere hablar en inglés"], "answer": 1, "explanation": "A key to magical moments ('la llave que me abrió las puertas...')."}
            ]
        },
        "exercises": [
            {
                "id": "d49-ex1",
                "type": "fill-in",
                "prompt": "Yo preterite of LLEGAR (remember the -gar spelling rule!): Ayer yo ______ (llegar) a tiempo.",
                "options": ["llegué", "llegé", "llegó", "llegaste"],
                "correct": 0,
                "explanation": "Verbs in -gar change g -> gu in the yo preterite: 'llegué'."
            },
            {
                "id": "d49-ex2",
                "type": "multiple-choice",
                "prompt": "Which narrative transition means 'Suddenly'?",
                "options": ["Primero", "De repente", "Al final", "Normalmente"],
                "correct": 1,
                "explanation": "'De repente' means 'Suddenly'."
            },
            {
                "id": "d49-ex3",
                "type": "fill-in",
                "prompt": "Complete: ______ (In the end), regresé a casa muy contento.",
                "options": ["Al final", "A el final", "De final", "Por final"],
                "correct": 0,
                "explanation": "'Al final' means 'In the end'."
            },
            {
                "id": "d49-ex4",
                "type": "translation",
                "prompt": "Translate: 'First I walked through the park, then I visited the museum.'",
                "options": ["Primero caminé por el parque, luego visité el museo.", "Primero camino por el parque, luego visito el museo.", "Primero caminé para el parque, luego visité el museo.", "Antes caminé el parque, después visité el museo."],
                "correct": 0,
                "explanation": "'Primero caminé por el parque, luego visité el museo' sequences two preterite actions accurately."
            }
        ],
        "speakingChallenge": [
            {"prompt": "Narrate a real or imagined weekend trip using 'Primero...', 'Luego...', and 'Al final...'", "hint": "El fin de semana pasado viajé a... Primero... Luego... Al final...", "sampleAnswer": "El fin de semana pasado viajé a Toledo. Primero visité la catedral, luego caminé por las calles históricas y al final comí mazapán delicioso."},
            {"prompt": "Use 'De repente' to describe an unexpected event in a story.", "hint": "Estaba caminando y, de repente...", "sampleAnswer": "Estaba paseando por el centro y, de repente, empezó a llover fuertemente."},
            {"prompt": "Say that a trip was unforgettable and you keep it in your heart.", "hint": "Fue un viaje inolvidable que guardo...", "sampleAnswer": "Fue un viaje totalmente inolvidable que guardo en mi memoria para siempre."}
        ],
        "dailyRevision": {
            "quickQuestions": [
                "What spelling change occurs in the 'yo' preterite of verbs ending in -gar? (g -> gu: llegué)",
                "What narrative phrase means 'suddenly'? (de repente)"
            ],
            "grammarRecall": "Narrative chronology: Primero -> luego/después -> de repente -> al final. -GAR preterite: llegué, jugué, pagué.",
            "vocabRecall": ["El viaje inolvidable", "Llegar (llegué)", "Descubrir", "Disfrutar de", "Perderse", "Al principio", "Al final", "De repente"]
        },
        "checklist": [
            "Read and comprehended a multi-paragraph Spanish narrative",
            "Applied narrative transition words (primero, luego, de repente, al final)",
            "Applied the -GAR spelling change in the preterite (llegar -> llegué)",
            "Answered 4 in-depth reading comprehension questions",
            "Completed all 4 storytelling exercises",
            "Narrated a personal travel story out loud in Spanish"
        ]
    },
    {
        "day": 50,
        "stage": 5,
        "title": "Building Longer Paragraphs & Complex Sentences",
        "subtitle": "Combining description with past narration + Stage 5 Milestone Assessment",
        "goals": [
            "Synthesize your full grammatical toolkit into cohesive, multi-sentence paragraphs",
            "Combine past actions (Preterite) with descriptions (Ser/Estar) seamlessly",
            "Use complex sentence connectors: *porque, por eso, sin embargo, además, aunque*",
            "Complete the Stage 5 Milestone Assessment (DAYS 41–50 COMPREHENSIVE TEST)"
        ],
        "bengaliNote": "You are now building complex paragraphs! Notice how natural storytelling alternates between **actions** that happened (Preterite: *Viajé, llegué, compré*) and **descriptions** of how things were (Ser/Estar: *La ciudad era hermosa, el día estuvo soleado, estaba muy contento*). This is the hallmark of true A1 mastery!",
        "vocabulary": [
            {"word": "El párrafo", "translation": "The paragraph", "pos": "noun", "gender": "masculine", "example": "Escribo un párrafo sobre mi vida.", "exampleTranslation": "I write a paragraph about my life."},
            {"word": "El texto / La redacción", "translation": "The text / The essay, writing piece", "pos": "noun", "gender": "masculine / feminine", "example": "Redacto un texto en español.", "exampleTranslation": "I draft a text in Spanish."},
            {"word": "La experiencia", "translation": "The experience", "pos": "noun", "gender": "feminine", "example": "Ha sido una experiencia transformadora.", "exampleTranslation": "It has been a transformative experience."},
            {"word": "El progreso / Progresar", "translation": "The progress / To progress", "pos": "noun / verb", "gender": "masculine", "example": "Noto mi progreso cada semana.", "exampleTranslation": "I notice my progress every week."},
            {"word": "La meta / El objetivo", "translation": "The goal / The objective", "pos": "noun", "gender": "feminine / masculine", "example": "Mi objetivo es dominar el nivel A1.", "exampleTranslation": "My objective is to master level A1."},
            {"word": "Expresar (ideas / opiniones)", "translation": "To express (ideas / opinions)", "pos": "verb", "gender": None, "example": "Puedo expresar mis ideas con claridad.", "exampleTranslation": "I can express my ideas clearly."},
            {"word": "Combinar", "translation": "To combine", "pos": "verb", "gender": None, "example": "Combino verbos y adjetivos.", "exampleTranslation": "I combine verbs and adjectives."},
            {"word": "Fluido(a) / La fluidez", "translation": "Fluent / Fluency", "pos": "adjective / noun", "gender": "mixed", "example": "Hablo con mayor fluidez.", "exampleTranslation": "I speak with greater fluency."},
            {"word": "En resumen / Para resumir", "translation": "In summary / To sum up", "pos": "phrase", "gender": None, "example": "En resumen, el viaje fue un éxito.", "exampleTranslation": "In summary, the trip was a success."},
            {"word": "Estar orgulloso(a) de", "translation": "To be proud of", "pos": "phrase", "gender": "variable", "example": "Estoy muy orgulloso de mi esfuerzo.", "exampleTranslation": "I am very proud of my effort."}
        ],
        "sentences": [
            {"spanish": "Cuando llegué a Madrid hace dos meses, no conocía a nadie; sin embargo, hoy tengo muchos amigos.", "english": "When I arrived in Madrid two months ago, I knew nobody; however, today I have many friends."},
            {"spanish": "Ayer fue un día largo porque trabajé por la mañana y estudié por la tarde.", "english": "Yesterday was a long day because I worked in the morning and studied in the afternoon."},
            {"spanish": "Aunque la gramática española tiene reglas complejas, con práctica diaria todo se vuelve natural.", "english": "Although Spanish grammar has complex rules, with daily practice everything becomes natural."},
            {"spanish": "El fin de semana pasado fuimos a la sierra, caminamos durante horas y descansamos al sol.", "english": "Last weekend we went to the mountains, walked for hours, and rested in the sun."},
            {"spanish": "En resumen, aprender español ha transformado mi manera de ver el mundo.", "english": "In summary, learning Spanish has transformed my way of seeing the world."},
            {"spanish": "Estoy muy orgulloso de haber completado cincuenta días de estudio riguroso.", "english": "I am very proud to have completed fifty days of rigorous study."}
        ],
        "grammar": {
            "title": "The Master Writing Blueprint: Paragraph Cohesion & Clause Weaving",
            "explanation": "A professional paragraph connects actions, causes, contrasts, and conclusions seamlessly using the complete grammar engine you have built.",
            "rules": [
                "1. Opening Anchor: Set the time and place (*Hace dos meses, en Madrid...*).",
                "2. Action Clauses (Preterite): State what happened (*Llegué, encontré un piso, comencé mis clases*).",
                "3. Descriptive Clauses (Ser/Estar): Describe the backdrop or feelings (*El piso era luminoso, la ciudad estaba llena de vida, me sentía emocionado*).",
                "4. Contrast & Cause (Connectors): Connect with *porque, por eso, sin embargo, además*.",
                "5. Closing Reflection: Synthesize with *En resumen...*, *Fue una experiencia que...*"
            ],
            "structures": [
                "The 5-Step Paragraph Template:",
                "[Tiempo y lugar] + [Acciones en pretérito] + [Descripciones] + [Conectores de contraste/causa] + [Conclusión y reflexión]"
            ],
            "examples": [
                {"spanish": "Ayer por la tarde fui a la biblioteca. Aunque había mucha gente, encontré una mesa tranquila. Estudié tres horas y, por eso, aprobé el examen de hoy.", "english": "Yesterday afternoon I went to the library. Although there were many people, I found a quiet table. I studied three hours and, therefore, passed today's exam."},
                {"spanish": "El sábado pasado celebré mi cumpleaños con mis amigos. Cociné comida bengalí para todos y ellos trajeron una tarta deliciosa. Fue un día muy especial.", "english": "Last Saturday I celebrated my birthday with my friends. I cooked Bengali food for everyone and they brought a delicious cake. It was a very special day."}
            ],
            "commonMistakes": [
                {"wrong": "Writing choppy bullet-point style sentences without connectors", "right": "Weave sentences together using 'pero, además, por eso, sin embargo'", "explanation": "Connectors create editorial fluidity."},
                {"wrong": "Orgulloso para mi progreso", "right": "Orgulloso DE mi progreso", "explanation": "'Estar orgulloso' requires the preposition 'de'."}
            ],
            "proTip": "Notice how alternating short punchy sentences with longer connected sentences creates a musical rhythm in Spanish prose. That is the secret of professional textbook and essay writing!"
        },
        "conversation": {
            "title": "A Teacher-Student Dialogue on Completing 50 Days",
            "context": "Professor Carmen conducts the Stage 5 evaluation interview with Sakib.",
            "dialogue": [
                {"speaker": "Profª Carmen", "role": "Teacher", "spanish": "Sakib, ¡cincuenta días completados! Cincuenta días de trabajo impecable.", "english": "Sakib, fifty days completed! Fifty days of impeccable work."},
                {"speaker": "Sakib", "role": "Student", "spanish": "Muchas gracias, profesora. La verdad es que me siento muy orgulloso de este camino.", "english": "Thank you very much, professor. The truth is that I feel very proud of this journey."},
                {"speaker": "Profª Carmen", "role": "Teacher", "spanish": "He leído tu redacción sobre tu viaje a Segovia y tu vida en Madrid. Tu capacidad para combinar el pretérito con descripciones y conectores es de un nivel excelente.", "english": "I have read your essay about your trip to Segovia and your life in Madrid. Your ability to combine the preterite with descriptions and connectors is at an excellent level."},
                {"speaker": "Sakib", "role": "Student", "spanish": "Al principio pensaba que el pretérito y las preposiciones como por y para eran imposibles, pero con los ejemplos diarios y la práctica constante todo cobró sentido.", "english": "At the beginning I thought the preterite and prepositions like por and para were impossible, but with the daily examples and constant practice everything made sense."},
                {"speaker": "Profª Carmen", "role": "Teacher", "spanish": "Solo quedan diez días: la etapa final de consolidación y el examen final de A1. ¿Cómo te ves para la recta final?", "english": "Only ten days remain: the final consolidation stage and the final A1 exam. How do you see yourself for the final stretch?"},
                {"speaker": "Sakib", "role": "Student", "spanish": "Me veo con máxima energía y confianza. Voy a dar lo mejor de mí para terminar con un sobresaliente.", "english": "I see myself with maximum energy and confidence. I am going to give my best to finish with an outstanding grade."}
            ],
            "keyPhrases": [
                {"phrase": "Trabajo impecable", "explanation": "'Impeccable / flawless work'."},
                {"phrase": "Cobró sentido", "explanation": "'Made sense / clicked into place'."},
                {"phrase": "La recta final", "explanation": "'The home stretch / final leg of a journey'."}
            ]
        },
        "reading": {
            "title": "Stage 5 Capstone: Cincuenta días — La consolidación de una voz en español",
            "passage": "Cincuenta días representan un hito monumental. En la pedagogía lingüística internacional, el paso del presente simple al pretérito marca el momento en que un estudiante deja de ser un mero repetidor de frases hechas y se convierte en un narrador de su propia vida. Sakib ya no solo dice qué hace hoy; ahora relata qué hizo ayer, qué soñó la semana pasada y qué descubrió en sus viajes por las ciudades históricas de España. Sabe hablar de profesiones y educación, describir síntomas de salud en la farmacia, reclamar pertenencias con posesivos y expresar emociones complejas con verbos reflexivos. Sus oraciones se encadenan con naturalidad usando conectores sofisticados como «sin embargo», «además» y «por lo tanto». Sakib mira el calendario: quedan exactamente diez días para culminar el desafío de sesenta días y presentarse al Examen Final de A1. La meta no solo está al alcance de la mano; está prácticamente conquistada.",
            "translation": "Fifty days represent a monumental milestone. In international language pedagogy, the transition from simple present to preterite marks the moment when a student stops being a mere repeater of canned phrases and becomes a narrator of their own life. Sakib no longer just says what he does today; now he recounts what he did yesterday, what he dreamed last week, and what he discovered on his trips through the historic cities of Spain. He knows how to talk about professions and education, describe health symptoms at the pharmacy, claim belongings with possessives, and express complex emotions with reflexive verbs. His sentences link naturally using sophisticated connectors like 'sin embargo', 'además', and 'por lo tanto'. Sakib looks at the calendar: exactly ten days remain to culminate the sixty-day challenge and sit for the Final A1 Exam. The goal is not only within arm's reach; it is practically conquered.",
            "questions": [
                {"question": "¿Qué marca el paso del presente simple al pretérito según la pedagogía?", "options": ["Que el alumno se cansa", "Que el estudiante deja de repetir frases y se convierte en narrador de su propia vida", "Que hay que empezar de nuevo", "Que no se puede hablar más"], "answer": 1, "explanation": "Becomes a narrator of their own life ('se convierte en un narrador de su propia vida')."},
                {"question": "¿Cuántos días quedan para culminar el desafío de 60 días?", "options": ["Treinta días", "Veinte días", "Exactamente diez días", "Cincuenta días"], "answer": 2, "explanation": "Exactly ten days remain ('quedan exactamente diez días')."},
                {"question": "¿Cómo califica el texto el estado actual de la meta A1?", "options": ["Imposible", "Prácticamente conquistada y al alcance de la mano", "Olvidadiza", "Muy lejana"], "answer": 1, "explanation": "Within arm's reach and practically conquered ('prácticamente conquistada')."}
            ]
        },
        "exercises": [
            {
                "id": "d50-ex1",
                "type": "fill-in",
                "prompt": "Complete with the correct connector of contrast: Estudié mucho; ______ (however), el examen fue difícil.",
                "options": ["sin embargo", "porque", "entonces", "también"],
                "correct": 0,
                "explanation": "'Sin embargo' expresses formal contrast ('however / nevertheless')."
            },
            {
                "id": "d50-ex2",
                "type": "fill-in",
                "prompt": "Complete: Estoy muy orgulloso ______ (of) mi esfuerzo en estos cincuenta días.",
                "options": ["de", "por", "para", "en"],
                "correct": 0,
                "explanation": "'Estar orgulloso' takes 'de': 'orgulloso de mi esfuerzo'."
            },
            {
                "id": "d50-ex3",
                "type": "multiple-choice",
                "prompt": "What does 'En resumen' mean in a text?",
                "options": ["In the beginning", "In summary / To sum up", "Suddenly", "Never"],
                "correct": 1,
                "explanation": "'En resumen' means 'In summary / To sum up'."
            },
            {
                "id": "d50-ex4",
                "type": "translation",
                "prompt": "Translate: 'Yesterday I was at home because I was very tired.'",
                "options": ["Ayer estuve en casa porque estaba muy cansado.", "Ayer fui en casa porque era muy cansado.", "Ayer estuve a casa porque tuve cansado.", "Ayer fue en casa porque hacía cansado."],
                "correct": 0,
                "explanation": "'Ayer estuve en casa porque estaba muy cansado' pairs location and state accurately."
            }
        ],
        "speakingChallenge": [
            {"prompt": "Say that you are proud of your progress across these 50 days.", "hint": "Estoy muy orgulloso de...", "sampleAnswer": "Estoy muy orgulloso de mi constancia y de mi progreso en estos cincuenta días de desafío de español."},
            {"prompt": "Combine past action with a reason: 'Yesterday I studied three hours because tomorrow I have an exam.'", "hint": "Ayer estudié tres horas porque...", "sampleAnswer": "Ayer estudié tres horas en la biblioteca porque quería repasar toda la gramática."},
            {"prompt": "Announce that you are entering the final 10 days of the challenge with full motivation!", "hint": "Solo quedan diez días...", "sampleAnswer": "¡Solo quedan diez días para completar mi desafío! ¡Tengo toda la energía para lograr mi meta de A1!"}
        ],
        "dailyRevision": {
            "quickQuestions": [
                "What preposition follows 'estar orgulloso'? (DE)",
                "How do you organize a cohesive narrative paragraph in Spanish?"
            ],
            "grammarRecall": "Paragraph architecture: Time/Place anchor + Preterite actions + Descriptions (Ser/Estar) + Connectors (sin embargo, además, por eso) + En resumen.",
            "vocabRecall": ["El párrafo", "La redacción", "El progreso", "La meta", "Expresar", "Fluidez", "En resumen", "Estar orgulloso de"]
        },
        "checklist": [
            "Constructed cohesive multi-clause paragraphs combining past and descriptions",
            "Used sophisticated connectors (sin embargo, además, por lo tanto, en resumen)",
            "Applied 'estar orgulloso de' with authentic emotion",
            "Completed the Stage 5 Milestone Reading Passage (50 Days milestone)",
            "Finished all 4 paragraph synthesis exercises",
            "CELEBRATED 50 DAYS COMPLETED — 5/6 OF THE ENTIRE CHALLENGE CONQUERED! 🇪🇸🎉"
        ]
    }
]

# Combine both parts
stage5_complete = stage5_days + stage5_part2

with open("d:/ag/espanol-handbook/data/lessons/stage5.js", "w", encoding="utf-8") as f:
    f.write("// Stage 5: Days 41 to 50 (Developing Stronger A1 Skills)\n")
    f.write("window.STAGE_5_LESSONS = ")
    json.dump(stage5_complete, f, ensure_ascii=False, indent=2)
    f.write(";\n")

print(f"Successfully generated stage5.js with all {len(stage5_complete)} full days!")
