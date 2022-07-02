# -*- coding: utf-8 -*-
"""
Twint - collecting corpora in alsatian.

This script allows to collect tweet in alsatian with the help of twint
See here: https://github.com/twintproject/twint

Autor: Audrey Deck
Created: 03-2021
"""

import twint

# Configure
c = twint.Config()
c.Username = "bleuelsass"
c.Limit = 1000
c.Store_csv = True
c.Output = "tweet_FBA.csv"

# Run
twint.run.Search(c)
