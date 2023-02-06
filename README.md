# Sample Steam Reviews with GPT-2

[![Build status][build-image]][build]
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

Run the [`gpt_2_for_reviews.ipynb`][gpt_2_for_reviews] notebook on Google Colab, which relies on the [`gpt_2_simple`](https://github.com/minimaxir/gpt-2-simple) package.
[![Open In Colab][colab-badge]][gpt_2_for_reviews]

## Results

Examples of generated reviews for Artifact:

> I hate Artifact so I know it's not for me) but I'm fine with buying the game, the mechanics are very good and it gives me a lot of satisfaction. I don't mind the microtransaction at all. The only problem is I'm not interested in playing that much anymore (besides Hearthstone where I started) and the progression seems a bit too steep. That's not to say I'm not interested, it's just not possible to become a daily player with the casual and the draft modes combined. I'm very interested in playing the expert modes and doing constructed, if that's your thing I'd probably consider it.

> I hate Artifact, this game is literally pay 2 win and pay 2 lose. The only way to get new cards is to buy them at the shop. You cannot earn cards by playing the game. I am a computer player, I achieved a lot with computer games. I love the game. I played it a lot. I don't like it. Why? It's not fun. I'm not going to argue. The game is very simple, but I have spent a good amount of money on it, so it's not fun at all.

> I love Artifact, so I bought it. I can't talk about the monetization, there is no way to earn cards for free. I don't want to take the time to talk about the other aspects of the game, like what cards you can get, what sort of decks you can play, and how things like hero spawns work. Please don't buy this game, it's not worth it at the moment. I've made more money from phantom draft than I would buying packs in Hearthstone. The price of the game is too expensive for my taste. I can't refund it, it's not worth it.

> I love Artifact, I love its gameplay and I love its lore. But I also really love the monetization. I paid $15 and got Artifact for the first time, and it doesn't even cost that much to play competitively. I also got to actually buy cards that are worth more than the price of a pack, and it's not even gambling between packs! And there's the business model. You can buy cards, sell them, trade them. It's really quite cool. And the lore. It's really nice. I love the lore of Dota 2. It's deep and complex and I love it. But I love the fact that you can buy cards from other players. And the fact that you can trade them at will. The only way to get cards is by buying them. So this is the first TCG I've ever played (and a really good one at that), but Valve has really outdone them. They've really polished it up and I really like it. They have a free draft mode which is pretty cool. They have free tournaments which are really fun. They have free hero emote and they changed it from a very powerful card, so you can play them in the free modes which are really fun. 

Results obtained after 1000 steps using the 117M model:

-   [Artifact](https://github.com/woctezuma/sample-steam-reviews-with-gpt-2/wiki/Artifact)
-   [Slay the Spire](https://github.com/woctezuma/sample-steam-reviews-with-gpt-2/wiki/Slay_the_Spire)
-   [etc.](https://github.com/woctezuma/sample-steam-reviews-with-gpt-2/wiki/)

Results obtained after 1000 steps using the 345M model:

-   [Artifact](https://github.com/woctezuma/sample-steam-reviews-with-gpt-2/wiki/Artifact_345M)
-   [Crusader Kings II](https://github.com/woctezuma/sample-steam-reviews-with-gpt-2/wiki/Crusader_Kings_II_345M)

NB: Due to the large number of training steps (about 1000) with respect to the small number of reviews (about 100), the algorithm may copy real reviews.
To avoid this behavior, one could:
-   (recommended) increase the temperature (by default, 0.7),
-   train on a larger dataset of reviews, e.g. using all the English reviews,
-   decrease the number of training steps.

## References


-   [OpenAI, a blog post about GPT-2, 2019](https://openai.com/blog/better-language-models/)
-   [Max Woolf, API for GPT-2, 2019](https://github.com/minimaxir/gpt-2-simple)
-   [GPT-2 Neural Network Poetry, 2019](https://www.gwern.net/GPT-2)
-   OpenAI's GPT-2 as [a Steam curator](https://store.steampowered.com/curator/34944761-OpenAI%2527s-GPT-2/),
-   My repository to sample Steam store descriptions: [`sample-steam-descriptions`](https://github.com/woctezuma/sample-steam-descriptions)
-   My other repository to sample reviews for Steam games: [`sample-steam-reviews`](https://github.com/woctezuma/sample-steam-reviews)

[build]: <https://github.com/woctezuma/sample-steam-reviews-with-gpt-2/actions>
[build-image]: <https://github.com/woctezuma/sample-steam-reviews-with-gpt-2/workflows/Python package/badge.svg?branch=master>

[pyup]: <https://pyup.io/repos/github/woctezuma/sample-steam-reviews-with-gpt-2/>
[dependency-image]: <https://pyup.io/repos/github/woctezuma/sample-steam-reviews-with-gpt-2/shield.svg>
[python3-image]: <https://pyup.io/repos/github/woctezuma/sample-steam-reviews-with-gpt-2/python-3-shield.svg>

[codecov]: <https://codecov.io/gh/woctezuma/sample-steam-reviews-with-gpt-2>
[codecov-image]: <https://codecov.io/gh/woctezuma/sample-steam-reviews-with-gpt-2/branch/master/graph/badge.svg>

[codacy]: <https://www.codacy.com/app/woctezuma/sample-steam-reviews-with-gpt-2>
[codacy-image]: <https://api.codacy.com/project/badge/Grade/8c6fdc640e014bab91e5c87d5386b523>

[gpt_2_for_reviews]: <https://colab.research.google.com/github/woctezuma/sample-steam-reviews-with-gpt-2/blob/master/gpt_2_for_reviews.ipynb>

[colab-badge]: <https://colab.research.google.com/assets/colab-badge.svg>
