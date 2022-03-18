# Nerdle

The goal of this project is to find the ideal starter word for Wordle.

## Executive Summary

If you care more about finding green letters, the following list of words are your best bet:

| Word | Probability of Green Letter | Probability of Green or Yellow Letter |
|------|-----------------------------|--------------------------|
| sores | 0.618135 | 0.883448 |
| sanes | 0.617363 | 0.906310 |
| sones | 0.614891 | 0.879663 |
| sales | 0.610952 | 0.903375 |
| seres | 0.609485 | 0.807214 |

Removing words with duplicate letters, the list changes to the following:

| Word | Probability of Green Letter | Probability of Green or Yellow Letter |
|------|-----------------------------|--------------------------|
| cares | 0.590793 | 0.930795 |
| bares | 0.589480 | 0.922299 |
| pares | 0.587086 | 0.925156 |
| canes | 0.583842 | 0.930100 |
| bores | 0.583687 | 0.899204 |

If you care more about getting at least one green **or** yellow letter, the best words are the following:

| Word | Probability of Green Letter | Probability of Green or Yellow Letter |
|------|-----------------------------|--------------------------|
| toeas | 0.530161 | 0.957287 |
| stoae | 0.344327 | 0.957287 |
| aloes | 0.536958 | 0.956901 |
| aeons | 0.513401 | 0.956438 |
| aeros | 0.507067 | 0.955665 |
