// Master Grammar Reference Handbook for CEFR A1 Spanish
window.HANDBOOK_GRAMMAR_REFERENCE = [
  {
    "id": "ref-gender-articles",
    "chapter": 1,
    "title": "Spanish Noun Gender & Articles (El Género y los Artículos)",
    "subtitle": "Masculine vs Feminine, Plural Rules, and Article Systems",
    "content": {
      "overview": "Every Spanish noun is inherently masculine or feminine. Grammatical gender influences the articles and adjectives that accompany the noun.",
      "genderRules": [
        {
          "category": "Typically Masculine",
          "endings": "-o, -or, -án, -en, days of the week, rivers, cardinal points",
          "examples": "el libro, el amor, el capitán, el lunes, el norte"
        },
        {
          "category": "Typically Feminine",
          "endings": "-a, -ción, -sión, -dad, -tad, -tud, -umbre",
          "examples": "la mesa, la canción, la ciudad, la libertad, la multitud"
        },
        {
          "category": "Greek Masculine Traps (-ma)",
          "endings": "Nouns of Greek origin ending in -ma",
          "examples": "el problema, el tema, el sistema, el idioma, el programa, el clima, el planeta"
        },
        {
          "category": "Feminine Ending in -o (Truncated)",
          "endings": "Shortened forms of feminine words",
          "examples": "la foto (la fotografía), la moto (la motocicleta), la radio"
        },
        {
          "category": "Irregular Invariable",
          "endings": "Words with atypical endings",
          "examples": "la mano (hand), el mapa (map), el día (day)"
        },
        {
          "category": "Tonic 'A' Feminine Nouns",
          "endings": "Feminine nouns starting with stressed 'a-' or 'ha-' take 'el' in singular to prevent hiatus",
          "examples": "el agua fría -> las aguas frías, el águila rápida -> las águilas rápidas"
        }
      ],
      "articlesTable": {
        "headers": [
          "Type",
          "Masculine Singular",
          "Feminine Singular",
          "Masculine Plural",
          "Feminine Plural"
        ],
        "rows": [
          [
            "Definite (The)",
            "el",
            "la",
            "los",
            "las"
          ],
          [
            "Indefinite (A / Some)",
            "un",
            "una",
            "unos",
            "unas"
          ]
        ]
      },
      "contractions": [
        {
          "rule": "a + el = al",
          "example": "Voy al supermercado. (I am going to the supermarket.)"
        },
        {
          "rule": "de + el = del",
          "example": "El libro del profesor. (The teacher's book.)"
        }
      ],
      "pluralRules": [
        {
          "rule": "Ends in vowel -> add -s",
          "example": "el libro -> los libros, la casa -> las casas"
        },
        {
          "rule": "Ends in consonant -> add -es",
          "example": "el hotel -> los hoteles, la ciudad -> las ciudades"
        },
        {
          "rule": "Ends in -z -> change to -ces",
          "example": "el pez -> los peces, la luz -> las luces"
        }
      ]
    }
  },
  {
    "id": "ref-pronouns",
    "chapter": 2,
    "title": "Subject Pronouns (Pronombres Personales de Sujeto)",
    "subtitle": "Spain (Castilian) Pronoun System with Vosotros",
    "content": {
      "overview": "Subject pronouns indicate who is performing the action. In Spanish, they are often omitted because the conjugated verb ending already specifies the person.",
      "pronounsTable": {
        "headers": [
          "Person",
          "Singular",
          "Plural",
          "Usage Note in Spain"
        ],
        "rows": [
          [
            "1st Person (I / We)",
            "yo (I)",
            "nosotros / nosotras (We)",
            "Nosotras is exclusively for all-female groups."
          ],
          [
            "2nd Person Informal (You / You all)",
            "tú (You)",
            "vosotros / vosotras (You all)",
            "Standard informal address across Spain in shops, universities, friends."
          ],
          [
            "2nd Person Formal (You / You all)",
            "usted (You formal)",
            "ustedes (You all formal)",
            "Used with doctors, elderly people, police, formal business."
          ],
          [
            "3rd Person (He/She/They)",
            "él (He), ella (She)",
            "ellos / ellas (They)",
            "Ellos for mixed or male groups; ellas for female groups."
          ]
        ]
      },
      "proTip": "Pronoun dropping (*omisión del pronombre*): 'Hablo español' is far more natural than 'Yo hablo español'. Only include 'yo' or 'él' for emphasis or to resolve ambiguity."
    }
  },
  {
    "id": "ref-ser-vs-estar",
    "chapter": 3,
    "title": "Ser vs Estar: The Two Spanish Verbs 'To Be'",
    "subtitle": "DOCTOR vs PLACE Rules & Adjectives That Change Meaning",
    "content": {
      "overview": "English has one verb 'to be'. Spanish has two: SER (essence, identity, permanent traits) and ESTAR (states, locations, conditions).",
      "conjugationTable": {
        "headers": [
          "Pronoun",
          "SER (Present)",
          "ESTAR (Present)"
        ],
        "rows": [
          [
            "yo",
            "soy",
            "estoy"
          ],
          [
            "tú",
            "eres",
            "estás"
          ],
          [
            "él / ella / usted",
            "es",
            "está"
          ],
          [
            "nosotros / nosotras",
            "somos",
            "estamos"
          ],
          [
            "vosotros / vosotras",
            "sois",
            "estáis"
          ],
          [
            "ellos / ellas / ustedes",
            "son",
            "están"
          ]
        ]
      },
      "acronyms": {
        "ser": {
          "acronym": "DOCTOR",
          "breakdown": [
            "D - Description (Soy alto y moreno)",
            "O - Occupation (Sakib es ingeniero)",
            "C - Characteristic (El hielo es frío)",
            "T - Time & Date (Hoy es lunes, son las tres)",
            "O - Origin & Material (Soy de Bangladés, la mesa es de madera)",
            "R - Relationship / Religion (Carlos es mi amigo)"
          ]
        },
        "estar": {
          "acronym": "PLACE",
          "breakdown": [
            "P - Position (El libro está encima de la mesa)",
            "L - Location (Madrid está en España — location ALWAYS takes estar!)",
            "A - Action in progress (Estoy estudiando)",
            "C - Condition (La sopa está caliente, la puerta está cerrada)",
            "E - Emotion & Mental State (Estoy contento, estás triste)"
          ]
        }
      },
      "meaningShifts": [
        {
          "adjective": "listo",
          "withSer": "Ser listo = To be smart / clever",
          "withEstar": "Estar listo = To be ready"
        },
        {
          "adjective": "rico",
          "withSer": "Ser rico = To be wealthy",
          "withEstar": "Estar rico = To taste delicious (food)"
        },
        {
          "adjective": "malo",
          "withSer": "Ser malo = To be bad / evil",
          "withEstar": "Estar malo = To be sick / ill"
        },
        {
          "adjective": "aburrido",
          "withSer": "Ser aburrido = To be boring (person/thing)",
          "withEstar": "Estar aburrido = To be bored"
        }
      ]
    }
  },
  {
    "id": "ref-regular-present",
    "chapter": 4,
    "title": "Regular Present-Tense Verbs (-AR, -ER, -IR)",
    "subtitle": "The Universal Ending Matrix for Present Indicative",
    "content": {
      "overview": "To conjugate regular verbs, remove the infinitive suffix (-ar, -er, -ir) and attach the person ending to the stem.",
      "matrixTable": {
        "headers": [
          "Pronoun",
          "-AR (Hablar)",
          "-ER (Comer)",
          "-IR (Vivir)"
        ],
        "rows": [
          [
            "yo",
            "-o (hablo)",
            "-o (como)",
            "-o (vivo)"
          ],
          [
            "tú",
            "-as (hablas)",
            "-es (comes)",
            "-es (vives)"
          ],
          [
            "él / ella / usted",
            "-a (habla)",
            "-e (come)",
            "-e (vive)"
          ],
          [
            "nosotros / nosotras",
            "-amos (hablamos)",
            "-emos (comemos)",
            "-imos (vivimos)"
          ],
          [
            "vosotros / vosotras",
            "-áis (habláis)",
            "-éis (coméis)",
            "-ís (vivís)"
          ],
          [
            "ellos / ellas / ustedes",
            "-an (hablan)",
            "-en (comen)",
            "-en (viven)"
          ]
        ]
      },
      "proTip": "Notice that -ER and -IR share identical endings across 4 of the 6 persons: -o, -es, -e, -en! They only differ in nosotros (-emos vs -imos) and vosotros (-éis vs -ís)."
    }
  },
  {
    "id": "ref-stem-changers",
    "chapter": 5,
    "title": "Stem-Changing Verbs (Boot Verbs / Verbos de Bota)",
    "subtitle": "Vowel Mutations: E -> IE, O -> UE, E -> I",
    "content": {
      "overview": "Stem-changing verbs mutate their root vowel when stressed (yo, tú, él, ellos). Nosotros and vosotros NEVER change (forming the shape of a boot).",
      "categories": [
        {
          "type": "E -> IE",
          "verbs": "Querer (to want), Preferir (to prefer), Empezar (to begin), Entender (to understand), Pensar (to think), Cerrar (to close)",
          "paradigm": "Querer: quiero, quieres, quiere, **queremos**, **queréis**, quieren"
        },
        {
          "type": "O -> UE",
          "verbs": "Poder (can/be able), Dormir (to sleep), Almorzar (to have lunch), Volver (to return), Costar (to cost), Encontrar (to find)",
          "paradigm": "Poder: puedo, puedes, puede, **podemos**, **podéis**, pueden"
        },
        {
          "type": "E -> I",
          "verbs": "Pedir (to ask for/order), Servir (to serve), Repetir (to repeat), Vestirse (to dress)",
          "paradigm": "Pedir: pido, pides, pide, **pedimos**, **pedís**, piden"
        },
        {
          "type": "U -> UE",
          "verbs": "Jugar (to play a sport/game)",
          "paradigm": "Jugar: juego, juegas, juega, **jugamos**, **jugáis**, juegan"
        }
      ]
    }
  },
  {
    "id": "ref-core-irregulars",
    "chapter": 6,
    "title": "Essential Irregular Present Verbs (Los Irregulares Clave)",
    "subtitle": "Tener, Hacer, Ir, Saber, Ver, Poner, Salir, Venir, Dar",
    "content": {
      "overview": "These verbs occur constantly in daily Spanish speech. Many feature an irregular 1st person 'yo' ('-go' verbs) or full root irregularity.",
      "verbsTable": {
        "headers": [
          "Verb",
          "yo",
          "tú",
          "él/ella",
          "nosotros",
          "vosotros",
          "ellos/ellas"
        ],
        "rows": [
          [
            "Tener (to have)",
            "tengo",
            "tienes",
            "tiene",
            "tenemos",
            "tenéis",
            "tienen"
          ],
          [
            "Hacer (to do/make)",
            "hago",
            "haces",
            "hace",
            "hacemos",
            "hacéis",
            "hacen"
          ],
          [
            "Ir (to go)",
            "voy",
            "vas",
            "va",
            "vamos",
            "vais",
            "van"
          ],
          [
            "Saber (to know facts)",
            "sé",
            "sabes",
            "sabe",
            "sabemos",
            "sabéis",
            "saben"
          ],
          [
            "Ver (to see)",
            "veo",
            "ves",
            "ve",
            "vemos",
            "veis",
            "ven"
          ],
          [
            "Poner (to put)",
            "pongo",
            "pones",
            "pone",
            "ponemos",
            "ponéis",
            "ponen"
          ],
          [
            "Salir (to leave/go out)",
            "salgo",
            "sales",
            "sale",
            "salimos",
            "salís",
            "salen"
          ],
          [
            "Venir (to come)",
            "vengo",
            "vienes",
            "viene",
            "venimos",
            "venís",
            "vienen"
          ],
          [
            "Dar (to give)",
            "doy",
            "das",
            "da",
            "damos",
            "dais",
            "dan"
          ]
        ]
      }
    }
  },
  {
    "id": "ref-gustar",
    "chapter": 7,
    "title": "Verbs Like GUSTAR (Psychological State Verbs)",
    "subtitle": "Encantar, Doler, Interesar, Parecer, Importar",
    "content": {
      "overview": "GUSTAR does not translate as 'I like X', but rather 'X pleases me'. The thing you like is the grammatical SUBJECT, and the person is the INDIRECT OBJECT.",
      "formula": "[Clarifier: A mí / A ti / A Carlos] + [Indirect Pronoun: me / te / le / nos / os / les] + [gusta (singular/verb) / gustan (plural)] + [Thing liked]",
      "examplesTable": {
        "headers": [
          "Type",
          "Spanish",
          "Literal Translation",
          "English Meaning"
        ],
        "rows": [
          [
            "Singular Noun",
            "Me gusta el café.",
            "The coffee pleases me.",
            "I like coffee."
          ],
          [
            "Plural Noun",
            "Me gustan los libros.",
            "The books please me.",
            "I like books."
          ],
          [
            "Infinitive Verb",
            "Nos gusta viajar.",
            "To travel pleases us.",
            "We like traveling."
          ],
          [
            "Emphasis",
            "A ella le gusta la música.",
            "To her the music pleases.",
            "She likes music."
          ]
        ]
      },
      "parallelVerbs": [
        {
          "verb": "Encantar",
          "meaning": "To love / adore",
          "example": "Me encanta la comida española."
        },
        {
          "verb": "Doler (o->ue)",
          "meaning": "To hurt",
          "example": "Me duele la cabeza / Me duelen los pies."
        },
        {
          "verb": "Interesar",
          "meaning": "To interest",
          "example": "Nos interesa la historia de Madrid."
        },
        {
          "verb": "Importar",
          "meaning": "To matter / care",
          "example": "No me importa el precio."
        }
      ]
    }
  },
  {
    "id": "ref-reflexives",
    "chapter": 8,
    "title": "Reflexive Verbs & Daily Routines (Verbos Reflexivos)",
    "subtitle": "Actions Performed on Oneself & Reflexive Pronoun Placement",
    "content": {
      "overview": "Reflexive verbs describe actions that the subject performs upon themselves. In the infinitive, they end in '-se' (levantarse, ducharse).",
      "pronouns": [
        {
          "person": "yo",
          "pronoun": "me",
          "example": "Yo me levanto a las siete."
        },
        {
          "person": "tú",
          "pronoun": "te",
          "example": "Tú te duchas con agua caliente."
        },
        {
          "person": "él / ella / usted",
          "pronoun": "se",
          "example": "Él se peina el pelo."
        },
        {
          "person": "nosotros",
          "pronoun": "nos",
          "example": "Nosotros nos acostamos tarde."
        },
        {
          "person": "vosotros",
          "pronoun": "os",
          "example": "Vosotros os laváis las manos."
        },
        {
          "person": "ellos / ellas / ustedes",
          "pronoun": "se",
          "example": "Ellos se visten deprisa."
        }
      ],
      "placementRules": [
        {
          "rule": "Before a conjugated verb",
          "example": "Me despierto temprano."
        },
        {
          "rule": "Attached to the end of an infinitive",
          "example": "Voy a ducharme. / Tengo que levantarme."
        },
        {
          "rule": "Attached to the end of a gerund",
          "example": "Estoy vistiéndome."
        }
      ]
    }
  },
  {
    "id": "ref-por-vs-para",
    "chapter": 9,
    "title": "Por vs Para: The Definitive Decider",
    "subtitle": "Cause vs Purpose, Duration vs Deadline, Exchange vs Recipient",
    "content": {
      "overview": "Both translate as 'for' in English, but they represent opposite conceptual vectors: POR looks backwards (cause, motivation), while PARA points forward (destination, purpose).",
      "comparisonTable": {
        "headers": [
          "Aspect",
          "POR (Cause, Route, Means)",
          "PARA (Destination, Goal, Recipient)"
        ],
        "rows": [
          [
            "Direction / Destination",
            "Viajo por España (through/around).",
            "Salgo para Madrid (headed toward)."
          ],
          [
            "Reason vs Purpose",
            "Gracias por tu ayuda (because of).",
            "Estudio para aprobar (in order to)."
          ],
          [
            "Time",
            "Estudié por dos horas (duration).",
            "La tarea es para el lunes (deadline)."
          ],
          [
            "Recipient",
            "Hice el pastel por mi madre (in her place).",
            "El regalo es para mi madre (for her to receive)."
          ],
          [
            "Exchange & Price",
            "Pagué 10€ por el menú (in exchange for).",
            "No applicable for price."
          ]
        ]
      },
      "idioms": [
        {
          "phrase": "Por favor",
          "meaning": "Please"
        },
        {
          "phrase": "Por fin",
          "meaning": "At last / finally"
        },
        {
          "phrase": "Por ejemplo",
          "meaning": "For example"
        },
        {
          "phrase": "Para siempre",
          "meaning": "Forever"
        }
      ]
    }
  },
  {
    "id": "ref-preterite-past",
    "chapter": 10,
    "title": "The Preterite Past Tense (Pretérito Indefinido)",
    "subtitle": "Completed Actions in Past Time with Full Regular & Irregular Tables",
    "content": {
      "overview": "The preterite is used for actions that began and finished at a specific point in the past (ayer, anoche, la semana pasada, en 2024).",
      "regularTable": {
        "headers": [
          "Pronoun",
          "-AR (Hablar)",
          "-ER (Comer)",
          "-IR (Vivir)"
        ],
        "rows": [
          [
            "yo",
            "hablé",
            "comí",
            "viví"
          ],
          [
            "tú",
            "hablaste",
            "comiste",
            "viviste"
          ],
          [
            "él / ella / usted",
            "habló",
            "comió",
            "vivió"
          ],
          [
            "nosotros / nosotras",
            "hablamos",
            "comimos",
            "vivimos"
          ],
          [
            "vosotros / vosotras",
            "hablasteis",
            "comisteis",
            "vivisteis"
          ],
          [
            "ellos / ellas / ustedes",
            "hablaron",
            "comieron",
            "vivieron"
          ]
        ]
      },
      "irregularsOverview": "SER and IR are identical in the preterite: fui, fuiste, fue, fuimos, fuisteis, fueron. Context resolves whether it means 'went' (followed by 'a') or 'was' (followed by adjective).",
      "irregularStems": [
        {
          "infinitive": "Estar",
          "stem": "estuv-",
          "conjugation": "estuve, estuviste, estuvo, estuvimos, estuvisteis, estuvieron"
        },
        {
          "infinitive": "Tener",
          "stem": "tuv-",
          "conjugation": "tuve, tuviste, tuvo, tuvimos, tuvisteis, tuvieron"
        },
        {
          "infinitive": "Hacer",
          "stem": "hic- (3rd hiz-)",
          "conjugation": "hice, hiciste, hizo, hicimos, hicisteis, hicieron"
        },
        {
          "infinitive": "Poder",
          "stem": "pud-",
          "conjugation": "pude, pudiste, pudo, pudimos, pudisteis, pudieron"
        },
        {
          "infinitive": "Poner",
          "stem": "pus-",
          "conjugation": "puse, pusiste, puso, pusimos, pusisteis, pusieron"
        },
        {
          "infinitive": "Saber",
          "stem": "sup-",
          "conjugation": "supe, supiste, supo, supimos, supisteis, supieron"
        },
        {
          "infinitive": "Decir",
          "stem": "dij-",
          "conjugation": "dije, dijiste, dijo, dijimos, dijisteis, dijeron"
        }
      ]
    }
  },
  {
    "id": "ref-questions-negation",
    "chapter": 11,
    "title": "Question Formation & Negation (Preguntas y Negación)",
    "subtitle": "Interrogative Pronouns with Tildes and Double Negatives",
    "content": {
      "overview": "Questions in Spanish begin with an upside-down question mark (¿) and end with (?). Question words always carry an accent mark (*tilde*).",
      "questionWords": [
        {
          "word": "¿Qué?",
          "meaning": "What?",
          "example": "¿Qué hora es?"
        },
        {
          "word": "¿Quién? / ¿Quiénes?",
          "meaning": "Who? (Singular / Plural)",
          "example": "¿Quién es ese chico?"
        },
        {
          "word": "¿Dónde? / ¿Adónde?",
          "meaning": "Where? / Where to?",
          "example": "¿Dónde vives? / ¿Adónde vas?"
        },
        {
          "word": "¿Cuándo?",
          "meaning": "When?",
          "example": "¿Cuándo sale el tren?"
        },
        {
          "word": "¿Cómo?",
          "meaning": "How?",
          "example": "¿Cómo te llamas?"
        },
        {
          "word": "¿Por qué?",
          "meaning": "Why? (Two words, with tilde; Answer is 'porque')",
          "example": "¿Por qué estudias español? Porque me gusta."
        },
        {
          "word": "¿Cuál? / ¿Cuáles?",
          "meaning": "Which? / What? (Choice from set)",
          "example": "¿Cuál es tu número de teléfono?"
        },
        {
          "word": "¿Cuánto/a/os/as?",
          "meaning": "How much? / How many?",
          "example": "¿Cuánto cuesta? / ¿Cuántos años tienes?"
        }
      ],
      "negationRules": [
        {
          "rule": "Simple Negation: 'No' before the conjugated verb",
          "example": "No hablo alemán. (I do not speak German.)"
        },
        {
          "rule": "Double Negation is standard and correct in Spanish!",
          "example": "No sé nada. (I don't know nothing = I don't know anything.)"
        },
        {
          "words": "Nunca (never), Nada (nothing), Nadie (nobody), Ninguno/a (none)",
          "example": "No veo a nadie en la calle. / Nunca viajo en avión."
        }
      ]
    }
  },
  {
    "id": "ref-possessives",
    "chapter": 12,
    "title": "Possessive Adjectives (Adjetivos Posesivos)",
    "subtitle": "Unstressed Possessives (mi, tu, su, nuestro, vuestro)",
    "content": {
      "overview": "Possessive adjectives agree in gender and number with the OBJECT POSSESSED, not with the owner.",
      "table": {
        "headers": [
          "Owner",
          "Singular Object",
          "Plural Object"
        ],
        "rows": [
          [
            "yo (my)",
            "mi (mi libro)",
            "mis (mis libros)"
          ],
          [
            "tú (your)",
            "tu (tu casa)",
            "tus (tus casas)"
          ],
          [
            "él / ella / usted (his/her/its/your)",
            "su (su coche)",
            "sus (sus coches)"
          ],
          [
            "nosotros (our)",
            "nuestro / nuestra",
            "nuestros / nuestras"
          ],
          [
            "vosotros (your all)",
            "vuestro / vuestra",
            "vuestros / vuestras"
          ],
          [
            "ellos / ellas / ustedes (their/your)",
            "su (su hotel)",
            "sus (sus hoteles)"
          ]
        ]
      },
      "warning": "'Su' and 'sus' can mean his, her, its, your (formal), or their! Clarify with 'de él', 'de ella', or 'de ustedes' when needed."
    }
  }
];
