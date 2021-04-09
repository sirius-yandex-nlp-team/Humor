from typing import Tuple
from humor.context import ctx
from humor.config import params

def get_data_paths(task: str = 'task_1') -> Tuple[str]:
    r'''
    
    '''
    paths = params.data[task]
    abs_paths = {k: str(ctx.root_dir / path) for k, path in paths.items()}
    return abs_paths
 