def precision_recall_at_k(recommended, relevant, k):
    hits = []
    top_k = recommended[:k]
    for i in set(relevant):
        if i in top_k:
            hits.append(i)

    precision_k = len(hits)/k
    recall_k = len(hits)/len(relevant)

    return[precision_k,recall_k]