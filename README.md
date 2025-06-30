# Apriori Algorithm Implementation

This project implements the Apriori algorithm to find frequent itemsets from a list of transactions, with constraints based on item prices.

## Files

- `homework4.py`: Main Python script that reads transactions and item prices, applies the Apriori algorithm, and returns results in the required dictionary format.
- `README.md`: This file.

## Functions

### `read_transactions(path)`
Reads a list of transactions from a file. Each line contains a transaction with item names.

### `read_prices(path)`
Reads item prices from a CSV file in the format: `item,price`.

### `get_frequent_1_itemsets(transactions, prices, s, k, m)`
Generates frequent 1-itemsets that satisfy minimum support (`s`), max total price (`k`), and minimum individual price (`m`).

### `generate_candidates(prev_frequent, size)`
Generates candidate itemsets of the given size from the previous frequent itemsets.

### `filter_candidates(candidates, transactions, prices, s, k, m)`
Filters candidate itemsets based on support count and price constraints.

### `apriori(transaction_filename, cost_filename, s, k, m)`
Main function that returns a dictionary containing:
- `c`: All candidate itemsets at each scan level.
- `f`: Frequent itemsets after filtering.

## Output Format

The output is a dictionary with the following structure:

```python
{
    1: {
        'c': {'A': 4, 'B': 5, ...},      # all candidate itemsets of size 1
        'f': {'A': 4, 'B': 5, ...}       # frequent 1-itemsets
    },
    2: {
        'c': {'AB': 3, 'AC': 2, ...},    # all candidate itemsets of size 2
        'f': {'AB': 3, ...}              # frequent 2-itemsets
    },
    ...
}
