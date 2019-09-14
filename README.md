# Political Synthesis

- Synthesizing political information on certain elections so that people can see policy → voter turnout
- https://ssir.org/articles/entry/increasing_voter_turnout_what_if_anything_can_be_done
    - how do you make it easy to access this thing?
        - website
    - how to implement:
        - based on area (to determine local candidates etc.)
            - how do you automate finding which candidates are running in a certain election
            - probably some database out there 
            - FEC:
                - https://api.open.fec.gov/developers/
        - search by candidate, by election → when, where HOW to vote for it
        - synthesizing policy from news articles, speeches, social media
            - identifying policy statements / positions / important content
                - TF-IDF
            - summarizing / making into an actual sentence?
                - Sentence Embedding
            - Different types of summarization:
                - Abstractive
                    - paraphrasing
                    - can condense a language much better, but needs natural language generation
                    - https://arxiv.org/abs/1812.02303
                        - seq2seq models
                        - https://google.github.io/seq2seq/
                            - This one is built for machine translation
                            - can be used for text summarization as well
                        - http://opennmt.net/
                            - http://opennmt.net/Models-py/#summarization
                - Extractive
                    - extracts objects without modifying them

## Topics
- Abortion
- Affirmative Action
- Budget/Taxation
- Climate Change / Environment
- Criminal Justice
- Campaign Finance / Reform
- Death Penalty
- Defense
- Drugs
- Education
- Financial Regulation
- Foreign Policy
    - Russia
    - NK
    - China
    - Saudi Arabia
- Guns
- Gender Equality 
- Healthcare
- Immigration
- Marriage Equality
- Military Personnel
- Sexual Orientation + Gender Identity
- Religion
- Renewable Energy


