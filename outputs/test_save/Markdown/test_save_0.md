2024-05-29 06:42:21.616479: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Could not find TensorRT

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
| <c>name</c>       | <d>str</d>        | <j>"test_save-0"</j> |
| <c>time</c>       | <d>int</d>        | <f>3600</f>       |
| <c>lr</c>         | <d>float</d>      | <f>0.01</f>       |
| <c>batch_size</c> | <d>int</d>        | <f>8</f>          |
| <c>steps</c>      | <d>int</d>        | <f>10000</f>      |

# Output

```
Traceback (most recent call last):
  File "/zhome/ea/9/137501/Desktop/ML_final/ML_final/main.py", line 141, in <module>
    Defaults.start()
  File "/zhome/ea/9/137501/Desktop/ML_final/project-env/lib/python3.11/site-packages/dtu/__init__.py", line 235, in start
    cls.run(*args)
  File "/zhome/ea/9/137501/Desktop/ML_final/ML_final/main.py", line 28, in run
    from big_vision_test import big_vision_test, update_fn
ImportError: cannot import name 'update_fn' from 'big_vision_test' (/zhome/ea/9/137501/Desktop/ML_final/ML_final/big_vision_test.py)

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 21875690: <test_save_0> in cluster <dcc> Exited

Job <test_save_0> was submitted from host <n-62-30-6> by user <s183914> in cluster <dcc> at Wed May 29 06:41:51 2024
Job was executed on host(s) <4*n-62-20-10>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Wed May 29 06:41:51 2024
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/ML_final/ML_final> was used as the working directory.
Started at Wed May 29 06:41:51 2024
Terminated at Wed May 29 06:42:33 2024
Results reported at Wed May 29 06:42:33 2024

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 4
#BSUB -R "rusage[mem=16G]"
#BSUB -R "select[gpu32gb]"
#BSUB -R "span[hosts=1]"
#BSUB -W 1440
# end of BSUB options
module -s load python3
source ../project-env/bin/activate

python main.py $MYARGS
------------------------------------------------------------

Exited with exit code 1.

Resource usage summary:

    CPU time :                                   6.29 sec.
    Max Memory :                                 191 MB
    Average Memory :                             191.00 MB
    Total Requested Memory :                     65536.00 MB
    Delta Memory :                               65345.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                5
    Run time :                                   114 sec.
    Turnaround time :                            42 sec.

The output (if any) is above this job summary.

