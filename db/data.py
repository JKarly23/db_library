usernames:list[str] = [
    "carlosjps","ale12","lucia_books","andres23","martina_read","pedro_lit","sofia_novels","juan_reader","valeria_bk",
    "nicolas42","maria_reads","pablo_lib","camila_bks","joseph_fan","laura_lover","david_book","noelia_word","santiago_pg",
    "elena_chap","antonio_nov"
]


user_type:list[str] = ["comprador","vendedor"]


list_special = ["!","#","$","%","&","()","*","+","-",".","/",":",";","<=>","?","@","[\]","^","_","`{","|""s","}","~"]


calles = [
    "Av. Principal", "Calle Central", "Calle 1", "Calle 2", "Av. Libertador",
    "Av. Bolívar", "Av. 5 de Mayo", "Av. Juárez", "Av. de la Constitución",
    "Av. Revolución", "Av. Hidalgo", "Calle del Sol", "Calle de la Luna",
    "Av. 20 de Noviembre", "Av. Reforma", "Av. Insurgentes", "Av. Chapultepec",
    "Av. Universitaria", "Calle Universidad", "Calle Mayor"
]


ciudades = [
    "Ciudad de México", "Lima", "Bogotá", "Santiago", "Buenos Aires",
    "Madrid", "Barcelona", "Roma", "Nueva York", "Los Ángeles",
    "Toronto", "São Paulo", "Tokio", "Pekín", "Moscú"
]


paises = [
    "México", "Perú", "Colombia", "Chile", "Argentina", "España", "Estados Unidos", "Canadá",
    "Brasil", "Japón", "China", "Rusia", "Francia", "Italia", "Alemania", "Australia"
]


categorias = [
    "Novela","Ciencia Ficción","Fantasía","Misterio","Romance","Terror","Aventura","Literatura Clásica",
    "Histórica","Biografía","Autobiografía","Cuentos","Poesía","Drama","Comedia","Ensayo","No Ficción",
    "Policíaca","Suspenso","Thriller","Ficción Juvenil","Ficción Contemporánea","Literatura Infantil","Fábulas",
    "Mitología","Epistolar","Viajes","Diarios","Memorias","Ficción Experimental","Antología","Paranormal","Distopía",
    "Utopía","Ciencia","Tecnología","Medicina","Psicología","Filosofía","Sociología","Política","Economía","Educación",
    "Autoayuda","Negocios","Religión","Espiritualidad","Astrología","Nutrición","Cocina","Deportes","Música","Arte",
    "Fotografía","Cine","Teatro","Arquitectura","Jardinería","Manualidades","Decoración","Moda","Viajes y Turismo",
    "Geografía","Historia del Arte","Antropología","Arqueología","Mitología","Literatura Erótica","Guías de Estudio",
    "Enciclopedias","Diccionarios","Manuales","Guías","Textos Académicos","Referencias","Estadística","Matemáticas",
    "Física","Química","Biología","Geología","Astronomía","Ecología","Medicina Alternativa","Veterinaria","Agricultura",
    "Ingeniería","Informática","Inteligencia Artificial","Ciberseguridad","Robótica","Programación","Redes y Telecomunicaciones",
    "Diseño Gráfico","Marketing","Publicidad","Relaciones Públicas","Trabajo Social","Derecho","Criminología"
]



