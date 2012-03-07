#!/usr/bin/env python

import sys


PARTS = [
    ("wimpy_name_one", "Kaffee"),
    ("manly_name", "Jessup"),
    ("want_noun", "answers"),
    ("want_really_noun", "truth"),
    ("unpleasant_truth_noun",  "wall"),
    ("unpleasant_truth_preposition", "on"),
    ("unpleasant_truth_consequence_verb", "guarded by"),
    ("unpleasant_truth_consequence_object", "men with guns"),
    ("wimpy_name_two", "Lt. Weinberg"),
    ("unfortunately_harmed_noun", "Santiago"),
    ("unfortunate_harmer_collectivenoun", "Marines"),
    ("unfortunate_harm_noun", "death"),
    ("ends_justifying_means_result_past", "saved lives"),
    ("ends_justifying_means_result_present", "saves lives"),
    ("manly_word_one_noun", "honor"),
    ("manly_word_two_noun", "code"),
    ("manly_word_three_noun", "loyalty"),
    ("manly_action_verbphrase", "defending something"),
    ("wimpy_action_verbphrase", "a punchline"),
    ("manly_action_results_noun", "freedom"),
    ("manly_assistance_tool_noun", "a weapon"),
    ("manly_assistance_tool_usage_verb", "pick up"),
    ("manly_assistance_verb", "stand a post"),
    ("messy_action_verb", "order"),
    ("messy_action_object", "the code red"),
]


SPEECH = """
%(manly_name)s: You want %(want_noun)s?
%(wimpy_name_one)s: I think I'm entitled to them.
%(manly_name)s: You want %(want_noun)s?
%(wimpy_name_one)s: I want the %(want_really_noun)s!
%(manly_name)s: You can't handle the %(want_really_noun)s! Son, we live in a world that has %(unpleasant_truth_noun)ss. And those %(unpleasant_truth_noun)ss have to be %(unpleasant_truth_consequence_verb)s %(unpleasant_truth_consequence_object)s. Who's gonna do it? You? You, %(wimpy_name_two)s? I have a greater responsibility than you can possibly fathom. You weep for %(unfortunately_harmed_noun)s and you curse the %(unfortunate_harmer_collectivenoun)s. You have that luxury. You have the luxury of not knowing what I know: that %(unfortunately_harmed_noun)s's %(unfortunate_harm_noun)s, while tragic, probably %(ends_justifying_means_result_past)s. And my existence, while grotesque and incomprehensible to you, %(ends_justifying_means_result_present)s...You don't want the %(want_really_noun)s. Because deep down, in places you don't talk about at parties, you want me %(unpleasant_truth_preposition)s that %(unpleasant_truth_noun)s. You need me %(unpleasant_truth_preposition)s that %(unpleasant_truth_noun)s.
We use words like %(manly_word_one_noun)s, %(manly_word_two_noun)s, %(manly_word_three_noun)s...we use these words as the backbone to a life spent %(manly_action_verbphrase)s. You use 'em as %(wimpy_action_verbphrase)s. I have neither the time nor the inclination to explain myself to a man who rises and sleeps under the blanket of the very %(manly_action_results_noun)s I provide, then questions the manner in which I provide it! I'd rather you just said thank you and went on your way. Otherwise, I suggest you %(manly_assistance_tool_usage_verb)s %(manly_assistance_tool_noun)s and %(manly_assistance_verb)s. Either way, I don't give a damn what you think you're entitled to!
%(wimpy_name_one)s: Did you %(messy_action_verb)s %(messy_action_object)s?
%(manly_name)s: (quietly) I did the job you sent me to do.
%(wimpy_name_one)s: Did you %(messy_action_verb)s %(messy_action_object)s?
%(manly_name)s: You're goddamn right I did!!
"""

PARTS_OF_SPEECH = dict(PARTS)
ORDER_OF_SPEECH = [part for part, default in PARTS]
updated_speech = dict(PARTS_OF_SPEECH)

while True:
    sys.stdout.write("%s\n" % (SPEECH % updated_speech))
    indexes = dict(enumerate(ORDER_OF_SPEECH))
    for index, key in indexes.iteritems():
        print "%0.2i: %40s: %s" % (index, key, updated_speech[key])
    sys.stdout.write("---\nEnter number then new value, or blank to reset: ")
    updates = sys.stdin.readline().split()
    update_key = int(updates[0])
    update_value = " ".join(updates[1:])
    if not update_value:
        update_value = PARTS_OF_SPEECH[indexes[update_key]]
    updated_speech[indexes[update_key]] = update_value

