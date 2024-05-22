
<style>
c { color: #9cdcfe; font-family: 'Verdana', sans-serif;} /* VARIABLE */
d { color: #4EC9B0; font-family: 'Verdana', sans-serif;} /* CLASS */
e { color: #569cd6; font-family: 'Verdana', sans-serif;} /* BOOL */
f { color: #b5cea8; font-family: 'Verdana', sans-serif;} /* NUMBERS */
j { color: #ce9178; font-family: 'Verdana', sans-serif;} /* STRING */
k { font-family: 'Verdana', sans-serif;} /* SYMBOLS */
</style>

# Parameters

| PARAMETER         | TYPE              | VALUE             |
|-------------------|-------------------|-------------------|
| <c>name</c>       | <d>str</d>        | <j>"Tester-0"</j> |
| <c>time</c>       | <d>int</d>        | <f>3600</f>       |

# Output

```
Traceback (most recent call last):
  File "/zhome/ea/9/137501/Desktop/ML_final/project-env/lib/python3.11/site-packages/jax/_src/lib/__init__.py", line 26, in <module>
    import jaxlib as jaxlib
ModuleNotFoundError: No module named 'jaxlib'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/zhome/ea/9/137501/Desktop/ML_final/ML_final/main.py", line 39, in <module>
    Defaults.start()
  File "/zhome/ea/9/137501/Desktop/ML_final/project-env/lib/python3.11/site-packages/dtu/__init__.py", line 235, in start
    cls.run(*args)
  File "/zhome/ea/9/137501/Desktop/ML_final/ML_final/main.py", line 19, in run
    from big_vision_test import big_vision_test
  File "/zhome/ea/9/137501/Desktop/ML_final/ML_final/big_vision_test.py", line 5, in <module>
    import jax
  File "/zhome/ea/9/137501/Desktop/ML_final/project-env/lib/python3.11/site-packages/jax/__init__.py", line 37, in <module>
    import jax.core as _core
  File "/zhome/ea/9/137501/Desktop/ML_final/project-env/lib/python3.11/site-packages/jax/core.py", line 18, in <module>
    from jax._src.core import (
  File "/zhome/ea/9/137501/Desktop/ML_final/project-env/lib/python3.11/site-packages/jax/_src/core.py", line 39, in <module>
    from jax._src import dtypes
  File "/zhome/ea/9/137501/Desktop/ML_final/project-env/lib/python3.11/site-packages/jax/_src/dtypes.py", line 33, in <module>
    from jax._src import config
  File "/zhome/ea/9/137501/Desktop/ML_final/project-env/lib/python3.11/site-packages/jax/_src/config.py", line 27, in <module>
    from jax._src import lib
  File "/zhome/ea/9/137501/Desktop/ML_final/project-env/lib/python3.11/site-packages/jax/_src/lib/__init__.py", line 28, in <module>
    raise ModuleNotFoundError(
ModuleNotFoundError: jax requires jaxlib to be installed. See https://github.com/google/jax#installation for installation instructions.

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 21832179: <Tester_0> in cluster <dcc> Exited

Job <Tester_0> was submitted from host <n-62-27-18> by user <s183914> in cluster <dcc> at Wed May 22 09:22:34 2024
Job was executed on host(s) <n-62-31-3>, in queue <hpc>, as user <s183914> in cluster <dcc> at Wed May 22 09:22:34 2024
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/ML_final/ML_final> was used as the working directory.
Started at Wed May 22 09:22:34 2024
Terminated at Wed May 22 09:22:42 2024
Results reported at Wed May 22 09:22:42 2024

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -n 1
#BSUB -R "rusage[mem=16G]"
#BSUB -R "span[hosts=1]"
#BSUB -W 4320
# end of BSUB options
module -s load python3
source ../project-env/bin/activate

python main.py $MYARGS
------------------------------------------------------------

Exited with exit code 1.

Resource usage summary:

    CPU time :                                   2.35 sec.
    Max Memory :                                 -
    Average Memory :                             -
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               -
    Max Swap :                                   -
    Max Processes :                              -
    Max Threads :                                -
    Run time :                                   77 sec.
    Turnaround time :                            8 sec.

The output (if any) is above this job summary.


<style>
c { color: #9cdcfe; font-family: 'Verdana', sans-serif;} /* VARIABLE */
d { color: #4EC9B0; font-family: 'Verdana', sans-serif;} /* CLASS */
e { color: #569cd6; font-family: 'Verdana', sans-serif;} /* BOOL */
f { color: #b5cea8; font-family: 'Verdana', sans-serif;} /* NUMBERS */
j { color: #ce9178; font-family: 'Verdana', sans-serif;} /* STRING */
k { font-family: 'Verdana', sans-serif;} /* SYMBOLS */
</style>

# Parameters

| PARAMETER         | TYPE              | VALUE             |
|-------------------|-------------------|-------------------|
| <c>name</c>       | <d>str</d>        | <j>"Tester-0"</j> |
| <c>time</c>       | <d>int</d>        | <f>3600</f>       |

# Output

```
Traceback (most recent call last):
  File "/zhome/ea/9/137501/Desktop/ML_final/ML_final/main.py", line 39, in <module>
    Defaults.start()
  File "/zhome/ea/9/137501/Desktop/ML_final/project-env/lib/python3.11/site-packages/dtu/__init__.py", line 235, in start
    cls.run(*args)
  File "/zhome/ea/9/137501/Desktop/ML_final/ML_final/main.py", line 19, in run
    from big_vision_test import big_vision_test
  File "/zhome/ea/9/137501/Desktop/ML_final/ML_final/big_vision_test.py", line 10, in <module>
    from big_vision.models.proj.paligemma import paligemma
  File "/zhome/ea/9/137501/Desktop/ML_final/ML_final/big_vision/models/proj/paligemma/paligemma.py", line 20, in <module>
    import flax.linen as nn
ModuleNotFoundError: No module named 'flax'

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 21832204: <Tester_0> in cluster <dcc> Exited

Job <Tester_0> was submitted from host <n-62-27-18> by user <s183914> in cluster <dcc> at Wed May 22 09:24:57 2024
Job was executed on host(s) <n-62-31-3>, in queue <hpc>, as user <s183914> in cluster <dcc> at Wed May 22 09:24:58 2024
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/ML_final/ML_final> was used as the working directory.
Started at Wed May 22 09:24:58 2024
Terminated at Wed May 22 09:25:04 2024
Results reported at Wed May 22 09:25:04 2024

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -n 1
#BSUB -R "rusage[mem=16G]"
#BSUB -R "span[hosts=1]"
#BSUB -W 4320
# end of BSUB options
module -s load python3
source ../project-env/bin/activate

python main.py $MYARGS
------------------------------------------------------------

Exited with exit code 1.

Resource usage summary:

    CPU time :                                   2.47 sec.
    Max Memory :                                 -
    Average Memory :                             -
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               -
    Max Swap :                                   -
    Max Processes :                              -
    Max Threads :                                -
    Run time :                                   16 sec.
    Turnaround time :                            7 sec.

The output (if any) is above this job summary.

Downloading from https://www.kaggle.com/api/v1/models/google/paligemma/jax/paligemma-3b-pt-224/1/download/paligemma-3b-pt-224.f16.npz...

<style>
c { color: #9cdcfe; font-family: 'Verdana', sans-serif;} /* VARIABLE */
d { color: #4EC9B0; font-family: 'Verdana', sans-serif;} /* CLASS */
e { color: #569cd6; font-family: 'Verdana', sans-serif;} /* BOOL */
f { color: #b5cea8; font-family: 'Verdana', sans-serif;} /* NUMBERS */
j { color: #ce9178; font-family: 'Verdana', sans-serif;} /* STRING */
k { font-family: 'Verdana', sans-serif;} /* SYMBOLS */
</style>

# Parameters

| PARAMETER         | TYPE              | VALUE             |
|-------------------|-------------------|-------------------|
| <c>name</c>       | <d>str</d>        | <j>"Tester-0"</j> |
| <c>time</c>       | <d>int</d>        | <f>3600</f>       |

# Output

```
  0%|          | 0.00/5.45G [00:00<?, ?B/s]  0%|          | 1.00M/5.45G [00:00<1:04:10, 1.52MB/s]  0%|          | 3.00M/5.45G [00:00<21:56, 4.44MB/s]    0%|          | 7.00M/5.45G [00:00<08:54, 10.9MB/s]  0%|          | 11.0M/5.45G [00:01<05:42, 17.0MB/s]  0%|          | 14.0M/5.45G [00:01<05:10, 18.8MB/s]  0%|          | 20.0M/5.45G [00:01<03:28, 28.0MB/s]  0%|          | 24.0M/5.45G [00:01<03:08, 31.0MB/s]  1%|          | 28.0M/5.45G [00:01<02:52, 33.7MB/s]  1%|          | 32.0M/5.45G [00:01<02:46, 35.0MB/s]  1%|          | 36.0M/5.45G [00:01<02:40, 36.2MB/s]  1%|          | 40.0M/5.45G [00:01<02:36, 37.2MB/s]  1%|          | 44.0M/5.45G [00:01<02:31, 38.2MB/s]  1%|          | 48.0M/5.45G [00:02<03:16, 29.4MB/s]  1%|          | 52.0M/5.45G [00:02<02:59, 32.3MB/s]  1%|          | 56.0M/5.45G [00:02<03:09, 30.5MB/s]  1%|          | 60.0M/5.45G [00:02<03:16, 29.4MB/s]  1%|          | 64.0M/5.45G [00:02<02:58, 32.3MB/s]  1%|          | 69.0M/5.45G [00:02<02:37, 36.7MB/s]  1%|▏         | 73.0M/5.45G [00:02<02:32, 38.0MB/s]  1%|▏         | 77.0M/5.45G [00:02<02:28, 39.0MB/s]  1%|▏         | 81.0M/5.45G [00:03<02:27, 39.1MB/s]  2%|▏         | 85.0M/5.45G [00:03<02:27, 39.0MB/s]  2%|▏         | 89.0M/5.45G [00:03<02:47, 34.3MB/s]  2%|▏         | 93.0M/5.45G [00:03<02:52, 33.4MB/s]  2%|▏         | 97.0M/5.45G [00:03<02:41, 35.6MB/s]  2%|▏         | 101M/5.45G [00:03<02:55, 32.7MB/s]   2%|▏         | 105M/5.45G [00:03<02:46, 34.5MB/s]  2%|▏         | 110M/5.45G [00:03<02:28, 38.6MB/s]  2%|▏         | 114M/5.45G [00:04<02:25, 39.4MB/s]  2%|▏         | 118M/5.45G [00:04<02:39, 36.0MB/s]  2%|▏         | 122M/5.45G [00:04<03:11, 29.8MB/s]  2%|▏         | 126M/5.45G [00:04<02:55, 32.6MB/s]  2%|▏         | 131M/5.45G [00:04<02:34, 36.9MB/s]  2%|▏         | 136M/5.45G [00:04<02:27, 38.6MB/s]  3%|▎         | 140M/5.45G [00:04<02:57, 32.1MB/s]  3%|▎         | 147M/5.45G [00:05<02:17, 41.4MB/s]  3%|▎         | 152M/5.45G [00:05<02:29, 38.0MB/s]  3%|▎         | 156M/5.45G [00:05<02:26, 38.8MB/s]  3%|▎         | 160M/5.45G [00:05<02:25, 39.0MB/s]  3%|▎         | 164M/5.45G [00:05<02:22, 39.8MB/s]  3%|▎         | 168M/5.45G [00:05<02:20, 40.3MB/s]  3%|▎         | 172M/5.45G [00:05<02:19, 40.6MB/s]  3%|▎         | 176M/5.45G [00:05<02:21, 40.1MB/s]  3%|▎         | 180M/5.45G [00:05<02:34, 36.7MB/s]  3%|▎         | 184M/5.45G [00:06<02:35, 36.4MB/s]  3%|▎         | 188M/5.45G [00:06<02:30, 37.5MB/s]  3%|▎         | 192M/5.45G [00:06<02:31, 37.2MB/s]  4%|▎         | 196M/5.45G [00:06<02:37, 35.9MB/s]  4%|▎         | 200M/5.45G [00:06<02:31, 37.3MB/s]  4%|▎         | 205M/5.45G [00:06<02:19, 40.5MB/s]  4%|▎         | 209M/5.45G [00:06<02:18, 40.7MB/s]  4%|▍         | 214M/5.45G [00:06<02:22, 39.4MB/s]  4%|▍         | 218M/5.45G [00:06<02:23, 39.2MB/s]  4%|▍         | 222M/5.45G [00:07<02:30, 37.4MB/s]  4%|▍         | 227M/5.45G [00:07<02:18, 40.4MB/s]  4%|▍         | 231M/5.45G [00:07<02:22, 39.4MB/s]  4%|▍         | 236M/5.45G [00:07<02:20, 39.9MB/s]  4%|▍         | 240M/5.45G [00:07<02:22, 39.4MB/s]  4%|▍         | 244M/5.45G [00:07<02:28, 37.6MB/s]  4%|▍         | 248M/5.45G [00:07<02:24, 38.6MB/s]  5%|▍         | 252M/5.45G [00:07<02:21, 39.3MB/s]  5%|▍         | 257M/5.45G [00:08<02:23, 39.0MB/s]  5%|▍         | 261M/5.45G [00:08<02:41, 34.4MB/s]  5%|▍         | 265M/5.45G [00:08<02:34, 35.9MB/s]  5%|▍         | 269M/5.45G [00:08<02:34, 36.0MB/s]  5%|▍         | 273M/5.45G [00:08<02:28, 37.4MB/s]  5%|▍         | 277M/5.45G [00:08<03:08, 29.5MB/s]  5%|▌         | 284M/5.45G [00:08<02:20, 39.5MB/s]  5%|▌         | 289M/5.45G [00:08<02:22, 38.8MB/s]  5%|▌         | 294M/5.45G [00:09<02:19, 39.7MB/s]  5%|▌         | 299M/5.45G [00:09<03:16, 28.1MB/s]  5%|▌         | 305M/5.45G [00:09<02:49, 32.6MB/s]  6%|▌         | 309M/5.45G [00:09<02:42, 34.0MB/s]  6%|▌         | 314M/5.45G [00:09<02:26, 37.6MB/s]  6%|▌         | 318M/5.45G [00:09<02:23, 38.4MB/s]  6%|▌         | 322M/5.45G [00:09<02:20, 39.2MB/s]  6%|▌         | 326M/5.45G [00:10<02:47, 32.9MB/s]  6%|▌         | 332M/5.45G [00:10<02:17, 39.9MB/s]  6%|▌         | 337M/5.45G [00:10<02:42, 33.8MB/s]  6%|▌         | 341M/5.45G [00:10<02:43, 33.6MB/s]  6%|▌         | 345M/5.45G [00:10<02:34, 35.5MB/s]  6%|▋         | 349M/5.45G [00:10<02:54, 31.4MB/s]  6%|▋         | 353M/5.45G [00:10<03:09, 28.8MB/s]  6%|▋         | 356M/5.45G [00:11<03:25, 26.7MB/s]  6%|▋         | 359M/5.45G [00:11<03:40, 24.8MB/s]  7%|▋         | 364M/5.45G [00:11<02:56, 30.9MB/s]  7%|▋         | 369M/5.45G [00:11<02:34, 35.3MB/s]  7%|▋         | 373M/5.45G [00:11<02:28, 36.8MB/s]  7%|▋         | 377M/5.45G [00:11<02:23, 38.1MB/s]  7%|▋         | 381M/5.45G [00:11<02:26, 37.2MB/s]  7%|▋         | 385M/5.45G [00:11<02:21, 38.3MB/s]  7%|▋         | 389M/5.45G [00:12<02:35, 35.0MB/s]  7%|▋         | 393M/5.45G [00:12<02:28, 36.6MB/s]  7%|▋         | 397M/5.45G [00:12<02:39, 34.1MB/s]  7%|▋         | 401M/5.45G [00:12<02:51, 31.7MB/s]  7%|▋         | 405M/5.45G [00:12<02:38, 34.1MB/s]  7%|▋         | 409M/5.45G [00:12<02:30, 36.0MB/s]  7%|▋         | 413M/5.45G [00:12<02:35, 34.7MB/s]  7%|▋         | 417M/5.45G [00:12<02:31, 35.7MB/s]  8%|▊         | 421M/5.45G [00:13<02:37, 34.4MB/s]  8%|▊         | 425M/5.45G [00:13<02:51, 31.5MB/s]  8%|▊         | 429M/5.45G [00:13<02:38, 34.0MB/s]  8%|▊         | 433M/5.45G [00:13<02:30, 35.8MB/s]  8%|▊         | 438M/5.45G [00:13<02:16, 39.4MB/s]  8%|▊         | 442M/5.45G [00:13<02:14, 39.9MB/s]  8%|▊         | 446M/5.45G [00:13<02:44, 32.8MB/s]  8%|▊         | 452M/5.45G [00:13<02:17, 39.1MB/s]  8%|▊         | 456M/5.45G [00:14<02:15, 39.7MB/s]  8%|▊         | 460M/5.45G [00:14<02:14, 39.9MB/s]  8%|▊         | 464M/5.45G [00:14<02:45, 32.3MB/s]  8%|▊         | 471M/5.45G [00:14<02:09, 41.2MB/s]  9%|▊         | 476M/5.45G [00:14<02:18, 38.5MB/s]  9%|▊         | 481M/5.45G [00:14<02:26, 36.5MB/s]  9%|▊         | 485M/5.45G [00:14<02:22, 37.6MB/s]  9%|▉         | 489M/5.45G [00:14<02:28, 36.0MB/s]  9%|▉         | 494M/5.45G [00:15<02:13, 39.9MB/s]  9%|▉         | 498M/5.45G [00:15<02:12, 40.2MB/s]  9%|▉         | 502M/5.45G [00:15<02:11, 40.4MB/s]  9%|▉         | 506M/5.45G [00:15<02:42, 32.7MB/s]  9%|▉         | 510M/5.45G [00:15<02:33, 34.5MB/s]  9%|▉         | 514M/5.45G [00:15<02:40, 33.0MB/s]  9%|▉         | 518M/5.45G [00:15<02:38, 33.5MB/s]  9%|▉         | 522M/5.45G [00:16<03:04, 28.7MB/s]  9%|▉         | 528M/5.45G [00:16<02:44, 32.3MB/s] 10%|▉         | 532M/5.45G [00:16<02:34, 34.3MB/s] 10%|▉         | 536M/5.45G [00:16<02:26, 36.0MB/s] 10%|▉         | 541M/5.45G [00:16<02:14, 39.3MB/s] 10%|▉         | 546M/5.45G [00:16<02:22, 37.0MB/s] 10%|▉         | 550M/5.45G [00:16<02:22, 37.0MB/s] 10%|▉         | 554M/5.45G [00:16<02:35, 34.0MB/s] 10%|█         | 558M/5.45G [00:17<02:38, 33.1MB/s] 10%|█         | 562M/5.45G [00:17<02:44, 31.9MB/s] 10%|█         | 566M/5.45G [00:17<02:33, 34.2MB/s] 10%|█         | 571M/5.45G [00:17<02:20, 37.4MB/s] 10%|█         | 575M/5.45G [00:17<02:17, 38.2MB/s] 10%|█         | 579M/5.45G [00:17<02:28, 35.3MB/s] 10%|█         | 583M/5.45G [00:17<02:32, 34.4MB/s] 11%|█         | 587M/5.45G [00:17<02:33, 34.0MB/s] 11%|█         | 591M/5.45G [00:18<02:36, 33.5MB/s] 11%|█         | 595M/5.45G [00:18<02:36, 33.3MB/s] 11%|█         | 599M/5.45G [00:18<02:35, 33.6MB/s] 11%|█         | 603M/5.45G [00:18<02:49, 30.7MB/s] 11%|█         | 609M/5.45G [00:18<02:23, 36.4MB/s] 11%|█         | 613M/5.45G [00:18<02:19, 37.4MB/s] 11%|█         | 617M/5.45G [00:18<02:15, 38.5MB/s] 11%|█         | 621M/5.45G [00:18<02:20, 36.9MB/s] 11%|█         | 625M/5.45G [00:19<02:26, 35.5MB/s] 11%|█▏        | 631M/5.45G [00:19<02:08, 40.2MB/s] 11%|█▏        | 635M/5.45G [00:19<02:21, 36.5MB/s] 11%|█▏        | 639M/5.45G [00:19<02:16, 37.8MB/s] 12%|█▏        | 643M/5.45G [00:19<02:14, 38.5MB/s] 12%|█▏        | 647M/5.45G [00:19<02:18, 37.3MB/s] 12%|█▏        | 651M/5.45G [00:19<02:46, 31.0MB/s] 12%|█▏        | 655M/5.45G [00:19<02:37, 32.7MB/s] 12%|█▏        | 659M/5.45G [00:20<02:28, 34.6MB/s] 12%|█▏        | 663M/5.45G [00:20<02:21, 36.3MB/s] 12%|█▏        | 667M/5.45G [00:20<02:25, 35.3MB/s] 12%|█▏        | 671M/5.45G [00:20<02:45, 31.1MB/s] 12%|█▏        | 677M/5.45G [00:20<02:17, 37.5MB/s] 12%|█▏        | 682M/5.45G [00:20<02:07, 40.3MB/s] 12%|█▏        | 687M/5.45G [00:20<02:11, 39.1MB/s] 12%|█▏        | 691M/5.45G [00:20<02:16, 37.5MB/s] 12%|█▏        | 695M/5.45G [00:21<02:40, 32.0MB/s] 13%|█▎        | 700M/5.45G [00:21<02:27, 34.6MB/s] 13%|█▎        | 704M/5.45G [00:21<02:28, 34.4MB/s] 13%|█▎        | 710M/5.45G [00:21<02:30, 33.9MB/s] 13%|█▎        | 716M/5.45G [00:21<02:08, 39.7MB/s] 13%|█▎        | 721M/5.45G [00:21<02:03, 41.2MB/s] 13%|█▎        | 726M/5.45G [00:21<02:06, 40.3MB/s] 13%|█▎        | 730M/5.45G [00:22<02:06, 40.3MB/s] 13%|█▎        | 735M/5.45G [00:22<02:06, 40.1MB/s] 13%|█▎        | 739M/5.45G [00:22<02:07, 39.7MB/s] 13%|█▎        | 743M/5.45G [00:22<02:31, 33.4MB/s] 13%|█▎        | 747M/5.45G [00:22<03:00, 28.1MB/s] 13%|█▎        | 751M/5.45G [00:22<02:53, 29.2MB/s] 14%|█▎        | 754M/5.45G [00:22<03:03, 27.5MB/s] 14%|█▎        | 757M/5.45G [00:23<03:11, 26.3MB/s] 14%|█▎        | 760M/5.45G [00:23<03:18, 25.4MB/s] 14%|█▎        | 763M/5.45G [00:23<03:23, 24.7MB/s] 14%|█▎        | 766M/5.45G [00:23<03:28, 24.2MB/s] 14%|█▍        | 769M/5.45G [00:23<03:31, 23.8MB/s] 14%|█▍        | 772M/5.45G [00:23<03:38, 23.0MB/s] 14%|█▍        | 775M/5.45G [00:23<03:33, 23.6MB/s] 14%|█▍        | 779M/5.45G [00:23<02:59, 28.0MB/s] 14%|█▍        | 784M/5.45G [00:24<02:34, 32.6MB/s] 14%|█▍        | 789M/5.45G [00:24<02:19, 36.0MB/s] 14%|█▍        | 793M/5.45G [00:24<02:29, 33.6MB/s] 14%|█▍        | 797M/5.45G [00:24<02:20, 35.6MB/s] 14%|█▍        | 801M/5.45G [00:24<02:22, 35.2MB/s] 14%|█▍        | 805M/5.45G [00:24<02:16, 36.8MB/s] 15%|█▍        | 809M/5.45G [00:24<02:23, 34.8MB/s] 15%|█▍        | 813M/5.45G [00:24<02:43, 30.5MB/s] 15%|█▍        | 817M/5.45G [00:25<02:45, 30.2MB/s] 15%|█▍        | 820M/5.45G [00:25<02:46, 29.9MB/s] 15%|█▍        | 823M/5.45G [00:25<02:55, 28.4MB/s] 15%|█▍        | 826M/5.45G [00:25<02:52, 28.8MB/s] 15%|█▍        | 830M/5.45G [00:25<02:35, 32.1MB/s] 15%|█▍        | 835M/5.45G [00:25<02:42, 30.6MB/s] 15%|█▌        | 841M/5.45G [00:25<02:13, 37.1MB/s] 15%|█▌        | 845M/5.45G [00:26<02:17, 36.1MB/s] 15%|█▌        | 849M/5.45G [00:26<02:15, 36.6MB/s] 15%|█▌        | 853M/5.45G [00:26<02:13, 37.0MB/s] 15%|█▌        | 857M/5.45G [00:26<02:12, 37.3MB/s] 15%|█▌        | 861M/5.45G [00:26<02:20, 35.2MB/s] 16%|█▌        | 865M/5.45G [00:26<02:29, 33.0MB/s] 16%|█▌        | 869M/5.45G [00:26<03:01, 27.1MB/s] 16%|█▌        | 873M/5.45G [00:27<03:17, 25.0MB/s] 16%|█▌        | 877M/5.45G [00:27<02:55, 28.0MB/s] 16%|█▌        | 880M/5.45G [00:27<03:03, 26.9MB/s] 16%|█▌        | 883M/5.45G [00:27<03:08, 26.2MB/s] 16%|█▌        | 886M/5.45G [00:27<03:12, 25.5MB/s] 16%|█▌        | 889M/5.45G [00:27<03:15, 25.1MB/s] 16%|█▌        | 892M/5.45G [00:27<03:16, 25.0MB/s] 16%|█▌        | 896M/5.45G [00:27<03:23, 24.2MB/s] 16%|█▌        | 899M/5.45G [00:28<03:11, 25.6MB/s] 16%|█▌        | 902M/5.45G [00:28<03:18, 24.7MB/s] 16%|█▌        | 905M/5.45G [00:28<03:23, 24.1MB/s] 16%|█▋        | 908M/5.45G [00:28<03:26, 23.7MB/s] 16%|█▋        | 911M/5.45G [00:28<03:29, 23.4MB/s] 16%|█▋        | 914M/5.45G [00:28<03:30, 23.2MB/s] 16%|█▋        | 917M/5.45G [00:28<03:32, 23.0MB/s] 16%|█▋        | 920M/5.45G [00:29<03:33, 22.9MB/s] 17%|█▋        | 923M/5.45G [00:29<03:33, 22.8MB/s] 17%|█▋        | 926M/5.45G [00:29<03:35, 22.6MB/s] 17%|█▋        | 929M/5.45G [00:29<03:55, 20.7MB/s] 17%|█▋        | 932M/5.45G [00:29<04:05, 19.8MB/s] 17%|█▋        | 934M/5.45G [00:29<04:10, 19.4MB/s] 17%|█▋        | 936M/5.45G [00:29<04:15, 19.1MB/s] 17%|█▋        | 938M/5.45G [00:30<04:18, 18.8MB/s] 17%|█▋        | 940M/5.45G [00:30<04:15, 19.0MB/s] 17%|█▋        | 944M/5.45G [00:30<03:17, 24.5MB/s] 17%|█▋        | 948M/5.45G [00:30<02:46, 29.1MB/s] 17%|█▋        | 951M/5.45G [00:30<02:45, 29.3MB/s] 17%|█▋        | 954M/5.45G [00:30<03:09, 25.6MB/s] 17%|█▋        | 957M/5.45G [00:30<03:06, 26.0MB/s] 17%|█▋        | 960M/5.45G [00:30<03:03, 26.3MB/s] 17%|█▋        | 963M/5.45G [00:30<03:10, 25.4MB/s] 17%|█▋        | 966M/5.45G [00:31<03:18, 24.3MB/s] 17%|█▋        | 969M/5.45G [00:31<03:23, 23.7MB/s] 17%|█▋        | 972M/5.45G [00:31<04:03, 19.8MB/s] 17%|█▋        | 975M/5.45G [00:31<03:47, 21.2MB/s] 18%|█▊        | 978M/5.45G [00:31<04:07, 19.4MB/s] 18%|█▊        | 980M/5.45G [00:31<04:18, 18.6MB/s] 18%|█▊        | 982M/5.45G [00:32<04:27, 18.0MB/s] 18%|█▊        | 984M/5.45G [00:32<05:12, 15.4MB/s] 18%|█▊        | 986M/5.45G [00:32<05:04, 15.8MB/s] 18%|█▊        | 988M/5.45G [00:32<05:27, 14.7MB/s] 18%|█▊        | 990M/5.45G [00:32<05:52, 13.6MB/s] 18%|█▊        | 992M/5.45G [00:32<06:01, 13.3MB/s] 18%|█▊        | 996M/5.45G [00:33<04:18, 18.6MB/s] 18%|█▊        | 0.98G/5.45G [00:33<03:26, 23.3MB/s] 18%|█▊        | 0.98G/5.45G [00:33<02:56, 27.1MB/s] 18%|█▊        | 0.99G/5.45G [00:33<02:25, 33.0MB/s] 18%|█▊        | 0.99G/5.45G [00:33<02:24, 33.1MB/s] 18%|█▊        | 0.99G/5.45G [00:33<02:15, 35.3MB/s] 18%|█▊        | 1.00G/5.45G [00:33<02:22, 33.6MB/s] 18%|█▊        | 1.00G/5.45G [00:33<02:29, 31.9MB/s] 18%|█▊        | 1.01G/5.45G [00:33<02:01, 39.1MB/s] 19%|█▊        | 1.01G/5.45G [00:34<02:03, 38.6MB/s] 19%|█▊        | 1.02G/5.45G [00:34<02:00, 39.4MB/s] 19%|█▊        | 1.02G/5.45G [00:34<01:59, 39.8MB/s] 19%|█▉        | 1.02G/5.45G [00:34<01:59, 39.8MB/s] 19%|█▉        | 1.03G/5.45G [00:34<01:58, 40.0MB/s] 19%|█▉        | 1.03G/5.45G [00:34<01:58, 39.8MB/s] 19%|█▉        | 1.04G/5.45G [00:34<02:13, 35.4MB/s] 19%|█▉        | 1.04G/5.45G [00:34<02:08, 37.0MB/s] 19%|█▉        | 1.04G/5.45G [00:35<02:18, 34.1MB/s] 19%|█▉        | 1.05G/5.45G [00:35<02:27, 32.0MB/s] 19%|█▉        | 1.05G/5.45G [00:35<02:18, 34.0MB/s] 19%|█▉        | 1.05G/5.45G [00:35<02:15, 34.9MB/s] 19%|█▉        | 1.06G/5.45G [00:35<02:27, 32.0MB/s] 20%|█▉        | 1.06G/5.45G [00:35<02:13, 35.3MB/s] 20%|█▉        | 1.07G/5.45G [00:35<02:44, 28.6MB/s] 20%|█▉        | 1.07G/5.45G [00:36<02:36, 30.1MB/s] 20%|█▉        | 1.08G/5.45G [00:36<02:07, 36.8MB/s] 20%|█▉        | 1.08G/5.45G [00:36<02:05, 37.2MB/s]