"""
Build Day 60 + Combine Stage 6 into data/lessons/stage6.js
"""
import json
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from build_stage6_days_51_55 import stage6_days_51_55
from build_stage6_part1 import stage6_part2

day_60 = [
    {
        "day": 60,
        "stage": 6,
        "title": "The Grand A1 Milestone & Capstone Reflection",
        "subtitle": "Celebration of 60 Days, The Final Challenge Assessment, and The Path to A2",
        "goals": [
            "Celebrate the triumphant completion of the 60-Day Spanish Learning Challenge!",
            "Reflect on the journey: from zero words on Day 1 to full conversational A1 autonomy on Day 60",
            "Review your linguistic growth: 600 words mastered, 350+ everyday sentences, 8 grammar pillars",
            "Prepare for the Official Final A1 Examination and receive your personalized Challenge Certificate for Sakib Ahmed"
        ],
        "bengaliNote": "আজ ৬০তম দিন — আপনার বিজয়ের দিন! (Today is Day 60 — your day of victory!). You have accomplished something truly magnificent: 60 days of uninterrupted dedication, discipline, and passion. You are no longer looking at Spanish from the outside; Spanish lives inside you. Congratulations, Sakib! ¡Enhorabuena de todo corazón!",
        "vocabulary": [
            {"word": "El logro / La victoria", "translation": "The achievement / The victory", "pos": "noun", "gender": "masculine / feminine", "example": "Completar sesenta días es un logro monumental.", "exampleTranslation": "Completing 60 days is a monumental achievement."},
            {"word": "La culminación / El hito", "translation": "The culmination / The milestone", "pos": "noun", "gender": "masculine", "example": "Hoy celebramos este hito histórico.", "exampleTranslation": "Today we celebrate this historic milestone."},
            {"word": "La perseverancia / La disciplina", "translation": "Perseverance / Discipline", "pos": "noun", "gender": "feminine", "example": "Tu perseverancia ha sido admirable.", "exampleTranslation": "Your perseverance has been admirable."},
            {"word": "El examen final de A1", "translation": "The Final A1 Examination", "pos": "noun", "gender": "masculine", "example": "Estoy listo para el examen final.", "exampleTranslation": "I am ready for the final exam."},
            {"word": "El certificado de aprovechamiento", "translation": "Certificate of completion / achievement", "pos": "noun", "gender": "masculine", "example": "Recibo mi certificado oficial con orgullo.", "exampleTranslation": "I receive my official certificate with pride."},
            {"word": "El nivel A1 consolidado", "translation": "Consolidated A1 level", "pos": "phrase", "gender": "masculine", "example": "Tienes un nivel A1 totalmente consolidado.", "exampleTranslation": "You have a totally consolidated A1 level."},
            {"word": "El camino hacia A2", "translation": "The path toward A2", "pos": "noun", "gender": "masculine", "example": "El camino hacia A2 empieza hoy.", "exampleTranslation": "The path toward A2 starts today."},
            {"word": "El hablante independiente", "translation": "Independent speaker", "pos": "noun", "gender": "masculine", "example": "Eres un hablante con autonomía.", "exampleTranslation": "You are a speaker with autonomy."},
            {"word": "La pasión duradera", "translation": "Lasting passion", "pos": "noun", "gender": "feminine", "example": "El español es una pasión duradera.", "exampleTranslation": "Spanish is a lasting passion."},
            {"word": "¡Lo conseguí! / ¡Lo logré!", "translation": "I did it! / I achieved it! (triumphant exclamation)", "pos": "phrase", "gender": None, "example": "¡Lo conseguí! ¡Sesenta días de español!", "exampleTranslation": "I did it! Sixty days of Spanish!"}
        ],
        "sentences": [
            {"spanish": "¡Hoy es el día sesenta: he completado con éxito mi desafío de español!", "english": "Today is day sixty: I have successfully completed my Spanish challenge!"},
            {"spanish": "Hace sesenta días no sabía conjugar ningún verbo; hoy hablo, leo y escribo con seguridad.", "english": "Sixty days ago I didn't know how to conjugate any verb; today I speak, read, and write with confidence."},
            {"spanish": "He aprendido más de seiscientas palabras útiles y domino la gramática fundamental de A1.", "english": "I have learned over six hundred useful words and master the fundamental grammar of A1."},
            {"spanish": "Agradezco profundamente a mis profesores, amigos y familiares por su apoyo constante.", "english": "I deeply thank my teachers, friends, and family for their constant support."},
            {"spanish": "El español ya no es un idioma extranjero para mí, es una parte viva de mi vida cotidiana.", "english": "Spanish is no longer a foreign language for me, it is a living part of my daily life."},
            {"spanish": "¡Estoy totalmente preparado para el Examen Final de A1 y listo para celebrar mi éxito!", "english": "I am totally prepared for the Final A1 Exam and ready to celebrate my success!"}
        ],
        "grammar": {
            "title": "The Master A1 Competence Portfolio: The 'Can-Do' Verification",
            "explanation": "According to the official CEFR (Common European Framework of Reference) A1 descriptors, here is what you can now demonstrably DO in Spanish:",
            "rules": [
                "1. Personal Interaction: You can introduce yourself, state your name, origin, age, profession, and family in full detail without hesitation.",
                "2. Everyday Transactions: You can order 3-course meals in restaurants, buy groceries in markets, book hotel rooms, and ask for the bill.",
                "3. Urban Navigation: You can ask and understand directions, take high-speed trains, buy return tickets, and navigate metro stations.",
                "4. Physical & Emotional States: You can describe your daily routine from waking to sleeping, express illness and symptoms at the pharmacy, and talk about emotions with reflexive verbs.",
                "5. Temporal Narration: You can tell the time, state dates, discuss weather and temperatures, and narrate completed past trips using the preterite simple past.",
                "6. Preferences & Logic: You can express likes and dislikes with GUSTAR, state desires with QUERER, obligations with TENER QUE, and connect complex ideas with PERO, PORQUE, and POR ESO."
            ],
            "structures": [
                "The CEFR A1 Formula for Sakib Ahmed:",
                "Comprensión Lectora (Reading) + Comprensión Auditiva (Listening) + Expresión Escrita (Writing) + Expresión Oral (Speaking) = A1 CONQUERED!"
            ],
            "examples": [
                {"spanish": "Puedo comunicarme con autonomía en cualquier situación cotidiana.", "english": "I can communicate with autonomy in any daily situation."},
                {"spanish": "Comprendo textos narrativos y reconozco giros idiomáticos nativos.", "english": "I understand narrative texts and recognize native idiomatic turns."}
            ],
            "commonMistakes": [
                {"wrong": "Stopping your Spanish practice after Day 60", "right": "Keep reading, watching Spanish series, and speaking weekly as you step toward A2", "explanation": "Language is a living garden; keep watering it with daily joy."}
            ],
            "proTip": "When you complete your Final Exam in the next section, your personalized Certificate of Achievement will be officially generated with your name: **Sakib Ahmed**, certifying your completion of the 60-Day Spanish Challenge!"
        },
        "conversation": {
            "title": "The Graduation Dialogue: A Toast to 60 Days",
            "context": "Sakib, Professor Carmen, and classmates Carlos, Laura, and Mateo celebrate on the final day.",
            "dialogue": [
                {"speaker": "Profª Carmen", "role": "Teacher", "spanish": "¡Atención a todos! Hoy celebramos un momento verdaderamente histórico. ¡Sakib ha completado el día sesenta de su desafío personal de español!", "english": "Attention everyone! Today we celebrate a truly historic moment. Sakib has completed day sixty of his personal Spanish challenge!"},
                {"speaker": "Todos", "role": "Classmates", "spanish": "¡¡¡Bravooooo! ¡Enhorabuena, Sakib! ¡Qué orgullo!", "english": "Bravoooo! Congratulations, Sakib! What pride!"},
                {"speaker": "Sakib", "role": "Student", "spanish": "Muchísimas gracias a todos, de corazón. Carmen, tus enseñanzas han sido una luz constante. Y a vosotros, amigos míos, gracias por cada conversación, cada risa y cada café compartido.", "english": "Thank you all so very much, from the bottom of my heart. Carmen, your teachings have been a constant light. And to you, my friends, thank you for every conversation, every laugh, and every shared coffee."},
                {"speaker": "Carlos", "role": "Classmate", "spanish": "Sakib, te acuerdas del primer día cuando decías 'me llamo es Sakib' y te daba vergüenza hablar? ¡Mírate ahora! Hablas con soltura, cuentas anécdotas en pretérito y bromeas como un madrileño.", "english": "Sakib, do you remember the first day when you said 'me llamo es Sakib' and felt embarrassed to speak? Look at you now! You speak with fluency, tell stories in the preterite, and joke like a local of Madrid."},
                {"speaker": "Laura", "role": "Classmate", "spanish": "¡Es verdad! Tu disciplina diaria ha sido una inspiración para todos nosotros.", "english": "That's true! Your daily discipline has been an inspiration to all of us."},
                {"speaker": "Profª Carmen", "role": "Teacher", "spanish": "Sakib Ahmed: has demostrado que con constancia, método y pasión, cualquier meta es posible. Brindemos por Sakib, por el idioma español y por su brillante futuro. ¡Salud!", "english": "Sakib Ahmed: you have demonstrated that with consistency, method, and passion, any goal is possible. Let's toast to Sakib, to the Spanish language, and to his brilliant future. Cheers!"},
                {"speaker": "Sakib", "role": "Student", "spanish": "¡Salud por el español! ¡Lo conseguí!", "english": "Cheers to Spanish! I did it!"}
            ],
            "keyPhrases": [
                {"phrase": "De corazón", "explanation": "'From the bottom of my heart'."},
                {"phrase": "Mírate ahora", "explanation": "'Look at you now!' (acknowledging dramatic growth)."},
                {"phrase": "¡Salud!", "explanation": "'Cheers! / To health!' (traditional Spanish toast)."}
            ]
        },
        "reading": {
            "title": "El gran manifiesto del día 60: La conquista de un nuevo mundo",
            "passage": "Sesenta días atrás, el idioma español era para Sakib un territorio inexplorado, un océano de sonidos bellos pero inalcanzables. Hoy, al llegar al final de este viaje pedagógico, el paisaje es radicalmente distinto. A lo largo de sesenta lecciones completas y rigurosas, Sakib ha construido piedra a piedra un edificio lingüístico indestructible.\n\nHa aprendido más de seiscientas palabras vivas que palpitan en su memoria: desde los alimentos del mercado hasta las piezas del cuerpo humano, desde los términos de los trenes de alta velocidad hasta los giros castizos de las tabernas madrileñas. Ha conquistado los dos verbos para 'ser' (ser y estar), ha dominado las tres familias verbales en presente y en pretérito, ha navegado las sutilezas de por y para, y ha hecho suyas las estructuras de gustar, doler y los verbos reflexivos.\n\nPero el mayor tesoro no está en las páginas de este manual, sino en su propia alma: Sakib ha descubierto una nueva voz. Cuando habla en español, no traduce: siente, ríe, se emociona y comparte su verdad con el mundo hispanohablante. El desafío de sesenta días ha terminado; pero el viaje de la vida en español acaba de comenzar. ¡Enhorabuena, Sakib Ahmed, hablante independiente de la lengua de Cervantes!",
            "translation": "Sixty days ago, the Spanish language was for Sakib an unexplored territory, an ocean of beautiful but unreachable sounds. Today, upon arriving at the end of this pedagogical journey, the landscape is radically different. Throughout sixty complete and rigorous lessons, Sakib has built stone by stone an indestructible linguistic edifice.\n\nHe has learned over six hundred living words that pulse in his memory: from market foods to parts of the human body, from high-speed train terms to traditional idioms of Madrid taverns. He has conquered the two verbs for 'to be' (ser and estar), has mastered the three verb families in present and preterite, has navigated the subtleties of por and para, and has made his own the structures of gustar, doler, and reflexive verbs.\n\nBut the greatest treasure is not in the pages of this manual, but in his own soul: Sakib has discovered a new voice. When he speaks in Spanish, he does not translate: he feels, laughs, gets emotional, and shares his truth with the Spanish-speaking world. The sixty-day challenge has ended; but the journey of life in Spanish has just begun. Congratulations, Sakib Ahmed, independent speaker of the language of Cervantes!",
            "questions": [
                {"question": "¿Cuántas palabras útiles ha dominado Sakib a lo largo de los 60 días?", "options": ["Solo diez", "Más de seiscientas palabras vivas", "Cincuenta palabras", "Ninguna palabra"], "answer": 1, "explanation": "Over 600 words ('más de seiscientas palabras vivas')."},
                {"question": "¿Cuál es el mayor tesoro según el texto?", "options": ["Un cofre de oro", "Haber descubierto una nueva voz en español sin necesidad de traducir", "Un coche nuevo", "Un billete de avión"], "answer": 1, "explanation": "Discovered a new voice in Spanish ('ha descubierto una nueva voz')."},
                {"question": "¿Qué proclama el texto sobre Sakib al final?", "options": ["Que debe volver a empezar A1", "¡Enhorabuena, Sakib Ahmed, hablante independiente de la lengua de Cervantes!", "Que no hable más", "Que el reto no sirvió"], "answer": 1, "explanation": "'¡Enhorabuena, Sakib Ahmed, hablante independiente de la lengua de Cervantes!'."}
            ]
        },
        "exercises": [
            {
                "id": "d60-ex1",
                "type": "multiple-choice",
                "prompt": "How many days did you complete in this Spanish challenge?",
                "options": ["30 days", "45 days", "60 complete days of daily lessons!", "10 days"],
                "correct": 2,
                "explanation": "60 complete daily lessons conquered!"
            },
            {
                "id": "d60-ex2",
                "type": "fill-in",
                "prompt": "The triumphant cry of victory: ¡Lo ______ (I did it / achieved it)! ¡Sesenta días!",
                "options": ["conseguí", "hago", "puedo", "tengo"],
                "correct": 0,
                "explanation": "'¡Lo conseguí!' or '¡Lo logré!' expresses triumphant achievement."
            },
            {
                "id": "d60-ex3",
                "type": "multiple-choice",
                "prompt": "What traditional toast did the class make for Sakib?",
                "options": ["¡Adiós!", "¡Salud!", "¡Socorro!", "¡Por favor!"],
                "correct": 1,
                "explanation": "'¡Salud!' is the traditional Spanish toast to health and achievement."
            },
            {
                "id": "d60-ex4",
                "type": "translation",
                "prompt": "Translate: 'Congratulations from the bottom of my heart, you achieved your goal!'",
                "options": ["¡Enhorabuena de todo corazón, lograste tu meta!", "¡Buenos días de corazón, tienes tu meta!", "¡De nada de corazón, eres tu meta!", "¡Hola de corazón, haces tu meta!"],
                "correct": 0,
                "explanation": "'¡Enhorabuena de todo corazón, lograste tu meta!' is the heartfelt congratulations."
            }
        ],
        "speakingChallenge": [
            {"prompt": "Deliver your triumphant Day 60 Victory Speech in Spanish!", "hint": "¡Hoy es el día sesenta! He completado mi desafío de español...", "sampleAnswer": "¡Hoy es el día sesenta! He completado con éxito mi desafío de español. Estoy profundamente orgulloso de mi esfuerzo y agradecido por este maravilloso viaje lingüístico."},
            {"prompt": "Say: 'I can understand, read, write, and speak Spanish with confidence.'", "hint": "Puedo comprender, leer, escribir y hablar español con...", "sampleAnswer": "Puedo comprender, leer, escribir y hablar español con total seguridad y confianza en situaciones cotidianas."},
            {"prompt": "Toast to your future in Spanish: '¡Salud por el español y por el futuro!'", "hint": "¡Salud por el español...!", "sampleAnswer": "¡Salud por el español, por el conocimiento y por un futuro lleno de éxitos y aventuras!"}
        ],
        "dailyRevision": {
            "quickQuestions": [
                "What is the CEFR level you have mastered across these 60 days? (Level A1 Breakthrough / Access)",
                "What is your next horizon? (Level A2 Waystage)"
            ],
            "grammarRecall": "A1 CEFR Mastery: Complete integration of all 8 grammatical pillars, 600 vocabulary words, reading comprehension, writing production, and conversational fluency.",
            "vocabRecall": ["El logro", "La victoria", "El hito", "El examen final", "El certificado", "¡Lo conseguí!", "¡Salud!", "El camino hacia A2"]
        },
        "checklist": [
            "Celebrated Day 60 — The Grand Capstone of the 60-Day Spanish Challenge",
            "Reflected on the complete transformation from Day 1 to Day 60",
            "Read and answered the Grand Reading Manifesto of Day 60",
            "Completed the final daily lesson exercises",
            "Delivered the Day 60 Victory Speech aloud with pride",
            "PROCEEDED TO THE FINAL A1 EXAMINATION AND PERSONALIZED CERTIFICATE! 🎓🇪🇸🏆"
        ]
    }
]

# Combine Stage 6
stage6_complete = stage6_days_51_55 + stage6_part2 + day_60

with open("d:/ag/espanol-handbook/data/lessons/stage6.js", "w", encoding="utf-8") as f:
    f.write("// Stage 6: Days 51 to 60 (A1 Consolidation and Final Assessment)\n")
    f.write("window.STAGE_6_LESSONS = ")
    json.dump(stage6_complete, f, ensure_ascii=False, indent=2)
    f.write(";\n")

print(f"Successfully generated stage6.js with all {len(stage6_complete)} full days!")
