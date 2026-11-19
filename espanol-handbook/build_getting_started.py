"""
Generate getting-started.js for Part A of the Spanish Handbook.
"""
import json

getting_started_data = {
    "title": "Part A: Getting Started — Tu Punto de Partida",
    "subtitle": "Your Complete Launchpad for the 60-Day Spanish Learning Challenge",
    "sections": [
        {
            "id": "welcome",
            "title": "1. Welcome to the 60-Day Spanish Challenge! 🇪🇸",
            "icon": "sparkles",
            "content": """
¡Bienvenido, Sakib! Welcome to your personal 60-Day Spanish Learning Journey. 

This handbook is designed specifically for **you**: a beginner (CEFR A1) learner whose native language is **Bangla**, using **clear English** explanations, and focusing on **Standard Spanish with a preference for Spain (Castilian Spanish)**.

Over the next 60 days, you are not just memorizing isolated words. You are building an authentic, resilient mental foundation that will allow you to:
- Understand basic spoken Spanish in everyday situations.
- Read signs, menus, short articles, and simple stories with confidence.
- Construct natural Spanish sentences without freezing or relying on Google Translate.
- Confidently introduce yourself, your family, your passions, and your routine.
- Navigate a Spanish restaurant, train station, market, and hotel.
- Appreciate the rich culture, history, and warmth of Spain.

**Golden Rule of A1:** We will **never rush you into A2**. A shaky foundation crumbles; a rock-solid A1 foundation will make everything in A2 and B1 feel effortless.
"""
        },
        {
            "id": "how-to-use",
            "title": "2. How to Use This Handbook",
            "icon": "book-open",
            "content": """
To achieve true fluency at the A1 level, consistency beats marathon study sessions. Dedicate **45 to 60 minutes each day**.

Here is your ideal daily ritual:
1. **Goal Setting (2 mins):** Read today's goals so your brain knows what to look for.
2. **Vocabulary Acquisition (10 mins):** Listen to the native audio, read the example sentence, and write the word in your notebook.
3. **Everyday Sentences (5 mins):** Practice saying the 5–8 practical sentences aloud until they roll off your tongue.
4. **Grammar Insight (10 mins):** Read the rules and observe the contrast diagrams. Notice how Spanish constructs thought.
5. **Conversation & Reading (10 mins):** Read the dialogue and passage out loud. Answer the comprehension questions.
6. **Active Exercises (10 mins):** Solve the exercises interactively before checking the answers.
7. **Speaking Challenge & Checklist (5 mins):** Answer the 3 speaking prompts out loud in Spanish, then mark off your daily checklist!
"""
        },
        {
            "id": "realistic-achievements",
            "title": "3. What You Can Realistically Achieve in 60 Days",
            "icon": "target",
            "content": """
Let's set honest, empowering, and realistic CEFR A1 expectations:

| What You WILL Achieve (A1 Mastery) | What Is Beyond 60 Days (A2 / B1) |
|---|---|
| Order food, drinks, and ask for the bill politely in Madrid or Barcelona | Debating political issues or complex economic theories |
| Introduce yourself, your background, nationality, and profession | Understanding rapid television dramas without subtitles |
| Conjugate present tense verbs (-ar, -er, -ir) and key irregulars (*ser, estar, tener, ir, hacer*) | Complex subjunctive mood (*ojalá que venga*) |
| Narrate basic past events with the preterite tense (*ayer comí paella*) | Reading literary novels by Cervantes or Gabriel García Márquez |
| Ask and follow directions in Spanish streets | Fluent professional business negotiations |
| Master ~600 high-frequency, authentic everyday words | Specialized technical or medical terminology |

You will cross the threshold from **"I don't speak Spanish"** to **"I can communicate my life, needs, and thoughts in Spanish!"**
"""
        },
        {
            "id": "alphabet",
            "title": "4. The Spanish Alphabet (El Abecedario)",
            "icon": "alphabet",
            "content": "Spanish has 27 official letters (including the unique letter **Ñ**). Unlike English, Spanish is an almost perfectly **phonetic language** — words are pronounced almost exactly as they are spelled!",
            "alphabetTable": [
                {"letter": "A a", "name": "a", "sound": "Ah (father / বাংলা 'আ')", "example": "amigo (friend)"},
                {"letter": "B b", "name": "be", "sound": "Soft B / V (বাংলা 'ব')", "example": "bueno (good)"},
                {"letter": "C c", "name": "ce", "sound": "TH before e/i (thin); K before a/o/u (cat)", "example": "casa (house), cena (dinner)"},
                {"letter": "D d", "name": "de", "sound": "Soft D with tongue against front teeth (বাংলা 'দ', not hard 'ড')", "example": "día (day)"},
                {"letter": "E e", "name": "e", "sound": "Eh (bed / বাংলা 'এ')", "example": "elefante (elephant)"},
                {"letter": "F f", "name": "efe", "sound": "F (farm)", "example": "familia (family)"},
                {"letter": "G g", "name": "ge", "sound": "H/Kh before e/i; G (go) before a/o/u", "example": "gato (cat), gente (people)"},
                {"letter": "H h", "name": "hache", "sound": "ALWAYS SILENT! Never pronounce H!", "example": "hola (pronounced 'ola')"},
                {"letter": "I i", "name": "i", "sound": "Ee (see / বাংলা 'ই')", "example": "isla (island)"},
                {"letter": "J j", "name": "jota", "sound": "Strong raspy H from throat (like Arabic خ or Scottish 'loch')", "example": "jamón (ham)"},
                {"letter": "K k", "name": "ka", "sound": "K (kilo) - only in loanwords", "example": "kilo (kilogram)"},
                {"letter": "L l", "name": "ele", "sound": "L (light / বাংলা 'ল')", "example": "libro (book)"},
                {"letter": "M m", "name": "eme", "sound": "M (mother / বাংলা 'ম')", "example": "madre (mother)"},
                {"letter": "N n", "name": "ene", "sound": "N (night / বাংলা 'ন')", "example": "noche (night)"},
                {"letter": "Ñ ñ", "name": "eñe", "sound": "Ny sound (canyon, onion / বাংলা 'ঞ' or 'নি')", "example": "España (Spain), niño (boy)"},
                {"letter": "O o", "name": "o", "sound": "Pure Oh (boat, no glide / বাংলা 'ও')", "example": "ojo (eye)"},
                {"letter": "P p", "name": "pe", "sound": "Crisp P without English puff of air (বাংলা 'প')", "example": "pan (bread)"},
                {"letter": "Q q", "name": "cu", "sound": "Always 'qu' followed by e/i, sounds like K", "example": "queso (cheese)"},
                {"letter": "R r", "name": "ere", "sound": "Single tap of tongue on alveolar ridge (বাংলা 'র')", "example": "pero (but), caro (expensive)"},
                {"letter": "RR rr", "name": "erre", "sound": "Rolled / trilled R (vibrant tongue vibration)", "example": "perro (dog), arroz (rice)"},
                {"letter": "S s", "name": "ese", "sound": "S (sun / বাংলা 'স')", "example": "sol (sun)"},
                {"letter": "T t", "name": "te", "sound": "Dental T with tongue behind teeth (বাংলা 'ত', never English 'ট')", "example": "té (tea), taza (cup)"},
                {"letter": "U u", "name": "u", "sound": "Oo (boot / বাংলা 'উ')", "example": "uno (one)"},
                {"letter": "V v", "name": "uve", "sound": "Pronounced identically to Spanish B! (Bilabial soft B)", "example": "vino (wine - sounds like 'beeno')"},
                {"letter": "W w", "name": "uve doble", "sound": "W - only in foreign loanwords", "example": "wifi"},
                {"letter": "X x", "name": "equis", "sound": "X (ks as in taxi)", "example": "éxito (success)"},
                {"letter": "Y y", "name": "i griega", "sound": "Y (yes) or ee (when alone)", "example": "y (and), yo (I)"},
                {"letter": "Z z", "name": "zeta", "sound": "In Spain: voiceless 'th' (think / thank you)", "example": "zapato (shoe), cerveza (beer)"}
            ]
        },
        {
            "id": "bengali-advantage",
            "title": "5. The Bengali Learner's Hidden Superpowers! 🇧🇩 🇪🇸",
            "icon": "zap",
            "content": """
As a native **Bangla speaker**, you have enormous natural linguistic advantages over native English speakers when learning Spanish!

### 🌟 Superpower 1: The Rolled "R" and Flapped "R"
English speakers spend months struggling to pronounce the single tap 'r' (*pero*) and trilled 'rr' (*perro*). In Bangla, your tongue is already completely trained! Your natural **র** is an immediate match for the Spanish tapped 'r'.

### 🌟 Superpower 2: Pure Dental "T" and "D" (ত and দ)
In English, "T" and "D" are aspirated alveolar consonants (ট and ড). If you say "taco" with an English 'T', it sounds foreign. But Spanish uses **dental T (ত)** and **dental D (দ)**, where the tip of the tongue touches the back of the upper front teeth — exactly like standard Bangla!
- *Té* (tea) = তের মতো উচ্চারণ (Not টে)
- *Día* (day) = দিনের মতো 'দ' (Not ডি)

### 🌟 Superpower 3: The Formal vs. Informal Distinction (তুমি vs. আপনি)
English speakers constantly struggle with the Spanish difference between **tú** (informal you) and **usted** (formal you). But as a Bengali speaker, this is already hard-wired into your cultural DNA!
- **Tú** = **তুমি (Tumi)** — used with friends, family, children, peers.
- **Usted** = **আপনি (Apni)** — used with elders, strangers, officials, bosses, and in formal business.
- **Vosotros** = **তোমরা (Tomra)** — Spain's plural informal you.
- **Ustedes** = **আপনারা (Apnara)** — plural formal you.

### 🌟 Superpower 4: Pure, Non-Diphthongized Vowels
English vowels tend to glide (e.g., "no" becomes *noh-oo*). Spanish vowels are pure and clean: **A, E, I, O, U** (আ, এ, ই, ও, উ). Bangla speakers naturally pronounce pure vowels without awkward glides!
"""
        },
        {
            "id": "pronunciation-rules",
            "title": "6. Essential Pronunciation Rules & Spain Spanish (Castellano)",
            "icon": "volume-2",
            "content": """
### 1. The Castilian "Distinción" (Ceceo / The 'TH' Sound)
In central and northern Spain (Standard European Spanish):
- The letter **Z** is ALWAYS pronounced like the English "th" in *think* / *path*.
  - *Zapato* = "thah-PAH-toh"
  - *Cerveza* = "ther-VEH-thah"
- The letter **C** before **E** or **I** is also pronounced like "th"!
  - *Gracias* = "GRAH-thee-ahs"
  - *Cinco* = "THEEN-koh"
- Before **A, O, U**, **C** sounds like a hard **K**: *casa* (KAH-sah), *coche* (KOH-cheh).

### 2. Silent "H"
The letter **H** is 100% silent in Spanish. Never pronounce it:
- *Hola* is pronounced **OH-lah**.
- *Hotel* is pronounced **oh-TEL**.
- *Hablar* is pronounced **ah-BLAR**.

### 3. The Raspy "J" and soft "G"
- The letter **J** (*jota*) and **G** before **E/I** make a deep, throaty sound like clearing your throat or the Scottish *loch*:
  - *Jamón* (ham) = "khah-MON"
  - *Jardín* (garden) = "khar-DEEN"
  - *Gente* (people) = "KHEN-teh"

### 4. B and V are Twins!
In Spanish, **B** and **V** make the exact same soft bilabial sound.
- *Boca* (mouth) and *Vaso* (glass) start with the identical sound. Native Spanish children often make spelling errors between B and V!

### 5. Double L (LL) and Y
In Spain, **LL** (*doble ele*) sounds like the "Y" in *yes* or a soft "ly":
- *Llamo* (I call) = "YAH-moh"
- *Pollo* (chicken) = "POH-yoh"
"""
        },
        {
            "id": "accent-marks",
            "title": "7. Accent Marks & Stress Rules (Las Tildes)",
            "icon": "file-text",
            "content": """
Spanish words have regular natural stress patterns. A written accent mark (called a **tilde**: á, é, í, ó, ú) only appears when a word breaks these natural rules, or to distinguish words that sound identical!

### The Two Natural Stress Rules:
1. **Rule 1 (Vowels, N, or S):** If a word ends in a **vowel (a, e, i, o, u)**, the letter **N**, or the letter **S**, stress naturally falls on the **second-to-last syllable**:
   - *CA-sa* (house) — ends in vowel 'a', stress on CA.
   - *HA-blan* (they speak) — ends in 'n', stress on HA.
   - *A-MI-gos* (friends) — ends in 's', stress on MI.
2. **Rule 2 (Other Consonants):** If a word ends in **any other consonant** (l, r, d, z, etc.), stress naturally falls on the **very last syllable**:
   - *ha-BLAR* (to speak) — ends in 'r', stress on BLAR.
   - *ci-u-DAD* (city) — ends in 'd', stress on DAD.
   - *ho-TEL* (hotel) — ends in 'l', stress on TEL.

### When You See a Tilde (á, é, í, ó, ú):
If a word breaks Rule 1 or Rule 2, Spanish puts a written accent mark over the stressed vowel to tell you: **"STRESS ME HERE!"**
- *ca-FÉ* (ends in vowel, but stress is on last syllable -> needs accent!)
- *MÚ-si-ca* (stress is on 3rd-to-last syllable -> needs accent!)
- *e-SA-men* (natural stress) vs. *e-XÁ-me-nes* (needs accent!)

### Meaning Differentiators (Diacritical Accents):
- *tú* (you) vs. *tu* (your)
- *él* (he) vs. *el* (the)
- *sí* (yes) vs. *si* (if)
- *té* (tea) vs. *te* (you object pronoun)
"""
        },
        {
            "id": "special-characters",
            "title": "8. Special Spanish Characters: ¿ ?, ¡ !, and Ñ",
            "icon": "help-circle",
            "content": """
### 1. Inverted Question Marks (¿ ?) and Exclamation Marks (¡ !)
In Spanish, every question begins with an **inverted question mark (¿)** and ends with a standard (**?**). Every exclamation begins with an **inverted exclamation mark (¡)** and ends with (**!**).
- *¿Cómo te llamas?* (What is your name?)
- *¡Qué maravilloso!* (How wonderful!)

**Why does Spanish do this?** In Spanish, word order in questions is often identical to statements! The upside-down mark tells the reader immediately what tone of voice to use before they even finish the sentence:
- *Tienes hambre.* (You are hungry. — Statement)
- *¿Tienes hambre?* (Are you hungry? — Question!)

### 2. The Letter Ñ (eñe)
**Ñ** is a distinct, proud letter with its own alphabet spot. It sounds like *ny* in canyon:
- *España* (Spain)
- *Señor* (Mr. / Sir)
- *Mañana* (Tomorrow / Morning)
- *Año* (Year — Note: *ano* without the tilde means anus, so always use the ñ!)
"""
        },
        {
            "id": "differences-spanish-english",
            "title": "9. Crucial Differences Between English and Spanish",
            "icon": "git-branch",
            "content": """
Keep these 4 core structural differences in mind:

1. **Every Noun Has a Gender:** Everything in the physical and abstract universe is either grammatically masculine (*el libro*, *el sol*) or feminine (*la mesa*, *la luna*).
2. **Subject Pronouns are Usually Dropped:** Because Spanish verb conjugations clearly indicate who is doing the action, native speakers rarely say *yo* (I) or *tú* (you).
   - English: "I speak Spanish." -> Spanish: *Hablo español.* (Not *Yo hablo español*, unless emphasizing *I*).
3. **Adjectives Usually Follow the Noun:** In English, we say "the red car". In Spanish, the noun comes first, followed by its description: *el coche rojo* (literally "the car red").
4. **Two Verbs for 'To Be': SER and ESTAR:** English uses "is/am/are" for everything. Spanish splits this into **Ser** (permanent essence/identity) and **Estar** (temporary state/location).
"""
        },
        {
            "id": "study-method",
            "title": "10. Your Daily Study System & Spaced Repetition",
            "icon": "check-circle",
            "content": """
To guarantee that you remember Day 1's words on Day 60, use our built-in **3-Layer Memory Loop**:

```
[Day N: New Lesson] -> [Day N+1: Quick Morning Recall] -> [Day N+5: Stage Revision]
```

- **Say It Aloud:** Never study Spanish silently. Your tongue, facial muscles, and ears need physical training.
- **Write by Hand:** Take 10 minutes daily to write today's 10 vocabulary words and grammar table in your dedicated physical notebook.
- **Embrace Small Mistakes:** Making errors is not failure; it is active linguistic computation. Every time you self-correct, a neural connection strengthens.
- **Use the Web App's Features:** Click the audio buttons to hear native pronunciation, use the flashcards, and mark off your daily checklist!
"""
        }
    ]
}

with open("d:/ag/espanol-handbook/data/getting-started.js", "w", encoding="utf-8") as f:
    f.write("// Part A: Getting Started Data\n")
    f.write("window.GETTING_STARTED_DATA = ")
    json.dump(getting_started_data, f, ensure_ascii=False, indent=2)
    f.write(";\n")

print("Generated getting-started.js successfully!")
