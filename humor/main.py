import click

from humor.models.FunBERT.train import train

@click.command()
@click.option('--test', is_flag=True, default=False, help='test model')
@click.option('--task', type=click.IntRange(0, 1), default=1, help='number of task')
@click.option('--model', type=click.Choice(['bert', 'roberta']), default='bert', help='architecture of model')
def main(test: bool, task: int, model: str):
    if test:
         pass
    else:
        train()

if __name__ == "__main__":
    main()