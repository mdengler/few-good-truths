#!/usr/bin/env python
"""

It's a common annoyance; you're in a meeting, someone says "You want
that feature?!", and some smart aleck has to follow it with "You can't
HANDLE that feature!".  Now you can be that smart aleck, but dorkier,
and with more parts of speech than you ever imagined.

This was a bit of fun to start with, but it's really cumbersome to
use.  But for those office polemics where you for some reason must be
the type of person to like this, it's useful.

"""

import os
import sys


PARTS = {
   "cliche": [
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
      ("manly_assistance_tool_usage_verb", "pick up"),
      ("manly_assistance_tool_noun", "a weapon"),
      ("manly_assistance_verb", "stand a post"),
      ("messy_action_verb", "order"),
      ("messy_action_object", "the code red"),
      ],

   "rmsvssteve": [
      ('wimpy_name_one', 'Richard'),
      ('manly_name', 'Steve'),
      ('want_noun', 'answers'),
      ('want_really_noun', 'freedom'),
      ('unpleasant_truth_noun', 'user'),
      ('unpleasant_truth_preposition', 'coddling'),
      ('unpleasant_truth_consequence_verb', 'coddled with'),
      ('unpleasant_truth_consequence_object', 'shiny UIs and fart apps'),
      ('wimpy_name_two', 'Linus'),
      ('unfortunately_harmed_noun', 'BSD-licensed code'),
      ('unfortunate_harmer_collectivenoun', 'proprietary hardware vendors'),
      ('unfortunate_harm_noun', 'proliferation'),
      ('ends_justifying_means_result_past', 'harmed Windows adoption'),
      ('ends_justifying_means_result_present', 'increases POSIX installs'),
      ('manly_word_one_noun', 'design'),
      ('manly_word_two_noun', 'beauty'),
      ('manly_word_three_noun', 'gradient fill'),
      ('manly_action_verbphrase', 'selling to users who don\'t understand mice with more than one button'),
      ('wimpy_action_verbphrase', 'anti-vi joke'),
      ('manly_action_results_noun', 'userbase'),
      ('manly_assistance_tool_usage_verb', 'take'),
      ('manly_assistance_tool_noun', 'a shower'),
      ('manly_assistance_verb', 'man a Genius bar for an hour'),
      ('messy_action_verb', 'sacrifice'),
      ('messy_action_object', 'Woz and copy PARC\'s ideas'),
      ],

   "javavsc++": [
      ('wimpy_name_one', 'Java'),
      ('manly_name', 'C++'),
      ('want_noun', 'a good programming language'),
      ('want_really_noun', 'best'),
      ('unpleasant_truth_noun', 'user'),
      ('unpleasant_truth_preposition', 'coddling'),
      ('unpleasant_truth_consequence_verb', 'coddled with'),
      ('unpleasant_truth_consequence_object', 'shiny UIs and fart apps'),
      ('wimpy_name_two', 'Linus'),
      ('unfortunately_harmed_noun', 'BSD-licensed code'),
      ('unfortunate_harmer_collectivenoun', 'proprietary hardware vendors'),
      ('unfortunate_harm_noun', 'proliferation'),
      ('ends_justifying_means_result_past', 'harmed Windows adoption'),
      ('ends_justifying_means_result_present', 'increases POSIX installs'),
      ('manly_word_one_noun', 'design'),
      ('manly_word_two_noun', 'beauty'),
      ('manly_word_three_noun', 'gradient fill'),
      ('manly_action_verbphrase', 'selling to users who don\'t understand mice with more than one button'),
      ('wimpy_action_verbphrase', 'anti-vi joke'),
      ('manly_action_results_noun', 'userbase'),
      ('manly_assistance_tool_usage_verb', 'take'),
      ('manly_assistance_tool_noun', 'a shower'),
      ('manly_assistance_verb', 'man a Genius bar for an hour'),
      ('messy_action_verb', 'sacrifice'),
      ('messy_action_object', 'Woz and copy PARC\'s ideas'),
      ],
   }

PARTS["custom"] = PARTS["cliche"][:]


SPEECH_TEMPLATE = """
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



if __name__ == "__main__":

   version = PARTS.keys()[0] # probably deterministic, but random's OK too
   parts_of_speech = dict(PARTS[version])
   order_of_speech = [part for part, default in PARTS[version]]

   while True:

      sys.stdout.write(SPEECH_TEMPLATE % (parts_of_speech))
      sys.stdout.write(os.linesep)
      indexes = dict(enumerate(order_of_speech))
      for index, key in indexes.iteritems():
         sys.stdout.write("%0.2i: %40s: %s%s" % (
               index, key, parts_of_speech[key], os.linesep))

         sys.stdout.write(
            """Enter:
   a) number then new value, or blank to reset; or
   b) version, where version is one of %s (for pre-defined versions); or
   3) dump, to print a repr of your dict (not that's not an image macro joke)
   d) eval <the repr>, to load a repr of your dict
   e) quit
"""
            % ", ".join(sorted(PARTS.keys())))

         sys.stdout.write("---> ")

         def my_repr():
            return "{'%s'}" % ", ".join(["'%s': '%s'" % (part, parts_of_speech[part])
                                         for part in order_of_speech])

         updates = sys.stdin.readline().split()
         if len(updates) < 1 or updates[0] == "quit":
            sys.stdout.write(my_repr() + os.linesep)
            sys.exit(0)

         elif updates[0] == "dump":
            # repr manually to do it in order, for sanity / cut & paste ease
            sys.stdout.write(my_repr() + os.linesep + os.linesep)

         elif updates[0] == "eval":
            parts_of_speech = eval(" ".join(updates[1:]))

         elif updates[0] in PARTS:
            version = updates[0]
            print version
            parts_of_speech = dict(PARTS[version])
            order_of_speech = [part for part, default in PARTS[version]]

         elif updates[0][0] in [str(i) for i in range(10)]:
            update_key = int(updates[0])
            update_value = " ".join(updates[1:])
            if not update_value:
               update_value = dict(PARTS[version])[indexes[update_key]]
            parts_of_speech[indexes[update_key]] = update_value

