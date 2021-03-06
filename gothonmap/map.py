#!/bin/python2
# -*- coding: UTF-8 -*-

language_ = u"\nIn english / en français"

hero_ = [u"What is your hero's name?", u"Quel est le nom de ton héro?"]

chapter_ = [u"CHAPTER", u"CHAPITRE"]

epilogue_ = [u"EPILOGUE", u"ÉPILOGUE"]

###############################################

quips_ = [
["%s, you die. Miserably. As always, you kinda \nsuck. Only this time, it's fatal.\n\nTHE END \n", "%s, you die. You are such a looser. Not only are \nyou an underachiever, you unachieved an \nunderachievement. \n\nTHE END \n", "%s, you die. I just want to let you know that I \nhave a small puppy that is better than you at this. \n\nTHE END"], ["%s, tu meurs. Misérablement. Comme toujours, \ntu rates ton coup. Seulement cette fois, \nc'est fatal.\n\nFIN \n", "%s, tu meurs. Quel perdant. Même à niveler \npar le bas tu n'arrives pas à t'abaisser assez \npour faire le minimum. \n\nFIN \n", "%s, tu meurs. Sache en passant que je possède un \nchiot qui sait faire des tours que tu \nne saurait même pas imiter. \n\nFIN"]]

continue_ = ["Press 'Enter' to continue.",
"Appuie sur 'Enter' pour continuer."
]

###############################################

lower_deck_cursive_ = [
"Lower Deck Cursive \n\n%s! The Gothon pirates have boarded your ship. You \nare the last standing crew member. No surprise! \nWhile your comrades were fighting, you were... \nsleeping! Anyhow, this vessel must not fall into \nenemy's hands. You are now running down the lower \ndeck cursive. A safe choice to avoid enemies. \nAhead: the armory. As you emerge from the last \nhatch, one insectoid pirate jumps out, guarding \nthe way to the armory. He's about to pull a \nweapon to blast you. What do you do? \n\n[a] shoot! [b] dodge! [c] tell a joke",
"Coursive du pont inférieur \n\n%s! Les pirates gothons ont abordé ton vaisseau. \nTu es le seul survivant de l'équipage. \nÉvidemment, alors que tes camarades \ncombattaient, tu... dormais! Peu importe, ce \nvaisseau ne doit pas tomber aux mains de \nl'ennemi. Te voilà donc à la course dans la \ncoursive du pont inférieur. Judicieux pour \néviter les ennuis. Droit devant: l'arsenal. \nAlors que tu t'extrais de la dernière \nécoutille, un pirate insectoïde fait irruption. \nIl bloque l'entrée de l'arsenal. Il \ns'apprête à dégainer pour te griller. Que \nfais-tu? \n\n[a] tire! [b] esquive! [c] raconte une blague"
]

lower_deck_cursive_a_ = [
"Lower Deck Cursive \n\nQuick on the draw, you yank out your blaster and \nfire it at the Gothon pirate. He leaps high in \nthe air. Your laser misses him entirely. The \npirate flies into an insane rage and blast you \nrepeatedly in the face until you are dead. Then, \nthe insectoid dissolves you with his saliva, and \nsuck you up.\n",
"Coursive du pont inférieur \n\nRapide sur la gâchette, tu fais cracher ton \nlaser en direction du pirate gothon. Ce dernier \nbondit dans les airs. Tu le rates. Fou de rage, \nle pirate bondit vers toi et te balance quelques \ndécharges à la tête. Tu t'effondres. Puis, \nl'insectoïde te liquéfie avec sa salive, \navant de t'aspirer.\n"
]

lower_deck_cursive_b_ = [
"Lower Deck Cursive \n\nYou dodge, weave, and slide as the pirate's \nblaster cranks a laser past your head. In the \nmiddle of your artful dodge, your foot slips. You \nbang your head on the wall, and pass out. You \nwake up shortly after, only to die as the \ninsectoid dissolves you with his saliva, and suck \nyou up.\n",
"Coursive du pont inférieur \n\nLe pirate te balance des jets de laser; tu les \nesquives. Dans ce ballet improvisé, tu finis \npar glisser. Ta tête donne contre le mur. Tu \nt'assommes et t'écroules. Tu ne reprends \nconnaissance que pour te rendre compte que \nl'insectoïde te liquéfie avec sa salive, \navant de t'aspirer.\n"
]

