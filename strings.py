answers = {
    "greeting" : ["Hello","Sawa"],
    "bloodtype" : ["What is your blood type ?","Aina yako ya damu ni nini?"],
    "weight" : ["What is your weight ?","Uzani wako ni nini?"],
    "height" : ["What is your height ?","Urefu wako ni nini ?"],
    "name" : ["How would you like me to call you?","Ungependaje kukuita?"],
    "default" : ["I did not quite catch what have you said","Sikuwa na kukamata kabisa nini umesema"],
    "changeLang" : ["I noticed that you speak a different language so I adapted quickly","Niligundua kwamba unasema lugha tofauti na hivyo nimebadili haraka"],
    "instVer" : ["In order to complete the verification text the code to the number : ","Ili kukamilisha maandishi ya uthibitisho msimbo kwa idadi:"],
    "freeCharge" : ["The Text Message Is Free Of Charge To The Consumer","Ujumbe wa Nakala Huru ya Malipo Kwa Mtumiaji"],
    "notVerified" : ["If the response doesn't say 'OK, Genuine/Original', promptly call for help","Ikiwa majibu hayasema 'Sahihi, ya kweli / ya asili', piga simu kwa msaada"],
    "medicine" : ["medicine","dawa"],
    "drug" : ["drug","dawa"]
}

swahili = ["Na","Mbaya", "Baiskeli", "Chungu", "Gari" , "Baridi" , "Hatari" , "Kinywaji",
"Kunywa",   "Kula" ,"Samahani","Chakula", "Rafiki","Nzuri","Kwaheri"   ,"Nisaidie tafadhali",   "Hapa",    "Moto",    "Vipi" , "Nimekasirika"  , "Ninasafiri"    ,"Nimefurahi"  ,"Ninaweza kusema" ,"Kiswahili",  
"Siwezi kusema" ,"Kiswahili",  "Ninakupenda" , "Pikipiki", "Hapana","Sawa" ,"Tafadhali"   
 ,"Samahani",    "Tamu",    
 "Asante",    "Asante sana"  , "Pale"  ,  "Sana",    "Maji"   , "Karibu"   ," Nini "   ,"Wakati gani" 
  " Wapi"  ,  "Unakwenda wapi" ,   "Ipi" ,    "Ndio"] 

checkAuthenticity ={[Sproxil,38353],[Pharmasecure,38351],[UBQ,20966],[Kezzler,20966],[Savante,38120],[M-Pedigree,1393]}

def checkIfReal(scratchCode,companyName):
    for x in checkAuthenticity:
        if a == x[0]
            return x[1]
    return -1

def instructionMessage(numberSMS)
    sendMessage(answers[instVer][language],author_id)
    sendMessage(numberSMS,author_id)
    sendMessage(answers[freeCharge][language],author_id)
    sendMessage(answers[notVerified][language],author_id)


