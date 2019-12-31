# NVEDU (Non Visual Education)

The NVEDU is an handheld device designed for visually challenged individuals to avail 

* Entertainment, 
* Education, and 
* Improvement of litrary knowledge 

The speciality of the device lies in the revolutionarily convinient and enabling method of operations and features provided (compared to the alternatives available today)

## Preview (Alpha)

![Aplha Preview Image](/assets/images/Sizecomparision-hand.png)

## Feature List

* Navigation of internal directory structure without visual cues (using audio)
* Media file manipulation (play, pause, seek)
* Modular with removable memory storage

## Controls

All controls are single key character configuration in PC ubutntu and buttons in raspbian

```
sa - stop all running processes
l - list all files in directory
n - say current directory name
x - move over next directory
z - move over previous directory
q - shift one file backward
e - shift one file forward
p - Proceed into directory
o - open current file
0 - pause audio
1 - play audio
4 - seek audio forward 10 seconds
3 - seek audio backward 10 seconds
```

## Cost Estimates

* Raspberry Pi Zero - ₹1,600

## Problems resolved

### Synchronization of values between processes

Tried solving using pool and multiprocessing values, but due to the asynchronous and independent nature of Process and add the fact that only one process should run at a time, the best solution is to remove the dependance on shared memory

Solved this problem by extracting the part that requires shared memory 