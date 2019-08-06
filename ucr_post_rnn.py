import sys
import argparse
import tensorflow as tf
from tensorflow import keras
from textgenrnn import textgenrnn

def main():
        config = tf.ConfigProto(
            gpu_options=tf.GPUOptions(per_process_gpu_memory_fraction=0.8)
        )

        config.gpu_options.allow_growth = True
        session = tf.Session(config=config)

        run_rnn(_initArguments())


def run_rnn(args):
	destination_path = r'\r_ucr_learned_titles.txt'

	output_mode = 'a'
	new_model_flag = False
	num_total_epochs = 5

	if args.mode != None:
			print(">> Using overwrite mode 'w+'")
			output_mode = 'w+'
	if args.new != None:
			print(">> Training from new model")
			new_model_flag = True

	if args.iter != None:
			print(">> Number of epochs:", args.iter)
			num_total_epochs = args.iter

	textgen = textgenrnn(name="ucr_post_titles")


	for x in range(num_total_epochs):
		print("GENERATION " + str(x))

		if x == 0:
			newModel = new_model_flag
		else:
			newModel = False

		textgen.train_from_largetext_file(r'\r_ucr_post_titles.txt',
										num_epochs=1,
										new_model=newModel,
										batch_size=256,
										word_level=True,
										rnn_bidirectional=True,
										train_size=0.9,
										max_gen_length=150,
										max_length=50,
										dropout=0.95,
										gen_epochs=3)

		# if ((5 % (x+1)) == 0):
		# 	textgen.generate_samples(n=4, temperatures=[1.2])

		texts = textgen.generate(return_as_list=True, n=3)
		with open(destination_path, output_mode) as f:
			f.write('\nNEW GEN\n\n')
			for text in texts:
				try:
					f.write("{}\n".format(text))
				except UnicodeEncodeError:
					continue

		# textgen.generate_to_file(r'\r_ucr_learned_titles.txt', n=3)

def generate_to_file(self, destination_path, **kwargs):
	texts = self.generate(return_as_list=True, **kwargs)
	with open(destination_path, output_mode) as f:
		f.write('\nNEW GEN\n\n')
		for text in texts:
			try:
				f.write("{}\n".format(text))
			except UnicodeEncodeError:
				continue

 
def _initArguments() -> argparse.Namespace:
        parser = argparse.ArgumentParser(description='Train and output RNN based on .txt file')

        parser.add_argument('-m', '--mode', type=str, help='Change output file to overwrite or append w+/a')
        parser.add_argument('-n', '--new', type=str, help='Train from new model')
        parser.add_argument('-i', '--iter', type=int, help='Number of epochs')

        return parser.parse_args()


main()
