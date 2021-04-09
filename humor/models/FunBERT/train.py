from humor.config import params
from humor.utils.get_paths import get_data_paths
from humor.models.FunBERT.model import FunBERT


def train():
    data_paths = get_data_paths('task_1')

    model = FunBERT(data_paths['train'], 
                    data_paths['dev'],
                    data_paths['test'],
                    data_paths['lm'],
                    params.data.train_bathch_size,
                    params.data.test_bathch_size,
                    params.optimizer.learning_rate, 
                    'lm_joke_bert.pth',
                    params.optimizer.epochs,
                    None,
                    'model_2.pth',
                    params.model.type)
    #obj.bert_model = obj.bert_model.roberta
    #obj.bert_model.load_state_dict(torch.load('lm_joke_bert.pth'))
    model.train()

if __name__ == "__main__":
    train()