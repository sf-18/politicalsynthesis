from src.presumm.src.prepro import data_builder
from pytorch_transformers import BertTokenizer
from src.presumm.models import data_loader, model_builder
from src.presumm.models.data_loader import load_dataset
from src.presumm.models.loss import abs_loss
from src.presumm.models.model_builder import AbsSummarizer
from src.presumm.models.predictor import build_predictor
from src.presumm.models.trainer import build_trainer

import json
import src.presumm.src.distributed
import torch

summary_file_path = "/summaries/"

def preprocess(text):
	data_builder.tokenize(text)
	data_builder.format_xsum_to_lines(text)
	data_builder.format_to_bert(text)
	return text

checkpoint = "model/model_step_148000.pt"

def summarize(text):
	model = AbsSummarizer(args, device, checkpoint)
	model.eval()

	test_iter = data_loader.Dataloader(preprocess(text), 500, 'cpu', shuffle=False, is_test=True)
	tokenizer = BertTokenizer.from_pretrained('bert-base-uncased', do_lower_case=False)
	symbols = {'BOS': tokenizer.vocab['[unused0]'], 'EOS': tokenizer.vocab['[unused1]'],
	           'PAD': tokenizer.vocab['[PAD]'], 'EOQ': tokenizer.vocab['[unused2]']}
	predictor = build_predictor(tokenizer, symbols)
	predictor.translate(test_iter, step)

def write_to_json(keywords, summary, candidate_name):
	data = {}
	for keyword in keywords:
		data[keyword] = summary
	with open(summary_file_path + candidate_name + '.json') as fp:
		json.dump(data, fp)
