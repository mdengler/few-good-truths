# few_good_truths

It's a common annoyance: you're in a meeting, someone says "You want
that feature?!", and some smart-aleck has to follow it with "You can't
HANDLE that feature!".  Now you can be that smart-aleck, but dorkier,
and with more parts of speech than you ever imagined.

This was a bit of fun to start with, though it's really cumbersome to
use.  But for those office polemics where you for some reason must be
the type of person to like this, it's useful.

Just some silly jokes.


# Examples

Example:

~~~
$ python2 few_good_truths.py

C++: You want high performance applications?
Python: I think I'm entitled to them.
C++: You want high performance applications?
Python: I want the best programming language!
C++: You can't handle the best programming language! Son, we live in a world that has memory locations. And those memory locations have to be addressed via pointers. Who's gonna do it? You? You, C#? I have a greater responsibility than you can possibly fathom. You weep for automatic memory management and you curse the trait system. You have that luxury. You have the luxury of not knowing what I know: that automatic memory management's elision, while tragic, probably increased performance. And my existence, while grotesque and incomprehensible to you, increases performance...You don't want the best programming language. Because deep down, in places you don't talk about at parties, you want me pointing to that memory location. You need me pointing to that memory location.
We use words like reference, smart pointer, trampoline...we use these words as the backbone to a life spent improving performance. You use 'em as punchline. I have neither the time nor the inclination to explain myself to a man who rises and sleeps under the blanket of the very performance I provide, then questions the manner in which I provide it! I'd rather you just said thank you and went on your way. Otherwise, I suggest you read the dragon book and write a compiler. Either way, I don't give a damn what you think you're entitled to!
Python: Did you sacrifice productivity for determinism?
C++: (quietly) I did the job you sent me to do.
Python: Did you sacrifice productivity for determinism?
C++: You're goddamn right I did!!

00:                           wimpy_name_one: Python
01:                               manly_name: C++
02:                                want_noun: high performance applications
03:                         want_really_noun: best programming language
04:                    unpleasant_truth_noun: memory location
05:             unpleasant_truth_preposition: pointing to
06:        unpleasant_truth_consequence_verb: addressed via
07:      unpleasant_truth_consequence_object: pointers
08:                           wimpy_name_two: C#
09:                unfortunately_harmed_noun: automatic memory management
10:        unfortunate_harmer_collectivenoun: trait system
11:                    unfortunate_harm_noun: elision
12:        ends_justifying_means_result_past: increased performance
13:     ends_justifying_means_result_present: increases performance
14:                      manly_word_one_noun: reference
15:                      manly_word_two_noun: smart pointer
16:                    manly_word_three_noun: trampoline
17:                  manly_action_verbphrase: improving performance
18:                  wimpy_action_verbphrase: punchline
19:                manly_action_results_noun: performance
20:         manly_assistance_tool_usage_verb: read
21:               manly_assistance_tool_noun: the dragon book
22:                    manly_assistance_verb: write a compiler
23:                        messy_action_verb: sacrifice
24:                      messy_action_object: productivity for determinism
Enter:
   a) number then new value, or blank to reset; or
   b) version, where version is one of cliche, custom, javavsc++, pythonvsc++, rmsvssteve (for pre-defined versions); or
   3) dump, to print a repr of your dict (not that's not an image macro joke)
   d) eval <the repr>, to load a repr of your dict
   e) quit
---> {'wimpy_name_one': 'Python', 'manly_name': 'C++', 'want_noun': 'high performance applications', 'want_really_noun': 'best programming language', 'unpleasant_truth_noun': 'memory location', 'unpleasant_truth_preposition': 'pointing to', 'unpleasant_truth_consequence_verb': 'addressed via', 'unpleasant_truth_consequence_object': 'pointers', 'wimpy_name_two': 'C#', 'unfortunately_harmed_noun': 'automatic memory management', 'unfortunate_harmer_collectivenoun': 'trait system', 'unfortunate_harm_noun': 'elision', 'ends_justifying_means_result_past': 'increased performance', 'ends_justifying_means_result_present': 'increases performance', 'manly_word_one_noun': 'reference', 'manly_word_two_noun': 'smart pointer', 'manly_word_three_noun': 'trampoline', 'manly_action_verbphrase': 'improving performance', 'wimpy_action_verbphrase': 'punchline', 'manly_action_results_noun': 'performance', 'manly_assistance_tool_usage_verb': 'read', 'manly_assistance_tool_noun': 'the dragon book', 'manly_assistance_verb': 'write a compiler', 'messy_action_verb': 'sacrifice', 'messy_action_object': 'productivity for determinism'}

~~~


## Interactive usage

To craft your cliché interactively, enter `$NUMBER replacement string <RETURN>`, like `21 the Dragon book` below:

~~~

[...]
I suggest you read the dragon book and
[...]

    18:                  wimpy_action_verbphrase: punchline
    19:                manly_action_results_noun: performance
    20:         manly_assistance_tool_usage_verb: read
    21:               manly_assistance_tool_noun: the dragon book
    22:                    manly_assistance_verb: write a compiler
    23:                        messy_action_verb: sacrifice
    24:                      messy_action_object: productivity for determinism
    Enter:
       a) number then new value, or blank to reset; or
       b) version, where version is one of cliche, custom, javavsc++, rmsvssteve (for pre-defined versions); or
       3) dump, to print a repr of your dict (not that's not an image macro joke)
       d) eval <the repr>, to load a repr of your dict
       e) quit
    ---> 21 the Dragon book

[...]
I suggest you read the Dragon book and
[...]
~~~


# Conclusion

Try `python2 few_good_truths.py rmsvssteve` to really geek out.  Send in your own `.pickle` files for bonus points.

