# French and Arabic for the Explore page's runtime: the strings that live in
# assets-src/walk.js and in the per-object config build.py inlines into the page.
# The site-wide table (translations.py) never touches <script> blocks, so without this
# a French or Arabic visitor met an English Nura, English badges and English captions.
#
# UI: keys are the exact single-quoted literals in walk.js. build.py writes
# assets/walk.fr.js and assets/walk.ar.js by swapping each literal for its translation,
# quotes included, so nothing can match inside a longer word or an identifier.
# Fragments that are concatenated in the code (' of ', ' to go.') are translated as
# fragments; the sentences were checked whole in both languages.
#
# OPENERS: Nura's per-area opening lines, keyed by the English line in build.py.
# CREDIT: the pieces walk_credit() glues together.

UI = {
"fr": {
    'Hear Nura tell it': 'Écouter Nura',
    'Read this aloud': 'Lire à voix haute',
    'Tell me more': 'Dis-m’en plus',
    'Thanks, Nura': 'Merci, Nura',
    'viewed ': 'vu ',
    '+ times': '+ fois',
    'Sound: on': 'Son : activé',
    'Sound: off': 'Son : coupé',
    'Sound is on. Tap to mute.': 'Le son est activé. Touchez pour couper.',
    'Sound is off. Tap to turn it on.': 'Le son est coupé. Touchez pour l’activer.',
    'First Turn': 'Premier tour',
    'Turn an object with your cursor': 'Faites tourner un objet avec le curseur',
    'Curator': 'Conservateur',
    'Love five objects': 'Aimez cinq objets',
    'Good Listener': 'Bonne oreille',
    'Ask Nura for more on ten objects': 'Demandez à Nura d’en dire plus sur dix objets',
    'Site Surveyor': 'Arpenteur des sites',
    'See something from every place we have scanned': 'Voyez un objet de chaque lieu que nous avons numérisé',
    'Guardian': 'Gardien',
    'Share an object so others see it': 'Partagez un objet pour que d’autres le voient',
    'Whole Collection': 'Collection complète',
    'Look at every object': 'Regardez chaque objet',
    'That is everything ': 'Voilà tout ce que ',
    ' has made so far.': ' a réalisé jusqu’ici.',
    'That is every piece we have from ': 'Voilà toutes les pièces que nous avons de ',
    ' left in the whole collection.': ' restantes dans toute la collection.',
    ' locked': ' verrouillé',
    'Badge earned': 'Badge obtenu',
    'I earned the "': 'J’ai obtenu le badge « ',
    '" badge in the Tanit XR ': ' » dans la ',
    'collection: ': 'collection Tanit XR : ',
    ' of ': ' sur ',
    ' Tunisian artifacts, ': ' objets du patrimoine tunisien, ',
    'all scanned by volunteers with their phones.': 'tous numérisés par des bénévoles avec leur téléphone.',
    'I ': 'C’est moi qui l’ai ',
    ' this one.': '.',
    'See all ': 'Voir les ',
    ' in one room': ' ensemble dans une salle',
    'Come back out': 'Ressortir',
    'Step inside': 'Entrer',
    'Loved \\u2665': 'Aimé ♥',
    'Love \\u2661': 'Aimer ♡',
    'Share to protect it': 'Partagez pour le protéger',
    ', scanned in Tunisia by Tanit XR volunteers so it is never lost. Share it to help protect it.':
        ', numérisé en Tunisie par les bénévoles de Tanit XR pour qu’il ne soit jamais perdu. Partagez-le pour aider à le protéger.',
    ', modelled by ': ', modélisé par ',
    'a Tanit XR volunteer': 'un bénévole de Tanit XR',
    ' for the Tanit XR virtual museum. ': ' pour le musée virtuel de Tanit XR. ',
    'Volunteers from Tunisia and around the world learn Tunisian culture together and make pieces inspired by it. Share it to help the museum grow.':
        'Des bénévoles de Tunisie et du monde entier apprennent la culture tunisienne ensemble et créent des pièces qui s’en inspirent. Partagez-la pour aider le musée à grandir.',
    'Want to see how we make these?': 'Vous voulez voir comment nous les fabriquons ?',
    'Show me': 'Montre-moi',
    'Share it': 'Partager',
    'Know someone who would love this one? Share it. Every share keeps it seen.':
        'Vous connaissez quelqu’un qui aimerait celui-ci ? Partagez-le. Chaque partage le garde vivant.',
    'Donate': 'Faire un don',
    'Everything here is free and made by volunteers. If it means something to you, a small donation keeps it going.':
        'Tout ici est gratuit et fait par des bénévoles. Si cela compte pour vous, un petit don permet de continuer.',
    'Visit the gallery': 'Visiter la galerie',
    'This is one of ': 'C’est l’une des ',
    ' pieces ': ' pièces que ',
    ' made. Want to see them all together?': ' a réalisées. Vous voulez les voir toutes ensemble ?',
    'Join us': 'Rejoignez-nous',
    'We do this every Thursday, together, from four continents. You could be one of us.':
        'Nous faisons cela chaque jeudi, ensemble, depuis quatre continents. Vous pourriez être des nôtres.',
    'Subscribe': 'S’abonner',
    'Every two weeks we send grants and open calls for artists and XR makers. Want them in your inbox?':
        'Toutes les deux semaines, nous envoyons des bourses et des appels à candidatures pour artistes et créateurs XR. Vous les voulez dans votre boîte mail ?',
    'Love this one': 'Aimer celui-ci',
    'If one of these gets you, press Love. They gather in one place for you.':
        'Si l’un d’eux vous touche, appuyez sur Aimer. Ils se rassemblent au même endroit pour vous.',
    'See it in VR': 'Le voir en VR',
    'You can stand next to this one in your headset.': 'Vous pouvez vous tenir à côté de celui-ci dans votre casque.',
    'Welcome. I am Nura. Let me show you what a hundred volunteers built with their phones. This stone was set down in Carthage more than two thousand years ago. A volunteer scanned it in a few minutes.':
        'Bienvenue. Je suis Nura. Laissez-moi vous montrer ce qu’une centaine de bénévoles ont construit avec leur téléphone. Cette pierre a été posée à Carthage il y a plus de deux mille ans. Un bénévole l’a numérisée en quelques minutes.',
    'How do you scan a stone?': 'Comment numérise-t-on une pierre ?',
    'Not everything here is a scan. Rachel has never been to Tunisia. She learned its history on our Thursday calls and modelled this for our museum. Every volunteer gets a gallery of their own.':
        'Tout ici n’est pas une numérisation. Rachel n’est jamais allée en Tunisie. Elle a appris son histoire lors de nos appels du jeudi et a modélisé ceci pour notre musée. Chaque bénévole a sa propre galerie.',
    'In January a storm uncovered this ancient city for a few days. A volunteer reached the beach and scanned it before the sea took it back. This is the only 3D record that exists. It is why we hurry.':
        'En janvier, une tempête a mis au jour cette cité antique pendant quelques jours. Un bénévole a rejoint la plage et l’a numérisée avant que la mer ne la reprenne. C’est le seul relevé 3D qui existe. Voilà pourquoi nous nous pressons.',
    'Next': 'Suivant',
    'The volunteers are building a whole museum for these objects, room by room, in their free time. Patrick modelled this hall; others are furnishing it.':
        'Les bénévoles construisent un musée entier pour ces objets, salle après salle, sur leur temps libre. Patrick a modélisé cette salle, d’autres la meublent.',
    'My collection': 'Ma collection',
    'My collection of Tunisian heritage scanned by Tanit XR volunteers, ':
        'Ma collection de patrimoine tunisien numérisé par les bénévoles de Tanit XR, ',
    ' objects. Share them to help protect them.': ' objets. Partagez-les pour aider à les protéger.',
    'BADGE EARNED': 'BADGE OBTENU',
    ' objects seen in the Tanit XR collection': ' objets vus dans la collection Tanit XR',
    'Scanned by a Tanit XR volunteer': 'Numérisé par un bénévole de Tanit XR',
    'Share this': 'Partager',
    'Caption copied. Paste it into your post when it opens.': 'Légende copiée. Collez-la dans votre publication quand elle s’ouvre.',
    'Paste the caption from the box above into your post.': 'Collez la légende ci-dessus dans votre publication.',
    'Opening ': 'Ouverture de ',
    ' with the caption filled in.': ' avec la légende pré-remplie.',
    'Picture saved': 'Image enregistrée',
    'Save the picture': 'Enregistrez l’image',
    ' and caption copied. ': ' et légende copiée. ',
    'Open Instagram on your phone, make a post, pick the picture, paste the caption.':
        'Ouvrez Instagram sur votre téléphone, créez une publication, choisissez l’image, collez la légende.',
    'Link copied.': 'Lien copié.',
    'Picture saved to your downloads.': 'Image enregistrée dans vos téléchargements.',
    '♥  SAVED': '♥  ENREGISTRÉ',
    'POINT HERE AND PULL THE TRIGGER TO SAVE': 'VISEZ ICI ET PRESSEZ LA GÂCHETTE POUR ENREGISTRER',
    'Back to the collection': 'Retour à la collection',
    'Scanned in Tunisia': 'Numérisé en Tunisie',
    'Made by volunteers': 'Réalisé par des bénévoles',
    'Your saved objects (': 'Vos objets enregistrés (',
    'Your collection': 'Votre collection',
    'Leave passthrough': 'Quitter la vue mixte',
    'Leave VR': 'Quitter la VR',
    'W H E R E   T O': 'O Ù   A L L E R',
    ' object': ' objet',
    ' objects': ' objets',
    ' you saved': ' enregistrés',
    'Modelled by ': 'Modélisé par ',
    'Optimized by ': 'Optimisé par ',
    ' piece': ' pièce',
    ' pieces': ' pièces',
    ' built from scratch': ' créées de zéro',
    ' scan': ' numérisation',
    ' scans': ' numérisations',
    ' prepared for the web': ' préparées pour le web',
    'Up close': 'De près',
    'Gallery': 'Galerie',
    ' modelled': ' modélisés',
    ' optimized': ' optimisés',
    'Inside the museum hall, a preview': 'Dans la salle du musée, un aperçu',
    'Welcome back! ': 'Content de vous revoir ! ',
    ' seen so far, ': ' vus jusqu’ici, ',
    ' to go.': ' restants.',
    'Hi, I am Nura. Drag anything to turn it, save what you like, and see how many ':
        'Bonjour, je suis Nura. Faites glisser un objet pour le tourner, enregistrez ce qui vous plaît, et voyez combien de ',
    'badges you can collect along the way.': 'badges vous pouvez collectionner en chemin.',
    ' scans, ': ' numérisations, ',
    ' sites, ': ' sites, ',
    ' volunteers on four continents, and not one paid person. ': ' bénévoles sur quatre continents, et pas une seule personne payée. ',
    'Scans, sites, volunteers on four continents, and not one paid person. ': 'Des numérisations, des sites, des bénévoles sur quatre continents, et pas une seule personne payée. ',
    'Everything you saw is free, forever. This is what your support does.': 'Tout ce que vous avez vu est gratuit, pour toujours. Voilà ce que fait votre soutien.',
    '" target="_blank" rel="noopener">Donate</a>': '" target="_blank" rel="noopener">Faire un don</a>',
    '">Volunteer</a>': '">Devenir bénévole</a>',
    '">Subscribe</a></span>': '">S’abonner</a></span>',
    'Which one should I show your friend? Tap it and I will make the card.': 'Lequel dois-je montrer à ton ami ? Touche-le et je prépare la carte.',
    'Now look at the back. A volunteer walked all the way round it with a phone.': 'Regarde l’arrière maintenant. Un bénévole en a fait tout le tour avec un téléphone.',
    'Slow down on the details. The texture is the phone\\\'s own photos, stitched together.': 'Prends le temps des détails. La texture, ce sont les photos du téléphone, assemblées.',
    'Every side is real. Nothing here was invented to fill a gap.': 'Chaque face est vraie. Rien ici n’a été inventé pour combler un trou.',
    'Measured from the scan itself, not guessed.': 'Mesuré sur la numérisation elle-même, pas estimé.',
    'It was modelled by hand, so it has no measured size. In the museum it stands at a comfortable height.': 'Il a été modélisé à la main, donc sans mesure réelle. Au musée il est à hauteur confortable.',
    'The exact spot is on the map chip under the label.': 'L’endroit exact est sur la puce carte sous l’étiquette.',
    'A Tanit XR volunteer.': 'Un bénévole de Tanit XR.',
    'The label does not give a date for this one. The archive page has the full description.': 'L’étiquette ne donne pas de date pour celui-ci. La page d’archive a la description complète.',
    'The label does not name the material. Turn it and look at the surface: the scan keeps every grain.': 'L’étiquette ne nomme pas la matière. Tourne-le et regarde la surface : la numérisation garde chaque grain.',
    'Opening the share card for you.': 'J’ouvre la carte de partage.',
    'Kept. It is in your collection, top right.': 'Gardé. Il est dans ta collection, en haut à droite.',
    'Press See it in VR at the bottom of the page.': 'Appuie sur Le voir en VR en bas de la page.',
    'On a headset, this page has a See it in VR button. On a phone, Share gives you a picture to keep.': 'Sur un casque, cette page a un bouton Le voir en VR. Sur un téléphone, Partager te donne une image à garder.',
    'Everything here is free and made by volunteers. The Donate button under the label keeps it that way.': 'Tout ici est gratuit et fait par des bénévoles. Le bouton Faire un don sous l’étiquette permet que ça continue.',
    'That is all the label knows. The archive page has the full description, and the volunteer who made it may know more.': 'C’est tout ce que sait l’étiquette. La page d’archive a la description complète, et le bénévole qui l’a faite en sait peut-être plus.',
},
"ar": {
    'Hear Nura tell it': 'اسمع نورا تحكيها',
    'Read this aloud': 'اقرأ هذا بصوت عالٍ',
    'Tell me more': 'أخبريني أكثر',
    'Thanks, Nura': 'شكرًا يا نورا',
    'viewed ': 'شوهدت ',
    '+ times': '+ مرة',
    'Sound: on': 'الصوت: مشغّل',
    'Sound: off': 'الصوت: مكتوم',
    'Sound is on. Tap to mute.': 'الصوت مشغّل. انقر لكتمه.',
    'Sound is off. Tap to turn it on.': 'الصوت مكتوم. انقر لتشغيله.',
    'First Turn': 'أول دورة',
    'Turn an object with your cursor': 'أدِر قطعة بالمؤشر',
    'Curator': 'أمين المجموعة',
    'Love five objects': 'أحبب خمس قطع',
    'Good Listener': 'مستمع جيد',
    'Ask Nura for more on ten objects': 'اطلب من نورا المزيد عن عشر قطع',
    'Site Surveyor': 'مسّاح المواقع',
    'See something from every place we have scanned': 'شاهد قطعة من كل مكان مسحناه',
    'Guardian': 'حارس',
    'Share an object so others see it': 'شارك قطعة ليراها الآخرون',
    'Whole Collection': 'المجموعة كاملة',
    'Look at every object': 'شاهد كل القطع',
    'That is everything ': 'هذا كل ما أنجزه ',
    ' has made so far.': ' حتى الآن.',
    'That is every piece we have from ': 'هذه كل القطع التي لدينا من ',
    ' left in the whole collection.': ' متبقية في المجموعة كاملة.',
    ' locked': ' مقفل',
    'Badge earned': 'حصلت على شارة',
    'I earned the "': 'حصلت على شارة "',
    '" badge in the Tanit XR ': '" في ',
    'collection: ': 'مجموعة Tanit XR: ',
    ' of ': ' من ',
    ' Tunisian artifacts, ': ' قطعة من التراث التونسي، ',
    'all scanned by volunteers with their phones.': 'كلها مسحها متطوعون بهواتفهم.',
    'I ': 'أنا من ',
    ' this one.': ' هذه القطعة.',
    'See all ': 'شاهد كل الـ',
    ' in one room': ' في قاعة واحدة',
    'Come back out': 'اخرج',
    'Step inside': 'ادخل',
    'Loved \\u2665': 'أحببتها ♥',
    'Love \\u2661': 'أحبّها ♡',
    'Share to protect it': 'شارك لتحميها',
    ', scanned in Tunisia by Tanit XR volunteers so it is never lost. Share it to help protect it.':
        '، مسحها متطوعو Tanit XR في تونس حتى لا تضيع أبدًا. شاركها لتساعد في حمايتها.',
    ', modelled by ': '، صمّمها ',
    'a Tanit XR volunteer': 'متطوع من Tanit XR',
    ' for the Tanit XR virtual museum. ': ' لمتحف Tanit XR الافتراضي. ',
    'Volunteers from Tunisia and around the world learn Tunisian culture together and make pieces inspired by it. Share it to help the museum grow.':
        'متطوعون من تونس ومن حول العالم يتعلّمون الثقافة التونسية معًا ويصنعون قطعًا مستوحاة منها. شاركها لتساعد المتحف على النمو.',
    'Want to see how we make these?': 'تريد أن ترى كيف نصنع هذه؟',
    'Show me': 'أريني',
    'Share it': 'شاركها',
    'Know someone who would love this one? Share it. Every share keeps it seen.':
        'تعرف شخصًا سيحب هذه القطعة؟ شاركها. كل مشاركة تبقيها حيّة.',
    'Donate': 'تبرّع',
    'Everything here is free and made by volunteers. If it means something to you, a small donation keeps it going.':
        'كل ما هنا مجاني ومن صنع متطوعين. إن كان يعني لك شيئًا، فتبرّع صغير يبقيه مستمرًا.',
    'Visit the gallery': 'زُر المعرض',
    'This is one of ': 'هذه واحدة من ',
    ' pieces ': ' قطع صنعها ',
    ' made. Want to see them all together?': '. تريد رؤيتها كلها معًا؟',
    'Join us': 'انضم إلينا',
    'We do this every Thursday, together, from four continents. You could be one of us.':
        'نفعل هذا كل خميس، معًا، من أربع قارات. يمكنك أن تكون واحدًا منا.',
    'Subscribe': 'اشترك',
    'Every two weeks we send grants and open calls for artists and XR makers. Want them in your inbox?':
        'كل أسبوعين نرسل منحًا ودعوات مفتوحة للفنانين وصنّاع الواقع الممتد. تريدها في بريدك؟',
    'Love this one': 'أحبب هذه',
    'If one of these gets you, press Love. They gather in one place for you.':
        'إن أعجبتك إحداها، اضغط على القلب. تتجمّع كلها في مكان واحد لك.',
    'See it in VR': 'شاهدها بالواقع الافتراضي',
    'You can stand next to this one in your headset.': 'يمكنك الوقوف بجانب هذه القطعة في نظارتك.',
    'Welcome. I am Nura. Let me show you what a hundred volunteers built with their phones. This stone was set down in Carthage more than two thousand years ago. A volunteer scanned it in a few minutes.':
        'مرحبًا. أنا نورا. دعني أريك ما بناه مئة متطوع بهواتفهم. وُضع هذا الحجر في قرطاج قبل أكثر من ألفي عام. ومسحه متطوع في دقائق.',
    'How do you scan a stone?': 'كيف تمسح حجرًا؟',
    'Not everything here is a scan. Rachel has never been to Tunisia. She learned its history on our Thursday calls and modelled this for our museum. Every volunteer gets a gallery of their own.':
        'ليس كل ما هنا مسحًا. راشيل لم تزر تونس قط. تعلّمت تاريخها في مكالمات الخميس وصمّمت هذه القطعة لمتحفنا. لكل متطوع معرض خاص به.',
    'In January a storm uncovered this ancient city for a few days. A volunteer reached the beach and scanned it before the sea took it back. This is the only 3D record that exists. It is why we hurry.':
        'في جانفي كشفت عاصفة هذه المدينة القديمة لأيام قليلة. وصل متطوع إلى الشاطئ ومسحها قبل أن يستعيدها البحر. هذا هو السجل ثلاثي الأبعاد الوحيد الموجود. لهذا نسارع.',
    'Next': 'التالي',
    'The volunteers are building a whole museum for these objects, room by room, in their free time. Patrick modelled this hall; others are furnishing it.':
        'يبني المتطوعون متحفًا كاملًا لهذه القطع، قاعة بعد قاعة، في وقت فراغهم. باتريك صمّم هذه القاعة، وآخرون يؤثثونها.',
    'My collection': 'مجموعتي',
    'My collection of Tunisian heritage scanned by Tanit XR volunteers, ':
        'مجموعتي من التراث التونسي الذي مسحه متطوعو Tanit XR، ',
    ' objects. Share them to help protect them.': ' قطع. شاركها لتساعد في حمايتها.',
    'BADGE EARNED': 'شارة جديدة',
    ' objects seen in the Tanit XR collection': ' قطعة شوهدت في مجموعة Tanit XR',
    'Scanned by a Tanit XR volunteer': 'مسحها متطوع من Tanit XR',
    'Share this': 'شارك',
    'Caption copied. Paste it into your post when it opens.': 'نُسخ التعليق. ألصقه في منشورك عندما يُفتح.',
    'Paste the caption from the box above into your post.': 'ألصق التعليق من المربع أعلاه في منشورك.',
    'Opening ': 'جارٍ فتح ',
    ' with the caption filled in.': ' مع التعليق جاهزًا.',
    'Picture saved': 'حُفظت الصورة',
    'Save the picture': 'احفظ الصورة',
    ' and caption copied. ': ' ونُسخ التعليق. ',
    'Open Instagram on your phone, make a post, pick the picture, paste the caption.':
        'افتح إنستغرام على هاتفك، أنشئ منشورًا، اختر الصورة، وألصق التعليق.',
    'Link copied.': 'نُسخ الرابط.',
    'Picture saved to your downloads.': 'حُفظت الصورة في التنزيلات.',
    '♥  SAVED': '♥  محفوظة',
    'POINT HERE AND PULL THE TRIGGER TO SAVE': 'وجّه هنا واضغط الزناد للحفظ',
    'Back to the collection': 'العودة إلى المجموعة',
    'Scanned in Tunisia': 'مُسحت في تونس',
    'Made by volunteers': 'من إنجاز المتطوّعين',
    'Your saved objects (': 'قطعك المحفوظة (',
    'Your collection': 'مجموعتك',
    'Leave passthrough': 'الخروج من الوضع المختلط',
    'Leave VR': 'الخروج من الواقع الافتراضي',
    'W H E R E   T O': 'إ ل ى   أ ي ن',
    ' object': ' قطعة',
    ' objects': ' قطع',
    ' you saved': ' حفظتها',
    'Modelled by ': 'صمّمها ',
    'Optimized by ': 'حسّنها ',
    ' piece': ' قطعة',
    ' pieces': ' قطع',
    ' built from scratch': ' صُنعت من الصفر',
    ' scan': ' مسح',
    ' scans': ' مسوحات',
    ' prepared for the web': ' جُهّزت للويب',
    'Up close': 'عن قرب',
    'Gallery': 'معرض',
    ' modelled': ' مصمّمة',
    ' optimized': ' محسّنة',
    'Inside the museum hall, a preview': 'داخل قاعة المتحف، معاينة',
    'Welcome back! ': 'أهلًا بعودتك! ',
    ' seen so far, ': ' شاهدتها حتى الآن، ',
    ' to go.': ' متبقية.',
    'Hi, I am Nura. Drag anything to turn it, save what you like, and see how many ':
        'مرحبًا، أنا نورا. اسحب أي قطعة لتديرها، واحفظ ما يعجبك، وانظر كم ',
    'badges you can collect along the way.': 'شارة يمكنك جمعها في الطريق.',
    ' scans, ': ' مسحًا، ',
    ' sites, ': ' مواقع، ',
    ' volunteers on four continents, and not one paid person. ': ' متطوعًا في أربع قارات، ولا شخص واحد مدفوع الأجر. ',
    'Scans, sites, volunteers on four continents, and not one paid person. ': 'مسوحات ومواقع ومتطوعون في أربع قارات، ولا شخص واحد مدفوع الأجر. ',
    'Everything you saw is free, forever. This is what your support does.': 'كل ما رأيته مجاني، إلى الأبد. هذا ما يفعله دعمك.',
    '" target="_blank" rel="noopener">Donate</a>': '" target="_blank" rel="noopener">تبرّع</a>',
    '">Volunteer</a>': '">تطوّع</a>',
    '">Subscribe</a></span>': '">اشترك</a></span>',
    'Which one should I show your friend? Tap it and I will make the card.': 'أيّها أُري صديقك؟ انقر عليها وسأجهّز البطاقة.',
    'Now look at the back. A volunteer walked all the way round it with a phone.': 'انظر الآن إلى الخلف. دار متطوع حولها كلها بهاتف.',
    'Slow down on the details. The texture is the phone\\\'s own photos, stitched together.': 'تمهّل عند التفاصيل. الملمس هو صور الهاتف نفسها، مخيطة معًا.',
    'Every side is real. Nothing here was invented to fill a gap.': 'كل جانب حقيقي. لا شيء هنا اختُرع لسدّ فراغ.',
    'Measured from the scan itself, not guessed.': 'مقاسة من المسح نفسه، لا تخمينًا.',
    'It was modelled by hand, so it has no measured size. In the museum it stands at a comfortable height.': 'صُمّمت يدويًا، فلا مقاس حقيقي لها. في المتحف تقف على ارتفاع مريح.',
    'The exact spot is on the map chip under the label.': 'الموقع الدقيق على شريحة الخريطة تحت البطاقة.',
    'A Tanit XR volunteer.': 'متطوع من Tanit XR.',
    'The label does not give a date for this one. The archive page has the full description.': 'البطاقة لا تذكر تاريخًا لهذه. صفحة الأرشيف فيها الوصف الكامل.',
    'The label does not name the material. Turn it and look at the surface: the scan keeps every grain.': 'البطاقة لا تذكر المادة. أدِرها وانظر إلى السطح: المسح يحفظ كل حبيبة.',
    'Opening the share card for you.': 'أفتح لك بطاقة المشاركة.',
    'Kept. It is in your collection, top right.': 'حُفظت. هي في مجموعتك، أعلى اليسار.',
    'Press See it in VR at the bottom of the page.': 'اضغط شاهدها بالواقع الافتراضي أسفل الصفحة.',
    'On a headset, this page has a See it in VR button. On a phone, Share gives you a picture to keep.': 'على النظارة، في هذه الصفحة زر شاهدها بالواقع الافتراضي. على الهاتف، زر شارك يعطيك صورة تحتفظ بها.',
    'Everything here is free and made by volunteers. The Donate button under the label keeps it that way.': 'كل ما هنا مجاني ومن صنع متطوعين. زر تبرّع تحت البطاقة يبقيه كذلك.',
    'That is all the label knows. The archive page has the full description, and the volunteer who made it may know more.': 'هذا كل ما تعرفه البطاقة. صفحة الأرشيف فيها الوصف الكامل، وربما يعرف المتطوع الذي صنعها أكثر.',
},
}