lower_deck_cursive_c_ = [
"Lower Deck Cursive \n\nLucky for you they made you learn Gothon insults \nin the academy.  You tell the one Gothon joke you \nknow. The Gothon stops, waits, then busts out \nlaughing. While he's laughing, you shoot him \nsquare in the head, putting him down. You then \njump through the armory door. It's dead quiet...\n",
"Coursive du pont inférieur \n\nTu trouves bien utile d'avoir mémorisé un peu \nde gothon à l'académie.  Tu racontes donc la \nseule blague dont tu te souviens. Le Gothon fige, \nréfléchit, puis éclate de rire. Alors qu'il \ns'esclaffe, tu lui balances un jet laser à la \ntête. Il s'écroule. Tu enjambes le corps et \npénètres dans l'arsenal. Il règne un silence \nmortuaire...\n"
]

lower_deck_cursive_else_ = [ 
"Lower Deck Cursive \n\nPlease, select either [a], [b] or [c]",
"Coursive du pont inférieur \n\nTu dois choisir entre [a], [b] ou [c]"
]

###############################################

armory_ = [
"The Armory \n\nYou lock the door and run to the far side of the \nroom. All the laser weapons are gone. You find \nthe explosive container. There is a keypad lock \non the box. You need a 3-digit code to get the \nbomb out. You can guess. However, after five \nattempts, you know the lock will fuse forever. \n\nPlease, enter three digits.",
"L'Arsenal \n\nTu verrouilles la porte et t'élances vers le \nfond de la pièce. Les armes laser ont été \nemportées. Tu retrouves le conteneur à \nexplosifs. Pour l'ouvrir, tu dois entrer un \ncode à trois chiffres sur le clavier. Tente de \ndeviner. Par contre, après cinq tentatives, le \nverrou se soude à jamais. \n\nEntre trois chiffres."
]

armory_hunch_ = [
"The Armory \n\nNot working. Hurry up! You remember that all the \ndigit combinations aboard begin with ",
"L'Arsenal \n\nRaté. Dépêche-toi! Tu te rappelles que les \ncombinaisons à bord débutent par "
]

armory_tip_ = [
"The Armory \n\nNot working. Mmmmh... OK! OK! OK! You remember. \nThese combinations are always ",
"L'Arsenal \n\nRaté. Mmmmh... OK! OK! OK! Ça revient. Les \ncombinaisons sont toujours "
]

armory_code_ = [
"The Armory \n\nThe container clicks open, the seal breaks, \nletting gas out. You find a dozen of time-bombs. \nYou grab one. You run as quickly as you can to \nthe starboard engine. Over there, you know the \nblast will trigger a chain reaction and destroy \nthe ship. \n",
"L'Arsenal \n\nLe verrou se déclenche, le scellant se fend, le \ncontenant se dépressurise. Tu prends une des \ndouzaines de bombes à retardement. Tu te diriges \nà la hâte vers le réacteur du tribord. Une \nexplosion y déclenchera une réaction en chaine \net détruira le vaisseau. \n"
]

armory_else_ = [
"The Armory \n\nThe lock buzzes once more. Only this time, you \nhear a sickening melting sound. The mechanism is \nfused together. Without weapon: no hope. You \ndecide to sit there. Time passes... and passes... \nSuddenly, you hear a muffled thud. Something hit \nthe ship? Then, another thud? And, more thuds. \nThis time, heavier and louder. The hull begins \nshaking and roaring. Soon, the temperature falls, \nair pressure drops, oxygen becomes scarcer... \nThey let the ship strand on the asteroid belt!! \nYou fall into a faint... to never wake up again. \n",
"L'Arsenal \n\nLe verrou bourdonne une dernière fois et tu \nl'entends se souder. Le mécanisme a sauté. \nSans arme, c'est l'impasse. Tu décides de \nt'assoir. Le temps passe... et passe... Soudain, \ntu entends un bruit sourd. Quelque chose \na percuté le vaisseau? Puis, un autre bruit? \nEt encore. De plus en plus lourd et fréquent. La \ncoque vrombit et grince. L'air se refroidit, \nla pression chute, l'oxygène se raréfie... Ils \nont laissé le vaisseau s'échouer dans la \nceinture d'astéroïdes!! Tu t'évanouis... \npour ne jamais te réveiller. \n"
]

