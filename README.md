# Language models as zero-shot planners with environment feedback

Project mentor: Maitreya Patel

Under the guidance of esteemed Dr.Chitta Baral.

## Objective

Use GPT-3 to decompose high-level tasks to low-level executable instructions for an agent in the VirtualHome environment. Compare the decomposition results between ours and the baseline.

## Approach

We divided our approach into two sequential steps. First, we check if GPT-3 can give the correct low-level instructions with a minimal prompt (no information about the environment given). Secondly, if GPT-3 fails to give the correct set of instructions, we supply it with a reduced set of objects and permissible actions along with an example set of instructions in the prompt. Since GPT-3 failed to give executable instructions with minimal prompts, we had to execute the second part of the plan.

## Setup

1. Clone virtualhome repo from [this](https://github.com/xavierpuigf/virtualhome) link
2. Run `pip install -r requirements.txt`

## SEE do_task.ipynb for detailed overview
