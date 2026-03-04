'''
This file contains the dictionary of regions that can be selected in the main script.

The key of the dictionary is the name of the region, the value is a list with the following elements:
  - the coordinates of region, for the maps (latitude, longitude)
  - the default zoom level for the maps
'''

regions_dict = {
    'Babiogorski National Park': [(49.59, 19.53), 12],
    'Bialowieski National Park': [(52.76, 23.80), 11],
    'Biebrzanski National Park': [(53.49, 22.96), 10],
    'Bieszczadzki National Park': [(49.10, 22.66), 11],
    'Bory Tucholskie National Park': [(53.81, 17.56), 11],
    'Drawienski National Park': [(53.10, 15.90), 11],
    'Gorczanski National Park': [(49.55, 20.13), 12],
    'Gory Stolowe National Park': [(50.46, 16.35), 12],
    'Kampinoski National Park': [(52.32, 20.57), 11],
    'Karkonoski National Park': [(50.79, 15.62), 11],
    'Magurski National Park': [(49.52, 21.44), 11],
    'Narwianski National Park': [(53.05, 22.87), 11],
    'Ojcowski National Park': [(50.20, 19.82), 12],
    'Pieninski National Park': [(49.41, 20.37), 12],
    'Poleski National Park': [(51.42, 23.19), 11],
    'Roztoczanski National Park': [(50.59, 23.02), 11],
    'Slowinski National Park': [(54.69, 17.30), 11],
    'Swietokrzyski National Park': [(50.89, 20.94), 11],
    'Tatrzanski National Park': [(49.25, 19.93), 11],
    'Ujscie Warty National Park': [(52.60, 14.78), 11],
    'Wielkopolski National Park': [(52.27, 16.76), 11],
    'Wigierski National Park': [(54.03, 23.10), 11],
    'Wolinski National Park': [(53.91, 14.47), 11]
}

