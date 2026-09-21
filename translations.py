# French and Arabic string tables for build.py.
# Keys are exact English strings from the generated HTML (whitespace-tolerant matching);
# longest keys are applied first. Keys with markup (">X</a>") pin short/ambiguous words
# to their context. Model descriptions, news article bodies, and opportunity listings
# intentionally stay in English for now.

FR = {
    # ---- navigation / header ----
    ">Home</a>": ">Accueil</a>",
    ">Archive</a>": ">Archives</a>",
    ">About</a>": ">À propos</a>",
    ">Our People</a>": ">Notre équipe</a>",
    ">Art, XR &amp; Impact Opportunities</a>": ">Art, XR &amp; opportunités à impact</a>",
    ">News</a>": ">Actualités</a>",
    ">El Jem Conference</a>": ">Conférence d’El Jem</a>",
    ">TanitXR &amp; the Unique Mappers</a>": ">TanitXR &amp; les Unique Mappers</a>",
    ">Volunteer</a>": ">Bénévolat</a>",
    ">Events</a>": ">Événements</a>",
    ">Contact</a>": ">Contact</a>",
    ">Donate</a>": ">Faire un don</a>",
    ">Opportunities</a>": ">Opportunités</a>",
    ">Workshops</a>": ">Ateliers</a>",
    "AR/VR Experiences": "Expériences AR/VR",

    # ---- footer ----
    "<h4>About Tanit XR</h4>": "<h4>À propos de Tanit XR</h4>",
    "Tanit XR is a nonprofit initiative working to digitally preserve Tunisia’s cultural heritage before it disappears to time, weather, or neglect. Through 3D scanning, an open digital archive, and immersive AR/VR experiences, we make mosaics, statues, and historic sites accessible to students, researchers, and the public everywhere.":
        "Tanit XR est une initiative à but non lucratif qui œuvre à préserver numériquement le patrimoine culturel tunisien avant qu’il ne disparaisse sous l’effet du temps, des intempéries ou de la négligence. Grâce à la numérisation 3D, à des archives numériques ouvertes et à des expériences immersives AR/VR, nous rendons mosaïques, statues et sites historiques accessibles aux élèves, aux chercheurs et au grand public, partout.",
    "<h4>Explore</h4>": "<h4>Explorer</h4>",
    "<h4>Get Involved</h4>": "<h4>Participer</h4>",
    "<h4>Contact</h4>": "<h4>Contact</h4>",
    "Email: ": "E-mail : ",
    "Phone: ": "Tél. : ",
    "Fiscally sponsored by Florida Community Innovation, a U.S. 501(c)(3) nonprofit.":
        "Sous parrainage fiscal de Florida Community Innovation, organisation américaine à but non lucratif 501(c)(3).",
    "© 2026 Tanit XR. All rights reserved.": "© 2026 Tanit XR. Tous droits réservés.",
    ">Privacy Policy</a>": ">Politique de confidentialité</a>",
    "Trending now": "Tendances",

    # ---- home ----
    "<title>Home – TANIT XR</title>": "<title>Accueil – TANIT XR</title>",
    "Preserving Heritage": "Préserver le patrimoine",
    "Preserving Tunisia’s endangered heritage. Climate change, erosion, and neglect threaten our ruins. We capture them in 3D and bring them to life in AR and VR so they are never forgotten.":
        "Préserver le patrimoine tunisien en danger. Le changement climatique, l’érosion et la négligence menacent nos ruines. Nous les capturons en 3D et leur donnons vie en AR et en VR pour qu’elles ne soient jamais oubliées.",
    ">Join the Mission</a>": ">Rejoignez la mission</a>",
    "Explore the Archive →": "Explorer les archives →",
    ">Explore the Archive</a>": ">Explorer les archives</a>",
    "Digital Scanning": "Numérisation 3D",
    "Recording mosaics, statues, and ruins at risk before time, weather, and climate erase them.":
        "Documenter les mosaïques, statues et ruines menacées avant que le temps, les intempéries et le climat ne les effacent.",
    "See how we scan →": "Découvrez comment nous numérisons →",
    "Open Archive": "Archives ouvertes",
    "A free, growing online library where anyone can explore Tunisia’s heritage. Perfect for teachers, students, and the public.":
        "Une bibliothèque en ligne gratuite et en pleine croissance où chacun peut explorer le patrimoine tunisien. Idéale pour les enseignants, les élèves et le grand public.",
    "Education &amp; Workshops": "Éducation &amp; ateliers",
    "Hands-on training for students and volunteers in scanning, model cleanup, and storytelling. Programs in Tunisia and online.":
        "Formations pratiques pour étudiants et bénévoles : numérisation, nettoyage de modèles 3D et narration. Programmes en Tunisie et en ligne.",
    "Attend a workshop →": "Participer à un atelier →",
    "Immersive learning: place mosaics in your space with AR or walk inside a Roman villa in VR. Designed for schools and museums.":
        "Apprentissage immersif : placez des mosaïques chez vous en AR ou parcourez une villa romaine en VR. Conçu pour les écoles et les musées.",
    "Try a demo →": "Essayer une démo →",
    "Partnerships &amp; Research": "Partenariats &amp; recherche",
    "Working with institutions and experts to document sites, enhance accuracy, and share context so history is preserved and understood.":
        "Nous travaillons avec des institutions et des experts pour documenter les sites, améliorer la précision et partager le contexte, afin que l’histoire soit préservée et comprise.",
    "Learn &amp; participate →": "Apprendre &amp; participer →",
    "Global Volunteer Network": "Réseau mondial de bénévoles",
    "Join from Tunisia or abroad. Scan on site, help classify models, write context, or build apps that bring heritage to life.":
        "Rejoignez-nous depuis la Tunisie ou l’étranger. Numérisez sur le terrain, aidez à classer les modèles, rédigez du contexte ou créez des applications qui font vivre le patrimoine.",
    "Volunteer with us →": "Devenez bénévole →",
    "Featured Scans": "Numérisations à la une",
    "Highlights from the Tanit XR Archive": "Les incontournables des archives Tanit XR",
    ">Open the Full Archive</a>": ">Ouvrir toutes les archives</a>",
    "Why It Matters": "Pourquoi c’est important",
    "Heritage on the Brink": "Un patrimoine au bord du gouffre",
    "Tunisia’s ruins are vanishing faster than they can be protected. Climate change brings floods, storms, and heat that accelerate erosion. Without urgent action, pieces of world history could disappear.":
        "Les ruines tunisiennes disparaissent plus vite qu’on ne peut les protéger. Le changement climatique apporte inondations, tempêtes et chaleur qui accélèrent l’érosion. Sans action urgente, des pans de l’histoire mondiale pourraient disparaître.",
    "A Lasting Record": "Une trace durable",
    "With every scan, Tanit XR creates a permanent archive. Even if the physical site is lost, the digital memory survives – for schools, museums, and future generations.":
        "À chaque numérisation, Tanit XR constitue une archive permanente. Même si le site physique disparaît, la mémoire numérique survit – pour les écoles, les musées et les générations futures.",
    ">Donate Now</a>": ">Faire un don</a>",
    ">Learn More</a>": ">En savoir plus</a>",
    "Our Team": "Notre équipe",
    "Powered by our people": "Portée par nos bénévoles",
    "Tanit XR is led by a dedicated core team and powered by a growing network of volunteers across Tunisia and the world.":
        "Tanit XR est menée par une équipe dévouée et portée par un réseau croissant de bénévoles en Tunisie et dans le monde.",
    "Read More →": "Lire la suite →",
    ">Meet Everyone</a>": ">Rencontrer toute l’équipe</a>",
    "Testimonials": "Témoignages",
    "Hear from the volunteers and mentors shaping Tanit XR": "La parole aux bénévoles et mentors qui façonnent Tanit XR",
    "I joined Tanit XR because I didn’t want to see our history disappear. When you walk through ruins in Carthage or Dougga, you can already see the erosion and damage from weather and time. Volunteering with Tanit XR gave me a way to fight back against that loss. Every scan I help with feels like I’m protecting a piece of Tunisia for future generations.":
        "J’ai rejoint Tanit XR parce que je ne voulais pas voir notre histoire disparaître. Quand on marche dans les ruines de Carthage ou de Dougga, on voit déjà l’érosion et les dégâts du temps et des intempéries. Le bénévolat chez Tanit XR m’a donné un moyen de lutter contre cette perte. Chaque numérisation à laquelle je participe, c’est un morceau de la Tunisie que je protège pour les générations futures.",
    "I joined Tanit XR because of the community. I love the people involved, and I am so grateful that we get to work together to celebrate our shared global, human heritage and shine a world spotlight on one of the most beautiful countries out there: Tunisia.":
        "J’ai rejoint Tanit XR pour sa communauté. J’adore les personnes qui s’y engagent, et je suis très reconnaissante de pouvoir travailler ensemble à célébrer notre patrimoine humain commun et à braquer les projecteurs du monde sur l’un des plus beaux pays qui soient : la Tunisie.",
    "I started Tanit XR by simply walking around Carthage with my phone, scanning ruins because I couldn’t stand the idea of them being lost forever. Over time I realized this was bigger than me: people in Tunisia and abroad wanted to help, and it became a movement. Climate change, erosion, and neglect are real threats, but every scan is a way to push back, to make sure our heritage is preserved and celebrated.":
        "J’ai commencé Tanit XR en marchant simplement dans Carthage avec mon téléphone, numérisant les ruines parce que je ne supportais pas l’idée qu’elles soient perdues à jamais. Avec le temps, j’ai compris que c’était plus grand que moi : des gens en Tunisie et à l’étranger voulaient aider, et c’est devenu un mouvement. Le changement climatique, l’érosion et la négligence sont des menaces réelles, mais chaque numérisation est une façon de résister, de faire en sorte que notre patrimoine soit préservé et célébré.",
    "Artifacts Scanned": "Artéfacts numérisés",
    "Sites Documented": "Sites documentés",
    "Volunteers</span>": "Bénévoles</span>",
    "Global Reach": "Portée mondiale",
    "Partners &amp; Supporters": "Partenaires &amp; soutiens",

    # ---- archive ----
    "<title>Archive – TANIT XR</title>": "<title>Archives – TANIT XR</title>",
    "Explore the Tanit XR Archive": "Explorer les archives Tanit XR",
    "&nbsp;›&nbsp; Archive</div>": "&nbsp;›&nbsp; Archives</div>",
    "A free, growing library of 3D scans of Tunisia’s endangered heritage — mosaics, statues, stelae, and ruins captured by our volunteers. Every model can be explored interactively, and viewed in augmented reality on your phone.":
        "Une bibliothèque gratuite et en pleine croissance de numérisations 3D du patrimoine tunisien en danger — mosaïques, statues, stèles et ruines capturées par nos bénévoles. Chaque modèle peut être exploré de manière interactive, et vu en réalité augmentée sur votre téléphone.",
    '>All (': ">Tout (",
    ">View on Sketchfab</a>": ">Voir sur Sketchfab</a>",
    "← Back to Archive": "← Retour aux archives",

    # ---- news ----
    "<title>News – TANIT XR</title>": "<title>Actualités – TANIT XR</title>",
    "<h1>News</h1>": "<h1>Actualités</h1>",
    "&nbsp;›&nbsp; News</div>": "&nbsp;›&nbsp; Actualités</div>",
    ">Published ": ">Publié le ",
    "← All News": "← Toutes les actualités",

    # ---- people ----
    "<title>Our People – TANIT XR</title>": "<title>Notre équipe – TANIT XR</title>",
    "<h1>Our People</h1>": "<h1>Notre équipe</h1>",
    "&nbsp;›&nbsp; Our People</div>": "&nbsp;›&nbsp; Notre équipe</div>",
    ">Our People</a> &nbsp;›&nbsp;": ">Notre équipe</a> &nbsp;›&nbsp;",
    "Meet the team": "Rencontrez l’équipe",
    "Core Team": "Équipe principale",
    "Community Contributors": "Contributrices et contributeurs",
    "<b>Are you a Tanit XR volunteer?</b>": "<b>Vous êtes bénévole chez Tanit XR ?</b>",
    ">Create your profile</a> and it will appear here once approved.":
        ">Créez votre profil</a> et il apparaîtra ici une fois approuvé.",
    "← Back to Our People": "← Retour à l’équipe",
    "Part of the Tanit XR volunteer network.": "Membre du réseau de bénévoles Tanit XR.",

    # ---- opportunities ----
    "<title>Art, XR &amp; Impact Opportunities – TANIT XR</title>": "<title>Art, XR & opportunités à impact – TANIT XR</title>",
    "<h1>Art, XR &amp; Impact Opportunities</h1>": "<h1>Art, XR &amp; opportunités à impact</h1>",
    "&nbsp;›&nbsp; Art, XR &amp; Impact Opportunities</div>": "&nbsp;›&nbsp; Art, XR &amp; opportunités à impact</div>",
    "A curated board of grants, residencies, fellowships, open calls, and events for artists, XR creators, educators, students, and changemakers — updated regularly by the Tanit XR team. Also published as our":
        "Un tableau soigneusement sélectionné de bourses, résidences, fellowships, appels à projets et événements pour artistes, créateurs XR, enseignants, étudiants et acteurs du changement — mis à jour régulièrement par l’équipe Tanit XR. Également publié dans notre",
    ">LinkedIn newsletter</a>.": ">newsletter LinkedIn</a>.",
    'placeholder="Search…"': 'placeholder="Rechercher…"',
    '<option value="">Type</option>': '<option value="">Type</option>',
    '<option value="">Eligibility</option>': '<option value="">Éligibilité</option>',
    '<option value="">Mode</option>': '<option value="">Mode</option>',
    ">Deadline soonest</option>": ">Date limite la plus proche</option>",
    ">Newest</option>": ">Plus récentes</option>",

    # ---- volunteer ----
    "<title>Volunteer – TANIT XR</title>": "<title>Bénévolat – TANIT XR</title>",
    "<h1>Volunteer</h1>": "<h1>Bénévolat</h1>",
    "&nbsp;›&nbsp; Volunteer</div>": "&nbsp;›&nbsp; Bénévolat</div>",
    "Want to join our team of volunteers?": "Envie de rejoindre notre équipe de bénévoles ?",
    '>⏰ Closing this week</button>': '>⏰ Se termine cette semaine</button>',
    '>Quick picks</span>': '>Raccourcis</span>',
    '>For artists</button>': '>Pour les artistes</button>',
    '>For XR creators</button>': '>Pour les créateurs XR</button>',
    '>For students</button>': '>Pour les étudiants</button>',
    '>For nonprofits</button>': '>Pour les associations</button>',
    '<summary>Type <span': '<summary>Type <span',
    '<summary>Eligibility <span': '<summary>Éligibilité <span',
    '<summary>Mode <span': '<summary>Mode <span',
    '<span>Sort:</span>': '<span>Trier :</span>',
    'placeholder="Search…"': 'placeholder="Rechercher…"',
    '<option value="soon">Deadline soonest</option><option value="new">Newest</option>': '<option value="soon">Date limite proche</option><option value="new">Plus récentes</option>',
    'placeholder="Search opportunities…"': 'placeholder="Rechercher une opportunité…"',
    '>Deadline soonest</button>': '>Date limite proche</button>',
    '>Newest</button>': '>Plus récentes</button>',
    '<span class="flabel">Sort</span>': '<span class="flabel">Trier</span>',
    '<span class="flabel">Type</span>': '<span class="flabel">Type</span>',
    '<span class="flabel">Eligibility</span>': '<span class="flabel">Éligibilité</span>',
    '<span class="flabel">Mode</span>': '<span class="flabel">Mode</span>',
    'class="pill on" data-v="">All</button>': 'class="pill on" data-v="">Tout</button>',
    '>Clear filters</button>': '>Effacer les filtres</button>',
    'Get these in your inbox': 'Recevez-les dans votre boîte mail',
    'New opportunities every one to two weeks. Free.': 'De nouvelles opportunités toutes les une à deux semaines. Gratuit.',
    'Opportunities and news, in your inbox': 'Opportunités et actualités, dans votre boîte mail',
    'Grants, residencies and open calls for artists and XR creators every one to two\nweeks, only things we’d apply to ourselves, plus occasional Tanit XR news. Free, unsubscribe any time.': 'Bourses, résidences et appels pour artistes et créateurs XR toutes les une à deux semaines — uniquement ce à quoi nous postulerions nous-mêmes — plus, de temps en temps, des nouvelles de Tanit XR. Gratuit, désabonnement à tout moment.',
    '> Opportunities (every 1–2 weeks)</label>': '> Opportunités (toutes les 1–2 semaines)</label>',
    '> Tanit XR news (occasional)</label>': '> Actualités Tanit XR (occasionnelles)</label>',
    'Work with the Tanit XR team': 'Travailler avec l’équipe Tanit XR',
    '<b>Links, all optional.</b> Only the ones you add appear on your profile, as icons.': '<b>Liens — tous facultatifs.</b> Seuls ceux que vous ajoutez apparaissent sur votre profil, sous forme d’icônes.',
    '>GitHub</label>': '>GitHub</label>',
    '>Sketchfab</label>': '>Sketchfab</label>',
    'Other (YouTube, X, Behance…)': 'Autre (YouTube, X, Behance…)',
    'Show a public email icon on your profile? (optional)': 'Afficher une icône e-mail publique sur votre profil ? (facultatif)',
    'Leave empty to keep your email private': 'Laissez vide pour garder votre e-mail privé',
    ' has made with us</h2>': ' a réalisé avec nous</h2>',
    '<h2 class="sec-title" style="font-size:32px">What ': '<h2 class="sec-title" style="font-size:32px">Ce que ',
    'Scanning &amp; optimization guide for volunteers (with Rachel West and Nick Kaufmann)': 'Guide de numérisation et d’optimisation pour les bénévoles (avec Rachel West et Nick Kaufmann)',
    'Social media videos for Tanit XR': 'Vidéos pour les réseaux sociaux de Tanit XR',
    'Built for the community': 'Construit pour la communauté',
    'Virtual museum, the original room and the modular building kit': 'Musée virtuel — la salle d’origine et le kit de construction modulaire',
    'Tutorial videos for volunteers': 'Tutoriels vidéo pour les bénévoles',
    'Mentoring students': 'Mentorat d’étudiants',
    '>Services</a>': '>Services</a>',
    '<h1>Services</h1>': '<h1>Services</h1>',
    '&nbsp;›&nbsp; Services</div>': '&nbsp;›&nbsp; Services</div>',
    '>Work with us</a>': '>Travailler avec nous</a>',
    '>Work with us</div>': '>Travailler avec nous</div>',
    'What we do for volunteers, we can do for you': 'Ce que nous faisons pour nos bénévoles, nous pouvons le faire pour vous',
    'Scanning &amp; 3D optimization': 'Numérisation et optimisation 3D',
    'Workshops &amp; training': 'Ateliers et formation',
    'Sharing opportunities': 'Diffusion d’opportunités',
    'Talks &amp; consulting': 'Conférences et conseil',
    'Custom XR experiences': 'Expériences XR sur mesure',
    'Hackathon &amp; challenge tracks': 'Parcours de hackathon et défis',
    'Three steps': 'Trois étapes',
    'Tell us what you need': 'Dites-nous ce dont vous avez besoin',
    'We scope it together': 'Nous cadrons ensemble',
    'You get the work, and the community gets funded': 'Vous obtenez le travail — et la communauté est financée',
    'Get in touch': 'Contactez-nous',
    'Partner with us': 'Devenez partenaire',
    'What are you interested in?': 'Qu’est-ce qui vous intéresse ?',
    'Tell us more': 'Dites-nous en plus',
    '>Send</button>': '>Envoyer</button>',
    'Prefer to give?': 'Vous préférez donner ?',
    'Every service funds the community, so does every donation': 'Chaque service finance la communauté — comme chaque don',
    '>Organization</label>': '>Organisation</label>',
    '>Name</label>': '>Nom</label>',
    'Recorded history lessons': 'Leçons d’histoire enregistrées',
    'Julia records a short lesson each week so volunteers in any time zone can follow along and pick a task.': 'Julia enregistre chaque semaine une courte leçon pour que les bénévoles de tous les fuseaux horaires puissent suivre et choisir une tâche.',
    '— coordinated on the Thursday call.': '— coordonné lors de l’appel du jeudi.',
    'Built so far by ': 'Construit jusqu’ici par ',
    'Artifacts scanned by volunteers': 'Artefacts numérisés par des bénévoles',
    'Heritage sites documented': 'Sites patrimoniaux documentés',
    'Volunteers on four continents': 'Bénévoles sur quatre continents',
    'People reached online': 'Personnes touchées en ligne',
    '>What we do</div>': '>Ce que nous faisons</div>',
    'Six ways the community works': 'Six façons dont la communauté agit',
    'Tanit XR started with a phone and the ruins Ines grew up next to.\nToday, volunteers in Tunisia, the US, Europe and Nigeria meet every week to scan, optimize, teach each other history,\nmentor students and publish research, building a free 3D archive of Tunisia’s heritage, and a model for other\nunder-represented regions.': 'Tanit XR a commencé avec un téléphone et les ruines près desquelles Ines a grandi. Aujourd’hui, des bénévoles en Tunisie, aux États-Unis, en Europe et au Nigeria se réunissent chaque semaine pour numériser, optimiser, s’enseigner l’histoire, accompagner des étudiants et publier des recherches — et construire une archive 3D gratuite du patrimoine tunisien, ainsi qu’un modèle pour d’autres régions sous-représentées.',
    '>Virtual Museum</a>': '>Musée virtuel</a>',
    '<h1>Virtual Museum</h1>': '<h1>Musée virtuel</h1>',
    '&nbsp;›&nbsp; Virtual Museum</div>': '&nbsp;›&nbsp; Musée virtuel</div>',
    'Visit the virtual museum': 'Visiter le musée virtuel',
    'In progress': 'En cours',
    'A museum built by volunteers, from real scans': 'Un musée construit par des bénévoles, à partir de vrais scans',
    'Walkthrough recorded in the Unity editor, March 2026.': 'Visite enregistrée dans l’éditeur Unity, mars 2026.',
    'How it works': 'Comment ça marche',
    'Rooms you can walk through, objects you can get close to': 'Des salles à parcourir, des objets à approcher',
    'Real artifacts': 'De vrais artefacts',
    'Modular rooms': 'Des salles modulaires',
    'Sound from the sites': 'Le son des sites',
    'A guide': 'Une guide',
    'Headset, browser, phone': 'Casque, navigateur, téléphone',
    'Made by the community': 'Fait par la communauté',
    '>Progress</div>': '>Avancement</div>',
    'From greybox to galleries': 'Du greybox aux galeries',
    'Inside the museum': 'Dans le musée',
    'Objects made by our volunteers': 'Objets créés par nos bénévoles',
    'Browse the scans on display': 'Parcourir les scans exposés',
    'Help finish it': 'Aidez-nous à le finir',
    'Build a room. Fund a room.': 'Construisez une salle. Financez une salle.',
    'The domed hall, March 2026.': 'La salle à coupole, mars 2026.',
    'The second wing in greybox, August 2026.': 'La deuxième aile en greybox, août 2026.',
    '>Volunteer Profile (members)</a>': '>Profil bénévole (membres)</a>',
    'Once accepted, create your profile': 'Une fois accepté·e, créez votre profil',
    'Accepted volunteers get their own page here: your scans, models and articles are credited to you.': 'Les bénévoles acceptés ont leur propre page ici : vos scans, modèles et articles vous sont attribués.',
    'For accepted Tanit XR volunteers only.': 'Réservé aux bénévoles acceptés de Tanit XR.',
    'Not a volunteer yet? Start with the': 'Pas encore bénévole ? Commencez par le',
    '>volunteer interest form</a>, profiles are created after you join.': '>formulaire d’intérêt bénévole</a> — les profils sont créés après votre admission.',
    'Finalist, Best Societal Impact': 'Finaliste, Meilleur impact sociétal',
    'Episode #1728': 'Épisode #1728',
    'Video interview': 'Entretien vidéo',
    'Culture feature (Arabic)': 'Article culture (en arabe)',
    'Two exhibitions': 'Deux expositions',
    'Track sponsor 2026': 'Sponsor d’un parcours 2026',
    'Feature article': 'Article de fond',
    'Our impact so far': 'Notre impact jusqu’ici',
    'Small team, growing archive': 'Petite équipe, archive grandissante',
    'Weekly community call, Thursdays, 12 pm Eastern': 'Appel communautaire hebdomadaire — le jeudi à 12h (heure de l’Est)',
    'Join Slack and the Thursday call': 'Rejoignez Slack et l’appel du jeudi',
    '>Exhibitions</h2>': '>Expositions</h2>',
    'A scanning day for a volunteer: transport, mobile data for uploads, backups.': 'Une journée de numérisation pour un bénévole : transport, données mobiles, sauvegardes.',
    'A month of hosting and tools for the archive and the volunteers who optimize models.': 'Un mois d’hébergement et d’outils pour l’archive et les bénévoles qui optimisent les modèles.',
    'A free workshop or course session for the community, Splats With Phones, history lessons, mentoring.': 'Une séance gratuite d’atelier ou de cours pour la communauté — Splats With Phones, leçons d’histoire, mentorat.',
    'Toward the virtual museum and, one day, a professional scanner like the XGRIDS PortalCam.': 'Pour le musée virtuel et, un jour, un scanner professionnel comme le PortalCam de XGRIDS.',
    'A volunteer community from Tunisia and around the world, scanning endangered heritage in 3D and bringing it to\nlife in AR and VR, and learning from each other along the way.': 'Une communauté de bénévoles de Tunisie et du monde entier qui numérise en 3D un patrimoine menacé, le fait revivre en AR et en VR — et apprend les uns des autres en chemin.',
    '>Join the Community</a>': '>Rejoindre la communauté</a>',
    'Recognized by': 'Reconnu par',
    'Finalist, Best Societal Impact': 'Finaliste — Meilleur impact sociétal',
    'Featured video': 'Vidéo à la une',
    'Paper, 3 languages': 'Article, 3 langues',
    'Track sponsor': 'Sponsor d’un parcours',
    '>Speaker</span>': '>Intervenante</span>',
    'More than an archive': 'Plus qu’une archive',
    'One phone, the ruins of Carthage, and now a community': 'Un téléphone, les ruines de Carthage — et aujourd’hui une communauté',
    'Tanit XR started with a phone and the ruins Ines grew up next to. Today it is a\nnetwork of volunteers in Tunisia, the US, Europe and Nigeria who meet every week, scan and optimize together, teach\neach other history, mentor students, publish research and build a free 3D archive of Tunisia’s heritage. The goal is\nto take this model to other under-represented regions.': 'Tanit XR a commencé avec un téléphone et les ruines près desquelles Ines a grandi. C’est aujourd’hui un réseau de bénévoles en Tunisie, aux États-Unis, en Europe et au Nigeria qui se réunissent chaque semaine, numérisent et optimisent ensemble, s’enseignent l’histoire, accompagnent des étudiants, publient des recherches et construisent une archive 3D gratuite du patrimoine tunisien. L’objectif : porter ce modèle vers d’autres régions sous-représentées.',
    'Scan &amp; Preserve': 'Numériser et préserver',
    'Optimize &amp; Build': 'Optimiser et construire',
    'Learn Together': 'Apprendre ensemble',
    'Mentor &amp; Grow': 'Accompagner et grandir',
    'Research &amp; Share': 'Chercher et partager',
    'Extend Beyond Tunisia': 'Au-delà de la Tunisie',
    'Volunteers capture statues, mosaics and ruins with their phones. Every scan becomes a permanent, open record.': 'Les bénévoles capturent statues, mosaïques et ruines avec leur téléphone. Chaque numérisation devient une archive ouverte et permanente.',
    'Remote volunteers turn raw scans into game-ready models, AR lessons and our VR museum.': 'Des bénévoles à distance transforment les scans bruts en modèles optimisés, en leçons AR et en musée VR.',
    'Weekly community calls, history lessons on the sites we scan, and the Splats With Phones workshop.': 'Appels communautaires hebdomadaires, leçons d’histoire sur les sites numérisés, et l’atelier Splats With Phones.',
    'Interview prep, portfolio reviews and mentoring for students and early-career volunteers, across four continents.': 'Préparation aux entretiens, revues de portfolio et mentorat pour étudiants et jeunes bénévoles — sur quatre continents.',
    'Papers, conference talks, podcasts and hackathon tracks. We publish what we learn.': 'Articles, conférences, podcasts et parcours de hackathon. Nous publions ce que nous apprenons.',
    'With the Unique Mappers in Nigeria we are testing the model in a second country. Under-represented heritage everywhere is the goal.': 'Avec les Unique Mappers au Nigeria, nous testons le modèle dans un deuxième pays. Le patrimoine sous-représenté, partout, est l’objectif.',
    '>See volunteer-made models →</a>': '>Voir les modèles des bénévoles →</a>',
    '>Join the community →</a>': '>Rejoindre la communauté →</a>',
    '>Press &amp; recognition →</a>': '>Presse et reconnaissance →</a>',
    '>TanitXR &amp; the Unique Mappers →</a>': '>TanitXR et les Unique Mappers →</a>',
    '>Community</a>': '>Communauté</a>',
    '>Press &amp; Recognition</a>': '>Presse et reconnaissance</a>',
    'We meet every week': 'Nous nous réunissons chaque semaine',
    'Tanit XR is a weekly call across time zones as much as it is an archive. We\nreview each other’s scans, learn the history behind them, run workshops, prepare students for interviews, share\nTunisian culture, and celebrate wins together.': 'Tanit XR, c’est autant un appel hebdomadaire entre fuseaux horaires qu’une archive. Nous relisons nos scans, apprenons leur histoire, animons des ateliers, préparons des étudiants aux entretiens, partageons la culture tunisienne et fêtons nos réussites ensemble.',
    '<li>Weekly community call</li><li>History lessons on the sites we scan</li><li>Splats With Phones workshop</li>': '<li>Appel communautaire hebdomadaire</li><li>Leçons d’histoire sur les sites numérisés</li><li>Atelier Splats With Phones</li>',
    '<li>Mentoring &amp; interview prep</li><li>Events, talks &amp; hackathons</li><li>Cultural exchange</li>': '<li>Mentorat et préparation aux entretiens</li><li>Événements, conférences et hackathons</li><li>Échange culturel</li>',
    'See how the community works': 'Voir comment fonctionne la communauté',
    'Climate is rewriting the coastline': 'Le climat redessine le littoral',
    'Storm Harry, January 2026': 'Tempête Harry, janvier 2026',
    'The storm stripped sediment off the coast at Nabeul and exposed parts of Neapolis, an ancient city lost to a\ntsunami in the 4th century. Within days our volunteers captured the newly revealed ruins in 3D, a record that\nexists no matter what the sea does next.': 'La tempête a arraché les sédiments de la côte de Nabeul et mis au jour une partie de Neapolis, cité antique engloutie par un tsunami au IVe siècle. En quelques jours, nos bénévoles ont capturé en 3D les ruines révélées — une trace qui existe quoi que fasse la mer ensuite.',
    'Floods, storms and heat are accelerating erosion across Tunisia’s sites. Every scan is a permanent, open record:\neven if the physical site is lost, the digital memory survives, for schools, museums and future generations.': 'Inondations, tempêtes et chaleur accélèrent l’érosion des sites tunisiens. Chaque scan est une archive ouverte et permanente : même si le site disparaît, la mémoire numérique survit — pour les écoles, les musées et les générations futures.',
    'Read the Neapolis story': 'Lire l’histoire de Neapolis',
    'What people are saying': 'Ce qu’on dit de nous',
    'All press, talks &amp; papers': 'Toute la presse, conférences et publications',
    'Where we’re going': 'Où nous allons',
    'Tunisia is the pilot': 'La Tunisie est le pilote',
    'The method, phones, volunteers, open data, works anywhere heritage is\nunder-documented. In 2026 the Unique Mappers Network began scanning in Nigeria with a mini-grant from our fiscal\nsponsor. If you want to bring this to your region, talk to us.': 'La méthode — téléphones, bénévoles, données ouvertes — fonctionne partout où le patrimoine est sous-documenté. En 2026, le réseau Unique Mappers a commencé à numériser au Nigeria grâce à une mini-bourse de notre sponsor fiscal. Vous voulez l’apporter dans votre région ? Parlons-en.',
    'Bring Tanit XR to your region': 'Apporter Tanit XR dans votre région',
    'The Nigeria pilot': 'Le pilote au Nigeria',
    "How we're funded": 'Comment nous sommes financés',
    'Honest numbers': 'Des chiffres honnêtes',
    'Tanit XR is run entirely by volunteers. So far most costs, travel to\nsites, tools, hosting, hackathon prizes, have been paid out of pocket by our founders, plus a few individual donations\nthrough our fiscal sponsor, the Florida Community Innovation Foundation (a US 501(c)(3), so donations are tax-deductible).\nWe are applying for grants and building partnerships to change that. Here is what a donation does:': 'Tanit XR fonctionne entièrement grâce à des bénévoles. Jusqu’ici, la plupart des coûts — déplacements sur les sites, outils, hébergement, prix de hackathon — ont été payés de leur poche par nos fondatrices, plus quelques dons individuels via notre sponsor fiscal, la Florida Community Innovation Foundation (501(c)(3) américaine : les dons sont déductibles). Nous candidatons à des subventions et construisons des partenariats pour changer cela. Voici ce que permet un don :',
    'A scanning day: transport, mobile data for uploads, backup storage.': 'Une journée de numérisation : transport, données mobiles, sauvegarde.',
    'Full documentation of one site with several captures and research.': 'La documentation complète d’un site, avec plusieurs captures et des recherches.',
    'A field day with collaborators, and the first time we can pay local contributors.': 'Une journée de terrain avec des collaborateurs — et la première fois que nous pouvons rémunérer des contributeurs locaux.',
    'A complete digital storytelling package for one site, plus better scanning tools.': 'Un récit numérique complet pour un site, plus de meilleurs outils de numérisation.',
    '>Partner with us</a>': '>Devenir partenaire</a>',
    'See the full breakdown': 'Voir le détail complet',
    'We started as an archive. We became a community.': 'Nous avons commencé comme une archive. Nous sommes devenus une communauté.',
    'What we do together': 'Ce que nous faisons ensemble',
    'A week at Tanit XR': 'Une semaine chez Tanit XR',
    'How to get in': 'Comment nous rejoindre',
    'No archaeology or 3D background needed. Our first scans were made with a phone.': 'Aucune formation en archéologie ou en 3D requise. Nos premiers scans ont été faits avec un téléphone.',
    'Fill the volunteer form': 'Remplissez le formulaire bénévole',
    'Join Slack and the weekly call': 'Rejoignez Slack et l’appel hebdomadaire',
    'Pick a first task': 'Choisissez une première tâche',
    'Create your profile': 'Créez votre profil',
    'Meet the community': 'Rencontrer la communauté',
    'What comes out of the weekly calls': 'Ce qui sort des appels hebdomadaires',
    'Bring the model to your region': 'Apporter le modèle dans votre région',
    'Weekly community call': 'Appel communautaire hebdomadaire',
    'History lessons': 'Leçons d’histoire',
    'Mentoring &amp; interview prep': 'Mentorat et préparation aux entretiens',
    'Events &amp; conferences': 'Événements et conférences',
    'Cultural exchange': 'Échange culturel',
    '<h1>Press &amp; Recognition</h1>': '<h1>Presse et reconnaissance</h1>',
    '<h1>Community</h1>': '<h1>Communauté</h1>',
    '&nbsp;›&nbsp; Community</div>': '&nbsp;›&nbsp; Communauté</div>',
    '&nbsp;›&nbsp; Press &amp; Recognition</div>': '&nbsp;›&nbsp; Presse et reconnaissance</div>',
    'Talks &amp; events': 'Conférences et événements',
    'Podcasts &amp; video': 'Podcasts et vidéo',
    '>Articles</h2>': '>Articles</h2>',
    '>Partnerships</h2>': '>Partenariats</h2>',
    '>Awards</h2>': '>Prix</h2>',
    'Featured by Niantic Spatial': 'Mis en avant par Niantic Spatial',
    '>Publications</h2>': '>Publications</h2>',
    'Media kit': 'Kit média',
    'Support the work': 'Soutenir le travail',
    'Volunteer-run, founder-funded, so far': 'Porté par des bénévoles, financé par les fondatrices — jusqu’ici',
    'Our recognition came before our funding. Help us change that.': 'La reconnaissance est arrivée avant le financement. Aidez-nous à changer cela.',
    'How we’re funded': 'Comment nous sommes financés',
    "Made by our volunteers": "Créés par nos bénévoles",
    "Contributions to Tanit XR": "Contributions à Tanit XR",
    "Apply for the next cohort": "Candidater à la prochaine cohorte",
    ">Full Name</label>": ">Nom complet</label>",
    ">Email</label>": ">E-mail</label>",
    ">Time Zone</label>": ">Fuseau horaire</label>",
    "Why do you want to join?": "Pourquoi voulez-vous participer ?",
    "Experience Level": "Niveau d’expérience",
    "Attendance Commitment": "Engagement de présence",
    "Anything else you want us to know?": "Autre chose à nous dire ?",
    ">Apply</button>": ">Candidater</button>",
    "Any level is welcome, pick one": "Tous les niveaux sont bienvenus — choisissez",
    "This course is live and interactive, pick one": "Ce cours est en direct et interactif — choisissez",
    ">None yet<": ">Aucune pour l’instant<", ">Beginner<": ">Débutant<", ">Some experience<": ">Un peu d’expérience<",
    ">Advanced<": ">Avancé<", ">Yes, I can attend at least 5 of 6 sessions<": ">Oui, je peux assister à au moins 5 séances sur 6<",
    ">Not sure yet<": ">Pas encore sûr<",
    "Recreated by hand, for VR &amp; learning": "Recréés à la main, pour la VR et l’apprentissage",
    "<strong>heritage scans</strong>": "<strong>numérisations du patrimoine</strong>",
    "Photogrammetry records of statues, mosaics, stelae and ruins — preservation quality, with game-ready twins.":
        "Relevés photogrammétriques de statues, mosaïques, stèles et ruines — qualité de conservation, avec des jumeaux optimisés pour le jeu.",
    "<strong>models made by our volunteers</strong>": "<strong>modèles créés par nos bénévoles</strong>",
    "Lamps, pottery, plants and everyday objects modeled by hand for our virtual museum. Click to explore in 3D.":
        "Lampes, poteries, plantes et objets du quotidien modélisés à la main pour notre musée virtuel. Cliquez pour explorer en 3D.",
    "Made by volunteers (": "Créés par des bénévoles (",
    "volunteer-made models": "modèles créés par des bénévoles",
    "See all ": "Voir les ",
    "View in 3D": "Voir en 3D",
    "Make one with us": "Créez-en un avec nous",
    "Beyond scanning, our volunteers model Tunisian lamps, pottery and plants from scratch for our\nvirtual museum. Press <b>View in 3D</b> to spin one around right here.":
        "Au-delà de la numérisation, nos bénévoles modélisent lampes, poteries et plantes tunisiennes pour notre musée virtuel. Appuyez sur <b>Voir en 3D</b> pour en faire tourner un ici même.",
    "What our volunteers create": "Ce que créent nos bénévoles",
    "From a phone scan to a museum-ready model": "D’un scan au téléphone à un modèle prêt pour le musée",
    "Volunteers scan sites on the ground, optimize models for VR, write articles, and model heritage\nobjects by hand — like these.":
        "Les bénévoles numérisent les sites sur le terrain, optimisent les modèles pour la VR, écrivent des articles et modélisent des objets du patrimoine à la main — comme ceux-ci.",
    "contributions to the archive": "contributions à l’archive",
    "contribution to the archive": "contribution à l’archive",
    "Press <b>View in 3D</b> on any model to explore it right here.": "Appuyez sur <b>Voir en 3D</b> sur un modèle pour l’explorer ici même.",
    "3D scans captured": "Numérisations 3D réalisées",
    "Models optimized for game/VR": "Modèles optimisés pour le jeu/la VR",
    "Models made by hand": "Modèles créés à la main",
    "Articles written": "Articles écrits",
    "Photogrammetry scan": "Numérisation photogrammétrique",
    "Game-ready optimization": "Optimisation pour le jeu",
    "Modeled for the virtual museum": "Modélisé pour le musée virtuel",
    "Fill out our volunteer interest form and we will connect with you about available opportunities.":
        "Remplissez notre formulaire d’intérêt bénévole et nous vous contacterons au sujet des missions disponibles.",
    ">Volunteer Interest Form</a>": ">Formulaire d’intérêt bénévole</a>",
    ">Read the Scanning Guide</a>": ">Lire le guide de numérisation</a>",
    "Frequently Asked Questions": "Questions fréquentes",
    "How can I become a volunteer?": "Comment devenir bénévole ?",
    "We’re so excited that you’re interested in volunteering! Please fill out our":
        "Nous sommes ravis de votre intérêt pour le bénévolat ! Merci de remplir notre",
    ">volunteer form</a> and we’ll get back to you via email.":
        ">formulaire bénévole</a> et nous vous répondrons par e-mail.",
    "What should I know before applying?": "Que dois-je savoir avant de postuler ?",
    "Our volunteer positions are currently unpaid and remote. We work with volunteers digitally all over the globe. We have some mentorship and networking opportunities available to our volunteers based on your chosen area of focus. Areas of focus we’re currently seeking are: grant writing, XR/VR development, business development, social media management, graphic design, and general interest. All levels of experience and expertise are welcome to volunteer.":
        "Nos missions bénévoles sont actuellement non rémunérées et à distance. Nous travaillons avec des bénévoles du monde entier, en numérique. Des opportunités de mentorat et de réseautage sont proposées selon votre domaine d’intérêt. Les domaines recherchés actuellement : rédaction de demandes de subventions, développement XR/VR, développement commercial, gestion des réseaux sociaux, design graphique et intérêt général. Tous les niveaux d’expérience sont les bienvenus.",
    "How does your team work together?": "Comment votre équipe travaille-t-elle ?",
    "As a global, virtual team, it’s important for us to communicate asynchronously. The majority of our communication is done via Slack. Once a week, we meet virtually and discuss ongoing, upcoming, and blocked tasks to keep our mission moving forward.":
        "En tant qu’équipe mondiale et virtuelle, il est important pour nous de communiquer de manière asynchrone. La majorité de nos échanges passe par Slack. Une fois par semaine, nous nous réunissons en ligne pour discuter des tâches en cours, à venir et bloquées, afin de faire avancer notre mission.",
    "Are there different ways to volunteer?": "Existe-t-il différentes façons de faire du bénévolat ?",
    "As one of our goals is to engage the public in preservation work, the ability to volunteer will eventually expand and become tiered. While we build our foundation, we hold only one tier. Keep checking back to see how you can get involved!":
        "L’un de nos objectifs étant d’impliquer le public dans le travail de préservation, les possibilités de bénévolat s’élargiront progressivement en plusieurs niveaux. Pendant que nous construisons nos fondations, il n’existe qu’un seul niveau. Revenez régulièrement pour voir comment vous impliquer !",
    "Do you work with organizations and external partners?": "Travaillez-vous avec des organisations et des partenaires externes ?",
    "Preservation, cultural conservation, and climate work is done best in community. We are open to all forms of partnership that help move our mission forward. If you are an archaeologist, non-profit, government agency, or any other organization aligned in the mission of conservation or preservation, please reach out to us at":
        "La préservation, la conservation culturelle et l’action climatique se font mieux en communauté. Nous sommes ouverts à toute forme de partenariat qui fait avancer notre mission. Si vous êtes archéologue, association, agence gouvernementale ou toute autre organisation alignée sur la mission de conservation ou de préservation, contactez-nous à",
    "How much time do I need to dedicate if I become a volunteer?": "Combien de temps dois-je consacrer si je deviens bénévole ?",
    "Volunteer tasks are project and task based. After expressing your interests via the volunteer form, a member of our leadership team will reach out to you with questions about your capacity for available work that aligns with your interests and expertise. You set the expectation on how much you can commit to and what time you have.":
        "Les missions bénévoles sont organisées par projets et par tâches. Après avoir exprimé vos intérêts via le formulaire, un membre de notre équipe de direction vous contactera pour évaluer vos disponibilités sur des missions correspondant à vos intérêts et compétences. C’est vous qui fixez le niveau d’engagement et le temps que vous pouvez y consacrer.",
    "Become a volunteer": "Devenir bénévole",
    "Join us in preserving Tunisia’s cultural heritage": "Rejoignez-nous pour préserver le patrimoine culturel tunisien",
    "We rely on our international volunteer support to bring TanitXR to life. We greatly appreciate any time you are willing to share with us as we work toward the digital preservation of Tunisia’s historically and culturally rich heritage sites.":
        "Nous comptons sur le soutien de nos bénévoles internationaux pour faire vivre TanitXR. Nous apprécions énormément chaque instant que vous acceptez de partager avec nous, au service de la préservation numérique des sites patrimoniaux si riches de la Tunisie.",
    ">Create Your Volunteer Profile</a>": ">Créer votre profil bénévole</a>",

    # ---- create profile ----
    "<title>Create Your Profile – TANIT XR</title>": "<title>Créer votre profil – TANIT XR</title>",
    "<h1>Create Your Profile</h1>": "<h1>Créer votre profil</h1>",
    "&nbsp;›&nbsp; Create Your Profile</div>": "&nbsp;›&nbsp; Créer votre profil</div>",
    "Already volunteering with Tanit XR? Submit your profile and, once approved by the team, it will appear on our":
        "Déjà bénévole chez Tanit XR ? Soumettez votre profil et, une fois approuvé par l’équipe, il apparaîtra sur notre page",
    ">Our People</a> page.": ">Notre équipe</a>.",
    '>Your Name</label>': ">Votre nom</label>",
    ">Your Role / What you do</label>": ">Votre rôle / ce que vous faites</label>",
    'placeholder="e.g. 3D Generalist, XR Developer, Researcher"': 'placeholder="ex. généraliste 3D, développeur·euse XR, chercheur·euse"',
    ">Short Bio</label>": ">Courte bio</label>",
    'placeholder="A few sentences about you and what you do with Tanit XR."': 'placeholder="Quelques phrases sur vous et votre rôle chez Tanit XR."',
    ">Photo (link)</label>": ">Photo (lien)</label>",
    'placeholder="Link to a headshot (Google Drive, Dropbox, LinkedIn photo…)"': 'placeholder="Lien vers une photo (Google Drive, Dropbox, photo LinkedIn…)"',
    "Or simply reply with a photo attached when we email you back.":
        "Ou répondez simplement avec une photo en pièce jointe quand nous vous écrirons.",
    ">Website / Portfolio</label>": ">Site web / portfolio</label>",
    "Used only to contact you about your profile — it is not published.":
        "Utilisé uniquement pour vous contacter au sujet de votre profil — il n’est pas publié.",
    ">Submit Profile</button>": ">Soumettre le profil</button>",

    # ---- scanning guide ----
    "<title>Tanit XR Scanning Guide – TANIT XR</title>": "<title>Guide de numérisation – TANIT XR</title>",
    "<h1>Tanit XR Scanning Guide</h1>": "<h1>Guide de numérisation Tanit XR</h1>",
    "&nbsp;›&nbsp; Scanning Guide</div>": "&nbsp;›&nbsp; Guide de numérisation</div>",
    "Using Scaniverse to Preserve Heritage": "Utiliser Scaniverse pour préserver le patrimoine",
    "📲 Getting Started": "📲 Pour commencer",
    "<b>App:</b> Download Scaniverse from the iOS App Store (iPhone 12 Pro or newer recommended for LiDAR support).":
        "<b>Application :</b> téléchargez Scaniverse sur l’App Store iOS (iPhone 12 Pro ou plus récent recommandé pour le LiDAR).",
    "<b>Goal:</b> Create detailed 3D scans of historical landmarks, ruins, pottery, architecture, and cultural artifacts for a global digital heritage archive.":
        "<b>Objectif :</b> créer des numérisations 3D détaillées de monuments historiques, ruines, poteries, architectures et artéfacts culturels pour une archive numérique mondiale du patrimoine.",
    "🧭 Choosing What to Scan": "🧭 Choisir quoi numériser",
    "Not sure where to start? Look for objects, places, and details that carry cultural, historical, artistic, or community meaning.":
        "Vous ne savez pas par où commencer ? Cherchez des objets, des lieux et des détails porteurs de sens culturel, historique, artistique ou communautaire.",
    "<b>Good things to scan include:</b>": "<b>Bonnes choses à numériser :</b>",
    "<b>Architecture and ruins</b> — doors, arches, columns, facades, walls, courtyards, tombs, monuments, and historic homes":
        "<b>Architecture et ruines</b> — portes, arches, colonnes, façades, murs, cours, tombeaux, monuments et maisons historiques",
    "<b>Objects and artifacts</b> — pottery, tools, carvings, statues, tiles, jewelry, textiles, inscriptions, and household items":
        "<b>Objets et artéfacts</b> — poteries, outils, sculptures, statues, carreaux, bijoux, textiles, inscriptions et objets du quotidien",
    "<b>Small details</b> — patterns, textures, symbols, damage, repairs, maker’s marks, or decorative elements":
        "<b>Petits détails</b> — motifs, textures, symboles, dégradations, réparations, marques d’artisan ou éléments décoratifs",
    "<b>Everyday heritage</b> — bakeries, workshops, markets, gathering places, family heirlooms, gardens, and community spaces":
        "<b>Patrimoine du quotidien</b> — boulangeries, ateliers, marchés, lieux de rassemblement, objets de famille, jardins et espaces communautaires",
    "<b>At-risk heritage</b> — places or objects threatened by weather, neglect, development, conflict, theft, or loss of memory":
        "<b>Patrimoine en danger</b> — lieux ou objets menacés par les intempéries, la négligence, l’urbanisation, les conflits, le vol ou la perte de mémoire",
    "<b>Before scanning, ask:</b>": "<b>Avant de numériser, demandez-vous :</b>",
    "What story does this object or place tell?": "Quelle histoire cet objet ou ce lieu raconte-t-il ?",
    "Who uses it, remembers it, or cares about it?": "Qui l’utilise, s’en souvient ou y tient ?",
    "Is it connected to a tradition, craft, family, neighborhood, or historic event?":
        "Est-il lié à une tradition, un artisanat, une famille, un quartier ou un événement historique ?",
    "Is it changing, disappearing, or at risk?": "Est-il en train de changer, de disparaître ou en danger ?",
    "<b>Please do not scan sacred, private, restricted, or sensitive objects without permission.</b> When in doubt, ask a local caretaker, community member, owner, or cultural authority first.":
        "<b>Merci de ne pas numériser d’objets sacrés, privés, à accès restreint ou sensibles sans autorisation.</b> En cas de doute, demandez d’abord à un gardien local, un membre de la communauté, un propriétaire ou une autorité culturelle.",
    "🕯️ Scanning Intangible Heritage": "🕯️ Numériser le patrimoine immatériel",
    "Some heritage is not just a building or object. It lives in stories, songs, rituals, recipes, crafts, dances, languages, memories, and everyday practices. This is called <b>intangible heritage</b>.":
        "Une partie du patrimoine n’est ni un bâtiment ni un objet. Elle vit dans les récits, les chants, les rituels, les recettes, l’artisanat, les danses, les langues, les souvenirs et les pratiques quotidiennes. C’est le <b>patrimoine immatériel</b>.",
    "You cannot always 3D scan intangible heritage directly, but you can document the objects, spaces, and people connected to it. Examples:":
        "On ne peut pas toujours numériser directement le patrimoine immatériel, mais on peut documenter les objets, espaces et personnes qui y sont liés. Exemples :",
    "A traditional bread recipe → scan the oven, tools, table, or bakery space":
        "Une recette de pain traditionnelle → numérisez le four, les outils, la table ou la boulangerie",
    "A weaving practice → scan the loom, textile patterns, tools, or finished pieces":
        "Un savoir-faire de tissage → numérisez le métier à tisser, les motifs, les outils ou les pièces finies",
    "A family story → scan the home, courtyard, photograph, object, or place connected to the memory":
        "Une histoire de famille → numérisez la maison, la cour, la photographie, l’objet ou le lieu liés au souvenir",
    "A festival or ritual → scan decorations, costumes, instruments, gathering spaces, or symbolic objects":
        "Une fête ou un rituel → numérisez les décorations, costumes, instruments, lieux de rassemblement ou objets symboliques",
    "A disappearing craft → scan the tools, workshop, materials, and finished work":
        "Un artisanat en voie de disparition → numérisez les outils, l’atelier, les matériaux et les œuvres finies",
    "When documenting intangible heritage, include context with your upload: what the tradition is called, who practices it, where it happens, how you learned about it, why it matters, and any story, memory, or quote that should go with the scan.":
        "Quand vous documentez du patrimoine immatériel, joignez du contexte à votre envoi : le nom de la tradition, qui la pratique, où elle a lieu, comment vous l’avez connue, pourquoi elle compte, et toute histoire, souvenir ou citation qui devrait accompagner la numérisation.",
    "<b>Always get permission</b> before recording people, private spaces, ceremonies, sacred practices, or personal stories. Tanit XR is not just preserving objects — we are preserving the worlds, memories, and meanings around them.":
        "<b>Demandez toujours la permission</b> avant d’enregistrer des personnes, des espaces privés, des cérémonies, des pratiques sacrées ou des histoires personnelles. Tanit XR ne préserve pas seulement des objets — nous préservons les mondes, les mémoires et les significations qui les entourent.",
    "🧱 Step-by-Step Scanning Instructions": "🧱 Instructions de numérisation pas à pas",
    "1. Open Scaniverse": "1. Ouvrez Scaniverse",
    "Tap the “+” button to start a new scan.": "Touchez le bouton « + » pour démarrer une nouvelle numérisation.",
    "Choose <b>“Mesh”</b> (not “Splat”) — this is what we need for Tanit XR.":
        "Choisissez <b>« Mesh »</b> (pas « Splat ») — c’est ce dont Tanit XR a besoin.",
    "Select the size of your object: <b>Small Object</b> (pottery, carvings, statues), <b>Medium Object</b> (doors, columns, mosaics), or <b>Large Area</b> (facades, walls, monuments).":
        "Sélectionnez la taille de votre objet : <b>Small Object</b> (poteries, sculptures, statues), <b>Medium Object</b> (portes, colonnes, mosaïques) ou <b>Large Area</b> (façades, murs, monuments).",
    "2. Begin the Scan": "2. Commencez la numérisation",
    "Move slowly around the object while recording a video.": "Déplacez-vous lentement autour de l’objet pendant l’enregistrement vidéo.",
    "Get multiple angles: walk around, crouch down, raise your phone, etc.":
        "Multipliez les angles : tournez autour, accroupissez-vous, levez votre téléphone, etc.",
    "Avoid fast movements and make sure to capture all sides.":
        "Évitez les mouvements rapides et veillez à capturer toutes les faces.",
    "In bright sun, try to scan in partial shade or overcast light.":
        "En plein soleil, essayez de numériser à l’ombre partielle ou par temps couvert.",
    "3. Save Without Processing (Important!)": "3. Enregistrez sans traiter (important !)",
    "If you’re outside and don’t have strong Wi-Fi or data, tap <b>“Save to process later.”</b>":
        "Si vous êtes dehors sans bon Wi-Fi ni données mobiles, touchez <b>« Save to process later »</b>.",
    "Processing uses a lot of data — it’s best to wait until you’re home with Wi-Fi.":
        "Le traitement consomme beaucoup de données — mieux vaut attendre d’être chez vous en Wi-Fi.",
    "🗂️ Processing and Exporting": "🗂️ Traitement et export",
    "4. Back at Home: Process Your Scan": "4. De retour chez vous : traitez votre numérisation",
    "Open the Scaniverse Library (bottom menu).": "Ouvrez la bibliothèque Scaniverse (menu du bas).",
    "Tap your saved scan, tap the name, and give it a clear title (e.g., “Ksar Ouled Soltane – Main Door”).":
        "Touchez votre scan enregistré, touchez le nom et donnez-lui un titre clair (ex. « Ksar Ouled Soltane – Porte principale »).",
    "Tap “Process” and wait for the app to complete the 3D model.":
        "Touchez « Process » et attendez que l’application termine le modèle 3D.",
    "5. Export the Model": "5. Exportez le modèle",
    "Once processed, tap “Share” &gt; “Export Model.”": "Une fois traité, touchez « Share » &gt; « Export Model ».",
    "Select <b>FBX</b> format and keep <b>textures enabled</b>.": "Sélectionnez le format <b>FBX</b> et gardez les <b>textures activées</b>.",
    "Name it “Scan Title_Location”.": "Nommez-le « Titre du scan_Lieu ».",
    "6. Share Your Model": "6. Partagez votre modèle",
    "Email your exported file (or a link to it) along with a short description of the model, any historical info you know, and your name to":
        "Envoyez votre fichier exporté (ou un lien) accompagné d’une courte description du modèle, des informations historiques que vous connaissez et de votre nom à",
    "For large files, share a Google Drive, Dropbox, or WeTransfer link.":
        "Pour les gros fichiers, partagez un lien Google Drive, Dropbox ou WeTransfer.",
    "✅ Tips for Great Scans": "✅ Conseils pour de belles numérisations",
    "Scan slowly and steadily": "Numérisez lentement et régulièrement",
    "Avoid people or shadows in your scan": "Évitez les personnes et les ombres dans votre scan",
    "Focus on texture and angles, walk around the object fully": "Soignez la texture et les angles — faites le tour complet de l’objet",
    "Natural daylight is good, but harsh sun causes glare — avoid scanning at noon":
        "La lumière naturelle est idéale, mais le soleil dur crée des reflets — évitez de numériser à midi",

    # ---- splats ----
    "<title>Splats With Phones – TANIT XR</title>": "<title>Splats With Phones – TANIT XR</title>",
    "This 6-week online course introduces splats using smartphones, taught by <b>Mark Jeffcock</b>.":
        "Ce cours en ligne de 6 semaines, animé par <b>Mark Jeffcock</b>, initie aux splats avec un smartphone.",
    "Participants will learn how to capture real-world objects using a phone, turn them into 3D models and Gaussian splats, and review scans together in an immersive learning environment.":
        "Les participants apprendront à capturer des objets réels avec un téléphone, à les transformer en modèles 3D et en splats gaussiens, puis à examiner les numérisations ensemble dans un environnement d’apprentissage immersif.",
    "The cohort meets once a week at 7PM Tunisia Time (2PM Eastern) for 1 hour, for 6 weeks. No prior experience is required. Attendance and engagement matter more than technical background.":
        "La cohorte se réunit une fois par semaine à 19 h (heure de Tunisie, 14 h heure de l’Est) pendant 1 heure, sur 6 semaines. Aucune expérience préalable n’est requise. L’assiduité et l’engagement comptent plus que le bagage technique.",
    "Due to limited spots, we review applications holistically based on availability, background, and motivation. More details are shared with accepted participants.":
        "Les places étant limitées, nous examinons les candidatures de manière globale selon la disponibilité, le parcours et la motivation. Plus de détails sont communiqués aux participants retenus.",
    "<b>Want to join the next cohort?</b> Email": "<b>Envie de rejoindre la prochaine cohorte ?</b> Écrivez à",
    "with your name, time zone, a short bio, why you want to join, and whether you can attend at least 5 of the 6 live sessions.":
        "en indiquant votre nom, votre fuseau horaire, une courte bio, votre motivation et si vous pouvez assister à au moins 5 des 6 sessions en direct.",

    # ---- el jem ----
    "<title>El Jem Conference – TANIT XR</title>": "<title>Conférence d’El Jem – TANIT XR</title>",
    "<h1>El Jem Conference</h1>": "<h1>Conférence d’El Jem</h1>",
    "&nbsp;›&nbsp; El Jem Conference</div>": "&nbsp;›&nbsp; Conférence d’El Jem</div>",
    "Download the full paper": "Télécharger l’article complet",

    # ---- unique mappers ----
    "<title>TanitXR &amp; the Unique Mappers – TANIT XR</title>": "<title>TanitXR & les Unique Mappers – TANIT XR</title>",
    "<h1>TanitXR &amp; the Unique Mappers</h1>": "<h1>TanitXR &amp; les Unique Mappers</h1>",
    "&nbsp;›&nbsp; TanitXR &amp; the Unique Mappers</div>": "&nbsp;›&nbsp; TanitXR &amp; les Unique Mappers</div>",
    "TanitXR is a project, fiscally sponsored by Florida Community Innovation, that empowers volunteers and students to scan at-risk heritage sites. The goal is not only to digitally preserve these places, but also to increase appreciation for them by bringing them into XR environments and experiences.":
        "TanitXR est un projet, sous parrainage fiscal de Florida Community Innovation, qui permet à des bénévoles et à des étudiants de numériser des sites patrimoniaux en danger. L’objectif n’est pas seulement de préserver numériquement ces lieux, mais aussi d’en accroître l’appréciation en les intégrant à des environnements et expériences XR.",
    "<b>The pilot country is Tunisia, and now we are excited to expand to Nigeria with the help of the Unique Mappers!</b>":
        "<b>Le pays pilote est la Tunisie, et nous sommes ravis de nous étendre au Nigeria avec l’aide des Unique Mappers !</b>",
    ">Linked here is a PDF with background on TanitXR’s mission</a>. Read on to learn about the Unique Mappers and the scope of the TanitXR collaboration.":
        ">Voici un PDF présentant la mission de TanitXR</a>. Poursuivez votre lecture pour découvrir les Unique Mappers et le périmètre de la collaboration avec TanitXR.",
    "About the Unique Mappers": "À propos des Unique Mappers",
    "The Unique Mappers Network was founded in 2017 by Victor Sunday during his PhD studies at the University of Nigeria, Enugu. Initially, the network focused on geographic information systems (GIS) and crowdsourcing through":
        "Le réseau Unique Mappers a été fondé en 2017 par Victor Sunday pendant son doctorat à l’Université du Nigeria, à Enugu. À l’origine, le réseau se concentrait sur les systèmes d’information géographique (SIG) et le crowdsourcing via",
    "with a goal of mapping streets and buildings.": "dans le but de cartographier rues et bâtiments.",
    "Over time, it grew into a diverse community of more than 500 citizen scientists across Nigeria. They engage in participatory mapping projects for disaster response, humanitarian action, and research, with a specific focus on Sustainable Development Goals (SDGs).":
        "Au fil du temps, il est devenu une communauté diverse de plus de 500 scientifiques citoyens à travers le Nigeria. Ils mènent des projets de cartographie participative pour la réponse aux catastrophes, l’action humanitaire et la recherche, avec un accent particulier sur les Objectifs de développement durable (ODD).",
    "What sets the Unique Mappers apart is their ability to mobilize volunteers from diverse backgrounds—including students, women, and youth—for impactful mapping projects.":
        "Ce qui distingue les Unique Mappers, c’est leur capacité à mobiliser des bénévoles d’horizons divers — étudiants, femmes et jeunes — pour des projets de cartographie à fort impact.",
    "They’ve expanded their scope to include efforts like mapping flood-affected regions, monitoring oil spills, and even mapping stalled blood vessels in the brain to support Alzheimer’s research through the":
        "Ils ont élargi leur champ d’action : cartographie des régions inondées, surveillance des marées noires, et même cartographie des vaisseaux sanguins obstrués dans le cerveau pour soutenir la recherche sur Alzheimer via le projet",
    ">Learn more about their citizen science work</a>.": ">En savoir plus sur leur travail de science citoyenne</a>.",
    "Unique Mappers &amp; TanitXR Collaboration": "Collaboration Unique Mappers &amp; TanitXR",
    "Unique Mappers volunteers are receiving a $500 mini-grant from Florida Community Innovation, TanitXR’s fiscal sponsor. Before the end of 2026, they will make at least 50 scans of heritage sites and help optimize them, optionally joining weekly stand-up meetings on Thursdays at 5 PM WAT (emailing":
        "Les bénévoles des Unique Mappers reçoivent une mini-subvention de 500 $ de Florida Community Innovation, parrain fiscal de TanitXR. D’ici fin 2026, ils réaliseront au moins 50 numérisations de sites patrimoniaux et aideront à les optimiser, avec la possibilité de participer aux réunions hebdomadaires du jeudi à 17 h WAT (écrire à",
    "to receive the Zoom link).": "pour recevoir le lien Zoom).",
    "The volunteers will:": "Les bénévoles vont :",
    "Capture 3D scans of heritage sites using photogrammetry (": "Capturer des numérisations 3D de sites patrimoniaux par photogrammétrie (",
    ">full scanning guide</a>). We plan to email the team behind": ">guide complet de numérisation</a>). Nous prévoyons de contacter l’équipe de",
    "and see what heritage sites they’re okay with us scanning, or if we need to do non-restricted heritage sites that are closer to the Unique Mappers’ homes. There are also potential partners like the":
        "pour savoir quels sites patrimoniaux nous pouvons numériser, ou si nous devons nous limiter à des sites non restreints, plus proches des domiciles des Unique Mappers. Il existe aussi des partenaires potentiels comme le",
    "that we hope to speak with.": "avec qui nous espérons échanger.",
    "Engage in 3D modeling, cultural preservation, and storytelling for an online gallery of Nigerian heritage":
        "S’engager dans la modélisation 3D, la préservation culturelle et la narration pour une galerie en ligne du patrimoine nigérian",
    "Present their work in a global December 2026 webinar": "Présenter leur travail lors d’un webinaire mondial en décembre 2026",
    "<b>We are excited and the best is yet to come!</b>": "<b>Nous sommes enthousiastes, et le meilleur reste à venir !</b>",

    # ---- immersegt ----
    "<title>ImmerseGT 2026 – TANIT XR</title>": "<title>ImmerseGT 2026 – TANIT XR</title>",
    "The pilot country for scanning is Tunisia, and contributors from around the world help turn these scans into immersive experiences.":
        "Le pays pilote pour la numérisation est la Tunisie, et des contributeurs du monde entier aident à transformer ces numérisations en expériences immersives.",
    ">The one-pager summarizing our mission is here</a>.": ">La fiche d’une page résumant notre mission est ici</a>.",
    "<b>TanitXR sponsored a track at": "<b>TanitXR a parrainé un track à",
    "from April 10–12!</b> Immerse GT was a 36-hour XR hackathon at Georgia Tech that brought together designers, developers, and storytellers to build immersive experiences. We gave a $300 prize to the winning team for our track.":
        "du 10 au 12 avril !</b> Immerse GT était un hackathon XR de 36 heures à Georgia Tech réunissant designers, développeurs et conteurs pour créer des expériences immersives. Nous avons remis un prix de 300 $ à l’équipe gagnante de notre track.",
    "For our track, we invited participants to work with real TanitXR 3D models":
        "Pour notre track, nous avons invité les participants à travailler avec de vrais modèles 3D TanitXR",
    "and the models we have optimized so far:": "et les modèles que nous avons optimisés jusqu’ici :",
    "We wanted them to create creative experiences that deepen appreciation for Tunisian heritage, which has been overlooked and misrepresented on the global stage.":
        "Nous voulions qu’ils créent des expériences originales qui approfondissent l’appréciation du patrimoine tunisien, longtemps négligé et mal représenté sur la scène mondiale.",
    "We are interested in projects that help people explore, understand, or care about heritage in new ways. That might mean immersion, storytelling, education, interaction, public contribution, or something none of us has thought of yet.":
        "Nous nous intéressons aux projets qui aident les gens à explorer, comprendre ou s’attacher au patrimoine de façons nouvelles : immersion, narration, éducation, interaction, contribution du public, ou quelque chose auquel personne n’a encore pensé.",
    "<h2>Background</h2>": "<h2>Contexte</h2>",
    "Named for Tanit, the goddess of protection in ancient Carthage (where modern-day Tunisia now is), TanitXR was founded in 2025 by":
        "Nommée d’après Tanit, déesse de la protection dans l’ancienne Carthage (l’actuelle Tunisie), TanitXR a été fondée en 2025 par",
    ", a Tunisian XR developer, to preserve the historic ruins she grew up loving.":
        ", développeuse XR tunisienne, pour préserver les ruines historiques qu’elle a toujours aimées.",
    "The project focuses on places that are slowly deteriorating due to climate exposure, rising seas, extreme weather, development, and lack of preservation resources. After local volunteers scan objects and landscapes with photogrammetry and publish them as interactive models, the global community helps create a permanent digital record that can be explored online and increase appreciation of shared human heritage in Tunisia.":
        "Le projet se concentre sur des lieux qui se dégradent lentement sous l’effet du climat, de la montée des eaux, des phénomènes météorologiques extrêmes, de l’urbanisation et du manque de moyens de préservation. Une fois que les bénévoles locaux ont numérisé objets et paysages par photogrammétrie et les ont publiés comme modèles interactifs, la communauté mondiale aide à constituer un enregistrement numérique permanent, explorable en ligne, qui renforce l’appréciation du patrimoine humain commun en Tunisie.",
    "Fundamentally, this work involves teaching people how to document heritage themselves. Tunisian and other students, artists, and volunteers learn to use accessible tools such as smartphone scanning to capture objects and spaces in their communities. The result is both a growing archive of Tunisian heritage and a participatory process that connects people – both locally in Tunisia and on the global stage – with historical sites.":
        "Fondamentalement, ce travail consiste à apprendre aux gens à documenter eux-mêmes le patrimoine. Étudiants, artistes et bénévoles, tunisiens et d’ailleurs, apprennent à utiliser des outils accessibles comme la numérisation par smartphone pour capturer les objets et espaces de leurs communautés. Le résultat est à la fois une archive croissante du patrimoine tunisien et un processus participatif qui relie les gens – en Tunisie comme sur la scène mondiale – aux sites historiques.",
    "Dr. Caroline Nickerson’s Workshop at Immerse GT": "L’atelier de Dr Caroline Nickerson à Immerse GT",
    "As part of the event,": "Dans le cadre de l’événement,",
    ", led a workshop connected to the TanitXR track on Saturday, April 11, at 2 PM ET in ISyE Main 228.":
        " a animé un atelier lié au track TanitXR le samedi 11 avril à 14 h (heure de l’Est), en salle ISyE Main 228.",
    "The workshop focused on citizen science, public participation, and XR. TanitXR’s model focuses on community empowerment, and Caroline shared best practices and lessons learned from all her involvements.":
        "L’atelier portait sur la science citoyenne, la participation du public et la XR. Le modèle de TanitXR mise sur l’autonomisation des communautés, et Caroline a partagé bonnes pratiques et enseignements tirés de tous ses engagements.",
    "ImmerseGT 2026 Results": "Résultats d’ImmerseGT 2026",
    "We were thrilled to see so many creative submissions for the TanitXR track at ImmerseGT 2026. All participants had a chance to explore powerful ways to use immersive technology to preserve, interpret, and share Tunisian heritage with global audiences.":
        "Nous avons été ravis de voir autant de propositions créatives pour le track TanitXR à ImmerseGT 2026. Tous les participants ont pu explorer des façons puissantes d’utiliser la technologie immersive pour préserver, interpréter et partager le patrimoine tunisien avec le monde.",
    "<b>Track Winner:": "<b>Vainqueur du track :",
    "From Mystery to History was selected as the winner of the TanitXR track for its innovative use of XR, generative AI, and photogrammetry to reimagine cultural heritage preservation.":
        "From Mystery to History a remporté le track TanitXR pour son usage innovant de la XR, de l’IA générative et de la photogrammétrie afin de réinventer la préservation du patrimoine culturel.",
    "The project stood out for its creativity, strong execution, and meaningful alignment with TanitXR’s mission to preserve and share Tunisia’s historical legacy through immersive experiences. We are incredibly proud of the team and excited to see how this project continues to evolve!":
        "Le projet s’est distingué par sa créativité, sa solide exécution et son alignement profond avec la mission de TanitXR : préserver et partager l’héritage historique de la Tunisie à travers des expériences immersives. Nous sommes très fiers de l’équipe et impatients de voir ce projet évoluer !",
    "Other projects from the TanitXR Track also demonstrated XR’s incredible potential to bring heritage preservation to life. We are deeply grateful to every participant who contributed ideas, creativity, and passion to this challenge.":
        "Les autres projets du track TanitXR ont eux aussi démontré l’incroyable potentiel de la XR pour faire vivre la préservation du patrimoine. Nous sommes profondément reconnaissants envers chaque participant qui a apporté idées, créativité et passion à ce défi.",
    ">Review submissions here</a>.": ">Découvrez les projets ici</a>.",
    "Stay Involved After the Hackathon": "Restez impliqués après le hackathon",
    "TanitXR is not just a hackathon prompt. It is an active and growing project, and we would love to stay connected with participants who want to keep building with us after ImmerseGT.":
        "TanitXR n’est pas qu’un sujet de hackathon. C’est un projet actif et en pleine croissance, et nous serions ravis de rester en contact avec les participants qui veulent continuer à construire avec nous après ImmerseGT.",
    "There are many ways to contribute. Some volunteers help with photogrammetry and scanning. Others help with research, writing, interpretation, outreach, or immersive development. If you are interested in staying involved, sign up through our":
        "Il existe de nombreuses façons de contribuer. Certains bénévoles aident à la photogrammétrie et à la numérisation ; d’autres à la recherche, à l’écriture, à l’interprétation, à la communication ou au développement immersif. Pour rester impliqué, inscrivez-vous via notre",
    ">volunteer page</a>.": ">page bénévolat</a>.",
    "We are always excited to work with people who care about heritage, storytelling, participation, and the future of immersive technology.":
        "Nous sommes toujours heureux de travailler avec des personnes qui ont à cœur le patrimoine, la narration, la participation et l’avenir des technologies immersives.",

    # ---- about ----
    "<title>About – TANIT XR</title>": "<title>À propos – TANIT XR</title>",
    "<h1>About</h1>": "<h1>À propos</h1>",
    "&nbsp;›&nbsp; About</div>": "&nbsp;›&nbsp; À propos</div>",
    "Our Impact So Far": "Notre impact jusqu’ici",
    "Tanit XR is a community effort to save Tunisia’s heritage from climate change, erosion, and neglect. Together, we’re building a digital archive to protect it for generations.":
        "Tanit XR est un effort communautaire pour sauver le patrimoine tunisien du changement climatique, de l’érosion et de la négligence. Ensemble, nous bâtissons une archive numérique pour le protéger pour des générations.",
    "We Are A Non-Profit Organization": "Nous sommes une organisation à but non lucratif",
    "Tanit XR operates under fiscal sponsorship with Florida Community Innovation (FCI), a U.S. 501(c)(3) nonprofit. This partnership allows us to accept tax-deductible donations while we grow toward becoming a fully independent nonprofit organization.":
        "Tanit XR opère sous le parrainage fiscal de Florida Community Innovation (FCI), organisation américaine à but non lucratif 501(c)(3). Ce partenariat nous permet d’accepter des dons déductibles des impôts pendant que nous grandissons vers une organisation pleinement indépendante.",
    "Our mission is to preserve Tunisia’s endangered heritage through digital scans, immersive technology, and education. With every artifact we scan and every volunteer we train, we are proving that heritage can be safeguarded for future generations — no matter the threats of climate change and neglect.":
        "Notre mission est de préserver le patrimoine tunisien en danger grâce aux numérisations, à la technologie immersive et à l’éducation. Avec chaque artéfact numérisé et chaque bénévole formé, nous prouvons que le patrimoine peut être protégé pour les générations futures — malgré les menaces du changement climatique et de la négligence.",
    "Tanit XR advances <b>Sustainable Development Goal 11.4</b>, which focuses on safeguarding cultural and natural heritage. We view the Sustainable Development Goals as an important shared framework for linking local action to global impact.":
        "Tanit XR fait progresser la <b>cible 11.4 des Objectifs de développement durable</b>, consacrée à la sauvegarde du patrimoine culturel et naturel. Nous voyons les ODD comme un cadre commun important pour relier l’action locale à l’impact mondial.",
    "Why I Started Tanit XR": "Pourquoi j’ai créé Tanit XR",
    "I grew up walking past the ruins of Carthage every day. To me, they were just there – a backdrop of my childhood. But slowly I began to notice how pieces were missing, how mosaics cracked and crumbled, how nothing was truly protected. Tunisia’s history is not kept in vaults or guarded museums. It is left in the open air, vulnerable to time, weather, and neglect. And every year, more of it disappears.":
        "J’ai grandi en passant chaque jour devant les ruines de Carthage. Pour moi, elles étaient simplement là – le décor de mon enfance. Mais peu à peu, j’ai remarqué les morceaux manquants, les mosaïques fissurées qui s’effritaient, l’absence de véritable protection. L’histoire de la Tunisie n’est pas conservée dans des coffres ou des musées gardés. Elle est laissée à l’air libre, vulnérable au temps, aux intempéries et à la négligence. Et chaque année, une part de plus disparaît.",
    "Tanit XR was born from the fear of losing this history forever and the belief that technology can change the story. With 3D scanning, digital archiving, and immersive storytelling, we can preserve what remains and share it with the world. Each scan is more than just data; it is a memory, a voice from the past, a way of saying: we were here, and we matter.":
        "Tanit XR est née de la peur de perdre cette histoire à jamais et de la conviction que la technologie peut changer le récit. Grâce à la numérisation 3D, à l’archivage numérique et à la narration immersive, nous pouvons préserver ce qui reste et le partager avec le monde. Chaque numérisation est plus que des données : c’est une mémoire, une voix du passé, une façon de dire : nous étions là, et nous comptons.",
    ", Founder</b>": ", Fondatrice</b>",
    "Join us to protect Tunisia’s Heritage": "Rejoignez-nous pour protéger le patrimoine tunisien",
    "You don’t need to be an archaeologist or a technologist to make an impact. Our first scans were made with a phone. Whether on the ground in Tunisia or helping remotely, every volunteer contributes to preserving history.":
        "Pas besoin d’être archéologue ou technologue pour avoir un impact. Nos premières numérisations ont été faites avec un téléphone. Sur le terrain en Tunisie ou à distance, chaque bénévole contribue à préserver l’histoire.",

    # ---- contact ----
    "<title>Contact – TANIT XR</title>": "<title>Contact – TANIT XR</title>",
    "Send us your Questions/Feedback": "Envoyez-nous vos questions et retours",
    "We’ll get back to you as soon as we can.": "Nous vous répondrons dès que possible.",
    ">Email Address</label>": ">Adresse e-mail</label>",
    ">Subject</label>": ">Objet</label>",
    ">Message</label>": ">Message</label>",
    ">Send Message</button>": ">Envoyer le message</button>",
    ">Apply Now</a>": ">Postuler</a>",
    "<b>Email:</b>": "<b>E-mail :</b>",
    "<b>Phone:</b>": "<b>Tél. :</b>",

    # ---- support ----
    "<title>Support – TANIT XR</title>": "<title>Soutenir – TANIT XR</title>",
    "<h1>Support</h1>": "<h1>Soutenir</h1>",
    "&nbsp;›&nbsp; Support</div>": "&nbsp;›&nbsp; Soutenir</div>",
    "As climate change, conflict, and neglect threaten historic sites like ancient ruins, our shared global heritage is at risk.":
        "Alors que le changement climatique, les conflits et la négligence menacent les sites historiques comme les ruines antiques, notre patrimoine mondial commun est en danger.",
    "XR—a term that includes augmented and virtual reality—offers powerful tools to help. XR offers a way to preserve disappearing heritage—by capturing sites in 3D, enriching visits with storytelling, and making global history accessible from anywhere.":
        "La XR — terme qui englobe réalité augmentée et réalité virtuelle — offre des outils puissants. Elle permet de préserver un patrimoine en voie de disparition : capturer les sites en 3D, enrichir les visites par la narration et rendre l’histoire mondiale accessible de partout.",
    "Named for the ancient Carthaginian goddess of protection and the moon, if we can protect heritage in Tunisia—using immersive technology, community storytelling, and local leadership—we can build a model to safeguard cultural sites around the world.":
        "Nommée d’après l’antique déesse carthaginoise de la protection et de la lune : si nous parvenons à protéger le patrimoine en Tunisie — par la technologie immersive, la narration communautaire et le leadership local — nous pouvons bâtir un modèle pour sauvegarder les sites culturels du monde entier.",
    ">DONATE HERE</a>": ">FAIRE UN DON</a>",
    "Help cover basic costs for scanning a site: like transportation, mobile data for uploads, and backup storage.":
        "Couvre les frais de base de la numérisation d’un site : transport, données mobiles pour les envois et stockage de sauvegarde.",
    "Support detailed documentation of a site, enabling multiple 3D captures, archival research, and creating educational content to go with it.":
        "Soutient la documentation détaillée d’un site : plusieurs captures 3D, recherche d’archives et création de contenus pédagogiques associés.",
    "Sponsor a field day with collaborators, covering travel, meals, and shared equipment to scan and document endangered ruins. It also helps us start compensating local contributors for their time and expertise.":
        "Parraine une journée de terrain avec nos collaborateurs : déplacements, repas et matériel partagé pour numériser et documenter des ruines en danger. Cela nous aide aussi à commencer à rémunérer les contributeurs locaux pour leur temps et leur expertise.",
    "Fund a full digital storytelling package for one site, including high-quality 3D scans, animated walk-throughs, historical research, and immersive media production. This tier also supports the purchase of better scanning tools so we can scale beyond just a phone.":
        "Finance un ensemble complet de narration numérique pour un site : numérisations 3D haute qualité, visites animées, recherche historique et production de médias immersifs. Ce palier soutient aussi l’achat de meilleurs outils de numérisation pour aller au-delà du simple téléphone.",
    "Donations are tax-deductible through our fiscal sponsor, Florida Community Innovation, a U.S. 501(c)(3) nonprofit.":
        "Les dons sont déductibles des impôts via notre parrain fiscal, Florida Community Innovation, organisation américaine à but non lucratif 501(c)(3).",

    # ---- coming soon / privacy ----
    "<title>Coming Soon – TANIT XR</title>": "<title>Bientôt disponible – TANIT XR</title>",
    "<h1>Coming Soon</h1>": "<h1>Bientôt disponible</h1>",
    "&nbsp;›&nbsp; Coming Soon</div>": "&nbsp;›&nbsp; Bientôt disponible</div>",
    "👀 Something exciting is on the way.": "👀 Quelque chose d’enthousiasmant arrive.",
    "This page will be live soon! In the meantime, explore our archive of 3D scans or join the volunteer network helping to preserve Tunisia’s heritage.":
        "Cette page sera bientôt en ligne ! En attendant, explorez nos archives de numérisations 3D ou rejoignez le réseau de bénévoles qui aide à préserver le patrimoine tunisien.",
    ">Back Home</a>": ">Retour à l’accueil</a>",
    "<title>Privacy Policy – TANIT XR</title>": "<title>Politique de confidentialité – TANIT XR</title>",
    "<h1>Privacy Policy</h1>": "<h1>Politique de confidentialité</h1>",
    "&nbsp;›&nbsp; Privacy Policy</div>": "&nbsp;›&nbsp; Politique de confidentialité</div>",
    "Tanit XR (“we”) runs tanitxr.org to share our heritage-preservation work. We collect as little personal information as possible.":
        "Tanit XR (« nous ») édite tanitxr.org pour partager notre travail de préservation du patrimoine. Nous collectons le moins d’informations personnelles possible.",
    "What we collect": "Ce que nous collectons",
    "<b>Contact &amp; volunteer forms:</b> the name, email address, and message details you choose to send us. We use them only to reply to you and to coordinate volunteer work, and we don’t sell or share them.":
        "<b>Formulaires de contact et de bénévolat :</b> le nom, l’adresse e-mail et le contenu des messages que vous choisissez de nous envoyer. Nous les utilisons uniquement pour vous répondre et coordonner le bénévolat ; nous ne les vendons ni ne les partageons.",
    "<b>Volunteer profiles:</b> if you submit a profile for our Our People page, the name, role, bio, photo, and links you provide are published on this website after review. Email us at":
        "<b>Profils bénévoles :</b> si vous soumettez un profil pour notre page Notre équipe, le nom, le rôle, la bio, la photo et les liens fournis sont publiés sur ce site après vérification. Écrivez-nous à",
    "any time to update or remove your profile.": "à tout moment pour modifier ou supprimer votre profil.",
    "What we don’t do": "Ce que nous ne faisons pas",
    "No advertising or tracking cookies.": "Aucun cookie publicitaire ni de suivi.",
    "No sale of personal data.": "Aucune vente de données personnelles.",
    "Third parties": "Tiers",
    "This site is hosted on GitHub Pages, forms are delivered by FormSubmit, 3D models are embedded from Sketchfab, and donations are processed by Tuesday (on behalf of our fiscal sponsor, Florida Community Innovation). Each of these services has its own privacy policy.":
        "Ce site est hébergé sur GitHub Pages, les formulaires sont acheminés par FormSubmit, les modèles 3D sont intégrés depuis Sketchfab et les dons sont traités par Tuesday (pour le compte de notre parrain fiscal, Florida Community Innovation). Chacun de ces services a sa propre politique de confidentialité.",
    "Questions? Contact": "Des questions ? Contactez",

    # ---- opportunity submission form ----
    "Know an opportunity we should feature?": "Vous connaissez une opportunité à partager ?",
    "Send it our way — if it’s a fit, it will appear on this board and in the newsletter.":
        "Envoyez-la-nous — si elle correspond, elle apparaîtra sur ce tableau et dans la newsletter.",
    ">Opportunity name</label>": ">Nom de l’opportunité</label>",
    ">Link</label>": ">Lien</label>",
    ">Deadline (if you know it)</label>": ">Date limite (si vous la connaissez)</label>",
    ">Who is it for / anything we should know</label>": ">Pour qui / ce qu’il faut savoir</label>",
    ">Your name or email (optional, so we can credit or thank you)</label>":
        ">Votre nom ou e-mail (facultatif, pour vous créditer ou vous remercier)</label>",
    ">Submit Opportunity</button>": ">Envoyer l’opportunité</button>",

    # ---- newsletter subscribe band ----
    "<div class=\"eyebrow\">Newsletter</div>": "<div class=\"eyebrow\">Newsletter</div>",
    "Never miss a deadline": "Ne manquez plus aucune date limite",
    "Get new grants, residencies, and open calls for art, XR &amp; impact in your inbox — free, from the Tanit XR team. You’ll also be first to hear how our heritage-preservation work is going.":
        "Recevez les nouvelles bourses, résidences et appels à projets art, XR &amp; impact dans votre boîte mail — gratuitement, de la part de l’équipe Tanit XR. Vous serez aussi les premiers informés de l’avancée de notre travail de préservation du patrimoine.",
    'placeholder="you@example.com"': 'placeholder="vous@exemple.com"',
    ">Subscribe Free</button>": ">S’abonner gratuitement</button>",
    "No spam, opportunities and Tanit XR news only. Also published on": "Pas de spam — uniquement des opportunités et des nouvelles de Tanit XR. Également publié sur",

    # ---- volunteer reminders ----
    "🤝 This scan exists because of volunteers — from scanning on site to cleanup and research.":
        "🤝 Cette numérisation existe grâce aux bénévoles — du scan sur site au nettoyage et à la recherche.",
    ">Join us →</a>": ">Rejoignez-nous →</a>",
    ">Volunteer →</a>": ">Bénévolat →</a>",
    "Every scan here was made by a volunteer": "Chaque numérisation ici a été réalisée par un bénévole",

    # ---- reorganized nav ----
    ">Get Involved</a>": ">Participer</a>",
    ">Create Your Profile</a>": ">Créer votre profil</a>",
    ">Scanning Guide</a>": ">Guide de numérisation</a>",

    # ---- added 2026-09-21: pages that were still English ----
    'before recording people, private spaces, ceremonies, sacred practices, or\npersonal stories. Tanit XR is not just preserving objects, we are preserving the worlds, memories, and\nmeanings around them.':
        'avant d’enregistrer des personnes, des espaces privés, des cérémonies, des pratiques sacrées ou\ndes histoires personnelles. Tanit XR ne préserve pas seulement des objets, nous préservons les mondes, les mémoires et les\nsens qui les entourent.',
    'The museum is ours to build, room by room. Fund one gallery, from its walls to the objects inside and the stories Nura tells there, and it carries your name in the browser and in the headset.':
        "Le musée est à nous de bâtir, salle après salle. Financez une galerie, de ses murs aux objets qu'elle abrite et aux histoires que Nura y raconte, et elle portera votre nom dans le navigateur comme dans le casque.",
    'Unity developers, 3D artists, sound designers and writers are\nbuilding this on Thursday calls. Donations pay for the tools and hosting that get it onto headsets and into classrooms.':
        'Des développeurs Unity, des artistes 3D, des concepteurs sonores et des rédacteurs\nconstruisent tout cela lors des appels du jeudi. Les dons financent les outils et l’hébergement qui amènent ce travail sur les casques et dans les classes.',
    'Walls, arches and courtyards are built from a kit of pre-made pieces designed by Patrick Molen, so volunteers can puzzle together a new gallery without starting from scratch.':
        'Les murs, les arcs et les cours sont construits à partir d’un kit de pièces préfabriquées conçu par Patrick Molen, pour que les bénévoles puissent assembler une nouvelle salle comme un puzzle, sans repartir de zéro.',
    'Beyond photogrammetry scans, our volunteers model Tunisian objects, pottery, lamps,\ntilework, everyday heritage, from scratch, for our virtual museum and community projects.':
        'Au-delà des scans par photogrammétrie, nos bénévoles modélisent de zéro des objets tunisiens, poteries, lampes,\ncarreaux de faïence, patrimoine du quotidien, pour notre musée virtuel et nos projets communautaires.',
    'Five halls of real heritage, scanned on location by volunteers with phones and cameras.\nEvery object here can be turned, zoomed and opened in full. Nothing is behind glass.':
        'Cinq salles de patrimoine réel, numérisées sur place par des bénévoles avec des téléphones et des appareils photo.\nChaque objet ici peut être tourné, agrandi et ouvert en entier. Rien n’est derrière une vitre.',
    'The sizes on the labels are the real ones. A full museum you can walk through is being\nbuilt separately by Patrick, Cam and the team, and every object here will hang in it.':
        "Les dimensions indiquées sur les cartels sont les vraies. Un musée entier dans lequel on peut marcher est\nconstruit à part par Patrick, Cam et l'équipe, et chaque objet présenté ici y trouvera sa place.",
    'What sets the Unique Mappers apart is their ability to mobilize volunteers from diverse\nbackgrounds, including students, women and youth, for impactful mapping projects.':
        'Ce qui distingue les Unique Mappers, c’est leur capacité à mobiliser des bénévoles de tous\nhorizons, étudiants, femmes et jeunes, pour des projets de cartographie qui comptent.',
    'An evening with the Tanit XR community, planned with TAYP, the Tunisian American Young Professionals. Save the date. Details will follow here and in the newsletter.':
        'Une soirée avec la communauté Tanit XR, organisée avec TAYP, les Tunisian American Young Professionals. Notez la date. Les détails suivront ici et dans la newsletter.',
    'Everything on this site was made by volunteers, on\nThursday calls and weekend scanning trips. Whatever time you have, there is a piece of this that is yours to\ndo.':
        'Tout ce qui se trouve sur ce site a été réalisé par des bénévoles, lors des\nappels du jeudi et des sorties de numérisation du week-end. Quel que soit le temps dont vous disposez, il y a ici une part qui vous\nrevient.',
    'and tell us what you enjoy doing. Someone from the team writes back, adds you to Slack, and you meet everyone on the next Thursday call. That is the whole process.':
        "et dites-nous ce que vous aimez faire. Quelqu'un de l'équipe vous répond, vous ajoute à Slack, et vous rencontrez tout le monde lors du prochain appel du jeudi. C'est tout le processus.",
    'Two thousand years ago, families set these stones in the Tophet of Carthage. Many still carry the sign of Tanit, the goddess this whole project is named after':
        'Il y a deux mille ans, des familles ont dressé ces pierres dans le Tophet de Carthage. Beaucoup portent encore le signe de Tanit, la déesse qui a donné son nom à tout ce projet',
    'Build out the virtual museum and save toward professional scanning gear such as the XGRIDS PortalCam, so the community can capture more than a phone allows.':
        'Développer le musée virtuel et mettre de côté pour du matériel de numérisation professionnel comme la XGRIDS PortalCam, afin que la communauté puisse capturer plus que ce que permet un téléphone.',
    'Volunteers from Tunisia, the US, Europe and Nigeria meet every Thursday at 12 pm Eastern (5 pm Tunisia) to review scans, plan trips and help each other.':
        "Des bénévoles de Tunisie, des États-Unis, d'Europe et du Nigeria se retrouvent chaque jeudi à 12 h (heure de l'Est), 17 h en Tunisie, pour revoir les numérisations, préparer les sorties et s'entraider.",
    'Volunteers who have never been to Tunisia learn its history while modeling lamps, pottery and plants for our virtual museum, and we learn about theirs.':
        'Des bénévoles qui ne sont jamais allés en Tunisie découvrent son histoire en modélisant des lampes, des poteries et des plantes pour notre musée virtuel, et nous découvrons la leur.',
    'The Unique Mappers Network (500+ citizen scientists) is replicating the Tanit XR model in Nigeria with a mini-grant from our fiscal sponsor.':
        'Le Unique Mappers Network (plus de 500 scientifiques citoyens) reproduit le modèle Tanit XR au Nigeria grâce à une mini-subvention de notre parrain fiscal.',
    'Every object here, one at a time, in your browser. Turn it with a finger, hear its story\nfrom Nura, save and share it, or put on a headset.':
        'Chaque objet ici, un par un, dans votre navigateur. Tournez-le du doigt, écoutez son histoire\nracontée par Nura, enregistrez-le et partagez-le, ou mettez un casque.',
    'Mosaics from the Roman villas of Carthage. Somebody set every one of these little stones by hand, and people walked over them for centuries':
        "Des mosaïques des villas romaines de Carthage. Quelqu'un a posé chacune de ces petites pierres à la main, et on a marché dessus pendant des siècles",
    'Punic stelae, Roman statues and mosaics, doors and tilework from the medina, the same scans you find in our open archive, placed life-size.':
        'Stèles puniques, statues et mosaïques romaines, portes et carreaux de faïence de la médina, les mêmes scans que dans notre archive ouverte, placés à taille réelle.',
    'Run a free workshop or course session for the community, Splats With Phones, history lessons, mentoring and interview prep for students.':
        'Animez un atelier ou un cours gratuit pour la communauté : Splats With Phones, cours d’histoire, mentorat et préparation aux entretiens pour les étudiants.',
    'Most were captured with a phone. The halls are\nalso being rebuilt as a real space you can walk in VR, room by room, by the same team.':
        "La plupart ont été capturés avec un téléphone. Les salles sont\naussi reconstruites en un véritable espace où l'on peut marcher en VR, pièce après pièce, par la même équipe.",
    'Impact you can point at: every gallery, experience and piece your support made possible is public, in 3D, with your name beside it.':
        'Un impact que vous pouvez montrer du doigt : chaque galerie, chaque expérience et chaque pièce que votre soutien a rendues possibles sont publiques, en 3D, avec votre nom à côté.',
    'Nathan Bowser interviewed Ines Said for Niantic Spatial about Tanit XR and our Scaniverse capture of the amphitheatre of El Jem.':
        'Nathan Bowser a interviewé Ines Said pour Niantic Spatial au sujet de Tanit XR et de notre capture Scaniverse de l’amphithéâtre d’El Jem.',
    'Our paper on digital documentation, XR and citizen science for community-driven heritage preservation, presented in April 2026.':
        "Notre article sur la documentation numérique, la XR et la science citoyenne au service d'une préservation du patrimoine portée par les communautés, présenté en avril 2026.",
    'Feature on how Tanit XR uses photogrammetry, Scaniverse and Gaussian splatting to build an open archive of Tunisian heritage.':
        'Reportage sur la façon dont Tanit XR utilise la photogrammétrie, Scaniverse et le splatting gaussien pour construire une archive ouverte du patrimoine tunisien.',
    'Tell us about your team and what matters to you. We come back with two or three ways to work together, with real numbers.':
        'Parlez-nous de votre équipe et de ce qui compte pour vous. Nous revenons vers vous avec deux ou trois façons de travailler ensemble, avec des chiffres concrets.',
    'Doors and tilework from Tunis and Kairouan that still open and close every day. This is heritage people live inside':
        "Des portes et des carreaux de faïence de Tunis et de Kairouan qui s'ouvrent et se ferment encore chaque jour. C'est un patrimoine que les gens habitent",
    'Lamps, pottery and plants modeled by volunteers furnish the rooms. Optimized scans keep it light enough for phones.':
        "Des lampes, des poteries et des plantes modélisées par des bénévoles meublent les salles. Des scans optimisés gardent l'ensemble assez léger pour les téléphones.",
    'Kent Bye interviewed Ines Said at AWE USA 2026 about phone-based reality capture, volunteers and heritage at risk.':
        'Kent Bye a interviewé Ines Said à l’AWE USA 2026 au sujet de la capture du réel au téléphone, des bénévoles et du patrimoine en danger.',
    'Tanit XR, Volunteer to help protect global heritage. Cultural memory powered by volunteers and digital technology.':
        'Tanit XR, devenez bénévole pour aider à protéger le patrimoine mondial. Une mémoire culturelle portée par des bénévoles et par les technologies numériques.',
    'Ines Said spoke at Augmented World Expo USA 2026 in Long Beach, California, on XR for social impact and heritage.':
        "Ines Said est intervenue à l'Augmented World Expo USA 2026, à Long Beach en Californie, sur la XR au service de l'impact social et du patrimoine.",
    'The technique is the easy part. Our guide also covers asking permission and\ntaking care of the place you are in.':
        'La technique est la partie facile. Notre guide explique aussi comment demander l’autorisation et\nprendre soin du lieu où vous êtes.',
    'We sponsored a heritage track and a $300 prize; Dr. Caroline Nickerson led a workshop on citizen science and XR.':
        'Nous avons parrainé un parcours patrimoine et un prix de 300 $ ; Dr. Caroline Nickerson a animé un atelier sur la science participative et la XR.',
    'Cover a month of hosting and software for the open archive and the volunteers who optimize and publish models.':
        'Couvrez un mois d’hébergement et de logiciels pour l’archive ouverte et pour les bénévoles qui optimisent et publient les modèles.',
    'It has landed in the Tanit XR inbox and a volunteer will read it soon. We usually reply within a few days.':
        "C'est arrivé dans la boîte de réception de Tanit XR et un bénévole le lira bientôt. Nous répondons en général sous quelques jours.",
    'Sound is on. Tap to mute. Music: Oriental Nights by Ahmad Al-Nakib (CC BY 3.0, via the Internet Archive)':
        'Le son est activé. Touchez pour couper. Musique : Oriental Nights de Ahmad Al-Nakib (CC BY 3.0, via l’Internet Archive)',
    'Where Tanit XR has been recognized, featured and heard. For\ninterviews, talks or media requests write to':
        'Là où Tanit XR a été distinguée, citée et entendue. Pour\nles interviews, les conférences ou les demandes des médias, écrivez à',
    'Columns and capitals from the temples, baths and villas. The roofs are long gone. These stayed standing':
        'Colonnes et chapiteaux des temples, des thermes et des villas. Les toits ont disparu depuis longtemps. Ceux-ci sont restés debout',
    'A member of the team welcomes you, and you meet everyone on the next call, Thursdays at 12 pm Eastern.':
        "Un membre de l'équipe vous accueille, puis vous rencontrez tout le monde lors du prochain appel, le jeudi à 12 h (heure de l'Est).",
    'Ambient sound recorded at the real places, wind, footsteps, echoes, so each gallery feels different.':
        "Des sons d'ambiance enregistrés sur les lieux réels, le vent, les pas, les échos, pour que chaque galerie ait son caractère.",
    'Optimize a scan, write the history of an object, model something Tunisian, or plan a scanning trip.':
        'Optimisez une numérisation, écrivez l’histoire d’un objet, modélisez quelque chose de tunisien ou préparez une sortie de numérisation.',
    ', bakeries, workshops, markets, gathering places, family heirlooms, gardens, and community spaces':
        ', boulangeries, ateliers, marchés, lieux de rassemblement, objets de famille, jardins et espaces communautaires',
    'New Neapolis Site Revealed By Recent Floods(Storm Harry) In Tunisia. Scanned by Youssef Lakdhar!.':
        'Nouveau site de Neapolis révélé par les récentes inondations (tempête Harry) en Tunisie. Numérisé par Youssef Lakdhar !.',
    ', pottery, tools, carvings, statues, tiles, jewelry, textiles, inscriptions, and household items':
        ', poteries, outils, sculptures, statues, carreaux de faïence, bijoux, textiles, inscriptions et objets du quotidien',
    'Ines Said on why Tanit XR exists and where it is going, published in the Women Write collection.':
        'Ines Said explique pourquoi Tanit XR existe et où elle va, dans la collection Women Write.',
    'Medium / Women Write, Tanit XR: Preserving Tunisia&#x27;s Heritage Through Immersive Technology':
        'Medium / Women Write, Tanit XR : préserver le patrimoine tunisien grâce aux technologies immersives',
    'The virtual museum in March 2026: a domed hall with striped arches, tiled floors and a fountain':
        'Le musée virtuel en mars 2026 : une salle à coupole avec des arcs rayés, des sols carrelés et une fontaine',
    'Portfolio reviews, mock interviews and career advice for students and early-career volunteers.':
        'Relecture de portfolios, entretiens blancs et conseils de carrière pour les étudiants et les bénévoles en début de parcours.',
    'The second wing of the virtual museum under construction, a colonnade and galleries in greybox':
        'La deuxième aile du musée virtuel en construction, une colonnade et des galeries en greybox',
    'A 6-week course with Mark Jeffcock on capturing 3D models and Gaussian splats with a phone.':
        'Un cours de 6 semaines avec Mark Jeffcock sur la capture de modèles 3D et de splats gaussiens avec un téléphone.',
    'Pick one, or shape one with us. We build each partnership around your team and your budget.':
        'Choisissez-en une, ou façonnons-la ensemble. Nous construisons chaque partenariat autour de votre équipe et de votre budget.',
    'A loom, a carpet. Nothing grand, just what people used, which is exactly why we kept them':
        "Un métier à tisser, un tapis. Rien de grandiose, juste ce dont les gens se servaient, et c'est exactement pour cela que nous les avons gardés",
    'Two hands holding a phone that shows the Draped Statue of Byrsa Hill in augmented reality':
        'Deux mains tenant un téléphone qui montre la Statue drapée de la colline de Byrsa en réalité augmentée',
    'Latin and Arabic inscriptions, every letter cut by hand. Some of them can still be read':
        'Des inscriptions latines et arabes, chaque lettre gravée à la main. Certaines se lisent encore',
    'What you do, what you are studying, or any communities or projects you are involved in.':
        'Ce que vous faites, ce que vous étudiez, ou les communautés et les projets auxquels vous participez.',
    ', patterns, textures, symbols, damage, repairs, maker’s marks, or decorative elements':
        ', motifs, textures, symboles, dégâts, réparations, marques d’artisan ou éléments décoratifs',
    'Every share helps more people see this. Pick where it goes, the caption comes along.':
        'Chaque partage permet à plus de monde de le voir. Choisissez où il part, la légende suit.',
    "Send it our way, if it's a fit, it will appear on this board\nand in the newsletter.":
        "Envoyez-le nous, si cela correspond, l'annonce apparaîtra sur ce tableau\net dans la newsletter.",
    'Carthage Magazine, Preserving Tunisia&#x27;s Heritage Through Immersive Technology':
        'Carthage Magazine, préserver le patrimoine tunisien grâce aux technologies immersives',
    'Material and Meaning: Marble Identity, and Cultural Exchange in Ancient Carthage':
        'Matière et sens : marbre, identité et échanges culturels dans la Carthage antique',
    'A tagine and a plate: the everyday Tunisia our volunteers wanted in the museum':
        'Un tajine et une assiette : la Tunisie de tous les jours que nos bénévoles voulaient dans le musée',
    'Music: Oriental Nights by Ahmad Al-Nakib (CC BY 3.0, via the Internet Archive)':
        "Musique : Oriental Nights d'Ahmad Al-Nakib (CC BY 3.0, via l'Internet Archive)",
    'Succulents, a cactus, clay pots and palms for the museum&#x27;s courtyards':
        'Des plantes grasses, un cactus, des pots en terre cuite et des palmiers pour les patios du musée',
    'The virtual museum courtyard with a pool, terraces and a sculpted canopy':
        'La cour du musée virtuel avec un bassin, des terrasses et un auvent sculpté',
    'Voices of VR #1728, Preserving Tunisian Cultural Heritage with Tanit XR':
        'Voices of VR #1728, préserver le patrimoine culturel tunisien avec Tanit XR',
    'Carved Architectural Blocks with Laurel Motifs, Water Temple, Zaghouan':
        'Blocs architecturaux sculptés à motifs de laurier, Temple des Eaux, Zaghouan',
    'Carved Architectural Block with Laurel Motifs, Water Temple, Zaghouan':
        'Bloc architectural sculpté à motifs de laurier, Temple des Eaux, Zaghouan',
    'El Jem Conference 2026, Paper in English, French and Tunisian Arabic':
        'Conférence d’El Jem 2026, article en anglais, français et arabe tunisien',
    'Second wing under construction, colonnade and galleries in greybox.':
        'Deuxième aile en construction, colonnade et galeries en greybox.',
    'Not Your Grandma’s Gallery – Open Call for Artists (The Holy Art)':
        'Not Your Grandma’s Gallery – Appel ouvert aux artistes (The Holy Art)',
    'The murex shell whose dye made Carthage rich and its cloth purple':
        'Le coquillage murex dont la teinture a enrichi Carthage et empourpré ses étoffes',
    'Used only to contact you about your profile, it is not published.':
        "Utilisé uniquement pour vous contacter au sujet de votre profil, il n'est pas publié.",
    'An amphora wearing a graduation cap, with a book titled Carthage':
        "Une amphore coiffée d'une toque de diplômé, avec un livre intitulé Carthage",
    'Looking for a specific scan, a\ndownload or the game-ready twins?':
        'Vous cherchez un scan précis, un\ntéléchargement ou les jumeaux prêts pour le jeu ?',
    'A globe with Tanit XR volunteers standing on every continent':
        'Un globe avec des bénévoles Tanit XR sur chaque continent',
    'VIVERSE Creator Program – Creator Grants for WebXR Worlds':
        'VIVERSE Creator Program – Bourses pour créateurs de mondes WebXR',
    'UNESCO Youth Climate Action Network – YoU-CAN Membership':
        "Réseau des jeunes de l'UNESCO pour l'action climatique – adhésion YoU-CAN",
    'Inscribed Architectural Fragment – Byrsa Hill, Carthage':
        'Fragment architectural inscrit – Colline de Byrsa, Carthage',
    'CityCamp Gainesville Hack Day 2026, heritage challenge':
        'CityCamp Gainesville Hack Day 2026, défi patrimoine',
    'Courtyard with pool, terraces and the sculpted canopy.':
        'Patio avec bassin, terrasses et auvent sculpté.',
    'TanitXR &amp; the Unique Mappers, expanding to Nigeria':
        'TanitXR et les Unique Mappers, une extension au Nigeria',
    'Games for Change 2026 Student Challenge (Competition)':
        'Games for Change 2026, défi étudiant (concours)',
    'Mini history lesson 2, Carthage&#x27;s craft quarters':
        "Mini leçon d'histoire 2, les quartiers artisanaux de Carthage",
    'Volunteer with Tanit XR, Preserve Heritage in 3D & XR':
        'Devenez bénévole avec Tanit XR, préservez le patrimoine en 3D et en XR',
    'Traditional Loom with Woven Carpet – Medina of Tunis':
        'Métier à tisser traditionnel avec tapis tissé – Médina de Tunis',
    'ImmerseGT at Georgia Tech, sponsored heritage track':
        'ImmerseGT à Georgia Tech, parcours patrimoine parrainé',
    'Morgan-Menil Fellowship 2026-27 (Drawing Institute)':
        'Bourse Morgan-Menil 2026-27 (Drawing Institute)',
    'Traditional Loom with Woven Carpet, Medina of Tunis':
        'Métier à tisser traditionnel avec tapis tissé, Médina de Tunis',
    'CityCamp Gainesville Hack Day: two Tanit XR tracks':
        'CityCamp Gainesville Hack Day : deux parcours Tanit XR',
    'Decorated Bust Fragment – Roman Villas of Carthage':
        'Fragment de buste décoré – Villas romaines de Carthage',
    'Bird and Floral Mosaic – Roman Villas of Carthage':
        'Mosaïque aux oiseaux et aux fleurs – Villas romaines de Carthage',
    'Decorated Bust Fragment, Roman villas of Carthage':
        'Fragment de buste décoré, villas romaines de Carthage',
    'Mihrab Niche – Madrasa Al-Bachia, Medina of Tunis':
        'Niche du mihrab – Medersa Al-Bachia, Médina de Tunis',
    'Bird and Floral Mosaic, Roman villas of Carthage':
        'Mosaïque aux oiseaux et aux fleurs, villas romaines de Carthage',
    'Decorated Bust Fragment – Roman Villas of Carth…':
        'Fragment de buste décoré – Villas romaines de Carth…',
    'Folger Institute Long-Term Fellowships 2026-2027':
        'Bourses de longue durée du Folger Institute 2026-2027',
    'Latin Inscription Slab  Water Temple of Zaghouan':
        'Dalle à inscription latine  Temple des Eaux de Zaghouan',
    'Roman Mosaic with Bird and Vine Motifs – Villas…':
        "Mosaïque romaine à motifs d'oiseaux et de vigne – Villas…",
    'Wooden Door with Tilework – Zawiya of Sidi Sahbi':
        'Porte en bois aux carreaux de faïence – Zaouïa de Sidi Sahbi',
    'Punic Stelae Row – Tophet of Salammbo, Carthage':
        'Rangée de stèles puniques – Tophet de Salammbô, Carthage',
    'Wooden Door with Tilework, Zawiya of Sidi Sahbi':
        'Porte en bois aux carreaux de faïence, Zaouïa de Sidi Sahbi',
    'Bird of Prey Statue – Roman Villas of Carthage':
        "Statue d'oiseau de proie – Villas romaines de Carthage",
    'Bobby Anspach Studios Foundation Grant Program':
        'Programme de bourses de la Bobby Anspach Studios Foundation',
    'Latin Inscription Slab, Water Temple, Zaghouan':
        'Dalle à inscription latine, Temple des Eaux, Zaghouan',
    'Punic Stelae Row, Tophet of Salammbo, Carthage':
        'Rangée de stèles puniques, Tophet de Salammbô, Carthage',
    'Reviewing scans together in an immersive space':
        'Revoir les numérisations ensemble dans un espace immersif',
    'Water and stone for the museum&#x27;s open air':
        "De l'eau et de la pierre pour l'espace en plein air du musée",
    'Architectural Fragments  - Baths of Antoninus': 'Fragments architecturaux  - Thermes d’Antonin',
    'Bird of Prey Statue, Roman villas of Carthage':
        "Statue d'oiseau de proie, villas romaines de Carthage",
    'Carved Architectural Block with Laurel Motifs':
        'Bloc architectural sculpté à motifs de laurier',
    'Every one of these was scanned by a volunteer': 'Chacun d’eux a été numérisé par un bénévole',
    'Fluted Column Fragment – Byrsa Hill, Carthage':
        'Fragment de colonne cannelée – Colline de Byrsa, Carthage',
    'Headless Draped Statue – Byrsa Hill, Carthage':
        'Statue drapée sans tête – Colline de Byrsa, Carthage',
    "Keep a country's memory, with your name on it":
        'Préservez la mémoire d’un pays, avec votre nom dessus',
    'Reitz Union, Room G330, University of Florida':
        'Reitz Union, salle G330, University of Florida',
    'Inscribed Architectural Fragment, Byrsa Hill':
        'Fragment architectural inscrit, colline de Byrsa',
    'Leadership and Techplomacy Summit Dubai 2026': 'Leadership and Techplomacy Summit Dubaï 2026',
    'Male Torso Statue – Roman Villas of Carthage': 'Torse masculin – Villas romaines de Carthage',
    'Punic Stelae – Tophet of Salammbo (Carthage)':
        'Stèles puniques – Tophet de Salammbô (Carthage)',
    'Architectural Fragments, Baths of Antoninus': 'Fragments architecturaux, thermes d’Antonin',
    'First Phoenicians and Tyrian Purple Origins':
        'Les premiers Phéniciens et les origines de la pourpre de Tyr',
    'Ornamental Mihrab (Mahram), Medina of Tunis': 'Mihrab ornemental (mahram), Médina de Tunis',
    'Roman Togatus Statue – Byrsa Hill, Carthage':
        'Statue romaine de togatus – Colline de Byrsa, Carthage',
    'Sacred Niche – Roman Water Temple, Zaghouan': 'Niche sacrée – Temple des Eaux romain, Zaghouan',
    'Marble Calligraphic Panel – Zitouna Mosque':
        'Panneau calligraphique en marbre – Mosquée Zitouna',
    'Punic Stela – Tophet of Salammbo, Carthage': 'Stèle punique – Tophet de Salammbô, Carthage',
    'Punic Stelae, Tophet of Salammbo, Carthage': 'Stèles puniques, tophet de Salammbô, Carthage',
    'Roman Draped Statue – Byrsa Hill, Carthage':
        'Statue romaine drapée – Colline de Byrsa, Carthage',
    'Tanit Stela – Tophet of Salammbo, Carthage': 'Stèle de Tanit – Tophet de Salammbô, Carthage',
    'Corinthian Capital – Byrsa Hill, Carthage': 'Chapiteau corinthien – Colline de Byrsa, Carthage',
    'Creative Director / Experiential Designer':
        "Directrice ou directeur créatif / Conception d'expériences",
    'Statue Fragment, Roman villas of Carthage': 'Fragment de statue, villas romaines de Carthage',
    'Tanit XR at CityCamp Gainesville Hack Day': 'Tanit XR au CityCamp Gainesville Hack Day',
    'Tilework Wall Panel, Zawiya of Sidi Sahbi':
        'Panneau mural en carreaux de faïence, zaouïa de Sidi Sahbi',
    'Bust Fragment – Roman Villas of Carthage': 'Fragment de buste – Villas romaines de Carthage',
    'Photogrammetry, Grants and Opportunities': 'Photogrammétrie, bourses et opportunités',
    'A 2,000-Year-Old Ghost Town on Cape Bon': 'Une ville fantôme vieille de 2 000 ans au Cap Bon',
    'Bir (Traditional Well), Medina of Tunis': 'Bir (puits traditionnel), Médina de Tunis',
    'Bust Fragment, Roman villas of Carthage': 'Fragment de buste, villas romaines de Carthage',
    'Come and help us keep Tunisia’s history':
        'Venez nous aider à préserver l’histoire de la Tunisie',
    'Reclining Figure – Byrsa Hill, Carthage': 'Figure allongée – Colline de Byrsa, Carthage',
    'Large Azure Stonecrop Succulent in Pot': 'Grande plante grasse bleutée en pot',
    'Small Azure Stonecrop Succulent in Pot': 'Petite plante grasse bleutée en pot',
    'Adopt a gallery in the virtual museum': 'Adoptez une salle du musée virtuel',
    'Do I need to know 3D, or archaeology?': 'Faut-il connaître la 3D ou l’archéologie ?',
    'Preservation scan and game-ready twin':
        'Numérisation 3D de conservation et jumeau prêt pour le jeu',
    'Washington, DC. Venue to be announced': 'Washington, DC. Lieu à annoncer',
    'Gaussian splat captured with a phone': 'Splat gaussien capturé avec un téléphone',
    'Sacred Niche, Water Temple, Zaghouan': 'Niche sacrée, temple des Eaux, Zaghouan',
    'See the whole collection at a glance': "Voir toute la collection d'un coup d'œil",
    'Your team&#x27;s hours, on real work': 'Les heures de votre équipe, sur du travail réel',
    'Interior with Tilework and Fountain': 'Intérieur avec carreaux de faïence et fontaine',
    'Learn to capture in 3D with a phone': 'Apprenez à capturer en 3D avec un téléphone',
    'Niantic Spatial feature on Tanit XR': 'Article de Niantic Spatial sur Tanit XR',
    'Roman Column – Byrsa Hill, Carthage': 'Colonne romaine – Colline de Byrsa, Carthage',
    'Stone Basin, Water Temple, Zaghouan': 'Bassin en pierre, temple des Eaux, Zaghouan',
    'Headless Draped Statue, Byrsa Hill': 'Statue drapée sans tête, colline de Byrsa',
    'Niche Wall, Water Temple, Zaghouan': 'Mur à niches, temple des Eaux, Zaghouan',
    'Press &amp; Recognition – TANIT XR': 'Presse et distinctions – TANIT XR',
    'The picture you are about to share': "L'image que vous allez partager",
    'Traditional Loom with Woven Carpet': 'Métier à tisser traditionnel avec tapis tissé',
    'Reality Hack 2026 Art Grant (MIT)': 'Bourse artistique Reality Hack 2026 (MIT)',
    'Sunday, September 20, 10am to 6pm': 'Dimanche 20 septembre, de 10h à 18h',
    'Take the four-minute guided visit': 'Faites la visite guidée de quatre minutes',
    'Tanit XR in person, Washington DC': 'Tanit XR en personne, Washington DC',
    'Transparent background, red mark.': 'Fond transparent, marque rouge.',
    'A Beginning: Why Tanit XR Exists': 'Un début : pourquoi Tanit XR existe',
    "Explore Tunisia's heritage in 3D": 'Explorez le patrimoine tunisien en 3D',
    'Inscribed Architectural Fragment': 'Fragment architectural inscrit',
    'Tunisian Wooden Woven Table Lamp': 'Lampe de table tunisienne en bois tressé',
    'What a partnership can look like': 'À quoi peut ressembler un partenariat',
    'Roman Draped Statue, Byrsa Hill': 'Statue romaine drapée, colline de Byrsa',
    'Domed hall with striped arches': 'Salle à coupole aux arcs rayés',
    'A care day for a coastal site': "Une journée d'entretien pour un site côtier",
    'Mihrab Niche, Medina of Tunis': 'Niche de mihrab, Médina de Tunis',
    'Murex Shell - Murex Brandaris': 'Coquillage murex - Murex brandaris',
    'Punic and Roman, exposed 2026': 'Punique et romain, mis au jour en 2026',
    '3D Modeler & Web Contributor': 'Modeleur 3D et contributeur web',
    'El Jem Conference 2026 paper': "Communication, conférence d'El Jem 2026",
    'Immerse the Bay XR Hackathon': 'Hackathon XR Immerse the Bay',
    'Reclining Figure, Byrsa Hill': 'Figure allongée, colline de Byrsa',
    'Galleries, with the stories': 'Les galeries, avec les histoires',
    'How much time does it take?': 'Combien de temps faut-il y consacrer ?',
    'RAY Fellowship Program 2026': 'Programme de bourses RAY 2026',
    'See the projects on Devpost': 'Voir les projets sur Devpost',
    'Splats With Phones workshop': 'Atelier Splats With Phones',
    'Strategy & Creative Support': 'Stratégie et soutien créatif',
    'Wall with the sign of Tanit': 'Mur au signe de Tanit',
    'Event · September 20, 2026': 'Événement · 20 septembre 2026',
    'Mentoring & interview prep': 'Mentorat et préparation aux entretiens',
    'Ornamental Mihrab (Mahram)': 'Mihrab ornemental (Mahram)',
    '2D Design & 3D Generalist': 'Design 2D et généraliste 3D',
    'Courtyard fountain, large': 'Fontaine de cour, grande',
    'Draped Statue, Byrsa Hill': 'Statue drapée, colline de Byrsa',
    'Fund the community itself': 'Financez la communauté elle-même',
    'How do you work together?': 'Comment travaillez-vous ensemble ?',
    'NEW INC Year 13 Open Call': 'NEW INC, appel à candidatures de la 13e année',
    'See it in your space (AR)': "Voir l'objet chez vous (RA)",
    'Splats With Phones course': 'Cours Splats With Phones',
    'What we have already done': 'Ce que nous avons déjà fait',
    'Explore in 3D – TANIT XR': 'Explorer en 3D – TANIT XR',
    'Fountains and courtyards': 'Fontaines et patios',
    'Illustrator and Designer': 'Illustration et design',
    'Partnerships & Community': 'Partenariats et communauté',
    'Press · October 12, 2025': 'Presse · 12 octobre 2025',
    'Roman Column, Byrsa Hill': 'Colonne romaine, colline de Byrsa',
    'Roman villas of Carthage': 'Villas romaines de Carthage',
    'See the experience first': 'Voir l’expérience d’abord',
    'Bring it to your region': 'Amenez le projet dans votre région',
    'Browse the full\narchive': "Parcourir l'archive\ncomplète",
    'Drawn by our volunteers': 'Dessiné par nos bénévoles',
    'Floors people walked on': 'Des sols que l’on a foulés',
    'From Mystery to History': "Du mystère à l'histoire",
    'Open your saved objects': 'Ouvrir vos objets enregistrés',
    'Water, carried and kept': 'L’eau, portée et gardée',
    'Architecture and ruins': 'Architecture et ruines',
    'Assorted Succulent Pot': 'Pot de plantes grasses variées',
    'Back to the collection': 'Retour à la collection',
    'Bird and Floral Mosaic': 'Mosaïque aux oiseaux et aux fleurs',
    'Fluted Column Fragment': 'Fragment de colonne cannelée',
    'Headless Draped Statue': 'Statue drapée sans tête',
    'ImmerseGT participants': 'Participants à ImmerseGT',
    'Podcast · July 2, 2026': 'Podcast · 2 juillet 2026',
    'Sidi Bou Said, Tunisia': 'Sidi Bou Saïd, Tunisie',
    'Standing Draped Statue': 'Statue drapée debout',
    'Start the conversation': 'Lancez la conversation',
    'The Kyoto Retreat 2026': 'La retraite de Kyoto 2026',
    'The people of Carthage': 'Les habitants de Carthage',
    'View this object in 3D': 'Voir cet objet en 3D',
    'Water Temple, Zaghouan': 'Temple des Eaux, Zaghouan',
    'AWE USA 2026, Speaker': 'AWE USA 2026, intervenante',
    'Enter the galleries ↓': 'Entrer dans les salles ↓',
    'Mini history lesson 3': 'Mini leçon d’histoire 3',
    'Objects and artifacts': 'Objets et artefacts',
    'Roman, 2nd century CE': 'Romain, IIe siècle de notre ère',
    'Where to find us next': 'Où nous retrouver bientôt',
    'April 10 to 12, 2026': 'Du 10 au 12 avril 2026',
    'Arch, fourth pattern': 'Arche, quatrième motif',
    'Arch, second pattern': 'Arc, deuxième motif',
    'Events & conferences': 'Événements et conférences',
    'Open the full record': 'Ouvrir la fiche complète',
    'Paper · دارجة تونسية': 'Article · دارجة تونسية',
    'Research and Writing': 'Recherche et rédaction',
    'See it in your space': 'Voyez-le chez vous',
    'Thursday, October 22': 'Jeudi 22 octobre',
    'Zawiya of Sidi Sahbi': 'Zaouïa de Sidi Sahbi',
    'Arch, first pattern': 'Arche, premier motif',
    'Arch, third pattern': 'Arc, troisième motif',
    'Medina of Tunis (7)': 'Médina de Tunis (7)',
    'Rooms of the museum': 'Les salles du musée',
    'Share my collection': 'Partager ma collection',
    'Share to protect it': 'Partagez pour le protéger',
    'Tilework Wall Panel': 'Panneau mural en carreaux de faïence',
    '7th century onward': 'À partir du VIIe siècle',
    '8th century onward': 'À partir du VIIIe siècle',
    'How these are made': 'Comment tout cela est fabriqué',
    'Lamps and lanterns': 'Lampes et lanternes',
    'Partnership · 2026': 'Partenariat · 2026',
    'Scanned in Tunisia': 'Numérisé en Tunisie',
    'Stained glass lamp': 'Lampe en vitrail',
    'Where prayer faces': 'Là où la prière se tourne',
    'Words cut in stone': 'Des mots gravés dans la pierre',
    'Browse every scan': 'Parcourir toutes les numérisations',
    'Everyday heritage': 'Le patrimoine du quotidien',
    'Exhibition · 2026': 'Exposition · 2026',
    'Male Torso Statue': 'Statue de torse masculin',
    'Preservation scan': 'Numérisation de préservation',
    'Roman Column Base': 'Base de colonne romaine',
    'Volunteer with us': 'Devenez bénévole',
    'by Claire Natanek': 'par Claire Natanek',
    '›&nbsp; Thank you': '›  Merci',
    'At-risk heritage': 'Patrimoine en danger',
    'Illustrations by': 'Illustrations de',
    'New Site (Flood)': 'Nouveau site (inondation)',
    'Podcasts & video': 'Podcasts et vidéos',
    'Save the picture': 'Enregistrer l’image',
    'Talk · June 2026': 'Conférence · juin 2026',
    'The building kit': 'Le kit de construction',
    '· August 6, 2026': '· 6 août 2026',
    'El Jem, Tunisia': 'El Jem, Tunisie',
    'Medina of Tunis': 'Médina de Tunis',
    'Paper · English': 'Article · anglais',
    'Previous object': 'Objet précédent',
    'Read this aloud': 'Lire à voix haute',
    'Your collection': 'Votre collection',
    'you can edit it': 'vous pouvez le modifier',
    '›&nbsp; Contact': '›  Contact',
    'Carved ceiling': 'Plafond sculpté',
    'Furnished room': 'Pièce meublée',
    'Large clay pot': 'Grand pot en terre cuite',
    'Read the paper': 'Lire l’article',
    'Talks & events': 'Conférences et événements',
    'XR Development': 'Développement XR',
    '3D Generalist': 'Généraliste 3D',
    'Community art': 'Art de la communauté',
    'Explore in 3D': 'Explorer en 3D',
    'Lamps (Unlit)': 'Lampes (éteintes)',
    'Small details': 'Petits détails',
    'Years covered': 'Années couvertes',
    'Badge earned': 'Badge obtenu',
    'Curved bench': 'Banc courbé',
    'From the sea': 'Venu de la mer',
    'Optimized by': 'Optimisé par',
    'Tell me more': 'En savoir plus',
    'XR Developer': 'Développeur XR',
    'August 2026': 'Août 2026',
    'Fill in the': 'Remplissez le',
    'How to scan': 'Comment numériser',
    'Lamps (Lit)': 'Lampes (allumées)',
    'Open to all': 'Ouvert à tous',
    'Ottoman era': 'Époque ottomane',
    'Wall, solid': 'Mur, plein',
    'Write to us': 'Écrivez-nous',
    '11 objects': '11 objets',
    '28 objects': '28 objets',
    'Contact us': 'Nous contacter',
    'March 2026': 'Mars 2026',
    'Share this': 'Partager',
    '3 objects': '3 objets',
    '5 objects': '5 objets',
    '7 objects': '7 objets',
    '8 objects': '8 objets',
    'Clay lamp': 'Lampe en terre cuite',
    'Copy link': 'Copier le lien',
    'Our story': 'Notre histoire',
    'Palm tree': 'Palmier',
    'Small pot': 'Petit pot',
    'Wall lamp': 'Lampe murale',
    'HALL III': 'SALLE III',
    'Share it': 'Partagez-le',
    'HALL IV': 'SALLE IV',
    'Got it': 'Compris',
    'HALL V': 'SALLE V',
    'Next →': 'Suivant →',

    # ---- added 2026-09-21: pages that were still English ----
    'Our paper on digital documentation, XR and citizen science for community-led heritage preservation, presented at the El Jem conference and published here in English, French and Tunisian Arabic.':
        'Notre article sur la documentation numérique, la XR et la science citoyenne pour une préservation du patrimoine menée par les communautés, présenté à la conférence d’El Jem et publié ici en anglais, en français et en arabe tunisien.',
    'Sponsor a community scanning and site clean-up day with local volunteers, covering travel, meals and shared equipment, and start compensating local contributors for their time.':
        'Parrainez une journée communautaire de numérisation et de nettoyage d’un site avec des bénévoles locaux, en couvrant les déplacements, les repas et le matériel partagé, et commencez à rémunérer les contributeurs locaux pour leur temps.',
    'Nathan Bowser interviewed Ines Said for Niantic Spatial about Tanit XR and the Scaniverse capture of the amphitheatre of El Jem; Niantic published the video on its channels.':
        'Nathan Bowser a interviewé Ines Said pour Niantic Spatial au sujet de Tanit XR et de la capture Scaniverse de l’amphithéâtre d’El Jem ; Niantic a publié la vidéo sur ses canaux.',
    'Tanit XR was a finalist in the Best Societal Impact category at Augmented World Expo USA 2026, the XR industry&#x27;s main awards, selected by public vote and expert review.':
        'Tanit XR a été finaliste dans la catégorie du meilleur impact sociétal à l’Augmented World Expo USA 2026, les principaux prix du secteur XR, à l’issue d’un vote du public et d’un examen par des experts.',
    'Nura, a guide character modeled in Blender, walks with you and tells the story behind each object. Her narrated tour, “Before It’s Gone,” is being written now.':
        'Nura, un personnage guide modélisé dans Blender, marche avec vous et raconte l’histoire de chaque objet. Sa visite commentée, « Before It’s Gone », est en cours d’écriture.',
    'This finely preserved doorway combines a heavy wooden door framed by intricate glazed tilework, characteristic of Tunisian Islamic architectural decoration.':
        'Ce portail finement conservé associe une lourde porte en bois encadrée de carreaux de faïence aux motifs complexes, caractéristiques du décor architectural islamique tunisien.',
    'We sponsored a heritage track and a $300 prize at Georgia Tech&#x27;s XR hackathon, and Dr. Caroline Nickerson led a workshop on citizen science and XR.':
        'Nous avons sponsorisé une piste patrimoine et un prix de 300 $ au hackathon XR de Georgia Tech, et la Dre Caroline Nickerson a animé un atelier sur la science citoyenne et la XR.',
    'Tell us what draws you to this cohort and what you hope to gain from it. We are interested in your motivation and curiosity, not perfection.':
        'Dites-nous ce qui vous attire dans cette promotion et ce que vous espérez en retirer. Ce qui nous intéresse, c’est votre motivation et votre curiosité, pas la perfection.',
    'Romans of Byrsa Hill and the villas, carved in marble. Most lost a head or an arm on the way to us, and they are still unmistakably people':
        'Des Romains de la colline de Byrsa et des villas, taillés dans le marbre. La plupart ont perdu une tête ou un bras en chemin, et ce sont toujours, sans aucun doute, des êtres humains',
    'From the temple over the spring at Zaghouan, water travelled ninety kilometres to Carthage. These basins and wells are where it arrived':
        'Depuis le temple au-dessus de la source de Zaghouan, l’eau parcourait quatre-vingt-dix kilomètres jusqu’à Carthage. Ces bassins et ces puits sont son point d’arrivée',
    'Short sessions on the sites and objects we scan, Carthage, the Tophet, the medina of Tunis, so every model comes with its story.':
        'De courtes sessions sur les sites et les objets que nous numérisons, Carthage, le Tophet, la médina de Tunis, pour que chaque modèle arrive avec son histoire.',
    'Whole places rather than single objects: passages under the baths, tiled interiors, and a city the sea gave back for a few days':
        'Des lieux entiers plutôt que des objets isolés : les galeries sous les thermes, des intérieurs en carreaux de faïence, et une ville que la mer a rendue quelques jours',
    'Volunteers scan sites on the ground, optimize models for VR, write articles, and model heritage\nobjects by hand, like these.':
        'Des bénévoles numérisent les sites sur le terrain, optimisent les modèles pour la VR, écrivent des articles et modélisent à la main des objets du\npatrimoine, comme ceux-ci.',
    'Planned for Viverse so it runs cross-platform, in VR, and as a scroll-to-walk version in any browser for classrooms.':
        'Prévu pour Viverse afin de fonctionner sur toutes les plateformes, en VR, et sous forme de version à parcourir au défilement dans n’importe quel navigateur, pour les salles de classe.',
    'Arches, walls, pillars and ceilings: puzzle pieces any volunteer can take and assemble into a gallery of their own':
        'Arcs, murs, piliers et plafonds : des pièces de puzzle que chaque bénévole peut prendre et assembler pour en faire sa propre galerie',
    'Numbers, monthly: visits, objects viewed, people trained, volunteer hours, from the same counter we use ourselves.':
        'Des chiffres, chaque mois : visites, objets consultés, personnes formées, heures de bénévolat, issus du même compteur que celui que nous utilisons.',
    'Stories your communications team can use: volunteers, sites, a storm, a rescue, with pictures we take ourselves.':
        'Des histoires que votre équipe communication peut utiliser : des bénévoles, des sites, une tempête, un sauvetage, avec des photos que nous prenons nous-mêmes.',
    'Photogrammetry records of statues, mosaics, stelae and ruins, preservation quality, with game-ready twins.':
        'Des relevés photogrammétriques de statues, mosaïques, stèles et ruines, de qualité conservation, avec des jumeaux prêts pour le jeu.',
    'Mihrabs and niches from mosques, madrasas and a Roman water temple. Each one tells you which way to turn':
        'Des mihrabs et des niches de mosquées, de médersas et d’un temple des eaux romain. Chacun vous indique dans quelle direction vous tourner',
    'Your logo on the site, in the experience and at our events, and a mention in every newsletter edition.':
        'Votre logo sur le site, dans l’expérience et lors de nos événements, ainsi qu’une mention dans chaque numéro de la newsletter.',
    ', places or objects threatened by weather, neglect, development, conflict, theft, or loss of memory':
        ', lieux ou objets menacés par les intempéries, l’abandon, l’urbanisation, les conflits, le vol ou l’oubli',
    'A tax-deductible gift through our fiscal sponsor, Florida Community Innovation, a U.S. 501(c)(3).':
        'Un don déductible des impôts via notre parrain fiscal, Florida Community Innovation, une organisation américaine 501(c)(3).',
    'We speak, exhibit and sponsor: AWE, the El Jem conference, ImmerseGT at Georgia Tech, and more.':
        'Nous intervenons, exposons et sponsorisons : AWE, le colloque d’El Jem, ImmerseGT à Georgia Tech, et bien d’autres.',
    'Whole spaces built by volunteers: the main hall, a furnished room, the plinths and rugs inside':
        'Des espaces entiers construits par des bénévoles : la salle principale, une pièce meublée, les socles et les tapis à l’intérieur',
    'The virtual museum in January 2026: first courtyard and corridor with scanned statues placed':
        'Le musée virtuel en janvier 2026 : première cour et couloir avec les statues numérisées en place',
    'Light the way it falls in a Tunisian home, modelled by volunteers who studied the real ones':
        'La lumière telle qu’elle tombe dans une maison tunisienne, modélisée par des bénévoles qui ont étudié les vraies',
    ', doors, arches, columns, facades, walls, courtyards, tombs, monuments, and historic homes':
        ', portes, arcs, colonnes, façades, murs, cours, tombeaux, monuments et maisons historiques',
    'Digital documentation, XR and citizen science for community-driven heritage preservation.':
        'Documentation numérique, XR et science citoyenne au service d’une préservation du patrimoine portée par les communautés.',
    'Employees who learned something real and can show their families what they helped keep.':
        'Des salariés qui ont appris quelque chose de concret et peuvent montrer à leurs proches ce qu’ils ont contribué à sauvegarder.',
    'Tell us what you like doing, scanning, 3D, writing, design, research, teaching.':
        'Dites-nous ce que vous aimez faire, la numérisation, la 3D, l’écriture, le design, la recherche, l’enseignement.',
    'Processing uses a lot of data, it’s best to wait until you’re home with Wi-Fi.':
        'Le traitement consomme beaucoup de données, mieux vaut attendre d’être chez vous avec le Wi-Fi.',
    'Natural daylight is good, but harsh sun causes glare, avoid scanning at noon':
        'La lumière naturelle est idéale, mais le soleil dur crée des reflets, évitez de numériser à midi',
    'Anything that might help us better understand you or your availability.':
        'Tout ce qui peut nous aider à mieux vous connaître ou à comprendre vos disponibilités.',
    'XR Women Museum, two exhibitions in FrameVR, curated by Paige Dansinger':
        'XR Women Museum, deux expositions dans FrameVR, sous le commissariat de Paige Dansinger',
    'ImmerseGT 2026, Sponsored track at Georgia Tech&#x27;s XR hackathon':
        'ImmerseGT 2026, piste sponsorisée au hackathon XR de Georgia Tech',
    'First courtyard and corridor blocked out; scanned statues placed.':
        'Première cour et couloir esquissés ; statues numérisées mises en place.',
    'Who we are, what we do, how to help, one page in three languages.':
        'Qui nous sommes, ce que nous faisons, comment aider, une page en trois langues.',
    'Storm Harry, Neapolis, and a Digital Moment of Preservation':
        'La tempête Harry, Neapolis, et un moment numérique de sauvegarde',
    'Tilework Wall Panel – Mausoleum of Sidi Sahbi, Kairouan':
        'Panneau mural en carreaux de faïence – mausolée de Sidi Sahbi, Kairouan',
    'While you wait, the weekly opportunity digest is free:':
        'En attendant, le récapitulatif hebdomadaire des opportunités est gratuit :',
    'Niantic Spatial, video interview with Nathan Bowser':
        'Niantic Spatial, entretien vidéo avec Nathan Bowser',
    '(not “Splat”), this is what we need for Tanit XR.':
        '(et non « Splat »), c’est ce dont nous avons besoin pour Tanit XR.',
    'Standing Draped Statue – Roman Villas of Carthage':
        'Statue drapée debout – villas romaines de Carthage',
    'Drag to look around. Tap anything to get closer.':
        'Faites glisser pour regarder autour de vous. Touchez un élément pour vous en approcher.',
    'Inscribed Architectural Fragment – Byrsa Hill, …':
        'Fragment architectural inscrit – colline de Byrsa, …',
    'XR Women Museum Open Call: Vibrancy as Practice':
        'Appel à projets du XR Women Museum : Vibrancy as Practice',
    'Carved Architectural Blocks with Laurel Motifs':
        'Blocs architecturaux sculptés à motifs de laurier',
    'Passthrough on a headset, camera AR on a phone':
        'Passthrough sur un casque, réalité augmentée par la caméra sur un téléphone',
    'Architectural Fragment with Relief Decoration': 'Fragment architectural à décor en relief',
    'Every object in here was saved by a volunteer': 'Chaque objet ici a été sauvé par un bénévole',
    'Fifteen minutes is enough to see if this fits':
        'Quinze minutes suffisent pour voir si cela vous convient',
    'Ornamental Mihrab (Mahram) – Medersa Slimanya': 'Mihrab ornemental (mahram) – médersa Slimania',
    'I run an organisation. Can we work with you?':
        'Je dirige une organisation. Pouvons-nous travailler avec vous ?',
    'Ornamental Wooden Door with Studded Patterns': 'Porte en bois ornée de motifs cloutés',
    'Neapolis Site Revealed By Floods In Tunisia':
        'Le site de Neapolis révélé par les inondations en Tunisie',
    'Underground Passageways, Baths of Antoninus': 'Galeries souterraines, thermes d’Antonin',
    'A talk, a workshop or a room at your event':
        'Une conférence, un atelier ou une salle lors de votre événement',
    'Statue Fragment – Roman Villas of Carthage': 'Fragment de statue – villas romaines de Carthage',
    'Walk through Tunisia, one object at a time': 'Parcourez la Tunisie, un objet à la fois',
    'Architectural Fragments with Inscriptions': 'Fragments architecturaux avec inscriptions',
    'Punic Stela, Tophet of Salammbo, Carthage': 'Stèle punique, tophet de Salammbô, Carthage',
    'Tanit Stela, Tophet of Salammbo, Carthage': 'Stèle de Tanit, Tophet de Salammbô, Carthage',
    'Bir (Traditional Well) – Medina of Tunis': 'Bir (puits traditionnel) – médina de Tunis',
    'Roman Column Base – Byrsa Hill, Carthage':
        'Base de colonne romaine – colline de Byrsa, Carthage',
    'El Jem Conference, our paper presented': 'Colloque d’El Jem, notre communication présentée',
    'Roman Mosaic with Bird and Vine Motifs': 'Mosaïque romaine à motifs d’oiseaux et de vigne',
    'Tiled corridor with a scanned artifact': 'Couloir carrelé avec un objet numérisé',
    'Build an immersive experience with us': 'Créez une expérience immersive avec nous',
    'Draped Statue – Byrsa Hill, Carthage': 'Statue drapée – colline de Byrsa, Carthage',
    'Stone Basin – Water Temple, Zaghouan': 'Bassin en pierre – temple des Eaux, Zaghouan',
    'Neapolis Site Revealed By Floods In': 'Site de Neapolis révélé par les inondations',
    'Niche Wall – Water Temple, Zaghouan': 'Mur à niches – Temple des Eaux, Zaghouan',
    'Traditional Door – Medina of Tunis': 'Porte traditionnelle – médina de Tunis',
    'Wooden Door – Zawiya of Sidi Sahib': 'Porte en bois – Zaouïa de Sidi Sahib',
    'Example: EST, GMT+1, Tunisia time': 'Exemple : EST, GMT+1, heure de Tunisie',
    'Splats With Phones cohort session': 'Séance du groupe Splats With Phones',
    'Roman Togatus Statue, Byrsa Hill': 'Statue romaine en toge, colline de Byrsa',
    'Scanned Roman statue in a niche': 'Statue romaine numérisée dans une niche',
    'Corinthian Capital, Byrsa Hill': 'Chapiteau corinthien, colline de Byrsa',
    'For companies and foundations': 'Pour les entreprises et les fondations',
    'Ornate Tunisian Hanging Lamp': 'Lampe suspendue tunisienne ouvragée',
    'Tophet of Salammbo, Carthage': 'Tophet de Salammbô, Carthage',
    'Scaniverse scanning example': 'Exemple de numérisation avec Scaniverse',
    'Virtual Museum, in progress': 'Musée virtuel, en cours',
    'Your message is on its way.': 'Votre message est en route.',
    'Watch the post on LinkedIn': 'Voir la publication sur LinkedIn',
    'subscribe to Opportunities': 's’abonner aux Opportunités',
    'Courtyard fountain, small': 'Fontaine de cour, petite',
    'Event · April 10–12, 2026': 'Événement · 10–12 avril 2026',
    'Marble Calligraphic Panel': 'Panneau calligraphique en marbre',
    'Nura has something to say': 'Nura a quelque chose à vous dire',
    'Virtual Museum – TANIT XR': 'Musée virtuel – TANIT XR',
    'Wooden Door with Tilework': 'Porte en bois avec carreaux de faïence',
    'Browse with descriptions': 'Parcourir avec les descriptions',
    'One-pager (EN / FR / AR)': 'Fiche d’une page (EN / FR / AR)',
    'Pots, plants and gardens': 'Poteries, plantes et jardins',
    'What do I get out of it?': 'Qu’est-ce que j’y gagne ?',
    'Decorated Bust Fragment': 'Fragment de buste décoré',
    'El Jem Conference paper': 'Communication au colloque d’El Jem',
    'Read the scanning guide': 'Lire le guide de numérisation',
    'Bir (Traditional Well)': 'Bir (puits traditionnel)',
    'Email info@tanitxr.org': 'Écrivez à info@tanitxr.org',
    'Latin Inscription Slab': 'Dalle à inscription latine',
    'See how a scan is made': 'Voyez comment se fait une numérisation',
    'Stones raised to Tanit': 'Des pierres dressées à Tanit',
    "The museum's main hall": 'La salle principale du musée',
    'Walk around it, slowly': 'Faites-en le tour, lentement',
    'Where this was scanned': 'Où cet objet a été numérisé',
    'Always get permission': 'Demandez toujours l’autorisation',
    'What held the roof up': 'Ce qui soutenait le toit',
    'A purple murex shell': 'Un coquillage de murex pourpre',
    'Community – TANIT XR': 'Communauté – TANIT XR',
    'Galleries – TANIT XR': 'Galeries – TANIT XR',
    'Roman Togatus Statue': 'Statue romaine de togatus',
    'Thank you – TANIT XR': 'Merci – TANIT XR',
    'Bird of Prey Statue': 'Statue d’oiseau de proie',
    'Roman Draped Statue': 'Statue romaine drapée',
    'Tanit XR volunteers': 'Les bénévoles de Tanit XR',
    'Baths of Antoninus': 'Thermes d’Antonin',
    'Doors still in use': 'Des portes toujours en usage',
    'Paper · April 2026': 'Article · Avril 2026',
    'Rooms and passages': 'Salles et passages',
    'Tanit XR Galleries': 'Galeries Tanit XR',
    'Where we have been': 'Où nous sommes allés',
    'Award · June 2026': 'Prix · Juin 2026',
    'Kitchen and table': 'Cuisine et table',
    'Map of everything': 'Carte de l’ensemble',
    'What you get back': 'Ce que vous y gagnez',
    '· August 18, 2026': '· 18 août 2026',
    'Explore it in 3D': 'Explorez-le en 3D',
    'Paper · Français': 'Article · Français',
    'Punic Stelae Row': 'Rangée de stèles puniques',
    'by Alyssa George': 'par Alyssa George',
    'Everyday things': 'Objets du quotidien',
    'Punic and Roman': 'Punique et romain',
    'See her profile': 'Voir son profil',
    '· July 31, 2026': '· 31 juillet 2026',
    'Display plinth': 'Socle d’exposition',
    'How do I join?': 'Comment participer ?',
    'Member profile': 'Profil du membre',
    'See their room': 'Voir leur salle',
    'volunteer form': 'formulaire de bénévolat',
    'Object viewer': 'Visionneuse d’objet',
    'Their profile': 'Leur profil',
    'Drag to turn': 'Faites glisser pour tourner',
    'January 2026': 'Janvier 2026',
    'Scanned here': 'Numérisé ici',
    'Video · 2026': 'Vidéo · 2026',
    '🎮 Game-ready': '🎮 Prêt pour le jeu',
    'Is it paid?': 'Est-ce rémunéré ?',
    'Next object': 'Objet suivant',
    'What we did': 'Ce que nous avons fait',
    'XR Creators': 'Créateurs XR',
    'April 2026': 'Avril 2026',
    'GAME READY': 'OPTIMISÉ POUR LE JEU',
    'XR Advisor': 'Conseiller XR',
    '← Previous': '← Précédent',
    '2 objects': '2 objets',
    '4 objects': '4 objets',
    'Back home': 'Retour à l’accueil',
    'Coming up': 'À venir',
    'Read more': 'En savoir plus',
    'Thank you': 'Merci',
    '1 object': '1 objet',
    'HALL II': 'SALLE II',
    'HALL I': 'SALLE I',

    # ---- added 2026-09-21: pages that were still English ----
    'Tanit XR is run entirely by volunteers. So far most costs, travel to\nsites, tools, hosting, hackathon prizes, have been paid out of pocket by our founders, plus a few individual donations\nthrough our fiscal sponsor, the Florida Community Innovation Foundation (a US 501(c)(3), so donations are tax-deductible).\nWe are applying for grants and building partnerships to change that. Donations keep the community running: hosting,\nvolunteer hours, optimizing and publishing models, the virtual museum, scanning and site clean-up days, our free course\nand workshops, and better equipment. Here is what a donation does:':
        'Tanit XR fonctionne entièrement grâce à des bénévoles. Jusqu’ici, la plupart des frais, les déplacements vers les sites, les outils, l’hébergement, les prix du hackathon, ont été payés de leur poche par nos fondateurs, avec quelques dons de particuliers passés par notre parrain fiscal, la Florida Community Innovation Foundation (une organisation américaine 501(c)(3), les dons sont donc déductibles des impôts). Nous demandons des subventions et construisons des partenariats pour que cela change. Les dons font vivre la communauté : hébergement, heures de bénévolat, optimisation et publication des modèles, musée virtuel, journées de numérisation et de nettoyage des sites, notre cours gratuit et nos ateliers, et du meilleur matériel. Voici ce que fait un don :',
    'Phoenician settlers founded Carthage and it grew into the capital of an empire that ran the western Mediterranean. Rome destroyed it in 146 BCE, then rebuilt it as the capital of Roman Africa. What stands today is layered. Punic stelae raised to Tanit and Baal Hammon sit a short walk from Roman columns, villa mosaics and the largest bath complex Rome built in Africa. Our volunteers scanned across four areas of the site.':
        'Des colons phéniciens ont fondé Carthage, qui est devenue la capitale d’un empire maîtrisant la Méditerranée occidentale. Rome l’a détruite en 146 av. J.-C., puis l’a rebâtie comme capitale de l’Afrique romaine. Ce qui subsiste aujourd’hui est fait de couches. Des stèles puniques dressées à Tanit et Baal Hammon se trouvent à quelques pas de colonnes romaines, de mosaïques de villas et du plus grand complexe de thermes que Rome ait bâti en Afrique. Nos bénévoles ont numérisé quatre zones du site.',
    'The Holy Art Gallery’s “Not Your Grandma’s Gallery” is an ongoing open call series for artists worldwide, positioned as high-energy, contemporary exhibitions across different cities. Listings typically note exhibition dates and a deadline to apply that may be marked as TBC depending on the edition. Check the current call page/post for the specific city, exhibition dates, and the latest submission deadline.':
        '« Not Your Grandma’s Gallery » de la Holy Art Gallery est une série d’appels à candidatures ouverte aux artistes du monde entier, pensée comme des expositions contemporaines et pleines d’énergie dans différentes villes. Les annonces indiquent en général les dates d’exposition et une date limite de candidature parfois notée « à confirmer » selon l’édition. Consultez la page ou la publication de l’appel en cours pour connaître la ville, les dates d’exposition et la date limite la plus récente.',
    'In early 2026 Storm Harry stripped sand off the seabed near Nabeul and exposed part of Neapolis, a Punic and later Roman city that collapsed into the sea after a tsunami in the 4th century CE. Stone blocks and wall lines were visible for a few days before the sediment returned. Tanit XR captured the newly exposed area inside that window. This hall holds one object, and it is the reason we work quickly.':
        'Début 2026, la tempête Harry a arraché le sable du fond marin près de Nabeul et mis au jour une partie de Neapolis, une cité punique puis romaine engloutie par un tsunami au IVe siècle de notre ère. Des blocs de pierre et des lignes de murs sont restés visibles quelques jours avant le retour des sédiments. Tanit XR a documenté la zone dégagée pendant cette fenêtre. Cette salle ne contient qu’un seul objet, et c’est la raison pour laquelle nous travaillons vite.',
    "Tanit XR is eighty-five volunteers on four continents who bring Tunisia's endangered heritage\ninto 3D and publish it free, for anyone, working alongside the institutions that look after the sites. Everything on\nthis site was built without a single paid person. A partnership pays for the museum, the experiences, the training and\nthe care of the places, and gives your team a real part in it.":
        'Tanit XR, ce sont quatre-vingt-cinq bénévoles sur quatre continents qui font passer le patrimoine tunisien en danger en 3D et le publient gratuitement, pour tout le monde, en travaillant aux côtés des institutions qui veillent sur les sites. Tout ce qui se trouve sur ce site a été construit sans une seule personne rémunérée. Un partenariat finance le musée, les expériences, la formation et l’entretien des lieux, et donne à votre équipe une vraie place dans tout cela.',
    'Under Hadrian, Rome built a temple around a mountain spring at Zaghouan. From here an aqueduct carried water more than 90 kilometres to Carthage, one of the longest in the Roman world. The temple is the monumental head of that system. Niches once held statues of water deities, laurel friezes ran along the cornices, and a Latin slab recorded who paid for it.':
        'Sous Hadrien, Rome a bâti un temple autour d’une source de montagne à Zaghouan. De là, un aqueduc portait l’eau sur plus de 90 kilomètres jusqu’à Carthage, l’un des plus longs du monde romain. Le temple est la tête monumentale de ce système. Des niches abritaient autrefois des statues de divinités des eaux, des frises de laurier couraient le long des corniches, et une dalle latine gardait la mémoire de ceux qui l’avaient financé.',
    'The first community-led virtual museum of Tunisian heritage. Every artifact inside was\nscanned in Tunisia by our volunteers and optimized by volunteers around the world; the rooms are modeled by hand so\nanyone in the community can build a new one. Built in Unity with photogrammetry and Gaussian splats. Still in\nprogress, this is what it looks like today.':
        'Le premier musée virtuel du patrimoine tunisien porté par une communauté. Chaque objet à l’intérieur a été numérisé en Tunisie par nos bénévoles et optimisé par des bénévoles partout dans le monde ; les salles sont modélisées à la main pour que n’importe qui dans la communauté puisse en construire une nouvelle. Réalisé avec Unity, en photogrammétrie et en splats gaussiens. Toujours en chantier, voici à quoi il ressemble aujourd’hui.',
    'The medina grew around the Zitouna Mosque and became one of the great cities of the Islamic world under the Almohads and the Hafsids. It is not a ruin. People live and work here now. These scans are doors, wells, looms and prayer niches recorded in streets that are still in daily use, including the Madrasa Al Bachia of 1752 and the Medersa Slimanya.':
        'La médina s’est développée autour de la mosquée Zitouna et est devenue l’une des grandes villes du monde islamique sous les Almohades et les Hafsides. Ce n’est pas une ruine. Des gens y vivent et y travaillent aujourd’hui. Ces numérisations sont des portes, des puits, des métiers à tisser et des niches de prière enregistrés dans des rues encore utilisées tous les jours, dont la Madrasa Al Bachia de 1752 et la Medersa Slimanya.',
    'Tanit XR is volunteers in Tunisia, the United States, Europe and Nigeria who meet\nevery week. We scan on the ground and optimize remotely, learn the history behind every object, run workshops,\nmentor students, attend events together, and share Tunisian culture with people who had never heard of Carthage.\nEverything we make is free and open.':
        'Tanit XR, ce sont des bénévoles en Tunisie, aux États-Unis, en Europe et au Nigéria qui se retrouvent chaque semaine. Nous numérisons sur le terrain et optimisons à distance, nous apprenons l’histoire derrière chaque objet, nous animons des ateliers, accompagnons des étudiants, participons à des événements ensemble et faisons connaître la culture tunisienne à des gens qui n’avaient jamais entendu parler de Carthage. Tout ce que nous faisons est gratuit et ouvert.',
    "A donation goes straight into the work: a volunteer's bus fare and mobile data for a day of scanning, a\nmonth of hosting for the free archive, a workshop that teaches someone in Tunisia to capture their own\nheritage, and one day a proper scanner so the community can record more than a phone allows. Here is what\neach amount does.":
        'Un don va directement au travail : le ticket de bus et les données mobiles d’un bénévole pour une journée de numérisation, un mois d’hébergement pour l’archive gratuite, un atelier qui apprend à quelqu’un en Tunisie à documenter son propre patrimoine, et un jour un vrai scanner pour que la communauté puisse enregistrer plus que ce que permet un téléphone. Voici ce que fait chaque montant.',
    'Mostly on Slack, across four continents and as many time zones. Once a week we meet on a call, Thursdays at 12 pm Eastern, 5 pm in Tunisia, to look at new scans, learn the history behind them and help each other with whatever is stuck. Julia records a short history lesson each week for anyone who cannot make it.':
        'Surtout sur Slack, sur quatre continents et autant de fuseaux horaires. Une fois par semaine, nous nous retrouvons en visio, le jeudi à midi heure de l’Est, 17 h en Tunisie, pour regarder les nouvelles numérisations, apprendre l’histoire qui va avec et s’entraider sur ce qui bloque. Julia enregistre chaque semaine une courte leçon d’histoire pour celles et ceux qui ne peuvent pas venir.',
    'Skills-based volunteering with a clear task: optimise a scan for the web, research an object&#x27;s history, translate a label into French or Arabic, build a piece of the virtual museum. Half a day or a season, online, with a volunteer of ours alongside. Everything your team makes is published under their names.':
        'Du bénévolat de compétences avec une tâche claire : optimiser une numérisation pour le web, faire des recherches sur l’histoire d’un objet, traduire une notice en français ou en arabe, construire une partie du musée virtuel. Une demi-journée ou une saison, en ligne, avec l’un de nos bénévoles à vos côtés. Tout ce que votre équipe produit est publié à son nom.',
    'Your work is credited to you, on your own page here and on every model you touch. You learn photogrammetry, 3D and XR by doing them on real heritage. Students get portfolio reviews, mock interviews and mentoring from people working in the field. And you become part of a community that genuinely likes each other.':
        'Votre travail est crédité à votre nom, sur votre propre page ici et sur chaque modèle que vous touchez. Vous apprenez la photogrammétrie, la 3D et le XR en les pratiquant sur du vrai patrimoine. Les étudiants bénéficient de relectures de portfolio, d’entretiens blancs et du mentorat de personnes qui travaillent dans le domaine. Et vous entrez dans une communauté dont les membres s’apprécient vraiment.',
    "Every object our volunteers have scanned in Tunisia, one at a\ntime, in 3D, in your browser. Turn each one with a finger. Nura, our guide, floats beside you and\ntells you what you are looking at. Save the ones you love, share them, collect badges, step into\neach maker's own gallery, or put on a headset.":
        'Chaque objet que nos bénévoles ont numérisé en Tunisie, un par un, en 3D, dans votre navigateur. Faites-le tourner du doigt. Nura, notre guide, flotte à côté de vous et vous raconte ce que vous regardez. Gardez ceux que vous aimez, partagez-les, collectionnez des badges, entrez dans la galerie de chaque créateur, ou mettez un casque.',
    "No. Our first scans were made with a phone by someone who had never scanned anything. People here write, design, research, teach, translate, organise trips, model objects, clean up scans, apply for grants and run our social media. If you are curious about Tunisia's history, there is a place for you.":
        'Non. Nos premières numérisations ont été faites au téléphone par quelqu’un qui n’avait jamais rien numérisé. Ici, des gens écrivent, conçoivent, font des recherches, enseignent, traduisent, organisent des sorties, modélisent des objets, nettoient des numérisations, déposent des demandes de subvention et animent nos réseaux sociaux. Si l’histoire de la Tunisie vous intrigue, il y a une place pour vous.',
    'Not yet. Everyone at Tanit XR is a volunteer, including the founders, and most costs so far have come out of our own pockets. We will never ask volunteers to work so that someone else earns; when funding arrives, the first people we want to pay are the volunteers on the ground in Tunisia.':
        'Pas encore. Tout le monde à Tanit XR est bénévole, y compris les fondateurs, et la plupart des frais sont jusqu’ici sortis de nos propres poches. Nous ne demanderons jamais à des bénévoles de travailler pour que quelqu’un d’autre gagne de l’argent ; quand des financements arriveront, les premières personnes que nous voulons payer sont les bénévoles sur le terrain en Tunisie.',
    'This intricately designed niche is part of the Roman Water Temple in Zaghouan, constructed during the reign of Emperor Hadrian in the 2nd century CE. The temple marked the starting point of the massive aqueduct that carried fresh water over 90 kilometers to the city of Carthage.':
        'Cette niche finement travaillée fait partie du Temple des Eaux romain de Zaghouan, construit sous le règne de l’empereur Hadrien au IIe siècle de notre ère. Le temple marquait le point de départ de l’immense aqueduc qui portait l’eau douce sur plus de 90 kilomètres jusqu’à la ville de Carthage.',
    'Our heritage challenge ran at the official Major League Hacking hack day hosted by Florida Community Innovation at the University of Florida, with two tracks: build an interactive experience from one of our real 3D scans, or make a public history piece with no code needed.':
        'Notre défi patrimoine s’est tenu lors du hack day officiel de la Major League Hacking organisé par Florida Community Innovation à l’University of Florida, avec deux parcours : construire une expérience interactive à partir de l’une de nos vraies numérisations 3D, ou réaliser un projet d’histoire publique sans écrire une ligne de code.',
    'Alyssa George, illustrator and designer from the University of South Florida, draws\nthe Tanit XR story: an amphora heading to class, volunteers on every continent, the Draped Statue of Byrsa Hill\nappearing on a phone, and the murex shell that gave Carthage its purple.':
        'Alyssa George, illustratrice et designer de l’University of South Florida, dessine l’histoire de Tanit XR : une amphore qui part en cours, des bénévoles sur tous les continents, la Statue drapée de la colline de Byrsa qui apparaît sur un téléphone, et le coquillage murex qui a donné à Carthage sa pourpre.',
    'As much as you can give. Tasks are small and self-contained: one scan to clean up, one object to research, one article to write. Some people come to the Thursday call every week, some appear once a month. You set the pace and you can pause whenever life gets busy.':
        'Autant que vous pouvez donner. Les tâches sont petites et autonomes : une numérisation à nettoyer, un objet à documenter, un article à écrire. Certaines personnes viennent à l’appel du jeudi chaque semaine, d’autres apparaissent une fois par mois. Vous fixez le rythme et vous pouvez faire une pause dès que la vie devient chargée.',
    'Our founder and team speak on community XR, phone 3D capture and heritage at risk: AWE, Voices of VR, Georgia Tech, the El Jem conference. Or we bring the 3D experience and a headset to your conference or office, with a volunteer to guide people through it.':
        'Notre fondatrice et notre équipe interviennent sur le XR communautaire, la capture 3D au téléphone et le patrimoine en danger : AWE, Voices of VR, Georgia Tech, la conférence d’El Jem. Ou nous apportons l’expérience 3D et un casque à votre conférence ou à votre bureau, avec un bénévole pour guider les gens.',
    'Open call presented by the XR Women Museum inviting submissions around the theme “Vibrancy as Practice.” Submit via the official form linked from the call announcement. Check the external link for the most current submission requirements and timeline.':
        'Appel à candidatures lancé par le XR Women Museum autour du thème « Vibrancy as Practice ». Les envois se font via le formulaire officiel indiqué dans l’annonce de l’appel. Consultez le lien externe pour connaître les conditions et le calendrier les plus à jour.',
    "Tanit XR is run entirely by volunteers. Nobody is paid, and most of what you see here, the scanning\ntrips, the tools, the hosting, the hackathon prizes, has so far been paid out of our founders' own pockets.\nThat cannot last, and it should not.":
        'Tanit XR fonctionne entièrement grâce à des bénévoles. Personne n’est payé, et la plus grande partie de ce que vous voyez ici, les sorties de numérisation, les outils, l’hébergement, les prix du hackathon, a jusqu’ici été payée par nos fondateurs de leur propre poche. Cela ne peut pas durer, et cela ne devrait pas durer.',
    'That is honestly most of it. Walk a full circle around the object with your phone, then\nanother circle a little higher, then one lower, so every photo overlaps the last. We use\nScaniverse, which is free. Nura is showing you the path right now.':
        'C’est franchement l’essentiel. Faites un tour complet autour de l’objet avec votre téléphone, puis un autre un peu plus haut, puis un autre plus bas, pour que chaque photo chevauche la précédente. Nous utilisons Scaniverse, qui est gratuit. Nura vous montre le chemin en ce moment même.',
    'Tanit XR is powered by volunteers: 3D scanning, model cleanup, XR development, historical research, writing, translation, and storytelling. Join from Tunisia or anywhere in the world, all experience levels welcome, fully remote friendly.':
        'Tanit XR fonctionne grâce à des bénévoles : numérisation 3D, nettoyage de modèles, développement XR, recherche historique, rédaction, traduction et récit. Rejoignez-nous depuis la Tunisie ou de n’importe où dans le monde, tous les niveaux d’expérience sont les bienvenus, et tout peut se faire à distance.',
    'Global network connecting youth-led organizations working on climate action, education, heritage, science, and communication. Members collaborate, access capacity-building, share knowledge, and participate in UNESCO climate initiatives.':
        'Réseau mondial qui relie des organisations dirigées par des jeunes et travaillant sur le climat, l’éducation, le patrimoine, la science et la communication. Les membres collaborent, accèdent à des formations, partagent leurs connaissances et participent aux initiatives climat de l’UNESCO.',
    'With the authorities who look after the sites, a day of cleaning and care at a coastal site with local volunteers: travel, meals, gloves and bags, and a modest fee for the locals who show up. The sea is the clock we work against.':
        'Avec les autorités qui veillent sur les sites, une journée de nettoyage et d’entretien sur un site côtier avec des bénévoles locaux : déplacement, repas, gants et sacs, et une petite indemnité pour les habitants qui viennent. La mer est l’horloge contre laquelle nous travaillons.',
    'A free, growing library of 3D scans of Tunisia’s endangered\nheritage, mosaics, statues, stelae, and ruins captured by our volunteers. Every model can be explored\ninteractively, and viewed in augmented reality on your phone.':
        'Une bibliothèque gratuite et grandissante de numérisations 3D du patrimoine tunisien en danger : mosaïques, statues, stèles et ruines capturées par nos bénévoles. Chaque modèle peut être exploré de façon interactive et vu en réalité augmentée sur votre téléphone.',
    'Al Jazeera&#x27;s culture desk profiled Tanit XR in Arabic: a non-profit building a precise digital library of Tunisia&#x27;s sites and artifacts with photogrammetry and Gaussian splats, before time and neglect erase them.':
        'Le service culture d’Al Jazeera a consacré un portrait à Tanit XR en arabe : une association à but non lucratif qui construit une bibliothèque numérique précise des sites et des objets tunisiens grâce à la photogrammétrie et aux splats gaussiens, avant que le temps et l’abandon ne les effacent.',
    'Tanit XR&#x27;s heritage challenge at the official MLH Hack Day hosted by Florida Community Innovation at the University of Florida: build something usable from our 3D scans, or a public-history project that needs no code.':
        'Le défi patrimoine de Tanit XR lors du Hack Day officiel MLH organisé par Florida Community Innovation à l’University of Florida : construire quelque chose d’utilisable à partir de nos numérisations 3D, ou un projet d’histoire publique qui ne demande aucun code.',
    'By Laura Harrison, Scientific Director, TanitXR. Scientific Director, TanitXR A scruffy brown donkey lowered its eyelids as a merchant filled its wooden cart with stacked bins of corn and melons. We saw several more like…':
        'Par Laura Harrison, directrice scientifique, TanitXR. Directrice scientifique, TanitXR Un âne brun et hirsute a baissé les paupières pendant qu’un marchand remplissait sa charrette en bois de caisses empilées de maïs et de melons. Nous en avons vu plusieurs autres comme…',
    'By: Margarita Johnson The intense light illuminates the plateau of Byrsa Hill in Carthage, and the wind shakes the surviving fragments of an ancient city that once stood as a rival to Rome itself. Corinthian columns rise…':
        'Par : Margarita Johnson La lumière intense éclaire le plateau de la colline de Byrsa à Carthage, et le vent secoue les fragments survivants d’une cité antique qui fut un jour la rivale de Rome elle-même. Des colonnes corinthiennes s’élèvent…',
    'By: Margarita Johnson The new year began with Storm Harry sweeping across Tunisia’s Mediterranean coastline, reshaping the coastline and disturbing layers of sand that had settled undisturbed for centuries. Local observe…':
        'Par : Margarita Johnson La nouvelle année a commencé avec la tempête Harry qui a balayé le littoral méditerranéen de la Tunisie, redessinant la côte et remuant des couches de sable posées là sans bouger depuis des siècles. Des observateurs locaux…',
    'Tanit XR is taking part in CityCamp Gainesville Hack Day on Sunday, September 20, 2026, at the Reitz Union, University of Florida, an official MLH Hack Day hosted by Florida Community Innovation. Our challenge: build som…':
        'Tanit XR participe au CityCamp Gainesville Hack Day le dimanche 20 septembre 2026, au Reitz Union de l’University of Florida, un hack day officiel MLH organisé par Florida Community Innovation. Notre défi : construire quelque…',
    'This is Tanit XR’s very first news article, and it feels right to begin with a story. Growing up among ruins I grew up in Tunisia surrounded by history. Walking past the ruins of Carthage felt ordinary, almost casual. An…':
        'C’est le tout premier article de Tanit XR, et il nous semble juste de commencer par une histoire. Grandir parmi les ruines J’ai grandi en Tunisie entourée d’histoire. Passer devant les ruines de Carthage paraissait ordinaire, presque banal. Un…',
    'Date/Period: 18th century (Husainid period) Material/Technique: Marble, carved plaster, qallaline ceramic tiles Description: This architectural element is a mahram, an ornamental niche inspired by the form of the mihrab.':
        'Date/Période : XVIIIe siècle (période husseinite) Matériau/Technique : marbre, plâtre sculpté, carreaux de faïence de Qallaline Description : cet élément architectural est un mahram, une niche ornementale inspirée de la forme du mihrab.',
    'Please write. We work with universities, museums, mapping communities and nonprofits, in Tunisia and beyond. The Unique Mappers in Nigeria are the first community bringing the model to a second country. Reach us at':
        'Écrivez-nous. Nous travaillons avec des universités, des musées, des communautés de cartographie et des associations, en Tunisie et ailleurs. Les Unique Mappers au Nigéria sont la première communauté à porter ce modèle dans un deuxième pays. Contactez-nous à',
    'Courses, mentoring for students, hosting and tools, the weekly call across four continents. The unglamorous part that keeps eighty-five volunteers working, and the first paid coordinator when we can afford one.':
        'Des cours, du mentorat pour les étudiants, l’hébergement et les outils, l’appel hebdomadaire sur quatre continents. La partie ingrate qui permet à quatre-vingt-cinq bénévoles de travailler, et le premier poste de coordination rémunéré quand nous pourrons nous le permettre.',
    'One promise we keep whatever the partnership: the archive stays free and open,\nand our volunteers are never made to work so that someone else earns. We sell training, events and our time, never the heritage.':
        'Une promesse que nous tenons quel que soit le partenariat : l’archive reste gratuite et ouverte, et nos bénévoles ne sont jamais mis à contribution pour que quelqu’un d’autre gagne de l’argent. Nous vendons de la formation, des événements et notre temps, jamais le patrimoine.',
    'A workshop for your team on phone photogrammetry, on objects and places we are free to scan, with the method our volunteers use. A skill people keep, and a new way to look at the street they walk every day.':
        'Un atelier pour votre équipe sur la photogrammétrie au téléphone, sur des objets et des lieux que nous sommes libres de numériser, avec la méthode qu’utilisent nos bénévoles. Une compétence que les gens gardent, et une nouvelle façon de regarder la rue qu’ils empruntent tous les jours.',
    'A curated board of grants, residencies, fellowships, open calls,\nand events for artists, XR creators, educators, students, and changemakers, updated regularly by the\nTanit XR team. Also published as our':
        'Un tableau sélectionné de bourses, résidences, programmes de recherche, appels à candidatures et événements pour les artistes, les créateurs XR, les enseignants, les étudiants et les porteurs de changement, mis à jour régulièrement par l’équipe de Tanit XR. Également publié dans notre',
    'Your developers and designers, our volunteers and our published scans, one weekend or one quarter: an AR lesson, a VR room, a piece for your own event. The kind of project your team asks to be part of.':
        'Vos développeurs et vos designers, nos bénévoles et nos numérisations publiées, le temps d’un week-end ou d’un trimestre : une leçon en réalité augmentée, une salle en VR, une pièce pour votre propre événement. Le genre de projet auquel votre équipe demande à participer.',
    'Remote volunteers turn raw scans into game-ready models, AR lessons and our virtual museum.':
        'À distance, des bénévoles transforment les numérisations brutes en modèles prêts pour le jeu, en leçons de réalité augmentée et en notre musée virtuel.',
    'The Tanit Stela in 3D, with Nura the guide floating beside it':
        'La Stèle de Tanit en 3D, avec Nura la guide qui flotte à côté',
    "A maker's gallery: pieces on plinths in a round room":
        'La galerie d’un créateur : des pièces sur des socles dans une salle ronde',
    'The museum&#x27;s main hall, Made by volunteers':
        'La grande salle du musée, réalisé par des bénévoles',
    'Al Jazeera, Al Jazeera · Culture feature': 'Al Jazeera, Al Jazeera · Reportage culturel',
    'Hall III &nbsp;·&nbsp; feature object': 'Salle III  ·  objet phare',
    'Hall II &nbsp;·&nbsp; feature object': 'Salle II  ·  objet phare',
    'Hall IV &nbsp;·&nbsp; feature object': 'Salle IV  ·  objet phare',
    'The museum&#x27;s main hall 3D model': 'La grande salle du musée, modèle 3D',
    'Hall I &nbsp;·&nbsp; feature object': 'Salle I  ·  objet phare',
    'Hall V &nbsp;·&nbsp; feature object': 'Salle V  ·  objet phare',
    'Ceramic Plate, Made by volunteers': 'Assiette en céramique, réalisé par des bénévoles',
    'Modern Tagine, Made by volunteers': 'Tajine moderne, réalisé par des bénévoles',
    'Underground Passageways 3D model': 'Passages souterrains, modèle 3D',
    'Murex Shell, Made by volunteers': 'Coquillage murex, réalisé par des bénévoles',
    'Splats With Phones – TANIT XR': 'Des splats au téléphone – TANIT XR',
    'Wall Lamp, Made by volunteers': 'Applique murale, réalisé par des bénévoles',
    'Al Jazeera · Culture feature': 'Al Jazeera · Reportage culturel',
    'Ruins on the Tunisian coast': 'Des ruines sur la côte tunisienne',
    'Walk through the collection': 'Parcourez la collection',
    'Bamboo, Made by volunteers': 'Bambou, réalisé par des bénévoles',
    'Pillar, Made by volunteers': 'Pilier, réalisé par des bénévoles',
    '›&nbsp; Splats With Phones': '›  Des splats au téléphone',
    'Optimize &amp;amp; Build': 'Optimiser &amp; construire',
    'Research &amp;amp; Share': 'Rechercher &amp; partager',
    'Architectural Fragments': 'Fragments architecturaux',
    'Rug, Made by volunteers': 'Tapis, réalisé par des bénévoles',
    'Scan &amp;amp; Preserve': 'Numériser &amp; préserver',
    'Underground Passageways': 'Passages souterrains',
    'Ceramic Plate 3D model': 'Assiette en céramique, modèle 3D',
    'Modern Tagine 3D model': 'Tajine moderne, modèle 3D',
    '›&nbsp; ImmerseGT 2026': '›  ImmerseGT 2026',
    'Mentor &amp;amp; Grow': 'Encadrer &amp; faire grandir',
    'Press & Recognition': 'Presse et distinctions',
    'Corinthian Capital': 'Chapiteau corinthien',
    'Made by volunteers': 'Réalisé par des bénévoles',
    'Splats With Phones': 'Des splats au téléphone',
    'Wall Lamp 3D model': 'Applique murale, modèle 3D',
    'Community Liaison': 'Liaison communautaire',
    'Makers’ galleries': 'Galeries des créateurs',
    'A lasting record': 'Une trace durable',
    'Reclining Figure': 'Figure allongée',
    'Regional Manager': 'Responsable régional',
    'Traditional Door': 'Porte traditionnelle',
    'Bamboo 3D model': 'Bambou, modèle 3D',
    'Chief Scientist': 'Responsable scientifique',
    'Pillar 3D model': 'Pilier, modèle 3D',
    'Project Manager': 'Chef de projet',
    'Statue Fragment': 'Fragment de statue',
    'Turn any object': 'Faites tourner n’importe quel objet',
    'Save and share': 'Enregistrer et partager',
    'Bust Fragment': 'Fragment de buste',
    'Ceramic Plate': 'Assiette en céramique',
    'Draped Statue': 'Statue drapée',
    'Illustration:': 'Illustration :',
    'Medium Object': 'Objet moyen',
    'Modern Tagine': 'Tajine moderne',
    'Mihrab Niche': 'Niche du mihrab',
    'Punic Stelae': 'Stèles puniques',
    'Roman Column': 'Colonne romaine',
    'Rug 3D model': 'Tapis, modèle 3D',
    'Sacred Niche': 'Niche sacrée',
    'Small Object': 'Petit objet',
    'Murex Shell': 'Coquillage murex',
    'Punic Stela': 'Stèle punique',
    'Stone Basin': 'Bassin en pierre',
    'Tanit Stela': 'Stèle de Tanit',
    'Works in VR': 'Fonctionne en VR',
    'Byrsa Hill': 'Colline de Byrsa',
    'Large Area': 'Grande zone',
    'Newsletter': 'Infolettre',
    'Niche Wall': 'Mur à niches',
    'Community': 'Communauté',
    'Galleries': 'Galeries',
    'Meet Nura': 'Rencontrez Nura',
    'Volunteer': 'Bénévolat',
    'Wall Lamp': 'Applique murale',
    'project.': 'projet.',
    'Caption': 'Légende',
    'English': 'Anglais',
    'Explore': 'Explorer',
    'Founder': 'Fondatrice',
    'Gallery': 'Galerie',
    'Objects': 'Objets',
    'Bamboo': 'Bambou',
    'Choose': 'Choisir',
    'Period': 'Période',
    'Pillar': 'Pilier',
    'Record': 'Enregistrer',
    'Share…': 'Partager…',
    '“Mesh”': '« Mesh »',
    'Clear': 'Effacer',
    'Close': 'Fermer',
    'Email': 'E-mail',
    'Halls': 'Salles',
    'Logon': 'Connexion',
    'Punic': 'Punique',
    'Saved': 'Enregistré',
    'Sound': 'Son',
    'saved': 'enregistré',
    'Join': 'Rejoindre',
    'More': 'Plus',
    'Map': 'Carte',
    'New': 'Nouveau',
    'Oct': 'oct.',
    'Rug': 'Tapis',

    # ---- added 2026-09-21: pages that were still English ----
    'Our mission is to preserve Tunisia’s endangered heritage through digital scans, immersive technology, and\neducation. With every artifact we scan and every volunteer we train, we are proving that heritage can be\nsafeguarded for future generations, no matter the threats of climate change and neglect.':
        'Notre mission est de préserver le patrimoine tunisien menacé grâce à la numérisation, aux technologies\nimmersives et à l’éducation. Chaque objet numérisé et chaque bénévole formé prouvent que le patrimoine peut\nêtre sauvegardé pour les générations futures, malgré le changement climatique et l’abandon.',
    'Ines scanning at Carthage': 'Ines en train de numériser à Carthage',

    # ---- added 2026-09-21: pages that were still English ----
    '›\xa0 ImmerseGT 2026': '›  ImmerseGT 2026',

    # ---- added 2026-09-21: pages that were still English ----
    'Tanit XR&#x27;s work was shown in the XR Women Museum, including its &quot;Garden: In Full Bloom&quot; exhibition, an immersive museum of 30+ gallery worlds directed by Paige Dansinger.':
        'Le travail de Tanit XR a été présenté au XR Women Museum, notamment dans son exposition « Garden: In Full Bloom », un musée immersif de plus de 30 mondes-galeries dirigé par Paige Dansinger.',
    'Al Jazeera, &quot;Tanit XR&quot;: a non-profit platform documenting Tunisian heritage digitally (Arabic)':
        'Al Jazeera, « Tanit XR » : une plateforme à but non lucratif qui documente le patrimoine tunisien en numérique (en arabe)',
    '&quot;Apteranthes europaea&quot; cactus': 'Cactus "Apteranthes europaea"',

    # ---- added 2026-09-21: pages that were still English ----
    "Get new grants, residencies, and open calls for art, XR &amp; impact in your\ninbox, free, from the Tanit XR team. You'll also be first to hear how our heritage-preservation work is\ngoing.":
        'Recevez gratuitement les nouvelles subventions, résidences et appels à candidatures en art, XR &amp; impact,\ndirectement de l’équipe Tanit XR. Vous serez aussi les premiers informés de l’avancée de notre travail de\npréservation du patrimoine.',

    # ---- added 2026-09-21: pages that were still English ----
    'Artifacts scanned': 'Objets numérisés',
    'Sites documented': 'Sites documentés',
    'Global reach': 'Portée mondiale',

    # ---- added 2026-09-21: pages that were still English ----
    'Continue to Press &amp; Recognition': 'Continuer vers Presse et distinctions',
    'Press &amp; Recognition – Tanit XR': 'Presse et distinctions – Tanit XR',
    '3D Modeler &amp; Web Contributor': 'Modeleur 3D et contributrice web',
    'Strategy &amp; Creative Support': 'Stratégie et soutien créatif',
    'The museum&#x27;s main hall': 'La salle principale du musée',

    # ---- added 2026-09-21: pages that were still English ----
    'Save &#9825;': 'Enregistrer &#9825;',

    # ---- added 2026-09-21: roles that were only half translated ----
    'Partnerships &amp; Community': 'Partenariats et communauté',
    '2D Design &amp; 3D Generalist': 'Design 2D et généraliste 3D',
}


AR = {
    # ---- navigation / header ----
    ">Home</a>": ">الرئيسية</a>",
    ">Archive</a>": ">الأرشيف</a>",
    ">About</a>": ">من نحن</a>",
    ">Our People</a>": ">فريقنا</a>",
    ">Art, XR &amp; Impact Opportunities</a>": ">فرص الفن والواقع الممتد والأثر</a>",
    ">News</a>": ">الأخبار</a>",
    ">El Jem Conference</a>": ">مؤتمر الجم</a>",
    ">TanitXR &amp; the Unique Mappers</a>": ">TanitXR وشبكة Unique Mappers</a>",
    ">Volunteer</a>": ">التطوع</a>",
    ">Events</a>": ">الفعاليات</a>",
    ">Contact</a>": ">اتصل بنا</a>",
    ">Donate</a>": ">تبرّع</a>",
    ">Opportunities</a>": ">الفرص</a>",
    ">Workshops</a>": ">ورشات العمل</a>",
    "AR/VR Experiences": "تجارب الواقع المعزز والافتراضي",

    # ---- footer ----
    "<h4>About Tanit XR</h4>": "<h4>عن تانيت XR</h4>",
    "Tanit XR is a nonprofit initiative working to digitally preserve Tunisia’s cultural heritage before it disappears to time, weather, or neglect. Through 3D scanning, an open digital archive, and immersive AR/VR experiences, we make mosaics, statues, and historic sites accessible to students, researchers, and the public everywhere.":
        "تانيت XR مبادرة غير ربحية تعمل على الحفظ الرقمي للتراث الثقافي التونسي قبل أن يندثر بفعل الزمن أو المناخ أو الإهمال. من خلال المسح ثلاثي الأبعاد وأرشيف رقمي مفتوح وتجارب غامرة بالواقع المعزز والافتراضي، نجعل الفسيفساء والتماثيل والمواقع التاريخية في متناول الطلاب والباحثين والجمهور في كل مكان.",
    "<h4>Explore</h4>": "<h4>استكشف</h4>",
    "<h4>Get Involved</h4>": "<h4>شارك معنا</h4>",
    "<h4>Contact</h4>": "<h4>اتصل بنا</h4>",
    "Email: ": "البريد الإلكتروني: ",
    "Phone: ": "الهاتف: ",
    "Fiscally sponsored by Florida Community Innovation, a U.S. 501(c)(3) nonprofit.":
        "برعاية مالية من Florida Community Innovation، منظمة أمريكية غير ربحية 501(c)(3).",
    "© 2026 Tanit XR. All rights reserved.": "© 2026 تانيت XR. جميع الحقوق محفوظة.",
    ">Privacy Policy</a>": ">سياسة الخصوصية</a>",
    "Trending now": "الرائج الآن",

    # ---- home ----
    "<title>Home – TANIT XR</title>": "<title>الرئيسية – TANIT XR</title>",
    "Preserving Heritage": "صون التراث",
    "Preserving Tunisia’s endangered heritage. Climate change, erosion, and neglect threaten our ruins. We capture them in 3D and bring them to life in AR and VR so they are never forgotten.":
        "نصون تراث تونس المهدّد. التغيّر المناخي والتعرية والإهمال تهدد آثارنا. نلتقطها بتقنية ثلاثية الأبعاد ونبعث فيها الحياة بالواقع المعزز والافتراضي حتى لا تُنسى أبدًا.",
    ">Join the Mission</a>": ">انضم إلى المهمة</a>",
    "Explore the Archive →": "استكشف الأرشيف ←",
    ">Explore the Archive</a>": ">استكشف الأرشيف</a>",
    "Digital Scanning": "المسح الرقمي",
    "Recording mosaics, statues, and ruins at risk before time, weather, and climate erase them.":
        "توثيق الفسيفساء والتماثيل والآثار المهددة قبل أن يمحوها الزمن والمناخ.",
    "See how we scan →": "شاهد كيف نقوم بالمسح ←",
    "Open Archive": "أرشيف مفتوح",
    "A free, growing online library where anyone can explore Tunisia’s heritage. Perfect for teachers, students, and the public.":
        "مكتبة مجانية متنامية على الإنترنت يمكن لأي شخص من خلالها استكشاف تراث تونس. مثالية للمعلمين والطلاب والجمهور.",
    "Education &amp; Workshops": "التعليم وورشات العمل",
    "Hands-on training for students and volunteers in scanning, model cleanup, and storytelling. Programs in Tunisia and online.":
        "تدريب عملي للطلاب والمتطوعين على المسح وتنقيح النماذج وسرد القصص. برامج في تونس وعبر الإنترنت.",
    "Attend a workshop →": "شارك في ورشة ←",
    "Immersive learning: place mosaics in your space with AR or walk inside a Roman villa in VR. Designed for schools and museums.":
        "تعلّم غامر: ضع الفسيفساء في مكانك بالواقع المعزز أو تجوّل داخل فيلا رومانية بالواقع الافتراضي. مصمم للمدارس والمتاحف.",
    "Try a demo →": "جرّب عرضًا ←",
    "Partnerships &amp; Research": "الشراكات والبحث",
    "Working with institutions and experts to document sites, enhance accuracy, and share context so history is preserved and understood.":
        "نعمل مع المؤسسات والخبراء لتوثيق المواقع وتحسين الدقة ومشاركة السياق حتى يُحفظ التاريخ ويُفهم.",
    "Learn &amp; participate →": "تعلّم وشارك ←",
    "Global Volunteer Network": "شبكة متطوعين عالمية",
    "Join from Tunisia or abroad. Scan on site, help classify models, write context, or build apps that bring heritage to life.":
        "انضم من تونس أو من الخارج. امسح في الميدان، أو ساعد في تصنيف النماذج، أو اكتب السياق، أو طوّر تطبيقات تُحيي التراث.",
    "Volunteer with us →": "تطوّع معنا ←",
    "Featured Scans": "نماذج مختارة",
    "Highlights from the Tanit XR Archive": "أبرز ما في أرشيف تانيت XR",
    ">Open the Full Archive</a>": ">افتح الأرشيف الكامل</a>",
    "Why It Matters": "لماذا هذا مهم",
    "Heritage on the Brink": "تراث على حافة الهاوية",
    "Tunisia’s ruins are vanishing faster than they can be protected. Climate change brings floods, storms, and heat that accelerate erosion. Without urgent action, pieces of world history could disappear.":
        "تتلاشى آثار تونس أسرع مما يمكن حمايتها. يجلب التغيّر المناخي فيضانات وعواصف وحرارة تسرّع التعرية. وبدون تحرك عاجل، قد تختفي أجزاء من تاريخ العالم.",
    "A Lasting Record": "سجلّ باقٍ",
    "With every scan, Tanit XR creates a permanent archive. Even if the physical site is lost, the digital memory survives – for schools, museums, and future generations.":
        "مع كل عملية مسح، تُنشئ تانيت XR أرشيفًا دائمًا. حتى لو فُقد الموقع المادي، تبقى الذاكرة الرقمية – للمدارس والمتاحف والأجيال القادمة.",
    ">Donate Now</a>": ">تبرّع الآن</a>",
    ">Learn More</a>": ">اعرف المزيد</a>",
    "Our Team": "فريقنا",
    "Powered by our people": "بسواعد فريقنا",
    "Tanit XR is led by a dedicated core team and powered by a growing network of volunteers across Tunisia and the world.":
        "تقود تانيت XR نواةٌ متفانية من الفريق، وتدعمها شبكة متنامية من المتطوعين في تونس والعالم.",
    "Read More →": "اقرأ المزيد ←",
    ">Meet Everyone</a>": ">تعرّف على الجميع</a>",
    "Testimonials": "شهادات",
    "Hear from the volunteers and mentors shaping Tanit XR": "اسمع من المتطوعين والموجّهين الذين يصنعون تانيت XR",
    "I joined Tanit XR because I didn’t want to see our history disappear. When you walk through ruins in Carthage or Dougga, you can already see the erosion and damage from weather and time. Volunteering with Tanit XR gave me a way to fight back against that loss. Every scan I help with feels like I’m protecting a piece of Tunisia for future generations.":
        "انضممت إلى تانيت XR لأنني لم أرد أن أرى تاريخنا يختفي. حين تمشي بين آثار قرطاج أو دقّة، ترى بالفعل التعرية وأضرار المناخ والزمن. منحني التطوع مع تانيت XR وسيلةً لمقاومة هذا الفقدان. كل عملية مسح أساهم فيها أشعر أنني أحمي قطعة من تونس للأجيال القادمة.",
    "I joined Tanit XR because of the community. I love the people involved, and I am so grateful that we get to work together to celebrate our shared global, human heritage and shine a world spotlight on one of the most beautiful countries out there: Tunisia.":
        "انضممت إلى تانيت XR من أجل المجتمع. أحب الأشخاص المشاركين فيه، وأنا ممتنة جدًا لأننا نعمل معًا للاحتفاء بتراثنا الإنساني المشترك وتسليط أضواء العالم على واحد من أجمل البلدان: تونس.",
    "I started Tanit XR by simply walking around Carthage with my phone, scanning ruins because I couldn’t stand the idea of them being lost forever. Over time I realized this was bigger than me: people in Tunisia and abroad wanted to help, and it became a movement. Climate change, erosion, and neglect are real threats, but every scan is a way to push back, to make sure our heritage is preserved and celebrated.":
        "بدأتُ تانيت XR بمجرد التجوّل في قرطاج بهاتفي، أمسح الآثار لأنني لم أحتمل فكرة ضياعها إلى الأبد. مع الوقت أدركت أن الأمر أكبر مني: أراد أشخاص في تونس وخارجها المساعدة، فصار حركة. التغيّر المناخي والتعرية والإهمال تهديدات حقيقية، لكن كل عملية مسح هي وسيلة للمقاومة، ولضمان صون تراثنا والاحتفاء به.",
    "Artifacts Scanned": "قطعة أثرية ممسوحة",
    "Sites Documented": "موقعًا موثّقًا",
    "Volunteers</span>": "متطوعًا</span>",
    "Global Reach": "وصول عالمي",
    "Partners &amp; Supporters": "الشركاء والداعمون",

    # ---- archive ----
    "<title>Archive – TANIT XR</title>": "<title>الأرشيف – TANIT XR</title>",
    "Explore the Tanit XR Archive": "استكشف أرشيف تانيت XR",
    "&nbsp;›&nbsp; Archive</div>": "&nbsp;›&nbsp; الأرشيف</div>",
    "A free, growing library of 3D scans of Tunisia’s endangered heritage — mosaics, statues, stelae, and ruins captured by our volunteers. Every model can be explored interactively, and viewed in augmented reality on your phone.":
        "مكتبة مجانية متنامية من النماذج ثلاثية الأبعاد لتراث تونس المهدد — فسيفساء وتماثيل وأنصاب وآثار وثّقها متطوعونا. يمكن استكشاف كل نموذج تفاعليًا ومشاهدته بالواقع المعزز على هاتفك.",
    '>All (': ">الكل (",
    ">View on Sketchfab</a>": ">شاهده على Sketchfab</a>",
    "← Back to Archive": "العودة إلى الأرشيف ←",

    # ---- news ----
    "<title>News – TANIT XR</title>": "<title>الأخبار – TANIT XR</title>",
    "<h1>News</h1>": "<h1>الأخبار</h1>",
    "&nbsp;›&nbsp; News</div>": "&nbsp;›&nbsp; الأخبار</div>",
    ">Published ": ">نُشر في ",
    "← All News": "كل الأخبار ←",

    # ---- people ----
    "<title>Our People – TANIT XR</title>": "<title>فريقنا – TANIT XR</title>",
    "<h1>Our People</h1>": "<h1>فريقنا</h1>",
    "&nbsp;›&nbsp; Our People</div>": "&nbsp;›&nbsp; فريقنا</div>",
    ">Our People</a> &nbsp;›&nbsp;": ">فريقنا</a> &nbsp;›&nbsp;",
    "Meet the team": "تعرّف على الفريق",
    "Core Team": "الفريق الأساسي",
    "Community Contributors": "مساهمو المجتمع",
    "<b>Are you a Tanit XR volunteer?</b>": "<b>هل أنت متطوع في تانيت XR؟</b>",
    ">Create your profile</a> and it will appear here once approved.":
        ">أنشئ ملفك الشخصي</a> وسيظهر هنا بعد الموافقة عليه.",
    "← Back to Our People": "العودة إلى فريقنا ←",
    "Part of the Tanit XR volunteer network.": "عضو في شبكة متطوعي تانيت XR.",

    # ---- opportunities ----
    "<title>Art, XR &amp; Impact Opportunities – TANIT XR</title>": "<title>فرص الفن والواقع الممتد والأثر – TANIT XR</title>",
    "<h1>Art, XR &amp; Impact Opportunities</h1>": "<h1>فرص الفن والواقع الممتد والأثر</h1>",
    "&nbsp;›&nbsp; Art, XR &amp; Impact Opportunities</div>": "&nbsp;›&nbsp; فرص الفن والواقع الممتد والأثر</div>",
    "A curated board of grants, residencies, fellowships, open calls, and events for artists, XR creators, educators, students, and changemakers — updated regularly by the Tanit XR team. Also published as our":
        "لوحة منتقاة من المنح والإقامات الفنية والزمالات والدعوات المفتوحة والفعاليات للفنانين ومبدعي الواقع الممتد والمعلمين والطلاب وصنّاع التغيير — يحدّثها فريق تانيت XR بانتظام. تُنشر أيضًا في",
    ">LinkedIn newsletter</a>.": ">نشرتنا على LinkedIn</a>.",
    'placeholder="Search…"': 'placeholder="ابحث…"',
    '<option value="">Type</option>': '<option value="">النوع</option>',
    '<option value="">Eligibility</option>': '<option value="">الأهلية</option>',
    '<option value="">Mode</option>': '<option value="">طريقة المشاركة</option>',
    ">Deadline soonest</option>": ">الأقرب موعدًا</option>",
    ">Newest</option>": ">الأحدث</option>",

    # ---- volunteer ----
    "<title>Volunteer – TANIT XR</title>": "<title>التطوع – TANIT XR</title>",
    "<h1>Volunteer</h1>": "<h1>التطوع</h1>",
    "&nbsp;›&nbsp; Volunteer</div>": "&nbsp;›&nbsp; التطوع</div>",
    "Want to join our team of volunteers?": "هل تريد الانضمام إلى فريق متطوعينا؟",
    '>⏰ Closing this week</button>': '>⏰ تنتهي هذا الأسبوع</button>',
    '>Quick picks</span>': '>اختصارات</span>',
    '>For artists</button>': '>للفنانين</button>',
    '>For XR creators</button>': '>لصنّاع XR</button>',
    '>For students</button>': '>للطلبة</button>',
    '>For nonprofits</button>': '>للجمعيات</button>',
    '<summary>Type <span': '<summary>النوع <span',
    '<summary>Eligibility <span': '<summary>الأهلية <span',
    '<summary>Mode <span': '<summary>الصيغة <span',
    '<span>Sort:</span>': '<span>ترتيب:</span>',
    'placeholder="Search…"': 'placeholder="ابحث…"',
    '<option value="soon">Deadline soonest</option><option value="new">Newest</option>': '<option value="soon">الأقرب موعدًا</option><option value="new">الأحدث</option>',
    'placeholder="Search opportunities…"': 'placeholder="ابحث عن فرصة…"',
    '>Deadline soonest</button>': '>الأقرب موعدًا</button>',
    '>Newest</button>': '>الأحدث</button>',
    '<span class="flabel">Sort</span>': '<span class="flabel">ترتيب</span>',
    '<span class="flabel">Type</span>': '<span class="flabel">النوع</span>',
    '<span class="flabel">Eligibility</span>': '<span class="flabel">الأهلية</span>',
    '<span class="flabel">Mode</span>': '<span class="flabel">الصيغة</span>',
    'class="pill on" data-v="">All</button>': 'class="pill on" data-v="">الكل</button>',
    '>Clear filters</button>': '>مسح الفلاتر</button>',
    'Get these in your inbox': 'احصل عليها في بريدك',
    'New opportunities every one to two weeks. Free.': 'فرص جديدة كل أسبوع أو أسبوعين. مجانًا.',
    'Opportunities and news, in your inbox': 'الفرص والأخبار في بريدك',
    'Grants, residencies and open calls for artists and XR creators every one to two\nweeks, only things we’d apply to ourselves, plus occasional Tanit XR news. Free, unsubscribe any time.': 'منح وإقامات ودعوات للفنانين وصنّاع XR كل أسبوع أو أسبوعين — فقط ما كنا لنتقدّم إليه بأنفسنا — مع أخبار تانيت XR من حين لآخر. مجانًا، ويمكنك إلغاء الاشتراك في أي وقت.',
    '> Opportunities (every 1–2 weeks)</label>': '> الفرص (كل أسبوع أو أسبوعين)</label>',
    '> Tanit XR news (occasional)</label>': '> أخبار تانيت XR (أحيانًا)</label>',
    'Work with the Tanit XR team': 'اعمل مع فريق تانيت XR',
    '<b>Links, all optional.</b> Only the ones you add appear on your profile, as icons.': '<b>الروابط — كلها اختيارية.</b> تظهر فقط الروابط التي تضيفها على ملفك، كأيقونات.',
    '>GitHub</label>': '>GitHub</label>',
    '>Sketchfab</label>': '>Sketchfab</label>',
    'Other (YouTube, X, Behance…)': 'أخرى (YouTube، X، Behance…)',
    'Show a public email icon on your profile? (optional)': 'إظهار أيقونة بريد عام على ملفك؟ (اختياري)',
    'Leave empty to keep your email private': 'اتركه فارغًا لإبقاء بريدك خاصًا',
    ' has made with us</h2>': ' مع تانيت XR</h2>',
    '<h2 class="sec-title" style="font-size:32px">What ': '<h2 class="sec-title" style="font-size:32px">ما صنعه ',
    'Scanning &amp; optimization guide for volunteers (with Rachel West and Nick Kaufmann)': 'دليل المسح والتحسين للمتطوعين (مع رايتشل ويست ونيك كوفمان)',
    'Social media videos for Tanit XR': 'فيديوهات تانيت XR لوسائل التواصل',
    'Built for the community': 'بُني للمجتمع',
    'Virtual museum, the original room and the modular building kit': 'المتحف الافتراضي — القاعة الأصلية وعُدّة البناء المعيارية',
    'Tutorial videos for volunteers': 'فيديوهات تعليمية للمتطوعين',
    'Mentoring students': 'إرشاد الطلبة',
    '>Services</a>': '>خدماتنا</a>',
    '<h1>Services</h1>': '<h1>خدماتنا</h1>',
    '&nbsp;›&nbsp; Services</div>': '&nbsp;›&nbsp; خدماتنا</div>',
    '>Work with us</a>': '>اعمل معنا</a>',
    '>Work with us</div>': '>اعمل معنا</div>',
    'What we do for volunteers, we can do for you': 'ما نفعله لمتطوعينا يمكننا فعله لك',
    'Scanning &amp; 3D optimization': 'المسح والتحسين ثلاثي الأبعاد',
    'Workshops &amp; training': 'ورش وتدريب',
    'Sharing opportunities': 'نشر الفرص',
    'Talks &amp; consulting': 'محاضرات واستشارات',
    'Custom XR experiences': 'تجارب XR مخصّصة',
    'Hackathon &amp; challenge tracks': 'مسارات هاكاثون وتحديات',
    'Three steps': 'ثلاث خطوات',
    'Tell us what you need': 'أخبرنا بما تحتاجه',
    'We scope it together': 'نحدّد النطاق معًا',
    'You get the work, and the community gets funded': 'تحصل على العمل — ويُموَّل المجتمع',
    'Get in touch': 'تواصل معنا',
    'Partner with us': 'كن شريكًا',
    'What are you interested in?': 'ما الذي يهمّك؟',
    'Tell us more': 'أخبرنا أكثر',
    '>Send</button>': '>إرسال</button>',
    'Prefer to give?': 'تفضّل التبرع؟',
    'Every service funds the community, so does every donation': 'كل خدمة تموّل المجتمع — وكذلك كل تبرع',
    '>Organization</label>': '>المنظمة</label>',
    '>Name</label>': '>الاسم</label>',
    'Recorded history lessons': 'دروس تاريخ مسجّلة',
    'Julia records a short lesson each week so volunteers in any time zone can follow along and pick a task.': 'تسجّل جوليا درسًا قصيرًا كل أسبوع ليتابعه المتطوعون في أي منطقة زمنية ويختاروا مهمة.',
    '— coordinated on the Thursday call.': '— بالتنسيق في لقاء الخميس.',
    'Built so far by ': 'بناه حتى الآن ',
    'Artifacts scanned by volunteers': 'قطعة مسحها المتطوعون',
    'Heritage sites documented': 'موقعًا تراثيًا موثّقًا',
    'Volunteers on four continents': 'متطوعًا في أربع قارات',
    'People reached online': 'شخصًا وصلنا إليهم عبر الإنترنت',
    '>What we do</div>': '>ما نفعله</div>',
    'Six ways the community works': 'ست طرق يعمل بها المجتمع',
    'Tanit XR started with a phone and the ruins Ines grew up next to.\nToday, volunteers in Tunisia, the US, Europe and Nigeria meet every week to scan, optimize, teach each other history,\nmentor students and publish research, building a free 3D archive of Tunisia’s heritage, and a model for other\nunder-represented regions.': 'بدأت تانيت XR بهاتف وبالأطلال التي كبرت إيناس بجوارها. واليوم يلتقي متطوعون في تونس والولايات المتحدة وأوروبا ونيجيريا كل أسبوع للمسح والتحسين وتعليم بعضهم التاريخ وإرشاد الطلبة ونشر البحوث — ليبنوا أرشيفًا ثلاثي الأبعاد مجانيًا للتراث التونسي، ونموذجًا لمناطق أخرى ناقصة التمثيل.',
    '>Virtual Museum</a>': '>المتحف الافتراضي</a>',
    '<h1>Virtual Museum</h1>': '<h1>المتحف الافتراضي</h1>',
    '&nbsp;›&nbsp; Virtual Museum</div>': '&nbsp;›&nbsp; المتحف الافتراضي</div>',
    'Visit the virtual museum': 'زُر المتحف الافتراضي',
    'In progress': 'قيد الإنجاز',
    'A museum built by volunteers, from real scans': 'متحف بناه متطوعون من مسوحات حقيقية',
    'Walkthrough recorded in the Unity editor, March 2026.': 'جولة مسجّلة في محرّر Unity، مارس 2026.',
    'How it works': 'كيف يعمل',
    'Rooms you can walk through, objects you can get close to': 'قاعات تمشي فيها، وقطع تقترب منها',
    'Real artifacts': 'قطع حقيقية',
    'Modular rooms': 'قاعات معيارية',
    'Sound from the sites': 'أصوات من المواقع',
    'A guide': 'مرشدة',
    'Headset, browser, phone': 'نظارة، متصفح، هاتف',
    'Made by the community': 'من صنع المجتمع',
    '>Progress</div>': '>التقدّم</div>',
    'From greybox to galleries': 'من الهيكل الرمادي إلى القاعات',
    'Inside the museum': 'داخل المتحف',
    'Objects made by our volunteers': 'قطع من صنع متطوعينا',
    'Browse the scans on display': 'استعرض المسوحات المعروضة',
    'Help finish it': 'ساعدنا على إكماله',
    'Build a room. Fund a room.': 'ابنِ قاعة. موِّل قاعة.',
    'The domed hall, March 2026.': 'القاعة المقبّبة، مارس 2026.',
    'The second wing in greybox, August 2026.': 'الجناح الثاني في الهيكل الرمادي، أوت 2026.',
    '>Volunteer Profile (members)</a>': '>ملف المتطوع (للأعضاء)</a>',
    'Once accepted, create your profile': 'بعد القبول، أنشئ ملفك',
    'Accepted volunteers get their own page here: your scans, models and articles are credited to you.': 'المتطوعون المقبولون يحصلون على صفحتهم هنا: تُنسب إليك مسوحاتك ونماذجك ومقالاتك.',
    'For accepted Tanit XR volunteers only.': 'للمتطوعين المقبولين في تانيت XR فقط.',
    'Not a volunteer yet? Start with the': 'لست متطوعًا بعد؟ ابدأ بـ',
    '>volunteer interest form</a>, profiles are created after you join.': '>استمارة الاهتمام بالتطوع</a> — تُنشأ الملفات بعد انضمامك.',
    'Finalist, Best Societal Impact': 'متأهل نهائي، أفضل أثر مجتمعي',
    'Episode #1728': 'الحلقة 1728',
    'Video interview': 'مقابلة فيديو',
    'Culture feature (Arabic)': 'تقرير ثقافي (بالعربية)',
    'Two exhibitions': 'معرضان',
    'Track sponsor 2026': 'راعي مسار 2026',
    'Feature article': 'مقال مطوّل',
    'Our impact so far': 'أثرنا حتى الآن',
    'Small team, growing archive': 'فريق صغير، أرشيف يكبر',
    'Weekly community call, Thursdays, 12 pm Eastern': 'لقاء أسبوعي للمجتمع — الخميس 12 ظهرًا بتوقيت شرق أمريكا',
    'Join Slack and the Thursday call': 'انضم إلى Slack ولقاء الخميس',
    '>Exhibitions</h2>': '>معارض</h2>',
    'A scanning day for a volunteer: transport, mobile data for uploads, backups.': 'يوم مسح لمتطوع: تنقّل، بيانات هاتف للرفع، نسخ احتياطية.',
    'A month of hosting and tools for the archive and the volunteers who optimize models.': 'شهر من الاستضافة والأدوات للأرشيف وللمتطوعين الذين يحسّنون النماذج.',
    'A free workshop or course session for the community, Splats With Phones, history lessons, mentoring.': 'جلسة ورشة أو درس مجاني للمجتمع — Splats With Phones، دروس تاريخ، إرشاد.',
    'Toward the virtual museum and, one day, a professional scanner like the XGRIDS PortalCam.': 'نحو المتحف الافتراضي، ويومًا ما ماسح احترافي مثل XGRIDS PortalCam.',
    'A volunteer community from Tunisia and around the world, scanning endangered heritage in 3D and bringing it to\nlife in AR and VR, and learning from each other along the way.': 'مجتمع من المتطوعين من تونس ومن حول العالم، يمسح التراث المهدّد ثلاثيًا ويحييه بالواقع المعزّز والافتراضي — ويتعلّم بعضنا من بعض على الطريق.',
    '>Join the Community</a>': '>انضم إلى المجتمع</a>',
    'Recognized by': 'اعتراف من',
    'Finalist, Best Societal Impact': 'متأهل نهائي — أفضل أثر مجتمعي',
    'Featured video': 'فيديو مميّز',
    'Paper, 3 languages': 'ورقة بثلاث لغات',
    'Track sponsor': 'راعي مسار',
    '>Speaker</span>': '>متحدّثة</span>',
    'More than an archive': 'أكثر من أرشيف',
    'One phone, the ruins of Carthage, and now a community': 'هاتف واحد، أطلال قرطاج — واليوم مجتمع',
    'Tanit XR started with a phone and the ruins Ines grew up next to. Today it is a\nnetwork of volunteers in Tunisia, the US, Europe and Nigeria who meet every week, scan and optimize together, teach\neach other history, mentor students, publish research and build a free 3D archive of Tunisia’s heritage. The goal is\nto take this model to other under-represented regions.': 'بدأت تانيت XR بهاتف وبالأطلال التي كبرت إيناس بجوارها. واليوم هي شبكة متطوعين في تونس والولايات المتحدة وأوروبا ونيجيريا يلتقون كل أسبوع، يمسحون ويحسّنون النماذج معًا، يعلّمون بعضهم التاريخ، يرشدون الطلبة، ينشرون البحوث ويبنون أرشيفًا ثلاثي الأبعاد مجانيًا للتراث التونسي. الهدف: نقل هذا النموذج إلى مناطق أخرى ناقصة التمثيل.',
    'Scan &amp; Preserve': 'المسح والحفظ',
    'Optimize &amp; Build': 'التحسين والبناء',
    'Learn Together': 'نتعلّم معًا',
    'Mentor &amp; Grow': 'الإرشاد والنمو',
    'Research &amp; Share': 'البحث والمشاركة',
    'Extend Beyond Tunisia': 'ما بعد تونس',
    'Volunteers capture statues, mosaics and ruins with their phones. Every scan becomes a permanent, open record.': 'يلتقط المتطوعون التماثيل والفسيفساء والأطلال بهواتفهم. كل مسح يصبح سجلًا مفتوحًا ودائمًا.',
    'Remote volunteers turn raw scans into game-ready models, AR lessons and our VR museum.': 'يحوّل المتطوعون عن بُعد المسوحات الخام إلى نماذج محسّنة ودروس بالواقع المعزّز ومتحفنا الافتراضي.',
    'Weekly community calls, history lessons on the sites we scan, and the Splats With Phones workshop.': 'لقاءات أسبوعية، ودروس تاريخ عن المواقع التي نمسحها، وورشة Splats With Phones.',
    'Interview prep, portfolio reviews and mentoring for students and early-career volunteers, across four continents.': 'تحضير للمقابلات ومراجعة الأعمال وإرشاد للطلبة والمتطوعين في بداية مسيرتهم — عبر أربع قارات.',
    'Papers, conference talks, podcasts and hackathon tracks. We publish what we learn.': 'أوراق ومحاضرات وبودكاست ومسارات هاكاثون. ننشر ما نتعلّمه.',
    'With the Unique Mappers in Nigeria we are testing the model in a second country. Under-represented heritage everywhere is the goal.': 'مع Unique Mappers في نيجيريا نجرّب النموذج في بلد ثانٍ. الهدف هو التراث ناقص التمثيل في كل مكان.',
    '>See volunteer-made models →</a>': '>شاهد نماذج المتطوعين →</a>',
    '>Join the community →</a>': '>انضم إلى المجتمع →</a>',
    '>Press &amp; recognition →</a>': '>الصحافة والتقدير →</a>',
    '>TanitXR &amp; the Unique Mappers →</a>': '>تانيت XR وUnique Mappers →</a>',
    '>Community</a>': '>المجتمع</a>',
    '>Press &amp; Recognition</a>': '>الصحافة والتقدير</a>',
    'We meet every week': 'نلتقي كل أسبوع',
    'Tanit XR is a weekly call across time zones as much as it is an archive. We\nreview each other’s scans, learn the history behind them, run workshops, prepare students for interviews, share\nTunisian culture, and celebrate wins together.': 'تانيت XR لقاء أسبوعي عبر المناطق الزمنية بقدر ما هي أرشيف. نراجع مسوحات بعضنا، نتعلّم تاريخها، ننظّم ورشًا، نحضّر الطلبة للمقابلات، نتشارك الثقافة التونسية ونحتفل بالنجاحات معًا.',
    '<li>Weekly community call</li><li>History lessons on the sites we scan</li><li>Splats With Phones workshop</li>': '<li>لقاء أسبوعي للمجتمع</li><li>دروس تاريخ عن المواقع التي نمسحها</li><li>ورشة Splats With Phones</li>',
    '<li>Mentoring &amp; interview prep</li><li>Events, talks &amp; hackathons</li><li>Cultural exchange</li>': '<li>إرشاد وتحضير للمقابلات</li><li>فعاليات ومحاضرات وهاكاثونات</li><li>تبادل ثقافي</li>',
    'See how the community works': 'شاهد كيف يعمل المجتمع',
    'Climate is rewriting the coastline': 'المناخ يعيد رسم الساحل',
    'Storm Harry, January 2026': 'العاصفة هاري، جانفي 2026',
    'The storm stripped sediment off the coast at Nabeul and exposed parts of Neapolis, an ancient city lost to a\ntsunami in the 4th century. Within days our volunteers captured the newly revealed ruins in 3D, a record that\nexists no matter what the sea does next.': 'جرفت العاصفة الرواسب عن ساحل نابل وكشفت أجزاءً من نيابوليس، المدينة القديمة التي ابتلعها تسونامي في القرن الرابع. في أيام، التقط متطوعونا الأطلال المكشوفة ثلاثيًا — سجلٌ يبقى مهما فعل البحر بعد ذلك.',
    'Floods, storms and heat are accelerating erosion across Tunisia’s sites. Every scan is a permanent, open record:\neven if the physical site is lost, the digital memory survives, for schools, museums and future generations.': 'الفيضانات والعواصف والحرارة تسرّع تآكل المواقع التونسية. كل مسح سجلٌ مفتوح ودائم: حتى لو ضاع الموقع، تبقى الذاكرة الرقمية — للمدارس والمتاحف والأجيال القادمة.',
    'Read the Neapolis story': 'اقرأ قصة نيابوليس',
    'What people are saying': 'ماذا يُقال عنا',
    'All press, talks &amp; papers': 'كل الصحافة والمحاضرات والأوراق',
    'Where we’re going': 'إلى أين نتّجه',
    'Tunisia is the pilot': 'تونس هي التجربة الأولى',
    'The method, phones, volunteers, open data, works anywhere heritage is\nunder-documented. In 2026 the Unique Mappers Network began scanning in Nigeria with a mini-grant from our fiscal\nsponsor. If you want to bring this to your region, talk to us.': 'الطريقة — هواتف ومتطوعون وبيانات مفتوحة — تصلح أينما كان التراث ناقص التوثيق. في 2026 بدأت شبكة Unique Mappers المسح في نيجيريا بمنحة صغيرة من راعينا المالي. إن أردت نقلها إلى منطقتك، تحدّث معنا.',
    'Bring Tanit XR to your region': 'انقل تانيت XR إلى منطقتك',
    'The Nigeria pilot': 'تجربة نيجيريا',
    "How we're funded": 'كيف نُموَّل',
    'Honest numbers': 'أرقام صادقة',
    'Tanit XR is run entirely by volunteers. So far most costs, travel to\nsites, tools, hosting, hackathon prizes, have been paid out of pocket by our founders, plus a few individual donations\nthrough our fiscal sponsor, the Florida Community Innovation Foundation (a US 501(c)(3), so donations are tax-deductible).\nWe are applying for grants and building partnerships to change that. Here is what a donation does:': 'تانيت XR تُدار بالكامل بالمتطوعين. حتى الآن دُفعت أغلب التكاليف — التنقّل إلى المواقع، الأدوات، الاستضافة، جوائز الهاكاثون — من جيب مؤسِّساتنا، إضافة إلى تبرعات فردية قليلة عبر راعينا المالي Florida Community Innovation Foundation (منظمة أمريكية 501(c)(3)، فالتبرعات معفاة من الضرائب). نتقدّم لمنح ونبني شراكات لتغيير ذلك. هذا ما يفعله التبرع:',
    'A scanning day: transport, mobile data for uploads, backup storage.': 'يوم مسح: تنقّل، بيانات هاتف للرفع، تخزين احتياطي.',
    'Full documentation of one site with several captures and research.': 'توثيق كامل لموقع واحد بعدة التقاطات وبحث.',
    'A field day with collaborators, and the first time we can pay local contributors.': 'يوم ميداني مع شركاء — وأول مرة نستطيع فيها مكافأة المساهمين المحليين.',
    'A complete digital storytelling package for one site, plus better scanning tools.': 'حزمة سرد رقمي كاملة لموقع واحد، مع أدوات مسح أفضل.',
    '>Partner with us</a>': '>كن شريكًا</a>',
    'See the full breakdown': 'التفاصيل الكاملة',
    'We started as an archive. We became a community.': 'بدأنا أرشيفًا. وصرنا مجتمعًا.',
    'What we do together': 'ما نفعله معًا',
    'A week at Tanit XR': 'أسبوع في تانيت XR',
    'How to get in': 'كيف تنضم',
    'No archaeology or 3D background needed. Our first scans were made with a phone.': 'لا حاجة لخلفية في الآثار أو الثلاثي الأبعاد. أولى مسوحاتنا كانت بهاتف.',
    'Fill the volunteer form': 'املأ استمارة التطوع',
    'Join Slack and the weekly call': 'انضم إلى Slack واللقاء الأسبوعي',
    'Pick a first task': 'اختر مهمة أولى',
    'Create your profile': 'أنشئ ملفك',
    'Meet the community': 'تعرّف على المجتمع',
    'What comes out of the weekly calls': 'ما يخرج من اللقاءات الأسبوعية',
    'Bring the model to your region': 'انقل النموذج إلى منطقتك',
    'Weekly community call': 'لقاء أسبوعي للمجتمع',
    'History lessons': 'دروس تاريخ',
    'Mentoring &amp; interview prep': 'إرشاد وتحضير للمقابلات',
    'Events &amp; conferences': 'فعاليات ومؤتمرات',
    'Cultural exchange': 'تبادل ثقافي',
    '<h1>Press &amp; Recognition</h1>': '<h1>الصحافة والتقدير</h1>',
    '<h1>Community</h1>': '<h1>المجتمع</h1>',
    '&nbsp;›&nbsp; Community</div>': '&nbsp;›&nbsp; المجتمع</div>',
    '&nbsp;›&nbsp; Press &amp; Recognition</div>': '&nbsp;›&nbsp; الصحافة والتقدير</div>',
    'Talks &amp; events': 'محاضرات وفعاليات',
    'Podcasts &amp; video': 'بودكاست وفيديو',
    '>Articles</h2>': '>مقالات</h2>',
    '>Partnerships</h2>': '>شراكات</h2>',
    '>Awards</h2>': '>جوائز</h2>',
    'Featured by Niantic Spatial': 'بعدسة Niantic Spatial',
    '>Publications</h2>': '>منشورات</h2>',
    'Media kit': 'ملف صحفي',
    'Support the work': 'ادعم العمل',
    'Volunteer-run, founder-funded, so far': 'بالمتطوعين، وبتمويل المؤسِّسات — حتى الآن',
    'Our recognition came before our funding. Help us change that.': 'جاء التقدير قبل التمويل. ساعدنا على تغيير ذلك.',
    'How we’re funded': 'كيف نُموَّل',
    "Made by our volunteers": "من صنع متطوعينا",
    "Contributions to Tanit XR": "مساهمات في تانيت XR",
    "Apply for the next cohort": "قدّم للدفعة القادمة",
    ">Full Name</label>": ">الاسم الكامل</label>",
    ">Email</label>": ">البريد الإلكتروني</label>",
    ">Time Zone</label>": ">المنطقة الزمنية</label>",
    "Why do you want to join?": "لماذا تريد الانضمام؟",
    ">Short Bio</label>": ">نبذة قصيرة</label>",
    "Experience Level": "مستوى الخبرة",
    "Attendance Commitment": "الالتزام بالحضور",
    "Anything else you want us to know?": "هل هناك شيء آخر تريد إخبارنا به؟",
    ">Apply</button>": ">قدّم</button>",
    "Any level is welcome, pick one": "كل المستويات مرحّب بها — اختر",
    "This course is live and interactive, pick one": "هذه الدورة مباشرة وتفاعلية — اختر",
    ">None yet<": ">لا خبرة بعد<", ">Beginner<": ">مبتدئ<", ">Some experience<": ">بعض الخبرة<",
    ">Advanced<": ">متقدّم<", ">Yes, I can attend at least 5 of 6 sessions<": ">نعم، أستطيع حضور 5 جلسات من 6 على الأقل<",
    ">Not sure yet<": ">لست متأكدًا بعد<",
    "Recreated by hand, for VR &amp; learning": "أُعيد صنعها يدويًا، للواقع الافتراضي والتعلّم",
    "<strong>heritage scans</strong>": "<strong>مسحًا للتراث</strong>",
    "Photogrammetry records of statues, mosaics, stelae and ruins — preservation quality, with game-ready twins.":
        "سجلات مسح ضوئي للتماثيل والفسيفساء والشواهد والأطلال — بجودة الحفظ، مع نسخ مُحسّنة للألعاب.",
    "<strong>models made by our volunteers</strong>": "<strong>نموذجًا من صنع متطوعينا</strong>",
    "Lamps, pottery, plants and everyday objects modeled by hand for our virtual museum. Click to explore in 3D.":
        "مصابيح وفخار ونباتات وأغراض يومية صُممت يدويًا لمتحفنا الافتراضي. انقر لاستكشافها ثلاثيًا.",
    "Made by volunteers (": "من صنع المتطوعين (",
    "volunteer-made models": "نموذجًا من صنع المتطوعين",
    "See all ": "عرض كل ",
    "View in 3D": "عرض ثلاثي الأبعاد",
    "Make one with us": "اصنع واحدًا معنا",
    "Beyond scanning, our volunteers model Tunisian lamps, pottery and plants from scratch for our\nvirtual museum. Press <b>View in 3D</b> to spin one around right here.":
        "إلى جانب المسح، يصمّم متطوعونا مصابيح وفخارًا ونباتات تونسية من الصفر لمتحفنا الافتراضي. اضغط <b>عرض ثلاثي الأبعاد</b> لتدوير أحدها هنا.",
    "What our volunteers create": "ما يصنعه متطوعونا",
    "From a phone scan to a museum-ready model": "من مسح بالهاتف إلى نموذج جاهز للمتحف",
    "Volunteers scan sites on the ground, optimize models for VR, write articles, and model heritage\nobjects by hand — like these.":
        "يمسح المتطوعون المواقع ميدانيًا، ويحسّنون النماذج للواقع الافتراضي، ويكتبون المقالات، ويصمّمون قطع التراث يدويًا — مثل هذه.",
    "contributions to the archive": "مساهمات في الأرشيف",
    "contribution to the archive": "مساهمة في الأرشيف",
    "Press <b>View in 3D</b> on any model to explore it right here.": "اضغط <b>عرض ثلاثي الأبعاد</b> على أي نموذج لاستكشافه هنا.",
    "3D scans captured": "مسوحات ثلاثية الأبعاد",
    "Models optimized for game/VR": "نماذج مُحسّنة للألعاب/الواقع الافتراضي",
    "Models made by hand": "نماذج مصنوعة يدويًا",
    "Articles written": "مقالات مكتوبة",
    "Photogrammetry scan": "مسح ضوئي فوتوغرامتري",
    "Game-ready optimization": "تحسين للألعاب",
    "Modeled for the virtual museum": "صُمّم للمتحف الافتراضي",
    "Fill out our volunteer interest form and we will connect with you about available opportunities.":
        "املأ استمارة الاهتمام بالتطوع وسنتواصل معك بشأن الفرص المتاحة.",
    ">Volunteer Interest Form</a>": ">استمارة الاهتمام بالتطوع</a>",
    ">Read the Scanning Guide</a>": ">اقرأ دليل المسح</a>",
    "Frequently Asked Questions": "الأسئلة الشائعة",
    "How can I become a volunteer?": "كيف أصبح متطوعًا؟",
    "We’re so excited that you’re interested in volunteering! Please fill out our":
        "يسعدنا اهتمامك بالتطوع! يرجى ملء",
    ">volunteer form</a> and we’ll get back to you via email.":
        ">استمارة التطوع</a> وسنرد عليك عبر البريد الإلكتروني.",
    "What should I know before applying?": "ماذا يجب أن أعرف قبل التقديم؟",
    "Our volunteer positions are currently unpaid and remote. We work with volunteers digitally all over the globe. We have some mentorship and networking opportunities available to our volunteers based on your chosen area of focus. Areas of focus we’re currently seeking are: grant writing, XR/VR development, business development, social media management, graphic design, and general interest. All levels of experience and expertise are welcome to volunteer.":
        "مهام التطوع لدينا حاليًا غير مدفوعة وعن بُعد. نعمل مع متطوعين رقميًا من جميع أنحاء العالم، ونوفر فرص إرشاد وتواصل بحسب مجال اهتمامك. المجالات المطلوبة حاليًا: كتابة طلبات المنح، تطوير XR/VR، تطوير الأعمال، إدارة وسائل التواصل الاجتماعي، التصميم الجرافيكي، والاهتمام العام. جميع مستويات الخبرة مرحّب بها.",
    "How does your team work together?": "كيف يعمل فريقكم معًا؟",
    "As a global, virtual team, it’s important for us to communicate asynchronously. The majority of our communication is done via Slack. Once a week, we meet virtually and discuss ongoing, upcoming, and blocked tasks to keep our mission moving forward.":
        "بوصفنا فريقًا عالميًا افتراضيًا، من المهم أن نتواصل بشكل غير متزامن. تتم معظم مراسلاتنا عبر Slack. ونجتمع افتراضيًا مرة في الأسبوع لمناقشة المهام الجارية والقادمة والمتعثرة لدفع مهمتنا قدمًا.",
    "Are there different ways to volunteer?": "هل هناك طرق مختلفة للتطوع؟",
    "As one of our goals is to engage the public in preservation work, the ability to volunteer will eventually expand and become tiered. While we build our foundation, we hold only one tier. Keep checking back to see how you can get involved!":
        "بما أن أحد أهدافنا إشراك الجمهور في أعمال الصون، ستتوسع إمكانيات التطوع تدريجيًا وتصبح على مستويات. وبينما نبني أساسنا، لدينا مستوى واحد فقط. عاود الزيارة لتعرف كيف يمكنك المشاركة!",
    "Do you work with organizations and external partners?": "هل تتعاونون مع منظمات وشركاء خارجيين؟",
    "Preservation, cultural conservation, and climate work is done best in community. We are open to all forms of partnership that help move our mission forward. If you are an archaeologist, non-profit, government agency, or any other organization aligned in the mission of conservation or preservation, please reach out to us at":
        "أعمال الصون والحفاظ الثقافي والعمل المناخي تتم على أفضل وجه بروح الجماعة. نحن منفتحون على كل أشكال الشراكة التي تدفع مهمتنا قدمًا. إذا كنت عالِم آثار أو جمعية أو جهة حكومية أو أي منظمة تشاركنا مهمة الصون والحفاظ، فتواصل معنا على",
    "How much time do I need to dedicate if I become a volunteer?": "كم من الوقت أحتاج أن أخصص إذا أصبحت متطوعًا؟",
    "Volunteer tasks are project and task based. After expressing your interests via the volunteer form, a member of our leadership team will reach out to you with questions about your capacity for available work that aligns with your interests and expertise. You set the expectation on how much you can commit to and what time you have.":
        "مهام التطوع قائمة على المشاريع والمهام. بعد التعبير عن اهتماماتك عبر الاستمارة، سيتواصل معك أحد أعضاء فريق القيادة للسؤال عن مدى تفرغك لأعمال متاحة تناسب اهتماماتك وخبراتك. أنت من يحدد حجم الالتزام والوقت المتاح لديك.",
    "Become a volunteer": "كن متطوعًا",
    "Join us in preserving Tunisia’s cultural heritage": "انضم إلينا في صون التراث الثقافي التونسي",
    "We rely on our international volunteer support to bring TanitXR to life. We greatly appreciate any time you are willing to share with us as we work toward the digital preservation of Tunisia’s historically and culturally rich heritage sites.":
        "نعتمد على دعم متطوعينا الدوليين لإحياء تانيت XR. ونقدّر كثيرًا أي وقت تشاركه معنا في عملنا نحو الصون الرقمي لمواقع تونس الغنية تاريخيًا وثقافيًا.",
    ">Create Your Volunteer Profile</a>": ">أنشئ ملفك التطوعي</a>",

    # ---- create profile ----
    "<title>Create Your Profile – TANIT XR</title>": "<title>أنشئ ملفك الشخصي – TANIT XR</title>",
    "<h1>Create Your Profile</h1>": "<h1>أنشئ ملفك الشخصي</h1>",
    "&nbsp;›&nbsp; Create Your Profile</div>": "&nbsp;›&nbsp; أنشئ ملفك الشخصي</div>",
    "Already volunteering with Tanit XR? Submit your profile and, once approved by the team, it will appear on our":
        "هل أنت متطوع بالفعل مع تانيت XR؟ أرسل ملفك الشخصي، وبعد موافقة الفريق سيظهر في صفحة",
    ">Our People</a> page.": ">فريقنا</a>.",
    ">Your Name</label>": ">اسمك</label>",
    ">Your Role / What you do</label>": ">دورك / ما الذي تقوم به</label>",
    'placeholder="e.g. 3D Generalist, XR Developer, Researcher"': 'placeholder="مثال: فنان 3D، مطوّر XR، باحث"',
    'placeholder="A few sentences about you and what you do with Tanit XR."': 'placeholder="بضع جمل عنك وعن دورك في تانيت XR."',
    ">Photo (link)</label>": ">صورة (رابط)</label>",
    'placeholder="Link to a headshot (Google Drive, Dropbox, LinkedIn photo…)"': 'placeholder="رابط لصورة شخصية (Google Drive أو Dropbox أو صورة LinkedIn…)"',
    "Or simply reply with a photo attached when we email you back.":
        "أو أرفق صورة في ردّك عندما نراسلك عبر البريد الإلكتروني.",
    ">Website / Portfolio</label>": ">موقع إلكتروني / أعمال</label>",
    "Used only to contact you about your profile — it is not published.":
        "يُستخدم فقط للتواصل معك بشأن ملفك — ولا يُنشر.",
    ">Submit Profile</button>": ">إرسال الملف</button>",

    # ---- scanning guide ----
    "<title>Tanit XR Scanning Guide – TANIT XR</title>": "<title>دليل المسح – TANIT XR</title>",
    "<h1>Tanit XR Scanning Guide</h1>": "<h1>دليل المسح من تانيت XR</h1>",
    "&nbsp;›&nbsp; Scanning Guide</div>": "&nbsp;›&nbsp; دليل المسح</div>",
    "Using Scaniverse to Preserve Heritage": "استخدام Scaniverse لصون التراث",
    "📲 Getting Started": "📲 البداية",
    "<b>App:</b> Download Scaniverse from the iOS App Store (iPhone 12 Pro or newer recommended for LiDAR support).":
        "<b>التطبيق:</b> حمّل Scaniverse من متجر تطبيقات iOS (يُنصح بآيفون 12 برو أو أحدث لدعم LiDAR).",
    "<b>Goal:</b> Create detailed 3D scans of historical landmarks, ruins, pottery, architecture, and cultural artifacts for a global digital heritage archive.":
        "<b>الهدف:</b> إنشاء نماذج ثلاثية الأبعاد مفصّلة للمعالم التاريخية والآثار والفخار والعمارة والقطع الثقافية لأرشيف رقمي عالمي للتراث.",
    "🧭 Choosing What to Scan": "🧭 اختيار ما تمسحه",
    "Not sure where to start? Look for objects, places, and details that carry cultural, historical, artistic, or community meaning.":
        "لا تعرف من أين تبدأ؟ ابحث عن أشياء وأماكن وتفاصيل تحمل معنى ثقافيًا أو تاريخيًا أو فنيًا أو مجتمعيًا.",
    "<b>Good things to scan include:</b>": "<b>أشياء جيدة للمسح:</b>",
    "<b>Architecture and ruins</b> — doors, arches, columns, facades, walls, courtyards, tombs, monuments, and historic homes":
        "<b>العمارة والآثار</b> — أبواب وأقواس وأعمدة وواجهات وجدران وأفنية ومقابر ومعالم وبيوت تاريخية",
    "<b>Objects and artifacts</b> — pottery, tools, carvings, statues, tiles, jewelry, textiles, inscriptions, and household items":
        "<b>الأشياء والقطع الأثرية</b> — فخار وأدوات ومنحوتات وتماثيل وبلاط وحليّ ومنسوجات ونقوش وأدوات منزلية",
    "<b>Small details</b> — patterns, textures, symbols, damage, repairs, maker’s marks, or decorative elements":
        "<b>التفاصيل الصغيرة</b> — زخارف وملامس ورموز وأضرار وترميمات وعلامات صنّاع وعناصر تزيينية",
    "<b>Everyday heritage</b> — bakeries, workshops, markets, gathering places, family heirlooms, gardens, and community spaces":
        "<b>التراث اليومي</b> — مخابز وورش وأسواق وأماكن تجمّع وموروثات عائلية وحدائق وفضاءات مجتمعية",
    "<b>At-risk heritage</b> — places or objects threatened by weather, neglect, development, conflict, theft, or loss of memory":
        "<b>التراث المهدد</b> — أماكن أو أشياء يهددها المناخ أو الإهمال أو العمران أو النزاعات أو السرقة أو فقدان الذاكرة",
    "<b>Before scanning, ask:</b>": "<b>قبل المسح، اسأل نفسك:</b>",
    "What story does this object or place tell?": "ما القصة التي يرويها هذا الشيء أو المكان؟",
    "Who uses it, remembers it, or cares about it?": "من يستخدمه أو يتذكره أو يهتم به؟",
    "Is it connected to a tradition, craft, family, neighborhood, or historic event?":
        "هل يرتبط بتقليد أو حرفة أو عائلة أو حيّ أو حدث تاريخي؟",
    "Is it changing, disappearing, or at risk?": "هل يتغيّر أو يختفي أو في خطر؟",
    "<b>Please do not scan sacred, private, restricted, or sensitive objects without permission.</b> When in doubt, ask a local caretaker, community member, owner, or cultural authority first.":
        "<b>يرجى عدم مسح الأشياء المقدسة أو الخاصة أو المقيّدة أو الحساسة دون إذن.</b> عند الشك، اسأل أولًا حارسًا محليًا أو أحد أفراد المجتمع أو المالك أو سلطة ثقافية.",
    "🕯️ Scanning Intangible Heritage": "🕯️ توثيق التراث غير المادي",
    "Some heritage is not just a building or object. It lives in stories, songs, rituals, recipes, crafts, dances, languages, memories, and everyday practices. This is called <b>intangible heritage</b>.":
        "بعض التراث ليس مبنى أو شيئًا ماديًا، بل يعيش في الحكايات والأغاني والطقوس والوصفات والحرف والرقصات واللغات والذكريات والممارسات اليومية. هذا هو <b>التراث غير المادي</b>.",
    "You cannot always 3D scan intangible heritage directly, but you can document the objects, spaces, and people connected to it. Examples:":
        "لا يمكن دائمًا مسح التراث غير المادي مباشرة، لكن يمكنك توثيق الأشياء والأماكن والأشخاص المرتبطين به. أمثلة:",
    "A traditional bread recipe → scan the oven, tools, table, or bakery space":
        "وصفة خبز تقليدية ← امسح الفرن أو الأدوات أو الطاولة أو المخبزة",
    "A weaving practice → scan the loom, textile patterns, tools, or finished pieces":
        "حرفة نسيج ← امسح المنسج أو زخارف النسيج أو الأدوات أو القطع الجاهزة",
    "A family story → scan the home, courtyard, photograph, object, or place connected to the memory":
        "حكاية عائلية ← امسح البيت أو الفناء أو الصورة أو الشيء أو المكان المرتبط بالذكرى",
    "A festival or ritual → scan decorations, costumes, instruments, gathering spaces, or symbolic objects":
        "مهرجان أو طقس ← امسح الزينة أو الأزياء أو الآلات أو أماكن التجمع أو الأشياء الرمزية",
    "A disappearing craft → scan the tools, workshop, materials, and finished work":
        "حرفة في طريق الاندثار ← امسح الأدوات والورشة والمواد والأعمال المنجزة",
    "When documenting intangible heritage, include context with your upload: what the tradition is called, who practices it, where it happens, how you learned about it, why it matters, and any story, memory, or quote that should go with the scan.":
        "عند توثيق التراث غير المادي، أرفق السياق مع ما ترسله: اسم التقليد، ومن يمارسه، وأين يحدث، وكيف عرفت عنه، ولماذا هو مهم، وأي قصة أو ذكرى أو اقتباس ينبغي أن يرافق النموذج.",
    "<b>Always get permission</b> before recording people, private spaces, ceremonies, sacred practices, or personal stories. Tanit XR is not just preserving objects — we are preserving the worlds, memories, and meanings around them.":
        "<b>احصل دائمًا على الإذن</b> قبل تسجيل الأشخاص أو الأماكن الخاصة أو الاحتفالات أو الممارسات المقدسة أو القصص الشخصية. تانيت XR لا تحفظ الأشياء فحسب — بل نحفظ العوالم والذكريات والمعاني من حولها.",
    "🧱 Step-by-Step Scanning Instructions": "🧱 خطوات المسح خطوة بخطوة",
    "1. Open Scaniverse": "1. افتح Scaniverse",
    "Tap the “+” button to start a new scan.": "اضغط زر « + » لبدء مسح جديد.",
    "Choose <b>“Mesh”</b> (not “Splat”) — this is what we need for Tanit XR.":
        "اختر <b>« Mesh »</b> (وليس « Splat ») — فهذا ما نحتاجه في تانيت XR.",
    "Select the size of your object: <b>Small Object</b> (pottery, carvings, statues), <b>Medium Object</b> (doors, columns, mosaics), or <b>Large Area</b> (facades, walls, monuments).":
        "اختر حجم الشيء: <b>Small Object</b> (فخار، منحوتات، تماثيل)، أو <b>Medium Object</b> (أبواب، أعمدة، فسيفساء)، أو <b>Large Area</b> (واجهات، جدران، معالم).",
    "2. Begin the Scan": "2. ابدأ المسح",
    "Move slowly around the object while recording a video.": "تحرّك ببطء حول الشيء أثناء تسجيل الفيديو.",
    "Get multiple angles: walk around, crouch down, raise your phone, etc.":
        "التقط زوايا متعددة: دُر حوله، وانخفض، وارفع هاتفك، وهكذا.",
    "Avoid fast movements and make sure to capture all sides.":
        "تجنّب الحركات السريعة واحرص على تغطية كل الجوانب.",
    "In bright sun, try to scan in partial shade or overcast light.":
        "تحت الشمس الساطعة، حاول المسح في ظل جزئي أو في ضوء غائم.",
    "3. Save Without Processing (Important!)": "3. احفظ دون معالجة (مهم!)",
    "If you’re outside and don’t have strong Wi-Fi or data, tap <b>“Save to process later.”</b>":
        "إذا كنت في الخارج دون واي فاي قوي أو بيانات، اضغط <b>« Save to process later »</b>.",
    "Processing uses a lot of data — it’s best to wait until you’re home with Wi-Fi.":
        "المعالجة تستهلك بيانات كثيرة — من الأفضل الانتظار حتى تكون في المنزل على الواي فاي.",
    "🗂️ Processing and Exporting": "🗂️ المعالجة والتصدير",
    "4. Back at Home: Process Your Scan": "4. في المنزل: عالج مسحك",
    "Open the Scaniverse Library (bottom menu).": "افتح مكتبة Scaniverse (القائمة السفلية).",
    "Tap your saved scan, tap the name, and give it a clear title (e.g., “Ksar Ouled Soltane – Main Door”).":
        "اضغط على المسح المحفوظ، ثم على الاسم، وأعطه عنوانًا واضحًا (مثال: « قصر أولاد سلطان – الباب الرئيسي »).",
    "Tap “Process” and wait for the app to complete the 3D model.":
        "اضغط « Process » وانتظر حتى يكمل التطبيق النموذج ثلاثي الأبعاد.",
    "5. Export the Model": "5. صدّر النموذج",
    "Once processed, tap “Share” &gt; “Export Model.”": "بعد المعالجة، اضغط « Share » &gt; « Export Model ».",
    "Select <b>FBX</b> format and keep <b>textures enabled</b>.": "اختر صيغة <b>FBX</b> وأبقِ <b>الخامات مفعّلة</b>.",
    "Name it “Scan Title_Location”.": "سمّه « عنوان المسح_الموقع ».",
    "6. Share Your Model": "6. شارك نموذجك",
    "Email your exported file (or a link to it) along with a short description of the model, any historical info you know, and your name to":
        "أرسل الملف المصدَّر (أو رابطًا له) مع وصف قصير للنموذج وأي معلومات تاريخية تعرفها واسمك إلى",
    "For large files, share a Google Drive, Dropbox, or WeTransfer link.":
        "للملفات الكبيرة، شارك رابط Google Drive أو Dropbox أو WeTransfer.",
    "✅ Tips for Great Scans": "✅ نصائح لمسح متقن",
    "Scan slowly and steadily": "امسح ببطء وثبات",
    "Avoid people or shadows in your scan": "تجنّب الأشخاص والظلال في المسح",
    "Focus on texture and angles, walk around the object fully": "اهتم بالملمس والزوايا — دُر حول الشيء دورة كاملة",
    "Natural daylight is good, but harsh sun causes glare — avoid scanning at noon":
        "ضوء النهار الطبيعي جيد، لكن الشمس القاسية تسبب وهجًا — تجنّب المسح عند الظهيرة",

    # ---- splats ----
    "<title>Splats With Phones – TANIT XR</title>": "<title>Splats With Phones – TANIT XR</title>",
    "This 6-week online course introduces splats using smartphones, taught by <b>Mark Jeffcock</b>.":
        "دورة على الإنترنت مدتها 6 أسابيع للتعريف بتقنية الـ Splats باستخدام الهواتف الذكية، يقدّمها <b>مارك جيفكوك</b>.",
    "Participants will learn how to capture real-world objects using a phone, turn them into 3D models and Gaussian splats, and review scans together in an immersive learning environment.":
        "سيتعلم المشاركون كيفية التقاط أشياء من العالم الحقيقي بالهاتف، وتحويلها إلى نماذج ثلاثية الأبعاد وGaussian splats، ومراجعة النماذج معًا في بيئة تعلّم غامرة.",
    "The cohort meets once a week at 7PM Tunisia Time (2PM Eastern) for 1 hour, for 6 weeks. No prior experience is required. Attendance and engagement matter more than technical background.":
        "تجتمع المجموعة مرة في الأسبوع في السابعة مساءً بتوقيت تونس (الثانية ظهرًا بالتوقيت الشرقي) لمدة ساعة، على مدى 6 أسابيع. لا يُشترط أي خبرة سابقة؛ فالحضور والتفاعل أهم من الخلفية التقنية.",
    "Due to limited spots, we review applications holistically based on availability, background, and motivation. More details are shared with accepted participants.":
        "نظرًا لمحدودية الأماكن، نراجع الطلبات مراجعة شاملة حسب التفرغ والخلفية والدافع. وتُشارك التفاصيل الإضافية مع المقبولين.",
    "<b>Want to join the next cohort?</b> Email": "<b>هل تريد الانضمام إلى الدفعة القادمة؟</b> راسل",
    "with your name, time zone, a short bio, why you want to join, and whether you can attend at least 5 of the 6 live sessions.":
        "مع ذكر اسمك ومنطقتك الزمنية ونبذة قصيرة عنك وسبب رغبتك في الانضمام، وما إذا كان بإمكانك حضور 5 جلسات على الأقل من أصل 6.",

    # ---- el jem ----
    "<title>El Jem Conference – TANIT XR</title>": "<title>مؤتمر الجم – TANIT XR</title>",
    "<h1>El Jem Conference</h1>": "<h1>مؤتمر الجم</h1>",
    "&nbsp;›&nbsp; El Jem Conference</div>": "&nbsp;›&nbsp; مؤتمر الجم</div>",
    "Download the full paper": "حمّل الورقة كاملة",

    # ---- unique mappers ----
    "<title>TanitXR &amp; the Unique Mappers – TANIT XR</title>": "<title>TanitXR وUnique Mappers – TANIT XR</title>",
    "<h1>TanitXR &amp; the Unique Mappers</h1>": "<h1>TanitXR وشبكة Unique Mappers</h1>",
    "&nbsp;›&nbsp; TanitXR &amp; the Unique Mappers</div>": "&nbsp;›&nbsp; TanitXR وشبكة Unique Mappers</div>",
    "TanitXR is a project, fiscally sponsored by Florida Community Innovation, that empowers volunteers and students to scan at-risk heritage sites. The goal is not only to digitally preserve these places, but also to increase appreciation for them by bringing them into XR environments and experiences.":
        "تانيت XR مشروع، برعاية مالية من Florida Community Innovation، يمكّن المتطوعين والطلاب من مسح مواقع تراثية مهددة. والهدف ليس حفظ هذه الأماكن رقميًا فحسب، بل أيضًا تعزيز تقديرها بإدخالها في بيئات وتجارب الواقع الممتد.",
    "<b>The pilot country is Tunisia, and now we are excited to expand to Nigeria with the help of the Unique Mappers!</b>":
        "<b>البلد الرائد هو تونس، ويسعدنا الآن التوسّع إلى نيجيريا بمساعدة شبكة Unique Mappers!</b>",
    ">Linked here is a PDF with background on TanitXR’s mission</a>. Read on to learn about the Unique Mappers and the scope of the TanitXR collaboration.":
        ">هنا ملف PDF يعرّف بمهمة تانيت XR</a>. تابع القراءة للتعرف على Unique Mappers ونطاق التعاون مع تانيت XR.",
    "About the Unique Mappers": "عن شبكة Unique Mappers",
    "The Unique Mappers Network was founded in 2017 by Victor Sunday during his PhD studies at the University of Nigeria, Enugu. Initially, the network focused on geographic information systems (GIS) and crowdsourcing through":
        "تأسست شبكة Unique Mappers عام 2017 على يد فيكتور صنداي أثناء دراسته للدكتوراه في جامعة نيجيريا بإينوغو. ركّزت الشبكة في البداية على نظم المعلومات الجغرافية (GIS) والتعهيد الجماعي عبر",
    "with a goal of mapping streets and buildings.": "بهدف رسم خرائط الشوارع والمباني.",
    "Over time, it grew into a diverse community of more than 500 citizen scientists across Nigeria. They engage in participatory mapping projects for disaster response, humanitarian action, and research, with a specific focus on Sustainable Development Goals (SDGs).":
        "ومع الوقت، نمت لتصبح مجتمعًا متنوعًا يضم أكثر من 500 عالِم مواطن في أنحاء نيجيريا، يشاركون في مشاريع خرائط تشاركية للاستجابة للكوارث والعمل الإنساني والبحث، مع تركيز خاص على أهداف التنمية المستدامة.",
    "What sets the Unique Mappers apart is their ability to mobilize volunteers from diverse backgrounds—including students, women, and youth—for impactful mapping projects.":
        "ما يميّز Unique Mappers هو قدرتها على حشد متطوعين من خلفيات متنوعة — من طلاب ونساء وشباب — لمشاريع خرائط مؤثرة.",
    "They’ve expanded their scope to include efforts like mapping flood-affected regions, monitoring oil spills, and even mapping stalled blood vessels in the brain to support Alzheimer’s research through the":
        "وسّعوا نطاق عملهم ليشمل رسم خرائط المناطق المتضررة من الفيضانات ورصد التسربات النفطية، وحتى رسم خرائط الأوعية الدموية المتعطلة في الدماغ لدعم أبحاث الزهايمر عبر مشروع",
    ">Learn more about their citizen science work</a>.": ">اعرف المزيد عن عملهم في علم المواطن</a>.",
    "Unique Mappers &amp; TanitXR Collaboration": "التعاون بين Unique Mappers وTanitXR",
    "Unique Mappers volunteers are receiving a $500 mini-grant from Florida Community Innovation, TanitXR’s fiscal sponsor. Before the end of 2026, they will make at least 50 scans of heritage sites and help optimize them, optionally joining weekly stand-up meetings on Thursdays at 5 PM WAT (emailing":
        "يتلقى متطوعو Unique Mappers منحة صغيرة قدرها 500 دولار من Florida Community Innovation، الراعي المالي لتانيت XR. وقبل نهاية 2026 سينجزون ما لا يقل عن 50 عملية مسح لمواقع تراثية ويساعدون في تحسينها، مع إمكانية الانضمام إلى اجتماعات أسبوعية أيام الخميس في الخامسة مساءً بتوقيت غرب أفريقيا (بمراسلة",
    "to receive the Zoom link).": "للحصول على رابط Zoom).",
    "The volunteers will:": "سيقوم المتطوعون بما يلي:",
    "Capture 3D scans of heritage sites using photogrammetry (": "التقاط نماذج ثلاثية الأبعاد لمواقع تراثية بتقنية القياس التصويري (",
    ">full scanning guide</a>). We plan to email the team behind": ">دليل المسح الكامل</a>). نخطط لمراسلة فريق",
    "and see what heritage sites they’re okay with us scanning, or if we need to do non-restricted heritage sites that are closer to the Unique Mappers’ homes. There are also potential partners like the":
        "لمعرفة المواقع التراثية التي يسمحون لنا بمسحها، أو ما إذا كان علينا الاكتفاء بمواقع غير مقيّدة أقرب إلى أماكن سكن المتطوعين. وهناك أيضًا شركاء محتملون مثل",
    "that we hope to speak with.": "نأمل التحدث معهم.",
    "Engage in 3D modeling, cultural preservation, and storytelling for an online gallery of Nigerian heritage":
        "المشاركة في النمذجة ثلاثية الأبعاد وصون الثقافة وسرد القصص لمعرض إلكتروني للتراث النيجيري",
    "Present their work in a global December 2026 webinar": "عرض أعمالهم في ندوة عالمية عبر الإنترنت في ديسمبر 2026",
    "<b>We are excited and the best is yet to come!</b>": "<b>نحن متحمسون، والأفضل قادم!</b>",

    # ---- immersegt ----
    "<title>ImmerseGT 2026 – TANIT XR</title>": "<title>ImmerseGT 2026 – TANIT XR</title>",
    "The pilot country for scanning is Tunisia, and contributors from around the world help turn these scans into immersive experiences.":
        "البلد الرائد في المسح هو تونس، ويساعد مساهمون من أنحاء العالم في تحويل هذه النماذج إلى تجارب غامرة.",
    ">The one-pager summarizing our mission is here</a>.": ">الملخص التعريفي بمهمتنا هنا</a>.",
    "<b>TanitXR sponsored a track at": "<b>رعت TanitXR مسارًا في",
    "from April 10–12!</b> Immerse GT was a 36-hour XR hackathon at Georgia Tech that brought together designers, developers, and storytellers to build immersive experiences. We gave a $300 prize to the winning team for our track.":
        "من 10 إلى 12 أفريل!</b> كان Immerse GT هاكاثون واقع ممتد لمدة 36 ساعة في جامعة جورجيا تك جمع مصممين ومطورين ورواة قصص لبناء تجارب غامرة. وقد قدّمنا جائزة 300 دولار للفريق الفائز في مسارنا.",
    "For our track, we invited participants to work with real TanitXR 3D models":
        "في مسارنا، دعونا المشاركين للعمل بنماذج TanitXR ثلاثية الأبعاد حقيقية",
    "and the models we have optimized so far:": "والنماذج التي حسّنّاها حتى الآن:",
    "We wanted them to create creative experiences that deepen appreciation for Tunisian heritage, which has been overlooked and misrepresented on the global stage.":
        "أردناهم أن يبتكروا تجارب تعمّق تقدير التراث التونسي الذي طالما أُهمل وشُوّه تمثيله على الساحة العالمية.",
    "We are interested in projects that help people explore, understand, or care about heritage in new ways. That might mean immersion, storytelling, education, interaction, public contribution, or something none of us has thought of yet.":
        "نهتم بالمشاريع التي تساعد الناس على استكشاف التراث أو فهمه أو الاهتمام به بطرق جديدة: الانغماس، أو السرد، أو التعليم، أو التفاعل، أو مساهمة الجمهور، أو شيء لم يخطر ببال أحد منا بعد.",
    "<h2>Background</h2>": "<h2>الخلفية</h2>",
    "Named for Tanit, the goddess of protection in ancient Carthage (where modern-day Tunisia now is), TanitXR was founded in 2025 by":
        "سُمّيت TanitXR على اسم تانيت، إلهة الحماية في قرطاج القديمة (تونس اليوم)، وقد أسّستها عام 2025",
    ", a Tunisian XR developer, to preserve the historic ruins she grew up loving.":
        "، وهي مطوّرة واقع ممتد تونسية، لصون الآثار التاريخية التي نشأت على حبها.",
    "The project focuses on places that are slowly deteriorating due to climate exposure, rising seas, extreme weather, development, and lack of preservation resources. After local volunteers scan objects and landscapes with photogrammetry and publish them as interactive models, the global community helps create a permanent digital record that can be explored online and increase appreciation of shared human heritage in Tunisia.":
        "يركّز المشروع على أماكن تتدهور ببطء بفعل التعرض المناخي وارتفاع مستوى البحر والطقس المتطرف والعمران ونقص موارد الصون. بعد أن يمسح المتطوعون المحليون الأشياء والمناظر بتقنية القياس التصويري وينشروها كنماذج تفاعلية، يساعد المجتمع العالمي في إنشاء سجل رقمي دائم يمكن استكشافه عبر الإنترنت ويعزز تقدير التراث الإنساني المشترك في تونس.",
    "Fundamentally, this work involves teaching people how to document heritage themselves. Tunisian and other students, artists, and volunteers learn to use accessible tools such as smartphone scanning to capture objects and spaces in their communities. The result is both a growing archive of Tunisian heritage and a participatory process that connects people – both locally in Tunisia and on the global stage – with historical sites.":
        "في جوهره، يقوم هذا العمل على تعليم الناس توثيق التراث بأنفسهم. يتعلم طلاب وفنانون ومتطوعون، من تونس وغيرها، استخدام أدوات في المتناول مثل المسح بالهاتف الذكي لالتقاط الأشياء والفضاءات في مجتمعاتهم. والنتيجة أرشيف متنامٍ للتراث التونسي وعملية تشاركية تربط الناس – محليًا في تونس وعالميًا – بالمواقع التاريخية.",
    "Dr. Caroline Nickerson’s Workshop at Immerse GT": "ورشة الدكتورة كارولين نيكرسون في Immerse GT",
    "As part of the event,": "في إطار الفعالية،",
    ", led a workshop connected to the TanitXR track on Saturday, April 11, at 2 PM ET in ISyE Main 228.":
        " قدّمت ورشة مرتبطة بمسار TanitXR يوم السبت 11 أفريل في الثانية ظهرًا بالتوقيت الشرقي في قاعة ISyE Main 228.",
    "The workshop focused on citizen science, public participation, and XR. TanitXR’s model focuses on community empowerment, and Caroline shared best practices and lessons learned from all her involvements.":
        "ركّزت الورشة على علم المواطن والمشاركة العامة والواقع الممتد. يقوم نموذج TanitXR على تمكين المجتمع، وقد شاركت كارولين أفضل الممارسات والدروس المستفادة من مختلف تجاربها.",
    "ImmerseGT 2026 Results": "نتائج ImmerseGT 2026",
    "We were thrilled to see so many creative submissions for the TanitXR track at ImmerseGT 2026. All participants had a chance to explore powerful ways to use immersive technology to preserve, interpret, and share Tunisian heritage with global audiences.":
        "سعدنا برؤية هذا الكم من المشاركات الإبداعية في مسار TanitXR بـ ImmerseGT 2026. أتيحت لجميع المشاركين فرصة استكشاف طرق قوية لاستخدام التقنيات الغامرة لصون التراث التونسي وتفسيره ومشاركته مع جمهور عالمي.",
    "<b>Track Winner:": "<b>الفائز بالمسار:",
    "From Mystery to History was selected as the winner of the TanitXR track for its innovative use of XR, generative AI, and photogrammetry to reimagine cultural heritage preservation.":
        "فاز مشروع From Mystery to History بمسار TanitXR لاستخدامه المبتكر للواقع الممتد والذكاء الاصطناعي التوليدي والقياس التصويري لإعادة تصور صون التراث الثقافي.",
    "The project stood out for its creativity, strong execution, and meaningful alignment with TanitXR’s mission to preserve and share Tunisia’s historical legacy through immersive experiences. We are incredibly proud of the team and excited to see how this project continues to evolve!":
        "تميّز المشروع بإبداعه وتنفيذه المتقن وتوافقه العميق مع مهمة TanitXR في صون الإرث التاريخي التونسي ومشاركته عبر تجارب غامرة. نحن فخورون جدًا بالفريق ومتشوقون لرؤية تطور هذا المشروع!",
    "Other projects from the TanitXR Track also demonstrated XR’s incredible potential to bring heritage preservation to life. We are deeply grateful to every participant who contributed ideas, creativity, and passion to this challenge.":
        "أظهرت مشاريع أخرى من مسار TanitXR أيضًا الإمكانات المذهلة للواقع الممتد في إحياء صون التراث. نحن ممتنون بعمق لكل مشارك أسهم بأفكاره وإبداعه وشغفه في هذا التحدي.",
    ">Review submissions here</a>.": ">استعرض المشاركات هنا</a>.",
    "Stay Involved After the Hackathon": "واصل المشاركة بعد الهاكاثون",
    "TanitXR is not just a hackathon prompt. It is an active and growing project, and we would love to stay connected with participants who want to keep building with us after ImmerseGT.":
        "TanitXR ليست مجرد موضوع هاكاثون، بل مشروع نشط ومتنامٍ، ويسعدنا البقاء على تواصل مع المشاركين الراغبين في مواصلة البناء معنا بعد ImmerseGT.",
    "There are many ways to contribute. Some volunteers help with photogrammetry and scanning. Others help with research, writing, interpretation, outreach, or immersive development. If you are interested in staying involved, sign up through our":
        "هناك طرق كثيرة للمساهمة: بعض المتطوعين يساعدون في القياس التصويري والمسح، وآخرون في البحث أو الكتابة أو التفسير أو التواصل أو التطوير الغامر. إذا كنت مهتمًا بمواصلة المشاركة، سجّل عبر",
    ">volunteer page</a>.": ">صفحة التطوع</a>.",
    "We are always excited to work with people who care about heritage, storytelling, participation, and the future of immersive technology.":
        "يسعدنا دائمًا العمل مع أشخاص يهتمون بالتراث والسرد والمشاركة ومستقبل التقنيات الغامرة.",

    # ---- about ----
    "<title>About – TANIT XR</title>": "<title>من نحن – TANIT XR</title>",
    "<h1>About</h1>": "<h1>من نحن</h1>",
    "&nbsp;›&nbsp; About</div>": "&nbsp;›&nbsp; من نحن</div>",
    "Our Impact So Far": "أثرنا حتى الآن",
    "Tanit XR is a community effort to save Tunisia’s heritage from climate change, erosion, and neglect. Together, we’re building a digital archive to protect it for generations.":
        "تانيت XR جهد مجتمعي لإنقاذ تراث تونس من التغيّر المناخي والتعرية والإهمال. معًا، نبني أرشيفًا رقميًا لحمايته لأجيال قادمة.",
    "We Are A Non-Profit Organization": "نحن منظمة غير ربحية",
    "Tanit XR operates under fiscal sponsorship with Florida Community Innovation (FCI), a U.S. 501(c)(3) nonprofit. This partnership allows us to accept tax-deductible donations while we grow toward becoming a fully independent nonprofit organization.":
        "تعمل تانيت XR تحت الرعاية المالية لمنظمة Florida Community Innovation ‏(FCI)، وهي منظمة أمريكية غير ربحية 501(c)(3). تتيح لنا هذه الشراكة قبول تبرعات معفاة من الضرائب بينما ننمو نحو منظمة غير ربحية مستقلة تمامًا.",
    "Our mission is to preserve Tunisia’s endangered heritage through digital scans, immersive technology, and education. With every artifact we scan and every volunteer we train, we are proving that heritage can be safeguarded for future generations — no matter the threats of climate change and neglect.":
        "مهمتنا صون تراث تونس المهدد عبر المسح الرقمي والتقنيات الغامرة والتعليم. فمع كل قطعة نمسحها وكل متطوع ندرّبه، نثبت أن التراث يمكن حمايته للأجيال القادمة — مهما كانت تهديدات التغيّر المناخي والإهمال.",
    "Tanit XR advances <b>Sustainable Development Goal 11.4</b>, which focuses on safeguarding cultural and natural heritage. We view the Sustainable Development Goals as an important shared framework for linking local action to global impact.":
        "تسهم تانيت XR في تحقيق <b>الغاية 11.4 من أهداف التنمية المستدامة</b> المعنية بحماية التراث الثقافي والطبيعي. ونرى في أهداف التنمية المستدامة إطارًا مشتركًا مهمًا يربط العمل المحلي بالأثر العالمي.",
    "Why I Started Tanit XR": "لماذا أسّست تانيت XR",
    "I grew up walking past the ruins of Carthage every day. To me, they were just there – a backdrop of my childhood. But slowly I began to notice how pieces were missing, how mosaics cracked and crumbled, how nothing was truly protected. Tunisia’s history is not kept in vaults or guarded museums. It is left in the open air, vulnerable to time, weather, and neglect. And every year, more of it disappears.":
        "نشأتُ وأنا أمرّ كل يوم بآثار قرطاج. كانت بالنسبة لي مجرد خلفية لطفولتي. لكن شيئًا فشيئًا بدأت ألاحظ القطع المفقودة، والفسيفساء المتشققة المتفتتة، وغياب أي حماية حقيقية. تاريخ تونس لا يُحفظ في خزائن أو متاحف محروسة، بل متروك في العراء، عرضة للزمن والمناخ والإهمال. وكل عام يختفي منه المزيد.",
    "Tanit XR was born from the fear of losing this history forever and the belief that technology can change the story. With 3D scanning, digital archiving, and immersive storytelling, we can preserve what remains and share it with the world. Each scan is more than just data; it is a memory, a voice from the past, a way of saying: we were here, and we matter.":
        "وُلدت تانيت XR من الخوف من ضياع هذا التاريخ إلى الأبد، ومن الإيمان بأن التكنولوجيا قادرة على تغيير القصة. بالمسح ثلاثي الأبعاد والأرشفة الرقمية والسرد الغامر، يمكننا صون ما تبقّى ومشاركته مع العالم. كل عملية مسح أكثر من مجرد بيانات؛ إنها ذاكرة، وصوت من الماضي، وطريقة لنقول: كنّا هنا، ونحن مهمون.",
    ", Founder</b>": "، المؤسِّسة</b>",
    "Join us to protect Tunisia’s Heritage": "انضم إلينا لحماية تراث تونس",
    "You don’t need to be an archaeologist or a technologist to make an impact. Our first scans were made with a phone. Whether on the ground in Tunisia or helping remotely, every volunteer contributes to preserving history.":
        "لست بحاجة لأن تكون عالِم آثار أو تقنيًا لتُحدث أثرًا. أولى عمليات المسح لدينا كانت بهاتف. سواء كنت في الميدان بتونس أو تساعد عن بُعد، كل متطوع يسهم في صون التاريخ.",

    # ---- contact ----
    "<title>Contact – TANIT XR</title>": "<title>اتصل بنا – TANIT XR</title>",
    "Send us your Questions/Feedback": "أرسل لنا أسئلتك وملاحظاتك",
    "We’ll get back to you as soon as we can.": "سنرد عليك في أقرب وقت ممكن.",
    ">Email Address</label>": ">البريد الإلكتروني</label>",
    ">Subject</label>": ">الموضوع</label>",
    ">Message</label>": ">الرسالة</label>",
    ">Send Message</button>": ">إرسال الرسالة</button>",
    ">Apply Now</a>": ">قدّم الآن</a>",
    "<b>Email:</b>": "<b>البريد الإلكتروني:</b>",
    "<b>Phone:</b>": "<b>الهاتف:</b>",

    # ---- support ----
    "<title>Support – TANIT XR</title>": "<title>ادعمنا – TANIT XR</title>",
    "<h1>Support</h1>": "<h1>ادعمنا</h1>",
    "&nbsp;›&nbsp; Support</div>": "&nbsp;›&nbsp; ادعمنا</div>",
    "As climate change, conflict, and neglect threaten historic sites like ancient ruins, our shared global heritage is at risk.":
        "مع تهديد التغيّر المناخي والنزاعات والإهمال للمواقع التاريخية كالآثار القديمة، أصبح تراثنا العالمي المشترك في خطر.",
    "XR—a term that includes augmented and virtual reality—offers powerful tools to help. XR offers a way to preserve disappearing heritage—by capturing sites in 3D, enriching visits with storytelling, and making global history accessible from anywhere.":
        "يوفّر الواقع الممتد — وهو مصطلح يشمل الواقع المعزز والافتراضي — أدوات قوية للمساعدة: طريقة لصون تراث آخذ في الاندثار، عبر التقاط المواقع بتقنية ثلاثية الأبعاد وإثراء الزيارات بالسرد وجعل تاريخ العالم في متناول الجميع من أي مكان.",
    "Named for the ancient Carthaginian goddess of protection and the moon, if we can protect heritage in Tunisia—using immersive technology, community storytelling, and local leadership—we can build a model to safeguard cultural sites around the world.":
        "سُمّينا على اسم إلهة الحماية والقمر في قرطاج القديمة. إذا استطعنا حماية التراث في تونس — بالتقنيات الغامرة والسرد المجتمعي والقيادة المحلية — فبإمكاننا بناء نموذج لحماية المواقع الثقافية حول العالم.",
    ">DONATE HERE</a>": ">تبرّع هنا</a>",
    "Help cover basic costs for scanning a site: like transportation, mobile data for uploads, and backup storage.":
        "يساعد في تغطية التكاليف الأساسية لمسح موقع: كالنقل وبيانات الهاتف للرفع والتخزين الاحتياطي.",
    "Support detailed documentation of a site, enabling multiple 3D captures, archival research, and creating educational content to go with it.":
        "يدعم التوثيق المفصّل لموقع: عدة عمليات التقاط ثلاثية الأبعاد وبحثًا أرشيفيًا وإنشاء محتوى تعليمي مرافق.",
    "Sponsor a field day with collaborators, covering travel, meals, and shared equipment to scan and document endangered ruins. It also helps us start compensating local contributors for their time and expertise.":
        "يرعى يومًا ميدانيًا مع المتعاونين، ويغطي التنقل والوجبات والمعدات المشتركة لمسح الآثار المهددة وتوثيقها. كما يساعدنا في البدء بمكافأة المساهمين المحليين على وقتهم وخبرتهم.",
    "Fund a full digital storytelling package for one site, including high-quality 3D scans, animated walk-throughs, historical research, and immersive media production. This tier also supports the purchase of better scanning tools so we can scale beyond just a phone.":
        "يموّل حزمة سرد رقمي كاملة لموقع واحد: نماذج ثلاثية الأبعاد عالية الجودة وجولات متحركة وبحثًا تاريخيًا وإنتاج وسائط غامرة. يدعم هذا المستوى أيضًا شراء أدوات مسح أفضل لنتجاوز الاعتماد على الهاتف وحده.",
    "Donations are tax-deductible through our fiscal sponsor, Florida Community Innovation, a U.S. 501(c)(3) nonprofit.":
        "التبرعات معفاة من الضرائب عبر راعينا المالي Florida Community Innovation، وهي منظمة أمريكية غير ربحية 501(c)(3).",

    # ---- coming soon / privacy ----
    "<title>Coming Soon – TANIT XR</title>": "<title>قريبًا – TANIT XR</title>",
    "<h1>Coming Soon</h1>": "<h1>قريبًا</h1>",
    "&nbsp;›&nbsp; Coming Soon</div>": "&nbsp;›&nbsp; قريبًا</div>",
    "👀 Something exciting is on the way.": "👀 شيء مشوّق في الطريق.",
    "This page will be live soon! In the meantime, explore our archive of 3D scans or join the volunteer network helping to preserve Tunisia’s heritage.":
        "ستكون هذه الصفحة متاحة قريبًا! في هذه الأثناء، استكشف أرشيف نماذجنا ثلاثية الأبعاد أو انضم إلى شبكة المتطوعين التي تساعد في صون تراث تونس.",
    ">Back Home</a>": ">العودة إلى الرئيسية</a>",
    "<title>Privacy Policy – TANIT XR</title>": "<title>سياسة الخصوصية – TANIT XR</title>",
    "<h1>Privacy Policy</h1>": "<h1>سياسة الخصوصية</h1>",
    "&nbsp;›&nbsp; Privacy Policy</div>": "&nbsp;›&nbsp; سياسة الخصوصية</div>",
    "Tanit XR (“we”) runs tanitxr.org to share our heritage-preservation work. We collect as little personal information as possible.":
        "تدير تانيت XR («نحن») موقع tanitxr.org لمشاركة عملنا في صون التراث. ونجمع أقل قدر ممكن من المعلومات الشخصية.",
    "What we collect": "ما الذي نجمعه",
    "<b>Contact &amp; volunteer forms:</b> the name, email address, and message details you choose to send us. We use them only to reply to you and to coordinate volunteer work, and we don’t sell or share them.":
        "<b>نماذج الاتصال والتطوع:</b> الاسم والبريد الإلكتروني ومحتوى الرسائل التي تختار إرسالها إلينا. نستخدمها فقط للرد عليك وتنسيق العمل التطوعي، ولا نبيعها ولا نشاركها.",
    "<b>Volunteer profiles:</b> if you submit a profile for our Our People page, the name, role, bio, photo, and links you provide are published on this website after review. Email us at":
        "<b>ملفات المتطوعين:</b> إذا أرسلت ملفًا شخصيًا لصفحة فريقنا، فإن الاسم والدور والنبذة والصورة والروابط التي تقدمها تُنشر على هذا الموقع بعد المراجعة. راسلنا على",
    "any time to update or remove your profile.": "في أي وقت لتحديث ملفك أو حذفه.",
    "What we don’t do": "ما الذي لا نفعله",
    "No advertising or tracking cookies.": "لا ملفات تعريف إعلانية أو للتتبع.",
    "No sale of personal data.": "لا بيع للبيانات الشخصية.",
    "Third parties": "أطراف ثالثة",
    "This site is hosted on GitHub Pages, forms are delivered by FormSubmit, 3D models are embedded from Sketchfab, and donations are processed by Tuesday (on behalf of our fiscal sponsor, Florida Community Innovation). Each of these services has its own privacy policy.":
        "يُستضاف هذا الموقع على GitHub Pages، وتُرسل النماذج عبر FormSubmit، وتُضمَّن النماذج ثلاثية الأبعاد من Sketchfab، وتُعالج التبرعات عبر Tuesday (نيابة عن راعينا المالي Florida Community Innovation). ولكل من هذه الخدمات سياسة خصوصية خاصة بها.",
    "Questions? Contact": "لديك أسئلة؟ تواصل مع",

    # ---- opportunity submission form ----
    "Know an opportunity we should feature?": "هل تعرف فرصة تستحق النشر؟",
    "Send it our way — if it’s a fit, it will appear on this board and in the newsletter.":
        "أرسلها إلينا — وإذا كانت مناسبة، ستظهر على هذه اللوحة وفي النشرة.",
    ">Opportunity name</label>": ">اسم الفرصة</label>",
    ">Link</label>": ">الرابط</label>",
    ">Deadline (if you know it)</label>": ">الموعد النهائي (إن كنت تعرفه)</label>",
    ">Who is it for / anything we should know</label>": ">لمن هي / ما ينبغي أن نعرفه</label>",
    ">Your name or email (optional, so we can credit or thank you)</label>":
        ">اسمك أو بريدك الإلكتروني (اختياري، لنشكرك أو ننسب الفضل إليك)</label>",
    ">Submit Opportunity</button>": ">إرسال الفرصة</button>",

    # ---- newsletter subscribe band ----
    "Never miss a deadline": "لا تفوّت أي موعد نهائي",
    "Get new grants, residencies, and open calls for art, XR &amp; impact in your inbox — free, from the Tanit XR team. You’ll also be first to hear how our heritage-preservation work is going.":
        "احصل على أحدث المنح والإقامات الفنية والدعوات المفتوحة في الفن والواقع الممتد والأثر في بريدك — مجانًا من فريق تانيت XR. وستكون أيضًا أول من يعرف مستجدات عملنا في صون التراث.",
    'placeholder="you@example.com"': 'placeholder="you@example.com"',
    ">Subscribe Free</button>": ">اشترك مجانًا</button>",
    "No spam, opportunities and Tanit XR news only. Also published on": "لا رسائل مزعجة — فرص وأخبار تانيت XR فقط. تُنشر أيضًا على",

    # ---- volunteer reminders ----
    "🤝 This scan exists because of volunteers — from scanning on site to cleanup and research.":
        "🤝 هذا النموذج موجود بفضل المتطوعين — من المسح في الموقع إلى التنقيح والبحث.",
    ">Join us →</a>": ">انضم إلينا ←</a>",
    ">Volunteer →</a>": ">التطوع ←</a>",
    "Every scan here was made by a volunteer": "كل نموذج هنا صنعه متطوع",

    # ---- reorganized nav ----
    ">Get Involved</a>": ">شارك معنا</a>",
    ">Create Your Profile</a>": ">أنشئ ملفك الشخصي</a>",
    ">Scanning Guide</a>": ">دليل المسح</a>",

    # ---- added 2026-09-21: pages that were still English ----
    'before recording people, private spaces, ceremonies, sacred practices, or\npersonal stories. Tanit XR is not just preserving objects, we are preserving the worlds, memories, and\nmeanings around them.':
        'قبل تصوير الأشخاص أو الفضاءات الخاصة أو المراسم أو الممارسات المقدسة أو\nالقصص الشخصية. Tanit XR لا يحفظ القطع فقط، بل نحفظ العوالم والذكريات\nوالمعاني المحيطة بها.',
    'The museum is ours to build, room by room. Fund one gallery, from its walls to the objects inside and the stories Nura tells there, and it carries your name in the browser and in the headset.':
        'المتحف مِلكنا نبنيه قاعة بعد قاعة. مَوِّل قاعة واحدة، من جدرانها إلى القطع التي بداخلها والقصص التي ترويها Nura فيها، وستحمل اسمك في المتصفح وفي نظارة الواقع الافتراضي.',
    'Unity developers, 3D artists, sound designers and writers are\nbuilding this on Thursday calls. Donations pay for the tools and hosting that get it onto headsets and into classrooms.':
        'مطورو Unity وفنانو الأبعاد الثلاثة ومصممو الصوت والكتّاب\nيبنون هذا العمل في مكالمات الخميس. التبرعات تغطي الأدوات والاستضافة التي توصله إلى نظارات الواقع الافتراضي وإلى الفصول الدراسية.',
    'Walls, arches and courtyards are built from a kit of pre-made pieces designed by Patrick Molen, so volunteers can puzzle together a new gallery without starting from scratch.':
        'تُبنى الجدران والأقواس والأفنية من مجموعة قطع جاهزة صممها Patrick Molen، حتى يتمكن المتطوعون من تركيب قاعة جديدة كأحجية، دون البدء من الصفر.',
    'Beyond photogrammetry scans, our volunteers model Tunisian objects, pottery, lamps,\ntilework, everyday heritage, from scratch, for our virtual museum and community projects.':
        'إلى جانب المسوحات بالتصوير المجسّم، يصمّم متطوعونا من الصفر قطعًا تونسية، فخّارًا ومصابيح\nوزليجًا، تراث الحياة اليومية، من أجل متحفنا الافتراضي ومشاريعنا المجتمعية.',
    'Five halls of real heritage, scanned on location by volunteers with phones and cameras.\nEvery object here can be turned, zoomed and opened in full. Nothing is behind glass.':
        'خمس قاعات من تراث حقيقي، مسحها متطوعون في الموقع بهواتف وكاميرات.\nكل قطعة هنا يمكن إدارتها وتكبيرها وفتحها كاملة. لا شيء خلف زجاج.',
    'The sizes on the labels are the real ones. A full museum you can walk through is being\nbuilt separately by Patrick, Cam and the team, and every object here will hang in it.':
        'المقاسات المذكورة في البطاقات هي المقاسات الحقيقية. أما المتحف الكامل الذي يمكن التجول داخله فيبنيه\nبشكل منفصل Patrick وCam والفريق، وستُعرض فيه كل قطعة من هنا.',
    'What sets the Unique Mappers apart is their ability to mobilize volunteers from diverse\nbackgrounds, including students, women and youth, for impactful mapping projects.':
        'ما يميّز Unique Mappers هو قدرتهم على تعبئة متطوعين من خلفيات\nمتنوعة، من طلبة ونساء وشباب، لإنجاز مشاريع خرائط ذات أثر.',
    'An evening with the Tanit XR community, planned with TAYP, the Tunisian American Young Professionals. Save the date. Details will follow here and in the newsletter.':
        'أمسية مع مجتمع Tanit XR، بالتعاون مع TAYP، جمعية الشباب المهنيين التونسيين الأمريكيين. احجز التاريخ في مفكرتك. ستتبع التفاصيل هنا وفي النشرة البريدية.',
    'Everything on this site was made by volunteers, on\nThursday calls and weekend scanning trips. Whatever time you have, there is a piece of this that is yours to\ndo.':
        'كل ما في هذا الموقع أنجزه متطوعون، في\nمكالمات الخميس ورحلات المسح في عطلة نهاية الأسبوع. مهما كان الوقت المتاح لديك، هناك جزء من هذا العمل\nينتظرك.',
    'and tell us what you enjoy doing. Someone from the team writes back, adds you to Slack, and you meet everyone on the next Thursday call. That is the whole process.':
        'وأخبرونا بما تحبون القيام به. يرد عليكم أحد أعضاء الفريق ويضيفكم إلى Slack، فتلتقون بالجميع في مكالمة الخميس القادمة. هذه هي كل الخطوات.',
    'Two thousand years ago, families set these stones in the Tophet of Carthage. Many still carry the sign of Tanit, the goddess this whole project is named after':
        'قبل ألفي عام، نصبت عائلات هذه الحجارة في توفة قرطاج. وما زال كثير منها يحمل علامة تانيت، الإلهة التي حمل هذا المشروع كله اسمها',
    'Build out the virtual museum and save toward professional scanning gear such as the XGRIDS PortalCam, so the community can capture more than a phone allows.':
        'توسيع المتحف الافتراضي وادخار ما يلزم لاقتناء معدات مسح احترافية مثل XGRIDS PortalCam، حتى يتمكن المجتمع من التقاط ما يتجاوز قدرات الهاتف.',
    'Volunteers from Tunisia, the US, Europe and Nigeria meet every Thursday at 12 pm Eastern (5 pm Tunisia) to review scans, plan trips and help each other.':
        'يلتقي متطوعون من تونس والولايات المتحدة وأوروبا ونيجيريا كل خميس على الساعة 12 ظهرا بتوقيت شرق الولايات المتحدة (5 مساء بتوقيت تونس) لمراجعة عمليات المسح والتخطيط للرحلات ومساعدة بعضهم البعض.',
    'Volunteers who have never been to Tunisia learn its history while modeling lamps, pottery and plants for our virtual museum, and we learn about theirs.':
        'متطوعون لم يزوروا تونس قط يتعرفون على تاريخها وهم ينمذجون المصابيح والفخار والنباتات لمتحفنا الافتراضي، ونتعرف نحن بدورنا على تاريخهم.',
    'The Unique Mappers Network (500+ citizen scientists) is replicating the Tanit XR model in Nigeria with a mini-grant from our fiscal sponsor.':
        'تقوم شبكة Unique Mappers (أكثر من 500 عالم مواطن) باستنساخ نموذج Tanit XR في نيجيريا بمنحة صغيرة من الراعي المالي لمشروعنا.',
    'Every object here, one at a time, in your browser. Turn it with a finger, hear its story\nfrom Nura, save and share it, or put on a headset.':
        'كل قطعة هنا، واحدة تلو الأخرى، في متصفحك. أدرها بإصبعك، واستمع إلى قصتها\nمن Nura، واحفظها وشاركها، أو ارتدِ نظارة الواقع الافتراضي.',
    'Mosaics from the Roman villas of Carthage. Somebody set every one of these little stones by hand, and people walked over them for centuries':
        'فسيفساء من الفيلات الرومانية بقرطاج. وضع أحدهم كل حجرة صغيرة منها بيده، ومشى الناس فوقها قرونا',
    'Punic stelae, Roman statues and mosaics, doors and tilework from the medina, the same scans you find in our open archive, placed life-size.':
        'نُصب بونية وتماثيل وفسيفساء رومانية وأبواب وزليج من المدينة العتيقة بتونس، وهي نفس المسوحات الموجودة في أرشيفنا المفتوح، معروضة بحجمها الطبيعي.',
    'Run a free workshop or course session for the community, Splats With Phones, history lessons, mentoring and interview prep for students.':
        'قدّموا ورشة أو حصة تكوين مجانية للمجتمع: Splats With Phones، دروس تاريخ، إرشاد، وتحضير للمقابلات لفائدة الطلبة.',
    'Most were captured with a phone. The halls are\nalso being rebuilt as a real space you can walk in VR, room by room, by the same team.':
        'أغلبها التُقط بهاتف. كما يُعاد بناء القاعات\nكفضاء حقيقي يمكنك التجول فيه بالواقع الافتراضي، قاعة بعد قاعة، على يد الفريق نفسه.',
    'Impact you can point at: every gallery, experience and piece your support made possible is public, in 3D, with your name beside it.':
        'أثر يمكنك أن تشير إليه: كل قاعة وكل تجربة وكل قطعة أتاحها دعمك متاحة للعموم، بالأبعاد الثلاثة، واسمك إلى جانبها.',
    'Nathan Bowser interviewed Ines Said for Niantic Spatial about Tanit XR and our Scaniverse capture of the amphitheatre of El Jem.':
        'أجرى Nathan Bowser حوارا مع Ines Said لفائدة Niantic Spatial حول Tanit XR وعملية التقاطنا بـScaniverse لمدرّج الجم.',
    'Our paper on digital documentation, XR and citizen science for community-driven heritage preservation, presented in April 2026.':
        'بحثنا حول التوثيق الرقمي والواقع الممتد والعلوم التشاركية من أجل حفظ التراث بقيادة المجتمعات، قُدّم في أبريل 2026.',
    'Feature on how Tanit XR uses photogrammetry, Scaniverse and Gaussian splatting to build an open archive of Tunisian heritage.':
        'تقرير عن كيفية استخدام Tanit XR للمسح التصويري وScaniverse والسبلات الغاوسي لبناء أرشيف مفتوح للتراث التونسي.',
    'Tell us about your team and what matters to you. We come back with two or three ways to work together, with real numbers.':
        'حدّثونا عن فريقكم وعمّا يهمّكم. نعود إليكم بطريقتين أو ثلاث للعمل معا، بأرقام حقيقية.',
    'Doors and tilework from Tunis and Kairouan that still open and close every day. This is heritage people live inside':
        'أبواب وزليج من تونس والقيروان لا تزال تُفتح وتُغلق كل يوم. هذا تراث يعيش الناس داخله',
    'Lamps, pottery and plants modeled by volunteers furnish the rooms. Optimized scans keep it light enough for phones.':
        'مصابيح وفخّار ونباتات صمّمها متطوعون تؤثث القاعات. والمسوحات المحسّنة تبقي التجربة خفيفة بما يكفي للهواتف.',
    'Kent Bye interviewed Ines Said at AWE USA 2026 about phone-based reality capture, volunteers and heritage at risk.':
        'أجرى Kent Bye حوارا مع Ines Said في AWE USA 2026 حول التقاط الواقع بالهاتف، والمتطوعين، والتراث المهدَّد.',
    'Tanit XR, Volunteer to help protect global heritage. Cultural memory powered by volunteers and digital technology.':
        'Tanit XR، تطوّع للمساهمة في حماية التراث العالمي. ذاكرة ثقافية يحملها المتطوعون والتقنيات الرقمية.',
    'Ines Said spoke at Augmented World Expo USA 2026 in Long Beach, California, on XR for social impact and heritage.':
        'تحدثت Ines Said في Augmented World Expo USA 2026 بمدينة لونغ بيتش في كاليفورنيا عن الواقع الممتد في خدمة الأثر الاجتماعي والتراث.',
    'The technique is the easy part. Our guide also covers asking permission and\ntaking care of the place you are in.':
        'التقنية هي الجزء السهل. دليلنا يشرح أيضا كيف تطلب الإذن وكيف\nتعتني بالمكان الذي أنت فيه.',
    'We sponsored a heritage track and a $300 prize; Dr. Caroline Nickerson led a workshop on citizen science and XR.':
        'رعينا مسارا خاصا بالتراث وجائزة قدرها 300 دولار، وقادت Dr. Caroline Nickerson ورشة حول العلوم التشاركية والواقع الممتد.',
    'Cover a month of hosting and software for the open archive and the volunteers who optimize and publish models.':
        'غطّوا شهرا من الاستضافة والبرمجيات للأرشيف المفتوح وللمتطوعين الذين يحسّنون النماذج وينشرونها.',
    'It has landed in the Tanit XR inbox and a volunteer will read it soon. We usually reply within a few days.':
        'وصلت رسالتك إلى بريد Tanit XR وسيقرؤها أحد المتطوعين قريبًا. نردّ عادة في غضون أيام قليلة.',
    'Sound is on. Tap to mute. Music: Oriental Nights by Ahmad Al-Nakib (CC BY 3.0, via the Internet Archive)':
        'الصوت مفعّل. انقر لكتمه. الموسيقى: Oriental Nights لـ Ahmad Al-Nakib (CC BY 3.0، عبر Internet Archive)',
    'Where Tanit XR has been recognized, featured and heard. For\ninterviews, talks or media requests write to':
        'أين حظيت Tanit XR بالتقدير والتغطية والاهتمام. لطلبات\nالمقابلات أو المحاضرات أو وسائل الإعلام راسلونا على',
    'Columns and capitals from the temples, baths and villas. The roofs are long gone. These stayed standing':
        'أعمدة وتيجان أعمدة من المعابد والحمامات والفيلات. السقوف اختفت منذ زمن بعيد. أما هذه فبقيت واقفة',
    'A member of the team welcomes you, and you meet everyone on the next call, Thursdays at 12 pm Eastern.':
        'يستقبلك أحد أعضاء الفريق، ثم تلتقي بالجميع في المكالمة القادمة، كل خميس على الساعة 12 ظهرًا بتوقيت شرق الولايات المتحدة.',
    'Ambient sound recorded at the real places, wind, footsteps, echoes, so each gallery feels different.':
        'أصوات محيطة مسجلة في الأماكن الحقيقية، الريح والخطوات والأصداء، حتى تبدو كل قاعة مختلفة عن الأخرى.',
    'Optimize a scan, write the history of an object, model something Tunisian, or plan a scanning trip.':
        'حسّن عملية مسح، أو اكتب تاريخ قطعة، أو أنجز نموذجا لشيء تونسي، أو خطّط لرحلة مسح.',
    ', bakeries, workshops, markets, gathering places, family heirlooms, gardens, and community spaces':
        '، المخابز والورشات والأسواق وأماكن التجمّع وموروثات العائلة والحدائق والفضاءات المشتركة',
    'New Neapolis Site Revealed By Recent Floods(Storm Harry) In Tunisia. Scanned by Youssef Lakdhar!.':
        'موقع جديد في نيابوليس كشفت عنه الفيضانات الأخيرة (عاصفة هاري) في تونس. مسحه Youssef Lakdhar!.',
    ', pottery, tools, carvings, statues, tiles, jewelry, textiles, inscriptions, and household items':
        '، فخار وأدوات ومنحوتات وتماثيل وزليج وحلي ومنسوجات ونقوش وأدوات منزلية',
    'Ines Said on why Tanit XR exists and where it is going, published in the Women Write collection.':
        'Ines Said تتحدث عن سبب وجود Tanit XR وعن وجهتها، ضمن مجموعة Women Write.',
    'Medium / Women Write, Tanit XR: Preserving Tunisia&#x27;s Heritage Through Immersive Technology':
        'Medium / Women Write، Tanit XR: صون التراث التونسي بالتقنيات الغامرة',
    'The virtual museum in March 2026: a domed hall with striped arches, tiled floors and a fountain':
        'المتحف الافتراضي في مارس 2026: قاعة بقبة وأقواس مخططة وأرضيات مبلطة ونافورة',
    'Portfolio reviews, mock interviews and career advice for students and early-career volunteers.':
        'مراجعة الملفات الفنية ومقابلات تجريبية ونصائح مهنية للطلبة والمتطوعين في بداية مسارهم.',
    'The second wing of the virtual museum under construction, a colonnade and galleries in greybox':
        'الجناح الثاني من المتحف الافتراضي قيد الإنشاء، رواق أعمدة وقاعات في مرحلة النماذج الأولية',
    'A 6-week course with Mark Jeffcock on capturing 3D models and Gaussian splats with a phone.':
        'دورة على مدى 6 أسابيع مع Mark Jeffcock حول التقاط النماذج ثلاثية الأبعاد وسحب غاوس بالهاتف.',
    'Pick one, or shape one with us. We build each partnership around your team and your budget.':
        'اختاروا واحدة، أو لنصممها معا. نبني كل شراكة حول فريقكم وميزانيتكم.',
    'A loom, a carpet. Nothing grand, just what people used, which is exactly why we kept them':
        'نول وسجادة. لا شيء فخم، مجرد ما كان الناس يستعملونه، ولهذا بالضبط حفظناهما',
    'Two hands holding a phone that shows the Draped Statue of Byrsa Hill in augmented reality':
        'يدان تمسكان هاتفا يعرض التمثال المكسوّ بالثوب من تل بيرصا بالواقع المعزّز',
    'Latin and Arabic inscriptions, every letter cut by hand. Some of them can still be read':
        'نقوش لاتينية وعربية، كل حرف منها محفور باليد. وبعضها لا يزال مقروءا',
    'What you do, what you are studying, or any communities or projects you are involved in.':
        'ما تعملونه، أو ما تدرسونه، أو أي مجتمعات ومشاريع تشاركون فيها.',
    ', patterns, textures, symbols, damage, repairs, maker’s marks, or decorative elements':
        '، أنماط، ملامس، رموز، أضرار، ترميمات، علامات الصانع، أو عناصر زخرفية',
    'Every share helps more people see this. Pick where it goes, the caption comes along.':
        'كل مشاركة تساعد عددًا أكبر من الناس على رؤية هذا. اختر وجهة النشر، والتعليق يرافقه.',
    "Send it our way, if it's a fit, it will appear on this board\nand in the newsletter.":
        'أرسلوها إلينا، وإن كانت مناسبة فستظهر على هذه اللوحة\nوفي النشرة البريدية.',
    'Carthage Magazine, Preserving Tunisia&#x27;s Heritage Through Immersive Technology':
        'Carthage Magazine، الحفاظ على التراث التونسي عبر التقنيات الغامرة',
    'Material and Meaning: Marble Identity, and Cultural Exchange in Ancient Carthage':
        'المادة والمعنى: الرخام والهوية والتبادل الثقافي في قرطاج القديمة',
    'A tagine and a plate: the everyday Tunisia our volunteers wanted in the museum':
        'طاجين وصحن: تونس اليومية التي أراد متطوعونا وجودها في المتحف',
    'Music: Oriental Nights by Ahmad Al-Nakib (CC BY 3.0, via the Internet Archive)':
        'الموسيقى: Oriental Nights لأحمد النقيب (CC BY 3.0، عبر Internet Archive)',
    'Succulents, a cactus, clay pots and palms for the museum&#x27;s courtyards':
        'نباتات عصارية وصبار وأوانٍ فخارية ونخيل لأفنية المتحف',
    'The virtual museum courtyard with a pool, terraces and a sculpted canopy':
        'فناء المتحف الافتراضي ببركة وشرفات ومظلة منحوتة',
    'Voices of VR #1728, Preserving Tunisian Cultural Heritage with Tanit XR':
        'Voices of VR #1728، حفظ التراث الثقافي التونسي مع Tanit XR',
    'Carved Architectural Blocks with Laurel Motifs, Water Temple, Zaghouan':
        'كتل معمارية منقوشة بزخارف الغار، معبد المياه، زغوان',
    'Carved Architectural Block with Laurel Motifs, Water Temple, Zaghouan':
        'كتلة معمارية منحوتة بزخارف الغار، معبد المياه، زغوان',
    'El Jem Conference 2026, Paper in English, French and Tunisian Arabic':
        'مؤتمر الجم 2026، ورقة بالإنجليزية والفرنسية والعربية التونسية',
    'Second wing under construction, colonnade and galleries in greybox.':
        'الجناح الثاني قيد الإنشاء، رواق الأعمدة والقاعات في مرحلة النماذج الأولية (greybox).',
    'Not Your Grandma’s Gallery – Open Call for Artists (The Holy Art)':
        'Not Your Grandma’s Gallery – دعوة مفتوحة للفنانين (The Holy Art)',
    'The murex shell whose dye made Carthage rich and its cloth purple':
        'صدفة الموركس التي أثرت صبغتها قرطاج وصبغت أقمشتها بالأرجوان',
    'Used only to contact you about your profile, it is not published.':
        'يُستعمل فقط للتواصل معك بخصوص ملفك الشخصي، ولا يُنشر.',
    'An amphora wearing a graduation cap, with a book titled Carthage':
        'جرة أمفورا تعتمر قبعة التخرج، وإلى جانبها كتاب عنوانه قرطاج',
    'Looking for a specific scan, a\ndownload or the game-ready twins?':
        'تبحث عن مسح معيّن أو\nملف للتنزيل أو النسخ الجاهزة للألعاب؟',
    'A globe with Tanit XR volunteers standing on every continent':
        'كرة أرضية يقف عليها متطوعو Tanit XR في كل قارة',
    'VIVERSE Creator Program – Creator Grants for WebXR Worlds':
        'برنامج VIVERSE للمبدعين – منح لصنّاع عوالم WebXR',
    'UNESCO Youth Climate Action Network – YoU-CAN Membership':
        'شبكة اليونسكو للعمل المناخي الشبابي – عضوية YoU-CAN',
    'Inscribed Architectural Fragment – Byrsa Hill, Carthage':
        'شظية معمارية منقوشة – تل بيرصا، قرطاج',
    'CityCamp Gainesville Hack Day 2026, heritage challenge':
        'CityCamp Gainesville Hack Day 2026، تحدي التراث',
    'Courtyard with pool, terraces and the sculpted canopy.': 'فناء ببركة وشرفات ومظلة منحوتة.',
    'TanitXR &amp; the Unique Mappers, expanding to Nigeria':
        'TanitXR وUnique Mappers، التوسّع إلى نيجيريا',
    'Documentation numérique, XR et science participative.':
        'التوثيق الرقمي والواقع الممتد والعلوم التشاركية.',
    'Games for Change 2026 Student Challenge (Competition)':
        'تحدي الطلبة Games for Change 2026 (مسابقة)',
    'Mini history lesson 2, Carthage&#x27;s craft quarters':
        'درس تاريخ مصغر 2، الأحياء الحرفية بقرطاج',
    'Volunteer with Tanit XR, Preserve Heritage in 3D & XR':
        'تطوّعوا مع Tanit XR، واحفظوا التراث بالثلاثي الأبعاد وتقنيات XR',
    'Traditional Loom with Woven Carpet – Medina of Tunis':
        'نول تقليدي مع سجادة منسوجة – المدينة العتيقة بتونس',
    'ImmerseGT at Georgia Tech, sponsored heritage track':
        'ImmerseGT في جورجيا تك، مسار تراثي برعاية',
    'Morgan-Menil Fellowship 2026-27 (Drawing Institute)':
        'زمالة Morgan-Menil 2026-27 (Drawing Institute)',
    'Traditional Loom with Woven Carpet, Medina of Tunis':
        'منسج تقليدي مع زربية منسوجة، المدينة العتيقة بتونس',
    'CityCamp Gainesville Hack Day: two Tanit XR tracks':
        'CityCamp Gainesville Hack Day: مساران لـ Tanit XR',
    'Decorated Bust Fragment – Roman Villas of Carthage':
        'شظية تمثال نصفي مزخرف – الفيلات الرومانية بقرطاج',
    'Bird and Floral Mosaic – Roman Villas of Carthage':
        'فسيفساء الطيور والزهور – الفيلات الرومانية بقرطاج',
    'Decorated Bust Fragment, Roman villas of Carthage':
        'شظية تمثال نصفي مزخرف، الفيلات الرومانية بقرطاج',
    'Mihrab Niche – Madrasa Al-Bachia, Medina of Tunis':
        'محراب – المدرسة الباشية، المدينة العتيقة بتونس',
    'Bird and Floral Mosaic, Roman villas of Carthage':
        'فسيفساء الطيور والزهور، الفيلات الرومانية بقرطاج',
    'Decorated Bust Fragment – Roman Villas of Carth…':
        'شظية تمثال نصفي مزخرف – الفيلات الرومانية بقرط…',
    'Folger Institute Long-Term Fellowships 2026-2027':
        'زمالات طويلة المدى من Folger Institute 2026-2027',
    'Latin Inscription Slab  Water Temple of Zaghouan': 'لوح بنقش لاتيني  معبد المياه بزغوان',
    'Roman Mosaic with Bird and Vine Motifs – Villas…':
        'فسيفساء رومانية بزخارف الطيور والكرمة – فيلات…',
    'Wooden Door with Tilework – Zawiya of Sidi Sahbi': 'باب خشبي بالزليج – زاوية سيدي الصحبي',
    'Punic Stelae Row – Tophet of Salammbo, Carthage': 'صف نُصب بونية – توفة سلامبو، قرطاج',
    'Wooden Door with Tilework, Zawiya of Sidi Sahbi': 'باب خشبي بالزليج، زاوية سيدي الصحبي',
    'Bird of Prey Statue – Roman Villas of Carthage': 'تمثال طائر جارح – الفيلات الرومانية بقرطاج',
    'Bobby Anspach Studios Foundation Grant Program': 'برنامج منح مؤسسة Bobby Anspach Studios',
    'Latin Inscription Slab, Water Temple, Zaghouan': 'لوح بنقش لاتيني، معبد المياه، زغوان',
    'Punic Stelae Row, Tophet of Salammbo, Carthage': 'صف من الأنصاب البونية، توفة سلامبو، قرطاج',
    'Reviewing scans together in an immersive space': 'مراجعة عمليات المسح معا في فضاء غامر',
    'Water and stone for the museum&#x27;s open air': 'ماء وحجر لفضاء المتحف المفتوح',
    'Architectural Fragments  - Baths of Antoninus': 'شظايا معمارية  - حمامات أنطونينوس',
    'Bird of Prey Statue, Roman villas of Carthage': 'تمثال طائر جارح، الفيلات الرومانية بقرطاج',
    'Carved Architectural Block with Laurel Motifs': 'كتلة معمارية منقوشة بزخارف الغار',
    'Every one of these was scanned by a volunteer': 'كل قطعة من هذه مسحها متطوّع',
    'Fluted Column Fragment – Byrsa Hill, Carthage': 'شظية عمود مضلّع – تل بيرصا، قرطاج',
    'Headless Draped Statue – Byrsa Hill, Carthage': 'تمثال مدثر بلا رأس – تل بيرصا، قرطاج',
    "Keep a country's memory, with your name on it": 'احفظوا ذاكرة بلد، باسمكم عليها',
    'Reitz Union, Room G330, University of Florida': 'Reitz Union، قاعة G330، جامعة فلوريدا',
    'Inscribed Architectural Fragment, Byrsa Hill': 'شظية معمارية منقوشة، تل بيرصا',
    'Leadership and Techplomacy Summit Dubai 2026': 'قمة القيادة والدبلوماسية التقنية، دبي 2026',
    'Male Torso Statue – Roman Villas of Carthage': 'تمثال جذع رجل – الفيلات الرومانية بقرطاج',
    'Punic Stelae – Tophet of Salammbo (Carthage)': 'نُصُب بونية – توفة سلامبو (قرطاج)',
    'Architectural Fragments, Baths of Antoninus': 'شظايا معمارية، حمامات أنطونينوس',
    'First Phoenicians and Tyrian Purple Origins': 'الفينيقيون الأوائل وأصول الأرجوان الصوري',
    'Ornamental Mihrab (Mahram), Medina of Tunis': 'محراب زخرفي (محرم)، المدينة العتيقة بتونس',
    'Roman Togatus Statue – Byrsa Hill, Carthage': 'تمثال روماني بالتوغا – تل بيرصا، قرطاج',
    'Sacred Niche – Roman Water Temple, Zaghouan': 'حنية مقدسة – معبد المياه الروماني، زغوان',
    'Marble Calligraphic Panel – Zitouna Mosque': 'لوحة خطّية من الرخام – جامع الزيتونة',
    'Punic Stela – Tophet of Salammbo, Carthage': 'نصب بوني – توفة سلامبو، قرطاج',
    'Punic Stelae, Tophet of Salammbo, Carthage': 'نصب بونية، توفة سلامبو، قرطاج',
    'Roman Draped Statue – Byrsa Hill, Carthage': 'تمثال روماني بثوب منسدل – تل بيرصا، قرطاج',
    'Tanit Stela – Tophet of Salammbo, Carthage': 'نصب تانيت – توفة سلامبو، قرطاج',
    'Corinthian Capital – Byrsa Hill, Carthage': 'تاج عمود كورنثي – تل بيرصا، قرطاج',
    'Creative Director / Experiential Designer': 'مدير إبداعي / مصمم تجارب',
    'Statue Fragment, Roman villas of Carthage': 'شظية تمثال، الفيلات الرومانية بقرطاج',
    'Tanit XR at CityCamp Gainesville Hack Day': 'Tanit XR في CityCamp Gainesville Hack Day',
    'Tilework Wall Panel, Zawiya of Sidi Sahbi': 'لوحة جدارية من الزليج، زاوية سيدي الصحبي',
    'Bust Fragment – Roman Villas of Carthage': 'شظية تمثال نصفي – الفيلات الرومانية بقرطاج',
    'Photogrammetry, Grants and Opportunities': 'المسح التصويري، المنح والفرص',
    'A 2,000-Year-Old Ghost Town on Cape Bon': 'مدينة أشباح عمرها 2000 عام في الوطن القبلي',
    'Bir (Traditional Well), Medina of Tunis': 'بئر تقليدية، المدينة العتيقة بتونس',
    'Bust Fragment, Roman villas of Carthage': 'شظية تمثال نصفي، الفيلات الرومانية بقرطاج',
    'Come and help us keep Tunisia’s history': 'تعال وساعدنا في حفظ تاريخ تونس',
    'Reclining Figure – Byrsa Hill, Carthage': 'تمثال مستلقٍ – تل بيرصا، قرطاج',
    'Article de la conférence d’El Jem 2026': 'ورقة مؤتمر الجم 2026',
    'Large Azure Stonecrop Succulent in Pot': 'نبتة عصارية كبيرة زرقاء في أصيص',
    'Small Azure Stonecrop Succulent in Pot': 'نبتة عصارية زرقاء صغيرة في إناء',
    'Adopt a gallery in the virtual museum': 'تبنّوا قاعة في المتحف الافتراضي',
    'Do I need to know 3D, or archaeology?': 'هل يلزمني إتقان الأبعاد الثلاثة أو علم الآثار؟',
    'Preservation scan and game-ready twin': 'مسح ثلاثي الأبعاد للحفظ ونسخة توأم جاهزة للألعاب',
    'Washington, DC. Venue to be announced': 'واشنطن العاصمة. سيُعلن عن المكان لاحقًا',
    'Gaussian splat captured with a phone': 'سبلات غاوسي ملتقط بهاتف',
    'Sacred Niche, Water Temple, Zaghouan': 'كوّة مقدسة، معبد المياه، زغوان',
    'See the whole collection at a glance': 'اطّلع على المجموعة كاملة في لمحة',
    'Your team&#x27;s hours, on real work': 'ساعات فريقك، في عمل حقيقي',
    'Interior with Tilework and Fountain': 'فضاء داخلي بالزليج ونافورة',
    'Learn to capture in 3D with a phone': 'تعلّم التقاط النماذج ثلاثية الأبعاد بهاتفك',
    'Niantic Spatial feature on Tanit XR': 'تقرير Niantic Spatial عن Tanit XR',
    'Roman Column – Byrsa Hill, Carthage': 'عمود روماني – تل بيرصا، قرطاج',
    'Stone Basin, Water Temple, Zaghouan': 'حوض حجري، معبد المياه، زغوان',
    'Headless Draped Statue, Byrsa Hill': 'تمثال مكسو بالثوب بلا رأس، تل بيرصا',
    'Niche Wall, Water Temple, Zaghouan': 'جدار المحاريب، معبد المياه، زغوان',
    'Press &amp; Recognition – TANIT XR': 'الصحافة والتقدير – TANIT XR',
    'The picture you are about to share': 'الصورة التي أنت على وشك مشاركتها',
    'Traditional Loom with Woven Carpet': 'منسج تقليدي مع زربية منسوجة',
    'Reality Hack 2026 Art Grant (MIT)': 'منحة Reality Hack 2026 الفنية (MIT)',
    'Sunday, September 20, 10am to 6pm': 'الأحد 20 سبتمبر، من العاشرة صباحا إلى السادسة مساء',
    'Take the four-minute guided visit': 'قوموا بالجولة المصحوبة في أربع دقائق',
    'Tanit XR in person, Washington DC': 'Tanit XR حضوريًا، واشنطن العاصمة',
    'Transparent background, red mark.': 'خلفية شفافة، علامة حمراء.',
    'A Beginning: Why Tanit XR Exists': 'البداية: لماذا وُجدت Tanit XR',
    "Explore Tunisia's heritage in 3D": 'استكشف التراث التونسي بالأبعاد الثلاثة',
    'Inscribed Architectural Fragment': 'شظية معمارية منقوشة',
    'Tunisian Wooden Woven Table Lamp': 'مصباح طاولة تونسي من الخشب المضفور',
    'What a partnership can look like': 'كيف يمكن أن تبدو الشراكة',
    'Roman Draped Statue, Byrsa Hill': 'تمثال روماني مكسوّ بالثوب، تل بيرصا',
    'Domed hall with striped arches': 'قاعة مقبّبة بأقواس مخططة',
    'A care day for a coastal site': 'يوم عناية بموقع ساحلي',
    'Mihrab Niche, Medina of Tunis': 'حنية محراب، المدينة العتيقة بتونس',
    'Murex Shell - Murex Brandaris': 'صدفة موركس - Murex brandaris',
    'Punic and Roman, exposed 2026': 'بوني وروماني، كُشف عنه سنة 2026',
    '3D Modeler & Web Contributor': 'نمذجة ثلاثية الأبعاد ومساهمة في الويب',
    'El Jem Conference 2026 paper': 'ورقة بحثية، مؤتمر الجم 2026',
    'Immerse the Bay XR Hackathon': 'هاكاثون الواقع الممتد Immerse the Bay',
    'Reclining Figure, Byrsa Hill': 'تمثال مستلقٍ، تل بيرصا',
    'Creative Capital Award 2027': 'جائزة Creative Capital 2027',
    'Galleries, with the stories': 'القاعات، مع الحكايات',
    'How much time does it take?': 'كم من الوقت يتطلب ذلك؟',
    'RAY Fellowship Program 2026': 'برنامج زمالة RAY 2026',
    'See the projects on Devpost': 'اطّلع على المشاريع على Devpost',
    'Splats With Phones workshop': 'ورشة Splats With Phones',
    'Strategy & Creative Support': 'الاستراتيجية والدعم الإبداعي',
    'Wall with the sign of Tanit': 'جدار يحمل علامة تانيت',
    'Event · September 20, 2026': 'فعالية · 20 سبتمبر 2026',
    'Mentoring & interview prep': 'الإرشاد والتحضير للمقابلات',
    'Ornamental Mihrab (Mahram)': 'محراب مزخرف (محرم)',
    '2D Design & 3D Generalist': 'تصميم ثنائي الأبعاد وأعمال ثلاثية الأبعاد',
    'Courtyard fountain, large': 'نافورة الفناء، كبيرة',
    'Draped Statue, Byrsa Hill': 'تمثال مكسوّ بالثوب، تل بيرصا',
    'Fund the community itself': 'موّل المجتمع نفسه',
    'How do you work together?': 'كيف تعملون معا؟',
    'NEW INC Year 13 Open Call': 'NEW INC، دعوة مفتوحة للسنة الثالثة عشرة',
    'See it in your space (AR)': 'شاهدوها في مكانكم (الواقع المعزز)',
    'Splats With Phones course': 'دورة Splats With Phones',
    'What we have already done': 'ما أنجزناه حتى الآن',
    'Explore in 3D – TANIT XR': 'استكشف بالأبعاد الثلاثة – TANIT XR',
    'Fountains and courtyards': 'النوافير والأفنية',
    'Illustrator and Designer': 'الرسم والتصميم',
    'Partnerships & Community': 'الشراكات والمجتمع',
    'Press · October 12, 2025': 'صحافة · 12 أكتوبر 2025',
    'Roman Column, Byrsa Hill': 'عمود روماني، تل بيرصا',
    'Roman villas of Carthage': 'الفيلات الرومانية بقرطاج',
    'See the experience first': 'شاهدوا التجربة أولا',
    'Bring it to your region': 'انقل المشروع إلى منطقتك',
    'Browse the full\narchive': 'تصفحوا الأرشيف\nكاملا',
    'Drawn by our volunteers': 'من رسم متطوعينا',
    'Floors people walked on': 'أرضيات مشى عليها الناس',
    'From Mystery to History': 'من الغموض إلى التاريخ',
    'Open your saved objects': 'افتح قطعك المحفوظة',
    'Water, carried and kept': 'الماء، محمولا ومحفوظا',
    'Architecture and ruins': 'العمارة والأطلال',
    'Assorted Succulent Pot': 'إناء نباتات عصارية متنوعة',
    'Back to the collection': 'العودة إلى المجموعة',
    'Bird and Floral Mosaic': 'فسيفساء بطيور وزخارف نباتية',
    'Fluted Column Fragment': 'شظية عمود مضلّع',
    'Headless Draped Statue': 'تمثال مدثر بلا رأس',
    'ImmerseGT participants': 'المشاركون في ImmerseGT',
    'Podcast · July 2, 2026': 'بودكاست · 2 جويلية 2026',
    'Sidi Bou Said, Tunisia': 'سيدي بوسعيد، تونس',
    'Standing Draped Statue': 'تمثال مدثر واقف',
    'Start the conversation': 'ابدأ المحادثة',
    'The Kyoto Retreat 2026': 'خلوة كيوتو 2026',
    'The people of Carthage': 'أهل قرطاج',
    'View this object in 3D': 'شاهد هذه القطعة ثلاثية الأبعاد',
    'Water Temple, Zaghouan': 'معبد المياه، زغوان',
    'AWE USA 2026, Speaker': 'AWE USA 2026، متحدثة',
    'Enter the galleries ↓': 'ادخلوا القاعات ↓',
    'Mini history lesson 3': 'درس تاريخ مصغّر 3',
    'Objects and artifacts': 'القطع والآثار',
    'Roman, 2nd century CE': 'روماني، القرن الثاني الميلادي',
    'Where to find us next': 'أين تجدوننا قريبا',
    'April 10 to 12, 2026': 'من 10 إلى 12 أبريل 2026',
    'Arch, fourth pattern': 'قوس، النقش الرابع',
    'Arch, second pattern': 'قوس، الزخرفة الثانية',
    'Events & conferences': 'فعاليات ومؤتمرات',
    'Open the full record': 'فتح السجل الكامل',
    'Paper · دارجة تونسية': 'ورقة بحثية · دارجة تونسية',
    'Research and Writing': 'البحث والكتابة',
    'See it in your space': 'شاهدوه في مكانكم',
    'Thursday, October 22': 'الخميس 22 أكتوبر',
    'Zawiya of Sidi Sahbi': 'زاوية سيدي الصحبي',
    'Arch, first pattern': 'قوس، النقش الأول',
    'Arch, third pattern': 'قوس، الزخرفة الثالثة',
    'Medina of Tunis (7)': 'المدينة العتيقة بتونس (7)',
    'Rooms of the museum': 'قاعات المتحف',
    'Share my collection': 'مشاركة مجموعتي',
    'Share to protect it': 'شارِك لتحميه',
    'Tilework Wall Panel': 'لوحة جدارية من الزليج',
    '7th century onward': 'من القرن السابع فصاعدا',
    '8th century onward': 'من القرن الثامن فصاعدًا',
    'Contact – TANIT XR': 'اتصلوا بنا – TANIT XR',
    'How these are made': 'كيف تُصنع هذه الأعمال',
    'Lamps and lanterns': 'مصابيح وفوانيس',
    'Partnership · 2026': 'شراكة · 2026',
    'Scanned in Tunisia': 'مسح في تونس',
    'Stained glass lamp': 'مصباح من الزجاج الملوّن',
    'Where prayer faces': 'حيث تتّجه الصلاة',
    'Words cut in stone': 'كلمات محفورة في الحجر',
    'Browse every scan': 'تصفّح كل عمليات المسح',
    'Everyday heritage': 'تراث الحياة اليومية',
    'Exhibition · 2026': 'معرض · 2026',
    'Male Torso Statue': 'تمثال جذع رجل',
    'Preservation scan': 'مسح من أجل الحفظ',
    'Roman Column Base': 'قاعدة عمود روماني',
    'Volunteer with us': 'تطوّع معنا',
    'by Claire Natanek': 'من إنجاز Claire Natanek',
    '›&nbsp; Thank you': '›  شكرًا لك',
    'At-risk heritage': 'تراث مهدَّد',
    'Illustrations by': 'الرسوم التوضيحية من إنجاز',
    'Logo, horizontal': 'الشعار، أفقي',
    'New Site (Flood)': 'موقع جديد (فيضان)',
    'Podcasts & video': 'بودكاست وفيديو',
    'Save the picture': 'حفظ الصورة',
    'Talk · June 2026': 'محاضرة · يونيو 2026',
    'The building kit': 'مجموعة عناصر البناء',
    '· August 6, 2026': '· 6 أوت 2026',
    'El Jem, Tunisia': 'الجم، تونس',
    'Medina of Tunis': 'المدينة العتيقة بتونس',
    'Paper · English': 'ورقة بحثية · بالإنجليزية',
    'Previous object': 'القطعة السابقة',
    'Read this aloud': 'استمعوا إلى النص',
    'Your collection': 'مجموعتك',
    'you can edit it': 'يمكنكم تعديلها',
    '›&nbsp; Contact': '›  اتصلوا بنا',
    'Article · 2026': 'مقال · 2026',
    'Carved ceiling': 'سقف منقوش',
    'Furnished room': 'غرفة مؤثثة',
    'Large clay pot': 'إناء فخاري كبير',
    'Logo, vertical': 'الشعار، عمودي',
    'Read the paper': 'اقرأوا الورقة البحثية',
    'Talks & events': 'محاضرات وفعاليات',
    'XR Development': 'تطوير الواقع الممتد',
    '3D Generalist': 'مصمّم ثلاثي الأبعاد متعدّد المهام',
    'Community art': 'فن المجتمع',
    'Explore in 3D': 'استكشاف ثلاثي الأبعاد',
    'Lamps (Unlit)': 'مصابيح (غير مضاءة)',
    'Small details': 'تفاصيل صغيرة',
    'Years covered': 'السنوات المشمولة',
    'Badge earned': 'تم الحصول على الشارة',
    'Curved bench': 'مقعد منحني',
    'From the sea': 'من البحر',
    'Kairouan (4)': 'القيروان (4)',
    'Neapolis (1)': 'نابوليس (1)',
    'Optimized by': 'تحسين بواسطة',
    'Tell me more': 'أخبروني أكثر',
    'XR Developer': 'مطوّر XR',
    'Zaghouan (7)': 'زغوان (7)',
    'August 2026': 'أغسطس 2026',
    'Fill in the': 'املأوا',
    'How to scan': 'كيفية المسح الثلاثي الأبعاد',
    'Lamps (Lit)': 'مصابيح (مضاءة)',
    'Open to all': 'مفتوح للجميع',
    'Ottoman era': 'العهد العثماني',
    'Wall, solid': 'جدار مصمت',
    'Write to us': 'راسلونا',
    '11 objects': '11 قطعة',
    '28 objects': '28 قطعة',
    'Contact us': 'اتصلوا بنا',
    'March 2026': 'مارس 2026',
    'Share this': 'شارك هذا',
    '3 objects': '3 قطع',
    '5 objects': '5 قطع',
    '7 objects': '7 قطع',
    '8 objects': '8 قطع',
    'Clay lamp': 'مصباح من الطين',
    'Copy link': 'نسخ الرابط',
    'Our story': 'قصتنا',
    'Palm tree': 'نخلة',
    'Small pot': 'إناء صغير',
    'Wall lamp': 'مصباح حائطي',
    'HALL III': 'القاعة الثالثة',
    'Share it': 'شاركوها',
    'HALL IV': 'القاعة الرابعة',
    'Got it': 'فهمت',
    'HALL V': 'القاعة الخامسة',
    'Next →': 'التالي →',

    # ---- added 2026-09-21: pages that were still English ----
    'Our paper on digital documentation, XR and citizen science for community-led heritage preservation, presented at the El Jem conference and published here in English, French and Tunisian Arabic.':
        'ورقتنا البحثية حول التوثيق الرقمي والواقع الممتد والعلم التشاركي من أجل حفظ التراث بقيادة المجتمعات، قُدّمت في مؤتمر الجم ونُشرت هنا بالإنجليزية والفرنسية والعربية التونسية.',
    'Sponsor a community scanning and site clean-up day with local volunteers, covering travel, meals and shared equipment, and start compensating local contributors for their time.':
        'ارعَ يوما مجتمعيا للمسح الثلاثي الأبعاد وتنظيف أحد المواقع مع متطوعين محليين، مع تغطية التنقل والوجبات والمعدات المشتركة، والبدء في تعويض المساهمين المحليين عن وقتهم.',
    'Nathan Bowser interviewed Ines Said for Niantic Spatial about Tanit XR and the Scaniverse capture of the amphitheatre of El Jem; Niantic published the video on its channels.':
        'أجرى Nathan Bowser مقابلة مع Ines Said لصالح Niantic Spatial حول Tanit XR وعملية التقاط مدرج الجم بتطبيق Scaniverse؛ ونشرت Niantic الفيديو على قنواتها.',
    'Tanit XR was a finalist in the Best Societal Impact category at Augmented World Expo USA 2026, the XR industry&#x27;s main awards, selected by public vote and expert review.':
        'كان Tanit XR من المتأهلين للنهائي في فئة أفضل أثر مجتمعي في معرض Augmented World Expo USA 2026، أبرز جوائز قطاع الواقع الممتد، بعد تصويت الجمهور وتقييم الخبراء.',
    'Nura, a guide character modeled in Blender, walks with you and tells the story behind each object. Her narrated tour, “Before It’s Gone,” is being written now.':
        'Nura، شخصية مرشدة صُممت في Blender، تسير معك وتروي قصة كل قطعة. وجولتها المصحوبة بالتعليق، “Before It’s Gone”، قيد الكتابة الآن.',
    'This finely preserved doorway combines a heavy wooden door framed by intricate glazed tilework, characteristic of Tunisian Islamic architectural decoration.':
        'يجمع هذا المدخل المحفوظ بعناية بين باب خشبي ثقيل يحيط به زليج مزجج دقيق الزخرفة، وهو من سمات الزخرفة المعمارية الإسلامية التونسية.',
    'We sponsored a heritage track and a $300 prize at Georgia Tech&#x27;s XR hackathon, and Dr. Caroline Nickerson led a workshop on citizen science and XR.':
        'رعينا مسارا خاصا بالتراث وجائزة قدرها 300 دولار في هاكاثون الواقع الممتد بجامعة جورجيا تك، وقادت الدكتورة Caroline Nickerson ورشة عمل حول العلوم التشاركية والواقع الممتد.',
    'Tell us what draws you to this cohort and what you hope to gain from it. We are interested in your motivation and curiosity, not perfection.':
        'أخبرنا بما يجذبك إلى هذه الدفعة وبما تأمل أن تحصل عليه منها. يهمنا دافعك وفضولك، لا الكمال.',
    'Romans of Byrsa Hill and the villas, carved in marble. Most lost a head or an arm on the way to us, and they are still unmistakably people':
        'رومان من تل بيرصا ومن الفيلات، منحوتون في الرخام. فقد معظمهم رأسا أو ذراعا في الطريق إلينا، ومع ذلك يبقون بشرا بلا لبس',
    'From the temple over the spring at Zaghouan, water travelled ninety kilometres to Carthage. These basins and wells are where it arrived':
        'من المعبد القائم فوق نبع زغوان، كانت المياه تقطع تسعين كيلومترًا إلى قرطاج. وهذه الأحواض والآبار هي حيث كانت تصل',
    'Short sessions on the sites and objects we scan, Carthage, the Tophet, the medina of Tunis, so every model comes with its story.':
        'جلسات قصيرة حول المواقع والقطع التي نمسحها، قرطاج، التوفة، المدينة العتيقة بتونس، حتى يأتي كل نموذج مصحوبا بقصته.',
    'Whole places rather than single objects: passages under the baths, tiled interiors, and a city the sea gave back for a few days':
        'أماكن كاملة لا قطعًا منفردة: الممرات تحت الحمامات، وفضاءات داخلية بالزليج، ومدينة أعادها البحر لبضعة أيام',
    'Volunteers scan sites on the ground, optimize models for VR, write articles, and model heritage\nobjects by hand, like these.':
        'متطوعون يمسحون المواقع على الأرض، ويحسّنون النماذج للواقع الافتراضي، ويكتبون المقالات، ويصممون قطع التراث\nيدويا، مثل هذه.',
    'Planned for Viverse so it runs cross-platform, in VR, and as a scroll-to-walk version in any browser for classrooms.':
        'مخطط له على Viverse ليعمل على مختلف المنصات وفي الواقع الافتراضي، وكنسخة تُستكشف بالتمرير في أي متصفح لفائدة الأقسام الدراسية.',
    'Arches, walls, pillars and ceilings: puzzle pieces any volunteer can take and assemble into a gallery of their own':
        'أقواس وجدران وأعمدة وأسقف: قطع أحجية يمكن لأي متطوع أن يأخذها ويركبها ليصنع قاعته الخاصة',
    'Numbers, monthly: visits, objects viewed, people trained, volunteer hours, from the same counter we use ourselves.':
        'أرقام شهرية: الزيارات، والقطع التي شوهدت، والأشخاص الذين تدربوا، وساعات التطوع، من العدّاد نفسه الذي نستعمله نحن.',
    'Stories your communications team can use: volunteers, sites, a storm, a rescue, with pictures we take ourselves.':
        'قصص يمكن لفريق التواصل لديكم استخدامها: متطوعون، مواقع، عاصفة، عملية إنقاذ، مع صور نلتقطها بأنفسنا.',
    'Photogrammetry records of statues, mosaics, stelae and ruins, preservation quality, with game-ready twins.':
        'سجلات بالمسح التصويري لتماثيل وفسيفساء ونُصب وأطلال، بجودة تصلح للحفظ، مع نسخ توأم جاهزة للألعاب.',
    'Mihrabs and niches from mosques, madrasas and a Roman water temple. Each one tells you which way to turn':
        'محاريب وكوّات من مساجد ومدارس ومعبد مياه روماني. كل واحد منها يدلك على الجهة التي تتجه إليها',
    'Your logo on the site, in the experience and at our events, and a mention in every newsletter edition.':
        'شعاركم على الموقع وداخل التجربة وفي فعالياتنا، مع ذكركم في كل عدد من النشرة الإخبارية.',
    ', places or objects threatened by weather, neglect, development, conflict, theft, or loss of memory':
        '، أماكن أو قطع مهددة بالطقس، أو الإهمال، أو التوسع العمراني، أو النزاعات، أو السرقة، أو النسيان',
    'A tax-deductible gift through our fiscal sponsor, Florida Community Innovation, a U.S. 501(c)(3).':
        'تبرع معفى من الضرائب عبر الراعي المالي لنا، Florida Community Innovation، وهي منظمة أمريكية مسجلة تحت بند 501(c)(3).',
    'We speak, exhibit and sponsor: AWE, the El Jem conference, ImmerseGT at Georgia Tech, and more.':
        'نحاضر ونعرض ونرعى: AWE، ومؤتمر الجم، وImmerseGT في جورجيا تك، وغيرها.',
    'Whole spaces built by volunteers: the main hall, a furnished room, the plinths and rugs inside':
        'فضاءات كاملة بناها متطوعون: القاعة الرئيسية، وغرفة مؤثثة، وقواعد العرض والسجاد بداخلها',
    'The virtual museum in January 2026: first courtyard and corridor with scanned statues placed':
        'المتحف الافتراضي في يناير 2026: الفناء الأول والممر مع التماثيل الممسوحة ثلاثي الأبعاد في أماكنها',
    'Light the way it falls in a Tunisian home, modelled by volunteers who studied the real ones':
        'الضوء كما يتسلل في بيت تونسي، صممه متطوعون درسوا البيوت الحقيقية',
    ', doors, arches, columns, facades, walls, courtyards, tombs, monuments, and historic homes':
        '، أبواب، أقواس، أعمدة، واجهات، جدران، أفنية، مقابر، معالم، ومنازل تاريخية',
    'Digital documentation, XR and citizen science for community-driven heritage preservation.':
        'التوثيق الرقمي والواقع الممتد والعلم التشاركي من أجل حفظ التراث بقيادة المجتمعات.',
    'Employees who learned something real and can show their families what they helped keep.':
        'موظفون تعلّموا شيئا حقيقيا ويمكنهم أن يُروا عائلاتهم ما ساهموا في الحفاظ عليه.',
    'Tell us what you like doing, scanning, 3D, writing, design, research, teaching.':
        'أخبرنا بما تحب أن تفعل، المسح الثلاثي الأبعاد، التصميم ثلاثي الأبعاد، الكتابة، التصميم، البحث، التدريس.',
    'Processing uses a lot of data, it’s best to wait until you’re home with Wi-Fi.':
        'المعالجة تستهلك الكثير من البيانات، ومن الأفضل الانتظار حتى تعود إلى المنزل وتتصل بشبكة Wi-Fi.',
    'Natural daylight is good, but harsh sun causes glare, avoid scanning at noon':
        'ضوء النهار الطبيعي جيد، لكن الشمس القوية تسبب وهجا، فتجنب المسح عند الظهيرة',
    'Anything that might help us better understand you or your availability.':
        'أي شيء يساعدنا على فهمك أو فهم أوقات فراغك بشكل أفضل.',
    'XR Women Museum, two exhibitions in FrameVR, curated by Paige Dansinger':
        'XR Women Museum، معرضان في FrameVR، من تنسيق Paige Dansinger',
    'ImmerseGT 2026, Sponsored track at Georgia Tech&#x27;s XR hackathon':
        'ImmerseGT 2026، مسار برعايتنا في هاكاثون الواقع الممتد بجامعة جورجيا تك',
    'First courtyard and corridor blocked out; scanned statues placed.':
        'تم تخطيط الفناء الأول والممر، ووُضعت التماثيل الممسوحة ثلاثي الأبعاد في أماكنها.',
    'Who we are, what we do, how to help, one page in three languages.':
        'من نحن، وماذا نفعل، وكيف يمكن المساعدة، صفحة واحدة بثلاث لغات.',
    'Storm Harry, Neapolis, and a Digital Moment of Preservation':
        'عاصفة هاري ونيابوليس ولحظة حفظ رقمية',
    'Tilework Wall Panel – Mausoleum of Sidi Sahbi, Kairouan':
        'لوحة جدارية من الزليج – ضريح سيدي الصاحب، القيروان',
    'While you wait, the weekly opportunity digest is free:':
        'في انتظار ذلك، النشرة الأسبوعية للفرص مجانية:',
    'Niantic Spatial, video interview with Nathan Bowser':
        'Niantic Spatial، مقابلة مصورة مع Nathan Bowser',
    '(not “Splat”), this is what we need for Tanit XR.':
        '(وليس “Splat”)، هذا ما نحتاجه في Tanit XR.',
    'Standing Draped Statue – Roman Villas of Carthage':
        'تمثال واقف بثوب منسدل – الفيلات الرومانية بقرطاج',
    'Drag to look around. Tap anything to get closer.':
        'اسحب لتنظر حولك. انقر على أي شيء لتقترب منه.',
    'Inscribed Architectural Fragment – Byrsa Hill, …': 'شظية معمارية منقوشة – تل بيرصا، …',
    'XR Women Museum Open Call: Vibrancy as Practice':
        'دعوة مفتوحة من XR Women Museum: Vibrancy as Practice',
    'Carved Architectural Blocks with Laurel Motifs': 'كتل معمارية منحوتة بزخارف الغار',
    'Passthrough on a headset, camera AR on a phone':
        'المرور البصري على النظارة، وواقع معزز بالكاميرا على الهاتف',
    'Architectural Fragment with Relief Decoration': 'شظية معمارية بزخرفة بارزة',
    'Every object in here was saved by a volunteer': 'كل قطعة هنا أنقذها متطوع',
    'Fifteen minutes is enough to see if this fits':
        'خمس عشرة دقيقة تكفي لمعرفة إن كان هذا مناسبا لك',
    'Ornamental Mihrab (Mahram) – Medersa Slimanya': 'محراب زخرفي (محرم) – المدرسة السليمانية',
    'I run an organisation. Can we work with you?': 'أدير مؤسسة. هل يمكننا العمل معكم؟',
    'Ornamental Wooden Door with Studded Patterns': 'باب خشبي مزخرف بنقوش من المسامير',
    'Neapolis Site Revealed By Floods In Tunisia': 'الفيضانات تكشف موقع نيابوليس في تونس',
    'Underground Passageways, Baths of Antoninus': 'الممرات تحت الأرض، حمامات أنطونينوس',
    'A talk, a workshop or a room at your event': 'محاضرة أو ورشة عمل أو قاعة في فعاليتكم',
    'Statue Fragment – Roman Villas of Carthage': 'شظية تمثال – الفيلات الرومانية بقرطاج',
    'Walk through Tunisia, one object at a time': 'تجوّل في تونس، قطعة بعد قطعة',
    'Architectural Fragments with Inscriptions': 'شظايا معمارية تحمل نقوشا',
    'Punic Stela, Tophet of Salammbo, Carthage': 'نصب بوني، توفة سلامبو، قرطاج',
    'Tanit Stela, Tophet of Salammbo, Carthage': 'نصب تانيت، توفة سلامبو، قرطاج',
    'Bir (Traditional Well) – Medina of Tunis': 'بئر (تقليدية) – المدينة العتيقة بتونس',
    'Roman Column Base – Byrsa Hill, Carthage': 'قاعدة عمود رومانية – تل بيرصا، قرطاج',
    'El Jem Conference, our paper presented': 'مؤتمر الجم، تقديم ورقتنا البحثية',
    'Roman Mosaic with Bird and Vine Motifs': 'فسيفساء رومانية بزخارف الطيور والكرمة',
    'Tiled corridor with a scanned artifact': 'ممر مكسو بالزليج مع قطعة أثرية ممسوحة ثلاثي الأبعاد',
    'Build an immersive experience with us': 'ابنِ معنا تجربة غامرة',
    'Draped Statue – Byrsa Hill, Carthage': 'تمثال بثوب منسدل – تل بيرصا، قرطاج',
    'Stone Basin – Water Temple, Zaghouan': 'حوض حجري – معبد المياه، زغوان',
    'Neapolis Site Revealed By Floods In': 'موقع نيابوليس الذي كشفت عنه الفيضانات',
    'Niche Wall – Water Temple, Zaghouan': 'جدار الكوّات – معبد المياه، زغوان',
    'Traditional Door – Medina of Tunis': 'باب تقليدي – المدينة العتيقة بتونس',
    'Wooden Door – Zawiya of Sidi Sahib': 'باب خشبي – زاوية سيدي الصاحب',
    'Example: EST, GMT+1, Tunisia time': 'مثال: EST، GMT+1، توقيت تونس',
    'Splats With Phones cohort session': 'جلسة مجموعة Splats With Phones',
    'Roman Togatus Statue, Byrsa Hill': 'تمثال روماني بالتوغا، تل بيرصا',
    'Scanned Roman statue in a niche': 'تمثال روماني ممسوح ثلاثي الأبعاد داخل كوّة',
    'Corinthian Capital, Byrsa Hill': 'تاج عمود كورنثي، تل بيرصا',
    'For companies and foundations': 'للشركات والمؤسسات',
    'Ornate Tunisian Hanging Lamp': 'مصباح معلق تونسي مزخرف',
    'Tophet of Salammbo, Carthage': 'توفة سلامبو، قرطاج',
    'Scaniverse scanning example': 'مثال على المسح باستخدام Scaniverse',
    'Virtual Museum, in progress': 'المتحف الافتراضي، قيد الإنجاز',
    'Your message is on its way.': 'رسالتك في طريقها إلينا.',
    'Watch the post on LinkedIn': 'شاهد المنشور على LinkedIn',
    'subscribe to Opportunities': 'الاشتراك في الفرص',
    'Courtyard fountain, small': 'نافورة فناء، صغيرة',
    'Event · April 10–12, 2026': 'فعالية · 10–12 أبريل 2026',
    'Marble Calligraphic Panel': 'لوح رخامي بخط عربي',
    'Nura has something to say': 'Nura لديها ما تقوله',
    'Virtual Museum – TANIT XR': 'المتحف الافتراضي – TANIT XR',
    'Wooden Door with Tilework': 'باب خشبي بزليج',
    'Browse with descriptions': 'تصفح مع الأوصاف',
    'One-pager (EN / FR / AR)': 'صفحة واحدة (EN / FR / AR)',
    'Pots, plants and gardens': 'أوانٍ ونباتات وحدائق',
    'What do I get out of it?': 'ماذا أستفيد من ذلك؟',
    'Decorated Bust Fragment': 'شظية تمثال نصفي مزخرف',
    'El Jem Conference paper': 'ورقة بحثية في مؤتمر الجم',
    'Read the scanning guide': 'اقرأ دليل المسح الثلاثي الأبعاد',
    'Bir (Traditional Well)': 'بئر (بئر تقليدية)',
    'Email info@tanitxr.org': 'راسلونا على info@tanitxr.org',
    'Latin Inscription Slab': 'لوح بنقش لاتيني',
    'See how a scan is made': 'شاهد كيف يتم المسح الثلاثي الأبعاد',
    'Stones raised to Tanit': 'حجارة أُقيمت لتانيت',
    "The museum's main hall": 'القاعة الرئيسية للمتحف',
    'Walk around it, slowly': 'طُفّ حولها ببطء',
    'Where this was scanned': 'أين تم مسح هذه القطعة',
    'Always get permission': 'احصل دائمًا على إذن',
    'Georgia Tech, Atlanta': 'جورجيا تك، أتلانتا',
    'What held the roof up': 'ما كان يحمل السقف',
    'A purple murex shell': 'صدفة موركس أرجوانية',
    'Community – TANIT XR': 'المجتمع – TANIT XR',
    'Galleries – TANIT XR': 'المعارض – TANIT XR',
    'Roman Togatus Statue': 'تمثال روماني بالتوغا',
    'Thank you – TANIT XR': 'شكرا لك – TANIT XR',
    'Bird of Prey Statue': 'تمثال طائر جارح',
    'Roman Draped Statue': 'تمثال روماني بثوب منسدل',
    'Tanit XR volunteers': 'متطوعو Tanit XR',
    'Baths of Antoninus': 'حمامات أنطونينوس',
    'Doors still in use': 'أبواب ما زالت تُستعمل',
    'Paper · April 2026': 'ورقة بحثية · أبريل 2026',
    'Rooms and passages': 'قاعات وممرات',
    'Tanit XR Galleries': 'قاعات Tanit XR',
    'Where we have been': 'أين كنا',
    'Award · June 2026': 'جائزة · يونيو 2026',
    'Kitchen and table': 'المطبخ والمائدة',
    'Map of everything': 'خريطة شاملة',
    'What you get back': 'ما الذي ستحصل عليه',
    '· August 18, 2026': '· 18 أغسطس 2026',
    'Explore it in 3D': 'استكشفها في ثلاثة أبعاد',
    'Paper · Français': 'ورقة بحثية · الفرنسية',
    'Punic Stelae Row': 'صف من النُصُب البونية',
    'by Alyssa George': 'بقلم Alyssa George',
    'Everyday things': 'أشياء من الحياة اليومية',
    'Punic and Roman': 'بوني وروماني',
    'See her profile': 'شاهد صفحتها الشخصية',
    '· July 31, 2026': '· 31 يوليو 2026',
    'Display plinth': 'قاعدة عرض',
    'How do I join?': 'كيف أنضم؟',
    'Member profile': 'الملف الشخصي للعضو',
    'See their room': 'شاهد قاعتهم',
    'volunteer form': 'استمارة التطوع',
    'Carthage (28)': 'قرطاج (28)',
    'Object viewer': 'عارض القطع',
    'Their profile': 'صفحتهم الشخصية',
    'Drag to turn': 'اسحب للتدوير',
    'January 2026': 'يناير 2026',
    'Scanned here': 'تمّ المسح هنا',
    'Video · 2026': 'فيديو · 2026',
    '🎮 Game-ready': '🎮 جاهز للألعاب',
    'Is it paid?': 'هل العمل مدفوع الأجر؟',
    'Next object': 'القطعة التالية',
    'What we did': 'ما الذي أنجزناه',
    'XR Creators': 'مبدعو الواقع الممتد',
    'April 2026': 'أبريل 2026',
    'GAME READY': 'جاهز للألعاب',
    'XR Advisor': 'مستشار في الواقع الممتد',
    '← Previous': '← السابق',
    '2 objects': 'قطعتان',
    '4 objects': '4 قطع',
    'Back home': 'العودة إلى الصفحة الرئيسية',
    'Coming up': 'قريبا',
    'Read more': 'اقرأ المزيد',
    'Thank you': 'شكرا لك',
    '1 object': 'قطعة واحدة',
    'HALL II': 'القاعة الثانية',
    'HALL I': 'القاعة الأولى',

    # ---- added 2026-09-21: pages that were still English ----
    'Tanit XR is run entirely by volunteers. So far most costs, travel to\nsites, tools, hosting, hackathon prizes, have been paid out of pocket by our founders, plus a few individual donations\nthrough our fiscal sponsor, the Florida Community Innovation Foundation (a US 501(c)(3), so donations are tax-deductible).\nWe are applying for grants and building partnerships to change that. Donations keep the community running: hosting,\nvolunteer hours, optimizing and publishing models, the virtual museum, scanning and site clean-up days, our free course\nand workshops, and better equipment. Here is what a donation does:':
        'يُدار Tanit XR بالكامل بجهود المتطوّعين. وحتى الآن، دفع مؤسّسونا معظم المصاريف من جيوبهم، من تنقّلات إلى المواقع وأدوات واستضافة وجوائز الهاكاثون، إلى جانب بعض تبرّعات الأفراد عبر راعينا المالي، مؤسسة Florida Community Innovation Foundation (وهي جمعية أمريكية بصفة 501(c)(3)، أي أنّ التبرّعات قابلة للخصم الضريبي). ونحن نتقدّم بطلبات منح ونبني شراكات لتغيير ذلك. التبرّعات هي ما يُبقي المجموعة تعمل: الاستضافة، وساعات التطوّع، وتحسين النماذج ونشرها، والمتحف الافتراضي، وأيام المسح وتنظيف المواقع، ودورتنا المجانية وورشاتنا، ومعدّات أفضل. وهذا ما يفعله التبرّع:',
    'Cet article a été présenté à la conférence d’El Jem en avril 2026. Il explore comment la documentation\nnumérique, la réalité étendue (XR) et la science participative peuvent soutenir une préservation du\npatrimoine évolutive et portée par les communautés, en Tunisie et au-delà. À travers l’exemple de Tanit XR,\nl’article montre comment des technologies accessibles et la formation de bénévoles permettent d’élargir les\nefforts de documentation, d’inclure des sites sous-représentés et de connecter des publics du monde entier\nau patrimoine tunisien.':
        'قُدّم هذا المقال في مؤتمر الجم في أفريل 2026. وهو يبحث كيف يمكن للتوثيق الرقمي والواقع الممتد (XR) والعلم التشاركي أن تدعم صيانة للتراث قابلة للتوسّع وتقودها المجتمعات المحلية، في تونس وخارجها. ومن خلال مثال Tanit XR، يبيّن المقال كيف تتيح التقنيات المتاحة وتكوين المتطوّعين توسيع جهود التوثيق، وإدراج مواقع ممثّلة تمثيلًا ناقصًا، وربط جمهور من مختلف أنحاء العالم بالتراث التونسي.',
    'Phoenician settlers founded Carthage and it grew into the capital of an empire that ran the western Mediterranean. Rome destroyed it in 146 BCE, then rebuilt it as the capital of Roman Africa. What stands today is layered. Punic stelae raised to Tanit and Baal Hammon sit a short walk from Roman columns, villa mosaics and the largest bath complex Rome built in Africa. Our volunteers scanned across four areas of the site.':
        'أسّس مستوطنون فينيقيون قرطاج، فصارت عاصمة إمبراطورية تسيطر على غرب المتوسّط. دمّرتها روما سنة 146 قبل الميلاد، ثم أعادت بناءها عاصمة لإفريقية الرومانية. وما يقف اليوم هو طبقات فوق طبقات: نصب بونية رُفعت لتانيت وبعل حمون تبعد خطوات عن أعمدة رومانية وفسيفساء الفيلات وأكبر مجمّع حمّامات بنته روما في إفريقيا. وقد مسح متطوّعونا أربع مناطق من الموقع.',
    'The Holy Art Gallery’s “Not Your Grandma’s Gallery” is an ongoing open call series for artists worldwide, positioned as high-energy, contemporary exhibitions across different cities. Listings typically note exhibition dates and a deadline to apply that may be marked as TBC depending on the edition. Check the current call page/post for the specific city, exhibition dates, and the latest submission deadline.':
        'سلسلة "Not Your Grandma’s Gallery" من Holy Art Gallery هي دعوة مفتوحة متواصلة للفنانين من كل أنحاء العالم، تُقدَّم بوصفها معارض معاصرة مفعمة بالحيوية في مدن مختلفة. وتذكر الإعلانات عادةً تواريخ المعرض وأجل التقديم، وقد يكون هذا الأجل غير مؤكّد حسب الدورة. راجع صفحة الدعوة الحالية لمعرفة المدينة وتواريخ المعرض وآخر أجل للتقديم.',
    'In early 2026 Storm Harry stripped sand off the seabed near Nabeul and exposed part of Neapolis, a Punic and later Roman city that collapsed into the sea after a tsunami in the 4th century CE. Stone blocks and wall lines were visible for a few days before the sediment returned. Tanit XR captured the newly exposed area inside that window. This hall holds one object, and it is the reason we work quickly.':
        'في مطلع 2026، أزاحت عاصفة هاري الرمل عن قاع البحر قرب نابل فكشفت جزءًا من نيابوليس، وهي مدينة بونية ثم رومانية ابتلعها البحر بعد تسونامي في القرن الرابع الميلادي. ظلّت كتل الحجارة وخطوط الجدران ظاهرة أيامًا قليلة قبل أن تعود الرواسب. وثّقت Tanit XR المنطقة المكشوفة حديثًا خلال تلك النافذة الزمنية. تضمّ هذه القاعة قطعة واحدة، وهي سبب عملنا بسرعة.',
    "Tanit XR is eighty-five volunteers on four continents who bring Tunisia's endangered heritage\ninto 3D and publish it free, for anyone, working alongside the institutions that look after the sites. Everything on\nthis site was built without a single paid person. A partnership pays for the museum, the experiences, the training and\nthe care of the places, and gives your team a real part in it.":
        'Tanit XR هي خمسة وثمانون متطوّعًا في أربع قارّات ينقلون التراث التونسي المهدّد إلى ثلاثة أبعاد وينشرونه مجّانًا للجميع، بالعمل إلى جانب المؤسسات التي ترعى المواقع. كل ما في هذا الموقع أُنجز دون أي شخص بأجر. والشراكة تموّل المتحف والتجارب والتكوين والعناية بالأماكن، وتمنح فريقكم دورًا حقيقيًا فيها.',
    'Under Hadrian, Rome built a temple around a mountain spring at Zaghouan. From here an aqueduct carried water more than 90 kilometres to Carthage, one of the longest in the Roman world. The temple is the monumental head of that system. Niches once held statues of water deities, laurel friezes ran along the cornices, and a Latin slab recorded who paid for it.':
        'في عهد هادريان، بنت روما معبدًا حول منبع جبلي في زغوان. ومن هناك حملت قناة مائية الماء أكثر من 90 كيلومترًا إلى قرطاج، وهي من أطول القنوات في العالم الروماني. والمعبد هو الرأس الضخم لذلك النظام. كانت الحنايا تحتضن تماثيل لآلهة المياه، وتمتدّ أفاريز الغار على الكرانيش، وسجّلت لوحة لاتينية أسماء من موّلوا البناء.',
    'The first community-led virtual museum of Tunisian heritage. Every artifact inside was\nscanned in Tunisia by our volunteers and optimized by volunteers around the world; the rooms are modeled by hand so\nanyone in the community can build a new one. Built in Unity with photogrammetry and Gaussian splats. Still in\nprogress, this is what it looks like today.':
        'أوّل متحف افتراضي للتراث التونسي يقوده مجتمع من المتطوّعين. كل قطعة بداخله مسحها متطوّعونا في تونس وحسّنها متطوّعون من مختلف أنحاء العالم؛ أمّا القاعات فمُنمذجة يدويًا حتى يتمكّن أي شخص في المجموعة من بناء قاعة جديدة. بُني بمحرّك Unity بالمسح التصويري والسحابات الغاوسية. وما زال العمل جاريًا، وهذا شكله اليوم.',
    'The medina grew around the Zitouna Mosque and became one of the great cities of the Islamic world under the Almohads and the Hafsids. It is not a ruin. People live and work here now. These scans are doors, wells, looms and prayer niches recorded in streets that are still in daily use, including the Madrasa Al Bachia of 1752 and the Medersa Slimanya.':
        'نمت المدينة حول جامع الزيتونة وصارت من كبرى مدن العالم الإسلامي في عهد الموحّدين والحفصيين. وهي ليست أطلالًا؛ فالناس يعيشون ويعملون فيها اليوم. هذه العمليات وثّقت أبوابًا وآبارًا وأنوالًا ومحاريب في شوارع ما زالت مستعملة يوميًا، ومنها المدرسة الباشية لسنة 1752 والمدرسة السليمانية.',
    'Tanit XR is volunteers in Tunisia, the United States, Europe and Nigeria who meet\nevery week. We scan on the ground and optimize remotely, learn the history behind every object, run workshops,\nmentor students, attend events together, and share Tunisian culture with people who had never heard of Carthage.\nEverything we make is free and open.':
        'Tanit XR هم متطوّعون في تونس والولايات المتحدة وأوروبا ونيجيريا يلتقون كل أسبوع. نمسح على الأرض ونحسّن النماذج عن بُعد، ونتعلّم تاريخ كل قطعة، وننظّم ورشات، ونرافق الطلبة، ونحضر الفعاليات معًا، ونعرّف بالثقافة التونسية أشخاصًا لم يسمعوا بقرطاج من قبل. وكل ما ننجزه مجاني ومفتوح.',
    "A donation goes straight into the work: a volunteer's bus fare and mobile data for a day of scanning, a\nmonth of hosting for the free archive, a workshop that teaches someone in Tunisia to capture their own\nheritage, and one day a proper scanner so the community can record more than a phone allows. Here is what\neach amount does.":
        'يذهب التبرّع مباشرة إلى العمل: تذكرة الحافلة وباقة الإنترنت لمتطوّع في يوم مسح، وشهر من الاستضافة للأرشيف المجاني، وورشة تعلّم شخصًا في تونس كيف يوثّق تراثه بنفسه، ويومًا ما ماسحًا حقيقيًا حتى تتمكّن المجموعة من تسجيل أكثر ممّا يتيحه الهاتف. وهذا ما يفعله كل مبلغ.',
    'Mostly on Slack, across four continents and as many time zones. Once a week we meet on a call, Thursdays at 12 pm Eastern, 5 pm in Tunisia, to look at new scans, learn the history behind them and help each other with whatever is stuck. Julia records a short history lesson each week for anyone who cannot make it.':
        'أساسًا على سلاك، عبر أربع قارّات وأربع مناطق زمنية. ومرّة في الأسبوع نلتقي في مكالمة، يوم الخميس على منتصف النهار بتوقيت شرق الولايات المتحدة، أي الخامسة مساءً في تونس، لنشاهد عمليات المسح الجديدة ونتعلّم تاريخها ويساعد بعضنا بعضًا فيما تعثّر. وتسجّل جوليا كل أسبوع درسًا تاريخيًا قصيرًا لمن لا يستطيع الحضور.',
    'Skills-based volunteering with a clear task: optimise a scan for the web, research an object&#x27;s history, translate a label into French or Arabic, build a piece of the virtual museum. Half a day or a season, online, with a volunteer of ours alongside. Everything your team makes is published under their names.':
        'تطوّع بالمهارات ومهمّة واضحة: تحسين مسح للويب، أو البحث في تاريخ قطعة، أو ترجمة بطاقة تعريفية إلى الفرنسية أو العربية، أو بناء جزء من المتحف الافتراضي. نصف يوم أو موسم كامل، عبر الإنترنت، ومعك أحد متطوّعينا. وكل ما ينجزه فريقك يُنشر بأسمائهم.',
    'Your work is credited to you, on your own page here and on every model you touch. You learn photogrammetry, 3D and XR by doing them on real heritage. Students get portfolio reviews, mock interviews and mentoring from people working in the field. And you become part of a community that genuinely likes each other.':
        'يُنسب عملك إليك، على صفحتك الخاصة هنا وعلى كل نموذج تشارك فيه. تتعلّم المسح التصويري والتصميم ثلاثي الأبعاد والواقع الممتد بممارستها على تراث حقيقي. ويحصل الطلبة على مراجعة لأعمالهم ومقابلات تجريبية ومرافقة من أشخاص يعملون في المجال. وتصبح جزءًا من مجموعة يحبّ أفرادها بعضهم فعلًا.',
    "Every object our volunteers have scanned in Tunisia, one at a\ntime, in 3D, in your browser. Turn each one with a finger. Nura, our guide, floats beside you and\ntells you what you are looking at. Save the ones you love, share them, collect badges, step into\neach maker's own gallery, or put on a headset.":
        'كل قطعة مسحها متطوّعونا في تونس، واحدة تلو الأخرى، بثلاثة أبعاد، داخل متصفّحك. أدِرها بإصبعك. تحوم نورا، دليلتنا، إلى جانبك وتحدّثك عمّا تراه. احفظ ما يعجبك، وشاركه، واجمع الأوسمة، وادخل معرض كل صانع، أو ارتدِ نظّارة الواقع الافتراضي.',
    "No. Our first scans were made with a phone by someone who had never scanned anything. People here write, design, research, teach, translate, organise trips, model objects, clean up scans, apply for grants and run our social media. If you are curious about Tunisia's history, there is a place for you.":
        'لا. أوّل عمليات مسح قمنا بها كانت بهاتف، وأنجزها شخص لم يسبق له أن مسح أي شيء. هنا يكتب الناس ويصمّمون ويبحثون ويعلّمون ويترجمون وينظّمون الرحلات ويصنعون النماذج وينقّحون عمليات المسح ويقدّمون طلبات المنح ويديرون حساباتنا على وسائل التواصل. إن كان تاريخ تونس يثير فضولك، فلك مكان بيننا.',
    'Not yet. Everyone at Tanit XR is a volunteer, including the founders, and most costs so far have come out of our own pockets. We will never ask volunteers to work so that someone else earns; when funding arrives, the first people we want to pay are the volunteers on the ground in Tunisia.':
        'ليس بعد. كل من في Tanit XR متطوّع، بمن فيهم المؤسّسون، ومعظم المصاريف حتى الآن جاءت من جيوبنا الخاصة. ولن نطلب يومًا من المتطوّعين أن يعملوا ليكسب غيرهم؛ وحين يصل التمويل، فإنّ أوّل من نريد أن ندفع لهم هم المتطوّعون العاملون على الأرض في تونس.',
    'This intricately designed niche is part of the Roman Water Temple in Zaghouan, constructed during the reign of Emperor Hadrian in the 2nd century CE. The temple marked the starting point of the massive aqueduct that carried fresh water over 90 kilometers to the city of Carthage.':
        'هذه الحنيّة الدقيقة الزخرفة جزء من معبد المياه الروماني في زغوان، الذي بُني في عهد الإمبراطور هادريان في القرن الثاني الميلادي. وكان المعبد نقطة انطلاق القناة المائية الضخمة التي حملت الماء العذب أكثر من 90 كيلومترًا إلى مدينة قرطاج.',
    'Our heritage challenge ran at the official Major League Hacking hack day hosted by Florida Community Innovation at the University of Florida, with two tracks: build an interactive experience from one of our real 3D scans, or make a public history piece with no code needed.':
        'أُقيم تحدّي التراث الذي نظّمناه ضمن يوم الهاكاثون الرسمي لـ Major League Hacking الذي استضافته Florida Community Innovation في جامعة فلوريدا، بمسارين: بناء تجربة تفاعلية انطلاقًا من أحد نماذجنا ثلاثية الأبعاد الحقيقية، أو إنجاز عمل في التاريخ العام لا يحتاج أي برمجة.',
    'Alyssa George, illustrator and designer from the University of South Florida, draws\nthe Tanit XR story: an amphora heading to class, volunteers on every continent, the Draped Statue of Byrsa Hill\nappearing on a phone, and the murex shell that gave Carthage its purple.':
        'أليسا جورج، رسّامة ومصمّمة من جامعة جنوب فلوريدا، ترسم قصة Tanit XR: جرّة تتّجه إلى الدرس، ومتطوّعون في كل القارّات، والتمثال المكسوّ بالثوب من تل بيرصا يظهر على شاشة هاتف، وصدفة الموركس التي منحت قرطاج لونها الأرجواني.',
    'As much as you can give. Tasks are small and self-contained: one scan to clean up, one object to research, one article to write. Some people come to the Thursday call every week, some appear once a month. You set the pace and you can pause whenever life gets busy.':
        'بقدر ما تستطيع أن تعطي. المهام صغيرة ومستقلّة: مسح يحتاج تنقيحًا، قطعة تحتاج بحثًا، مقال يحتاج كتابة. بعضهم يحضر مكالمة الخميس كل أسبوع، وبعضهم يظهر مرّة في الشهر. أنت من يحدّد الإيقاع، ويمكنك التوقّف مؤقّتًا كلّما انشغلت الحياة.',
    'Our founder and team speak on community XR, phone 3D capture and heritage at risk: AWE, Voices of VR, Georgia Tech, the El Jem conference. Or we bring the 3D experience and a headset to your conference or office, with a volunteer to guide people through it.':
        'تتحدّث مؤسِّستنا وفريقنا عن الواقع الممتد المجتمعي والتقاط النماذج ثلاثية الأبعاد بالهاتف والتراث المهدّد: في AWE وVoices of VR وجورجيا تك ومؤتمر الجم. أو نأتي بالتجربة ثلاثية الأبعاد ونظّارة إلى مؤتمركم أو مكتبكم، مع متطوّع يرافق الحاضرين خلالها.',
    'Open call presented by the XR Women Museum inviting submissions around the theme “Vibrancy as Practice.” Submit via the official form linked from the call announcement. Check the external link for the most current submission requirements and timeline.':
        'دعوة مفتوحة يطلقها XR Women Museum لتقديم الأعمال حول موضوع "Vibrancy as Practice". تُقدَّم المشاركات عبر الاستمارة الرسمية المرفقة بإعلان الدعوة. راجع الرابط الخارجي للاطّلاع على أحدث شروط التقديم والمواعيد.',
    "Tanit XR is run entirely by volunteers. Nobody is paid, and most of what you see here, the scanning\ntrips, the tools, the hosting, the hackathon prizes, has so far been paid out of our founders' own pockets.\nThat cannot last, and it should not.":
        'يُدار Tanit XR بالكامل بجهود المتطوّعين. لا أحد يتقاضى أجرًا، ومعظم ما ترونه هنا، من رحلات المسح والأدوات والاستضافة وجوائز الهاكاثون، دفعه المؤسّسون حتى الآن من جيوبهم. هذا لا يمكن أن يستمرّ، ولا ينبغي له أن يستمرّ.',
    'That is honestly most of it. Walk a full circle around the object with your phone, then\nanother circle a little higher, then one lower, so every photo overlaps the last. We use\nScaniverse, which is free. Nura is showing you the path right now.':
        'هذا هو الجزء الأكبر منها بصراحة. دُر دورة كاملة حول القطعة بهاتفك، ثم دورة أخرى أعلى قليلًا، ثم دورة أدنى، بحيث تتداخل كل صورة مع التي قبلها. نحن نستعمل Scaniverse، وهو مجاني. ونورا تريك المسار الآن.',
    'Tanit XR is powered by volunteers: 3D scanning, model cleanup, XR development, historical research, writing, translation, and storytelling. Join from Tunisia or anywhere in the world, all experience levels welcome, fully remote friendly.':
        'يقوم Tanit XR على المتطوّعين: مسح ثلاثي الأبعاد، وتنقيح النماذج، وتطوير الواقع الممتد، والبحث التاريخي، والكتابة، والترجمة، وسرد القصص. انضمّ من تونس أو من أي مكان في العالم، وكل المستويات مرحّب بها، والعمل عن بُعد ممكن بالكامل.',
    'Global network connecting youth-led organizations working on climate action, education, heritage, science, and communication. Members collaborate, access capacity-building, share knowledge, and participate in UNESCO climate initiatives.':
        'شبكة عالمية تجمع منظمات يقودها شباب وتعمل في مجالات العمل المناخي والتعليم والتراث والعلوم والاتصال. يتعاون الأعضاء، ويستفيدون من بناء القدرات، ويتبادلون المعرفة، ويشاركون في مبادرات اليونسكو المناخية.',
    'With the authorities who look after the sites, a day of cleaning and care at a coastal site with local volunteers: travel, meals, gloves and bags, and a modest fee for the locals who show up. The sea is the clock we work against.':
        'بالتعاون مع السلطات التي ترعى المواقع، يوم تنظيف وعناية في موقع ساحلي مع متطوّعين محلّيين: التنقّل، والوجبات، والقفازات والأكياس، ومنحة بسيطة لأهل المنطقة الذين يحضرون. البحر هو الساعة التي نسابقها.',
    'A free, growing library of 3D scans of Tunisia’s endangered\nheritage, mosaics, statues, stelae, and ruins captured by our volunteers. Every model can be explored\ninteractively, and viewed in augmented reality on your phone.':
        'مكتبة مجانية ومتنامية من عمليات المسح ثلاثي الأبعاد للتراث التونسي المهدّد: فسيفساء وتماثيل ونصب وأطلال وثّقها متطوّعونا. يمكن استكشاف كل نموذج بشكل تفاعلي ومشاهدته بالواقع المعزّز على هاتفك.',
    'Al Jazeera&#x27;s culture desk profiled Tanit XR in Arabic: a non-profit building a precise digital library of Tunisia&#x27;s sites and artifacts with photogrammetry and Gaussian splats, before time and neglect erase them.':
        'خصّص القسم الثقافي في الجزيرة تقريرًا عن Tanit XR بالعربية: جمعية غير ربحية تبني مكتبة رقمية دقيقة للمواقع والقطع التونسية بالمسح التصويري والسحابات الغاوسية، قبل أن يمحوها الزمن والإهمال.',
    'Tanit XR&#x27;s heritage challenge at the official MLH Hack Day hosted by Florida Community Innovation at the University of Florida: build something usable from our 3D scans, or a public-history project that needs no code.':
        'تحدّي التراث من Tanit XR في يوم الهاكاثون الرسمي لـ MLH الذي تستضيفه Florida Community Innovation في جامعة فلوريدا: ابنِ شيئًا قابلًا للاستعمال انطلاقًا من نماذجنا ثلاثية الأبعاد، أو أنجز مشروعًا في التاريخ العام لا يحتاج أي برمجة.',
    'By Laura Harrison, Scientific Director, TanitXR. Scientific Director, TanitXR A scruffy brown donkey lowered its eyelids as a merchant filled its wooden cart with stacked bins of corn and melons. We saw several more like…':
        'بقلم لورا هاريسون، المديرة العلمية، TanitXR. المديرة العلمية، TanitXR خفض حمار بنّي أشعث جفنيه بينما كان تاجر يملأ عربته الخشبية بصناديق مكدّسة من الذرة والبطّيخ. ورأينا عدّة حمير أخرى مثله…',
    'By: Margarita Johnson The intense light illuminates the plateau of Byrsa Hill in Carthage, and the wind shakes the surviving fragments of an ancient city that once stood as a rival to Rome itself. Corinthian columns rise…':
        'بقلم: مارغريتا جونسون يغمر الضوء الساطع هضبة تل بيرصا في قرطاج، وتهزّ الريح ما تبقّى من شظايا مدينة قديمة كانت يومًا منافسة لروما نفسها. وترتفع أعمدة كورنثية…',
    'By: Margarita Johnson The new year began with Storm Harry sweeping across Tunisia’s Mediterranean coastline, reshaping the coastline and disturbing layers of sand that had settled undisturbed for centuries. Local observe…':
        'بقلم: مارغريتا جونسون بدأت السنة الجديدة بعاصفة هاري التي اجتاحت الساحل المتوسطي التونسي، فأعادت تشكيل الشاطئ وحرّكت طبقات من الرمل ظلّت ساكنة قرونًا. ويلاحظ سكان المنطقة…',
    'Tanit XR is taking part in CityCamp Gainesville Hack Day on Sunday, September 20, 2026, at the Reitz Union, University of Florida, an official MLH Hack Day hosted by Florida Community Innovation. Our challenge: build som…':
        'يشارك Tanit XR في يوم الهاكاثون CityCamp Gainesville يوم الأحد 20 سبتمبر 2026، في قاعة رايتز يونيون بجامعة فلوريدا، وهو يوم هاكاثون رسمي من MLH تستضيفه Florida Community Innovation. تحدّينا: أن تبنوا شيئًا…',
    'This is Tanit XR’s very first news article, and it feels right to begin with a story. Growing up among ruins I grew up in Tunisia surrounded by history. Walking past the ruins of Carthage felt ordinary, almost casual. An…':
        'هذا أوّل مقال إخباري لـ Tanit XR، ويبدو من المناسب أن نبدأ بحكاية. النشأة بين الأطلال نشأت في تونس محاطة بالتاريخ. كان المرور بجانب أطلال قرطاج أمرًا عاديًا، بل شبه عابر. و…',
    'Date/Period: 18th century (Husainid period) Material/Technique: Marble, carved plaster, qallaline ceramic tiles Description: This architectural element is a mahram, an ornamental niche inspired by the form of the mihrab.':
        'التاريخ/الحقبة: القرن الثامن عشر (العهد الحسيني) المادة/التقنية: رخام، جبس منحوت، زليج قلّالين الوصف: هذا العنصر المعماري هو محرم، وهو حنيّة زخرفية مستوحاة من شكل المحراب.',
    'Please write. We work with universities, museums, mapping communities and nonprofits, in Tunisia and beyond. The Unique Mappers in Nigeria are the first community bringing the model to a second country. Reach us at':
        'راسلنا من فضلك. نحن نعمل مع الجامعات والمتاحف ومجموعات رسم الخرائط والجمعيات، في تونس وخارجها. ومجموعة Unique Mappers في نيجيريا هي أوّل مجتمع ينقل هذه التجربة إلى بلد ثانٍ. تواصل معنا على',
    'Courses, mentoring for students, hosting and tools, the weekly call across four continents. The unglamorous part that keeps eighty-five volunteers working, and the first paid coordinator when we can afford one.':
        'دروس، ومرافقة للطلبة، واستضافة وأدوات، والمكالمة الأسبوعية عبر أربع قارّات. هذا هو الجانب غير اللامع الذي يبقي خمسة وثمانين متطوّعًا في العمل، وأوّل منسّق بأجر حين نقدر على ذلك.',
    'One promise we keep whatever the partnership: the archive stays free and open,\nand our volunteers are never made to work so that someone else earns. We sell training, events and our time, never the heritage.':
        'وعد واحد نحفظه مهما كانت الشراكة: يبقى الأرشيف مجانيًا ومفتوحًا، ولا يُطلب من متطوّعينا أبدًا أن يعملوا ليكسب غيرهم. نحن نبيع التكوين والفعاليات ووقتنا، ولا نبيع التراث أبدًا.',
    'A workshop for your team on phone photogrammetry, on objects and places we are free to scan, with the method our volunteers use. A skill people keep, and a new way to look at the street they walk every day.':
        'ورشة لفريقك حول المسح التصويري بالهاتف، على قطع وأماكن يُسمح لنا بمسحها، بالطريقة نفسها التي يستعملها متطوّعونا. مهارة تبقى مع أصحابها، ونظرة جديدة إلى الشارع الذي يمرّون به كل يوم.',
    'A curated board of grants, residencies, fellowships, open calls,\nand events for artists, XR creators, educators, students, and changemakers, updated regularly by the\nTanit XR team. Also published as our':
        'لوحة منتقاة من المنح والإقامات الفنية والزمالات والدعوات المفتوحة والفعاليات، موجّهة للفنانين وصنّاع الواقع الممتد والمعلّمين والطلبة وصنّاع التغيير، يحدّثها فريق Tanit XR بانتظام. ويُنشر أيضًا في إطار',
    'Your developers and designers, our volunteers and our published scans, one weekend or one quarter: an AR lesson, a VR room, a piece for your own event. The kind of project your team asks to be part of.':
        'مطوّروكم ومصمّموكم، ومتطوّعونا ونماذجنا المنشورة، في عطلة أسبوع واحدة أو في فصل كامل: درس بالواقع المعزّز، أو قاعة بالواقع الافتراضي، أو عمل خاص بفعاليتكم. هذا هو نوع المشاريع التي يطلب فريقكم أن يكون جزءًا منها.',
    'Remote volunteers turn raw scans into game-ready models, AR lessons and our virtual museum.':
        'يحوّل المتطوّعون عن بُعد عمليات المسح الخام إلى نماذج جاهزة للألعاب ودروس بالواقع المعزّز ومتحفنا الافتراضي.',
    'The Tanit Stela in 3D, with Nura the guide floating beside it':
        'نصب تانيت بثلاثة أبعاد، وإلى جانبه نورا الدليلة تحوم',
    "A maker's gallery: pieces on plinths in a round room":
        'معرض أحد الصنّاع: قطع على قواعد في قاعة مستديرة',
    'The museum&#x27;s main hall, Made by volunteers': 'القاعة الرئيسية للمتحف، من إنجاز المتطوّعين',
    'Al Jazeera, Al Jazeera · Culture feature': 'الجزيرة، الجزيرة · تقرير ثقافي',
    'Hall III &nbsp;·&nbsp; feature object': 'القاعة الثالثة  ·  القطعة البارزة',
    'Hall II &nbsp;·&nbsp; feature object': 'القاعة الثانية  ·  القطعة البارزة',
    'Hall IV &nbsp;·&nbsp; feature object': 'القاعة الرابعة  ·  القطعة البارزة',
    'The museum&#x27;s main hall 3D model': 'القاعة الرئيسية للمتحف، نموذج ثلاثي الأبعاد',
    'Hall I &nbsp;·&nbsp; feature object': 'القاعة الأولى  ·  القطعة البارزة',
    'Hall V &nbsp;·&nbsp; feature object': 'القاعة الخامسة  ·  القطعة البارزة',
    'Ceramic Plate, Made by volunteers': 'طبق خزفي، من إنجاز المتطوّعين',
    'Modern Tagine, Made by volunteers': 'طاجين حديث، من إنجاز المتطوّعين',
    'Underground Passageways 3D model': 'ممرّات تحت الأرض، نموذج ثلاثي الأبعاد',
    'Murex Shell, Made by volunteers': 'صدفة الموركس، من إنجاز المتطوّعين',
    'Splats With Phones – TANIT XR': 'السحابات الغاوسية بالهاتف – TANIT XR',
    'Wall Lamp, Made by volunteers': 'مصباح حائط، من إنجاز المتطوّعين',
    'Al Jazeera · Culture feature': 'الجزيرة · تقرير ثقافي',
    'Ruins on the Tunisian coast': 'أطلال على الساحل التونسي',
    'Walk through the collection': 'تجوّل في المجموعة',
    'Bamboo, Made by volunteers': 'خيزران، من إنجاز المتطوّعين',
    'Pillar, Made by volunteers': 'عمود، من إنجاز المتطوّعين',
    '›&nbsp; Splats With Phones': '›  السحابات الغاوسية بالهاتف',
    'Optimize &amp;amp; Build': 'التحسين &amp; البناء',
    'Research &amp;amp; Share': 'البحث &amp; المشاركة',
    'Architectural Fragments': 'شظايا معمارية',
    'Rug, Made by volunteers': 'زربية، من إنجاز المتطوّعين',
    'Scan &amp;amp; Preserve': 'المسح &amp; الحفظ',
    'Underground Passageways': 'ممرّات تحت الأرض',
    'Ceramic Plate 3D model': 'طبق خزفي، نموذج ثلاثي الأبعاد',
    'Modern Tagine 3D model': 'طاجين حديث، نموذج ثلاثي الأبعاد',
    '›&nbsp; ImmerseGT 2026': '›  ImmerseGT 2026',
    'Mentor &amp;amp; Grow': 'الإرشاد &amp; النموّ',
    'Press & Recognition': 'الصحافة والتكريمات',
    'Corinthian Capital': 'تاج عمود كورنثي',
    'Made by volunteers': 'من إنجاز المتطوّعين',
    'Splats With Phones': 'السحابات الغاوسية بالهاتف',
    'Wall Lamp 3D model': 'مصباح حائط، نموذج ثلاثي الأبعاد',
    'Community Liaison': 'منسّق العلاقات المجتمعية',
    'Makers’ galleries': 'معارض الصنّاع',
    'A lasting record': 'سجلّ يدوم',
    'Reclining Figure': 'تمثال مستلقٍ',
    'Regional Manager': 'المسؤول الإقليمي',
    'Traditional Door': 'باب تقليدي',
    'Bamboo 3D model': 'خيزران، نموذج ثلاثي الأبعاد',
    'Chief Scientist': 'المسؤول العلمي',
    'Pillar 3D model': 'عمود، نموذج ثلاثي الأبعاد',
    'Project Manager': 'مدير المشروع',
    'Statue Fragment': 'شظية تمثال',
    'Turn any object': 'أدِر أي قطعة',
    'Save and share': 'احفظ وشارك',
    'Bust Fragment': 'شظية تمثال نصفي',
    'Ceramic Plate': 'طبق خزفي',
    'Draped Statue': 'تمثال مكسوّ بالثوب',
    'Illustration:': 'الرسوم:',
    'Medium Object': 'قطعة متوسطة',
    'Modern Tagine': 'طاجين حديث',
    'Mihrab Niche': 'حنيّة محراب',
    'Publications': 'المنشورات',
    'Punic Stelae': 'نصب بونية',
    'Roman Column': 'عمود روماني',
    'Rug 3D model': 'زربية، نموذج ثلاثي الأبعاد',
    'Sacred Niche': 'حنيّة مقدّسة',
    'Small Object': 'قطعة صغيرة',
    'Murex Shell': 'صدفة الموركس',
    'Punic Stela': 'نصب بوني',
    'Stone Basin': 'حوض حجري',
    'Tanit Stela': 'نصب تانيت',
    'Works in VR': 'يعمل بالواقع الافتراضي',
    'Al Jazeera': 'الجزيرة',
    'Byrsa Hill': 'تل بيرصا',
    'Large Area': 'مساحة كبيرة',
    'Newsletter': 'النشرة البريدية',
    'Niche Wall': 'جدار الحنايا',
    'Community': 'المجتمع',
    'Galleries': 'المعارض',
    'Meet Nura': 'تعرّف على نورا',
    'Volunteer': 'التطوّع',
    'Wall Lamp': 'مصباح حائط',
    'Articles': 'مقالات',
    'Carthage': 'قرطاج',
    'Français': 'الفرنسية',
    'Kairouan': 'القيروان',
    'Neapolis': 'نيابوليس',
    'Services': 'الخدمات',
    'project.': 'مشروع.',
    'Caption': 'التعليق',
    'Contact': 'اتصل بنا',
    'English': 'الإنجليزية',
    'Explore': 'استكشف',
    'Founder': 'المؤسِّسة',
    'Gallery': 'معرض',
    'Message': 'الرسالة',
    'Objects': 'القطع',
    'Badges': 'الأوسمة',
    'Bamboo': 'خيزران',
    'Choose': 'اختر',
    'Period': 'الحقبة',
    'Pillar': 'عمود',
    'Record': 'تسجيل',
    'Share…': 'مشاركة…',
    'Clear': 'مسح',
    'Close': 'إغلاق',
    'Email': 'البريد الإلكتروني',
    'Halls': 'القاعات',
    'Logon': 'تسجيل الدخول',
    'Punic': 'بوني',
    'Saved': 'محفوظ',
    'Sound': 'الصوت',
    'saved': 'محفوظ',
    'Join': 'انضمّ',
    'Menu': 'القائمة',
    'Mode': 'الوضع',
    'More': 'المزيد',
    'Site': 'الموقع',
    'Type': 'النوع',
    'Map': 'خريطة',
    'New': 'جديد',
    'Oct': 'أكتوبر',
    'Rug': 'زربية',

    # ---- added 2026-09-21: pages that were still English ----
    'Our mission is to preserve Tunisia’s endangered heritage through digital scans, immersive technology, and\neducation. With every artifact we scan and every volunteer we train, we are proving that heritage can be\nsafeguarded for future generations, no matter the threats of climate change and neglect.':
        'مهمتنا هي حفظ التراث التونسي المهدّد عبر المسح الرقمي والتقنيات الغامرة والتعليم. مع كل قطعة نمسحها وكل\nمتطوّع ندرّبه، نثبت أن التراث يمكن صونه للأجيال القادمة، رغم تغيّر المناخ والإهمال.',
    'Ana Beatriz Vega González': 'آنا بياتريث فيغا غونثاليث',
    'Ines scanning at Carthage': 'إيناس تقوم بالمسح في قرطاج',
    'Caroline Nickerson, PhD': 'د. كارولين نيكرسون',
    'Dr. Caroline Nickerson': 'د. كارولين نيكرسون',
    'Dr. Laura Harrison': 'د. لورا هاريسون',

    # ---- added 2026-09-21: pages that were still English ----
    '›\xa0 ImmerseGT 2026': '›  ImmerseGT 2026',

    # ---- added 2026-09-21: pages that were still English ----
    'Tanit XR&#x27;s work was shown in the XR Women Museum, including its &quot;Garden: In Full Bloom&quot; exhibition, an immersive museum of 30+ gallery worlds directed by Paige Dansinger.':
        'عُرض عمل Tanit XR في XR Women Museum، ضمن معرضه "Garden: In Full Bloom"، وهو متحف غامر يضمّ أكثر من 30 عالمًا معرضيًا تديره بيج دانسينجر.',
    'Al Jazeera, &quot;Tanit XR&quot;: a non-profit platform documenting Tunisian heritage digitally (Arabic)':
        'الجزيرة، "Tanit XR": منصّة غير ربحية توثّق التراث التونسي رقميًا (بالعربية)',
    '&quot;Apteranthes europaea&quot; cactus': 'صبّار "Apteranthes europaea"',

    # ---- added 2026-09-21: pages that were still English ----
    "Get new grants, residencies, and open calls for art, XR &amp; impact in your\ninbox, free, from the Tanit XR team. You'll also be first to hear how our heritage-preservation work is\ngoing.":
        'احصلوا مجانًا على المنح والإقامات الفنية والدعوات المفتوحة في الفن والواقع الممتد والأثر الاجتماعي،\nمباشرة من فريق Tanit XR. وستكونون أول من يعرف أخبار عملنا في حفظ التراث.',

    # ---- added 2026-09-21: pages that were still English ----
    'Artifacts scanned': 'قطع أثرية ممسوحة',
    'Sites documented': 'مواقع موثّقة',
    'Global reach': 'امتداد عالمي',

    # ---- added 2026-09-21: pages that were still English ----
    'Continue to Press &amp; Recognition': 'المتابعة إلى الصحافة والتقدير',
    'Press &amp; Recognition – Tanit XR': 'الصحافة والتقدير – Tanit XR',
    '3D Modeler &amp; Web Contributor': 'نمذجة ثلاثية الأبعاد ومساهمة في الويب',
    'Strategy &amp; Creative Support': 'الاستراتيجية والدعم الإبداعي',
    'The museum&#x27;s main hall': 'القاعة الرئيسية للمتحف',

    # ---- added 2026-09-21: pages that were still English ----
    'Save &#9825;': 'حفظ &#9825;',

    # ---- added 2026-09-21: roles that were only half translated ----
    'Partnerships &amp; Community': 'الشراكات والمجتمع',
    '2D Design &amp; 3D Generalist': 'تصميم ثنائي الأبعاد ومصمّم ثلاثي الأبعاد متعدّد المهام',
}

