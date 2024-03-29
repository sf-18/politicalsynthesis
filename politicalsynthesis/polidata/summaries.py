#!/usr/bin/python3

import os, sys
import nltk
import glob
import string
import random

from .search_topics import get_candidate_content

class SumBasic(object):

	def __init__(self, method, text_files):
		self.method = method
		self.text_files = text_files
		self.full_text_str = ""
		self.pre_text = []
		self.stopwords='''i
me
my
myself
we
our
ours
ourselves
you
your
yours
yourself
yourselves
he
him
his
himself
she
her
hers
herself
it
its
itself
they
them
their
theirs
themselves
what
which
who
whom
this
that
these
those
am
is
are
was
were
be
been
being
have
has
had
having
do
does
did
doing
a
an
the
and
but
if
or
because
as
until
while
of
at
by
for
with
about
against
between
into
through
during
before
after
above
below
to
from
up
down
in
out
on
off
over
under
again
further
then
once
here
there
when
where
why
how
all
any
both
each
few
more
most
other
some
such
no
nor
not
only
own
same
so
than
too
very
s
t
can
will
just
don
should
now'''

	def import_docs(self):
		for tf in self.text_files:
			self.full_text_str += tf
			self.full_text_str += " "

	def preprocess(self):
		self.full_text_str = self.full_text_str.replace('\n','')
		sentences = self.full_text_str.split('.')
		sentences_no_punc = [''.join(c for c in s if c not in string.punctuation) for s in sentences]

		# When adding the sentences back to create the summary, add a '. ' to 
		# make it look smooth again
		#for i in range(len(sentences_no_punc)):
		#	sentences_no_punc[i] = sentences_no_punc[i].strip() 

		self.pre_text = sentences_no_punc

	def freq_dist(self):
		# Map words (converted to lowercase) that aren't stop words to their
		# probability of occurring in the whole text.		
		word_freqs = {}
		for sen in self.pre_text:
			tokens = sen.split()
			for t in tokens:
				if any(char.isalpha() or char.isdigit() for char in t):
					if t.lower() not in self.stopwords:
						if t.lower() in word_freqs:
							word_freqs[t.lower()] += 1
						else:
							word_freqs[t.lower()] = 1
		count = sum(word_freqs.values())
		word_freqs.update({k: float(word_freqs[k]/count)  for k in word_freqs.keys()})
		return word_freqs

	def assign_weights(self, freq_dist):
		# Map index of sentence in list of sentences (already preprocessed)
		# to weight of that sentence.
		weights = {}
		for i in range(len(self.pre_text)):
			count = 0
			prob = 0
			tokens = self.pre_text[i].split()
			for t in tokens:
				if t.lower() in freq_dist:
					count += 1
					prob += freq_dist[t.lower()]
			if count != 0: weights[i] = float(prob / count)
		return weights

	def orig(self):
		fd = self.freq_dist()
		
		summary = ""
		while len(summary.split()) < 100:
			weights = self.assign_weights(fd)
			sorted_weights = sorted(weights.items(), key=lambda x: x[1], reverse=True)
			highest_prob_word = max(fd, key=fd.get)
			for i in range(len(sorted_weights)):
				weighted_sentence = self.pre_text[sorted_weights[i][0]]
				if highest_prob_word in weighted_sentence.lower():
					summary += weighted_sentence 
					summary += ". "
					break

			for word in weighted_sentence.split():
				if word.lower() in fd.keys():
					fd[word.lower()] *= fd[word.lower()]

		return summary

	def best_avg(self):
		fd = self.freq_dist()
    
		summary = ""
		while len(summary.split()) < 100:
			weights = self.assign_weights(fd)
			sorted_weights = sorted(weights.items(), key=lambda x: x[1], reverse=True)
			i = 0
			weighted_sentence = self.pre_text[sorted_weights[i][0]]                      
			while weighted_sentence in summary:
				weighted_sentence = self.pre_text[sorted_weights[i][0]]
				i+=1
			summary += weighted_sentence 
			summary += ". "

			for word in weighted_sentence.split():
				if word.lower() in fd.keys():
					fd[word.lower()] *= fd[word.lower()]

		return summary

	def simplified(self):
		fd = self.freq_dist()

		summary = ""
		while len(summary.split()) < 100:
			weights = self.assign_weights(fd)
			sorted_weights = sorted(weights.items(), key=lambda x: x[1], reverse=True)
			highest_prob_word = max(fd, key=fd.get)
			for i in range(len(sorted_weights)):
				weighted_sentence = self.pre_text[sorted_weights[i][0]]
				if highest_prob_word in weighted_sentence.lower():
					if weighted_sentence not in summary:
						summary += weighted_sentence 
						summary += ". "
						break

		return summary


	def leading(self):
		summary = ""
		i = 0
		while len(summary.split()) < 100:
			summary += self.pre_text[i]
			summary += ". "
			i += 1

		return summary

def get_candidate_topic_summary(candidate, topic):
	text = get_candidate_content(candidate, topic)
	sb = SumBasic("simplified", text)
	sb.import_docs()
	sb.preprocess()
	weights = sb.assign_weights(sb.freq_dist())
	return sb.simplified()