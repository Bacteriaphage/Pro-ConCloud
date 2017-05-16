# Pro-ConCloud
## Introduction
This is a light-weight project. It can crawler the comments for a specific product from amazon.com and analyze the key words they provides. After that the program can work out a key word cloud for both advantages and drawback for this product.
The project is seperate in 3 parts:
1. save HTML to local
2. extract key information from raw HTML
3. match word and do analysis
4. draw a word cloud or display statistics

special thanks to Amueller for the  awesome word cloud package

*The input URL should be the comment page for one product at amazon.com*

## Manual

PCcloud.py 1.0 (2017 March 29 9:28PM)

usage: [sudo] python filename [argument]

Arguments:

    --                No argument(only grap web page and waiting).
    -p                Give average point for a product.
    -d -p             Draw a word cloud for all positive words.
    -d -n             Draw a word cloud for all negative words.
    -d -b             Draw a word cloud for both pos and neg words.
    -d -a             Draw a word cloud for any word appeared in comment.
    --help            Show help page.

No argument:

    <Enter>           Show all instruction.
    draw              Start drawing word cloud.
    avgStar           Show the average star of one product.
    exit              Exit program.

Draw:

    <Enter>           Show all drawing option.
    positive          Draw a word cloud for all positive words.
    negative          Draw a word cloud for all negative words.
    both              Draw a word cloud for both pos and neg words.
    all               Draw a word cloud for all words appeared in comment.
    exit              Exit drawing.
