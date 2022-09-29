# coding=utf-8
import numpy as np
# Flask utils
from flask import Flask, url_for, request, render_template
import pickle
area_mean = {'abasaheb raikar nagar': 8550.0,
 'adarsh colony': 17200.0,
 'adarsh nagar': 17187.5,
 'airport road': 9125.0,
 'akurdi': 15455.76923076923,
 'alandi': 7694.444444444444,
 'alandi road': 12000.0,
 'amanora town ship': 21333.333333333332,
 'ambedkar nagar': 17083.333333333332,
 'ambegaon': 12193.333333333334,
 'ambegaon bk': 10122.58064516129,
 'ambegaon budruk': 11452.830188679245,
 'ambegaon kh': 6833.333333333333,
 'ambegaon pathar': 7043.478260869565,
 'anand nagar': 14336.363636363636,
 'anand park': 14750.0,
 'anand park nagar': 17833.333333333332,
 'anthon nagar': 10600.0,
 'apex colony': 22000.0,
 'ashok nagar': 20100.0,
 'ashoka nagar': 21320.833333333332,
 'aundh': 18957.508761785713,
 'aundh annexe': 21416.666666666668,
 'aundh gaon': 19307.69230769231,
 'aundh road': 15400.0,
 'autadwadi handewadi': 14262.5,
 'awhalwadi': 5750.0,
 'azad nagar': 14750.0,
 'b.t kawade road': 19693.333333333332,
 'baderaj colony': 12500.0,
 'bakhori': 7500.0,
 'bakori': 4500.0,
 'balaji nagar': 8428.57142857143,
 'balewadi': 22371.995327256638,
 'balewadi phata': 21068.0,
 'baner': 22388.96376253289,
 'baner pashan link road': 18394.736842105263,
 'baner-sus': 18800.0,
 'bankar vasti': 12166.666666666666,
 'bavdhan': 18339.708246851853,
 'bekrai nagar': 7535.714285714285,
 'beside sundar sankul society': 10000.0,
 'bhageerath': 29333.333333333332,
 'bhagwan nagar': 14666.666666666666,
 'bhagyoday nagar': 7900.0,
 'bhairav nagar': 9795.454545454546,
 'bhairavnagar dhanori rd': 6250.0,
 'bhandarkar road': 33500.0,
 'bharati vidyapeeth': 12444.444444444445,
 'bhausaheb kalate nagar': 16000.0,
 'bhawani peth': 21222.222222222223,
 'bhekrai nagar': 8698.076923076924,
 'bhelkenagar': 13250.0,
 'bhosale nagar': 21150.0,
 'bhosari': 11070.0,
 'bhugaon': 13458.89847595238,
 'bhujbal vasti': 17571.428571428572,
 'bhukum': 11727.272727272728,
 'bhumkar nagar': 17584.21052631579,
 'bhunde vasti': 21682.272727272728,
 'bhusari colony': 17855.454545454544,
 'bibwewadi': 14513.414634146342,
 'bibwewadi annex': 12900.0,
 'bibwewadi kondhwa road': 14666.666666666666,
 'bijali nagar': 10333.333333333334,
 'bijle nagar': 11000.0,
 'bijlinagar': 12083.333333333334,
 'boat club road': 29791.067425714285,
 'bopkhel': 8200.0,
 'bopodi': 15916.666666666666,
 'borade vasti': 10075.0,
 'borate vasti': 7750.0,
 'borhade wadi': 12500.0,
 'bund garden': 20714.285714285714,
 'camp': 19416.666666666668,
 'chaitanya nagar': 12000.0,
 'chakan': 9380.0,
 'chandan nagar': 12155.0,
 'chandni chowk': 14250.0,
 'chandrabhaga nagar': 17250.0,
 'charholi': 14904.761904761905,
 'charholi budruk': 12785.714285714286,
 'charholi kurd': 13750.0,
 'chaudhari park': 15250.0,
 'chikhali': 12015.378105131578,
 'chinchwad': 15195.045045045044,
 'chinchwad gaon': 12846.153846153846,
 'chintamani nagar': 14833.333333333334,
 'chovisawadi': 4950.0,
 'clover park': 19309.52380952381,
 'dahanukar colony': 19005.263157894737,
 'dangat patil nagar': 9833.333333333334,
 'dange chowk': 14800.0,
 'dapodi': 13535.714285714286,
 'dashrath nagar': 21666.666666666668,
 'datta mandir road': 24000.0,
 'dattanagar': 10525.0,
 'dattawadi': 15875.0,
 'daund': 5500.0,
 'defence area': 13250.0,
 'dehu': 9500.0,
 'dehu road': 8833.333333333334,
 'dhankawadi': 11534.09090909091,
 'dhanori': 14667.1875,
 'dhanori jakat naka': 8500.0,
 'dhayari': 10347.560975609756,
 'dhayari phata': 12323.529411764706,
 'dhayri': 6500.0,
 'dhore nagar': 14000.0,
 'digambar nagar': 26714.285714285714,
 'dighi': 10068.65671641791,
 'dombi wadi': 26500.0,
 'dudhane nagar': 12000.0,
 'eknath pathare vasti': 17833.333333333332,
 'eon free zone': 21219.140333125,
 'erandwana gaothan': 16750.0,
 'erandwane': 20833.333333333332,
 'f c road': 21700.0,
 'fatima nagar': 15488.888888888889,
 'fursungi gaon': 10076.923076923076,
 'gadital': 13650.0,
 'gahunje': 12371.42857142857,
 'gaikwad nagar': 7500.0,
 'gaikwad vasti': 10500.0,
 'gandhi peth': 12500.0,
 'ganesh nagar': 15695.652173913044,
 'ganesh peth': 14750.0,
 'ganga nagar': 7166.666666666667,
 'gangarde nagar': 15000.0,
 'gangotri nagar': 10000.0,
 'garmal': 8500.0,
 'ghorpade peth': 10166.666666666666,
 'ghorpadi': 15997.058823529413,
 'ghotawade phata': 6000.0,
 'giridhar nagar': 8285.714285714286,
 'gokhale nagar': 15727.272727272728,
 'gokul colony': 14250.0,
 'gokul nagar': 9750.0,
 'gokulnagar': 11400.0,
 'gondhale nagar': 11111.111111111111,
 'gujarat colony': 14777.777777777777,
 'gujrat colony': 19000.0,
 'gulab nagar': 7500.0,
 'gultekadi': 21666.666666666668,
 'guruvar peth': 13357.142857142857,
 'hadapsar': 15886.81992239382,
 'hadapsar gaon': 13445.0,
 'handewadi': 11581.159420289856,
 'handewadi road': 10833.333333333334,
 'hanuman nagar': 16550.0,
 'happy colony': 18500.0,
 'hingane mala': 10000.0,
 'hingne budrukh': 13000.0,
 'hingne khurd': 11214.285714285714,
 'hinjewadi': 16218.77037037037,
 'hinjewadi phase 1': 18349.157877346937,
 'hinjewadi phase 2': 19024.590163934427,
 'ideal colony': 18714.285714285714,
 'indira nagar': 13750.0,
 'indrayani nagar': 13166.666666666666,
 'indrayani nagar sector 2': 13500.0,
 'ingawale nagar': 15275.0,
 'j.m road': 23250.0,
 'jadhav nagar': 8333.333333333334,
 'jadhav wadi': 8500.0,
 'jagtap dairy': 12500.0,
 'jai bhavani nagar': 24002.5,
 'jambhe': 11500.0,
 'jambhul': 5000.0,
 'jambhulkar mala': 15250.0,
 'jambhulwadi': 13666.666666666666,
 'janwadi': 7000.0,
 'jarande nagar': 13500.0,
 'jawakar nagar': 18750.0,
 'jawalkar nagar': 11250.0,
 'jaymala nagar': 8000.0,
 'jijai nagar': 22333.333333333332,
 'jyotiba colony': 13250.0,
 'kad nagar': 13200.0,
 'kadamwak wasti': 5500.0,
 'kalas': 15111.111111111111,
 'kalas area': 15562.5,
 'kale padal': 10078.947368421053,
 'kalepadal': 9187.5,
 'kalewadi': 11487.205128205129,
 'kalewadi phata': 11613.333333333334,
 'kalwad wasti': 9083.416666666666,
 'kalyani nagar': 25598.200327534243,
 'kalyani nagar annexe': 26500.0,
 'kamgar nagar': 11875.0,
 'kanchan nagari': 7750.0,
 'kanhe': 6666.666666666667,
 'kanifnath colony': 9500.0,
 'karambhumi nagar': 7250.0,
 'karpe nagar': 20200.0,
 'karve nagar': 15831.756756756757,
 'karve road': 21000.0,
 'karvenagar': 11800.0,
 'kasar amboli': 8300.0,
 'kasarsai': 8500.0,
 'kasarwadi': 13166.666666666666,
 'kasba peth': 12500.0,
 'kashid nagar': 12000.0,
 'kashid park': 14350.0,
 'kashinath patil nagar': 7333.333333333333,
 'kaspate vasti': 18067.74193548387,
 'kate wasti': 14480.76923076923,
 'katey basti': 24000.0,
 'katraj': 10589.411764705883,
 'katraj kondhwa road': 11000.0,
 'kavde nagar': 24000.0,
 'kedari nagar': 29333.333333333332,
 'kemse vasti': 14125.0,
 'keshav nagar': 15469.270833333334,
 'keshav nagar chinchwad': 11666.666666666666,
 'keshavnagar': 7333.333333333333,
 'kesnand': 8562.5,
 'khadki': 17607.14285714286,
 'khandve nagar': 7353.333333333333,
 'kharabwadi': 7500.0,
 'kharadi': 19982.465112782153,
 'kharadi annex': 13500.0,
 'kharalwadi': 13750.0,
 'khese park': 11812.5,
 'kirkatwadi': 7752.941176470588,
 'kirtane baugh': 25576.5519925,
 'kirti nagar': 15833.333333333334,
 'kiwale': 11532.258064516129,
 'kolawadi': 5666.666666666667,
 'kolhewadi': 6000.0,
 'kondhawe dhawade': 9125.0,
 'kondhwa': 18027.64627018018,
 'kondhwa budruk': 14080.434782608696,
 'koregaon bhima': 6975.0,
 'koregaon mul': 4500.0,
 'koregaon park': 23145.980341571427,
 'koregaon park annexe': 21604.043293529412,
 'kothrud': 16765.363636363636,
 'kothrud depo': 10250.0,
 'kranti nagar': 17000.0,
 'krishna nagar': 16500.0,
 'krushna colony': 12000.0,
 'kunj colony': 22400.0,
 'kutwal colony': 14323.529411764706,
 'lane no-2': 11500.0,
 'law college road': 18666.666666666668,
 'laxman nagar': 23106.25,
 'laxmi colony': 9200.0,
 'laxmi nagar': 13199.9,
 'laxmi-narayan nagar': 14100.0,
 'lohegaon': 10715.724719101123,
 'lohegaon-dhanori road': 8500.0,
 'lokmanya colony': 19333.333333333332,
 'lokmanya nagar': 18666.666666666668,
 'loni': 11000.0,
 'loni kalbhor': 9245.0,
 'lonikand': 7500.0,
 'lullanagar': 22365.30612244898,
 'maan': 13763.636363636364,
 'madhav nagar': 14593.75,
 'magarpatta': 20437.106222037037,
 'magarpatta city': 15600.0,
 'mahadeonagar': 6833.333333333333,
 'mahadev nagar': 10000.0,
 'mahalunge': 16294.820512820514,
 'mahalunge ingale': 7162.5,
 'maji sainik nagar': 22000.0,
 'malwadi': 15222.222222222223,
 'mamta nagar': 10166.666666666666,
 'mamurdi': 9625.0,
 'manaji nagar': 10500.0,
 'mandai': 15750.0,
 'mane wasti': 15300.0,
 'mangal das road': 26384.367995,
 'mangalwar peth': 17625.0,
 'mangdewadi': 5250.0,
 'manik baug': 12392.904761904761,
 'manjari budruk': 7797.073529411765,
 'manjari khurd': 12750.0,
 'manjri': 13571.739130434782,
 'manjri bk': 11437.5,
 'market yard': 19272.727272727272,
 'marunji': 12151.351351351352,
 'mate nagar': 11785.714285714286,
 'matoba nagar': 23500.0,
 'mauli nagar': 11750.0,
 'mayur colony': 25837.53846153846,
 'meera nagar': 25000.0,
 'meeta nagar': 10833.333333333334,
 'mhada colony': 24808.510638297874,
 'mhasoba nagar': 15500.0,
 'mhatre bridge': 12000.0,
 'midc': 12600.0,
 'mitra mandal colony': 4000.0,
 'model colony': 24844.07747263158,
 'mohamadwadi': 22174.932645053763,
 'mohan nagar': 14183.333333333334,
 'mohanwadi': 16750.0,
 'morwadi': 16118.75,
 'moshi': 12537.04347826087,
 'mukund nagar': 25666.666666666668,
 'mumbai-bangalore highway': 25000.0,
 'mundhwa': 13865.0,
 'munjaba vasti': 9825.0,
 'nagar road': 18055.555555555555,
 'nakhate vasti': 14000.0,
 'nana peth': 13750.0,
 'nande': 11750.0,
 'nanded': 14000.0,
 'nanded city': 9166.666666666666,
 'nandel fata': 12083.333333333334,
 'nandini takle nagar': 13333.333333333334,
 'narayan peth': 15950.0,
 'narhe': 8764.935064935065,
 'navi peth': 25937.5,
 'near datta mandir': 10750.0,
 'nehru nagar': 14142.857142857143,
 'nere': 11220.833333333334,
 'new nana peth': 14500.0,
 'new sangavi': 11333.333333333334,
 'new sanghvi': 11455.0,
 'nibm': 18818.400943396227,
 'nibm annex': 21750.0,
 'nigade nagar': 21333.333333333332,
 'nigdi': 15197.67441860465,
 'nigdi gaothan': 11250.0,
 'nighoje': 9000.0,
 'nimbaj nagar': 10357.142857142857,
 'nimbalkar nagar': 10875.0,
 'niranjan park': 15625.0,
 'north hadapsar': 17818.18181818182,
 'old sangvi': 11946.296296296296,
 'padmavati': 15285.714285714286,
 'panchawati': 15567.1839975,
 'panchod': 9800.0,
 'pandhare wasti': 13684.615384615385,
 'pandhari nagar': 16071.42857142857,
 'pandurang colony': 21000.0,
 'panmala': 17000.0,
 'papde wasti': 6600.0,
 'parande nagar': 11625.0,
 'parkhe vasti': 15957.142857142857,
 'parvati darshan': 14000.0,
 'parvati paytha': 10300.0,
 'pashan': 20609.17316112903,
 'pashan-sus road': 17222.222222222223,
 'pathare wasti': 7750.0,
 'patil nagar': 21366.666666666668,
 'paud gaon': 4750.0,
 'paud road': 15888.888888888889,
 'pawana nagar': 16600.0,
 'pawar nagar': 9000.0,
 'pawna nagar': 17750.0,
 'perugate': 25000.0,
 'phase-3 hinjewadi': 17744.139784946237,
 'phugewadi': 13000.0,
 'phulenagar': 10800.0,
 'phursungi': 12133.720930232557,
 'pimple gurav': 13580.967741935483,
 'pimple nilakh': 18251.34572276923,
 'pimple saudagar': 19881.340579710144,
 'pimpri': 14551.28205128205,
 'pimpri chinchwad': 14664.516129032258,
 'pingale wasti': 17075.0,
 'pirangut': 7666.666666666667,
 'pisoli': 11802.380952380952,
 'postal colony': 11200.0,
 'prabhat road': 29285.714285714286,
 'pradhikaran': 15968.75,
 'pragati nagar': 17500.0,
 'pranjali patil nagar': 14000.0,
 'prasad nagar': 15000.0,
 'pratibha nagar': 6500.0,
 'pratik nagar': 13875.0,
 'punawale': 14223.140495867769,
 'pune': 12107.142857142857,
 'pune  bibwewadi': 9666.666666666666,
 'pune  nibm': 19500.0,
 'pune mumbai highway': 19700.0,
 'pune nagar road': 7000.0,
 'pune-satara road': 12300.0,
 'pura bhandari colony': 15500.0,
 'purnanagar': 17500.0,
 'raghavendra nagar': 19722.222222222223,
 'raghoba patil nagar': 8388.888888888889,
 'rahatani': 17668.14285714286,
 'rahatni': 10750.0,
 'rajaram patil nagar': 18400.0,
 'rajendra nagar': 15500.0,
 'rajiv nagar north': 19000.0,
 'rakshak nagar': 14875.0,
 'ram nagar': 16500.0,
 'rambagh colony': 12500.0,
 'rambaug colony': 23250.0,
 'ramkrishna paramhans nagar': 14625.0,
 'ranjangaon': 6000.0,
 'rasta peth': 13300.0,
 'ratnadeep colony': 6333.333333333333,
 'ravet': 14519.277108433735,
 'renuka nagar': 10833.333333333334,
 'rupeenagar': 5750.0,
 'sadashiv peth': 19050.0,
 'sade satra nali': 20750.0,
 'sahakar nagar': 18125.0,
 'sahakar nagar ii': 25000.0,
 'sahu colony': 14500.0,
 'sai colony': 12125.0,
 'sai nagar': 12000.0,
 'sai nagar park': 20000.0,
 'sai vittal nagar': 8000.0,
 'saibaba nagar': 13500.0,
 'sainath nagar': 15250.0,
 'sainathnagar nigdi': 9500.0,
 'sainikwadi': 12200.0,
 'sakal nagar': 16900.0,
 'sakore nagar': 20687.5,
 'salisbury park': 16388.88888888889,
 'salunke vihar': 22050.0,
 'samarth colony': 18000.0,
 'sambhaji nagar': 10750.0,
 'sanaswadi': 4500.0,
 'sanewadi': 21181.81818181818,
 'sangam nagar': 9250.0,
 'sangamvadi': 19846.153846153848,
 'sanghvi': 10214.285714285714,
 'sangvi': 15166.666666666666,
 'sanjay park': 15400.0,
 'sant nagar': 8154.545454545455,
 'sant tukaram nagar': 11666.666666666666,
 'santosh nagar': 9400.0,
 'sasane colony': 9166.666666666666,
 'sasane nagar': 10880.357142857143,
 'sasanenagar': 14000.0,
 'satar nagar': 10833.333333333334,
 'satav nagar': 13055.555555555555,
 'satavwadi': 7500.0,
 'sathe nagar': 12300.0,
 'sector no-26 pradhikaran': 18312.5,
 'sector no-27 pradhikaran': 7850.0,
 'sector no-27a pradhikaran': 14333.333333333334,
 'sector no-3 bhosari': 17833.333333333332,
 'sector no-4 moshi': 11124.75,
 'sector-16 chikhali': 9000.0,
 'sector-25 pradhikaran': 12000.0,
 'sector-29 ravet': 15217.391304347826,
 'sector-6 moshi': 13750.0,
 'senapati bapat road': 22333.333333333332,
 'seva nagar': 15250.0,
 'shahunagar': 12919.9,
 'shani nagar': 7000.0,
 'shaniwar peth': 15785.714285714286,
 'shankar kalat nagar': 19110.694029850747,
 'shanti nagar': 16250.0,
 'shastri nagar': 18893.939393939392,
 'shatrunjay nagar': 20000.0,
 'shewalewadi': 13611.111111111111,
 'shikrapur': 5800.0,
 'shikshaknagar': 12000.0,
 'shinde vasti': 15860.0,
 'shindenagar': 14652.777777777777,
 'shindewadi': 5500.0,
 'shiraswadi': 4250.0,
 'shirgaon': 8800.0,
 'shitole nagar': 7750.0,
 'shiv colony': 5500.0,
 'shivaji nagar': 20294.117647058825,
 'shivajinagar': 22000.0,
 'shivane': 8697.058823529413,
 'shivneri nagar': 10750.0,
 'shivtirth nagar': 16416.666666666668,
 'shree datta colony': 25250.0,
 'shreenath nagar': 8250.0,
 'shriram nagar': 11000.0,
 'shukravar peth': 12375.0,
 'siddartha nagar': 15821.690352352942,
 'siddharth nagar': 18234.375,
 'siddheshwar nagar': 13250.0,
 'sinhagad road': 13500.0,
 'sinhgad road': 13996.907216494845,
 'somatane': 8775.0,
 'somatne phata': 8600.0,
 'someshwarwadi': 19272.727272727272,
 'somnath nagar': 11365.0,
 'somwar peth': 15750.0,
 'sopan baug': 24111.241594000003,
 'sopan nagar': 12500.0,
 'st tukaram nagar': 17166.666666666668,
 'subhash nagar': 11000.0,
 'sudarshan nagar': 11314.285714285714,
 'sukhsagar nagar': 9872.727272727272,
 'sunita nagar': 10250.0,
 'suryalok nagari': 15700.0,
 'sus': 15984.126984126984,
 'sutarwadi': 12125.0,
 'swami samarth nagar': 9714.285714285714,
 'swami vivekanand nagar': 11400.0,
 'swar gate': 19000.0,
 'swatantrya sainik nagar': 24250.0,
 'tadiwala road': 12250.0,
 'talajai pathar': 15125.0,
 'talawade': 13750.0,
 'talegaon': 8982.051282051281,
 'talegaon dabhade': 9466.666666666666,
 'tanaji nagar': 11375.0,
 'tapkir nagar': 11833.333333333334,
 'tathawade': 16744.162790697676,
 'taware colony': 17875.0,
 'telco colony': 10500.0,
 'thergaon': 14512.511904761905,
 'thite nagar': 15245.454545454546,
 'tilekar nagar': 9100.0,
 'tilekar vasti': 22333.333333333332,
 'tingre nagar': 15710.135135135135,
 'tukai darshan': 7937.5,
 'tukaram nagar': 17171.428571428572,
 'tulaja bhawani nagar': 22040.909090909092,
 'ubale nagar': 12115.0,
 'udyog nagar': 13187.5,
 'undri': 15698.267045454546,
 'upper indira nagar': 10166.666666666666,
 'uruli devachi': 8791.666666666666,
 'uruli kanchan': 6750.0,
 'uttam nagar': 8833.333333333334,
 'vadgaon': 12500.0,
 'vadgaon budruk': 11409.09090909091,
 'vadgaon maval': 11625.0,
 'vadgaon sheri': 11707.377049180328,
 'vadgaonsheri': 10500.0,
 'vaiduwadi': 15533.333333333334,
 'vallabh nagar': 21857.14285714286,
 'varale': 7500.0,
 'veerbhadra nagar': 26428.571428571428,
 'venu nagar cotes': 19250.0,
 'vidyanagar': 15000.0,
 'vighnaharta nagar': 8700.0,
 'vijay nagar': 11166.666666666666,
 'vikas nagar': 12812.5,
 'viman nagar': 20489.58323802721,
 'vinayak nagar': 12400.0,
 'vishal nagar': 17483.870967741936,
 'vishawshanti colony': 18000.0,
 'vishnu dev nagar': 19625.0,
 'vishnupuram colony': 12250.0,
 'vishrantwadi': 15701.801801801801,
 'vittalvadi': 14000.0,
 'vitthal nagar': 12500.0,
 'wadachi wadi': 11000.0,
 'wadebolai': 15250.0,
 'wadegaon': 10500.0,
 'wadeshwar nagar': 10000.0,
 'wadgaon budruk': 13018.75,
 'wadgaon sheri': 13137.797485619047,
 'wadgaonsheri': 12812.5,
 'wadki': 7000.0,
 'wadmukhwadi': 10333.333333333334,
 'wageshwar nagar': 11166.666666666666,
 'wagholi': 12512.976635514018,
 'wagholi  wagholi': 6000.0,
 'wakad': 18519.142616282305,
 'wakad annexe': 16000.0,
 'wakadkar wasti': 14818.181818181818,
 'wakdewadi': 30000.0,
 'walhekarwadi': 8958.333333333334,
 'walvekar nagar': 18000.0,
 'wanawari': 13785.714285714286,
 'wanowrie': 23368.263473053892,
 'wanwadi': 21262.29508196721,
 'warje': 12893.518518518518,
 'warje malwadi': 10962.962962962964,
 'wireless colony': 19385.714285714286,
 'yamuna nagar': 11178.57142857143,
 'yashoda colony': 11000.0,
 'yashwant nagar': 14750.0,
 'yashwantrao chavan nagar': 5666.666666666667,
 'yerwada': 16155.172413793103,
 'yewalewadi': 10560.441860465116,
 'yojana nagar': 5666.666666666667}