# Nura's opening line per area (NURA_OPENERS in build.py) and per object (NURA_HI).
OPENERS = {
"fr": {
    "This was a portrait of someone once. We only have part of them now.":
        "C’était le portrait de quelqu’un, autrefois. Il ne nous en reste qu’une partie.",
    "This used to hold up a roof. Quite a job, for two thousand years.":
        "Ceci soutenait un toit. Un sacré travail, pendant deux mille ans.",
    "Someone placed this stone here more than two thousand years ago.":
        "Quelqu’un a posé cette pierre ici il y a plus de deux mille ans.",
    "People walked across this every day. Look at the detail under their feet.":
        "Des gens marchaient dessus chaque jour. Regardez le détail sous leurs pieds.",
    "This door is still in use. Someone probably opened it this morning.":
        "Cette porte sert encore. Quelqu’un l’a sans doute ouverte ce matin.",
    "This niche shows which way to face when you pray.":
        "Cette niche indique la direction de la prière.",
    "Someone carved these letters by hand. See if you can read any.":
        "Quelqu’un a gravé ces lettres à la main. Essayez d’en lire quelques-unes.",
    "Water ran through here on its way to a whole city.":
        "L’eau passait par ici en route vers toute une ville.",
    "This one is a whole place, not a single object. Turn it slowly.":
        "Celui-ci est un lieu entier, pas un simple objet. Tournez-le lentement.",
    "Nothing grand, just something people used. That is why we kept it.":
        "Rien de grandiose, juste un objet du quotidien. C’est pour cela que nous l’avons gardé.",
    "This one does not fit a category, which makes it my favourite kind.":
        "Celui-ci n’entre dans aucune catégorie, et c’est ce que je préfère.",
    "This one is not a scan. A volunteer built it from nothing.":
        "Celui-ci n’est pas une numérisation. Un bénévole l’a créé de zéro.",
    "A volunteer modelled this from photos of real Tunisian lamps. Look at how the light would fall.":
        "Un bénévole l’a modélisé d’après des photos de vraies lampes tunisiennes. Regardez comment la lumière tomberait.",
    "Every Tunisian courtyard has these. A volunteer grew this one from nothing.":
        "Chaque patio tunisien en a. Un bénévole a fait pousser celui-ci de zéro.",
    "Something from a Tunisian kitchen, modelled by someone who wanted it in the museum.":
        "Un objet de cuisine tunisienne, modélisé par quelqu’un qui le voulait au musée.",
    "This shell made Carthage rich. Its dye was the purple of emperors.":
        "Ce coquillage a enrichi Carthage. Sa teinture était la pourpre des empereurs.",
    "Water in the middle of the courtyard, like a real Tunisian house.":
        "De l’eau au milieu du patio, comme dans une vraie maison tunisienne.",
    "This is a whole room of the museum, built by a volunteer.":
        "C’est une salle entière du musée, construite par un bénévole.",
    "A building block. Volunteers snap these together into new galleries.":
        "Une brique de construction. Les bénévoles les assemblent en nouvelles galeries.",
    "Have a look at this one.": "Regardez celui-ci.",
    # per-object lines (NURA_HI in build.py)
    "Not a person this time. An eagle, wings folded, from a Roman villa in Carthage. Weather has softened the feathers.":
        "Pas une personne cette fois. Un aigle, ailes repliées, d’une villa romaine de Carthage. Le temps a adouci ses plumes.",
    "Laurel leaves, cut in stone. Romans gave laurel to winners and emperors. No letters here, just the pattern.":
        "Des feuilles de laurier, taillées dans la pierre. Les Romains offraient le laurier aux vainqueurs et aux empereurs. Pas de lettres ici, juste le motif.",
    "This niche held a statue of a water spirit. The spring behind it fed an aqueduct that ran over 90 km to Carthage.":
        "Cette niche abritait la statue d’un esprit des eaux. La source derrière elle alimentait un aqueduc de plus de 90 km jusqu’à Carthage.",
    "A household well in the medina. Families drew their own water here long before pipes.":
        "Un puits domestique de la médina. Les familles y tiraient leur eau bien avant les canalisations.",
    "Glazed tiles from a house in the medina. Hard to scan: the glaze reflects like a mirror.":
        "Des carreaux vernissés d’une maison de la médina. Difficile à numériser : la glaçure reflète comme un miroir.",
    "Glazed tiles inside the Zawiya of Sidi Sahib in Kairouan. Hard to scan: the glaze reflects like a mirror.":
        "Des carreaux vernissés à l’intérieur de la zaouïa de Sidi Sahib, à Kairouan. Difficile à numériser : la glaçure reflète comme un miroir.",
    "This is a piece of a drowned city. A storm pulled the sand back and volunteers scanned it before the sea covered it again.":
        "C’est un morceau de cité engloutie. Une tempête a retiré le sable et des bénévoles l’ont numérisé avant que la mer ne le recouvre.",
    "Look for the sign of Tanit: a triangle, a bar, a circle. Families carved it on stones like this two thousand years ago.":
        "Cherchez le signe de Tanit : un triangle, une barre, un cercle. Des familles le gravaient sur des pierres comme celle-ci il y a deux mille ans.",
},
"ar": {
    "This was a portrait of someone once. We only have part of them now.":
        "كان هذا صورة لشخص ما يومًا. لم يبقَ لنا منه سوى جزء.",
    "This used to hold up a roof. Quite a job, for two thousand years.":
        "كان هذا يحمل سقفًا. عمل شاق، طوال ألفي عام.",
    "Someone placed this stone here more than two thousand years ago.":
        "وضع أحدهم هذا الحجر هنا قبل أكثر من ألفي عام.",
    "People walked across this every day. Look at the detail under their feet.":
        "كان الناس يمشون عليه كل يوم. انظر إلى التفاصيل تحت أقدامهم.",
    "This door is still in use. Someone probably opened it this morning.":
        "هذا الباب ما زال يُستعمل. ربما فتحه أحدهم هذا الصباح.",
    "This niche shows which way to face when you pray.":
        "هذا المحراب يدلّ على اتجاه القبلة.",
    "Someone carved these letters by hand. See if you can read any.":
        "نقش أحدهم هذه الحروف بيده. جرّب أن تقرأ بعضها.",
    "Water ran through here on its way to a whole city.":
        "كان الماء يجري من هنا في طريقه إلى مدينة بأكملها.",
    "This one is a whole place, not a single object. Turn it slowly.":
        "هذا مكان كامل، لا قطعة واحدة. أدِره ببطء.",
    "Nothing grand, just something people used. That is why we kept it.":
        "لا شيء فخم، مجرد شيء استعمله الناس. ولهذا احتفظنا به.",
    "This one does not fit a category, which makes it my favourite kind.":
        "هذه لا تنتمي إلى أي فئة، ولهذا هي النوع المفضل عندي.",
    "This one is not a scan. A volunteer built it from nothing.":
        "هذه ليست مسحًا. صنعها متطوع من لا شيء.",
    "A volunteer modelled this from photos of real Tunisian lamps. Look at how the light would fall.":
        "صمّمها متطوع من صور مصابيح تونسية حقيقية. انظر كيف كان الضوء سيسقط.",
    "Every Tunisian courtyard has these. A volunteer grew this one from nothing.":
        "كل فناء تونسي فيه مثلها. متطوع أنبت هذه من لا شيء.",
    "Something from a Tunisian kitchen, modelled by someone who wanted it in the museum.":
        "شيء من مطبخ تونسي، صمّمه شخص أراده في المتحف.",
    "This shell made Carthage rich. Its dye was the purple of emperors.":
        "هذه الصدفة أغنت قرطاج. صبغتها كانت أرجوان الأباطرة.",
    "Water in the middle of the courtyard, like a real Tunisian house.":
        "ماء في وسط الفناء، كما في بيت تونسي حقيقي.",
    "This is a whole room of the museum, built by a volunteer.":
        "هذه قاعة كاملة من المتحف، بناها متطوع.",
    "A building block. Volunteers snap these together into new galleries.":
        "لبنة بناء. يركّبها المتطوعون معًا في معارض جديدة.",
    "Have a look at this one.": "ألقِ نظرة على هذه.",
    "Not a person this time. An eagle, wings folded, from a Roman villa in Carthage. Weather has softened the feathers.":
        "ليس شخصًا هذه المرة. نسر مطويّ الجناحين، من فيلا رومانية في قرطاج. الطقس ليّن ريشه.",
    "Laurel leaves, cut in stone. Romans gave laurel to winners and emperors. No letters here, just the pattern.":
        "أوراق غار منحوتة في الحجر. كان الرومان يمنحون الغار للمنتصرين والأباطرة. لا حروف هنا، فقط الزخرفة.",
    "This niche held a statue of a water spirit. The spring behind it fed an aqueduct that ran over 90 km to Carthage.":
        "هذه الحنية كانت تحمل تمثال روح الماء. النبع خلفها كان يغذّي قناة تمتد أكثر من 90 كم إلى قرطاج.",
    "A household well in the medina. Families drew their own water here long before pipes.":
        "بئر منزلية في المدينة العتيقة. كانت العائلات تستقي منها قبل الأنابيب بزمن طويل.",
    "Glazed tiles from a house in the medina. Hard to scan: the glaze reflects like a mirror.":
        "بلاط مزجّج من بيت في المدينة العتيقة. صعب المسح: الزجاج يعكس كالمرآة.",
    "Glazed tiles inside the Zawiya of Sidi Sahib in Kairouan. Hard to scan: the glaze reflects like a mirror.":
        "بلاط مزجّج داخل زاوية سيدي الصاحب في القيروان. صعب المسح: الزجاج يعكس كالمرآة.",
    "This is a piece of a drowned city. A storm pulled the sand back and volunteers scanned it before the sea covered it again.":
        "هذه قطعة من مدينة غارقة. أزاحت عاصفة الرمل ومسحها المتطوعون قبل أن يغطيها البحر من جديد.",
    "Look for the sign of Tanit: a triangle, a bar, a circle. Families carved it on stones like this two thousand years ago.":
        "ابحث عن رمز تانيت: مثلث وخط ودائرة. نقشته العائلات على حجارة كهذه قبل ألفي عام.",
},
}

