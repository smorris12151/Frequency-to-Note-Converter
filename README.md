# Frequency to Note Conversion / Harmonic Overtone Generation




### To Run
Copy and paste the following into your command line of choice:
```
git clone https://github.com/smorris12151/Frequency-to-Note-Converter.git

cd Frequency-to-Note-Converter/src

python3 main.py

```
Note: `git` and `python3` are required.

## CLI Usage Example

![CLI Functionality 1](/imgs/demo1.png)
![CLI Functionality 2](/imgs/demo2.png)

## Background Info / Design Motivations

The goal of this project is to provide a succinct way of accurately mapping some arbitrary input frequency, represented as a float, as a musical note. To understand the math involved with this, some background music theory information is helpful:

### Music Theory Terms

|Units|Description|Example|
| --- | --- | ---|
|Semitones| The difference from one note to its immediate neighbor| $A$ to $A$# is one semitone; $A$ to $B$ is two semitones, and so on.|
|Chromatic Scale| A series of 12 notes, each one semitone apart from its neighbor, ending with a higher register of its starting note. | [$A$, $A$#, $B$, $C$, $C$#, $D$, $D$#, $E$, $F$, $F$#, $G$, $G$#] -> the next note in this series would be A, one octave up from the starting point.|
|Octave| A difference of 12 semitones, from a given note to the same note in a higher register, notated as $A_3$, $A_4$, etc | $A_2$ + 12 semitones = $A_3$|
|Cents| A smaller unit of measurement to define changes in notes; there are 100 cents to a semitone.| $A_3$ + 54 cents is different than $A_3$ + 55 cents (though most wouldn't hear any difference.)|
|Musical Note| An entirely arbitrary distinction between different audio frequencies, whos' naming conventions vary from culture to culture and style to style. | $A$# is equivalent to $B$ flat; Similarly, in some German music, $B$ natural is labeled as $H$! Ergo, names do not necessarily make the note.|

### Notes as Frequencies

Without getting too far into psychoacoustics, we as humans percieve changes in note as an exponential relationship of frequency; the basic mathematical relationship of this phenomenon is as follows:

$$f_n = f_0 \cdot 2^{\frac{n}{12}}$$

Our variables are defined as follows:
- $f_0$ is the frequency of our "0th" note
- $f_n$ is the frequency of our "nth" note, ie the frequency we are trying to calculate
- $n$ is the semitone jump from our 0th note to our nth note.
    - Note, by treating n as a floating point number with two decimal point precision, we can treat the digits to the left of the decimal point as our semitone value, and those two directly to the right as our cent value.
    - Ergo, if $n = 3.42$, we are working with a jump of 3 semitones and 42 cents.

### Anchoring Frequency / Defining our Tuning

In our above equation, the value $f_0$, and therefore, the exact frequency of all notes in that defined tuning, is more or less arbitrary; different cultures and styles of music choose different values for $f_0$, varying sometimes even from composer to composer! 

In general though, our default Western Standard is $A440$, indicating that the note $A_4$ is tuned to **440 Hz**.

### Calculating our Frequencies / Populating our Notes

With $f_0$ defined we can calculate an entire piano's worth of frequency values by subbing in integer values for $n$! 

In fact, as mentioned previously, if we extend $n$'s precision to two decimal places we can increase the precision of our frequency calculation 100 fold.

If we consider the lowest note on a standard 88 key piano, $A_0$, when we tune our piano to $A440$, this note has a frequency of **27.50 Hz**. By tradition, we start counting our octaves at $C$ instead of $A$; as such, we can define the following dictionary of "base frequencies" by working off of $A_0$:
| Note | Frequency|
|---|---|
|$C_0$|16.35 Hz|
|$C$#$_0$|17.32 Hz|
|$D_0$|18.35 Hz|
|$D$#$_0$|19.45 Hz|
|$E_0$|20.60 Hz|
|$F_0$|21.83 Hz|
|$F$#$_0$|23.12 Hz|
|$G_0$|24.50 Hz|
|$G$#$_0$|25.96 Hz|
|$A_0$|27.50 Hz|
|$A$#$_0$|29.14 Hz|
|$B_0$|30.87 Hz|

Note that this is not reflective of an actual piano keyboard - as mentioned, the lowest note on a standard piano is $A_0$; similarly, the range of human hearing generally peters out at about 20 Hz. This table of base frequencies is purely for the sake of programmatically building out note objects.

### Notes as Objects in Python

In our program, we define a Note object as follows:

```
class Note:
     def __init__(self, freq, factory):
        self.noteFactory = factory
        self.freq = freq
        self.name = factory.calculateNoteName(freq)
        self.octave = math.floor(factory.calculateOctave(freq))
        self.semitone = math.floor(factory.calculateSemitone(freq))
        self.cent = factory.calculateCents(freq)
```

Where our "factory" attribute, is the NoteFactory that builds our notes; the idea being that the global variables, such as our anchor/tuning frequency, are defined in the Note Factory. This allows for easy automation / standardization of our Note objects, and is defined as follows:

```
class NoteFactory:
    def __init__(self, anchorA):
        self.anchorA = anchorA
        self.C0 = round(anchorA * (2**(-57/12)), 2)
        self.noteNames = ['A','A#','B','C','C#','D','D#','E','F','F#','G','G#']
```
As you can see in our calculation for $C_0$'s frequency, we use our initial Anchor $A$ value, along with the number of semitones from that $A$ to our $C_0$ to calculate a new anchor value for our Note Factory, rooted at $C_0$ instead of $A_4$, for the sake of simpler calculations.

By leveraging our $C_0$ frequency and our list of note names, we can calculate all attributes of our Note objects with these basic functions:

```
def getAnchorA(self):
        return self.anchorA

def getNoteNames(self):
    return self.noteNames

def getC0(self):
    return self.C0

def calculateOctave(self, inputFreq):
    # Returns a float for later calculations
    return math.log2(inputFreq/self.getC0())

def calculateSemitone(self, inputFreq):
    #rounding semitone to 2 decimal places for clean cent calculation. Offset of -9 to reflect A0 as our 0th semitone (as seen on a normal piano).
    return round((self.calculateOctave(inputFreq) * 12), 2) - 9

def calculateCents(self, inputFreq):
    #modulo 1 takes the digits behind the decimal, multiply by 10 for int value of cents
    cents = self.calculateSemitone(inputFreq) % 1
    return int(cents*10)

def calculateJump(self, inputFreq):
    #Returns integer jump from anchorA for referencing noteNames array
    return int(self.calculateSemitone(inputFreq) % 12)

def calculateNoteName(self, inputFreq):
    index = self.calculateJump(inputFreq)
    return (self.getNoteNames())[index]
```

At this point, we can pass an arbitrary frequency and some tuned Note Factory into our Note Constructor, and spit out the corresponding musical note for said frequency. 

Ta Da!

![Basic Frequency to Note Conversion Example](/imgs/basic_conversion.png)


## Potential Use Case: Calculating Harmonic Series

One potential use of this sort of frequency to note conversion is a programmatic calculation of a given note's harmonic series.

According to [wikipedia](https://en.wikipedia.org/wiki/Harmonic_series_(music)), a Harmonic Series is a "sequence of harmonics, musical tones, or pure tones whose frequency is an integer multiple of a fundamental frequency."

We've already shown how to build notes from some fundamental frequency; ergo, we can easily build a function to calculate some note's harmonic series by simply building a Python list of note objects, each one with a frequency that is an integer multiple of our original note's frequency.

Below is an implementation of this function, as found in the Note class:

```
def calculateOverTones(self, numOverTones):
        
        overTones = []
        for i in range(1, numOverTones + 1):
            overToneFreq = self.freq * i
            overToneNote = Note(overToneFreq, self.getNoteFactory())
            overTones.append(overToneNote)
        return overTones
```

And integrated with our CLI:

![Harmonic Series Generation Example](/imgs/h_series.png)

This lays the groundwork for everything from a spectral analyser to a harmonizer; it's all just multiplication of frequencies!

## Next Steps

As demonstrated above (and through the provided CLI), I've pretty well fleshed out the logic for a frequency to note converter. Eventually, I aim to do the following:

0. Write test suite to sanity check my math (so far, my testing has been completely non-automated, simply comparing generated values to my own notebook calculations.)
1. Re-implement in C++; benchmark and compare runtimes from Python to C++
2. Rewrite as a Hardware driver for my STM32F030 Nucleo Dev board, taking advantage of the Analog I/O to build a rudimentary guitar tuner.


# Thanks for reading!