categorias_libros = {
    "Novela": [
        "Cien Años de Soledad - Gabriel García Márquez",
        "Orgullo y Prejuicio - Jane Austen",
        "Crimen y Castigo - Fiódor Dostoyevski",
        "Don Quijote de la Mancha - Miguel de Cervantes",
        "El Gran Gatsby - F. Scott Fitzgerald",
        "Matar a un Ruiseñor - Harper Lee"
    ],
    "Ciencia Ficción": [
        "1984 - George Orwell",
        "Dune - Frank Herbert",
        "Neuromante - William Gibson",
        "Fahrenheit 451 - Ray Bradbury",
        "El Juego de Ender - Orson Scott Card",
        "La Fundación - Isaac Asimov"
    ],
    "Fantasía": [
        "El Señor de los Anillos - J.R.R. Tolkien",
        "Juego de Tronos - George R.R. Martin",
        "Harry Potter y la Piedra Filosofal - J.K. Rowling",
        "Las Crónicas de Narnia - C.S. Lewis",
        "El Nombre del Viento - Patrick Rothfuss",
        "La Rueda del Tiempo - Robert Jordan"
    ],
    "Misterio": [
        "El Nombre de la Rosa - Umberto Eco",
        "Los Hombres que no Amaban a las Mujeres - Stieg Larsson",
        "Asesinato en el Orient Express - Agatha Christie",
        "El Código Da Vinci - Dan Brown",
        "La Sombra del Viento - Carlos Ruiz Zafón",
        "La Chica del Tren - Paula Hawkins"
    ],
    "Romance": [
        "Bajo la Misma Estrella - John Green",
        "Orgullo y Prejuicio - Jane Austen",
        "Cumbres Borrascosas - Emily Brontë",
        "Posdata: Te Amo - Cecelia Ahern",
        "Yo Antes de Ti - Jojo Moyes",
        "El Cuaderno de Noah - Nicholas Sparks"
    ],
    "Terror": [
        "El Resplandor - Stephen King",
        "Drácula - Bram Stoker",
        "Frankenstein - Mary Shelley",
        "It - Stephen King",
        "La Casa Infernal - Richard Matheson",
        "El Exorcista - William Peter Blatty"
    ],
    "Aventura": [
        "La Isla del Tesoro - Robert Louis Stevenson",
        "Los Tres Mosqueteros - Alexandre Dumas",
        "Robinson Crusoe - Daniel Defoe",
        "El Hobbit - J.R.R. Tolkien",
        "El Conde de Montecristo - Alexandre Dumas",
        "Veinte Mil Leguas de Viaje Submarino - Jules Verne"
    ],
    "Literatura Clásica": [
        "Orgullo y Prejuicio - Jane Austen",
        "Moby Dick - Herman Melville",
        "Hamlet - William Shakespeare",
        "La Odisea - Homero",
        "Anna Karenina - Lev Tolstói",
        "El Retrato de Dorian Gray - Oscar Wilde"
    ],
    "Histórica": [
        "Los Pilares de la Tierra - Ken Follett",
        "Guerra y Paz - Lev Tolstói",
        "El Nombre de la Rosa - Umberto Eco",
        "Viento del Este, Viento del Oeste - Pearl S. Buck",
        "En el Nombre de la Rosa - Umberto Eco",
        "Memorias de una Geisha - Arthur Golden"
    ],
    "Biografía": [
        "Steve Jobs - Walter Isaacson",
        "Alexander Hamilton - Ron Chernow",
        "Churchill: A Life - Martin Gilbert",
        "El Diario de Ana Frank - Ana Frank",
        "Long Walk to Freedom - Nelson Mandela",
        "Einstein: His Life and Universe - Walter Isaacson"
    ],
    "Autobiografía": [
        "El Diario de Ana Frank - Ana Frank",
        "Mi Vida - Bill Clinton",
        "I Know Why the Caged Bird Sings - Maya Angelou",
        "Becoming - Michelle Obama",
        "Long Walk to Freedom - Nelson Mandela",
        "Educated - Tara Westover"
    ],
    "Cuentos": [
        "Cuentos Completos - Jorge Luis Borges",
        "Las Mil y Una Noches - Anónimo",
        "Cuentos de los Hermanos Grimm - Jacob Grimm y Wilhelm Grimm",
        "Cuentos de Eva Luna - Isabel Allende",
        "Cuentos de Amor, de Locura y de Muerte - Horacio Quiroga",
        "El Aleph - Jorge Luis Borges"
    ],
    "Poesía": [
        "Las Flores del Mal - Charles Baudelaire",
        "Poemas Completos - Pablo Neruda",
        "Hojas de Hierba - Walt Whitman",
        "Veinte Poemas de Amor y Una Canción Desesperada - Pablo Neruda",
        "Poeta en Nueva York - Federico García Lorca",
        "La Tierra Baldía - T.S. Eliot"
    ],
    "Drama": [
        "Hamlet - William Shakespeare",
        "Un Tranvía Llamado Deseo - Tennessee Williams",
        "Casa de Muñecas - Henrik Ibsen",
        "Muerte de un Viajante - Arthur Miller",
        "Romeo y Julieta - William Shakespeare",
        "La Casa de Bernarda Alba - Federico García Lorca"
    ],
    "Comedia": [
        "El Tartufo - Molière",
        "Mucho Ruido y Pocas Nueces - William Shakespeare",
        "La Divina Comedia - Dante Alighieri",
        "La Tía Mame - Patrick Dennis",
        "Tres Sombreros de Copa - Miguel Mihura",
        "El Mundo Según Garp - John Irving"
    ],
    "Ensayo": [
        "Ensayos - Michel de Montaigne",
        "Meditaciones - Marco Aurelio",
        "El Anti-Edipo - Gilles Deleuze y Félix Guattari",
        "El Alma del Hombre Bajo el Socialismo - Oscar Wilde",
        "La República - Platón",
        "Walden - Henry David Thoreau"
    ],
    "No Ficción": [
        "Sapiens: De Animales a Dioses - Yuval Noah Harari",
        "Homo Deus: Breve Historia del Mañana - Yuval Noah Harari",
        "Educated - Tara Westover",
        "El Gen: Una Historia Íntima - Siddhartha Mukherjee",
        "El Poder del Ahora - Eckhart Tolle",
        "Héroes y Villanos - Rebecca Solnit"
    ],
    "Policíaca": [
        "El Sabueso de los Baskerville - Arthur Conan Doyle",
        "El Halcón Maltés - Dashiell Hammett",
        "El Silencio de los Corderos - Thomas Harris",
        "El Nombre de la Rosa - Umberto Eco",
        "La Dalia Negra - James Ellroy",
        "La Novia Gitana - Carmen Mola"
    ],
    "Suspenso": [
        "La Chica del Tren - Paula Hawkins",
        "Perdida - Gillian Flynn",
        "El Código Da Vinci - Dan Brown",
        "La Viuda - Fiona Barton",
        "La Paciente Silenciosa - Alex Michaelides",
        "La Ventana Indiscreta - Cornell Woolrich"
    ],
    "Thriller": [
        "Los Hombres que no Amaban a las Mujeres - Stieg Larsson",
        "El Psicoanalista - John Katzenbach",
        "El Código Da Vinci - Dan Brown",
        "Perdida - Gillian Flynn",
        "La Chica del Tren - Paula Hawkins",
        "La Paciente Silenciosa - Alex Michaelides"
    ],
    "Ficción Juvenil": [
        "Harry Potter y la Piedra Filosofal - J.K. Rowling",
        "Los Juegos del Hambre - Suzanne Collins",
        "Crepúsculo - Stephenie Meyer",
        "Percy Jackson y el Ladrón del Rayo - Rick Riordan",
        "Divergente - Veronica Roth",
        "El Señor de las Moscas - William Golding"
    ],
    "Ficción Contemporánea": [
        "El Alquimista - Paulo Coelho",
        "La Sombra del Viento - Carlos Ruiz Zafón",
        "La Verdad Sobre el Caso Harry Quebert - Joël Dicker",
        "Los Pilares de la Tierra - Ken Follett",
        "Kafka en la Orilla - Haruki Murakami",
        "Cien Años de Soledad - Gabriel García Márquez"
    ],
    "Literatura Infantil": [
        "El Principito - Antoine de Saint-Exupéry",
        "Matilda - Roald Dahl",
        "Las Aventuras de Pinocho - Carlo Collodi",
        "Alicia en el País de las Maravillas - Lewis Carroll",
        "El Mago de Oz - L. Frank Baum",
        "La Historia Interminable - Michael Ende"
    ],
    "Fábulas": [
        "Fábulas de Esopo - Esopo",
        "Fábulas de La Fontaine - Jean de La Fontaine",
        "Fábulas - Samaniego",
        "Fábulas de Iriarte - Tomás de Iriarte",
        "Fábulas Completas - Félix María Samaniego",
        "Fábulas Fantásticas - Augusto Monterroso"
    ],
    "Mitología": [
        "La Ilíada - Homero",
        "Mitología Nórdica - Neil Gaiman",
        "El Epopeya de Gilgamesh - Anónimo",
        "Los Mitos Griegos - Robert Graves",
        "Las Metamorfosis - Ovidio",
        "Los Mitos de Cthulhu - H.P. Lovecraft"
    ],
    "Epistolar": [
        "Cartas a un Joven Poeta - Rainer Maria Rilke",
        "Las Cartas de Abelardo y Eloísa - Anónimo",
        "Querido Lector - Mary Ann Shaffer",
        "Cartas a Theo - Vincent van Gogh",
        "Cartas Desde Mi Molino - Alphonse Daudet",
        "La Soledad de los Números Primos - Paolo Giordano"
    ],
    "Viajes": [
        "En el Camino - Jack Kerouac",
        "El Corazón de las Tinieblas - Joseph Conrad",
        "El Viaje del Beagle - Charles Darwin",
        "Los Viajes de Marco Polo - Marco Polo",
        "La Vuelta al Mundo en 80 Días - Jules Verne",
        "Aventuras de un Joven Naturalista - David Attenborough"
    ],
    "Diarios": [
        "El Diario de Ana Frank - Ana Frank",
        "Diarios de la Guerra de España - George Orwell",
        "El Diario de un Escritor - Fiódor Dostoyevski",
        "Diarios - Franz Kafka",
        "Diarios 1931-1944 - Mihail Sebastian",
        "El Diario de Virginia Woolf - Virginia Woolf"
    ],
    "Memorias": [
        "Memorias de Adriano - Marguerite Yourcenar",
        "Las Memorias de Sherlock Holmes - Arthur Conan Doyle",
        "Memorias de una Geisha - Arthur Golden",
        "Las Memorias de Winston Churchill - Winston Churchill",
        "Memorias de un Hombre de Acción - Pío Baroja",
        "Memorias del Subsuelo - Fiódor Dostoyevski"
    ],
    "Ficción Experimental": [
        "Ulises - James Joyce",
        "La Casa de Hojas - Mark Z. Danielewski",
        "Tristram Shandy - Laurence Sterne",
        "Rayuela - Julio Cortázar",
        "La Naranja Mecánica - Anthony Burgess",
        "El Ruido y la Furia - William Faulkner"
    ],
    "Antología": [
        "Antología Poética - Pablo Neruda",
        "Antología Poética - Jorge Luis Borges",
        "Antología de la Literatura Fantástica - Jorge Luis Borges",
        "Antología de la Poesía Española - Anónimo",
        "Antología de la Poesía Romántica - Gustavo Adolfo Bécquer",
        "Antología de Cuentos Latinoamericanos - Anónimo"
    ],
    "Paranormal": [
        "Carrie - Stephen King",
        "El Exorcista - William Peter Blatty",
        "La Casa de los Espíritus - Isabel Allende",
        "Cementerio de Animales - Stephen King",
        "El Extraño Caso del Dr. Jekyll y Mr. Hyde - Robert Louis Stevenson",
        "Entrevista con el Vampiro - Anne Rice"
    ],
    "Distopía": [
        "1984 - George Orwell",
        "Un Mundo Feliz - Aldous Huxley",
        "El Cuento de la Criada - Margaret Atwood",
        "Fahrenheit 451 - Ray Bradbury",
        "El Hombre en el Castillo - Philip K. Dick",
        "Nosotros - Yevgueni Zamiatin"
    ],
    "Utopía": [
        "Utopía - Tomás Moro",
        "La Isla - Aldous Huxley",
        "Walden Dos - B.F. Skinner",
        "Ecotopía - Ernest Callenbach",
        "Looking Backward - Edward Bellamy",
        "Nueva Atlántida - Francis Bacon"
    ],
    "Ciencia": [
        "Breve Historia del Tiempo - Stephen Hawking",
        "El Gen: Una Historia Íntima - Siddhartha Mukherjee",
        "Sapiens: De Animales a Dioses - Yuval Noah Harari",
        "Cosmos - Carl Sagan",
        "El Origen de las Especies - Charles Darwin",
        "El Universo en una Cáscara de Nuez - Stephen Hawking"
    ],
    "Tecnología": [
        "The Innovators - Walter Isaacson",
        "The Lean Startup - Eric Ries",
        "Cómo Funciona Google - Eric Schmidt y Jonathan Rosenberg",
        "El Código Limpio - Robert C. Martin",
        "El Mito del Hombre Rápido - Frederick P. Brooks",
        "La Cuarta Revolución Industrial - Klaus Schwab"
    ],
    "Medicina": [
        "El Gen Egoísta - Richard Dawkins",
        "El Hombre que Confundió a su Mujer con un Sombrero - Oliver Sacks",
        "El Emperador de Todos los Males - Siddhartha Mukherjee",
        "La Anatomía de Gray - Henry Gray",
        "Cómo Morimos - Sherwin B. Nuland",
        "La Inmortalidad: El Futuro de la Medicina - Ray Kurzweil"
    ],
    "Psicología": [
        "El Hombre en Busca de Sentido - Viktor Frankl",
        "Psicología de la Personalidad - Marvin Zuckerman",
        "Pensar Rápido, Pensar Despacio - Daniel Kahneman",
        "Los Siete Hábitos de la Gente Altamente Efectiva - Stephen Covey",
        "Inteligencia Emocional - Daniel Goleman",
        "El Poder del Hábito - Charles Duhigg"
    ],
    "Filosofía": [
        "La República - Platón",
        "El Anticristo - Friedrich Nietzsche",
        "Así Habló Zaratustra - Friedrich Nietzsche",
        "El Mundo de Sofía - Jostein Gaarder",
        "Meditaciones - Marco Aurelio",
        "Crítica de la Razón Pura - Immanuel Kant"
    ],
    "Sociología": [
        "La Sociedad del Espectáculo - Guy Debord",
        "Vigilar y Castigar - Michel Foucault",
        "El Capital - Karl Marx",
        "Los Orígenes del Totalitarismo - Hannah Arendt",
        "El Miedo a la Libertad - Erich Fromm",
        "La Sociedad de Consumo - Jean Baudrillard"
    ],
    "Política": [
        "El Príncipe - Nicolás Maquiavelo",
        "La Democracia en América - Alexis de Tocqueville",
        "El Contrato Social - Jean-Jacques Rousseau",
        "Capitalismo y Libertad - Milton Friedman",
        "La Riqueza de las Naciones - Adam Smith",
        "El Fin de la Historia y el Último Hombre - Francis Fukuyama"
    ],
    "Economía": [
        "La Riqueza de las Naciones - Adam Smith",
        "El Capital - Karl Marx",
        "Economía en una Lección - Henry Hazlitt",
        "Pensar Rápido, Pensar Despacio - Daniel Kahneman",
        "El Capital en el Siglo XXI - Thomas Piketty",
        "Freakonomics - Steven Levitt y Stephen Dubner"
    ],
    "Educación": [
        "La Educación Prohibida - German Doin",
        "Pedagogía del Oprimido - Paulo Freire",
        "El Corazón Educativo de la Escuela - Inger Enkvist",
        "Inteligencias Múltiples - Howard Gardner",
        "La Escuela que Necesitamos - Diane Ravitch",
        "El Niño y la Cultura - Lev Vygotsky"
    ],
    "Autoayuda": [
        "Los Siete Hábitos de la Gente Altamente Efectiva - Stephen Covey",
        "El Monje que Vendió su Ferrari - Robin Sharma",
        "Cómo Ganar Amigos e Influir sobre las Personas - Dale Carnegie",
        "El Secreto - Rhonda Byrne",
        "Piense y Hágase Rico - Napoleon Hill",
        "El Poder del Ahora - Eckhart Tolle"
    ],
    "Negocios": [
        "Padre Rico, Padre Pobre - Robert Kiyosaki",
        "La Semana Laboral de 4 Horas - Timothy Ferriss",
        "El Arte de la Guerra - Sun Tzu",
        "El Lado Positivo del Fracaso - John C. Maxwell",
        "Los Secretos de la Mente Millonaria - T. Harv Eker",
        "La Inteligencia Emocional en el Trabajo - Daniel Goleman"
    ],
    "Religión": [
        "La Biblia - Anónimo",
        "El Corán - Anónimo",
        "El Libro Tibetano de los Muertos - Padmasambhava",
        "Confesiones - San Agustín",
        "El Bhagavad Gita - Anónimo",
        "El Tao Te Ching - Lao Tse"
    ],
    "Espiritualidad": [
        "El Poder del Ahora - Eckhart Tolle",
        "Los Cuatro Acuerdos - Don Miguel Ruiz",
        "El Camino del Zen - Alan Watts",
        "Un Curso de Milagros - Helen Schucman",
    ]
}       


comentarios_libro = [
    "No parecia una gran historia, era monotono y carece de trama",
    "El libro carece de desarrollo de personajes y la trama es predecible.",
    "La historia es interesante pero la ejecución deja mucho que desear.",
    "El libro tiene una trama bien construida y personajes convincentes.",
    "Una obra maestra; cautivante desde la primera página hasta el final. Altamente recomendado."
]
