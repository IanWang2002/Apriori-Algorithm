from collections import defaultdict
from itertools import combinations

def read_transactions(path):
    with open(path, 'r') as f:
        return [sorted(list(line.strip())) for line in f if line.strip()]

def read_prices(path):
    price_dict = {}
    with open(path, 'r') as f:
        for line in f:
            parts = line.strip().split(',')
            if len(parts) != 2:
                continue  # Skip bad lines
            item, price = parts
            price_dict[item] = int(price)
    return price_dict

def get_frequent_1_itemsets(transactions, prices, s, k, m):
    count = defaultdict(int)
    for transaction in transactions:
        for item in transaction:
            count[item] += 1

    cand_dict = dict(count)
    freq = {}
    for item, support in count.items():
        item_price = prices[item]
        if support >= s and item_price <= k and item_price >= m:
            freq[item] = support

    return cand_dict, freq

def generate_candidates(prev_frequent, size):
    items = sorted(prev_frequent)
    candidates = set()
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            union = sorted(set(items[i]) | set(items[j]))
            if len(union) == size:
                if all(''.join(sorted(sub)) in prev_frequent for sub in combinations(union, size - 1)):
                    candidates.add(''.join(union))
    return sorted(candidates)

def filter_candidates(candidates, transactions, prices, s, k, m):
    count = defaultdict(int)
    for t in transactions:
        t_set = set(t)
        for cand in candidates:
            if set(cand).issubset(t_set):
                count[cand] += 1

    frequent = {}
    for cand, support in count.items():
        item_prices = [prices[i] for i in cand]
        if support >= s and sum(item_prices) <= k and min(item_prices) >= m:
            frequent[cand] = support
    return count, frequent

def apriori(transaction_filename, cost_filename, s, k, m):
    apriori_result = {}
    transactions = read_transactions(transaction_filename)
    prices = read_prices(cost_filename)

    scan = 1
    cand_dict, freq_itemsets = get_frequent_1_itemsets(transactions, prices, s, k, m)
    apriori_result[scan] = {
        'c': dict(sorted(cand_dict.items())),
        'f': dict(sorted(freq_itemsets.items()))
    }

    while True:
        scan += 1
        candidates = generate_candidates(freq_itemsets, scan)
        if not candidates:
            break

        cand_dict, freq_dict = filter_candidates(candidates, transactions, prices, s, k, m)
        apriori_result[scan] = {
            'c': dict(sorted(cand_dict.items())),
            'f': dict(sorted(freq_dict.items()))
        }

        if len(freq_dict) <= 1:
            break

        freq_itemsets = freq_dict

    return apriori_result