###############################################

the_bridge_ = [
"The Bridge \n\nYou burst onto the bridge with your \nbomb under your arm. You surprise three Gothon \npirates. The three lezardoids haven't pulled \ntheir weapons out yet, as they see the active \nbomb under your arm. What do you do? \n\n[a] throw the bomb [b] slowly place the bomb",
"Le pont \n\nTu émerges sur le pont du réacteur et tu \nsurprends trois pirates gothons. Les trois \nlézaroïdes n'ont pas encore dégainé, mais \nils fixent la bombe que tu portes. Que fais-tu? \n\n[a] lance la bombe [b] dépose la bombe"
]

the_bridge_throw_ = [
"The Bridge \n\nIn a panic, you trigger off the timer, throw the \nbomb and make a leap for the door. Right as you \ndrop it, a pirate shoots you in the back, killing \nyou. As you die you see another pirate \nfrantically trying to disarm the bomb. They got \nyou, but they won't make it alive either. \n",
"Le pont \n\nEn panique, tu déclenches la minuterie et tu \nbalances la bombe. Alors que tu t'élances vers \nla porte, un pirate te tire mortellement dans le \ndos. Tu perds connaissance en voyant les pirates \ndésespérément essayer de désarmer l'engin \nexplosif. Ils t'ont eu, mais ils y passeront \neux aussi. \n"
]

the_bridge_slowly_ = [
"The Bridge \n\nYou point your blaster at the bomb under your \narm. The pirates put their hands up. You inch \nbackward to the door and then carefully place the \nbomb on the floor, pointing your blaster at it. \nThen you set off the timer, jump back through the \ndoor, punch the close button and blast the lock. \nNow, you must reach the escape pods to get off \nthis tin can. \n",
"Le pont \n\nTu pointes ton laser vers la bombe que tu tiens. \nLes pirates lèvent les bras. Tu recules vers la \nporte et tu poses délicatement la bombe au sol \ntout en la maintenant en joue. Puis, tu \ndéclenches la minuterie, passes la porte, \nfrappes le bouton de fermeture et fais sauter la \nconsole. Maintenant, tu dois gagner les navettes \nde secours pour t'éjecter du vaisseau. \n"
]

the_bridge_else_ = [
"The Bridge \n\nPlease, select between [a] and [b] \n",
"Le pont \n\nTu dois choisir entre [a] et [b] \n"
]

###############################################

escape_pod_ = [
"Escape Pod \n\nYou get to the boarding bay. \nSuddenly, the ship rattles! The bomb just \nexploded. The reactor will melt down and the ship \nwill soon be disintegrated! There are five pods, \nwhich one do you take? \n\nEnter a digit, from 1 to 5.",
"Navette de secours \n\nTu atteins la zone d'embarquement. Soudain, le \nvaisseau tremble! La bombe vient d'exploser. Le \nréacteur va se fissurer et le vaisseau va \nbientôt se disloquer! Il y a cinq navettes, \nlaquelle choisis-tu? \n\nEntre un chiffre, de 1 à 5."
]

escape_pod_not_ = [
"Escape Pod \n\nYou punch the keypad, the \nairlock opens, you jump into pod %s, and trigger \nthe evasion procedure. The pod easily slides out \ninto space, then... explodes as the hull ruptures, \ncrushing your body into jam jelly. \n",
"Navette de secours \n\nTu frappes le bouton d'ouverture, le sas \ns'ouvre, tu bondis à l'intérieur de la \nnavette %s et tu lances la procédure \nd'évasion. La navette s'éjecte dans l'espace, \npuis... explose alors que la coque se rupture, \nbroyant ton corps comme de la confiture. \n"
]

escape_pod_else_ = [
"Escape Pod \n\nYou punch the keypad, the airlock opens, you jump \ninto pod %s, and trigger the evasion procedure. \nThe pod easily slides out into space, heading to \nthe planet below. VICTORY! You look in the \nporthole and see your ship explode like a bright \nstar, taking out the Gothon ship at the same \ntime... \n",
"Navette de secours \n\nTu frappes le bouton d'ouverture, le sas \ns'ouvre, tu bondis à l'intérieur de la \nnavette %s, puis tu enclenches la procédure \nd'évacuation. La navette s'éjecte dans \nl'espace, puis ajuste sa trajectoire sur la \nplanète. VICTOIRE! Tu regardes dans le hublot \net tu assistes à l'explosion de ton \nvaisseau. L'onde de choc emporte le vaisseau \ngothon... \n"
]

