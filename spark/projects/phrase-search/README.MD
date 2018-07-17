Say, you have a huge list of phrases and you want to search these phrases in a huge dataset.

Phrases:
------------------
id  | phrase
------------------
1    | pot boiler
2    | hot cake
3    | cold turkey
4    | to be or not to be


Content:

|id  | phrase     |
|----|-------------------------------------------------------------------------------------------------------------------
|1   |Earlier the work he did was a hot cake but once he quit cold turkey, he never received a call from the publishers. |
|2L  |The question for him was to be or not to be on look out for pot boiler.|

Result:
--------------------------------------------------
(Phrase Id, Content Id) | Result (Positions in Content)
--------------------------------------------------
(3, 1)                  | [57]
(2, 1)                  | [31]
(4, 2)                  | [27]
(1, 2)                  | [61]

