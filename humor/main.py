import click

from humor.models.FunBERT.train import train

@click.command()
@click.option('--test', is_flag=True, default=False, help='test model')
@click.option('--task', type=click.IntRange(0, 1), default=1, help='number of task')
@click.option('--model', type=click.Choice(['bert', 'roberta']), default='bert', help='architecture of model')
def main(test, task, model):
    task = 'task_1' if task == 1 else 'task_2' 
    if test:
        pass
    else:
        train(task=task, model_type=model)

if __name__ == "__main__":
    main()