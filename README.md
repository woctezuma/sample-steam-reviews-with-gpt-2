# Sample Steam Reviews with GPT-2

[![Build status][build-image]][build]
[![Updates][dependency-image]][pyup]
[![Python 3][python3-image]][pyup]
[![Code coverage][codecov-image]][codecov]
[![Code Quality][codacy-image]][codacy]

This repository contains Python code to sample Steam reviews, with the GPT-2 language model.

![Generated review, using GPT-2](https://github.com/woctezuma/sample-steam-reviews-with-gpt-2/wiki/img/cover.png)

## Requirements

-   Install the latest version of [Python 3.X](https://www.python.org/downloads/).
-   Install the required packages:

```bash
pip install -r requirements.txt
```

## Usage

### Concatenate Steam reviews in a large text file

The following code allows to download and concatenate in a large text file:
-   recent reviews (less than 28 days old),
-   written in English (as declared on Steam, and then checked with an external tool),
-   and consisting of at least 150 characters.

For a given `appID = app_id_number`, run:

```
python export_review_data.py app_id_number
```

For instance, to download reviews for [*Artifact*](https://store.steampowered.com/app/583950/Artifact/), whose `appID` is `583950`, run:

```
python export_review_data.py 583950
```

A data snapshot is available in [`data/`](data/).

### Fine-tune a pre-trained GPT-2 model

Run the [`gpt_2_for_reviews.ipynb`](gpt_2_for_reviews.ipynb) notebook on Google Colab, which relies on the [`gpt_2_simple`](https://github.com/minimaxir/gpt-2-simple) package.

## Results

Seed:
```
```

Generated samples:
```
TODO
```

## References


-   [OpenAI, a blog post about GPT-2, 2019](https://openai.com/blog/better-language-models/)
-   [Max Woolf, API for GPT-2, 2019](https://github.com/minimaxir/gpt-2-simple)
-   My repository to sample Steam store descriptions: [`sample-steam-descriptions`](https://github.com/woctezuma/sample-steam-descriptions)
-   My other repository to sample reviews for Steam games: [`sample-steam-reviews`](https://github.com/woctezuma/sample-steam-reviews)

[build]: <https://travis-ci.org/woctezuma/sample-steam-reviews-with-gpt-2>
[build-image]: <https://travis-ci.org/woctezuma/sample-steam-reviews-with-gpt-2.svg?branch=master>

[pyup]: <https://pyup.io/repos/github/woctezuma/sample-steam-reviews-with-gpt-2/>
[dependency-image]: <https://pyup.io/repos/github/woctezuma/sample-steam-reviews-with-gpt-2/shield.svg>
[python3-image]: <https://pyup.io/repos/github/woctezuma/sample-steam-reviews-with-gpt-2/python-3-shield.svg>

[codecov]: <https://codecov.io/gh/woctezuma/sample-steam-reviews-with-gpt-2>
[codecov-image]: <https://codecov.io/gh/woctezuma/sample-steam-reviews-with-gpt-2/branch/master/graph/badge.svg>

[codacy]: <https://www.codacy.com/app/woctezuma/sample-steam-reviews-with-gpt-2>
[codacy-image]: <https://api.codacy.com/project/badge/Grade/8c6fdc640e014bab91e5c87d5386b523>
