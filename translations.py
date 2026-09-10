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
    "Any level is welcome — pick one": "Tous les niveaux sont bienvenus — choisissez",
    "This course is live and interactive — pick one": "Ce cours est en direct et interactif — choisissez",
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
    "Focus on texture and angles — walk around the object fully": "Soignez la texture et les angles — faites le tour complet de l’objet",
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
    "No spam — opportunities and Tanit XR news only. Also published on": "Pas de spam — uniquement des opportunités et des nouvelles de Tanit XR. Également publié sur",

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
    "Any level is welcome — pick one": "كل المستويات مرحّب بها — اختر",
    "This course is live and interactive — pick one": "هذه الدورة مباشرة وتفاعلية — اختر",
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
    "Focus on texture and angles — walk around the object fully": "اهتم بالملمس والزوايا — دُر حول الشيء دورة كاملة",
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
    "No spam — opportunities and Tanit XR news only. Also published on": "لا رسائل مزعجة — فرص وأخبار تانيت XR فقط. تُنشر أيضًا على",

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
}

