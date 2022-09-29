# coding=utf-8
import numpy as np
# Flask utils
from flask import Flask, url_for, request, render_template
import pickle
area_mean = {'Abasaheb Raikar Nagar': 9562.5,
 'Adarsh Colony': 17200.0,
 'Adarsh Nagar': 17187.5,
 'Airport Road': 9125.0,
 'Akurdi': 15512.727272727272,
 'Alandi': 7852.941176470588,
 'Alandi Road': 12000.0,
 'Amanora town ship': 21375.0,
 'Ambedkar Nagar': 16785.714285714286,
 'Ambegaon': 12734.48275862069,
 'Ambegaon Bk': 10946.666666666666,
 'Ambegaon Budruk': 12343.75,
 'Ambegaon Kh': 6833.333333333333,
 'Ambegaon Pathar': 7900.0,
 'Anand Nagar': 14362.71186440678,
 'Anand Park': 14750.0,
 'Anand Park Nagar': 17833.333333333332,
 'Anthon Nagar': 9200.0,
 'Apex Colony': 22000.0,
 'Ashok Nagar': 20100.0,
 'Ashoka Nagar': 22007.40740740741,
 'Aundh': 19293.398773006134,
 'Aundh Annexe': 21416.666666666668,
 'Aundh Gaon': 19307.69230769231,
 'Aundh Road': 14050.0,
 'Autadwadi Handewadi': 14262.5,
 'Awhalwadi': 6000.0,
 'Azad Nagar': 14750.0,
 'B.T Kawade Road': 19832.25806451613,
 'Baderaj Colony': 12500.0,
 'Bakhori': 7500.0,
 'Balaji Nagar': 8285.714285714286,
 'Balewadi': 22357.125,
 'Balewadi Phata': 22340.68181818182,
 'Baner': 22157.344873940398,
 'Baner Pashan Link Road': 18583.333333333332,
 'Baner-Sus': 20266.666666666668,
 'Bankar Vasti': 12166.666666666666,
 'Baramati': 15500.0,
 'Bavdhan': 18325.528301886792,
 'Bebadohal': 15000.0,
 'Bekrai Nagar': 8181.818181818182,
 'Bhageerath': 29000.0,
 'Bhagwan Nagar': 12125.0,
 'Bhagyoday Nagar': 7900.0,
 'Bhairav Nagar': 9795.454545454546,
 'Bhandarkar Road': 33500.0,
 'Bharati Vidyapeeth': 11900.0,
 'Bhausaheb Kalate Nagar': 16000.0,
 'Bhawani Peth': 21222.222222222223,
 'Bhekrai Nagar': 9245.454545454546,
 'Bhelkenagar': 13250.0,
 'Bhosale Nagar': 21150.0,
 'Bhosari': 10896.969696969696,
 'Bhugaon': 13615.51282051282,
 'Bhujbal Vasti': 17571.428571428572,
 'Bhukum': 11428.57142857143,
 'Bhumkar Nagar': 17305.0,
 'Bhunde Vasti': 21682.272727272728,
 'Bhusari Colony': 17986.274509803923,
 'Bhusari colony': 18375.0,
 'Bibwewadi': 14489.024390243903,
 'Bibwewadi Annex': 15000.0,
 'Bibwewadi Kondhwa Road': 14666.666666666666,
 'Bijali Nagar': 10333.333333333334,
 'Bijle Nagar': 11000.0,
 'Bijlinagar': 12083.333333333334,
 'Boat Club Road': 31800.0,
 'Bopkhel': 9250.0,
 'Bopodi': 16000.0,
 'Borade Vasti': 10075.0,
 'Borhade Wadi': 12500.0,
 'Budhwar Peth': 15000.0,
 'Bund Garden': 23200.0,
 'Camp': 19416.666666666668,
 'Chaitanya Nagar': 12000.0,
 'Chakan': 10011.538461538461,
 'Chandan Nagar': 12397.619047619048,
 'Chandni Chowk': 14250.0,
 'Chandrabhaga Nagar': 17250.0,
 'Charholi': 14636.363636363636,
 'Charholi Budruk': 12785.714285714286,
 'Charholi Kurd': 13750.0,
 'Chaudhari Park': 15250.0,
 'Chikhali': 12060.632934935064,
 'Chinchwad': 15460.091743119267,
 'Chinchwad Gaon': 12846.153846153846,
 'Chintamani Nagar': 14833.333333333334,
 'Chovisawadi': 6900.0,
 'Clover Park': 18552.63157894737,
 'Dahanukar Colony': 18783.333333333332,
 'Dangat Patil Nagar': 10500.0,
 'Dange Chowk': 14678.57142857143,
 'Dapodi': 13535.714285714286,
 'Dashrath Nagar': 21666.666666666668,
 'Dattanagar': 11108.333333333334,
 'Dattawadi': 16409.090909090908,
 'Deccan Gymkhana': 9000.0,
 'Defence Area': 11666.666666666666,
 'Dehu': 13000.0,
 'Dehu Road': 9218.75,
 'Dhankawadi': 11336.95652173913,
 'Dhanori': 14766.145833333334,
 'Dhanori Jakat Naka': 8500.0,
 'Dhayari': 10120.481927710844,
 'Dhayari Phata': 12323.529411764706,
 'Dhayri': 8000.0,
 'Dhore Nagar': 14000.0,
 'Digambar Nagar': 25500.0,
 'Dighi': 10501.587301587302,
 'Dombi Wadi': 26500.0,
 'Dudhane Nagar': 12000.0,
 'Eknath Pathare Vasti': 17833.333333333332,
 'Eon Free Zone': 21565.55381806818,
 'Erandwana Gaothan': 16750.0,
 'Erandwane': 20214.285714285714,
 'F C Road': 21700.0,
 'Fatima Nagar': 15364.285714285714,
 'Fursungi Gaon': 11600.0,
 'Gadital': 13650.0,
 'Gahunje': 11950.0,
 'Gaikwad Nagar': 7500.0,
 'Gaikwad Vasti': 10500.0,
 'Gandhi Peth': 12500.0,
 'Ganesh Nagar': 15475.0,
 'Ganesh Peth': 14750.0,
 'Ganesh nagar': 16000.0,
 'Ganga Nagar': 7300.0,
 'Gangarde Nagar': 15000.0,
 'Gangotri Nagar': 10000.0,
 'Garmal': 8500.0,
 'Ghorpade Peth': 10166.666666666666,
 'Ghorpadi': 16358.333333333334,
 'Ghotawade Phata': 6000.0,
 'Giridhar Nagar': 8285.714285714286,
 'Gokhale Nagar': 15916.666666666666,
 'Gokul Colony': 14250.0,
 'Gokul Nagar': 9166.666666666666,
 'Gondhale Nagar': 11111.111111111111,
 'Gujarat Colony': 14857.142857142857,
 'Gujrat Colony': 19000.0,
 'Gulab Nagar': 7500.0,
 'Gultekadi': 21666.666666666668,
 'Guru Nanak Nagar': 16500.0,
 'Guruvar Peth': 13357.142857142857,
 'HADAPSAR': 21000.0,
 'Hadapsar': 15842.26326378323,
 'Hadapsar Gaon': 13471.42857142857,
 'Hadapsar Indutrial Estate': 19500.0,
 'Handewadi': 11755.223880597016,
 'Handewadi Road': 9250.0,
 'Hanuman Nagar': 16550.0,
 'Happy Colony': 18500.0,
 'Hingane Mala': 10000.0,
 'Hingne Budrukh': 13000.0,
 'Hingne Khurd': 12250.0,
 'Hinjewadi': 16453.13543599258,
 'Hinjewadi Phase 1': 18192.174719799998,
 'Hinjewadi Phase 2': 19016.129032258064,
 'Ideal Colony': 18166.666666666668,
 'Indira Nagar': 13750.0,
 'Indrayani Nagar': 13166.666666666666,
 'Indrayani Nagar Sector 2': 12666.666666666666,
 'Ingawale Nagar': 15275.0,
 'J.M Road': 23250.0,
 'Jadhav Nagar': 8333.333333333334,
 'Jadhav Wadi': 8500.0,
 'Jagtap Dairy': 12500.0,
 'Jai Bhavani Nagar': 24002.5,
 'Jambhe': 11500.0,
 'Jambhul': 6000.0,
 'Jambhulkar Mala': 15250.0,
 'Jambhulwadi': 15000.0,
 'Janwadi': 7000.0,
 'Jarande Nagar': 13500.0,
 'Jawakar Nagar': 18750.0,
 'Jawalkar Nagar': 11250.0,
 'Jaymala Nagar': 8000.0,
 'Jijai Nagar': 22333.333333333332,
 'Jyotiba Colony': 13500.0,
 'Kad Nagar': 12862.5,
 'Kalas': 15111.111111111111,
 'Kalas Area': 15562.5,
 'Kale Padal': 10444.444444444445,
 'Kalepadal': 10333.333333333334,
 'Kalewadi': 11743.615384615385,
 'Kalewadi Phata': 11613.333333333334,
 'Kalwad Wasti': 9750.1,
 'Kalyani Nagar': 25646.18235053435,
 'Kalyani Nagar Annexe': 27071.428571428572,
 'Kamgar Nagar': 11875.0,
 'Kanchan Nagari': 12000.0,
 'Kanhe': 8500.0,
 'Kanifnath Colony': 9500.0,
 'Karpe Nagar': 20200.0,
 'Karve Nagar': 16111.805555555555,
 'Karve Road': 19166.666666666668,
 'Kasar Amboli': 7900.0,
 'Kasarsai': 8500.0,
 'Kasarwadi': 13166.666666666666,
 'Kasba Peth': 12500.0,
 'Kashid Nagar': 12000.0,
 'Kashid Park': 14500.0,
 'Kashinath Patil Nagar': 7333.333333333333,
 'Kaspate Vasti': 18034.375,
 'Kate Wasti': 14480.76923076923,
 'Katey Basti': 24000.0,
 'Katraj': 11330.666666666666,
 'Katraj Kondhwa Road': 12250.0,
 'Kavde Nagar': 24000.0,
 'Kedari Nagar': 29333.333333333332,
 'Kemse Vasti': 14125.0,
 'Keshav Nagar': 15941.081081081082,
 'Keshav Nagar Chinchwad': 11666.666666666666,
 'Keshavnagar': 9000.0,
 'Kesnand': 8785.714285714286,
 'Khadki': 17607.14285714286,
 'Khandve Nagar': 7191.666666666667,
 'Kharabwadi': 7500.0,
 'Kharadi': 20175.59491287599,
 'Kharadi Annex': 13500.0,
 'Kharalwadi': 13750.0,
 'Khese Park': 11444.444444444445,
 'Kirkatwadi': 8480.0,
 'Kirtane Baugh': 26384.367995,
 'Kirti Nagar': 15833.333333333334,
 'Kiwale': 11532.258064516129,
 'Kolhewadi': 6000.0,
 'Kondhawe Dhawade': 9125.0,
 'Kondhwa': 17937.931034482757,
 'Kondhwa Budruk': 15273.809523809523,
 'Koregaon Bhima': 8450.0,
 'Koregaon Mul': 6000.0,
 'Koregaon Park': 23598.354525789477,
 'Koregaon Park Annexe': 21794.117647058825,
 'Kothrud': 17028.833333333332,
 'Kranti Nagar': 17000.0,
 'Krushna Colony': 12000.0,
 'Kunj Colony': 22400.0,
 'Kutwal Colony': 14906.25,
 'Lane No-2': 11500.0,
 'Law College Road': 18000.0,
 'Laxman Nagar': 23106.25,
 'Laxmi Colony': 9200.0,
 'Laxmi Nagar': 12222.111111111111,
 'Laxmi Vihar': 20000.0,
 'Laxmi-Narayan Nagar': 14250.0,
 'Lohegaon': 11351.585987261147,
 'Lohegaon-dhanori road': 8500.0,
 'Lokmanya Colony': 19333.333333333332,
 'Lokmanya Nagar': 18666.666666666668,
 'Loni': 14000.0,
 'Loni Kalbhor': 9888.235294117647,
 'Lonikand': 7833.333333333333,
 'Lullanagar': 22428.571428571428,
 'MIDC': 12600.0,
 'Maan': 13950.0,
 'Madhav Nagar': 14593.75,
 'Madhuban Society': 10000.0,
 'Magarpatta': 20544.831703641976,
 'Magarpatta City': 15600.0,
 'Mahadeonagar': 7200.0,
 'Mahadev Nagar': 10000.0,
 'Mahalunge': 16837.425,
 'Mahalunge Ingale': 7162.5,
 'Maji Sainik Nagar': 20800.0,
 'Mallik Nagar': 13500.0,
 'Malwadi': 15222.222222222223,
 'Mamta Nagar': 9750.0,
 'Mamurdi': 10000.0,
 'Manaji Nagar': 10500.0,
 'Mandai': 15750.0,
 'Mane Wasti': 15300.0,
 'Mangal Das Road': 26384.367995,
 'Mangalwar Peth': 17625.0,
 'Manik Baug': 12392.904761904761,
 'Manjari Budruk': 8245.301886792453,
 'Manjari Khurd': 12750.0,
 'Manjri': 14945.0,
 'Manjri BK': 12000.0,
 'Market yard': 19956.521739130436,
 'Marunji': 12238.888888888889,
 'Mate Nagar': 11750.0,
 'Matoba Nagar': 23500.0,
 'Mayur Colony': 25063.428571428572,
 'Meera Nagar': 27333.333333333332,
 'Meeta Nagar': 10833.333333333334,
 'Mhada Colony': 24638.297872340427,
 'Mhasoba Nagar': 17000.0,
 'Mitra Mandal Colony': 5500.0,
 'Model Colony': 24533.333333333332,
 'Mohamadwadi': 22250.20589,
 'Mohan Nagar': 14183.333333333334,
 'Mohanwadi': 16800.0,
 'Morwadi': 16052.941176470587,
 'Moshi': 12528.957746478873,
 'Mukund Nagar': 25666.666666666668,
 'Mumbai-Bangalore Highway': 25000.0,
 'Mundhwa': 13452.5,
 'Munjaba Vasti': 10078.947368421053,
 'NIBM': 18822.434579439254,
 'Nagar Road': 18055.555555555555,
 'Nakhate Vasti': 14000.0,
 'Nana Peth': 13750.0,
 'Nande': 11750.0,
 'Nanded': 14000.0,
 'Nanded City': 7500.0,
 'Nandel Fata': 12083.333333333334,
 'Nandini Takle Nagar': 13333.333333333334,
 'Narayan Peth': 15722.222222222223,
 'Narhe': 9186.363636363636,
 'Navi Peth': 25937.5,
 'Nehru Nagar': 14142.857142857143,
 'Nere': 12165.0,
 'New Nana Peth': 14500.0,
 'New Sangavi': 12500.0,
 'New Sanghvi': 11370.731707317073,
 'Newale Wasti': 6100.0,
 'Nigade Nagar': 20125.0,
 'Nigdi': 15232.558139534884,
 'Nigdi Gaothan': 11250.0,
 'Nighoje': 10000.0,
 'Nimbaj Nagar': 10357.142857142857,
 'Nimbalkar Nagar': 10875.0,
 'Niranjan Park': 15625.0,
 'North Hadapsar': 17818.18181818182,
 'Old Sangvi': 11948.214285714286,
 'Padmavati': 15285.714285714286,
 'Panchawati': 12500.0,
 'Panchod': 9800.0,
 'Pandhare Wasti': 13684.615384615385,
 'Pandhari Nagar': 16071.42857142857,
 'Pandurang Colony': 21000.0,
 'Panmala': 17000.0,
 'Papde Wasti': 7000.0,
 'Parande Nagar': 14333.333333333334,
 'Parkhe Vasti': 15957.142857142857,
 'Parvati Darshan': 14000.0,
 'Parvati Gaon': 15500.0,
 'Parvati Paytha': 10300.0,
 'Pashan': 20841.26984126984,
 'Pashan Sus Road': 16250.0,
 'Pashan-Sus Road': 18333.333333333332,
 'Pathare Wasti': 7750.0,
 'Patil Nagar': 21366.666666666668,
 'Paud Gaon': 6000.0,
 'Paud Road': 17066.666666666668,
 'Pawana Nagar': 16600.0,
 'Pawar Nagar': 9000.0,
 'Pawna Nagar': 17750.0,
 'Perugate': 25000.0,
 'Phase-3 Hinjewadi': 17734.072164948455,
 'Phugewadi': 13000.0,
 'Phulenagar': 10800.0,
 'Phursungi': 12717.948717948719,
 'Pimple Gurav': 13680.967741935483,
 'Pimple Nilakh': 18282.539682539682,
 'Pimple Saudagar': 19887.992831541218,
 'Pimpri': 14972.972972972973,
 'Pimpri Chinchwad': 14708.8,
 'Pingale Wasti': 19844.444444444445,
 'Pirangut': 7923.076923076923,
 'Pisoli': 11730.952380952382,
 'Postal Colony': 11200.0,
 'Prabhat Road': 29285.714285714286,
 'Pradhikaran': 16088.235294117647,
 'Pragati Nagar': 17500.0,
 'Pranjali Patil Nagar': 14000.0,
 'Prasad Nagar': 15000.0,
 'Pratibha Nagar': 8000.0,
 'Pratik Nagar': 13875.0,
 'Premnagar': 23000.0,
 'Punawale': 14213.709677419354,
 'Pune': 13000.0,
 'Pune  Bibwewadi': 9666.666666666666,
 'Pune Mumbai Highway': 19700.0,
 'Pune Nagar Road': 7000.0,
 'Pune Station': 10000.0,
 'Pune-Satara Road': 12300.0,
 'Pura Bhandari Colony': 15500.0,
 'Purnanagar': 17500.0,
 'RAHATNI': 8500.0,
 'Raghavendra Nagar': 19850.0,
 'Raghoba Patil Nagar': 8388.888888888889,
 'Rahatani': 17742.563829787236,
 'Rahatni': 13000.0,
 'Rajaram Patil Nagar': 18400.0,
 'Rajendra Nagar': 15500.0,
 'Rajiv Nagar North': 19000.0,
 'Rakshak Nagar': 14875.0,
 'Ram Nagar': 16500.0,
 'Rambagh Colony': 12500.0,
 'Rambaug Colony': 23382.352941176472,
 'Ramkrishna Paramhans Nagar': 14625.0,
 'Ranjangaon': 6000.0,
 'Rasta Peth': 13388.888888888889,
 'Ratnadeep Colony': 6333.333333333333,
 'Ravet': 14501.183431952662,
 'Renuka Nagar': 10833.333333333334,
 'Rupeenagar': 5750.0,
 'Sadashiv Peth': 18882.352941176472,
 'Sade Satra Nali': 20750.0,
 'Sadhu Vaswani Nagar': 21000.0,
 'Sahakar Nagar': 18125.0,
 'Sahakar Nagar II': 25000.0,
 'Sahu Colony': 14000.0,
 'Sai Colony': 12125.0,
 'Sai Nagar': 12000.0,
 'Sai Nagar Park': 20000.0,
 'Sai Vittal Nagar': 8000.0,
 'Saibaba Nagar': 13500.0,
 'Sainath Nagar': 15250.0,
 'Sainathnagar Nigdi': 9500.0,
 'Sainikwadi': 12180.0,
 'Sakal Nagar': 16900.0,
 'Sakore Nagar': 20764.70588235294,
 'Salisbury Park': 16388.88888888889,
 'Salunke Vihar': 21953.125,
 'Samarth Colony': 14500.0,
 'Sambhaji Nagar': 10750.0,
 'Sanaswadi': 4000.0,
 'Sanewadi': 21181.81818181818,
 'Sangam Nagar': 9250.0,
 'Sangamvadi': 19833.333333333332,
 'Sanghvi': 11250.0,
 'Sangvi': 15166.666666666666,
 'Sanjay Park': 15400.0,
 'Sant Nagar': 8970.0,
 'Sant Tukaram Nagar': 13857.142857142857,
 'Santosh Nagar': 10500.0,
 'Sasane Colony': 9166.666666666666,
 'Sasane Nagar': 10933.92857142857,
 'Sasanenagar': 14000.0,
 'Satar Nagar': 10833.333333333334,
 'Satav Nagar': 13100.0,
 'Satavwadi': 7500.0,
 'Sathe Nagar': 12300.0,
 'Sector No-26 Pradhikaran': 18312.5,
 'Sector No-27 Pradhikaran': 11500.0,
 'Sector No-27A Pradhikaran': 14333.333333333334,
 'Sector No-3 Bhosari': 17833.333333333332,
 'Sector No-4 Moshi': 11124.75,
 'Sector-16 Chikhali': 9000.0,
 'Sector-25 Pradhikaran': 12000.0,
 'Sector-29 Ravet': 15000.0,
 'Sector-6 Moshi': 13750.0,
 'Senapati Bapat Road': 22333.333333333332,
 'Seva Nagar': 15250.0,
 'Shahunagar': 12919.9,
 'Shani Nagar': 8000.0,
 'Shaniwar Peth': 15615.384615384615,
 'Shankar Kalat Nagar': 19258.701492537315,
 'Shanti Nagar': 13666.666666666666,
 'Shastri Nagar': 18242.85714285714,
 'Shatrunjay Nagar': 20000.0,
 'Shewalewadi': 13750.0,
 'Shikrapur': 12500.0,
 'Shikshaknagar': 12000.0,
 'Shinde Vasti': 15860.0,
 'Shindenagar': 14652.777777777777,
 'Shindewadi': 5500.0,
 'Shirgaon': 10500.0,
 'Shitole Nagar': 8833.333333333334,
 'Shivaji Nagar': 20375.0,
 'Shivajinagar': 22000.0,
 'Shivane': 8877.777777777777,
 'Shivneri Nagar': 10750.0,
 'Shivtirth Nagar': 16785.714285714286,
 'Shree Datta Colony': 25250.0,
 'Shreenath Nagar': 8250.0,
 'Shriram Nagar': 11000.0,
 'Shukravar Peth': 13571.42857142857,
 'Siddartha Nagar': 15821.690352352942,
 'Siddharth Nagar': 19143.75,
 'Siddheshwar Nagar': 13250.0,
 'Sinhagad Road': 13500.0,
 'Sinhgad Road': 14047.959183673469,
 'Somatane': 9033.333333333334,
 'Somatne Phata': 8600.0,
 'Someshwarwadi': 19272.727272727272,
 'Somnath Nagar': 11347.619047619048,
 'Somwar Peth': 15461.538461538461,
 'Sopan Baug': 23125.0,
 'Sopan Nagar': 12500.0,
 'St Tukaram Nagar': 17166.666666666668,
 'Subhash Nagar': 11500.0,
 'Sudarshan Nagar': 10744.444444444445,
 'Sukhsagar Nagar': 10310.0,
 'Sunita Nagar': 10250.0,
 'Suryalok Nagari': 13375.0,
 'Sus': 15960.317460317461,
 'Sutarwadi': 12900.0,
 'Swami Samarth Nagar': 9714.285714285714,
 'Swami Vivekanand Nagar': 11400.0,
 'Swar Gate': 19000.0,
 'Swatantrya Sainik Nagar': 24000.0,
 'Tadiwala Road': 12250.0,
 'Talajai Pathar': 18500.0,
 'Talawade': 12700.0,
 'Talegaon': 9154.838709677419,
 'Talegaon Dabhade': 9737.931034482759,
 'Tanaji Nagar': 11375.0,
 'Tapkir Nagar': 12375.0,
 'Tathawade': 17280.463414634145,
 'Taware Colony': 17875.0,
 'Telco Colony': 10500.0,
 'Thergaon': 14805.487804878048,
 'Thite Nagar': 15231.42857142857,
 'Tilekar Nagar': 9461.538461538461,
 'Tilekar Vasti': 22333.333333333332,
 'Tingre Nagar': 15900.666666666666,
 'Tukai Darshan': 9300.0,
 'Tukaram Nagar': 17742.85714285714,
 'Tulaja Bhawani Nagar': 22197.014925373136,
 'Ubale Nagar': 12014.285714285714,
 'Udyog Nagar': 12642.857142857143,
 'Undri': 15973.226744186046,
 'Upper Indira Nagar': 10166.666666666666,
 'Uruli Devachi': 7950.0,
 'Uruli Kanchan': 7750.0,
 'Uttam Nagar': 8833.333333333334,
 'Vadgaon': 20000.0,
 'Vadgaon Budruk': 11900.0,
 'Vadgaon Maval': 13666.666666666666,
 'Vadgaon Sheri': 11915.079365079366,
 'Vadgaonsheri': 11250.0,
 'Vaiduwadi': 13650.0,
 'Vallabh Nagar': 21857.14285714286,
 'Varale': 7500.0,
 'Veerbhadra Nagar': 26428.571428571428,
 'Venu Nagar Cotes': 19250.0,
 'Vidyanagar': 13625.0,
 'Vighnaharta Nagar': 8700.0,
 'Vijay Nagar': 13250.0,
 'Vikas Nagar': 12812.5,
 'Viman Nagar': 20581.419972721087,
 'Vinayak Nagar': 12400.0,
 'Vishal Nagar': 17451.612903225807,
 'Vishawshanti Colony': 18000.0,
 'Vishnu Dev Nagar': 19625.0,
 'Vishnupuram Colony': 12250.0,
 'Vishrantwadi': 15659.82142857143,
 'Vittalvadi': 14000.0,
 'Vitthal Nagar': 14000.0,
 'WAKAD': 10111.111111111111,
 'Wadachi Wadi': 11000.0,
 'Wadebolai': 15250.0,
 'Wadegaon': 13750.0,
 'Wadeshwar Nagar': 10000.0,
 'Wadgaon Budruk': 13925.0,
 'Wadgaon Sheri': 13094.174757281553,
 'Wadgaonsheri': 9875.0,
 'Wadki': 7833.333333333333,
 'Wadmukhwadi': 10333.333333333334,
 'Wageshwar Nagar': 11166.666666666666,
 'Wagholi': 12646.996870109546,
 'Wagholi  Wagholi': 6000.0,
 'Wakad': 18783.961239416498,
 'Wakad Annexe': 16000.0,
 'Wakadkar Wasti': 15250.0,
 'Wakdewadi': 30000.0,
 'Walhekarwadi': 8958.333333333334,
 'Walvekar Nagar': 18000.0,
 'Wanawari': 13000.0,
 'Wanowrie': 23341.954022988506,
 'Wanwadi': 20814.516129032258,
 'Warje': 13056.074766355141,
 'Warje Malwadi': 10928.57142857143,
 'Wireless Colony': 19605.0,
 'Yamuna Nagar': 11178.57142857143,
 'Yashoda Colony': 11000.0,
 'Yashwant nagar': 14750.0,
 'Yashwantrao Chavan Nagar': 6500.0,
 'Yerwada': 16815.78947368421,
 'Yewalewadi': 10648.756097560976,
 'aundh': 19250.0,
 'hadapsar': 9450.0,
 'karvenagar': 11500.0,
 'katraj': 11250.0,
 'keshav nagar': 11500.0,
 'mhatre bridge': 12000.0,
 'narhe': 10750.0,
 'paud road': 12500.0,
 'pimple gurav': 9500.0,
 'pune': 11750.0,
 'pune  NIBM': 19500.0,
 'wadgaon sheri': 12750.0,
 'wadgaonsheri': 16333.333333333334}


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
        #elif furnishing == 'Semifurnished':
            #furnishing = 'furnishing_Semifurnished'
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
       'powerbackup', 'pooja_room', 'study_room', 'servant_room', 'store_room',
       'brok_amt', 'deposit_amt', 'mnt_amt', 'address_num',
       'furnishing_Furnished', 'furnishing_Unfurnished', 'floor_type_Cement',
       'floor_type_Ceramic', 'floor_type_Concrete', 'floor_type_Granite',
       'floor_type_Marble', 'floor_type_Mosaic', 'floor_type_Not provided',
       'floor_type_Others', 'floor_type_Polished concrete',
       'floor_type_Spartex', 'floor_type_Vinyl', 'floor_type_Wood',
       'gate_community_No', 'wheelchairadption_None']
        lst = np.array(lst)
        address_number = area_mean[locality]
        fur_index = np.where(lst==furnishing)[0][0]
        floor_index = np.where(lst==floor_type)[0][0]
        x = np.zeros(30)
        x[0] = bhk
        x[1] = area
        x[2] = floor_number
        x[3] = parking
        x[4] = lightbill
        x[5] = powerbackup
        x[6] = pooja
        x[7] = study
        x[8] = servant
        x[9] = store
        x[10] = brokerage
        x[11] = deposit
        x[12] = maintainance
        x[13] = address_number
        x[28] = 0
        x[29] = 0

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
