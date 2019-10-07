from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.cluster import cosine_distance
from string import punctuation
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import numpy as np


class TextRank:

    def __init__(self, text, n=10,lang='indonesian'):
        '''
        Penjelasan setiap variable:
        1.n = parameter jumlah kalimat yang di outputkan (<= sen_len)
        2.stop_words = menyimpan list kata yang merupakan stopwords
        3.tokenized_sent = menyimpan hasil tokenisasi text berupa kalimat
        4.similiarity_matrix = matrix dengan nilai kemiripan tiap kalimat pada corpus
        5.p = nilai dari hasil algoritma pagerank yang di gunakan untuk ranking output kalimat
        '''
        self.n = n
        self.stop_words = []
        self.tokenized_sent  = None
        self.similiarity_matrix = None
        self.p = None

        #run methods
        self.preprocessing(text, lang)
        self.build_sim_matrix()
        self.pagerank()


    def preprocessing(self, text, lang):
        '''
        melakukan tokenisasi text menjadi beberapa kata dan kalimat
        '''
        if lang == 'indonesian':
            self.stop_words = stopwords.words('indonesian') + list(punctuation)
        elif lang == 'english':
            self.stop_words = stopwords.words('english') + list(punctuation)
        self.tokenized_sent = list(set(sent_tokenize(text)))
    

    def sent_similiarity(self,sen1, sen2):
        '''
        fungsi ini digunakan untuk mengukur seberapa mirip kah 1 kalimat dengan kalimat yang lainnya.
        
        cara kerja:
        1. kalimat 1 dan kalimat 2 di pecah menjadi beberaka kata (tokenisasi) dan diubah menjadi lowercase 
           lalu dari hasil tokenisasi, kata-kata yang merupakan stopwords di hilangkan.
        2. kata-kata dari kalimat 1 dan 2 digabung menjadi satu
        3. bentuk sebuah vector untuk kalimat 1 dan 2
        4. ukur seberapa mirip nya kalimat 1 dan 2 menggunakan cosine similiarity (1 - cosine_distance)
        '''
        sen1 = [word.lower() for word in word_tokenize(sen1) if word.lower() not in self.stop_words or word.lower() not in sen1]
        sen2 = [word.lower() for word in word_tokenize(sen2) if word.lower() not in self.stop_words or word.lower() not in sen2]
        all_words = list(set(sen1+sen2))

        #build vector
        vect_1 = np.zeros(len(all_words))
        vect_2 = np.zeros(len(all_words))

        for word in sen1:
            vect_1[all_words.index(word)] += 1

        for word in sen2:
            vect_2[all_words.index(word)] += 1

        return 1 - cosine_distance(vect_1, vect_2)

    def build_sim_matrix(self):
        '''
        fungsi ini membentuk matrix 2d yg dimana value nya di isi dengan nilai cosine similiarity antar 2 kata
        '''
        #build 2d numpy-matrix with all zeroes
        length = len(self.tokenized_sent) 
        s = np.zeros((length, length))

        #fill the matrix with cosine similiarity value
        for i in range(length):
            for j in range(length):
                if i != j:
                    s[i][j] = self.sent_similiarity(self.tokenized_sent[i], self.tokenized_sent[j])


        #normailze matrix row wise
        np.seterr(divide='ignore', invalid='ignore')
        for i in range(len(s)):
            s[i] /= s[i].sum()

        #replace nan with 0
        s[np.isnan(s)] = 0
        
        self.similiarity_matrix = s

    def pagerank(self, eps=0.0001, d=0.85):
        '''
        pagerank merupakan fungsi IR(information retrival) scoring yang di kembangkan oleh google.
        algoritma textrank menggunakan fungsi pagerank untuk melakukan scoring terhadap setiap kata pada text
        '''
        #create a vector with length matrix sd
        length = len(self.similiarity_matrix)
        p = np.ones(length) / (length)

        #generate delta value which is lesser or equal to epsilon (convergence is assumed)
        while True:
            new_p = np.ones(length) * (1-d) / length + (d * self.similiarity_matrix.T.dot(p))
            delta = abs(new_p - p).sum()
            if delta <= eps : 
                self.p = new_p
                break
            p = new_p
    
    def summarize(self):
        '''
        pengambilan kalimat berdasarkan score pagerank
        '''
        temp = []
        result = []

        #sort index value based on pagerank score
        p1 = {value:index for index,value in enumerate(self.p)}
        p1 = sorted(p1.items(), key=lambda kv:kv[0],reverse=True)

        #append sentence based on n value
        if self.n > len(self.tokenized_sent): self.n = len(self.tokenized_sent)
        
        for i in range(self.n):
            temp.append(p1[i][1])
        temp.sort()

        for index in temp:
            result.append(self.tokenized_sent[index])
        
        return result
            



        


