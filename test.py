import torch
from main2 import RNNModule, get_data_from_file,predict

from argparse import Namespace

flags = Namespace(
    train_file='trump.txt',
    seq_size=32,
    batch_size=16,
    embedding_size=64,
    lstm_size=64,
    gradients_norm=5,
    initial_words=['I', 'am'],
    predict_top_k=5,
    checkpoint_path='checkpoint',
)

def getOutPut():
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    int_to_vocab, vocab_to_int, n_vocab, in_text, out_text = get_data_from_file(
        flags.train_file, flags.batch_size, flags.seq_size)

    net = RNNModule(n_vocab, flags.seq_size,
                    flags.embedding_size, flags.lstm_size)
    net = net.to(device)


    predict(device, net, flags.initial_words, n_vocab,
            vocab_to_int, int_to_vocab, top_k=5)


if __name__ == '__main__':
    getOutPut()