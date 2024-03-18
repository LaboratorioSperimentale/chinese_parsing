import glob
from spacy_conll import init_parser


nlp = init_parser("zh_core_web_trf", "spacy", include_headers=True)

documents = glob.glob("input/*")

for document_name in documents:
	prefix = document_name.split("/")[-1].rsplit(".", 1)[0]

	document = open(f"{document_name}", encoding="utf-8").read()
	doc2 = nlp(document)


	with open(f"output/{prefix}.conllu", "w", encoding="utf-8") as fout:
		conll = doc2._.conll_str
		print(conll, file=fout)