# the pieces of walk_credit(): "Scanned by a Tanit XR volunteer · optimized by Rachel West",
# "Modelled by Patrick Molen". Applied longest first, on that one string only.
CREDIT = {
"fr": [("Scanned by a Tanit XR volunteer", "Numérisé par un bénévole de Tanit XR"),
       ("Scanned by ", "Numérisé par "), ("optimized by ", "optimisé par "),
       ("Optimized by ", "Optimisé par "), ("Modelled by ", "Modélisé par "),
       ("modelled by ", "modélisé par ")],
"ar": [("Scanned by a Tanit XR volunteer", "مسحها متطوع من Tanit XR"),
       ("Scanned by ", "مسحها "), ("optimized by ", "حسّنها "),
       ("Optimized by ", "حسّنها "), ("Modelled by ", "صمّمها "), ("modelled by ", "صمّمها ")],
}
# the volunteer cameo verb: "I optimized this one."
VERB = {"fr": {"optimized": "optimisé", "modelled": "modélisé"},
        "ar": {"optimized": "حسّنت", "modelled": "صمّمت"}}


def size(text, lang):
    """'0.98 m tall' and friends, from human_size()."""
    import re
    if not text or lang == "en":
        return text
    m = re.match(r"^(.+?) m (tall|wide|long)$", text)
    if not m:
        return text
    n, kind = m.groups()
    if lang == "fr":
        return f"{n} m de " + {"tall": "haut", "wide": "large", "long": "long"}[kind]
    return {"tall": "ارتفاعها", "wide": "عرضها", "long": "طولها"}[kind] + f" {n} م"


def credit(text, lang):
    for a, b in CREDIT.get(lang, []):
        text = text.replace(a, b)
    return text


def opener(text, lang):
    """Nura's 'hi': the opener, optionally followed by ' <size>.'"""
    import re
    if not text or lang == "en":
        return text
    table = OPENERS.get(lang, {})
    m = re.match(r"^(.*?)( (\S+ m (?:tall|wide|long))\.)?$", text)
    base, tail, sz = m.group(1), m.group(2), m.group(3)
    out = table.get(base, base)
    if sz:
        out += " " + size(sz, lang) + "."
    return out


def script(js, lang):
    """walk.js with every listed literal swapped, quotes included."""
    if lang == "en":
        return js
    for k, v in sorted(UI[lang].items(), key=lambda kv: -len(kv[0])):
        js = js.replace("'" + k + "'", "'" + v.replace("\\", "\\\\").replace("'", "\\'") + "'")
    return js
