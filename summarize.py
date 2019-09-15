"""
Summary should be a list of the abstracted summaries corresponding to the topic at keyword at thesame index.
""" 
import json
summary_file_path = "/summaries/"
from prepro import data_builder
import torch
from pytorch_transformers import BertTokenizer

import distributed
from PreSumm.models import data_loader, model_builder
from PreSumm.models.data_loader import load_dataset
from PreSumm.models.loss import abs_loss
from PreSumm.models.model_builder import AbsSummarizer
from PreSumm.models.predictor import build_predictor
from PreSumm.models.trainer import build_trainer

def preprocess(text):
	data_builder.tokenize(text)
	data_builder.format_xsum_to_lines(text)
	data_builder.format_to_bert(text)
	return text

checkpoint = ""

def summarize(text):
	model = AbsSummarizer(args, device, checkpoint)
    model.eval()

    test_iter = data_loader.Dataloader(args, load_dataset(args, 'test', shuffle=False),
                                       args.test_batch_size, device,
                                       shuffle=False, is_test=True)
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased', do_lower_case=True, cache_dir=args.temp_dir)
    symbols = {'BOS': tokenizer.vocab['[unused0]'], 'EOS': tokenizer.vocab['[unused1]'],
               'PAD': tokenizer.vocab['[PAD]'], 'EOQ': tokenizer.vocab['[unused2]']}
    predictor = build_predictor(args, tokenizer, symbols, model, logger)
    predictor.translate(test_iter, step)

def write_to_json(keywords, summary, candidate_name):
	data = {}
	for keyword in keywords:
		data[keyword] = summary
	with open(summary_file_path + candidate_name + '.json') as fp:
		json.dump(data, fp)