###############################################

win_ = [
"%s, you win! Not only did you defeat the \nboss, you eradicated the Gothon pirates! \nYou a true hero! \n\nNonetheless, keep in mind that it's only a \nPython script. \n\nTHE END \n",
"%s, tu gagnes! Tu as non seulement défait le \nchef, mais tu as éradiqué les pirates gothons. \nTu es un héros! Néanmoins, garde en tête qu'il \nne s'agit que d'un script Python. \n\nFIN \n"
]

###############################################

final_fight_ = [
"Final Fight \n\nBut wait... Just like in any good movie, we are \nnot over. A Gothon was hidden in the pod! %s, \nyou are now facing... %s, the Gothon boss! You \nwill have to fight him, bare hands!! Isn't it \nepic? Ah, remember that you wear a smart suit. \nDon't worry against concussions or minor \ninjuries. Your integrated health pack will \ninject you a healing serum. Your enemy is \nnaturally endowed with this ability. Only your \nsuit is way more effective! \n",
"Combat Final \n\nMais encore... Comme dans un classique du \ncinéma, il y a une chute. Un Gothon était \ncaché dans la navette! %s, tu fais face à... \n%s, le chef des Gothons! Tu dois l'affronter, \nà mains nues!! N'est-ce par épique? Rappelle-toi \nque ta combinaison est intelligente. Ne crains \npas les coupures ou les contusions. Ton pack \nmédical va t'injecter un sérum de guérison. \nTon ennemi est naturellement doté de cette \naptitude. Or ton pack est beaucoup plus efficace! \n"
]

###############################################

stats_ = [ 
"Final fight \n\nYour adversary is stronger (Power: %s) \nthan you %s (Power: %s). \n\nHowever, with your special suit, you \nrecover faster (Rate: %s) \nthan this vilain (Rate: %s). \n",
"Combat Final \n\nTon adversaire est plus puissant (Force: %s) \nque toi %s (Force: %s). \n\nCependant, avec ta combinaison, tu \nrécupères plus rapidement (Taux: %s) \nque le vilain (Taux: %s). \n"
]

hp_hero_ = [
"\n%s, your HP are: %d",
"\n%s, tes PdeV sont: %d"
]

hp_monster_ = [
"%s's HP are: %d\n",
"Les PdeV de %s sont: %d\n"
]

what_ = [
"%s, what do you do?",
"%s, que fais-tu?"
]

what_attack_ = [
"[1] Attack",
"[1] Attaquer"
]

what_defend_ = [
"[2] Remain defensive, and recover\n",
"[2] Rester défensif pour récupérer"
]

what_except_ = [
"Please, %s, select [1] or [2]\n",
"%s, tu dois choisir [1] ou [2]\n"
]

what_no_ = [
"What? There is no such action! \nPlease, focus!\n",
"Quoi? Ce n'est pas un choix! \nOn se concentre!\n"
]

hero_hp_ = [
"Unfortunately, this blow is fatal to you.\n",
"Malheureusement, ce coup t'est fatal.\n"
]

monster_hp_ = [
"I think you fatally hit the weak point... \nThe Gothon collapses.\n",
"Je crois que tu as touché le point faible... \nLe Gothon s'écroule.\n"
]

attack_ = [
"%s attacks %s. %s loses %d HP.\n",
"%s attaque %s. %s perd %d PdeV.\n"
]

special_attack_ = [
"%s, you throw a powerful blow to %s. \n%s loses %d HP.\n",
"%s, tu balances un solide coup à %s. \n%s perd %d PdeV.\n"
]

devastating_attack_ = [
"%s, you found a weak point. \n%s loses %d HP.\n",
"%s, tu as trouvé un point faible. \n%s perd %d PdeV.\n"
]

defend_ = [
"%s is defending.\n",
"%s se défend.\n"
]

rest_ = [
"After resting, \n%s's HP increase by %d.\n",
"Après récupération, \nles PdeV de %s augmentent de %d.\n"
]

###############################################
