# import math
# from collections import defaultdict

# def clean_words(m):
#     m = m.replace('\n', ' ')
#     m = m.replace('.', ' ')
#     m = m.replace('  ', ' ')
#     m = m.lower()
#     return m

# def nice_print2Ddict(d):
#     dkeys = list(d.keys())
#     dkeys.sort()

#     for k in dkeys:
#         print('\n', k)
#         d2 = d[k]
#         k2s = list(d2.keys())
#         k2s.sort()
#         print('*', end=' ')
#         for k2 in k2s:
#             print("{}:{:.3f}".format(k2, d2[k2]), end='; ')
#     print()

# def culture_tf_idf(culture_list):
#     # Initialize dictionaries
#     Ftd = defaultdict(lambda: defaultdict(int))  # term frequency in document
#     Nt = defaultdict(int)  # number of documents containing term
    
#     # Read documents and compute term frequencies
#     for doc in culture_list:
#         with open(doc, 'r') as f:
#             header = f.readline().strip()
#             content = f.read()
#             content = clean_words(content)
#             words = content.split()
#             total_words = len(words)
            
#             # Compute term frequency for this document
#             term_freq = defaultdict(int)
#             for word in words:
#                 term_freq[word] += 1
            
#             # Update Ftd and Nt
#             for word, count in term_freq.items():
#                 Ftd[doc][word] = count
#                 Nt[word] += 1
    
#     # Total number of documents
#     N = len(culture_list)
    
#     # Compute TF-IDF
#     TF_IDF = {}
#     for doc, term_freq in Ftd.items():
#         tfidf = {}
#         total_terms = sum(term_freq.values())
#         for term, count in term_freq.items():
#             tf = count / total_terms
#             idf = math.log(N / (1 + Nt[term]), 10)
#             tfidf[term] = tf * idf
#         TF_IDF[doc] = tfidf
    
#     return TF_IDF

# if __name__ == '__main__': 
#  cultures = ['chinese.txt', 'thai.txt', 'japanese.txt', 'western.txt']
#  res = culture_tf_idf(cultures) 
#  nice_print2Ddict(res)
import math

def clean_words(m):
    m = m.replace('\n', ' ')
    m = m.replace('.', ' ')
    m = m.replace('  ', ' ')
    m = m.lower()
    return m

def culture_tf_idf(culture_list):
    ####################################################
    # Find f[t,d] ~ as a dictionary of dictionaries
    ####################################################
    Ftd = {}

    for c in culture_list:
        d = {}

        with open(c, 'r') as f:
            header = f.readline()
            msg = f.read()

            if header[-1] == '\n':
                header = header[:-1]

            msg = clean_words(msg)

            words = msg.split()
            for t in words:
                if t in d:
                    d[t] += 1
                else:
                    d[t] = 1

            Ftd[c] = d

    ########################################################
    # Compute IDF
    ########################################################
    N = len(Ftd)  # number of documents
    Nt = {}
    for d in Ftd:
        term_freq = Ftd[d]
        for t in term_freq:
            if t in Nt:
                Nt[t] += 1
            else:
                Nt[t] = 1

    ########################################################
    # Compute TF-IDF
    ########################################################
    TF_IDF = {}
    for d in Ftd:
        term_freq = Ftd[d]
        sum_all_ftd = sum(term_freq.values())

        tfidf_ = {}
        for t in term_freq:
            tf = term_freq[t] / sum_all_ftd
            idf = math.log(N / (1 + Nt[t]))
            tfidf_[t] = tf * idf

        TF_IDF[d] = tfidf_

    return TF_IDF

def nice_print2Ddict(d):
    dkeys = list(d.keys())
    dkeys.sort()

    for k in dkeys:
        print('\n', k)

        d2 = d[k]
        k2s = list(d2.keys())
        k2s.sort()

        print('*', end=' ')
        for k2 in k2s:
            print("{}:{:.3f}".format(k2, d2[k2]), end='; ')

    print()

if __name__ == '__main__':
    cultures = ['chinese.txt',
                'thai.txt',
                'japanese.txt']

    res = culture_tf_idf(cultures)
    nice_print2Ddict(res)
