Say, you have a huge list of phrases and you want to search these phrases in a huge dataset.

### Phrases:

|id   | phrase |
|-----|-------------
|1    |pot boiler|
|2    |hot cake|
|3    |cold turkey|
|4    |to be or not to be|
|5    |ice ice baby|

### Content:

|id  | text     |
|----|-----------------------------------------------------------------------------------------|
|1   |Earlier the work he did was a hot cake but once he quit cold turkey he never received a call from the publishers boiler|
|2   |The question to be or not to for him was to be or not to be on look out for pot boiler cold|
|3   |ice baby ice|
|4   |ice ice ice baby baby ice ice baby|

### Result:

|(Phrase Id, Content Id) | Result (Word Positions in Content)|
|------------------------|-------------------------|
|(4, 2)                  | [10]                     |
|(5, 4)                  | [1, 5]                 |
|(2, 1)                  | [7]                     |
|(3, 1)                  | [13]                     |
|(1, 2)                  | [20]                     |

The code is available in both python and scala in the respective folders.

### Note:
The work is still heavily under developement. The code is not yet modular. If you want to use it right now, you might have to fiddle around the code.

TODO:
* Make Modular
* Write comments
* Remove the actual phrase from key
