### Behavior of `process.run()` with buffered commands

Run with:

`python -m avocado run /root/avocado-buffer/test.py`

Alternatively:
- `./run.sh`
or
- `./docker_run.sh`

Sample output:
```
=> Running avocado
=> Tailing log until avocado ends
2020-09-22 01:59:01,259 test             L0008 DEBUG| [logme] Test #1 | process with buffer (no live logging)
2020-09-22 01:59:16,289 process          L0416 DEBUG| [stdout] [logme] Iteration #0
2020-09-22 01:59:16,289 process          L0416 DEBUG| [stdout] [logme] Iteration #1
2020-09-22 01:59:16,289 process          L0416 DEBUG| [stdout] [logme] Iteration #2
2020-09-22 01:59:16,289 process          L0416 DEBUG| [stdout] [logme] Iteration #3
2020-09-22 01:59:16,290 process          L0416 DEBUG| [stdout] [logme] Iteration #4
2020-09-22 01:59:16,325 test             L0013 DEBUG| [logme] Test #2 | process without buffer via python -u (live logging ok)
2020-09-22 01:59:16,341 process          L0416 DEBUG| [stdout] [logme] Iteration #0
2020-09-22 01:59:19,344 process          L0416 DEBUG| [stdout] [logme] Iteration #1
2020-09-22 01:59:22,347 process          L0416 DEBUG| [stdout] [logme] Iteration #2
2020-09-22 01:59:25,350 process          L0416 DEBUG| [stdout] [logme] Iteration #3
2020-09-22 01:59:28,350 process          L0416 DEBUG| [stdout] [logme] Iteration #4
2020-09-22 01:59:31,386 test             L0018 DEBUG| [logme] Test #3 | process without buffer via script (live logging ok)
2020-09-22 01:59:31,404 process          L0416 DEBUG| [stdout] [logme] Iteration #0
2020-09-22 01:59:34,407 process          L0416 DEBUG| [stdout] [logme] Iteration #1
2020-09-22 01:59:37,410 process          L0416 DEBUG| [stdout] [logme] Iteration #2
2020-09-22 01:59:40,413 process          L0416 DEBUG| [stdout] [logme] Iteration #3
2020-09-22 01:59:43,415 process          L0416 DEBUG| [stdout] [logme] Iteration #4
2020-09-22 01:59:46,454 test             L0026 DEBUG| [logme] Test #4 | process without buffer via aexpect (live logging ok)
2020-09-22 01:59:46,516 test             L0024 DEBUG| [logme] Iteration #0
2020-09-22 01:59:49,519 test             L0024 DEBUG| [logme] Iteration #1
2020-09-22 01:59:52,522 test             L0024 DEBUG| [logme] Iteration #2
2020-09-22 01:59:55,523 test             L0024 DEBUG| [logme] Iteration #3
2020-09-22 01:59:58,526 test             L0024 DEBUG| [logme] Iteration #4
=> Done
```
