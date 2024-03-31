from mrjob.job import MRJob
from collections import defaultdict
from mrjob.step import MRStep
import csv

class MRCombinedCSVProcessor(MRJob):
    vocab = set()
    saved_vocab=set()
    whole_file = defaultdict(int)
    whole_tf=[]
    whole_tf_idf=[]
    whole_idf=[]

    def mapper_first(self, _, lines):
        # Initialize an empty dictionary
        csv_dict = {}

        # Read each line of the CSV file
        for line in lines.split('\n'):
            try:
                # Parse the CSV line
                columns = line.split(',')
                key = columns[0]
                value = columns[1]
                csv_dict[key] = value
                self.whole_file[key] = value
            except Exception as e:
                # Skip lines with errors
                pass

        # Yield the entire dictionary
        yield None, csv_dict

    def reducer_first(self, _, csv_dicts):
        # Initialize a vocabulary set to store unique words
        vocab_set = set()

        # Iterate over dictionaries to update the vocabulary set
        for csv_dict in csv_dicts:
            for value in csv_dict.values():
                words = value.split()
                vocab_set.update(words)

        # Sort the vocabulary set
        self.vocab = sorted(vocab_set)

        word_index_dict = defaultdict(int)
        
        for index, word in enumerate(self.vocab):
            word_index_dict[index] = word

        whole_word=self.vocab
        self.saved_vocab=whole_word
        yield None, whole_word


    def mapper_tf(self, _,whole_word):
        for key,value in self.whole_file.items():
            words=value.split()
            local_tf = [0] * len(whole_word)
            for index in range(len(whole_word)):
                first_word=whole_word[index]
                local_tf[index] = words.count(first_word)
            self.whole_tf.append(local_tf)
            yield None,whole_word

  
    
    def mapper_idf(self, _, whole):
        docs=[]
        self.saved_vocab=whole
        for key,value in self.whole_file.items():
            docs.append(value)
        idf = [0] * len(whole)
        for index, word in enumerate(whole):
            idf[index] = sum([1 for doc in docs if word in doc])
        yield idf,self.saved_vocab

    def reducer_tf_idf(self,Idf,whole):
        full_tf=self.whole_tf
        whole_tfidf=full_tf
        self.whole_idf=Idf
        #self.saved_vocab=whole
        for i,doc in enumerate(full_tf):
            for j in range(len(doc)):
              whole_tfidf[i][j]=full_tf[i][j]/Idf[i]
        self.whole_tf_idf=whole_tfidf
        yield Idf,whole_tfidf

         
   
    def mapper_query(self,idf,tfidf):
        with open('/home/sahil/Documents/Search_Engine/query.txt', 'r') as f:
            query = f.readline().strip()


        vocab_set=set()

        for key,value in self.whole_file.items():
            words=value.split()
            vocab_set.update(words)

        self.vocab = sorted(vocab_set)

        query_tf = [0] * len(self.vocab)
        for index in range(len(self.vocab)):
            first_word=self.vocab[index]
            query_tf[index] = query.count(first_word)

        for index,i in enumerate(query_tf):
            query_tf[index]=query_tf[index]/idf[index]
            value=query_tf[index]

        Rank=[0] * len(tfidf)
        for index,i in enumerate(Rank):
            total = sum(float(x) * float(y) for x, y in zip(query_tf, tfidf[index]))
            Rank[index]=total
        sorted_indices = sorted(range(len(Rank)), key=lambda i: Rank[i], reverse=True)
        sorted_list = [Rank[i] for i in sorted_indices]

        # Print the sorted list and corresponding indices
        yield sorted_list,sorted_indices


    def reducer_query(self,sorted_list,sorted_indices):
        yield sorted_list,sorted_indices


    def steps(self):
        return [
            MRStep(mapper=self.mapper_first, reducer=self.reducer_first),
            MRStep(mapper=self.mapper_tf),
            MRStep(mapper=self.mapper_idf),
            MRStep(reducer=self.reducer_tf_idf),
            MRStep(mapper=self.mapper_query)
        ]
    

if __name__ == '__main__':
    MRCombinedCSVProcessor.run()
