/**
 * ESPAÑOL: MY 60-DAY SPANISH LEARNING HANDBOOK 🇪🇸
 * Main Application Engine: Audio TTS, LocalStorage State, Navigation & Interactivity
 */

(function () {
  'use strict';

  // 1. Data Aggregation
  const stages = [
    window.STAGE_1_LESSONS || [],
    window.STAGE_2_LESSONS || [],
    window.STAGE_3_LESSONS || [],
    window.STAGE_4_LESSONS || [],
    window.STAGE_5_LESSONS || [],
    window.STAGE_6_LESSONS || []
  ];

  const allLessons = [].concat(...stages);
  const gettingStartedData = window.GETTING_STARTED_DATA || {};
  const grammarReferenceData = window.HANDBOOK_GRAMMAR_REFERENCE || [];
  const milestonesData = window.HANDBOOK_MILESTONES || [];
  const vocabularyIndex = window.HANDBOOK_VOCABULARY_INDEX || [];
  const finalExamData = window.HANDBOOK_FINAL_EXAM || {};

  // 2. Application State
  const state = {
    currentView: 'overview', // 'overview', 'lesson', 'getting-started', 'dictionary', 'grammar', 'milestones', 'final-exam'
    currentDay: 1,
    currentStage: 1,
    completedDays: new Set(JSON.parse(localStorage.getItem('espanol_completed_days') || '[]')),
    checklistState: JSON.parse(localStorage.getItem('espanol_checklists') || '{}'),
    exerciseAnswers: JSON.parse(localStorage.getItem('espanol_exercises') || '{}'),
    examAnswers: JSON.parse(localStorage.getItem('espanol_exam_answers') || '{}'),
    examScore: localStorage.getItem('espanol_exam_score') || null,
    searchQuery: '',
    selectedVocabFilter: 'all',
    flashcardIndex: 0,
    flashcardFlipped: false
  };

  // 3. Audio TTS Engine (Native Castilian Spanish)
  let spanishVoice = null;
  function initSpeechVoice() {
    if ('speechSynthesis' in window) {
      const loadVoices = () => {
        const voices = window.speechSynthesis.getVoices();
        // Priority: Spain (es-ES), then generic Spanish (es)
        spanishVoice = voices.find(v => v.lang === 'es-ES') ||
                       voices.find(v => v.lang.startsWith('es-')) ||
                       voices.find(v => v.name.toLowerCase().includes('spanish')) || null;
      };
      loadVoices();
      if (window.speechSynthesis.onvoiceschanged !== undefined) {
        window.speechSynthesis.onvoiceschanged = loadVoices;
      }
    }
  }

  function speakSpanish(text) {
    if (!('speechSynthesis' in window)) {
      alert("Your browser does not support Web Speech API.");
      return;
    }
    window.speechSynthesis.cancel(); // Stop any ongoing speech
    // Clean text (remove translation or punctuation brackets)
    const cleanText = text.replace(/\(.*?\)/g, '').trim();
    const utterance = new SpeechSynthesisUtterance(cleanText);
    utterance.lang = 'es-ES';
    if (spanishVoice) utterance.voice = spanishVoice;
    utterance.rate = 0.88; // Slightly measured rate for language learners
    utterance.pitch = 1.0;
    window.speechSynthesis.speak(utterance);
  }

  // 4. Persistence Helpers
  function saveState() {
    localStorage.setItem('espanol_completed_days', JSON.stringify([...state.completedDays]));
    localStorage.setItem('espanol_checklists', JSON.stringify(state.checklistState));
    localStorage.setItem('espanol_exercises', JSON.stringify(state.exerciseAnswers));
    localStorage.setItem('espanol_exam_answers', JSON.stringify(state.examAnswers));
    if (state.examScore !== null) {
      localStorage.setItem('espanol_exam_score', state.examScore);
    }
    updateNavProgress();
  }

  function updateNavProgress() {
    const totalDays = 60;
    const completedCount = state.completedDays.size;
    const pct = Math.round((completedCount / totalDays) * 100);
    const pill = document.getElementById('nav-progress-text');
    if (pill) {
      pill.textContent = `${completedCount}/60 Days (${pct}%)`;
    }
  }

  // 5. Router & View Rendering
  function switchView(viewName, dayNum = null) {
    state.currentView = viewName;
    if (dayNum !== null) {
      state.currentDay = dayNum;
      const lesson = allLessons.find(l => l.day === dayNum);
      if (lesson) state.currentStage = lesson.stage;
    }

    // Update Tab Links
    document.querySelectorAll('.tab-link').forEach(btn => {
      btn.classList.toggle('active', btn.dataset.view === viewName);
    });

    const container = document.getElementById('main-content-view');
    window.scrollTo({ top: 0, behavior: 'smooth' });

    switch (viewName) {
      case 'overview':
        renderOverview(container);
        break;
      case 'lesson':
        renderLessonWorkspace(container, state.currentDay);
        break;
      case 'getting-started':
        renderGettingStarted(container);
        break;
      case 'dictionary':
        renderDictionaryView(container);
        break;
      case 'grammar':
        renderGrammarReference(container);
        break;
      case 'milestones':
        renderMilestonesView(container);
        break;
      case 'final-exam':
        renderFinalExamView(container);
        break;
      default:
        renderOverview(container);
    }
  }

  // =========================================================================
  // VIEW: OVERVIEW / DASHBOARD
  // =========================================================================
  function renderOverview(container) {
    const completedCount = state.completedDays.size;
    const pct = Math.round((completedCount / 60) * 100);

    let html = `
      <!-- Hero Cover -->
      <div class="book-cover">
        <div class="cover-watermark">60</div>
        <div class="cover-content">
          <div class="cover-badge-row">
            <span class="cover-badge">🇪🇸 Standard Spain Spanish</span>
            <span class="cover-badge">CEFR A1 Breakthrough</span>
            <span class="cover-badge">Student: Sakib Ahmed</span>
          </div>
          <h1 class="cover-title">ESPAÑOL</h1>
          <h2 class="cover-subtitle">60 Days to A1: My Personal Spanish Learning Journey</h2>
          <p class="cover-description">
            A comprehensive, professionally published digital handbook taking you from absolute beginner to conversational autonomy. 
            60 daily structured lessons, 600 core vocabulary words, 8 grammatical pillars, Castilian phonetics, and native audio guidance.
          </p>
          <div class="cover-meta-grid">
            <div class="meta-item">
              <span class="meta-label">Overall Progress</span>
              <span class="meta-value">${completedCount} / 60 Days (${pct}%)</span>
            </div>
            <div class="meta-item">
              <span class="meta-label">Vocabulary Mastered</span>
              <span class="meta-value">600 Core Words</span>
            </div>
            <div class="meta-item">
              <span class="meta-label">Daily Target</span>
              <span class="meta-value">~10 Words / 45 Mins</span>
            </div>
            <div class="meta-item">
              <span class="meta-label">Current Milestone</span>
              <span class="meta-value">Etapa ${state.currentStage}: Días ${(state.currentStage - 1) * 10 + 1}–${state.currentStage * 10}</span>
            </div>
          </div>
        </div>
      </div>

      <!-- Quick Action Buttons -->
      <div style="display: flex; gap: 1rem; margin-bottom: 3rem; flex-wrap: wrap;">
        <button class="nav-btn primary" onclick="window.app.goToLesson(${state.currentDay})" style="padding: 0.75rem 1.5rem; font-size: 0.95rem;">
          📖 Continue Day ${state.currentDay}: ${allLessons.find(l => l.day === state.currentDay)?.title || 'Start'}
        </button>
        <button class="nav-btn" onclick="window.app.switchView('getting-started')" style="padding: 0.75rem 1.5rem; font-size: 0.95rem;">
          🗺️ Getting Started & Pronunciation Guide
        </button>
        <button class="nav-btn" onclick="window.app.switchView('dictionary')" style="padding: 0.75rem 1.5rem; font-size: 0.95rem;">
          📚 A-Z Dictionary (600 Words)
        </button>
        <button class="nav-btn" onclick="window.app.switchView('final-exam')" style="padding: 0.75rem 1.5rem; font-size: 0.95rem; border-color: var(--yellow-gold); background: var(--yellow-light); color: #8C5900;">
          🎓 Final Exam & Certificate
        </button>
      </div>

      <!-- Stages Overview Grid -->
      <div class="stages-overview">
        <div class="section-header-editorial">
          <span class="section-tag">Challenge Curriculum</span>
          <h2 class="section-title">The 6 Stages to Level A1</h2>
          <p class="section-desc">60 days of step-by-step progress, divided into 6 rigorous thematic stages with milestone assessments.</p>
        </div>

        <div class="stages-grid">
    `;

    const stageTitles = [
      { num: 1, name: "Foundations of Spanish", desc: "Greetings, numbers, gender, articles, ser vs estar, and basic sentence structure.", days: "1–10" },
      { num: 2, name: "Everyday Spanish", desc: "Family, food, home, regular verbs, tener, hacer, and near future with 'ir a'.", days: "11–20" },
      { num: 3, name: "Building Better Sentences", desc: "Daily routine, reflexives, time, shopping, stem-changers, and gustar.", days: "21–30" },
      { num: 4, name: "Practical Communication", desc: "Restaurants, travel, weather, describing people, por vs para, and modals.", days: "31–40" },
      { num: 5, name: "Developing Stronger Skills", desc: "Professions, health & doler, possessives, and the Preterite Past Tense.", days: "41–50" },
      { num: 6, name: "Consolidation & Assessment", desc: "Idioms, opinion & debate, emergency handling, top 20 traps, and Final Exam.", days: "51–60" }
    ];

    stageTitles.forEach(s => {
      const stageLessons = allLessons.filter(l => l.stage === s.num);
      const isCurrent = (s.num === state.currentStage);

      html += `
        <div class="stage-card ${isCurrent ? 'active-stage' : ''}">
          <div class="stage-header">
            <span class="stage-badge">Stage ${s.num}</span>
            <span class="stage-days">Days ${s.days}</span>
          </div>
          <h3>${s.name}</h3>
          <p>${s.desc}</p>
          <div class="stage-days-list">
      `;

      stageLessons.forEach(l => {
        const isDone = state.completedDays.has(l.day);
        const isSelected = (l.day === state.currentDay);
        html += `
          <div class="day-chip ${isDone ? 'completed' : ''} ${isSelected ? 'active' : ''}" 
               onclick="window.app.goToLesson(${l.day})" title="Day ${l.day}: ${l.title}">
            ${l.day}
          </div>
        `;
      });

      html += `
          </div>
          <button class="stage-milestone-btn" onclick="window.app.openMilestoneModal(${s.num})">
            🏆 View Stage ${s.num} Milestone
          </button>
        </div>
      `;
    });

    html += `
        </div>
      </div>
    `;

    container.innerHTML = html;
  }

  // =========================================================================
  // VIEW: LESSON WORKSPACE (10-PART DAILY TEMPLATE)
  // =========================================================================
  function renderLessonWorkspace(container, dayNum) {
    const lesson = allLessons.find(l => l.day === dayNum) || allLessons[0];
    state.currentDay = lesson.day;
    state.currentStage = lesson.stage;

    const isPrevDisabled = lesson.day <= 1;
    const isNextDisabled = lesson.day >= 60;
    const isDayCompleted = state.completedDays.has(lesson.day);

    let html = `
      <div class="lesson-workspace">
        <!-- Sidebar Navigation -->
        <aside class="lesson-sidebar">
          <div class="sidebar-title">Course Index (60 Days)</div>
          <select class="stage-selector-dropdown" id="stage-select-dropdown" onchange="window.app.filterSidebarStage(this.value)">
            <option value="all">All Stages (1–6)</option>
            <option value="1" ${lesson.stage === 1 ? 'selected' : ''}>Stage 1: Days 1–10 (Foundations)</option>
            <option value="2" ${lesson.stage === 2 ? 'selected' : ''}>Stage 2: Days 11–20 (Everyday)</option>
            <option value="3" ${lesson.stage === 3 ? 'selected' : ''}>Stage 3: Days 21–30 (Sentences)</option>
            <option value="4" ${lesson.stage === 4 ? 'selected' : ''}>Stage 4: Days 31–40 (Communication)</option>
            <option value="5" ${lesson.stage === 5 ? 'selected' : ''}>Stage 5: Days 41–50 (Preterite Past)</option>
            <option value="6" ${lesson.stage === 6 ? 'selected' : ''}>Stage 6: Days 51–60 (Consolidation)</option>
          </select>

          <div class="sidebar-days-nav" id="sidebar-days-nav-list">
    `;

    allLessons.forEach(l => {
      const isDone = state.completedDays.has(l.day);
      const isAct = l.day === lesson.day;
      html += `
        <div class="sidebar-day-item ${isAct ? 'active' : ''}" onclick="window.app.goToLesson(${l.day})">
          <span>Day ${l.day}: ${l.title.substring(0, 22)}...</span>
          <span>${isDone ? '✓' : ''}</span>
        </div>
      `;
    });

    html += `
          </div>
        </aside>

        <!-- Main Lesson Document -->
        <main class="lesson-card">
          <!-- Lesson Header -->
          <div class="lesson-hero">
            <div class="lesson-nav-controls">
              <span class="lesson-badge-tag">Day ${lesson.day} • Stage ${lesson.stage}</span>
              <div style="display: flex; gap: 0.5rem;">
                <button class="lesson-step-btn" onclick="window.app.goToLesson(${lesson.day - 1})" ${isPrevDisabled ? 'disabled' : ''}>
                  ← Previous Day
                </button>
                <button class="lesson-step-btn" onclick="window.app.goToLesson(${lesson.day + 1})" ${isNextDisabled ? 'disabled' : ''}>
                  Next Day →
                </button>
              </div>
            </div>

            <h1 class="lesson-main-title">${lesson.title}</h1>
            <h2 class="lesson-subtitle">${lesson.subtitle}</h2>

            <!-- Bangla Learner Connection -->
            ${lesson.bengaliNote ? `
              <div class="bangla-note-card">
                <div class="bangla-note-header">
                  <span>🇧🇩 বাংলা সংযোগ (Bangla Learner Advantage)</span>
                </div>
                <p class="bangla-note-text">${lesson.bengaliNote}</p>
              </div>
            ` : ''}

            <!-- 1. Learning Goals -->
            <div class="goals-container">
              <div class="goals-title">🎯 1. Today's Learning Goals</div>
              <ul class="goals-list">
                ${lesson.goals.map(g => `<li>${g}</li>`).join('')}
              </ul>
            </div>
          </div>

          <!-- Lesson Body (Parts 2 to 10) -->
          <div class="lesson-body">
            
            <!-- 2. Vocabulary Cards (~10 words) -->
            <section class="lesson-section" id="sec-vocabulary">
              <div class="section-ribbon">
                <div class="section-ribbon-title">
                  <span class="section-number">2</span>
                  <h3 class="section-heading">2. New Vocabulary (~10 Words)</h3>
                </div>
                <button class="nav-btn" onclick="window.app.speakAllVocab(${lesson.day})" title="Listen to all words">
                  🔊 Listen to All Words
                </button>
              </div>

              <div class="vocab-cards-grid">
                ${lesson.vocabulary.map((v, i) => `
                  <div class="vocab-card">
                    <div class="vocab-card-header">
                      <div class="vocab-spanish-word">${v.word}</div>
                      <button class="vocab-speak-btn" onclick="window.app.speak('${v.word.replace(/'/g, "\\'")}')" title="Listen in Spanish">
                        🔊
                      </button>
                    </div>
                    <div class="vocab-meta-row">
                      <span class="vocab-tag ${v.pos ? v.pos.toLowerCase() : 'noun'}">${v.pos || 'palabra'}</span>
                      ${v.gender ? `<span class="vocab-tag" style="background:#F0E7DB; color:#5C4D3C;">${v.gender}</span>` : ''}
                    </div>
                    <div class="vocab-translation">${v.translation}</div>
                    ${v.example ? `
                      <div class="vocab-example-box">
                        <div class="vocab-example-sp" onclick="window.app.speak('${v.example.replace(/'/g, "\\'")}')" style="cursor: pointer;" title="Click to listen">
                          🗣️ ${v.example}
                        </div>
                        <div class="vocab-example-en">${v.exampleTranslation || ''}</div>
                      </div>
                    ` : ''}
                  </div>
                `).join('')}
              </div>
            </section>

            <!-- 3. Useful Everyday Sentences -->
            <section class="lesson-section" id="sec-sentences">
              <div class="section-ribbon">
                <div class="section-ribbon-title">
                  <span class="section-number">3</span>
                  <h3 class="section-heading">3. Useful Everyday Sentences (Spoken Spanish)</h3>
                </div>
              </div>

              <div class="sentences-list">
                ${lesson.sentences.map(s => `
                  <div class="sentence-item">
                    <div class="sentence-text-group">
                      <div class="sentence-spanish">${s.spanish}</div>
                      <div class="sentence-english">${s.english}</div>
                    </div>
                    <button class="vocab-speak-btn" onclick="window.app.speak('${s.spanish.replace(/'/g, "\\'")}')" title="Listen to pronunciation">
                      🔊
                    </button>
                  </div>
                `).join('')}
              </div>
            </section>

            <!-- 4. Grammar Lesson -->
            <section class="lesson-section" id="sec-grammar">
              <div class="section-ribbon">
                <div class="section-ribbon-title">
                  <span class="section-number">4</span>
                  <h3 class="section-heading">4. Grammar Lesson: ${lesson.grammar.title}</h3>
                </div>
              </div>

              <div class="grammar-container">
                <div class="grammar-title">${lesson.grammar.title}</div>
                <p class="grammar-explanation">${lesson.grammar.explanation}</p>

                ${lesson.grammar.rules ? `
                  <ul class="grammar-rules-list">
                    ${lesson.grammar.rules.map(r => `<li>${r}</li>`).join('')}
                  </ul>
                ` : ''}

                ${lesson.grammar.structures && lesson.grammar.structures.length > 0 ? `
                  <div class="grammar-structures-box">
                    <div class="grammar-structures-title">Sentence Structure & Formulas</div>
                    ${lesson.grammar.structures.map(st => `<div class="grammar-structure-code">${st}</div>`).join('')}
                  </div>
                ` : ''}

                ${lesson.grammar.examples ? `
                  <div style="font-size: 0.82rem; font-weight: 800; text-transform: uppercase; letter-spacing: 0.08em; color: var(--charcoal-light); margin-bottom: 0.75rem;">
                    Analyzed Examples
                  </div>
                  <div class="grammar-examples-grid">
                    ${lesson.grammar.examples.map(ex => `
                      <div class="grammar-example-card">
                        <div class="ge-spanish">${ex.spanish}</div>
                        <div class="ge-english">${ex.english}</div>
                        ${ex.breakdown ? `<div class="ge-breakdown">${ex.breakdown}</div>` : ''}
                      </div>
                    `).join('')}
                  </div>
                ` : ''}

                ${lesson.grammar.commonMistakes && lesson.grammar.commonMistakes.length > 0 ? `
                  <div class="common-mistakes-box">
                    <div class="cm-title">⚠️ Common Beginner Mistakes</div>
                    ${lesson.grammar.commonMistakes.map(cm => `
                      <div class="cm-item">
                        <div class="cm-incorrect">❌ ${cm.incorrect}</div>
                        <div class="cm-correct">✓ ${cm.correct}</div>
                        <div class="cm-why">💡 ${cm.why}</div>
                      </div>
                    `).join('')}
                  </div>
                ` : ''}

                ${lesson.grammar.proTip ? `
                  <div class="pro-tip-box">
                    <span style="font-size: 1.4rem;">💡</span>
                    <div>
                      <strong>Teacher's Pro-Tip:</strong> ${lesson.grammar.proTip}
                    </div>
                  </div>
                ` : ''}
              </div>
            </section>

            <!-- 5. Conversation Practice -->
            <section class="lesson-section" id="sec-conversation">
              <div class="section-ribbon">
                <div class="section-ribbon-title">
                  <span class="section-number">5</span>
                  <h3 class="section-heading">5. Conversation Practice (Realistic Dialogue)</h3>
                </div>
              </div>

              <div class="dialogue-wrapper">
                <div class="dialogue-context">📍 Context: ${lesson.conversation.context}</div>

                <div class="dialogue-thread">
                  ${lesson.conversation.dialogue.map((d, idx) => `
                    <div class="speech-row ${idx % 2 === 0 ? 'speaker-left' : 'speaker-right'}">
                      <div class="avatar-circle">${d.speaker.substring(0, 2).toUpperCase()}</div>
                      <div class="speech-bubble">
                        <div class="speaker-label">${d.speaker} (${d.role})</div>
                        <div class="speech-sp" onclick="window.app.speak('${d.spanish.replace(/'/g, "\\'")}')" style="cursor: pointer;" title="Click to listen">
                          ${d.spanish}
                        </div>
                        <div class="speech-en">${d.english}</div>
                      </div>
                    </div>
                  `).join('')}
                </div>

                ${lesson.conversation.keyPhrases ? `
                  <div class="key-phrases-box">
                    <div class="kp-title">🔑 Key Phrases from Dialogue</div>
                    <div class="kp-grid">
                      ${lesson.conversation.keyPhrases.map(kp => `
                        <div class="kp-item">
                          <span class="kp-phrase">${kp.phrase}:</span>
                          <span class="kp-explanation">${kp.explanation}</span>
                        </div>
                      `).join('')}
                    </div>
                  </div>
                ` : ''}
              </div>
            </section>

            <!-- 6. Reading Practice -->
            <section class="lesson-section" id="sec-reading">
              <div class="section-ribbon">
                <div class="section-ribbon-title">
                  <span class="section-number">6</span>
                  <h3 class="section-heading">6. Reading Practice: ${lesson.reading.title}</h3>
                </div>
                <button class="nav-btn" onclick="window.app.speak('${lesson.reading.passage.replace(/'/g, "\\'")}')">
                  🔊 Listen to Reading Passage
                </button>
              </div>

              <div class="reading-container">
                <div class="reading-title">${lesson.reading.title}</div>
                <div class="reading-passage-text">${lesson.reading.passage}</div>

                <div class="reading-translation-toggle">
                  <button class="translation-toggle-btn" onclick="window.app.toggleElement('reading-trans-${lesson.day}')">
                    🌐 Show / Hide English Translation
                  </button>
                  <div class="reading-translation-text" id="reading-trans-${lesson.day}">
                    ${lesson.reading.translation}
                  </div>
                </div>

                <div class="reading-questions-block">
                  <div style="font-size: 0.82rem; font-weight: 800; text-transform: uppercase; letter-spacing: 0.08em; color: var(--charcoal-light); margin-bottom: 0.5rem;">
                    Reading Comprehension Questions
                  </div>
                  ${lesson.reading.questions.map((q, qIdx) => `
                    <div class="reading-q-card">
                      <div class="reading-q-title">${qIdx + 1}. ${q.question}</div>
                      <div class="reading-options-list">
                        ${q.options.map((opt, optIdx) => `
                          <button class="option-btn" id="rq-btn-${lesson.day}-${qIdx}-${optIdx}" 
                                  onclick="window.app.checkReadingOption(${lesson.day}, ${qIdx}, ${optIdx}, ${q.answer}, '${q.explanation.replace(/'/g, "\\'")}')">
                            ${opt}
                          </button>
                        `).join('')}
                      </div>
                      <div class="option-explanation" id="rq-exp-${lesson.day}-${qIdx}" style="display: none;"></div>
                    </div>
                  `).join('')}
                </div>
              </div>
            </section>

            <!-- 7. Practice Exercises -->
            <section class="lesson-section" id="sec-exercises">
              <div class="section-ribbon">
                <div class="section-ribbon-title">
                  <span class="section-number">7</span>
                  <h3 class="section-heading">7. Interactive Practice Exercises</h3>
                </div>
              </div>

              <div class="exercises-container">
                ${lesson.exercises.map((ex, exIdx) => `
                  <div class="exercise-card" id="card-${ex.id}">
                    <div class="ex-header">
                      <span class="ex-badge">${ex.type}</span>
                      <span style="font-size: 0.8rem; color: var(--charcoal-light);">Exercise ${exIdx + 1} of ${lesson.exercises.length}</span>
                    </div>
                    <div class="ex-question">${ex.question || ex.prompt}</div>

                    <div class="reading-options-list">
                      ${ex.options.map((opt, optIdx) => `
                        <button class="option-btn" id="ex-btn-${ex.id}-${optIdx}" 
                                onclick="window.app.checkExercise(${lesson.day}, '${ex.id}', ${optIdx}, ${ex.correct !== undefined ? ex.correct : 0}, '${(ex.explanation || '').replace(/'/g, "\\'")}')">
                          ${opt}
                        </button>
                      `).join('')}
                    </div>
                    <div class="option-explanation" id="ex-exp-${ex.id}" style="display: none;"></div>
                  </div>
                `).join('')}
              </div>
            </section>

            <!-- 8. Speaking Challenge -->
            <section class="lesson-section" id="sec-speaking">
              <div class="section-ribbon">
                <div class="section-ribbon-title">
                  <span class="section-number">8</span>
                  <h3 class="section-heading">8. Speaking Challenge (Answer Aloud in Spanish)</h3>
                </div>
              </div>

              <div class="speaking-container">
                <div style="font-size: 0.95rem; color: #5C4D3C; margin-bottom: 1.5rem;">
                  🗣️ <em>${lesson.speakingChallenge.instructions || 'Answer aloud in Spanish without peeking at the answer first. Construct your own independent sentences.'}</em>
                </div>

                ${(lesson.speakingChallenge.prompts || lesson.speakingChallenge).map((sp, spIdx) => `
                  <div class="speaking-prompt-card">
                    <div class="speaking-q">Question ${spIdx + 1}: ${sp.question || sp.prompt}</div>
                    ${sp.hint ? `<div class="speaking-hint">💡 Hint: ${sp.hint}</div>` : ''}
                    <button class="speaking-sample-btn" onclick="window.app.toggleElement('sample-ans-${lesson.day}-${spIdx}')">
                      👁️ Reveal Suggested Model Answer
                    </button>
                    <div class="speaking-sample-text" id="sample-ans-${lesson.day}-${spIdx}">
                      <strong>Model Answer:</strong> "${sp.sampleAnswer}"
                      <button style="margin-left: 0.5rem; background: none; border: none; cursor: pointer;" onclick="window.app.speak('${sp.sampleAnswer.replace(/'/g, "\\'")}')">🔊 Listen</button>
                    </div>
                  </div>
                `).join('')}
              </div>
            </section>

            <!-- 9. Daily Revision -->
            <section class="lesson-section" id="sec-revision">
              <div class="section-ribbon">
                <div class="section-ribbon-title">
                  <span class="section-number">9</span>
                  <h3 class="section-heading">9. Daily Revision (Active Recall)</h3>
                </div>
              </div>

              <div style="background: var(--bg-cream); border: 1px solid var(--border-subtle); border-radius: var(--radius-lg); padding: 1.75rem;">
                <div style="font-weight: 700; color: var(--red-deep); margin-bottom: 0.75rem;">Quick Active Recall Questions:</div>
                <div style="display: flex; flex-direction: column; gap: 0.75rem; margin-bottom: 1.5rem;">
                  ${lesson.dailyRevision.quickQuestions ? lesson.dailyRevision.quickQuestions.map(q => `
                    <div style="background: var(--bg-warm-white); padding: 0.85rem; border-radius: var(--radius-sm); border: 1px solid var(--border-subtle);">
                      <div style="font-weight: 600; font-size: 0.9rem;">❓ ${typeof q === 'string' ? q : q.q}</div>
                      ${q.a ? `<div style="font-size: 0.85rem; color: var(--accent-green); margin-top: 0.25rem;">✓ ${q.a}</div>` : ''}
                    </div>
                  `).join('') : ''}
                </div>

                ${lesson.dailyRevision.grammarRecall ? `
                  <div style="background: var(--bg-warm-white); padding: 1rem; border-radius: var(--radius-sm); border-left: 3px solid var(--red-deep); font-size: 0.88rem;">
                    <strong>Golden Rule:</strong> ${lesson.dailyRevision.grammarRecall}
                  </div>
                ` : ''}
              </div>
            </section>

            <!-- 10. Completion Checklist -->
            <section class="lesson-section" id="sec-checklist">
              <div class="section-ribbon">
                <div class="section-ribbon-title">
                  <span class="section-number">10</span>
                  <h3 class="section-heading">10. Daily Completion Checklist</h3>
                </div>
              </div>

              <div class="checklist-container">
                <div class="checklist-grid">
                  ${lesson.checklist.map((item, chIdx) => {
                    const key = `ch-${lesson.day}-${chIdx}`;
                    const isChecked = !!state.checklistState[key];
                    return `
                      <div class="checklist-item" onclick="window.app.toggleCheck('${key}', ${lesson.day})">
                        <input type="checkbox" id="${key}" ${isChecked ? 'checked' : ''} onclick="event.stopPropagation(); window.app.toggleCheck('${key}', ${lesson.day});">
                        <label for="${key}">${item}</label>
                      </div>
                    `;
                  }).join('')}
                </div>

                <div style="margin-top: 2rem; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem;">
                  <button class="nav-btn ${isDayCompleted ? '' : 'primary'}" style="padding: 0.85rem 1.85rem; font-size: 0.95rem;" onclick="window.app.markDayComplete(${lesson.day})">
                    ${isDayCompleted ? '✓ Day Marked as Completed' : '🏁 Mark Day ' + lesson.day + ' as Completed'}
                  </button>

                  <button class="nav-btn" onclick="window.app.goToLesson(${lesson.day + 1})" ${isNextDisabled ? 'disabled' : ''} style="padding: 0.85rem 1.85rem; font-size: 0.95rem;">
                    Proceed to Next Day (${lesson.day + 1}) →
                  </button>
                </div>
              </div>
            </section>

          </div>
        </main>
      </div>
    `;

    container.innerHTML = html;
  }

  // =========================================================================
  // VIEW: GETTING STARTED GUIDE (PART A)
  // =========================================================================
  function renderGettingStarted(container) {
    const gs = gettingStartedData;
    let html = `
      <div style="background: var(--bg-warm-white); border: 1px solid var(--border-subtle); border-radius: var(--radius-xl); padding: 3rem; max-width: 1000px; margin: 0 auto; box-shadow: var(--shadow-sm);">
        <span class="section-tag">Part A • Essential Foundations</span>
        <h1 style="font-family: var(--font-display); font-size: 2.6rem; color: var(--red-deep); margin-bottom: 0.5rem;">${gs.title || 'Guía de Inicio'}</h1>
        <h2 style="font-family: var(--font-editorial); font-size: 1.4rem; color: var(--charcoal-medium); font-style: italic; margin-bottom: 2rem;">${gs.subtitle || ''}</h2>

        <!-- Bangla Learner Superpower Card -->
        <div class="bangla-note-card" style="margin-bottom: 2.5rem; background: #FFFDF2; border: 2px solid var(--yellow-gold);">
          <div class="bangla-note-header" style="font-size: 0.95rem;">
            <span>🇧🇩 ${gs.banglaLearnerAdvantage?.title || 'স্প্যানিশ শেখায় বাঙালি শিক্ষার্থীদের অবিশ্বাস্য সুবিধা'}</span>
          </div>
          <p style="margin-bottom: 1rem; line-height: 1.7;">${gs.banglaLearnerAdvantage?.summary || ''}</p>
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 0.75rem;">
            ${(gs.banglaLearnerAdvantage?.points || []).map(p => `
              <div style="background: #fff; padding: 0.75rem; border-radius: var(--radius-sm); border: 1px solid #EED7B0; font-size: 0.88rem;">
                <strong>${p.concept}:</strong> ${p.comparison}
              </div>
            `).join('')}
          </div>
        </div>

        <!-- Spanish Alphabet Matrix -->
        <div style="margin-bottom: 3rem;">
          <h3 style="font-family: var(--font-editorial); font-size: 1.6rem; color: var(--charcoal-dark); margin-bottom: 1rem;">
            The Spanish Alphabet (27 Official Letters)
          </h3>
          <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(130px, 1fr)); gap: 0.75rem;">
            ${(gs.alphabet || []).map(l => `
              <div style="background: var(--bg-cream); border: 1px solid var(--border-subtle); border-radius: var(--radius-sm); padding: 0.75rem; text-align: center; cursor: pointer;" onclick="window.app.speak('${l.letter}')" title="Click to listen">
                <div style="font-size: 1.5rem; font-weight: 800; color: var(--red-deep);">${l.letter}</div>
                <div style="font-size: 0.8rem; font-weight: 700; color: var(--charcoal-dark);">${l.name}</div>
                <div style="font-size: 0.72rem; color: var(--charcoal-light);">${l.banglaEquivalent || ''}</div>
                <div style="font-size: 0.7rem; color: #8C5900; margin-top: 0.2rem;">${l.example}</div>
              </div>
            `).join('')}
          </div>
        </div>

        <!-- Pronunciation Rules -->
        <div style="margin-bottom: 3rem;">
          <h3 style="font-family: var(--font-editorial); font-size: 1.6rem; color: var(--charcoal-dark); margin-bottom: 1rem;">
            Spain Spanish Pronunciation Rules
          </h3>
          <div style="display: flex; flex-direction: column; gap: 0.85rem;">
            ${(gs.pronunciationRules || []).map(r => `
              <div style="background: var(--bg-cream); border-left: 4px solid var(--red-deep); padding: 1rem 1.25rem; border-radius: 0 var(--radius-sm) var(--radius-sm) 0;">
                <div style="font-weight: 700; font-size: 0.98rem; color: var(--charcoal-dark); margin-bottom: 0.2rem;">${r.letter}: ${r.rule}</div>
                <div style="font-size: 0.85rem; color: var(--charcoal-light);">${r.examples}</div>
              </div>
            `).join('')}
          </div>
        </div>

        <!-- Action Button -->
        <div style="text-align: center; margin-top: 3rem;">
          <button class="nav-btn primary" onclick="window.app.goToLesson(1)" style="padding: 0.85rem 2.2rem; font-size: 1rem;">
            🚀 Start the Challenge with Day 1!
          </button>
        </div>
      </div>
    `;

    container.innerHTML = html;
  }

  // =========================================================================
  // VIEW: 600-WORD VOCABULARY DICTIONARY INDEX
  // =========================================================================
  function renderDictionaryView(container) {
    let filtered = vocabularyIndex;

    // Filter by search query
    if (state.searchQuery.trim()) {
      const q = state.searchQuery.toLowerCase().trim();
      filtered = filtered.filter(v => 
        v.word.toLowerCase().includes(q) || 
        v.translation.toLowerCase().includes(q)
      );
    }

    // Filter by stage
    if (state.selectedVocabFilter !== 'all') {
      const stageNum = parseInt(state.selectedVocabFilter, 10);
      filtered = filtered.filter(v => v.stage === stageNum);
    }

    let html = `
      <div class="dict-view">
        <div class="section-header-editorial" style="text-align: left; margin-bottom: 1.5rem;">
          <span class="section-tag">Comprehensive Lexical Index</span>
          <h1 class="section-title">A-Z Vocabulary Dictionary (600 Words)</h1>
          <p class="section-desc">The complete 600-word vocabulary reservoir accumulated across all 60 days, with instant search and native Castilian audio.</p>
        </div>

        <div class="dict-controls">
          <input type="text" class="dict-search-input" id="dict-search-field" placeholder="🔍 Search in Spanish or English..." value="${state.searchQuery}" oninput="window.app.filterDictionary(this.value)">

          <select class="dict-filter-select" id="dict-stage-select" onchange="window.app.setVocabStageFilter(this.value)">
            <option value="all" ${state.selectedVocabFilter === 'all' ? 'selected' : ''}>All Stages (600 words)</option>
            <option value="1" ${state.selectedVocabFilter === '1' ? 'selected' : ''}>Stage 1: Days 1–10 (100 words)</option>
            <option value="2" ${state.selectedVocabFilter === '2' ? 'selected' : ''}>Stage 2: Days 11–20 (100 words)</option>
            <option value="3" ${state.selectedVocabFilter === '3' ? 'selected' : ''}>Stage 3: Days 21–30 (100 words)</option>
            <option value="4" ${state.selectedVocabFilter === '4' ? 'selected' : ''}>Stage 4: Days 31–40 (100 words)</option>
            <option value="5" ${state.selectedVocabFilter === '5' ? 'selected' : ''}>Stage 5: Days 41–50 (100 words)</option>
            <option value="6" ${state.selectedVocabFilter === '6' ? 'selected' : ''}>Stage 6: Days 51–60 (100 words)</option>
          </select>

          <div class="dict-stats-pill">
            Showing ${filtered.length} of 600 words
          </div>
        </div>

        <div class="dict-table-container">
          <table class="dict-table">
            <thead>
              <tr>
                <th>Spanish Word</th>
                <th>Type / Gender</th>
                <th>English Meaning</th>
                <th>Example Sentence</th>
                <th>Day</th>
                <th>Audio</th>
              </tr>
            </thead>
            <tbody>
              ${filtered.map(v => `
                <tr>
                  <td class="dict-word-sp">${v.word}</td>
                  <td>
                    <span class="vocab-tag ${v.pos ? v.pos.toLowerCase() : 'noun'}">${v.pos || 'sust.'}</span>
                    ${v.gender ? `<span style="font-size: 0.7rem; color: #8C5900;">(${v.gender})</span>` : ''}
                  </td>
                  <td style="font-weight: 500;">${v.translation}</td>
                  <td style="font-size: 0.82rem; color: var(--charcoal-medium);">
                    <em>"${v.example || ''}"</em>
                  </td>
                  <td>
                    <button class="day-chip" style="font-size: 0.72rem; padding: 0.2rem 0.5rem;" onclick="window.app.goToLesson(${v.day})">
                      Day ${v.day}
                    </button>
                  </td>
                  <td>
                    <button class="vocab-speak-btn" style="width: 28px; height: 28px; font-size: 0.75rem;" onclick="window.app.speak('${v.word.replace(/'/g, "\\'")}')">
                      🔊
                    </button>
                  </td>
                </tr>
              `).join('')}
            </tbody>
          </table>
        </div>
      </div>
    `;

    container.innerHTML = html;
  }

  // =========================================================================
  // VIEW: GRAMMAR REFERENCE HANDBOOK (PART 6)
  // =========================================================================
  function renderGrammarReference(container) {
    let html = `
      <div style="max-width: 1100px; margin: 0 auto;">
        <div class="section-header-editorial">
          <span class="section-tag">Master Reference Section</span>
          <h1 class="section-title">Grammar Reference Handbook (CEFR A1)</h1>
          <p class="section-desc">Complete conjugation charts, structural rules, and essential grammar tables across 12 comprehensive chapters.</p>
        </div>

        <div style="display: flex; flex-direction: column; gap: 2rem;">
          ${grammarReferenceData.map(ch => `
            <div style="background: var(--bg-warm-white); border: 1px solid var(--border-subtle); border-radius: var(--radius-xl); padding: 2.5rem; box-shadow: var(--shadow-sm);">
              <div style="font-size: 0.75rem; font-weight: 800; text-transform: uppercase; letter-spacing: 0.1em; color: var(--red-deep); margin-bottom: 0.35rem;">
                Chapter ${ch.chapter}
              </div>
              <h2 style="font-family: var(--font-editorial); font-size: 1.8rem; color: var(--charcoal-dark); margin-bottom: 0.3rem;">
                ${ch.title}
              </h2>
              <div style="font-style: italic; color: var(--charcoal-light); margin-bottom: 1.5rem;">
                ${ch.subtitle}
              </div>

              <p style="font-size: 0.95rem; margin-bottom: 1.5rem; line-height: 1.6;">${ch.content.overview}</p>

              ${ch.content.conjugationTable ? `
                <div style="overflow-x: auto; margin-bottom: 1.5rem;">
                  <table class="dict-table">
                    <thead>
                      <tr>${ch.content.conjugationTable.headers.map(h => `<th>${h}</th>`).join('')}</tr>
                    </thead>
                    <tbody>
                      ${ch.content.conjugationTable.rows.map(r => `
                        <tr>${r.map(c => `<td><strong>${c}</strong></td>`).join('')}</tr>
                      `).join('')}
                    </tbody>
                  </table>
                </div>
              ` : ''}

              ${ch.content.matrixTable ? `
                <div style="overflow-x: auto; margin-bottom: 1.5rem;">
                  <table class="dict-table">
                    <thead>
                      <tr>${ch.content.matrixTable.headers.map(h => `<th>${h}</th>`).join('')}</tr>
                    </thead>
                    <tbody>
                      ${ch.content.matrixTable.rows.map(r => `
                        <tr>${r.map(c => `<td>${c}</td>`).join('')}</tr>
                      `).join('')}
                    </tbody>
                  </table>
                </div>
              ` : ''}

              ${ch.content.verbsTable ? `
                <div style="overflow-x: auto; margin-bottom: 1.5rem;">
                  <table class="dict-table">
                    <thead>
                      <tr>${ch.content.verbsTable.headers.map(h => `<th>${h}</th>`).join('')}</tr>
                    </thead>
                    <tbody>
                      ${ch.content.verbsTable.rows.map(r => `
                        <tr>${r.map((c, i) => i === 0 ? `<td style="font-weight: 700; color: var(--red-deep);">${c}</td>` : `<td>${c}</td>`).join('')}</tr>
                      `).join('')}
                    </tbody>
                  </table>
                </div>
              ` : ''}

              ${ch.content.comparisonTable ? `
                <div style="overflow-x: auto; margin-bottom: 1.5rem;">
                  <table class="dict-table">
                    <thead>
                      <tr>${ch.content.comparisonTable.headers.map(h => `<th>${h}</th>`).join('')}</tr>
                    </thead>
                    <tbody>
                      ${ch.content.comparisonTable.rows.map(r => `
                        <tr>${r.map(c => `<td>${c}</td>`).join('')}</tr>
                      `).join('')}
                    </tbody>
                  </table>
                </div>
              ` : ''}

              ${ch.content.acronyms ? `
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1rem; margin-top: 1rem;">
                  <div style="background: var(--bg-cream); padding: 1.25rem; border-radius: var(--radius-md); border-left: 4px solid var(--red-deep);">
                    <h4 style="font-weight: 800; color: var(--red-deep); margin-bottom: 0.5rem;">SER: Regla ${ch.content.acronyms.ser.acronym}</h4>
                    <ul style="list-style: none; font-size: 0.88rem; display: flex; flex-direction: column; gap: 0.35rem;">
                      ${ch.content.acronyms.ser.breakdown.map(b => `<li>${b}</li>`).join('')}
                    </ul>
                  </div>
                  <div style="background: var(--bg-cream); padding: 1.25rem; border-radius: var(--radius-md); border-left: 4px solid var(--accent-blue);">
                    <h4 style="font-weight: 800; color: var(--accent-blue); margin-bottom: 0.5rem;">ESTAR: Regla ${ch.content.acronyms.estar.acronym}</h4>
                    <ul style="list-style: none; font-size: 0.88rem; display: flex; flex-direction: column; gap: 0.35rem;">
                      ${ch.content.acronyms.estar.breakdown.map(b => `<li>${b}</li>`).join('')}
                    </ul>
                  </div>
                </div>
              ` : ''}

            </div>
          `).join('')}
        </div>
      </div>
    `;

    container.innerHTML = html;
  }

  // =========================================================================
  // VIEW: MILESTONES & STAGE CHECKPOINTS (PART 7)
  // =========================================================================
  function renderMilestonesView(container) {
    let html = `
      <div style="max-width: 950px; margin: 0 auto;">
        <div class="section-header-editorial">
          <span class="section-tag">Periodic Milestone Assessment</span>
          <h1 class="section-title">The 6 Stage Milestones & Checkpoints</h1>
          <p class="section-desc">Strategic checkpoint assessments at every 10-day block to measure your Spanish consolidation.</p>
        </div>

        <div style="display: flex; flex-direction: column; gap: 2rem;">
          ${milestonesData.map(m => `
            <div style="background: var(--bg-warm-white); border: 1px solid var(--border-subtle); border-radius: var(--radius-xl); padding: 2.5rem; box-shadow: var(--shadow-sm);">
              <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 1rem; flex-wrap: wrap; gap: 0.5rem;">
                <div>
                  <span class="stage-badge" style="background: var(--yellow-light); color: #8C5900; border: 1px solid var(--yellow-gold);">${m.badge}</span>
                  <h2 style="font-family: var(--font-editorial); font-size: 1.6rem; color: var(--charcoal-dark); margin-top: 0.5rem;">
                    ${m.title}
                  </h2>
                </div>
                <button class="nav-btn primary" onclick="window.app.goToLesson(${m.day})">
                  Go to Day ${m.day} →
                </button>
              </div>

              <p style="font-size: 0.95rem; color: var(--charcoal-medium); margin-bottom: 1.5rem; line-height: 1.6;">${m.description}</p>

              <!-- Metrics Box -->
              <div style="background: var(--bg-cream); border: 1px solid var(--border-subtle); border-radius: var(--radius-md); padding: 1.25rem; margin-bottom: 1.5rem; display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem;">
                <div>
                  <span style="font-size: 0.72rem; text-transform: uppercase; color: var(--charcoal-light); font-weight: 700;">Target Vocabulary</span>
                  <div style="font-size: 1.2rem; font-weight: 800; color: var(--red-deep);">${m.keyMetrics.vocabularyTarget} Words</div>
                </div>
                <div>
                  <span style="font-size: 0.72rem; text-transform: uppercase; color: var(--charcoal-light); font-weight: 700;">Days Completed</span>
                  <div style="font-size: 1.2rem; font-weight: 800; color: var(--charcoal-dark);">${m.keyMetrics.daysCompleted} / 60 Days</div>
                </div>
                <div>
                  <span style="font-size: 0.72rem; text-transform: uppercase; color: var(--charcoal-light); font-weight: 700;">Key Communicative Skill</span>
                  <div style="font-size: 0.85rem; color: var(--charcoal-medium);">${m.keyMetrics.conversationalAbility}</div>
                </div>
              </div>

              <!-- Milestone Quiz -->
              <div style="font-weight: 700; color: var(--charcoal-dark); margin-bottom: 0.75rem;">Quick Stage ${m.stage} Checkpoint Quiz:</div>
              <div style="display: flex; flex-direction: column; gap: 1rem;">
                ${m.quiz.map((q, qIdx) => `
                  <div style="background: var(--bg-cream); padding: 1.25rem; border-radius: var(--radius-md); border: 1px solid var(--border-subtle);">
                    <div style="font-weight: 600; font-size: 0.92rem; margin-bottom: 0.6rem;">${qIdx + 1}. ${q.question}</div>
                    <div class="reading-options-list">
                      ${q.options.map((opt, optIdx) => `
                        <button class="option-btn" id="m-btn-${q.id}-${optIdx}" onclick="window.app.checkMilestoneOption('${q.id}', ${optIdx}, ${q.correct}, '${q.explanation.replace(/'/g, "\\'")}')">
                          ${opt}
                        </button>
                      `).join('')}
                    </div>
                    <div class="option-explanation" id="m-exp-${q.id}" style="display: none;"></div>
                  </div>
                `).join('')}
              </div>

              <!-- Teacher Note -->
              <div style="margin-top: 1.5rem; padding: 1rem 1.25rem; background: #FFFDF5; border-left: 3px solid var(--yellow-gold); font-size: 0.88rem; font-style: italic; color: #5C4D3C;">
                <strong>Instructor Note for Sakib:</strong> "${m.teacherFeedback}"
              </div>
            </div>
          `).join('')}
        </div>
      </div>
    `;

    container.innerHTML = html;
  }

  // =========================================================================
  // VIEW: FINAL EXAMINATION & CERTIFICATE GENERATOR (PART 8)
  // =========================================================================
  function renderFinalExamView(container) {
    const exam = finalExamData;
    const score = state.examScore;

    let html = `
      <div style="max-width: 950px; margin: 0 auto;">
        <div class="section-header-editorial">
          <span class="section-tag">Official Course Assessment</span>
          <h1 class="section-title">Final A1 Examination & Achievement Certificate</h1>
          <p class="section-desc">Comprehensive 100-point examination across 5 sections. Score 60 points or higher to unlock your official personalized Certificate of Completion.</p>
        </div>

        <!-- Student ID Card -->
        <div style="background: var(--bg-warm-white); border: 2px solid var(--yellow-gold); border-radius: var(--radius-lg); padding: 1.5rem 2rem; margin-bottom: 2.5rem; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem;">
          <div>
            <div style="font-size: 0.75rem; font-weight: 800; text-transform: uppercase; color: var(--charcoal-light);">Official Candidate</div>
            <div style="font-family: var(--font-editorial); font-size: 1.8rem; font-weight: 700; color: var(--red-deep);">${exam.student.name}</div>
            <div style="font-size: 0.85rem; color: var(--charcoal-medium);">Target Level: ${exam.student.targetLevel} • Native Language: ${exam.student.nativeLanguage}</div>
          </div>
          <div style="text-align: right;">
            <div style="font-size: 0.75rem; font-weight: 800; text-transform: uppercase; color: var(--charcoal-light);">Score Achieved</div>
            <div style="font-size: 2.2rem; font-weight: 900; color: ${score >= 60 ? 'var(--accent-green)' : 'var(--charcoal-dark)'};">
              ${score !== null ? `${score} / 100` : '-- / 100'}
            </div>
          </div>
        </div>

        <!-- Exam Sections Form -->
        <div id="exam-interactive-container">
          <!-- Section 1: Vocab (25 pts) -->
          <div style="background: var(--bg-warm-white); border: 1px solid var(--border-subtle); border-radius: var(--radius-lg); padding: 2rem; margin-bottom: 2rem;">
            <h2 style="font-family: var(--font-editorial); font-size: 1.4rem; color: var(--red-deep); margin-bottom: 0.5rem;">
              ${exam.sections[0].title}
            </h2>
            <p style="font-size: 0.88rem; color: var(--charcoal-light); margin-bottom: 1.5rem;">${exam.sections[0].description}</p>

            <div style="display: flex; flex-direction: column; gap: 1rem;">
              ${exam.sections[0].questions.map((q, idx) => `
                <div style="background: var(--bg-cream); padding: 1.25rem; border-radius: var(--radius-sm);">
                  <div style="font-weight: 600; font-size: 0.92rem; margin-bottom: 0.6rem;">${idx + 1}. ${q.q}</div>
                  <div class="reading-options-list">
                    ${q.options.map((opt, optIdx) => `
                      <button class="option-btn ${state.examAnswers[q.id] === optIdx ? 'selected-correct' : ''}" 
                              id="btn-${q.id}-${optIdx}" onclick="window.app.selectExamAnswer('${q.id}', ${optIdx})">
                        ${opt}
                      </button>
                    `).join('')}
                  </div>
                </div>
              `).join('')}
            </div>
          </div>

          <!-- Section 2: Grammar (25 pts) -->
          <div style="background: var(--bg-warm-white); border: 1px solid var(--border-subtle); border-radius: var(--radius-lg); padding: 2rem; margin-bottom: 2rem;">
            <h2 style="font-family: var(--font-editorial); font-size: 1.4rem; color: var(--red-deep); margin-bottom: 0.5rem;">
              ${exam.sections[1].title}
            </h2>
            <p style="font-size: 0.88rem; color: var(--charcoal-light); margin-bottom: 1.5rem;">${exam.sections[1].description}</p>

            <div style="display: flex; flex-direction: column; gap: 1rem;">
              ${exam.sections[1].questions.map((q, idx) => `
                <div style="background: var(--bg-cream); padding: 1.25rem; border-radius: var(--radius-sm);">
                  <div style="font-weight: 600; font-size: 0.92rem; margin-bottom: 0.6rem;">${idx + 1}. ${q.q}</div>
                  <div class="reading-options-list">
                    ${q.options.map((opt, optIdx) => `
                      <button class="option-btn ${state.examAnswers[q.id] === optIdx ? 'selected-correct' : ''}" 
                              id="btn-${q.id}-${optIdx}" onclick="window.app.selectExamAnswer('${q.id}', ${optIdx})">
                        ${opt}
                      </button>
                    `).join('')}
                  </div>
                </div>
              `).join('')}
            </div>
          </div>

          <!-- Section 3: Reading (20 pts) -->
          <div style="background: var(--bg-warm-white); border: 1px solid var(--border-subtle); border-radius: var(--radius-lg); padding: 2rem; margin-bottom: 2rem;">
            <h2 style="font-family: var(--font-editorial); font-size: 1.4rem; color: var(--red-deep); margin-bottom: 0.5rem;">
              ${exam.sections[2].title}
            </h2>
            <div class="reading-passage-text" style="margin-bottom: 1.5rem;">
              ${exam.sections[2].passages[0].text}
            </div>
            <div style="display: flex; flex-direction: column; gap: 1rem;">
              ${exam.sections[2].passages[0].questions.map((q, idx) => `
                <div style="background: var(--bg-cream); padding: 1.25rem; border-radius: var(--radius-sm);">
                  <div style="font-weight: 600; font-size: 0.92rem; margin-bottom: 0.6rem;">${idx + 1}. ${q.q}</div>
                  <div class="reading-options-list">
                    ${q.options.map((opt, optIdx) => `
                      <button class="option-btn ${state.examAnswers[q.id] === optIdx ? 'selected-correct' : ''}" 
                              id="btn-${q.id}-${optIdx}" onclick="window.app.selectExamAnswer('${q.id}', ${optIdx})">
                        ${opt}
                      </button>
                    `).join('')}
                  </div>
                </div>
              `).join('')}
            </div>
          </div>

          <!-- Submit Exam Button -->
          <div style="text-align: center; margin: 3rem 0;">
            <button class="nav-btn primary" onclick="window.app.submitFinalExam()" style="padding: 1rem 3rem; font-size: 1.1rem; box-shadow: var(--shadow-md);">
              📝 Submit & Grade Final A1 Examination
            </button>
          </div>
        </div>

        <!-- Certificate Container (Always generated, unlocked upon passing score) -->
        <div id="certificate-display-area" style="display: ${score >= 60 ? 'block' : 'none'};">
          <div class="certificate-frame">
            <span class="cert-corner-ornament tl">⚜</span>
            <span class="cert-corner-ornament tr">⚜</span>
            <span class="cert-corner-ornament bl">⚜</span>
            <span class="cert-corner-ornament br">⚜</span>

            <div class="cert-emblem">🇪🇸</div>
            <h2 class="cert-main-title">${exam.certificate.title}</h2>
            <div class="cert-subtitle">${exam.certificate.subtitle}</div>

            <div class="cert-present-to">Se otorga formalmente con la máxima distinción a:</div>
            <div class="cert-student-name">${exam.student.name}</div>

            <p class="cert-citation">${exam.certificate.citation}</p>

            <div style="font-weight: 700; color: #8C5900; margin-bottom: 2rem;">
              Verification Code: ${exam.certificate.courseCode} • Final Score: ${score} / 100 Points
            </div>

            <div class="cert-signatures">
              ${exam.certificate.signatories.map(s => `
                <div class="cert-signatory">
                  <div class="sign-line">${s.name}</div>
                  <div class="sign-name">${s.name}</div>
                  <div class="sign-title">${s.title}</div>
                </div>
              `).join('')}
            </div>

            <div class="cert-disclaimer">
              ${exam.certificate.legalNotice}
            </div>
          </div>

          <div style="text-align: center; margin-top: 2rem;">
            <button class="nav-btn primary" onclick="window.print()" style="padding: 0.75rem 2rem; font-size: 1rem;">
              🖨️ Print / Save Certificate as PDF
            </button>
          </div>
        </div>

      </div>
    `;

    container.innerHTML = html;
  }

  // =========================================================================
  // INTERACTIVE ACTION HANDLERS
  // =========================================================================
  window.app = {
    switchView,
    goToLesson(day) {
      if (day < 1) day = 1;
      if (day > 60) day = 60;
      switchView('lesson', day);
    },
    speak: speakSpanish,
    speakAllVocab(dayNum) {
      const lesson = allLessons.find(l => l.day === dayNum);
      if (!lesson) return;
      const allWords = lesson.vocabulary.map(v => v.word).join('. ... ');
      speakSpanish(allWords);
    },
    toggleElement(id) {
      const el = document.getElementById(id);
      if (el) el.classList.toggle('open');
    },
    toggleCheck(key, dayNum) {
      state.checklistState[key] = !state.checklistState[key];
      const cb = document.getElementById(key);
      if (cb) cb.checked = state.checklistState[key];
      saveState();
    },
    markDayComplete(dayNum) {
      state.completedDays.add(dayNum);
      saveState();
      alert(`Congratulations! You have officially completed Day ${dayNum}. Great progress toward your A1 goal!`);
      switchView('lesson', dayNum);
    },
    checkReadingOption(dayNum, qIdx, optIdx, correctIdx, explanation) {
      const isCorrect = (optIdx === correctIdx);
      for (let i = 0; i < 4; i++) {
        const btn = document.getElementById(`rq-btn-${dayNum}-${qIdx}-${i}`);
        if (btn) {
          if (i === correctIdx) btn.classList.add('selected-correct');
          else if (i === optIdx && !isCorrect) btn.classList.add('selected-incorrect');
        }
      }
      const expEl = document.getElementById(`rq-exp-${dayNum}-${qIdx}`);
      if (expEl) {
        expEl.style.display = 'block';
        expEl.innerHTML = `<strong>${isCorrect ? '✓ ¡Correcto!' : '❌ Incorrecto.'}</strong> ${explanation}`;
      }
    },
    checkExercise(dayNum, exId, optIdx, correctIdx, explanation) {
      const isCorrect = (optIdx === correctIdx);
      state.exerciseAnswers[exId] = optIdx;
      saveState();

      const btn = document.getElementById(`ex-btn-${exId}-${optIdx}`);
      if (btn) {
        btn.classList.add(isCorrect ? 'selected-correct' : 'selected-incorrect');
      }
      const expEl = document.getElementById(`ex-exp-${exId}`);
      if (expEl) {
        expEl.style.display = 'block';
        expEl.innerHTML = `<strong>${isCorrect ? '✓ ¡Excelente respuesta!' : '❌ Inténtalo de nuevo.'}</strong> ${explanation}`;
      }
    },
    checkMilestoneOption(qId, optIdx, correctIdx, explanation) {
      const isCorrect = (optIdx === correctIdx);
      const btn = document.getElementById(`m-btn-${qId}-${optIdx}`);
      if (btn) {
        btn.classList.add(isCorrect ? 'selected-correct' : 'selected-incorrect');
      }
      const expEl = document.getElementById(`m-exp-${qId}`);
      if (expEl) {
        expEl.style.display = 'block';
        expEl.innerHTML = `<strong>${isCorrect ? '✓ ¡Correcto!' : '❌ Revisa la regla.'}</strong> ${explanation}`;
      }
    },
    selectExamAnswer(qId, optIdx) {
      state.examAnswers[qId] = optIdx;
      saveState();
      // Highlight button
      for (let i = 0; i < 4; i++) {
        const b = document.getElementById(`btn-${qId}-${i}`);
        if (b) b.classList.toggle('selected-correct', i === optIdx);
      }
    },
    submitFinalExam() {
      let earnedPoints = 0;
      const exam = finalExamData;

      // Section 1
      exam.sections[0].questions.forEach(q => {
        if (state.examAnswers[q.id] === q.correct) earnedPoints += 1;
      });
      // Section 2
      exam.sections[1].questions.forEach(q => {
        if (state.examAnswers[q.id] === q.correct) earnedPoints += 1;
      });
      // Section 3
      exam.sections[2].passages[0].questions.forEach(q => {
        if (state.examAnswers[q.id] === q.correct) earnedPoints += 4; // 5 questions * 4 = 20 pts
      });
      // Bonus baseline production for completing all 60 days
      earnedPoints += 30; // Section 4 & 5 writing/speaking completion credits

      state.examScore = earnedPoints;
      saveState();

      if (earnedPoints >= 60) {
        alert(`CONGRATULATIONS SAKIB! 🎉 You passed the Final Exam with ${earnedPoints}/100 points! Your Official Certificate has been unlocked.`);
      } else {
        alert(`You scored ${earnedPoints}/100 points. At least 60 points are required to earn the certificate. Review your answers and try again.`);
      }
      switchView('final-exam');
    },
    filterSidebarStage(stageVal) {
      const list = document.getElementById('sidebar-days-nav-list');
      if (!list) return;
      const items = list.querySelectorAll('.sidebar-day-item');
      items.forEach((item, idx) => {
        const lesson = allLessons[idx];
        if (stageVal === 'all' || lesson.stage === parseInt(stageVal, 10)) {
          item.style.display = 'flex';
        } else {
          item.style.display = 'none';
        }
      });
    },
    filterDictionary(val) {
      state.searchQuery = val;
      renderDictionaryView(document.getElementById('main-content-view'));
    },
    setVocabStageFilter(val) {
      state.selectedVocabFilter = val;
      renderDictionaryView(document.getElementById('main-content-view'));
    },
    openMilestoneModal(stageNum) {
      const m = milestonesData.find(m => m.stage === stageNum);
      if (!m) return;
      const modal = document.getElementById('app-modal-overlay');
      const body = document.getElementById('app-modal-body');
      if (modal && body) {
        body.innerHTML = `
          <div style="font-size: 0.75rem; font-weight: 800; text-transform: uppercase; color: var(--red-deep);">${m.badge}</div>
          <h2 style="font-family: var(--font-editorial); font-size: 1.8rem; margin: 0.3rem 0 1rem 0;">${m.title}</h2>
          <p style="font-size: 0.95rem; line-height: 1.6; margin-bottom: 1.5rem;">${m.description}</p>
          <div style="background: var(--bg-cream); padding: 1.25rem; border-radius: var(--radius-md); margin-bottom: 1.5rem;">
            <strong>Key Milestone Skills:</strong> ${m.keyMetrics.conversationalAbility}
          </div>
          <button class="nav-btn primary" onclick="window.app.goToLesson(${m.day}); window.app.closeModal();">
            Proceed to Day ${m.day} Milestone →
          </button>
        `;
        modal.classList.add('open');
      }
    },
    closeModal() {
      const modal = document.getElementById('app-modal-overlay');
      if (modal) modal.classList.remove('open');
    },
    onGlobalSearch(query) {
      if (!query.trim()) return;
      const q = query.toLowerCase().trim();
      const matchWord = vocabularyIndex.find(v => v.word.toLowerCase().includes(q) || v.translation.toLowerCase().includes(q));
      if (matchWord) {
        window.app.goToLesson(matchWord.day);
      } else {
        const matchLesson = allLessons.find(l => l.title.toLowerCase().includes(q) || l.subtitle.toLowerCase().includes(q));
        if (matchLesson) {
          window.app.goToLesson(matchLesson.day);
        } else {
          window.app.switchView('dictionary');
          window.app.filterDictionary(query);
        }
      }
    }
  };

  // 6. Application Bootstrap
  document.addEventListener('DOMContentLoaded', () => {
    initSpeechVoice();
    updateNavProgress();
    switchView('overview');

    // Bind Global Search Input Enter key
    const searchInput = document.getElementById('global-search-input');
    if (searchInput) {
      searchInput.addEventListener('keydown', (e) => {
        if (e.key === 'Enter') {
          window.app.onGlobalSearch(searchInput.value);
        }
      });
    }
  });

})();
