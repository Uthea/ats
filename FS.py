from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from string import punctuation
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from nltk.stem import PorterStemmer
from operator import itemgetter

class FrequencySummary:

    def __init__(self,text, n=10, lang='indonesian'):
        '''
        Penjelasan setiap variable:
        1.stop_words = menyimpan list kata yang merupakan stopwords
        2.text = menyimpan corpus yang ingin di ringkas
        3.words = hasil tokenisasi corpus berupa kata
        4.freq_count = hasil perhitungan frekuensi kemunculan tiap kata
        5.stemmer = jenis stemmer yang digunakan
        6.sentences = menyimpan index kalimat berserta scorenya
        7.token_sen = menyimpan hasil tokenisasi text berupa kalimat
        8.index = menyimpan index setiap kalimat dan scorenya dalam bentuk tuple (untuk proses fungsi terakhir)
        9.sen_len = jumlah kalimat yang tetokenisasi
        10.n = parameter jumlah kalimat yang di outputkan (<= sen_len)
        '''
        self.stop_words = []
        self.text = text
        self.words = None
        self.freq_count = {}
        self.stemmer = None
        self.sentences = {}
        self.token_sen = []
        self.index = ()
        self.sen_len = len(sent_tokenize(self.text))
        self.n = n

        #run methods
        self.set_language(lang)
        self.preprocessing()
        self.count_frequency()
        self.sentence_scoring()
    
    def set_language(self, lang):
        '''
        konfigurasi stopwords dan stemmer yang digunakan sesuai bahasa yang dipilih
        lang = indonesian atau english
        '''
        if lang == 'indonesian':
            self.stop_words = stopwords.words('indonesian') + list(punctuation)
            self.stemmer = StemmerFactory().create_stemmer()
        elif lang == 'english':
            self.stop_words = stopwords.words('english') + list(punctuation)
            self.stemmer = PorterStemmer()
    
    def preprocessing(self):
        '''
        melakukan tokenisasi text menjadi beberapa kata dan kalimat serta menghapus stopwords dari list kata
        yang tertokenisasi
        '''
        rwords = word_tokenize(self.text)
        self.words = [self.stemmer.stem(word.lower()) for word in rwords if word.lower() not in self.stop_words]
        self.token_sen = sent_tokenize(self.text)

    def count_frequency(self):
        '''
        menghitung frekuensi setiap kata yang ada di dalam text yang telah tertokenisasi 
        (tahap ini membentuk dictionary dengan key sebagai kata yang telah di stemming 
        dan value sebagai jumlah frekuensi)
        '''
        for word in self.words:
            if word not in self.freq_count:
                self.freq_count[word] = 1
            else : self.freq_count[word] +=1
    
    def sentence_scoring(self):
        '''
        melakukan penilaian terhadap setiap kalimat tertokenisasi yang ada di dalam text
        (nilai frekuensi sebuah kata yang ada di dalam suatu kalimat ditotalkan)
        '''
        for position,sentence in enumerate(self.token_sen):
            words = word_tokenize(sentence)
            score = 0
            for word in words:
                stem = self.stemmer.stem(word.lower()) 
                if stem in self.freq_count:
                    score += self.freq_count[stem]
            self.sentences[position] = score
        self.index = sorted(self.sentences.items(), key=itemgetter(1),reverse=True)
    
    def summarize(self):
        '''
        melakukan summarization berdasarkan nilai setiap kalimat.
        proses ini bekerja dengan mengambil kalimat yang memiliki nilai tertinggi
        (jumlah kalimat yang di ambil tergantung parameter n).
        lalu kalimat yang telah dipilih akan di sort berdasarkan urutan index kemunculan pada text aslinya (ascending)
        '''
        #open('output.txt', 'w')
        output = []
        if self.n > self.sen_len : self.n = self.sen_len
        lst = sorted([index[0] for index in self.index[:self.n]])
        for index in lst:
            output.append(self.token_sen[index])
        return output


