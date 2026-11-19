"""
Script to update all UI titles, section headers, buttons, placeholders, and tooltips
in js/app.js to clear, accessible English for the beginner student.
"""

def update_app_js():
    path = "d:/ag/espanol-handbook/js/app.js"
    with open(path, "r", encoding="utf-8") as f:
        code = f.read()

    replacements = [
        # Nav progress
        ("${completedCount}/60 Días (${pct}%)", "${completedCount}/60 Days (${pct}%)"),
        ("alert(\"Tu navegador no soporta síntesis de voz (Web Speech API).\");", "alert(\"Your browser does not support Web Speech API.\");"),

        # Overview
        ("600 Palabras Clave", "600 Core Words"),
        ("📖 Continuar Día ${state.currentDay}: ${allLessons.find(l => l.day === state.currentDay)?.title || 'Comenzar'}",
         "📖 Continue Day ${state.currentDay}: ${allLessons.find(l => l.day === state.currentDay)?.title || 'Start'}"),
        ("🗺️ Guía de Inicio y Pronunciación", "🗺️ Getting Started & Pronunciation Guide"),
        ("📚 Diccionario A-Z (600 Palabras)", "📚 A-Z Dictionary (600 Words)"),
        ("🎓 Examen Final y Certificado", "🎓 Final Exam & Certificate"),
        ("<span class=\"section-tag\">Estructura del Desafío</span>", "<span class=\"section-tag\">Challenge Curriculum</span>"),
        ("<h2 class=\"section-title\">Las 6 Etapas Hacia el Nivel A1</h2>", "<h2 class=\"section-title\">The 6 Stages to Level A1</h2>"),
        ("<p class=\"section-desc\">Sesenta días de progresión gradual, divididos en 6 bloques temáticos rigurosos con evaluaciones periódicas.</p>",
         "<p class=\"section-desc\">60 days of step-by-step progress, divided into 6 rigorous thematic stages with milestone assessments.</p>"),
        ("<span class=\"stage-badge\">Etapa ${s.num}</span>", "<span class=\"stage-badge\">Stage ${s.num}</span>"),
        ("<span class=\"stage-days\">Días ${s.days}</span>", "<span class=\"stage-days\">Days ${s.days}</span>"),
        ("title=\"Día ${l.day}: ${l.title}\"", "title=\"Day ${l.day}: ${l.title}\""),
        ("🏆 Ver Hito de la Etapa ${s.num}", "🏆 View Stage ${s.num} Milestone"),

        # Sidebar
        ("<div class=\"sidebar-title\">Índice del Curso (60 Días)</div>", "<div class=\"sidebar-title\">Course Index (60 Days)</div>"),
        ("<option value=\"all\">Todas las Etapas (1–6)</option>", "<option value=\"all\">All Stages (1–6)</option>"),
        ("Etapa 1: Días 1–10 (Foundations)", "Stage 1: Days 1–10 (Foundations)"),
        ("Etapa 2: Días 11–20 (Everyday)", "Stage 2: Days 11–20 (Everyday)"),
        ("Etapa 3: Días 21–30 (Sentences)", "Stage 3: Days 21–30 (Sentences)"),
        ("Etapa 4: Días 31–40 (Communication)", "Stage 4: Days 31–40 (Communication)"),
        ("Etapa 5: Días 41–50 (Preterite Past)", "Stage 5: Days 41–50 (Preterite Past)"),
        ("Etapa 6: Días 51–60 (Consolidation)", "Stage 6: Days 51–60 (Consolidation)"),
        ("<span>Día ${l.day}: ${l.title.substring(0, 22)}...</span>", "<span>Day ${l.day}: ${l.title.substring(0, 22)}...</span>"),

        # Lesson Hero
        ("<span class=\"lesson-badge-tag\">Día ${lesson.day} • Etapa ${lesson.stage}</span>",
         "<span class=\"lesson-badge-tag\">Day ${lesson.day} • Stage ${lesson.stage}</span>"),
        ("← Día Anterior", "← Previous Day"),
        ("Siguiente Día →", "Next Day →"),
        ("<div class=\"goals-title\">🎯 1. Objetivos de Aprendizaje de Hoy</div>",
         "<div class=\"goals-title\">🎯 1. Today's Learning Goals</div>"),

        # Section 2 Vocab
        ("<h3 class=\"section-heading\">Nuevo Vocabulario (Aproximadamente 10 Palabras)</h3>",
         "<h3 class=\"section-heading\">2. New Vocabulary (~10 Words)</h3>"),
        ("title=\"Escuchar todas las palabras en español\"", "title=\"Listen to all words\""),
        ("🔊 Escuchar Todo", "🔊 Listen to All Words"),
        ("title=\"Pronunciar en español\"", "title=\"Listen in Spanish\""),
        ("title=\"Haz clic para escuchar\"", "title=\"Click to listen\""),

        # Section 3 Sentences
        ("<h3 class=\"section-heading\">Frases Cotidianas Prácticas (Spoken Spanish)</h3>",
         "<h3 class=\"section-heading\">3. Useful Everyday Sentences (Spoken Spanish)</h3>"),
        ("title=\"Escuchar pronunciación\"", "title=\"Listen to pronunciation\""),

        # Section 4 Grammar
        ("<h3 class=\"section-heading\">Lección de Gramática: ${lesson.grammar.title}</h3>",
         "<h3 class=\"section-heading\">4. Grammar Lesson: ${lesson.grammar.title}</h3>"),
        ("<div class=\"grammar-structures-title\">Estructura y Fórmulas</div>",
         "<div class=\"grammar-structures-title\">Sentence Structure & Formulas</div>"),
        ("Ejemplos Analizados", "Analyzed Examples"),
        ("<div class=\"cm-title\">⚠️ Errores Comunes de Principiantes</div>",
         "<div class=\"cm-title\">⚠️ Common Beginner Mistakes</div>"),
        ("<strong>Consejo del Profesor (Pro-Tip):</strong>", "<strong>Teacher's Pro-Tip:</strong>"),

        # Section 5 Conversation
        ("<h3 class=\"section-heading\">Práctica de Conversación (Diálogo Realista)</h3>",
         "<h3 class=\"section-heading\">5. Conversation Practice (Realistic Dialogue)</h3>"),
        ("<div class=\"dialogue-context\">📍 Contexto: ${lesson.conversation.context}</div>",
         "<div class=\"dialogue-context\">📍 Context: ${lesson.conversation.context}</div>"),
        ("<div class=\"kp-title\">🔑 Frases Clave del Diálogo</div>",
         "<div class=\"kp-title\">🔑 Key Phrases from Dialogue</div>"),

        # Section 6 Reading
        ("<h3 class=\"section-heading\">Práctica de Lectura: ${lesson.reading.title}</h3>",
         "<h3 class=\"section-heading\">6. Reading Practice: ${lesson.reading.title}</h3>"),
        ("🔊 Escuchar Lectura", "🔊 Listen to Reading Passage"),
        ("🌐 Ver / Ocultar Traducción al Inglés", "🌐 Show / Hide English Translation"),
        ("Preguntas de Comprensión", "Reading Comprehension Questions"),

        # Section 7 Exercises
        ("<h3 class=\"section-heading\">Ejercicios Prácticos Interactivos</h3>",
         "<h3 class=\"section-heading\">7. Interactive Practice Exercises</h3>"),
        ("<span>Ejercicio ${exIdx + 1} de ${lesson.exercises.length}</span>",
         "<span>Exercise ${exIdx + 1} of ${lesson.exercises.length}</span>"),

        # Section 8 Speaking
        ("<h3 class=\"section-heading\">Reto Oral (Speaking Challenge)</h3>",
         "<h3 class=\"section-heading\">8. Speaking Challenge (Answer Aloud in Spanish)</h3>"),
        ("Responde en voz alta en español sin mirar la solución primero. Genera tus propias frases autónomas.",
         "Answer aloud in Spanish without peeking at the answer first. Construct your own independent sentences."),
        ("<div class=\"speaking-q\">Pregunta ${spIdx + 1}: ${sp.question || sp.prompt}</div>",
         "<div class=\"speaking-q\">Question ${spIdx + 1}: ${sp.question || sp.prompt}</div>"),
        ("<div class=\"speaking-hint\">💡 Pista: ${sp.hint}</div>",
         "<div class=\"speaking-hint\">💡 Hint: ${sp.hint}</div>"),
        ("👁️ Revelar Respuesta Sugerida", "👁️ Reveal Suggested Model Answer"),
        ("<strong>Ejemplo:</strong>", "<strong>Model Answer:</strong>"),
        ("🔊 Escuchar", "🔊 Listen"),

        # Section 9 Revision
        ("<h3 class=\"section-heading\">Repaso Diario (Active Recall)</h3>",
         "<h3 class=\"section-heading\">9. Daily Revision (Active Recall)</h3>"),
        ("<div style=\"font-weight: 700; color: var(--red-deep); margin-bottom: 0.75rem;\">Preguntas de Recordación Activa:</div>",
         "<div style=\"font-weight: 700; color: var(--red-deep); margin-bottom: 0.75rem;\">Quick Active Recall Questions:</div>"),
        ("<strong>Regla de Oro:</strong>", "<strong>Golden Rule:</strong>"),

        # Section 10 Checklist
        ("<h3 class=\"section-heading\">Lista de Verificación Diaria (Checklist)</h3>",
         "<h3 class=\"section-heading\">10. Daily Completion Checklist</h3>"),
        ("${isDayCompleted ? '✓ Día Marcado Como Completado' : '🏁 Marcar Día ' + lesson.day + ' Como Completado'}",
         "${isDayCompleted ? '✓ Day Marked as Completed' : '🏁 Mark Day ' + lesson.day + ' as Completed'}"),
        ("Avanzar al Día Siguiente (${lesson.day + 1}) →", "Proceed to Next Day (${lesson.day + 1}) →"),

        # Getting Started View
        ("<span class=\"section-tag\">Parte A • Preparación Fundamental</span>",
         "<span class=\"section-tag\">Part A • Essential Foundations</span>"),
        ("El Alfabeto Español (27 Letras Oficiales)", "The Spanish Alphabet (27 Official Letters)"),
        ("Reglas de Pronunciación del Español de España", "Spain Spanish Pronunciation Rules"),
        ("🚀 ¡Comenzar el Desafío en el Día 1!", "🚀 Start the Challenge with Day 1!"),

        # Dictionary View
        ("<span class=\"section-tag\">Índice Léxico Exhaustivo</span>",
         "<span class=\"section-tag\">Comprehensive Lexical Index</span>"),
        ("<h1 class=\"section-title\">Diccionario Alfabético A-Z (600 Palabras)</h1>",
         "<h1 class=\"section-title\">A-Z Vocabulary Dictionary (600 Words)</h1>"),
        ("<p class=\"section-desc\">El reservorio de vocabulario completo acumulado a lo largo de los 60 días, con buscador instantáneo y audio nativo.</p>",
         "<p class=\"section-desc\">The complete 600-word vocabulary reservoir accumulated across all 60 days, with instant search and native Castilian audio.</p>"),
        ("placeholder=\"🔍 Buscar por palabra en español o inglés...\"",
         "placeholder=\"🔍 Search in Spanish or English...\""),
        ("Todas las Etapas (600 palabras)", "All Stages (600 words)"),
        ("Etapa 1: Días 1–10 (100 palabras)", "Stage 1: Days 1–10 (100 words)"),
        ("Etapa 2: Días 11–20 (100 palabras)", "Stage 2: Days 11–20 (100 words)"),
        ("Etapa 3: Días 21–30 (100 palabras)", "Stage 3: Days 21–30 (100 words)"),
        ("Etapa 4: Días 31–40 (100 palabras)", "Stage 4: Days 31–40 (100 words)"),
        ("Etapa 5: Días 41–50 (100 palabras)", "Stage 5: Days 41–50 (100 words)"),
        ("Etapa 6: Días 51–60 (100 palabras)", "Stage 6: Days 51–60 (100 words)"),
        ("Mostrando ${filtered.length} de 600 palabras", "Showing ${filtered.length} of 600 words"),
        ("<th>Palabra en Español</th>", "<th>Spanish Word</th>"),
        ("<th>Tipo / Género</th>", "<th>Type / Gender</th>"),
        ("<th>Significado en Inglés</th>", "<th>English Meaning</th>"),
        ("<th>Ejemplo de Uso</th>", "<th>Example Sentence</th>"),
        ("<th>Día</th>", "<th>Day</th>"),
        ("<th>Audio</th>", "<th>Audio</th>"),
        ("Día ${v.day}", "Day ${v.day}"),

        # Grammar Reference View
        ("<span class=\"section-tag\">Sección de Consulta Permanente</span>",
         "<span class=\"section-tag\">Master Reference Section</span>"),
        ("<h1 class=\"section-title\">Manual de Referencia Gramatical (Nivel A1)</h1>",
         "<h1 class=\"section-title\">Grammar Reference Handbook (CEFR A1)</h1>"),
        ("<p class=\"section-desc\">Tablas de conjugación completas, esquemas analíticos y reglas esenciales condensadas en 12 capítulos.</p>",
         "<p class=\"section-desc\">Complete conjugation charts, structural rules, and essential grammar tables across 12 comprehensive chapters.</p>"),
        ("Capítulo ${ch.chapter}", "Chapter ${ch.chapter}"),

        # Milestones View
        ("<span class=\"section-tag\">Evaluación de Avance Periódico</span>",
         "<span class=\"section-tag\">Periodic Milestone Assessment</span>"),
        ("<h1 class=\"section-title\">Los 6 Hitos de Aprendizaje (Milestones)</h1>",
         "<h1 class=\"section-title\">The 6 Stage Milestones & Checkpoints</h1>"),
        ("<p class=\"section-desc\">Evaluaciones estratégicas al completar cada bloque de 10 días para medir la consolidación de tu español.</p>",
         "<p class=\"section-desc\">Strategic checkpoint assessments at every 10-day block to measure your Spanish consolidation.</p>"),
        ("Ir al Día ${m.day} →", "Go to Day ${m.day} →"),
        ("<span style=\"font-size: 0.72rem; text-transform: uppercase; color: var(--charcoal-light); font-weight: 700;\">Vocabulario Meta</span>",
         "<span style=\"font-size: 0.72rem; text-transform: uppercase; color: var(--charcoal-light); font-weight: 700;\">Target Vocabulary</span>"),
        ("Palabras</div>", "Words</div>"),
        ("<span style=\"font-size: 0.72rem; text-transform: uppercase; color: var(--charcoal-light); font-weight: 700;\">Días Superados</span>",
         "<span style=\"font-size: 0.72rem; text-transform: uppercase; color: var(--charcoal-light); font-weight: 700;\">Days Completed</span>"),
        ("/ 60 Días</div>", "/ 60 Days</div>"),
        ("<span style=\"font-size: 0.72rem; text-transform: uppercase; color: var(--charcoal-light); font-weight: 700;\">Capacidad Clave</span>",
         "<span style=\"font-size: 0.72rem; text-transform: uppercase; color: var(--charcoal-light); font-weight: 700;\">Key Communicative Skill</span>"),
        ("Test Rápido del Hito ${m.stage}:", "Quick Stage ${m.stage} Checkpoint Quiz:"),
        ("Nota del Tutor para Sakib:", "Instructor Note for Sakib:"),

        # Final Exam View
        ("<span class=\"section-tag\">Evaluación Oficial de Culminación</span>",
         "<span class=\"section-tag\">Official Course Assessment</span>"),
        ("<h1 class=\"section-title\">Examen Final de A1 y Certificado de Logro</h1>",
         "<h1 class=\"section-title\">Final A1 Examination & Achievement Certificate</h1>"),
        ("<p class=\"section-desc\">Evaluación integral de 100 puntos en 5 secciones. Al superar el examen con al menos 60 puntos, desbloquearás tu Certificado Oficial personalizado.</p>",
         "<p class=\"section-desc\">Comprehensive 100-point examination across 5 sections. Score 60 points or higher to unlock your official personalized Certificate of Completion.</p>"),
        ("<div style=\"font-size: 0.75rem; font-weight: 800; text-transform: uppercase; color: var(--charcoal-light);\">Candidato Oficial</div>",
         "<div style=\"font-size: 0.75rem; font-weight: 800; text-transform: uppercase; color: var(--charcoal-light);\">Official Candidate</div>"),
        ("Nivel Destino:", "Target Level:"),
        ("Idioma Materno:", "Native Language:"),
        ("<div style=\"font-size: 0.75rem; font-weight: 800; text-transform: uppercase; color: var(--charcoal-light);\">Puntuación Obtenida</div>",
         "<div style=\"font-size: 0.75rem; font-weight: 800; text-transform: uppercase; color: var(--charcoal-light);\">Score Achieved</div>"),
        ("📝 Enviar y Calificar Examen Final de A1", "📝 Submit & Grade Final A1 Examination"),
        ("Código de Verificación:", "Verification Code:"),
        ("Calificación Final:", "Final Score:"),
        ("Puntos", "Points"),
        ("🖨️ Imprimir / Guardar Certificado en PDF", "🖨️ Print / Save Certificate as PDF"),

        # Alerts and Feedback
        ("¡Felicitaciones! Has completado oficialmente el Día ${dayNum}. ¡Tu esfuerzo te acerca a la meta de A1!",
         "Congratulations! You have officially completed Day ${dayNum}. Great progress toward your A1 goal!"),
        ("¡ENHORABUENA SAKIB! 🎉 Has superado el Examen Final con ${earnedPoints}/100 puntos. Tu Certificado Oficial ha sido desbloqueado.",
         "CONGRATULATIONS SAKIB! 🎉 You passed the Final Exam with ${earnedPoints}/100 points! Your Official Certificate has been unlocked."),
        ("Has obtenido ${earnedPoints}/100 puntos. Se requieren al menos 60 puntos para obtener el certificado. Revisa tus respuestas e inténtalo de nuevo.",
         "You scored ${earnedPoints}/100 points. At least 60 points are required to earn the certificate. Review your answers and try again."),
        ("Avanzar al Día ${m.day} del Hito →", "Proceed to Day ${m.day} Milestone →"),
        ("<strong>Competencias Clave del Hito:</strong>", "<strong>Key Milestone Skills:</strong>")
    ]

    count = 0
    for old, new in replacements:
        if old in code:
            code = code.replace(old, new)
            count += 1
        else:
            print(f"Warning: could not find string: {old[:40]}...")

    with open(path, "w", encoding="utf-8") as f:
        f.write(code)

    print(f"Successfully performed {count} string replacements in js/app.js!")

if __name__ == "__main__":
    update_app_js()
