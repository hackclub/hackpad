# Bill of Materials
* 1x PCB
* 1x Seeed Studio XIAO RP2040
* 4x M3 16mm bolt (same as in orpheuspad)
* 4x M3 bolt threaded heat insert (same as in orpheuspad)
* 1x SSD1306 128x64 0.96in 4-pin OLED display
* 9x Cherry MX switches (same as in orpheuspad)
* 9x DSA caps
# How to use
Like old phone keyboards! Layout:

|  |  |  |
| --- | --- | --- |
| `[_]` `[.]` `[,]` `[?]` `["]` `[:]` `[;]` | `[a]` `[b]` `[c]` | `[d]` `[e]` `[f]` |
| `[g]` `[h]` `[i]` | `[j]` `[k]` `[l]` | `[m]` `[n]` `[o]` |
| `[p]` `[q]` `[r]` `[s]` | `[t]` `[u]` `[v]` | `[w]` `[x]` `[y]` `[z]` |

Just keep pressing the same key until the letter you want appears
There's no way to type numbers as of now, but I will try my best to implement a second layout once I get the thing shipped to me.
The OLED is blank for now, but I want it to display the word you are typing in the future.

# About
This is a keyboard that works like the ones on old keypad phones - keys 2-9 have 3 or 4 letters on each of them, and you input each letter by pressing the number repeatedly until your desired letter shows up.
I only found out about matrix wiring by the time I was almost done with CAD (oops), so I could only add 9 switches by direct wiring.
As I'm missing a few keys compared to the old phone keypads, I'm mapping space to the 1 key.
I have plans to implement a predictive text mode that guesses which words you want to type from you only pressing each key once. This is what the OLED is for - that's where the algorithm's guesses for which word you are trying to type will be displayed. However, this is quite complicated and I don't have time to implement it at this moment, so the firmware only has the multitap mode in it as of now.