parks_info = {
'Babiogorski National Park': ["Babiogórski National Park was established on 30 October 1954 to protect the Babia Góra massif in southern Poland; in 1976 the area was also designated a UNESCO biosphere reserve. The park sits in the Lesser Poland Voivodeship on the Slovak border and centres on the Diablak peak, which rises to about 1,725 m and creates pronounced altitudinal vegetation zones."
"\n\n The park covers roughly 33.9 km² (about 3,392 ha) with an additional protective buffer (otulina). Vegetation follows clear elevation belts. Lower slopes are dominated by mixed beech–fir forests, midslopes include spruce and sycamore, upper slopes feature dwarf mountain pine and mountain meadows, and the summit supports alpinetype pastures and rare highmountain plants." 
"\n\n Babiogóra supports a rich mountain fauna including large mammals such as brown bear, wolf, lynx, and red deer, and notable bird species like the capercaillie (wood grouse). Its varied habitats also host many specialist alpine and subalpine plants, including species uncommon elsewhere in the Beskids."
"\n\n Sources: "
"\n https://bgpn.gov.pl/english-version"
"\n https://www.poland.travel/en/babiogorski-national-park/"
"\n https://nationalparksassociation.org/poland-national-parks/babia-gora-national-park/"],
'Bialowieski National Park': ["Białowieża National Park protects a core part of the ancient Białowieża Forest on the Poland–Belarus border and was established to conserve one of the last and largest remnants of Europe’s primeval lowland forest. The wider Białowieża Forest is a transboundary UNESCO World Heritage site recognised for its outstanding natural values." 
"\n\n The park covers about 105 km² and forms part of a much larger forest complex that together spans well over 100,000 hectares across both countries. The landscape includes oldgrowth mixed broadleaved and coniferous stands, river valleys, and swampy meadows."
"\n\n Białowieża is famous for its rich biodiversity, notably the European bison (the species’ largest freeliving population), and supports many large mammals (elk, wolf, lynx), otters, and a diverse bird and plant community typical of primeval temperate forest."
"\n\n Sources:" 
"\n https://whc.unesco.org/en/list/33/"],
'Biebrzanski National Park': ["Biebrzański National Park was established on 9 September 1993 to protect the extensive wetland complex along the Biebrza River in northeastern Poland. It is recognised for its large, relatively undisturbed marshes and floodplain systems."
"\n\n The park is Poland’s largest national park, covering roughly 592 km² (≈59,223 ha). Its landscape is dominated by vast peat bogs, floodplain marshes, wet meadows, river channels and patches of riverine and mixed forest. Seasonal flooding and a mosaic of open and wooded wetlands create a dynamic habitat network."
"\n\n Biebrza is especially important for wetland biodiversity and birds. It supports very high densities and diversity of waterfowl and waders and is a key refuge for species such as the Eurasian elk (moose), many waterbirds, and other wetland specialists. The park also contains diverse wetland plants, peatland communities and forested stands that together sustain its rich fauna and flora."
"\n\n Sources:"
"\n https://archiwum2.biebrza.org.pl/lang,en"
"\n https://nationalparksassociation.org/poland-national-parks/biebrza-national-park/"],
'Bieszczadzki National Park': ["Bieszczadzki National Park was established in 1973 to protect the wild, mountainous landscapes of the Polish Bieszczady in the country’s southeast. It forms part of the larger East Carpathian biosphere reserve and is recognised for its relatively intact wilderness and cultural history of pastoralism and lowintensity land use." 
"\n\n The park covers about 292 km² and is dominated by extensive forested slopes, high mountain meadows (połoniny), ridges and river valleys. Roughly 91% of the area is forest, with strictly protected zones and a mix of oldgrowth stands and secondary woodland."
"\n\n Bieszczady supports a rich mountain fauna including large mammals such as brown bear, wolf, lynx, and red deer, and a diverse bird community. Its plant life ranges from mixed montane forests on lower slopes to dwarf mountain beech and alpine meadow species on the highest ridges, making the park important for both forest and highmountain biodiversity."
"\n\n Sources: "
"\n https://nationalparksassociation.org/poland-national-parks/bieszczady-national-park/"
"\n https://www.polandtraveltours.com/en/travelguide/bieszczady-national-park/"
"\n https://archiwum.bdpn.pl/index.php?option=com_content&task=view&id=837&Itemid=190" ],
'Bory Tucholskie National Park': ["Bory Tucholskie National Park (Tuchola Forest) was created in 1996 to protect a valuable fragment of the large Tuchola Forest in northern Poland. It lies in the Pomeranian Voivodeship and preserves a mosaic of forests, lakes and wetlands shaped by glacial processes."
"\n\n The park covers about 46.1 km² and is dominated by pine forests, with substantial areas of lakes, peatlands, swamps and meadows. Roughly fourfifths of the park is forest, with water and peatland making up most of the remainder."
"\n\n Bory Tucholskie supports a typical northern lowland fauna and flora. Large mammals such as deer and wild boar, and species like otter and wolf occur in the area, while the park is also important for birds (over 100 species reported) and for wetland and forest plant communities adapted to sandy soils, peat bogs and lakeshores."
"\n\n Sources:"
"\n https://www.polskieszlaki.pl/en/bory-tucholskie-national-park/"],
'Drawienski National Park': ["Drawieński National Park (Drawa National Park) was established in 1990 to protect the river valley and forested landscapes of the Drawa River basin in northwestern Poland. The park lies within the Drawsko Plain and is named after the winding Drawa River, whose valley and associated lakes and wetlands are central to the park’s character."
"\n\n The park covers roughly 113–115 km² (about 11,300–11,500 ha), most of which is forested. Its terrain is a postglacial mosaic of mixed and coniferous forests, ribbon lakes, peat bogs, sandy glacial landforms and river channels. It also includes lobelia (clearwater) lakes and numerous smaller water bodies."
"\n\n Drawieński National Park supports a diverse freshwater and forest biota. The river and lakes host valuable fish and aquatic invertebrates, while forests and wetlands shelter mammals such as beaver and otter (the otter is a park symbol), deer and other typical northern lowland species. The park is also important for birds (over 150 species reported) and for rich plant communities, with around 700 vascular plant species recorded."
"\n\n Sources:"
"\n https://www.poland.travel/en/drawa-national-park/"],
'Gorczanski National Park': ["Gorczański National Park was created in 1981 to protect the wooded ridges and valleys of the Gorce Mountains in southern Poland, centred on peaks such as Turbacz and Gorc and forming part of the Western Beskids."
"\n\n The park covers about 70.3 km² (with a larger protective buffer zone) and is dominated by montane forests such as beech, fir and spruce, and is interspersed with mountain meadows (glades) and deep valleys. The landscape shows clear altitudinal vegetation belts typical of the Carpathians."
"\n\n Gorce supports typical Carpathian wildlife, including large mammals such as red deer, roe deer, wild boar, wolf and lynx, and notable species like the capercaillie and the park’s emblematic fire salamander. Plant life ranges from mixed montane forests on lower slopes to alpine and endemic meadow species on higher glades."
"\n\n Sources:"
"\n https://www.poland.travel/en/gorczanski-national-park/"
"\n https://visitmalopolska.pl/en_GB/obiekt/-/poi/gorczanski-park-narodowy?inheritRedirect=true"
"\n https://gpn.gov.pl/english-version"],
'Gory Stolowe National Park': ["Góry Stołowe National Park (Stołowe Mountains National Park) was established in 1993 to protect the distinctive Table Mountains on the Polish–Czech border, a landscape of flattopped sandstone plateaus and dramatic rock formations that attract both scientific interest and tourism. The park lies in the Lower Silesian Voivodeship and centres on wellknown features such as Szczeliniec Wielki and the Błędne Skały rock labyrinth."
"\n\n The park covers about 63 km² (≈6,340 ha), of which the majority is forested (roughly 57.8 km²), with the remainder made up of rocky plateaus, gorges, lakes and small patches of meadow and heath. Its geology, such as horizontally layered sandstones shaped by erosion, creates extensive cliffs, crevices and rock mazes that strongly influence local vegetation patterns and microhabitats."
"\n\n The park’s habitats support a mix of forest and rockspecialist species. Forests shelter typical Central European woodland fauna and many bird species, while rock crevices provide roosting sites for several bat species and nesting niches for large owls. Plant communities range from mixed forest stands to specialised cliff and plateau flora adapted to thin, sandy soils."
"\n\n Sources:"
"\n https://www.poland.travel/en/gory-stolowe-national-park/"
"\n https://pngs.gov.pl/english-version"],
'Kampinoski National Park': ["Kampinoski National Park was established in 1959 in the Masovian Voivodeship, on the north‑western outskirts of Warsaw. The idea of protecting the Kampinos Forest dates back to the 1920s, when concerns arose that the expanding capital might engulf this remnant of a once vast lowland wilderness. Today it is recognised as a UNESCO Biosphere Reserve, reflecting its ecological value and long conservation history."
"\n\n The park covers 385.44 km², making it one of Poland’s largest national parks. Its landscape is a distinctive mosaic of inland dunes, swamps, wet meadows, forests, and rushes, shaped by post‑glacial processes and the parallel course of the Vistula River. Forests include bog‑alder, ash‑alder floodplain, pine–oak mixed, and oak–lime–hornbeam types, interspersed with extensive wetland systems."
"\n\n The park supports around 50 mammal species, including elk (reintroduced in 1951), red deer, wild boar, beaver, and the recently recolonising wolf. It is also an important bird sanctuary, with roughly 200 bird species, among them black stork, lesser spotted eagle, and crane. The diversity of habitats also sustains numerous amphibians, reptiles, butterflies, and other insects, making the area a significant site for entomological research."
"\n\n Sources:"
"\n https://kampn.gov.pl/english-version"],
'Karkonoski National Park': ["Karkonoski National Park was established in 1959 to protect the highest part of the Sudetes along the Polish–Czech border, centred on the Karkonosze Mountains and iconic peaks such as Śnieżka. The park preserves dramatic glacial landforms, cirques and peatbogs that have long attracted scientific interest and tourism."
"\n\n The park covers roughly 55–60 km² and includes a steep altitudinal sequence of habitats. Montane and subalpine forests (spruce, beech mixes), dwarf mountain pine near the treeline, alpinetype meadows and highmountain peatbogs. Lakes, rocky outcrops and eroded sandstone also shape a highly varied mosaic."
"\n\n Karkonosze supports rich biodiversity driven by its vertical vegetation zones. Thousands of invertebrate species and several hundred vertebrate species have been recorded, including specialist alpine plants, montane birds and mammals adapted to mountain forests and peatbogs. The park also contains internationally important peatbog habitats."
"\n\n Sources: "
"\n https://kpnmab.pl/en/lang"
"\n https://www.poland.travel/en/karkonosze-national-park/"
"\n https://eunis.eea.europa.eu/sites/852"],
'Magurski National Park': ["Magurski National Park (Magura National Park) was established in 1995 to protect the forested Magura Wątkowska massif in the Low Beskids on Poland’s southeastern border region. The park conserves a largely forested mountain landscape and the upper basin of the Wisłoka River."
"\n\n The park covers roughly 194 km² (about 19,439 ha), of which the vast majority is forest (around 185 km²). The terrain is a mosaic of gentle, forested hills, river valleys, meadows and small wetlands typical of the Lower Beskids, with beech–fir–spruce stands dominating the vegetation."
"\n\n Magurski supports a rich mountain fauna and birdlife, including large carnivores such as wolf, lynx and brown bear, and raptors like the lesser spotted eagle. Its flora includes diverse mountain and forest species, with many protected and regionally rare plants found in the park’s varied forest and meadow habitats."
"\n\n Sources:"
"\n https://mpn.gov.pl/english-version"
"\n https://nationalparksassociation.org/poland-national-parks/magura-national-park/"],
'Narwianski National Park': ["Narwiański National Park protects a unique, braided section of the Narew River in northeastern Poland and was established in 1996 to conserve the swampy, multichannel river valley often called the “Polish Amazon.”"
"\n\n The park covers about 73–154 km² depending on whether you count core and buffer areas (official park area commonly reported as ~73.5 km² / 7,350 ha) and is dominated by a maze of channels, oxbow lakes, reedbeds, floodplain meadows, peatlands and riparian forests that remain wet yearround."
"\n\n Narwiański is an important refuge for wetland biodiversity and birds. Nearly 200 bird species have been recorded, with over 150 breeding species including several endangered wetland specialists (for example aquatic warbler and corncrake). The park also supports rich waterplant communities and typical floodplain fauna."
"\n\n Sources:"
"\n https://www.poland.travel/en/narwianski-national-park/"
"\n https://npn.gov.pl/narew-national-park"],
'Ojcowski National Park': ["Ojcowski National Park was established in 1956 and is located in the Lesser Poland Voivodeship, north of Kraków. It takes its name from the village of Ojców, where the park’s headquarters are situated. The area forms part of the Kraków–Częstochowa Upland, a region known for dramatic limestone formations, deep ravines and a long history of human presence."
"\n\n It is Poland’s smallest national park, covering 21.46 km². The landscape is dominated by karst terrain, including limestone cliffs, gorges, caves and rock formations such as Hercules’ Club and the White Hand. The Prądnik River valley shapes much of the park’s scenery, creating a varied mosaic of forested slopes, rocky outcrops and sheltered valley floors."
"\n\n The park’s vegetation includes deciduous forests and xerothermic plant communities, with many species adapted to the sunny limestone slopes. Its fauna is notably rich, including bats, ungulates, predatory mammals, birds of prey, amphibians, reptiles and a wide range of invertebrates all thrive in the caves, forests and riverine habitats."
"\n\n Sources:"
"\n https://nationalparksassociation.org/poland-national-parks/ojcow-national-park/"
"\n https://www.globalnationalparks.com/poland/ojcow/wildlife-and-flora/"],
'Pieninski National Park': ["Pieniński National Park was established in 1932, making it the oldest national park in Poland. It protects the central section of the Pieniny Mountains along the Poland–Slovakia border, with its headquarters in Krościenko nad Dunajcem. The park is famous for its dramatic limestone peaks, especially Trzy Korony and Sokolica, and the spectacular Dunajec River Gorge, one of Poland’s most iconic natural landscapes."
"\n\n The park covers 23.46 km², of which 13.11 km² is forested and 7.5 km² is strictly protected. Its terrain includes steep limestone cliffs, deep gorges, rocky outcrops, mixed beech–fir forests, and small pine stands on barren slopes. The Dunajec River carves through the mountains, creating a mosaic of microhabitats across three main ranges: Pieniny Spiskie, Małe Pieniny, and Pieniny Właściwe (where the park is located)."
"\n\n Pieniński National Park is one of the beststudied biodiversity hotspots in Poland, with an estimated 13,000–15,000 species occurring within its boundaries. Around 7,100 species have been formally recorded, including 6,800 invertebrates. The park is known for its butterflies, most famously the Apollo butterfly, which survives in Poland mainly due to conservation efforts here. Vegetation includes mixed beech–fir forests, endemic plants such as the Pieniny dandelion and Pieniny wallflower, and specialised grassland and cliff communities."
"\n\n Sources:"
"\n https://piepn.gov.pl/english-version"
"\n https://www.poland.travel/en/pieninski-national-park/"
"\n https://life.pieninypn.pl/en/1153/0/fauna.html"],
'Poleski National Park': ["Poleski National Park, located in the Lublin Voivodeship of eastern Poland, was officially established on 1 May 1990 to protect the unique wetland landscapes of the Polish part of Polesia. The idea of creating a national park in this region dates back to the interwar period, with early proposals made in 1933 by botanist Władysław Szafer, and later refined in the 1950s and 1960s. The present park represents the first Polish conservation project focused on water and peatbog ecosystems."
"\n\n The park covers approximately 97.6 km², with an additional buffer zone of 137 km². Its landscape is predominantly flat and boggy, characterised by peat bogs, marshes, swamps, karst lakes, and patches of pine and birch forest. Notable lakes include Moszne and Długie, and the area forms part of the Łęczna–Włodawa Plain, a region shaped by postglacial processes."
"\n\n Poleski National Park is one of Poland’s richest wetland habitats, supporting around 1,000 species of vascular plants, including many marshland specialists. The fauna includes 290 rare species, with 200 bird species, 48 mammals, 21 fish species, and 13 amphibians recorded."
"\n\n Sources:"
"\n https://its-poland.com/attraction/polesie-national-park"
"\n https://nationalparksassociation.org/poland-national-parks/polesie-national-park/"
"\n https://polpn.gov.pl/historia-poleskiego-parku-narodowego"
"\n https://www2.poleskipn.pl/index.php/historia"],
'Roztoczanski National Park': ["Roztoczański National Park was established in 1974 to protect the most valuable natural areas of the central Roztocze range in southeastern Poland. Its history is closely tied to the Zamoyski family estate, founded in 1589, whose former lands form much of today’s protected area. The park’s headquarters are located in Zwierzyniec."
"\n\n The park covers 84.83 km², of which 81.02 km² is forest and 8.06 km² is strictly protected. It is one of Poland’s most heavily forested national parks, dominated by beech and fir stands. The varied geology, soils and microclimates create a mosaic of habitats, including fertile mountain beech forests, mixed fir forests, wetground forests and coniferous swamps, several of which are priority habitats under the Natura 2000 network."
"\n\n The park hosts a rich mixture of lowland and upland plant species, including stenothermal species from southeastern Europe. Around 190 bird species have been recorded, and the park is also known for its population of Polish konik horses, bred as a modern analogue of the extinct tarpan."
"\n\n Sources:"
"\n https://rpn.gov.pl/english-version"
"\n https://www.poland.travel/en/roztoczanski-national-park/"],
'Slowinski National Park': ["Słowiński National Park was established in 1967 to protect one of Europe’s most distinctive coastal landscapes on the Baltic Sea, between the towns of Łeba and Rowy. Its creation followed a 1966 government decree that recognised the exceptional natural value of the region’s lakes, peatbogs and dune systems. The park later gained international recognition as a UNESCO Biosphere Reserve (1976) and a Ramsar wetland site (1995)."
"\n\n The park covers 186.18 km², including 32.5 km of Baltic coastline. Its landscape is dominated by moving sand dunes, some shifting up to 10 metres per year, along with coastal lakes, bogs, peatlands, meadows and maritime forests. These habitats form a dynamic system of sandspits, lagoons and wetlands that is unique in Europe."
"\n\n Słowiński National Park supports around 920 vascular plant species, alongside rich communities of mosses, algae and fungi. Vegetation ranges from pioneer dune plants such as sand couch grass and sea rocket to maritime pine forests and peatbog specialists like sundews and royal fern. The wetlands and lakes provide important habitat for migratory and breeding waterbirds, contributing to the park’s international conservation status."
"\n\n Sources:"
"\n https://spn.gov.pl/slowinski-park-narodowy"
"\n https://grokipedia.com/page/Slovincian_National_Park"
"\n https://www.parks.it/world/PL/parco.nazionale.slowinski/Eindex.php"
"\n https://slowinskipark.keep.pl/historia/"],
'Swietokrzyski National Park': ["Swietokrzyski National Park is a National Park in Swietokrzyskie Voivodeship in central Poland. The Swietokrzyskie Mountains are the oldest in Poland. Elevated in three different tectonic periods, they spread out in the Malopolska Upland, between Pilica and the Vistula river. Their outlines are gentle and their heights are small, the highest peak is Lysica at 612 meters."
"\n\n The history of efforts to protect this part of Poland dates back to the times before World War I. The first forest reserve was established in 1921, and expanded in subsequent years to eventually form the National Park in 1950. The area of today's Park is approximately 76 square kilometres, of which 72 km2 are forested. There are five strictly protected zones with a total area of over 17 km2."
"\n\n The park is famous for its trees, of which 674 are regarded as monuments of nature and as such are under protection. Among them is a 270-year-old European silver fir measuring 51 meters, considered the tallest conifer in Poland. The park's fauna is represented by more than 4000 species of invertebrates and 210 species of vertebrae (including 187 protected). Some of the large mammals found in the park include the deer (whose silhouette appears in Park's logo), wild boar, beaver and fox."
"Much less common, making occasional appearances are Moose and Nyctereutes. Among many birds of prey nesting in the park are 4 species of owls: the Eurasian pygmy owl, Boreal owl, Long-eared owl and the rare and majestic Ural Owl."
"\n\n Sources:"
"\n https://swpn.gov.pl/swietokrzyski-national-park"],
'Tatrzanski National Park': ["Tatrzański National Park was established in 1954 to protect the Polish section of the Tatra Mountains, the country’s only area of true Alpine character. It lies in the Lesser Poland Voivodeship, with Zakopane as the nearest town, and forms a continuous protected area with Slovakia’s TANAP. The idea of safeguarding the Tatras dates back to the midnineteenth century, when Krakówbased scientists first advocated formal conservation."
"\n\n The park covers 211.64 km², encompassing jagged granite ridges, forested slopes, postglacial valleys, numerous caves, and iconic mountain lakes such as Morskie Oko and Czarny Staw pod Rysami. Vegetation follows clear altitudinal belts where spruce, fir, larch, beech and sycamore dominate the foothills. Higher zones feature spruce and stone pine, giving way to Alpine meadows and rocky summits."
"\n\n The park is renowned for its Tatra chamois, which serves as its emblem, and also supports brown bear, lynx, wolf, marmot and a rich assemblage of mountain birds and invertebrates. Its flora includes both Alpine and Carpathian species, with many plants adapted to highmountain conditions and postglacial habitats."
"\n\n Sources:"
"\n https://www.poland.travel/en/tatrzanski-national-park/"
"\n https://www.jstor.org/stable/3673791"],
'Ujscie Warty National Park': ["Ujście Warty National Park is Poland’s youngest national park, created in 2001 to protect the lowest stretch of the Warta River up to its confluence with the Oder, which forms part of the Polish–German border. It lies in the Lubusz Voivodeship, with its headquarters in Chyrzyno, near Kostrzyn nad Odrą. The area was historically covered by wet riparian forests, later transformed through river regulation, drainage and grazing into open wet meadows and floodplain landscapes."
"\n\n The park covers roughly 80–81 km², with a buffer zone of over 100 km². It is characterised by extensive floodplains, marshes, wet meadows, oxbow lakes, river channels and seasonally inundated basins. Water levels can fluctuate by up to 3.5 metres, creating a dynamic wetland mosaic shaped by regular flooding."
"\n\n Ujście Warty is one of Europe’s most important refuges for waterbirds and marshland species. Large areas remain underwater for weeks each year, attracting exceptional numbers and diversity of birds, including breeding, migratory and wintering populations. The park is widely recognised as a “bird kingdom”, supporting species that depend on open, wet grasslands and floodplain habitats."
"\n\n Sources:"
"\n https://www.wikiwand.com/en/articles/Ujscie_Warty_National_Park"
"\n https://www.poland.travel/en/ujscie-warty-national-park/"
"\n https://pnuw.gov.pl/ujscie-warty-national-park"],
'Wielkopolski National Park': ["Wielkopolski National Park was established in 1957 in the Greater Poland Voivodeship, around 15 km south of Poznań. It was created to protect the region’s distinctive postglacial landscape, shaped by the last Scandinavian ice sheet, and is one of Poland’s older national parks."
"\n\n The park covers 75.84 km², featuring a varied terrain of moraine hills, kettle lakes, ancient sand dunes, and extensive forests. Notable lakes include Góreckie and Kociołek, which reflect the surrounding woodland. The landscape is a classic example of postglacial geomorphology, with numerous erratic boulders and wellpreserved forest–lake ecosystems."
"\n\n Vegetation is dominated by beech and oak forests, with areas of pine and hornbeam, creating a rich mosaic of habitats. These woodlands, together with the lakes and wetlands, support a wide range of wildlife typical of central European lowland forests. The park also maintains several strictly protected zones to safeguard its most natural plant communities and associated fauna."
"\n\n Sources:"
"\n http://nationalparksassociation.org/poland-national-parks/wielkopolska-national-park/"
"\n https://ppn.gov.pl/wielkopolski"],
'Wigierski National Park': ["Wigierski National Park was established in 1989 in the Podlaskie Voivodeship of northeastern Poland. It protects a landscape shaped by the Baltic glaciation, encompassing parts of the Masurian Lake District and the Augustów Primeval Forest. The park takes its name from Lake Wigry, the largest of its many lakes, and is recognised internationally as a Ramsar wetland site."
"\n\n The park covers roughly 150–151 km², including 9,464 ha of forest, 2,908 ha of water, and 2,714 ha of other land, much of it traditionally farmed. Its terrain features postglacial lakes, peat bogs, marshes, and mixed coniferous forests, with the River Czarna Hańcza flowing through the area."
"\n\n Wigierski National Park supports a rich wetland and forest fauna. Notable mammals include elk, red deer, roe deer, wolf and beaver, the latter serving as the park’s emblem. The lakes and waterways host rare fish such as powan, European whitefish, and bulltrout, while the wetlands attract a wide variety of aquatic birds. Vegetation ranges from pine and spruce forests to moor, aquatic and meadow plant communities."
"\n\n Sources:"
"\n https://www.poland.travel/en/wigierski-national-park/"
"\n https://wigry.org.pl/index_en.html"],
'Wolinski National Park': ["Woliński National Park was established in 1960 and is located on Wolin Island in the far northwest of Poland, within the West Pomeranian Voivodeship. Its headquarters are in Międzyzdroje. The park protects a striking coastal landscape, including the Polish cliff coast and the islandlike delta of the Świna River, making it one of the country’s most distinctive national parks."
"\n\n The park covers 109.37 km², including forests, coastal cliffs, marine waters and the extensive wetlands of the Świna backdelta. Forests, mainly mixed stands of beech, oak and pine, cover most of the land area, while the park also includes a 17km stretch of Baltic coastline and over 4,700 ha of aquatic ecosystems. The landscape naturally divides into two contrasting zones: the deltaic wetlands and the moraine uplands."
"\n\n Woliński National Park also supports a rich biodiversity. Around 200 bird species have been recorded, including waterfowl, wetland birds and cliffnesting species. The whitetailed eagle is the park’s emblem and can be observed near the nature museum. The park also maintains a display reserve for European bison. Its flora includes an estimated 1,300 vascular plant species."
"\n\n Sources:"
"\n https://wopn.gov.pl/informacje-ogolne"
"\n https://www.poland.travel/en/wolinski-national-park/"]
}