# Define a flask app
app = Flask(__name__)

model = pickle.load(open("model.pkl", 'rb'))







@app.route('/', methods=['GET'])
def home():
    # Main page
    return render_template('home.html')


@app.route('/result',methods=['GET','POST'])
def home1():
    if request.method =="POST":
        bhk = int(request.form['bedroom'])
        area = int(request.form['area'])
        locality = request.form['locality']
        locality = locality.lower()
        pooja = request.form['pooja']
        servant = request.form['servant']
        lightbill = request.form['lightbill']
        study = request.form['study']
        store = request.form['store']
        powerbackup = request.form['powerbackup']
        parking = int(request.form['parking'])
        furnishing = request.form['furnishing']
        floor_type = request.form['floorType']
        floor_number = int(request.form['floor'])
        brokerage = int(request.form['brokerage'])
        maintainance = int(request.form['maintainance'])
        deposit = int(request.form['deposit'])
        

        #Pooja room

        if pooja == 'No':
            pooja = 0
        else:
            pooja = 1

        #Servant room

        if servant == 'No':
            servant = 0
        else:
            servant = 1

        #lightbill

        if lightbill == 'No':
            lightbill = 0
        else:
            lightbill = 1

        #Study room

        if study == 'No':
            study = 0
        else:
            study = 1

        #Store room

        if store == 'No':
            store = 0
        else:
            store = 1
        
        #furnishing

        if furnishing == 'Unfurnished':
            furnishing = 'furnishing_Unfurnished'
        elif furnishing == 'Semifurnished':
            furnishing = 'furnishing_Semifurnished'
        else:
            furnishing = 'furnishing_Furnished'

        #floor type

        if floor_type == 'Cement':
            floor_type = 'floor_type_Cement'
        elif floor_type == 'Ceramic':
            floor_type = 'floor_type_Ceramic'
        elif floor_type == 'Concrete':
            floor_type = 'floor_type_Concrete'
        elif floor_type == 'Granite':
            floor_type = 'floor_type_Granite'
        elif floor_type == 'IPSfinish':
            floor_type = 'floor_type_IPSfinish'
        elif floor_type == 'Marble':
            floor_type = 'floor_type_Marble'
        elif floor_type == 'Mosaic':
            floor_type = 'floor_type_Mosaic'
        elif floor_type == 'Polished Concrete':
            floor_type = 'floor_type_Polished concrete'
        elif floor_type == 'Spartex':
            floor_type = 'floor_type_Spartex'
        elif floor_type == 'Stone':
            floor_type = 'floor_type_Stone'
        elif floor_type == 'Vinyl':
            floor_type = 'floor_type_Vinyl'
        elif floor_type == 'Vitrified':
            floor_type = 'floor_type_Vitrified'
        elif floor_type == 'Wood':
            floor_type = 'floor_type_Wood'
        else:
            floor_type = 'floor_type_Not provided'

        lst = ['bedroom', 'area', 'floor_number', 'parking', 'lightbill',
       'powerbackup', 'pooja_room', 'study_room', 'servant_room', 'brok_amt',
       'deposit_amt', 'mnt_amt', 'address_num', 'furnishing_Semifurnished',
       'furnishing_Unfurnished', 'floor_type_Ceramic', 'floor_type_Concrete',
       'floor_type_Marble', 'floor_type_Mosaic', 'floor_type_Not provided',
       'floor_type_Others', 'floor_type_Polished concrete',
       'floor_type_Spartex', 'floor_type_Vinyl', 'floor_type_Vitrified',
       'floor_type_Wood', 'gate_community_Yes', 'wheelchairadption_Yes']
        lst = np.array(lst)
        address_number = area_mean[locality]
        fur_index = np.where(lst==furnishing)[0][0]
        floor_index = np.where(lst==floor_type)[0][0]
        x = np.zeros(28)
        x[0] = bhk
        x[1] = area
        x[2] = floor_number
        x[3] = parking
        x[4] = lightbill
        x[5] = powerbackup
        x[6] = pooja
        x[7] = study
        x[8] = servant
        x[9] = brokerage
        x[10] = deposit
        x[11] = maintainance
        x[12] = address_number
        x[26] = 1
        x[27] = 1

        if fur_index >= 0:
            x[fur_index] = 1
    
        if floor_index >= 0:
            x[floor_index] = 1

        prediction = model.predict([x])
        rent = round(prediction[0])
        return render_template("result.html", prediction_text=f"Approximate Rent is {rent} Rs.")

    else:
        render_template('home.html')





if __name__ == '__main__':
    app.run(debug=True)
