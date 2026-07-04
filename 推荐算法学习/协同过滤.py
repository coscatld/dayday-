import math
import numpy as np
from pydantic_core.core_schema import none_schema



class CosineSimilarity:
    def __call__(self,a,b):
        dot = sum(x * y for x, y in zip(a,b))
        norm_a = math.sqrt(sum(x * x for x in a))
        norm_b = math.sqrt(sum(y * y for y in b))
        if norm_a == 0 or norm_b == 0:
            return 0
        return dot / (norm_a * norm_b)

class PearsonCorrelation:
    def __call__(self,a,b):
        a_avg = self.Average(a)
        b_avg = self.Average(b)
        p = q = l = 0
        for i in range(0,len(a)):
            p+= (a[i]-a_avg)*(b[i]-b_avg)
            q+=(a[i]-a_avg)**2
            l+=(b[i]-b_avg)**2
        return p/(math.sqrt(q)*math.sqrt(l))
    def Average(self,n:list):
        return sum(n) / len(n)

class UserCF:
    def __init__(self, ratings, similarity_method="cosine"):
        self.ratings = ratings

        if similarity_method == "cosine":
            self.similarity = CosineSimilarity()
        elif similarity_method == "pearson":
            self.similarity = PearsonCorrelation()
        else:
            raise ValueError("similarity_method 只能是 'cosine' 或 'pearson'")

    def get_common_rating_vectors(self, user1, user2):
        items1 = self.ratings[user1]
        items2 = self.ratings[user2]

        common_items = set(items1.keys()) & set(items2.keys())

        if len(common_items) == 0:
            return [], []

        vector1 = []
        vector2 = []

        for item in common_items:
            vector1.append(items1[item])
            vector2.append(items2[item])

        return vector1, vector2

    def user_similarity(self, user1, user2):
        vector1, vector2 = self.get_common_rating_vectors(user1, user2)

        if len(vector1) == 0:
            return 0

        return self.similarity(vector1, vector2)

    def recommend(self, target_user, top_k_users=2, top_n_items=3):
        user_similarities = []

        for other_user in self.ratings:
            if other_user == target_user:
                continue

            sim = self.user_similarity(target_user, other_user)

            if sim > 0:
                user_similarities.append((other_user, sim))

        user_similarities.sort(key=lambda x: x[1], reverse=True)

        nearest_users = user_similarities[:top_k_users]

        target_items = set(self.ratings[target_user].keys())
        scores = {}

        for user, sim in nearest_users:
            for item, rating in self.ratings[user].items():
                if item in target_items:
                    continue

                if item not in scores:
                    scores[item] = 0

                scores[item] += sim * rating

        result = sorted(scores.items(), key=lambda x: x[1], reverse=True)

        return result[:top_n_items]


ratings = {
    "u1": {"i1": 5, "i2": 3, "i3": 4},
    "u2": {"i1": 4, "i2": 2, "i4": 5},
    "u3": {"i2": 5, "i3": 4, "i4": 4},
    "u4": {"i1": 2, "i3": 5, "i4": 3}
}


model = UserCF(ratings, similarity_method="cosine")

print(model.user_similarity("u1", "u2"))
print(model.recommend("u1"))